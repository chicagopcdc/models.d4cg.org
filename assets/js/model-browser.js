function withLoading(callback) {
  const loader = document.getElementById("model-loading");
  const start = performance.now();

  if (loader) {
    loader.style.display = "flex";
  }

  requestAnimationFrame(function() {
    setTimeout(function() {
      callback();

      const elapsed = performance.now() - start;
      const remaining = Math.max(0, 250 - elapsed);

      setTimeout(function() {
        if (loader) {
          loader.style.display = "none";
        }
      }, remaining);
    }, 0);
  });
}

function getSelectedView() {
  const selector = document.getElementById("view-selector");
  return selector ? selector.value : "base";
}

function isRawMode() {
  const checkbox = document.getElementById("view-mode-checkbox");
  return checkbox ? checkbox.checked : false;
}

function switchView(view) {
  withLoading(function() {
    applyViewFilter(view);

    if (isRawMode()) {
      updateRawSchema();
    }
  });
}

function switchModelMode(isRaw) {
  withLoading(function() {
    document.getElementById("docs-model-view").style.display = isRaw ? "none" : "block";
    document.getElementById("raw-model-view").style.display = isRaw ? "block" : "none";

    const toc = document.querySelector(".model-toc");
    if (toc) {
      toc.style.display = isRaw ? "none" : "";
    }

    if (isRaw) {
      updateRawSchema();
    }
  });
}

