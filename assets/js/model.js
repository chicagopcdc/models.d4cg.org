let rawSchemaFiles = null;
const rawViewCache = {};


/* =========================================================
   Loading
========================================================= */

function withLoading(callback) {
  const loader = document.getElementById("raw-loading");
  const rawRenderer = document.getElementById("raw-schema-renderer");
  const showRawLoader = isRawMode();
  const start = performance.now();

  if (showRawLoader && loader) {
    loader.style.display = "flex";

    if (rawRenderer) {
      rawRenderer.style.display = "none";
    }
  }

  requestAnimationFrame(function() {
    setTimeout(function() {
      callback();

      const elapsed = performance.now() - start;
      const remaining = Math.max(0, 250 - elapsed);

      setTimeout(function() {
        if (showRawLoader && loader) {
          loader.style.display = "none";
        }

        if (showRawLoader && rawRenderer) {
          rawRenderer.style.display = "";
        }
      }, remaining);
    }, 0);
  });
}

function updateSlotIndicators() {
  const view = getSelectedView();

  document.querySelectorAll(".slot-action-icon").forEach(function(button) {
    const required = button.dataset.required === "true";
    const priorities = (button.dataset.prioritySubsets || "").split(/\s+/).filter(Boolean);
    const priority = !required && view !== "base" && priorities.includes(view);

    button.classList.toggle("is-required", required);
    button.classList.toggle("is-priority", priority);
    button.classList.toggle("is-optional", !required && !priority);
  });

  document.querySelectorAll(".priority-legend-item").forEach(function(item) {
    item.style.display = view === "base" ? "none" : "inline-flex";
  });
}

/* =========================================================
   Current state
========================================================= */

function getSelectedView() {
  const selector = document.getElementById("view-selector");
  return selector ? selector.value : "base";
}


function isRawMode() {
  const checkbox = document.getElementById("view-mode-checkbox");
  return checkbox ? checkbox.checked : false;
}


/* =========================================================
   View switching
========================================================= */

function switchView(view) {
  withLoading(function() {
    applyViewFilter(view);

    if (isRawMode()) {
      updateRawSchema();
    }
  });
}


function switchModelMode(isRaw) {
  const slotLegend = document.querySelector(".slot-icon-legend");

  if (slotLegend) {
    slotLegend.style.display = isRaw ? "none" : "";
  }

  withLoading(function() {
    document.getElementById("docs-model-view").style.display =
      isRaw ? "none" : "block";

    document.getElementById("raw-model-view").style.display =
      isRaw ? "block" : "none";

    const toc = document.querySelector(".model-toc");

    if (toc) {
      toc.style.display = isRaw ? "none" : "";
    }

    if (isRaw) {
      updateRawSchema();
    }
  });
}


/* =========================================================
   View membership
========================================================= */

function elementHasView(element, view) {
  if (view === "base") {
    return true;
  }

  const subsets = (element.dataset.subsets || "")
    .split(" ")
    .filter(Boolean);

  return subsets.includes(view);
}


function itemHasView(itemDef, view) {
  if (view === "base") {
    return true;
  }

  if (!itemDef || typeof itemDef !== "object") {
    return false;
  }

  return (itemDef.in_subset || []).includes(view);
}


/* =========================================================
   View matrix
========================================================= */

function updateViewMatrix(view) {
  const matrix = document.getElementById("view-matrix-wrap");

  if (!matrix) {
    return;
  }

  matrix.querySelectorAll("[data-view-col]").forEach(function(cell) {
    cell.style.display = "";
    cell.classList.remove("active-view-col");
  });

  if (view === "base") {
    return;
  }

  const activeCells = matrix.querySelectorAll(
    '[data-view-col="' + CSS.escape(view) + '"]'
  );

  activeCells.forEach(function(cell) {
    cell.classList.add("active-view-col");
  });

  matrix.querySelectorAll("tr").forEach(function(row) {
    const activeCell = row.querySelector(
      '[data-view-col="' + CSS.escape(view) + '"]'
    );

    if (!activeCell) {
      return;
    }

    const firstViewCell = Array.from(row.children).find(function(cell) {
      return cell.hasAttribute("data-view-col");
    });

    if (firstViewCell && activeCell !== firstViewCell) {
      row.insertBefore(activeCell, firstViewCell);
    }
  });
}


/* =========================================================
   Clipped cells
========================================================= */

function updateClippedCells() {
  document.querySelectorAll(".cell-details").forEach(function(details) {
    const span = details.querySelector("summary span");

    if (!span) {
      return;
    }

    details.classList.toggle(
      "is-clipped",
      span.scrollWidth > span.clientWidth
    );
  });
}


/* =========================================================
   Mermaid
========================================================= */

function renderMermaidDiagrams() {
  if (!window.mermaid) {
    return;
  }

  document.querySelectorAll(".class-diagram-renderer").forEach(function(renderer) {
    renderer.removeAttribute("data-processed");
  });

  mermaid.run({
    querySelector: ".class-diagram-renderer"
  });
}


