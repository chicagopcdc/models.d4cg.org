import argparse
import copy
import json
from pathlib import Path

import yaml


COMMONS = {
    "pcdc": {
        "folder": "pcdc",
        "title": "Pediatric Oncology",
        "nav_order": 2,
    },
    "predict": {
        "folder": "predict",
        "title": "Monogenic Diabetes",
        "nav_order": 3,
    },
}

# See https://lucide.dev/icons for future options
DOMAIN_ICONS = {
    "demographics": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-icon lucide-user"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>""",
    "testing": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-dna-icon lucide-dna"><path d="m10 16 1.5 1.5"/><path d="m14 8-1.5-1.5"/><path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993"/><path d="m16.5 10.5 1 1"/><path d="m17 6-2.891-2.891"/><path d="M2 15c6.667-6 13.333 0 20-6"/><path d="m20 9 .891.891"/><path d="M3.109 14.109 4 15"/><path d="m6.5 12.5 1 1"/><path d="m7 18 2.891 2.891"/><path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993"/></svg>""",
    "disease_attributes": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-network-icon lucide-network"><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/></svg>""",
    "intervention": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-hospital-icon lucide-hospital"><path d="M12 7v4"/><path d="M14 21v-3a2 2 0 0 0-4 0v3"/><path d="M14 9h-4"/><path d="M18 11h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 21V5a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16"/></svg>""",
    "monitoring": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-stethoscope-icon lucide-stethoscope"><path d="M11 2v2"/><path d="M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/></svg>""",
}

COPY_ICON = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy-icon lucide-copy"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>"""


def load_yaml(path, required=True):
    if path is None or not path.exists():
        if required:
            raise FileNotFoundError(f"Missing required YAML file: {path}")
        return None

    with open(path, "r", encoding="utf-8") as file_in:
        return yaml.safe_load(file_in) or {}


def load_structured_file(path, required=False):
    if path is None or not path.exists():
        if required:
            raise FileNotFoundError(f"Missing required file: {path}")
        return None

    suffix = path.suffix.lower()

    if suffix in {".yaml", ".yml"}:
        return load_yaml(path, required=required)

    if suffix == ".json":
        with open(path, "r", encoding="utf-8") as file_in:
            return json.load(file_in)

    raise ValueError(f"Unsupported structured file type: {path}. Expected .yaml, .yml, or .json.")


def load_model(model_dir):
    schema_path = model_dir / "schema.yaml"
    slots_path = model_dir / "slots.yaml"
    enums_path = model_dir / "enums.yaml"
    terminology_path = model_dir / "terminology.yaml"

    schema_source = load_yaml(schema_path, required=True)
    slots_source = load_yaml(slots_path, required=True)
    enums_source = load_yaml(enums_path, required=True)
    terminology = load_yaml(terminology_path, required=False) or {}

    schema = copy.deepcopy(schema_source)
    schema["slots"] = copy.deepcopy(slots_source.get("slots", {}))
    schema["enums"] = copy.deepcopy(enums_source.get("enums", {}))

    raw_files = {
        "schema.yaml": schema_source,
        "slots.yaml": slots_source,
        "enums.yaml": enums_source,
    }

    return schema, terminology, raw_files


def html_escape(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def normalize_curie(curie):
    if curie is None:
        return ""

    curie = str(curie).strip()

    if not curie:
        return ""

    if ":" not in curie:
        if curie.upper().startswith("C") and curie[1:].isdigit():
            return f"ncit:{curie.upper()}"
        return curie

    prefix, code = curie.split(":", 1)
    return f"{prefix.strip().lower()}:{code.strip()}"


def build_terminology_index(terminology):
    index = {}

    for source, source_def in terminology.items():
        if not isinstance(source_def, dict):
            continue

        source_url = source_def.get("source_url", "")

        for curie, concept_def in source_def.get("concepts", {}).items():
            if not isinstance(concept_def, dict):
                continue

            normalized = normalize_curie(curie)

            index[normalized] = {
                "source": source,
                "source_url": source_url,
                "d4cg_label": concept_def.get("d4cg_label", ""),
                "description": concept_def.get("description", ""),
                "last_updated": concept_def.get("last_updated", ""),
            }

    return index


def terminology_concept(curie, terminology_index):
    if not curie:
        return {}

    return terminology_index.get(normalize_curie(curie), {})


def curie_to_url(curie, schema, terminology_index):
    if not curie:
        return ""

    normalized = normalize_curie(curie)

    if normalized.startswith("ncit:"):
        local_id = normalized.split(":", 1)[1]
        return "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/" + local_id

    term = terminology_concept(curie, terminology_index)
    source_url = term.get("source_url", "")

    if source_url:
        return source_url

    if ":" not in str(curie):
        return ""

    prefix, local_id = str(curie).split(":", 1)
    prefixes = schema.get("prefixes", {})
    prefix_url = prefixes.get(prefix) or prefixes.get(prefix.lower()) or prefixes.get(prefix.upper()) or ""

    if isinstance(prefix_url, dict):
        prefix_url = prefix_url.get("prefix_reference") or prefix_url.get("reference") or ""

    if not prefix_url:
        return ""

    return str(prefix_url) + local_id


def safe_id(value):
    return str(value).replace(" ", "-").replace("_", "-").replace(".", "-").lower()


def subset_attr(subsets):
    if not subsets:
        return ""

    return ' data-subsets="' + html_escape(" ".join(subsets)) + '"'


def has_subset(item_def, subset):
    return subset in item_def.get("in_subset", [])


def render_release_archive(commons, releases):
    commons_def = COMMONS[commons]

    lines = [
        "---",
        "layout: default",
        "title: Past Releases",
        f"parent: {commons_def['title']}",
        "nav_order: 1",
        "---",
        "",
        f"# {commons_def['title']} Past Releases",
        "",
        "| Release | Status | Date | Notes |",
        "| --- | --- | --- | --- |",
    ]

    for release in releases:
        label = release["version"]

        if release["status"] == "Current":
            label += " (current)"

        lines.append(f"| [{label}]({release['url']}) | {release['status']} | {release['date']} | {release['notes']} |")

    lines.append("")
    return "\n".join(lines)


def render_change_notes(notes):
    if not notes:
        return ""

    return ""


def init_view_front_matter(schema, commons, page_context):
    model_title = COMMONS[commons]["title"]

    if page_context == "current":
        nav_title = model_title
        nav_lines = [
            "nav_order: " + str(COMMONS[commons]["nav_order"]),
            "has_children: true",
        ]
    else:
        nav_title = str(schema["version"])
        nav_lines = [
            "nav_exclude: true",
            "search_exclude: true",
        ]

    lines = [
        "---",
        "layout: default",
        f"title: {nav_title}",
    ]

    lines.extend(nav_lines)
    lines.extend(["---", ""])

    return "\n".join(lines)


def render_view_selector(schema):
    rows = [
        '<div class="view-selector">',
        '<label for="view-selector" class="text-delta">View</label>',
        '<select id="view-selector" onchange="switchView(this.value)">',
    ]

    for view_name, view_def in schema["subsets"].items():
        label = view_def.get("title", view_name)
        selected = " selected" if view_name == "base" else ""
        rows.append(f'<option value="{html_escape(view_name)}"{selected}>{html_escape(label)}</option>')

    rows.extend([
        "</select>",
        "</div>",
    ])

    return "\n".join(rows)


def render_view_header(schema, notes):
    version = str(schema["version"])
    title = schema.get("title", "")

    header_comps = [
        f"# {html_escape(title)} `{html_escape(version)}`",
        render_model_meta(schema),
        render_view_selector(schema),
        '<div id="view-description" class="view-description"></div>',
    ]

    change_notes = render_change_notes(notes)

    if change_notes:
        header_comps.append(change_notes)

    return "\n\n".join(header_comps)


def render_view_mode_toggle():
    return """
<div class="view-mode-toggle">
  <span class="toggle-label">Rendered</span>
  <label class="switch">
    <input id="view-mode-checkbox" type="checkbox" onchange="switchModelMode(this.checked)">
    <span class="slider"></span>
  </label>
  <span class="toggle-label">Raw</span>
</div>
"""


def enum_modal_id(enum_name):
    return "enum-modal-" + safe_id(enum_name)


def count_pvs(schema, enum_name):
    enum_def = schema.get("enums", {}).get(enum_name, {})
    return len(enum_def.get("permissible_values", {}))


def first_existing_enum(schema, enum_names):
    for enum_name in enum_names:
        if enum_name in schema.get("enums", {}):
            return enum_name

    return None


def render_model_meta(schema):
    contributor_enum = first_existing_enum(schema, ["DataContributorIdEnum", "DataContributorIDEnum"])
    study_enum = first_existing_enum(schema, ["StudyIdEnum", "StudyIDEnum"])

    contributor_count = count_pvs(schema, contributor_enum) if contributor_enum else 0
    study_count = count_pvs(schema, study_enum) if study_enum else 0

    lines = [
        '<div class="model-meta-grid">',
        '<div><span>Schema ID</span><span class="model-meta-value">' + f'<code>{html_escape(schema.get("id", ""))}</code>' + "</span></div>",
        '<div><span>License</span><span class="model-meta-value">' + html_escape(schema.get("license", "")) + "</span></div>",
        '<div><span>Concepts</span><span class="model-meta-value">' + f'{len(schema.get("classes", {}))} classes · {len(schema.get("slots", {}))} slots · {len(schema.get("enums", {}))} enums' + "</span></div>",
    ]

    if contributor_count or study_count:
        provenance = []

        if contributor_count:
            provenance.append(f'<button type="button" class="model-meta-link" onclick="openEnumModal(\'{enum_modal_id(contributor_enum)}\')">{contributor_count} contributors</button>')

        if study_count:
            provenance.append(f'<button type="button" class="model-meta-link" onclick="openEnumModal(\'{enum_modal_id(study_enum)}\')">{study_count} studies</button>')

        lines.append('<div><span>Community</span><span class="model-meta-value">' + " · ".join(provenance) + "</span></div>")

    lines.append("</div>")
    return "\n".join(lines)


def clean_view_schema(value):
    if isinstance(value, dict):
        out = {}

        for key, child in value.items():
            if key in ["in_subset", "slot_usage"]:
                continue

            out[key] = clean_view_schema(child)

        return out

    if isinstance(value, list):
        return [clean_view_schema(child) for child in value]

    return value


def filter_schema_by_subset(schema, subset):
    if subset == "base":
        return schema

    filtered = dict(schema)
    filtered["classes"] = {}
    filtered["slots"] = {}
    filtered["enums"] = {}

    kept_slot_names = set()

    for class_name, class_def in schema.get("classes", {}).items():
        if not has_subset(class_def, subset):
            continue

        slot_usage = class_def.get("slot_usage", {})
        kept_class_slots = []

        for slot_name in class_def.get("slots", []):
            usage_def = slot_usage.get(slot_name, {})

            if has_subset(usage_def, subset):
                kept_class_slots.append(slot_name)
                kept_slot_names.add(slot_name)

        if not kept_class_slots:
            continue

        new_class_def = dict(class_def)
        new_class_def["slots"] = kept_class_slots
        new_class_def.pop("slot_usage", None)

        filtered["classes"][class_name] = clean_view_schema(new_class_def)

    for slot_name in kept_slot_names:
        if slot_name in schema.get("slots", {}):
            filtered["slots"][slot_name] = clean_view_schema(schema["slots"][slot_name])

    enum_names = set()

    for slot_def in filtered["slots"].values():
        slot_range = slot_def.get("range")

        if slot_range in schema.get("enums", {}):
            enum_names.add(slot_range)

    for enum_name in enum_names:
        enum_def = schema["enums"][enum_name]
        new_enum_def = dict(enum_def)
        new_pvs = {}

        for pv_name, pv_def in enum_def.get("permissible_values", {}).items():
            if has_subset(pv_def, subset):
                new_pvs[pv_name] = clean_view_schema(pv_def)

        if new_pvs:
            new_enum_def["permissible_values"] = new_pvs
            filtered["enums"][enum_name] = clean_view_schema(new_enum_def)

    filtered["subsets"] = {
        subset: clean_view_schema(schema["subsets"][subset])
    }

    return filtered


def render_class_tree(class_name, class_def, full_schema, view_schema):
    lines = ["erDiagram"]

    for slot in class_def.get("slots", []):
        slot_def = full_schema.get("slots", {}).get(slot, {})
        slot_range = slot_def.get("range")

        if slot_range in view_schema.get("classes", {}):
            lines.append(f"    {slot_range} ||--o{{ {class_name} : {slot}")

    if len(lines) == 1:
        return ""

    return "\n".join(lines)


def render_class_diagrams(class_name, class_def, schema):
    diagrams = {}

    for subset in class_def.get("in_subset", []):
        view_schema = filter_schema_by_subset(schema, subset)

        if class_name not in view_schema.get("classes", {}):
            continue

        tree = render_class_tree(class_name, class_def, schema, view_schema)

        if tree:
            diagrams[subset] = tree

    if not diagrams:
        return ""

    payload = html_escape(json.dumps(diagrams))

    return (
        f'<details class="diagram-details" data-diagrams="{payload}">\n'
        '<summary class="text-delta">Diagram</summary>\n\n'
        '<pre class="mermaid class-diagram-renderer"></pre>\n\n'
        "</details>"
    )


def render_enum_button(enum_name):
    enum_id = enum_modal_id(enum_name)

    return (
        '<button type="button" '
        'class="enum-link" '
        f'onclick="openEnumModal(\'{enum_id}\')">'
        f"{html_escape(enum_name)}"
        "</button>"
    )


def render_class_copy_icon(class_name):
    return (
        '<button type="button" '
        'class="copy-action class-copy-icon" '
        f'data-class-name="{html_escape(class_name)}" '
        'onclick="copyClass(this)" '
        'aria-label="Copy class" '
        'title="Copy class">'
        f"{COPY_ICON}"
        "</button>"
    )


def render_slot_copy_icon(class_name, slot_name):
    return (
        '<button type="button" '
        'class="copy-action slot-copy-icon" '
        f'data-class-name="{html_escape(class_name)}" '
        f'data-slot-name="{html_escape(slot_name)}" '
        'onclick="copySlot(this)" '
        'aria-label="Copy slot" '
        'title="Copy slot">'
        f"{COPY_ICON}"
        "</button>"
    )


def render_pv_copy_icon(pv_name, meaning):
    return (
        '<button type="button" '
        'class="copy-action pv-copy-icon" '
        f'data-pv-name="{html_escape(pv_name)}" '
        f'data-pv-meaning="{html_escape(meaning)}" '
        'onclick="copyPv(this)" '
        'aria-label="Copy permissible value" '
        'title="Copy permissible value">'
        f"{COPY_ICON}"
        "</button>"
    )


def clipped_cell(content_html, title_text="", cell_class=""):
    return (
        f'<td class="{cell_class}" title="{html_escape(title_text)}">'
        '<details class="cell-details">'
        "<summary>"
        f"<span>{content_html}</span>"
        "</summary>"
        "</details>"
        "</td>"
    )


def copyable_clipped_cell(content_html, title_text, cell_class, copy_button):
    return (
        f'<td class="{cell_class} copyable-cell" title="{html_escape(title_text)}">'
        f"{copy_button}"
        '<details class="cell-details">'
        "<summary>"
        f"<span>{content_html}</span>"
        "</summary>"
        "</details>"
        "</td>"
    )


def render_enum_modals(schema, terminology_index):
    if not schema.get("enums"):
        return ""

    comps = []

    for enum_name, enum_def in sorted(schema["enums"].items()):
        enum_id = enum_modal_id(enum_name)
        pv_count = len(enum_def.get("permissible_values", {}))

        rows = [
            f'<div id="{enum_id}" class="enum-modal" data-pv-count="{pv_count}" onclick="closeEnumModal(\'{enum_id}\')">',
            '<div class="enum-modal-content" onclick="event.stopPropagation()">',
            f'<button type="button" class="enum-modal-close" onclick="closeEnumModal(\'{enum_id}\')">×</button>',
            f"<h3>{html_escape(enum_name)}</h3>",
            '<div class="enum-modal-body">',
            '<div class="enum-modal-loading raw-loading" style="display:none;">Loading…</div>',
            '<div class="enum-modal-loaded-content"></div>',
            '<template class="enum-modal-template">',
            '<table class="model-table enum-table">',
            "<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>",
            "<tbody>",
        ]

        for pv_name, pv_def in enum_def.get("permissible_values", {}).items():
            meaning = pv_def.get("meaning", "")
            subsets = pv_def.get("in_subset", [])
            meaning_url = curie_to_url(meaning, schema, terminology_index)

            if meaning_url:
                meaning_html = f'<a href="{html_escape(meaning_url)}" target="_blank" rel="noopener">{html_escape(meaning)}</a>'
            else:
                meaning_html = html_escape(meaning)

            term = terminology_concept(meaning, terminology_index)
            description = term.get("description", "")

            copy_button = render_pv_copy_icon(pv_name, meaning)

            rows.append(
                f'<tr{subset_attr(subsets)}>'
                f'{copyable_clipped_cell(html_escape(pv_name), pv_name, "enum-pv", copy_button)}'
                f'{clipped_cell(description, description, "enum-description")}'
                f'<td class="enum-meaning" title="{html_escape(meaning)}"><span>{meaning_html}</span></td>'
                "</tr>"
            )

        rows.extend([
            "</tbody>",
            "</table>",
            "</template>",
            "</div>",
            "</div>",
            "</div>",
        ])

        comps.append("\n".join(rows))

    return "\n\n".join(comps)

def render_view_matrix(schema):
    views = []

    for view in schema.get("subsets", {}).keys():
        if view != "base":
            views.append(view)

    rows = [
        '<div id="view-matrix-wrap" class="view-matrix-wrap">',
        '<div class="view-matrix-title">Class Inclusion by View</div>',
        '<div class="view-matrix-scroll">',
        '<table class="view-matrix">',
        "<thead>",
        "<tr>",
        "<th>Domain</th>",
        "<th>Class</th>",
    ]

    for view in views:
        label = schema["subsets"][view].get("name", view).upper()
        rows.append(f'<th class="view-matrix-col" data-view-col="{html_escape(view)}" title="{html_escape(label)}">{html_escape(label)}</th>')

    rows.extend([
        "</tr>",
        "</thead>",
        "<tbody>",
    ])

    class_rows = []

    for class_name, class_def in schema.get("classes", {}).items():
        domain = class_def.get("annotations", {}).get("domain")

        if isinstance(domain, dict):
            domain = domain.get("value")

        if not domain:
            raise ValueError(f"Class is missing required domain annotation: {class_name}")

        if str(domain).lower() == "internal":
            continue

        class_rows.append((domain, class_name, class_def))

    for domain, class_name, class_def in sorted(class_rows):
        subsets = set(class_def.get("in_subset", []))
        domain_label = str(domain).replace("_", " ").title()

        rows.append(
            f'<tr class="view-matrix-row" data-class-ref="class-{safe_id(class_name)}"{subset_attr(list(subsets))}>'
            f'<td title="{html_escape(domain_label)}">{html_escape(domain_label)}</td>'
            f'<td title="{html_escape(class_name)}"><a href="#class-{safe_id(class_name)}">{html_escape(class_name)}</a></td>'
        )

        for view in views:
            included = view in subsets
            cell_class = "included" if included else "not-included"
            rows.append(f'<td class="view-matrix-col {cell_class}" data-view-col="{html_escape(view)}"></td>')

        rows.append("</tr>")

    rows.extend([
        "</tbody>",
        "</table>",
        "</div>",
        "</div>",
    ])

    return "\n".join(rows)


def render_model_toc(schema):
    domains = {}

    for class_name, class_def in schema.get("classes", {}).items():
        domain = class_def.get("annotations", {}).get("domain")

        if isinstance(domain, dict):
            domain = domain.get("value")

        if not domain:
            raise ValueError(f"Class is missing required domain annotation: {class_name}")

        if str(domain).lower() == "internal":
            continue

        domains.setdefault(domain, []).append(class_name)

    rows = ['<nav class="model-toc" aria-label="Model contents">']

    for domain in domains.keys():
        rows.append(f'<a class="model-toc-domain" href="#domain-{safe_id(domain)}">{html_escape(str(domain).title())}</a>')

        for class_name in domains[domain]:
            class_subsets = " ".join(schema["classes"][class_name].get("in_subset", []))
            rows.append(f'<a class="model-toc-class" data-subsets="{html_escape(class_subsets)}" href="#class-{safe_id(class_name)}">{html_escape(class_name)}</a>')

    rows.append("</nav>")
    return "\n".join(rows)


def render_class_section(class_name, class_def, schema, terminology_index):
    subsets = class_def.get("in_subset", [])
    class_id = "class-" + safe_id(class_name)

    comps = [
        f'<section id="{class_id}" class="class-section"{subset_attr(subsets)} markdown="1">'
    ]

    comps.append(f"## {class_name}")

    description = class_def.get("description", "")

    if description:
        comps.append(f'<p class="class-description">{html_escape(description)}</p>')

    diagrams = render_class_diagrams(class_name, class_def, schema)

    if diagrams:
        comps.append(diagrams)

    comps.append(render_class_table(class_name, class_def, schema, terminology_index))
    comps.append("</section>")

    return "\n\n".join(comp for comp in comps if comp)


def render_class_table(class_name, class_def, schema, terminology_index):
    rows = []
    slot_usage = class_def.get("slot_usage", {})

    for slot_name in class_def.get("slots", []):
        slot_def = schema.get("slots", {}).get(slot_name, {})
        usage_def = slot_usage.get(slot_name, {})
        subsets = usage_def.get("in_subset", ["base"])
        slot_range = slot_def.get("range", "")
        slot_uri = slot_def.get("slot_uri", "")

        term = terminology_concept(slot_uri, terminology_index)
        description = term.get("description", "")

        if slot_range in schema.get("enums", {}):
            range_html = render_enum_button(slot_range)
        else:
            range_html = f'<code class="primitive-range">{html_escape(slot_range)}</code>' if slot_range else ""

        copy_button = render_slot_copy_icon(class_name, slot_name)

        rows.append(
            f'<tr{subset_attr(subsets)}>'
            f'{copyable_clipped_cell(html_escape(slot_name), slot_name, "slot-name", copy_button)}'
            f'{clipped_cell(html_escape(description), description, "slot-description")}'
            f'<td class="slot-range" title="{html_escape(slot_range)}"><span>{range_html}</span></td>'
            "</tr>"
        )

    return (
        '<div class="class-table-wrap">'
        f"{render_class_copy_icon(class_name)}"
        '<table class="model-table class-slot-table">'
        "<thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead>"
        "<tbody>"
        + "\n".join(rows)
        + "</tbody>"
        "</table>"
        "</div>"
    )


def render_domain_intro(domain, schema):
    docs = schema.get("annotations", {}).get("docs", {})
    domain_docs = docs.get("domains", {}).get(domain, {})
    title = domain_docs.get("title", str(domain).title())
    description = domain_docs.get("description", "")
    icon = DOMAIN_ICONS.get(domain, "")

    parts = [f'<div class="domain-banner domain-{safe_id(domain)}">']

    if icon:
        parts.append(f'<div class="domain-icon">{icon}</div>')

    parts.append('<div class="domain-banner-text">')
    parts.append(f'<div class="domain-heading">{html_escape(title)}</div>')

    if description:
        parts.append(f'<p class="domain-description">{html_escape(description)}</p>')

    parts.append("</div>")
    parts.append("</div>")

    return "\n".join(parts)


def render_domain_sections(schema, terminology_index):
    domains = {}

    for class_name, class_def in schema.get("classes", {}).items():
        domain = class_def.get("annotations", {}).get("domain")

        if isinstance(domain, dict):
            domain = domain.get("value")

        if not domain:
            raise ValueError(f"Class is missing required domain annotation: {class_name}")

        domains.setdefault(domain, []).append((class_name, class_def))

    comps = []

    for domain in domains.keys():
        if str(domain).lower() == "internal":
            continue

        domain_id = "domain-" + safe_id(domain)

        comps.append(f'<section id="{domain_id}" class="domain-section" data-domain="{safe_id(domain)}" markdown="1">')
        comps.append(render_domain_intro(domain, schema))

        for class_name, class_def in domains[domain]:
            comps.append(render_class_section(class_name, class_def, schema, terminology_index))

        comps.append("</section>")

    return "\n\n".join(comps)


def render_raw_schema_payload(raw_files):
    raw = json.dumps(raw_files)
    raw = raw.replace("</", "<\\/")

    return f'<script id="raw-schema-payload" type="application/json">{raw}</script>'


def render_view_metadata_payload(schema):
    view_metadata = {}

    for subset, subset_def in schema.get("subsets", {}).items():
        view_metadata[subset] = {
            "title": subset_def.get("title", subset),
            "name": subset_def.get("name", subset),
            "description": subset_def.get("description", ""),
        }

    raw = json.dumps(view_metadata)
    raw = raw.replace("</", "<\\/")

    return f'<script id="view-metadata-payload" type="application/json">{raw}</script>'


def version_sort_key(value):
    return tuple(int(part) if part.isdigit() else part for part in str(value).split("."))


def release_sort_key(release):
    return version_sort_key(release["version"])


def discover_releases(commons_folder, current_version):
    releases_dir = Path(commons_folder) / "releases"

    if not releases_dir.exists():
        return []

    releases = []

    for path in releases_dir.iterdir():
        if not path.is_dir():
            continue

        index_path = path / "index.md"

        if not index_path.exists():
            continue

        version = path.name
        status = "Current" if version == current_version else "Past"

        releases.append({
            "version": version,
            "status": status,
            "url": f"./{version}/",
            "date": "",
            "notes": "",
        })

    releases.sort(key=release_sort_key, reverse=True)
    return releases


def render_raw_file_selector(raw_files):
    rows = ['<div class="raw-file-selector">']

    index = 0

    for filename in raw_files.keys():
        active = " active" if index == 0 else ""

        rows.append(
            '<button type="button" '
            f'class="raw-file-button{active}" '
            f'data-raw-file="{html_escape(filename)}" '
            f'onclick="switchRawFile(\'{html_escape(filename)}\')">'
            f"{html_escape(filename)}"
            "</button>"
        )

        index += 1

    rows.append("</div>")

    return "\n".join(rows)


def render_model(schema, terminology_index, raw_files):
    comps = []

    comps.append('<div id="docs-model-view" markdown="1">')
    comps.append('<div class="model-main" markdown="1">')
    comps.append(render_domain_sections(schema, terminology_index))
    comps.append(render_enum_modals(schema, terminology_index))
    comps.append("</div>")
    comps.append("</div>")

    comps.append(render_model_toc(schema))

    comps.append('<div id="raw-model-view" style="display:none;">')
    comps.append(render_raw_file_selector(raw_files))

    comps.append('<div class="raw-content-wrap">')
    comps.append(
        '<button type="button" '
        'class="copy-action raw-copy-icon" '
        'onclick="copyRaw(this)" '
        'aria-label="Copy displayed YAML" '
        'title="Copy displayed YAML">'
        f'{COPY_ICON}'
        '</button>'
    )
    comps.append('<div id="raw-loading" class="raw-loading" style="display:none;">Loading…</div>')
    comps.append('<div id="raw-schema-renderer" class="yaml-renderer"></div>')
    comps.append("</div>")

    comps.append("</div>")

    comps.append(render_view_metadata_payload(schema))
    comps.append(render_raw_schema_payload(raw_files))

    return "\n\n".join(comp for comp in comps if comp)


def assemble_view(schema, notes, commons, page_context, terminology_index, raw_files):
    view_comps = []

    view_comps.append(init_view_front_matter(schema, commons, page_context))

    view_comps.append('<div class="model-header" markdown="1">')
    view_comps.append(render_view_header(schema, notes))

    view_comps.append(
        '<details class="scope-matrix-details">\n'
        '<summary class="text-delta">Scope Matrix</summary>\n\n'
        + render_view_matrix(schema)
        + "\n\n</details>"
    )

    view_comps.append(render_view_mode_toggle())
    view_comps.append("</div>")

    view_comps.append(render_model(schema, terminology_index, raw_files))

    return "\n\n".join(comp for comp in view_comps if comp)


def main(commons, version, notes_path):
    commons_folder = COMMONS[commons]["folder"]
    model_dir = Path(commons_folder) / "releases" / version / "model"

    schema, terminology, raw_files = load_model(model_dir)
    terminology_index = build_terminology_index(terminology)

    notes = load_structured_file(notes_path, required=False) if notes_path else None

    schema_version = str(schema["version"])

    if schema_version != str(version):
        raise ValueError(f"Version mismatch: command line version is {version}, but schema.yaml declares {schema_version}")

    pages = []

    current_view = assemble_view(schema, notes, commons, "current", terminology_index, raw_files)
    release_view = assemble_view(schema, notes, commons, "release", terminology_index, raw_files)

    pages.append((Path(f"{commons_folder}/index.md"), current_view))
    pages.append((Path(f"{commons_folder}/releases/{version}/index.md"), release_view))

    releases = discover_releases(commons_folder, version)

    found_current_release = False

    for release in releases:
        if release["version"] == version:
            found_current_release = True
            break

    if not found_current_release:
        releases.append({
            "version": version,
            "status": "Current",
            "url": f"./{version}/",
            "date": "",
            "notes": "",
        })

    releases.sort(key=release_sort_key, reverse=True)

    pages.insert(0, (Path(f"{commons_folder}/releases/index.md"), render_release_archive(commons, releases)))

    for path, markdown in pages:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate static D4CG Data Model docs site.")

    parser.add_argument("--commons", required=True, choices=COMMONS.keys(), help="Commons to generate: pcdc or predict.")
    parser.add_argument("--version", required=True, help="Release version to generate, for example 2.0.")
    parser.add_argument("--change_notes", required=False, help="Optional YAML or JSON change notes file.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate an existing release folder.")

    args = parser.parse_args()

    notes_path = Path(args.change_notes) if args.change_notes else None

    main(args.commons, args.version, notes_path)