function elementHasView(element, view) {
  if (view === "base") {
    return true;
  }

  const subsets = (element.dataset.subsets || "").split(" ").filter(Boolean);
  return subsets.includes(view);
}

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

  const activeCells = matrix.querySelectorAll('[data-view-col="' + CSS.escape(view) + '"]');

  activeCells.forEach(function(cell) {
    cell.classList.add("active-view-col");
  });

  matrix.querySelectorAll("tr").forEach(function(row) {
    const activeCell = row.querySelector('[data-view-col="' + CSS.escape(view) + '"]');
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

function updateClippedCells() {
  document.querySelectorAll(".cell-details").forEach(function(details) {
    const span = details.querySelector("summary span");
    if (!span) {
      return;
    }

    details.classList.toggle("is-clipped", span.scrollWidth > span.clientWidth);
  });
}

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

function applyViewFilter(view) {
  const metadata = JSON.parse(document.getElementById("view-metadata-payload").textContent);
  const current = metadata[view] || metadata["base"];

  document.getElementById("view-description").textContent = current.description || "";

  document.querySelectorAll("[data-subsets]").forEach(function(element) {
    if (element.closest("#view-matrix-wrap")) {
      return;
    }
    element.style.display = elementHasView(element, view) ? "" : "none";
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

    domainLink.style.display = hasVisibleClass ? "" : "none";
  });

  document.querySelectorAll(".domain-section").forEach(function(domain) {
    const visibleClasses = Array.from(domain.querySelectorAll(".class-section")).filter(function(section) {
      return section.style.display !== "none";
    });
    domain.style.display = visibleClasses.length ? "" : "none";
  });

  document.querySelectorAll(".diagram-details").forEach(function(details) {
    const diagrams = JSON.parse(details.dataset.diagrams || "{}");
    const diagramText = diagrams[view] || "";
    const renderer = details.querySelector(".class-diagram-renderer");

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
}

window.addEventListener("resize", updateModelTocPosition);

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function renderJsonValue(value, label = null, comma = false) {
  const commaText = comma ? "," : "";

  if (value !== null && typeof value === "object" && !Array.isArray(value)) {
    const keys = Object.keys(value);
    const summary = label ? '<span class="json-key">"' + escapeHtml(label) + '"</span>: ' : "";
    let html = '<details open class="json-node"><summary>' + summary + '<span class="json-closed">{...}</span><span class="json-open">{</span></summary>';
    html += '<div class="json-children">';

    keys.forEach(function(key, i) {
      html += renderJsonValue(value[key], key, i < keys.length - 1);
    });

    html += '</div>';
    html += '<div class="json-end">}' + commaText + '</div>';
    html += '</details>';

    return html;
  }

  if (Array.isArray(value)) {
    const summary = label ? '<span class="json-key">"' + escapeHtml(label) + '"</span>: ' : "";

    const isPrimitiveArray = value.every(function(item) {
        return item === null || typeof item !== "object";
    });

    const forceExpanded =
        label === "slots";

    if (isPrimitiveArray && !forceExpanded) {
        const items = value.map(function(item) {
        return '<span class="json-value">' + escapeHtml(JSON.stringify(item)) + '</span>';
        }).join(", ");

        return '<div class="json-line">' + summary + '[' + items + ']' + commaText + '</div>';
    }

    let html = '<details open class="json-node"><summary>' + summary + '<span class="json-closed">[...]</span><span class="json-open">[</span></summary>';
    html += '<div class="json-children">';

    value.forEach(function(item, i) {
        html += renderJsonValue(item, null, i < value.length - 1);
    });

    html += '</div>';
    html += '<div class="json-end">]' + commaText + '</div>';
    html += '</details>';

    return html;
    }

  const primitive = escapeHtml(JSON.stringify(value));

  if (label) {
    return '<div class="json-line"><span class="json-key">"' + escapeHtml(label) + '"</span>: <span class="json-value">' + primitive + '</span>' + commaText + '</div>';
  }

  return '<div class="json-line"><span class="json-value">' + primitive + '</span>' + commaText + '</div>';
}

function buildDocsToc() {
  const toc = document.getElementById("docs-toc");
  if (!toc) return;

  const headings = document.querySelectorAll(".main-content h1[id], .main-content h2[id]");
  toc.innerHTML = "";

  headings.forEach(function(heading) {
    const link = document.createElement("a");
    link.href = "#" + heading.id;
    link.textContent = heading.textContent.trim();
    link.className = heading.tagName === "H1" ? "model-toc-domain" : "model-toc-class";
    toc.appendChild(link);
  });
}

document.addEventListener("DOMContentLoaded", buildDocsToc);

function updateRawSchema() {
  const rawRenderer = document.getElementById("raw-schema-renderer");
  const payload = document.getElementById("raw-schema-payload");

  if (!rawRenderer || !payload) {
    return;
  }

  const view = getSelectedView();
  const schemas = JSON.parse(payload.textContent);
  const selectedSchema = schemas[view] || schemas["base"];

  rawRenderer.innerHTML = renderJsonValue(selectedSchema);
}

function openEnumModal(enumId) {
  document.getElementById(enumId).classList.add("enum-modal-open");
  updateClippedCells();
}

function closeEnumModal(enumId) {
  document.getElementById(enumId).classList.remove("enum-modal-open");
}

document.addEventListener("keydown", function(event) {
  if (event.key === "Escape") {
    document.querySelectorAll(".enum-modal-open").forEach(function(modal) {
      modal.classList.remove("enum-modal-open");
    });
  }
});

document.addEventListener("DOMContentLoaded", function() {
  applyViewFilter("base");
  initModelTocScrollSpy();
  updateClippedCells();
});

function updateModelTocVisibility(view) {
  document.querySelectorAll(".model-toc-class[data-subsets]").forEach(function(link) {
    link.style.display = elementHasView(link, view) ? "" : "none";
  });
}

function initModelTocScrollSpy() {
  const links = Array.from(document.querySelectorAll(".model-toc a"));
  const sections = links
    .map(function(link) {
      const id = link.getAttribute("href");
      return id ? document.querySelector(id) : null;
    })
    .filter(Boolean);

  function updateActiveTocLink() {
    let active = null;

    sections.forEach(function(section) {
      const rect = section.getBoundingClientRect();
      if (rect.top <= 120 && rect.bottom > 120 && section.style.display !== "none") {
        active = section.id;
      }
    });

    links.forEach(function(link) {
      link.classList.toggle("active", link.getAttribute("href") === "#" + active);
    });

    const activeLink = links.find(function(link) {
      return link.classList.contains("active");
    });

    if (activeLink) {
      activeLink.scrollIntoView({
        block: "nearest",
        inline: "nearest"
      });
    }
  }

  document.addEventListener("scroll", updateActiveTocLink, { passive: true });
  updateActiveTocLink();
}

function updateModelTocPosition() {
  const toc = document.querySelector(".model-toc");
  const main = document.querySelector(".main");

  if (!toc || !main || isRawMode()) {
    return;
  }

  toc.style.display = "";

  const tocRect = toc.getBoundingClientRect();
  const mainRect = main.getBoundingClientRect();
  const gap = 24;

  if (tocRect.left < mainRect.right + gap || tocRect.right > window.innerWidth - gap) {
    toc.style.display = "none";
  }
}