/* =========================================================
   Apply rendered model view
========================================================= */

function applyViewFilter(view) {
  const metadata = JSON.parse(
    document.getElementById("view-metadata-payload").textContent
  );

  const current = metadata[view] || metadata["base"];

  document.getElementById("view-description").textContent =
    current.description || "";

  document.querySelectorAll("[data-subsets]").forEach(function(element) {
    if (element.closest("#view-matrix-wrap")) {
      return;
    }

    element.style.display =
      elementHasView(element, view) ? "" : "none";
  });

  document.querySelectorAll(".model-toc-domain").forEach(function(domainLink) {
    let hasVisibleClass = false;
    let next = domainLink.nextElementSibling;

    while (next && next.classList.contains("model-toc-class")) {
      if (next.style.display !== "none") {
        hasVisibleClass = true;
        break;
      }

      next = next.nextElementSibling;
    }

    domainLink.style.display =
      hasVisibleClass ? "" : "none";
  });

  document.querySelectorAll(".domain-section").forEach(function(domain) {
    const visibleClasses = Array.from(
      domain.querySelectorAll(".class-section")
    ).filter(function(section) {
      return section.style.display !== "none";
    });

    domain.style.display =
      visibleClasses.length ? "" : "none";
  });

  document.querySelectorAll(".diagram-details").forEach(function(details) {
    const diagrams = JSON.parse(
      details.dataset.diagrams || "{}"
    );

    const diagramText =
      diagrams[view] || "";

    const renderer = details.querySelector(
      ".class-diagram-renderer"
    );

    if (!diagramText || !renderer) {
      details.style.display = "none";
      return;
    }

    details.style.display = "";
    renderer.textContent = diagramText;
  });

  updateViewMatrix(view);
  updateModelTocVisibility(view);
  updateModelTocPosition();
  renderMermaidDiagrams();
  updateClippedCells();
  updateSlotIndicators();
}


window.addEventListener(
  "resize",
  updateModelTocPosition
);


/* =========================================================
   HTML escaping
========================================================= */

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}


/* =========================================================
   General object helpers
========================================================= */

function deepClone(value) {
  return JSON.parse(
    JSON.stringify(value)
  );
}


function cleanRawViewValue(value) {
  if (Array.isArray(value)) {
    return value.map(function(item) {
      return cleanRawViewValue(item);
    });
  }

  if (
    value !== null &&
    typeof value === "object"
  ) {
    const cleaned = {};

    Object.keys(value).forEach(function(key) {
      if (
        key === "in_subset" ||
        key === "slot_usage"
      ) {
        return;
      }

      cleaned[key] =
        cleanRawViewValue(value[key]);
    });

    return cleaned;
  }

  return value;
}


/* =========================================================
   Raw schema source loading
========================================================= */

function loadRawSchemaFiles() {
  if (rawSchemaFiles !== null) {
    return rawSchemaFiles;
  }

  const payload = document.getElementById(
    "raw-schema-payload"
  );

  if (!payload) {
    rawSchemaFiles = {};
    return rawSchemaFiles;
  }

  try {
    rawSchemaFiles =
      JSON.parse(payload.textContent);
  } catch (error) {
    console.error(
      "Unable to parse raw schema payload:",
      error
    );

    rawSchemaFiles = {};
  }

  return rawSchemaFiles;
}


/* =========================================================
   Raw view subset filtering
========================================================= */

function getRawViewSlotNames(schemaSource, view) {
  const keptSlotNames = new Set();
  const classes = schemaSource.classes || {};

  Object.values(classes).forEach(function(classDef) {
    if (view !== "base" && !itemHasView(classDef, view)) {
      return;
    }

    if (view === "base") {
      (classDef.slots || []).forEach(function(slotName) {
        keptSlotNames.add(slotName);
      });

      return;
    }

    const slotUsage = classDef.slot_usage || {};

    Object.entries(slotUsage).forEach(function(entry) {
      const slotName = entry[0];
      const usageDef = entry[1];

      if (itemHasView(usageDef, view)) {
        keptSlotNames.add(slotName);
      }
    });
  });

  return keptSlotNames;
}


function getRawViewEnumNames(schemaSource, slotsSource, enumsSource, view) {
  const enumNames = new Set();
  const keptSlotNames = getRawViewSlotNames(schemaSource, view);

  keptSlotNames.forEach(function(slotName) {
    const slotDef = (slotsSource.slots || {})[slotName];

    if (!slotDef) {
      return;
    }

    const range = slotDef.range;

    if (range && (enumsSource.enums || {})[range]) {
      enumNames.add(range);
    }
  });

  return enumNames;
}


function filterRawSchemaFile(schemaSource, view) {
  if (view === "base") {
    return deepClone(schemaSource);
  }

  const filtered = deepClone(schemaSource);

  filtered.classes = {};

  const classes = schemaSource.classes || {};

  Object.entries(classes).forEach(function(entry) {
    const className = entry[0];
    const classDef = entry[1];

    if (!itemHasView(classDef, view)) {
      return;
    }

    const slotUsage = classDef.slot_usage || {};

    const keptSlots = (classDef.slots || []).filter(function(slotName) {
      const usageDef = slotUsage[slotName] || {};
      return itemHasView(usageDef, view);
    });

    if (!keptSlots.length) {
      return;
    }

    const newClass = cleanRawViewValue(classDef);

    newClass.slots = keptSlots;
    filtered.classes[className] = newClass;
  });

  if (
    schemaSource.subsets &&
    schemaSource.subsets[view]
  ) {
    filtered.subsets = {
      [view]: cleanRawViewValue(
        schemaSource.subsets[view]
      )
    };
  }

  return cleanRawViewValue(filtered);
}


function filterRawSlotsFile(schemaSource, slotsSource, view) {
  if (view === "base") {
    return deepClone(slotsSource);
  }

  const filtered = deepClone(slotsSource);

  filtered.slots = {};

  const keptSlotNames = getRawViewSlotNames(schemaSource, view);

  keptSlotNames.forEach(function(slotName) {
    const slotDef = (slotsSource.slots || {})[slotName];

    if (!slotDef) {
      return;
    }

    filtered.slots[slotName] =
      cleanRawViewValue(slotDef);
  });

  return cleanRawViewValue(filtered);
}


function filterRawEnumsFile(schemaSource, slotsSource, enumsSource, view) {
  if (view === "base") {
    return deepClone(enumsSource);
  }

  const filtered = deepClone(enumsSource);

  filtered.enums = {};

  const enumNames = getRawViewEnumNames(
    schemaSource,
    slotsSource,
    enumsSource,
    view
  );

  enumNames.forEach(function(enumName) {
    const enumDef = (enumsSource.enums || {})[enumName];

    if (!enumDef) {
      return;
    }

    const newEnum = cleanRawViewValue(enumDef);
    const permissibleValues = enumDef.permissible_values || {};
    const newPermissibleValues = {};

    Object.entries(permissibleValues).forEach(function(entry) {
      const pvName = entry[0];
      const pvDef = entry[1];

      if (!itemHasView(pvDef, view)) {
        return;
      }

      newPermissibleValues[pvName] =
        cleanRawViewValue(pvDef);
    });

    if (!Object.keys(newPermissibleValues).length) {
      return;
    }

    newEnum.permissible_values =
      newPermissibleValues;

    filtered.enums[enumName] =
      newEnum;
  });

  return cleanRawViewValue(filtered);
}


function getRawFileForView(filename, view) {
  const cacheKey = view + "::" + filename;

  if (
    Object.prototype.hasOwnProperty.call(
      rawViewCache,
      cacheKey
    )
  ) {
    return rawViewCache[cacheKey];
  }

  const files = loadRawSchemaFiles();

  const schemaSource = files["schema.yaml"] || {};
  const slotsSource = files["slots.yaml"] || {};
  const enumsSource = files["enums.yaml"] || {};

  let result = {};

  if (filename === "schema.yaml") {
    result = filterRawSchemaFile(schemaSource, view);
  }

  else if (filename === "slots.yaml") {
    result = filterRawSlotsFile(schemaSource, slotsSource, view);
  }

  else if (filename === "enums.yaml") {
    result = filterRawEnumsFile(schemaSource, slotsSource, enumsSource, view);
  }

  rawViewCache[cacheKey] = result;

  return result;
}


/* =========================================================
   Copy helpers
========================================================= */

function getCopyDataType(slotDef, enumsSource) {
  const slotRange = slotDef.range || "";

  if (
    slotRange &&
    (enumsSource.enums || {})[slotRange]
  ) {
    return "enum";
  }

  return slotRange;
}


function slotIsInView(classDef, slotName, view) {
  if (view === "base") {
    return true;
  }

  const usageDef =
    (classDef.slot_usage || {})[slotName] || {};

  return itemHasView(usageDef, view);
}


function pvIsInView(pvDef, view) {
  if (view === "base") {
    return true;
  }

  return itemHasView(pvDef, view);
}


function cleanTsvCell(value) {
  if (value === null || value === undefined) {
    return "";
  }

  return String(value)
    .replaceAll("\t", " ")
    .replace(/\r?\n/g, " ");
}


function rowsToTsv(rows) {
  return rows.map(function(row) {
    return row.map(function(cell) {
      return cleanTsvCell(cell);
    }).join("\t");
  }).join("\n");
}


function buildSlotCopyRows(className, slotName, view) {
  const files = loadRawSchemaFiles();
  const schemaSource = files["schema.yaml"] || {};
  const slotsSource = files["slots.yaml"] || {};
  const enumsSource = files["enums.yaml"] || {};
  const classDef = (schemaSource.classes || {})[className];

  if (!classDef) {
    return [];
  }

  if (view !== "base" && !itemHasView(classDef, view)) {
    return [];
  }

  if (!slotIsInView(classDef, slotName, view)) {
    return [];
  }

  const slotDef = (slotsSource.slots || {})[slotName];

  if (!slotDef) {
    return [];
  }

  const slotRange = slotDef.range || "";
  const dataType = getCopyDataType(slotDef, enumsSource);
  const tier = getCopyTier(classDef, slotName, view);
  const slotMeaning = slotDef.slot_uri || "";

  const rows = [
    ["slot", slotName, dataType, tier, "", slotMeaning, "", ""]
  ];

  const enumDef = (enumsSource.enums || {})[slotRange];

  if (!enumDef) {
    return rows;
  }

  Object.entries(enumDef.permissible_values || {}).forEach(function(entry) {
    const pvName = entry[0];
    const pvDef = entry[1];

    if (!pvIsInView(pvDef, view)) {
      return;
    }

    rows.push(["pv", "", "", "", pvName, pvDef.meaning || "", "", ""]);
  });

  return rows;
}


function buildClassCopyRows(className, view) {
  const files = loadRawSchemaFiles();
  const schemaSource = files["schema.yaml"] || {};
  const classDef = (schemaSource.classes || {})[className];

  if (!classDef) {
    return [];
  }

  if (view !== "base" && !itemHasView(classDef, view)) {
    return [];
  }

  let cardinality = ((classDef.annotations || {}).cardinality || "");

  if (cardinality && typeof cardinality === "object" && "value" in cardinality) {
    cardinality = cardinality.value;
  }

 const rows = [
    ["class", className, "class", cardinality, "", "", "", ""]
  ];

  (classDef.slots || []).forEach(function(slotName) {
    if (!slotIsInView(classDef, slotName, view)) {
      return;
    }

    const slotRows = buildSlotCopyRows(className, slotName, view);

    slotRows.forEach(function(row) {
      rows.push(row);
    });
  });

  return rows;
}

function getCopyTier(classDef, slotName, view) {
  const usageDef = (classDef.slot_usage || {})[slotName] || {};

  if (usageDef.required === true) {
    return "required";
  }

  let priority = ((usageDef.annotations || {}).priority || []);

  if (priority && typeof priority === "object" && !Array.isArray(priority) && "value" in priority) {
    priority = priority.value;
  }

  if (!Array.isArray(priority)) {
    priority = priority ? [priority] : [];
  }

  if (view !== "base" && priority.includes(view)) {
    return "priority";
  }

  return "optional";
}

function fallbackCopyText(text) {
  const textarea = document.createElement("textarea");

  textarea.value = text;
  textarea.setAttribute("readonly", "");

  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  textarea.style.pointerEvents = "none";

  document.body.appendChild(textarea);

  textarea.select();

  const successful =
    document.execCommand("copy");

  document.body.removeChild(textarea);

  if (!successful) {
    throw new Error("Fallback copy command failed.");
  }
}


function showCopySuccess(button) {
  const originalTitle =
    button.dataset.originalTitle ||
    button.getAttribute("title") ||
    "";

  button.dataset.originalTitle =
    originalTitle;

  button.classList.add("copy-success");
  button.setAttribute("title", "Copied");

  setTimeout(function() {
    button.classList.remove("copy-success");
    button.setAttribute(
      "title",
      originalTitle
    );
  }, 1000);
}


async function copyTextToClipboard(text, button) {
  if (!text) {
    return;
  }

  try {
    await navigator.clipboard.writeText(text);
    showCopySuccess(button);
  } catch (error) {
    try {
      fallbackCopyText(text);
      showCopySuccess(button);
    } catch (fallbackError) {
      console.error(
        "Unable to copy to clipboard:",
        error,
        fallbackError
      );
    }
  }
}


function copyClass(button) {
  const className =
    button.dataset.className;

  const view =
    getSelectedView();

  const rows =
    buildClassCopyRows(
      className,
      view
    );

  copyTextToClipboard(
    rowsToTsv(rows),
    button
  );
}


function copySlot(button) {
  const className =
    button.dataset.className;

  const slotName =
    button.dataset.slotName;

  const view =
    getSelectedView();

  const rows =
    buildSlotCopyRows(
      className,
      slotName,
      view
    );

  copyTextToClipboard(
    rowsToTsv(rows),
    button
  );
}


function copyPv(button) {
  const pvName = button.dataset.pvName || "";
  const pvMeaning = button.dataset.pvMeaning || "";
  const rows = [
    ["pv", "", "", "", pvName, pvMeaning, "", ""]
  ];

  copyTextToClipboard(rowsToTsv(rows), button);
}


/* =========================================================
   YAML rendering
========================================================= */

function yamlScalar(value) {
  if (value === null) {
    return "null";
  }

  if (typeof value === "string") {
    return value;
  }

  if (typeof value === "boolean") {
    return value ? "true" : "false";
  }

  return String(value);
}


function renderYamlValue(
  value,
  label = null,
  listItem = false
) {
  const listPrefix =
    listItem ? "- " : "";

  if (
    value !== null &&
    typeof value === "object" &&
    !Array.isArray(value)
  ) {
    const keys =
      Object.keys(value);

    if (
      label === null &&
      !listItem
    ) {
      return keys.map(function(key) {
        return renderYamlValue(
          value[key],
          key,
          false
        );
      }).join("");
    }

    const summary =
      listPrefix +
      (
        label !== null
          ? '<span class="yaml-key">' +
            escapeHtml(label) +
            '</span>:'
          : ""
      );

    let html =
      '<details open class="yaml-node">' +
      '<summary>' +
      summary +
      '<span class="yaml-closed"> ...</span>' +
      '<span class="yaml-open"></span>' +
      '</summary>';

    html +=
      '<div class="yaml-children">';

    keys.forEach(function(key) {
      html += renderYamlValue(
        value[key],
        key,
        false
      );
    });

    html += '</div>';
    html += '</details>';

    return html;
  }

  if (Array.isArray(value)) {
    const isPrimitiveArray =
      value.every(function(item) {
        return (
          item === null ||
          typeof item !== "object"
        );
      });

    const forceExpanded =
      label === "slots";

    if (
      isPrimitiveArray &&
      !forceExpanded
    ) {
      const items =
        value.map(function(item) {
          return (
            '<span class="yaml-value">' +
            escapeHtml(
              yamlScalar(item)
            ) +
            '</span>'
          );
        }).join(", ");

      const keyText =
        label !== null
          ? '<span class="yaml-key">' +
            escapeHtml(label) +
            '</span>: '
          : "";

      return (
        '<div class="yaml-line">' +
        listPrefix +
        keyText +
        '[' +
        items +
        ']' +
        '</div>'
      );
    }

    const summary =
      listPrefix +
      (
        label !== null
          ? '<span class="yaml-key">' +
            escapeHtml(label) +
            '</span>:'
          : ""
      );

    let html =
      '<details open class="yaml-node">' +
      '<summary>' +
      summary +
      '<span class="yaml-closed"> ...</span>' +
      '<span class="yaml-open"></span>' +
      '</summary>';

    html +=
      '<div class="yaml-children">';

    value.forEach(function(item) {
      html += renderYamlValue(
        item,
        null,
        true
      );
    });

    html += '</div>';
    html += '</details>';

    return html;
  }

  const primitive =
    escapeHtml(
      yamlScalar(value)
    );

  if (label !== null) {
    return (
      '<div class="yaml-line">' +
      listPrefix +
      '<span class="yaml-key">' +
      escapeHtml(label) +
      '</span>: ' +
      '<span class="yaml-value">' +
      primitive +
      '</span>' +
      '</div>'
    );
  }

  return (
    '<div class="yaml-line">' +
    listPrefix +
    '<span class="yaml-value">' +
    primitive +
    '</span>' +
    '</div>'
  );
}


/* =========================================================
   Raw file selection / rendering
========================================================= */

function getSelectedRawFile() {
  const activeButton =
    document.querySelector(
      ".raw-file-button.active"
    );

  if (activeButton) {
    return activeButton.dataset.rawFile;
  }

  return "schema.yaml";
}


function updateRawSchema() {
  const rawRenderer =
    document.getElementById(
      "raw-schema-renderer"
    );

  if (!rawRenderer) {
    return;
  }

  const view =
    getSelectedView();

  let filename =
    getSelectedRawFile();

  const allowedFiles = [
    "schema.yaml",
    "slots.yaml",
    "enums.yaml"
  ];

  if (!allowedFiles.includes(filename)) {
    filename =
      "schema.yaml";
  }

  const selectedFile =
    getRawFileForView(
      filename,
      view
    );

  rawRenderer.innerHTML =
    renderYamlValue(
      selectedFile
    );

  document
    .querySelectorAll(
      ".raw-file-button"
    )
    .forEach(function(button) {
      button.classList.toggle(
        "active",
        button.dataset.rawFile === filename
      );
    });
}


function switchRawFile(filename) {
  document
    .querySelectorAll(
      ".raw-file-button"
    )
    .forEach(function(button) {
      button.classList.toggle(
        "active",
        button.dataset.rawFile === filename
      );
    });

  withLoading(function() {
    updateRawSchema();
  });
}


/* =========================================================
   Documentation-page TOC
========================================================= */

function buildDocsToc() {
  const toc =
    document.getElementById(
      "docs-toc"
    );

  if (!toc) {
    return;
  }

  const headings =
    document.querySelectorAll(
      ".main-content h1[id], " +
      ".main-content h2[id]"
    );

  toc.innerHTML = "";

  headings.forEach(function(heading) {
    const link =
      document.createElement("a");

    link.href =
      "#" + heading.id;

    link.textContent =
      heading.textContent.trim();

    link.title =
      link.textContent;

    link.className =
      heading.tagName === "H1"
        ? "model-toc-domain"
        : "model-toc-class";

    toc.appendChild(link);
  });
}


document.addEventListener(
  "DOMContentLoaded",
  buildDocsToc
);


/* =========================================================
   Enum modal
========================================================= */

function openEnumModal(enumId) {
  const modal = document.getElementById(enumId);

  if (!modal) {
    return;
  }

  modal.classList.add("enum-modal-open");

  if (modal.dataset.loaded === "true") {
    return;
  }

  const loader = modal.querySelector(".enum-modal-loading");
  const content = modal.querySelector(".enum-modal-loaded-content");
  const template = modal.querySelector(".enum-modal-template");
  const modalBody = modal.querySelector(".enum-modal-body");
  const pvCount = Number(modal.dataset.pvCount || 0);
  const useLoader = pvCount >= 250;

  function loadEnum() {
    content.style.visibility = "hidden";
    content.style.display = "";

    if (template && !content.hasChildNodes()) {
      content.appendChild(template.content.cloneNode(true));
    }

    const view = getSelectedView();

    content.querySelectorAll("[data-subsets]").forEach(function(element) {
      element.style.display = elementHasView(element, view) ? "" : "none";
    });

    updateClippedCells();

    requestAnimationFrame(function() {
      void content.offsetHeight;

      requestAnimationFrame(function() {
        content.style.visibility = "visible";

        if (modalBody) {
          modalBody.style.minHeight = "0";
        }

        if (loader) {
          loader.style.display = "none";
        }

        modal.dataset.loaded = "true";
      });
    });
  }

  if (useLoader && loader) {
    loader.style.display = "flex";
    content.style.visibility = "hidden";

    requestAnimationFrame(function() {
      requestAnimationFrame(loadEnum);
    });
  } else {
    loadEnum();
  }
}

function closeEnumModal(enumId) {
  document
    .getElementById(enumId)
    .classList.remove(
      "enum-modal-open"
    );
}


document.addEventListener(
  "keydown",
  function(event) {
    if (event.key === "Escape") {
      document
        .querySelectorAll(
          ".enum-modal-open"
        )
        .forEach(function(modal) {
          modal.classList.remove(
            "enum-modal-open"
          );
        });
    }
  }
);


/* =========================================================
   Model TOC visibility
========================================================= */

function updateModelTocVisibility(view) {
  document
    .querySelectorAll(
      ".model-toc-class[data-subsets]"
    )
    .forEach(function(link) {
      link.style.display =
        elementHasView(
          link,
          view
        )
          ? ""
          : "none";
    });
}


/* =========================================================
   Model TOC scroll spy
========================================================= */

function initModelTocScrollSpy() {
  const links =
    Array.from(
      document.querySelectorAll(
        ".model-toc a"
      )
    );

  links.forEach(function(link) {
    link.title = link.textContent.trim();
  });

  const sections =
    links
      .map(function(link) {
        const id =
          link.getAttribute(
            "href"
          );

        return id
          ? document.querySelector(id)
          : null;
      })
      .filter(Boolean);

  function updateActiveTocLink() {
    let active = null;

    sections.forEach(function(section) {
      const rect =
        section.getBoundingClientRect();

      if (
        rect.top <= 120 &&
        rect.bottom > 120 &&
        section.style.display !== "none"
      ) {
        active =
          section.id;
      }
    });

    links.forEach(function(link) {
      link.classList.toggle(
        "active",
        link.getAttribute("href") ===
          "#" + active
      );
    });

    const activeLink =
      links.find(function(link) {
        return link.classList.contains(
          "active"
        );
      });

    if (activeLink) {
      activeLink.scrollIntoView({
        block: "nearest",
        inline: "nearest"
      });
    }
  }

  document.addEventListener(
    "scroll",
    updateActiveTocLink,
    {
      passive: true
    }
  );

  updateActiveTocLink();
}


/* =========================================================
   Model TOC positioning
========================================================= */

function updateModelTocPosition() {
  const toc =
    document.querySelector(
      ".model-toc"
    );

  const main =
    document.querySelector(
      ".main"
    );

  if (
    !toc ||
    !main ||
    isRawMode()
  ) {
    return;
  }

  toc.style.display = "";

  const tocRect =
    toc.getBoundingClientRect();

  const mainRect =
    main.getBoundingClientRect();

  const gap = 24;

  if (
    tocRect.left <
      mainRect.right + gap ||
    tocRect.right >
      window.innerWidth - gap
  ) {
    toc.style.display =
      "none";
  }
}


/* =========================================================
   Initialization
========================================================= */

document.addEventListener(
  "DOMContentLoaded",
  function() {
    applyViewFilter("base");
    initModelTocScrollSpy();
    updateClippedCells();
  }
);


/* =========================================================
   Bundle Export
========================================================= */

let terminologyDescriptions = null;

function loadTerminologyDescriptions() {
  if (terminologyDescriptions) {
    return terminologyDescriptions;
  }

  const payload = document.getElementById("terminology-description-payload");
  terminologyDescriptions = payload ? JSON.parse(payload.textContent) : {};
  return terminologyDescriptions;
}

function normalizeExportCurie(value) {
  if (!value) {
    return "";
  }

  const curie = String(value).trim();

  if (!curie.includes(":")) {
    if (/^C\d+$/i.test(curie)) {
      return "ncit:" + curie.toUpperCase();
    }

    return curie;
  }

  const separator = curie.indexOf(":");
  const prefix = curie.substring(0, separator).trim().toLowerCase();
  const code = curie.substring(separator + 1).trim();

  return prefix + ":" + code;
}

function getExportDescription(meaning) {
  if (!meaning) {
    return "";
  }

  const descriptions = loadTerminologyDescriptions();
  return descriptions[normalizeExportCurie(meaning)] || "";
}

function getExportNotes(itemDef) {
  const comments = itemDef.comments || [];

  if (Array.isArray(comments)) {
    return comments.join("\n");
  }

  return comments ? String(comments) : "";
}

function getClassCardinality(classDef) {
  let cardinality = ((classDef.annotations || {}).cardinality || "");

  if (cardinality && typeof cardinality === "object" && "value" in cardinality) {
    cardinality = cardinality.value;
  }

  return cardinality ? String(cardinality) : "";
}

function getClassDomain(classDef) {
  let domain = ((classDef.annotations || {}).domain || "");

  if (domain && typeof domain === "object" && "value" in domain) {
    domain = domain.value;
  }

  return domain ? String(domain) : "";
}

function classIsInternal(classDef) {
  let domain = ((classDef.annotations || {}).domain || "");

  if (domain && typeof domain === "object" && "value" in domain) {
    domain = domain.value;
  }

  return String(domain).toLowerCase() === "internal";
}

function getBundleClasses(view) {
  const files = loadRawSchemaFiles();
  const schemaSource = files["schema.yaml"] || {};
  const classes = [];

  Object.entries(schemaSource.classes || {}).forEach(function(entry) {
    const className = entry[0];
    const classDef = entry[1];

    if (classIsInternal(classDef)) {
      return;
    }

    if (view !== "base" && !itemHasView(classDef, view)) {
      return;
    }

    const slots = (classDef.slots || []).filter(function(slotName) {
      return slotIsInView(classDef, slotName, view);
    });

    if (slots.length) {
      classes.push({
        name: className,
        definition: classDef,
        slots: slots
      });
    }
  });

  return classes;
}

function buildBundleDictionaryRows(view) {
  const files = loadRawSchemaFiles();
  const schemaSource = files["schema.yaml"] || {};
  const slotsSource = files["slots.yaml"] || {};
  const enumsSource = files["enums.yaml"] || {};
  const viewDef = (schemaSource.subsets || {})[view] || {};

  const rows = [
    ["info", "Title", schemaSource.title || schemaSource.name || "", "", "", "", "", ""],
    ["info", "Subset", viewDef.title || viewDef.name || view, "", "", "", "", ""],
    ["info", "Version", schemaSource.version || "", "", "", "", "", ""],
    ["info", "License", "CC BY-NC 4.0", "", "", "", "", ""],
    ["info", "Export Date", new Date().toISOString().split("T")[0], "", "", "", "", ""],
    [],
    [
      "RowType",
      "Name",
      "Data Type",
      "Cardinality/Tier",
      "Permissible Value",
      "Meaning",
      "Description",
      "Implementation Notes"
    ]
  ];

  const classes = getBundleClasses(view);
  let currentDomain = "";

  classes.forEach(function(classInfo, classIndex) {
    const className = classInfo.name;
    const classDef = classInfo.definition;

    if (classIndex > 0) {
      rows.push([]);
    }

    const domain = getClassDomain(classDef);

    if (domain && domain !== currentDomain) {
      rows.push(["domain", domain, "", "", "", "", "", ""]);
      currentDomain = domain;
    }

    rows.push([
      "class",
      className,
      "class",
      getClassCardinality(classDef),
      "",
      "",
      classDef.description || "",
      getExportNotes(classDef)
    ]);

    classInfo.slots.forEach(function(slotName) {
      const slotDef = (slotsSource.slots || {})[slotName];

      if (!slotDef) {
        return;
      }

      const slotRange = slotDef.range || "";
      const meaning = slotDef.slot_uri || "";

      rows.push([
        "slot",
        slotName,
        getCopyDataType(slotDef, enumsSource),
        getCopyTier(classDef, slotName, view),
        "",
        meaning,
        getExportDescription(meaning),
        getExportNotes(slotDef)
      ]);

      const enumDef = (enumsSource.enums || {})[slotRange];

      if (!enumDef) {
        return;
      }

      Object.entries(enumDef.permissible_values || {}).forEach(function(entry) {
        const pvName = entry[0];
        const pvDef = entry[1];

        if (!pvIsInView(pvDef, view)) {
          return;
        }

        const pvMeaning = pvDef.meaning || "";

        rows.push([
          "pv",
          "",
          "",
          "",
          pvName,
          pvMeaning,
          getExportDescription(pvMeaning),
          getExportNotes(pvDef)
        ]);
      });
    });
  });

  return rows;
}

function escapeTsvValue(value) {
  if (value === null || value === undefined) {
    return "";
  }

  return String(value)
    .replace(/\t/g, " ")
    .replace(/\r?\n/g, " ");
}

function rowsToBundleTsv(rows) {
  return rows.map(function(row) {
    return row.map(escapeTsvValue).join("\t");
  }).join("\n") + "\n";
}

function buildClassTemplateTsv(classInfo) {
  return classInfo.slots.map(escapeTsvValue).join("\t") + "\n";
}

function writeTarString(header, offset, length, value) {
  const bytes = new TextEncoder().encode(String(value));

  for (let index = 0; index < Math.min(bytes.length, length); index += 1) {
    header[offset + index] = bytes[index];
  }
}

function writeTarOctal(header, offset, length, value) {
  const text = Number(value).toString(8).padStart(length - 1, "0") + "\0";
  writeTarString(header, offset, length, text);
}

function createTarHeader(filename, size, modifiedTime) {
  const header = new Uint8Array(512);

  writeTarString(header, 0, 100, filename);
  writeTarOctal(header, 100, 8, 420);
  writeTarOctal(header, 108, 8, 0);
  writeTarOctal(header, 116, 8, 0);
  writeTarOctal(header, 124, 12, size);
  writeTarOctal(header, 136, 12, modifiedTime);

  for (let index = 148; index < 156; index += 1) {
    header[index] = 32;
  }

  writeTarString(header, 156, 1, "0");
  writeTarString(header, 257, 6, "ustar");
  writeTarString(header, 263, 2, "00");
  writeTarString(header, 265, 32, "D4CG");
  writeTarString(header, 297, 32, "D4CG");

  let checksum = 0;

  for (let index = 0; index < header.length; index += 1) {
    checksum += header[index];
  }

  const checksumText = checksum.toString(8).padStart(6, "0") + "\0 ";
  writeTarString(header, 148, 8, checksumText);

  return header;
}

function buildTar(files) {
  const encoder = new TextEncoder();
  const parts = [];
  const baseTime = Math.floor(Date.now() / 1000);
  let totalLength = 1024;

  const tarFiles = files.map(function(file, index) {
    return {
      file: file,
      originalIndex: index
    };
  }).reverse();

  tarFiles.forEach(function(item) {
    const content = encoder.encode(item.file.content);
    const paddingLength = (512 - (content.length % 512)) % 512;
    const modifiedTime = baseTime - item.originalIndex;

    parts.push({
      header: createTarHeader(item.file.name, content.length, modifiedTime),
      content: content,
      padding: new Uint8Array(paddingLength)
    });

    totalLength += 512 + content.length + paddingLength;
  });

  const output = new Uint8Array(totalLength);
  let offset = 0;

  parts.forEach(function(part) {
    output.set(part.header, offset);
    offset += part.header.length;

    output.set(part.content, offset);
    offset += part.content.length;

    output.set(part.padding, offset);
    offset += part.padding.length;
  });

  return output;
}

function safeBundleFilename(value) {
  return String(value)
    .trim()
    .replace(/[^A-Za-z0-9._-]+/g, "_")
    .replace(/^_+|_+$/g, "");
}

function exportContributorBundle(button) {
  const view = getSelectedView();
  const files = loadRawSchemaFiles();
  const schemaSource = files["schema.yaml"] || {};
  const version = schemaSource.version || "";
  const classes = getBundleClasses(view);
  const bundleFiles = [];

  bundleFiles.push({
    name: "00_data_dictionary.tsv",
    content: rowsToBundleTsv(buildBundleDictionaryRows(view))
  });

  classes.forEach(function(classInfo, index) {
    const number = String(index + 1).padStart(2, "0");

    bundleFiles.push({
      name: number + "_" + safeBundleFilename(classInfo.name) + ".tsv",
      content: buildClassTemplateTsv(classInfo)
    });
  });

  const tar = buildTar(bundleFiles);
  const blob = new Blob([tar], {type: "application/x-tar"});
  const modelName = safeBundleFilename(schemaSource.name || schemaSource.title || "d4cg").toLowerCase();
  const versionName = safeBundleFilename(version);
  const viewName = safeBundleFilename(view);
  const filename = [modelName, versionName, viewName, "contributor-bundle"].filter(Boolean).join("-") + ".tar";
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");

  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();

  setTimeout(function() {
    URL.revokeObjectURL(url);
  }, 1000);
}