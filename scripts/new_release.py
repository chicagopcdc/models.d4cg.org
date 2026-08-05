import json, argparse
from pathlib import Path


COMMONS = {
    "pcdc": {
        "folder": "pcdc",
        "title": "Pediatric Oncology",
        "nav_order": 2
    },
    "predict": {
        "folder": "predict",
        "title": "Monogenic Diabetes",
        "nav_order": 3
    }
}

DOMAIN_ICONS = {
    "demographics": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-icon lucide-user"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>""",
    "testing": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-dna-icon lucide-dna"><path d="m10 16 1.5 1.5"/><path d="m14 8-1.5-1.5"/><path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993"/><path d="m16.5 10.5 1 1"/><path d="m17 6-2.891-2.891"/><path d="M2 15c6.667-6 13.333 0 20-6"/><path d="m20 9 .891.891"/><path d="M3.109 14.109 4 15"/><path d="m6.5 12.5 1 1"/><path d="m7 18 2.891 2.891"/><path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993"/></svg>""",
    "disease_attributes": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-network-icon lucide-network"><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/></svg>""",
    "intervention": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-hospital-icon lucide-hospital"><path d="M12 7v4"/><path d="M14 21v-3a2 2 0 0 0-4 0v3"/><path d="M14 9h-4"/><path d="M18 11h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 21V5a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16"/></svg>""",
    "monitoring": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-stethoscope-icon lucide-stethoscope"><path d="M11 2v2"/><path d="M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/></svg>"""
}


def load_json(path, required):
    if path is None or not path.exists():
        if required:
            raise FileNotFoundError(f"Missing required JSON file: {path}")
        return None

    with open(path, "r") as json_file:
        return json.load(json_file)


def html_escape(value):
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def curie_to_url(curie, schema):
    if not curie or ":" not in curie:
        return ""

    prefix, local_id = curie.split(":", 1)

    if prefix.lower() == "ncit":
        return "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/" + local_id

    prefix_url = schema.get("prefixes", {}).get(prefix, "")
    if not prefix_url:
        return ""

    return prefix_url + local_id


def safe_id(value):
    return (
        str(value)
        .replace(" ", "-")
        .replace("_", "-")
        .replace(".", "-")
        .lower()
    )


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
        "| --- | --- | --- | --- |"
    ]

    for release in releases:
        label = release["version"]
        if release["status"] == "Current":
            label += " (current)"

        lines.append(
            f"| [{label}]({release['url']}) | {release['status']} | {release['date']} | {release['notes']} |"
        )

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
            "has_children: true"
        ]
    else:
        nav_title = str(schema["version"])
        nav_lines = ["nav_exclude: true", "search_exclude: true"]

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
        '<select id="view-selector" onchange="switchView(this.value)">'
    ]

    for view_name, view_def in schema["subsets"].items():
        label = view_def.get("title", view_name)
        selected = " selected" if view_name == "base" else ""
        rows.append(f'<option value="{view_name}"{selected}>{html_escape(label)}</option>')

    rows.extend([
        "</select>",
        "</div>"
    ])

    return "\n".join(rows)


def render_view_header(schema, notes):
    version = str(schema["version"])
    title = schema.get("title")

    header_comps = [
        f"# {html_escape(title)} `{html_escape(version)}`",
        render_model_meta(schema),
        render_view_selector(schema),
        '<div id="view-description" class="view-description"></div>'
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
        f'<div><span>Schema ID</span><span class="model-meta-value"><code>{html_escape(schema.get("id", ""))}</code></span></div>',
        f'<div><span>License</span><span class="model-meta-value">{html_escape(schema.get("license", ""))}</span></div>',
        (
            '<div><span>Concepts</span><span class="model-meta-value">'
            f'{len(schema.get("classes", {}))} classes · '
            f'{len(schema.get("slots", {}))} slots · '
            f'{len(schema.get("enums", {}))} enums'
            '</span></div>'
        )
    ]

    if contributor_count or study_count:
        provenance = []

        if contributor_count:
            provenance.append(
                f'<button type="button" class="model-meta-link" onclick="openEnumModal(\'{enum_modal_id(contributor_enum)}\')">{contributor_count} contributors</button>'
            )

        if study_count:
            provenance.append(
                f'<button type="button" class="model-meta-link" onclick="openEnumModal(\'{enum_modal_id(study_enum)}\')">{study_count} studies</button>'
            )

        lines.append(
            '<div><span>Community</span><span class="model-meta-value">'
            + " · ".join(provenance) +
            '</span></div>'
        )

    lines.append('</div>')
    return "\n".join(lines)


def clean_view_schema(value):
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if k in ["in_subset", "slot_usage"]:
                continue
            out[k] = clean_view_schema(v)
        return out

    if isinstance(value, list):
        return [clean_view_schema(v) for v in value]

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

    enum_names = {
        slot_def.get("range")
        for slot_def in filtered["slots"].values()
        if slot_def.get("range") in schema.get("enums", {})
    }

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
    lines = [
        "erDiagram"
    ]

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
        '</details>'
    )


def render_enum_button(enum_name):
    enum_id = "enum-modal-" + safe_id(enum_name)
    return (
        f'<button type="button" class="enum-link" '
        f'onclick="openEnumModal(\'{enum_id}\')">'
        f'{html_escape(enum_name)}'
        f'</button>'
    )

def render_enum_modals(schema):
    if not schema.get("enums"):
        return ""

    comps = []

    for enum_name, enum_def in sorted(schema["enums"].items()):
        enum_id = "enum-modal-" + safe_id(enum_name)
        rows = [
            f'<div id="{enum_id}" class="enum-modal" onclick="closeEnumModal(\'{enum_id}\')">',
            '<div class="enum-modal-content" onclick="event.stopPropagation()">',
            f'<button type="button" class="enum-modal-close" onclick="closeEnumModal(\'{enum_id}\')">×</button>',
            f'<h3>{html_escape(enum_name)}</h3>',
            '<table class="model-table enum-table">',
            '<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>',
            '<tbody>'
        ]

        for pv_name, pv_def in enum_def.get("permissible_values", {}).items():
            meaning = pv_def.get("meaning", "")
            meaning_url = curie_to_url(meaning, schema)
            comments = "<br>".join([html_escape(c) for c in pv_def.get("comments", [])])
            subsets = pv_def.get("in_subset", [])

            if meaning_url:
                meaning_html = (
                    f'<a href="{html_escape(meaning_url)}" target="_blank" rel="noopener">'
                    f'{html_escape(meaning)}'
                    '</a>'
                )
            else:
                meaning_html = html_escape(meaning)

            description = pv_def.get("description", "")
            if not description:
                description = "<br>".join([html_escape(c) for c in pv_def.get("comments", [])])

            rows.append(
                f'<tr{subset_attr(subsets)}>'
                f'{clipped_cell(html_escape(pv_name), pv_name, "enum-pv")}'
                f'{clipped_cell(description, description, "enum-description")}'
                f'<td class="enum-meaning" title="{html_escape(meaning)}"><span>{meaning_html}</span></td>'
                "</tr>"
            )

        rows.extend([
            '</tbody>',
            '</table>',
            '</div>',
            '</div>'
        ])

        comps.append("\n".join(rows))

    return "\n\n".join(comps)


def render_view_matrix(schema):
    views = [v for v in schema.get("subsets", {}).keys() if v != "base"]

    rows = [
        '<div id="view-matrix-wrap" class="view-matrix-wrap">',
        '<div class="view-matrix-title">Class Inclusion by View</div>',
        '<div class="view-matrix-scroll">',
        '<table class="view-matrix">',
        '<thead>',
        '<tr>',
        '<th>Domain</th>',
        '<th>Class</th>'
    ]

    for view in views:
        label = schema["subsets"][view].get("name", view).upper()
        rows.append(
            f'<th class="view-matrix-col" data-view-col="{html_escape(view)}" '
            f'title="{html_escape(label)}">{html_escape(label)}</th>'
        )

    rows.extend([
        '</tr>',
        '</thead>',
        '<tbody>'
    ])

    class_rows = []

    for class_name, class_def in schema.get("classes", {}).items():
        domain = class_def.get("annotations", {}).get("domain")

        if isinstance(domain, dict):
            domain = domain.get("value")

        if not domain:
            raise ValueError(f"Class is missing required domain annotation: {class_name}")

        if domain.lower() == "internal":
            continue

        class_rows.append((domain, class_name, class_def))

    for domain, class_name, class_def in sorted(class_rows):
        subsets = set(class_def.get("in_subset", []))
        domain_label = domain.replace("_", " ").title()

        rows.append(
            f'<tr class="view-matrix-row" data-class-ref="class-{safe_id(class_name)}"{subset_attr(list(subsets))}>'
            f'<td title="{html_escape(domain_label)}">{html_escape(domain_label)}</td>'
            f'<td title="{html_escape(class_name)}">'
            f'<a href="#class-{safe_id(class_name)}">{html_escape(class_name)}</a>'
            f'</td>'
        )

        for view in views:
            included = view in subsets
            cell_class = "included" if included else "not-included"
            rows.append(
                f'<td class="view-matrix-col {cell_class}" data-view-col="{html_escape(view)}"></td>'
            )

        rows.append('</tr>')

    rows.extend([
        '</tbody>',
        '</table>',
        '</div>',
        '</div>'
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
        if domain.lower() == "internal":
            continue

        if domain not in domains:
            domains[domain] = []
        domains[domain].append(class_name)

    rows = ['<nav class="model-toc" aria-label="Model contents">']

    for domain in domains.keys():
        rows.append(f'<a class="model-toc-domain" href="#domain-{safe_id(domain)}">{html_escape(domain.title())}</a>')
        for class_name in domains[domain]:
            rows.append(f'<a class="model-toc-class" data-subsets="{html_escape(" ".join(schema["classes"][class_name].get("in_subset", [])))}" href="#class-{safe_id(class_name)}">{html_escape(class_name)}</a>')

    rows.append("</nav>")
    return "\n".join(rows)


def render_class_section(class_name, class_def, schema):
    subsets = class_def.get("in_subset", [])
    class_id = "class-" + safe_id(class_name)
    comps = [f'<section id="{class_id}" class="class-section"{subset_attr(subsets)} markdown="1">']
    comps.append(f"## {class_name}")
    description = class_def.get("description", "")
    if description:
        comps.append(f'<p class="class-description">{html_escape(description)}</p>')

    diagrams = render_class_diagrams(class_name, class_def, schema)
    if diagrams:
        comps.append(diagrams)

    comps.append(render_class_table(class_name, class_def, schema))
    comps.append("</section>")

    return "\n\n".join([c for c in comps if c])


def render_json_value(value, label=None, level=0, comma=False):
    comma_text = "," if comma else ""

    if isinstance(value, dict):
        summary = f'<span class="json-key">"{html_escape(label)}"</span>: ' if label else ""
        rows = [
            f'<details open class="json-node"><summary>{summary}<span class="json-closed">{{...}}</span><span class="json-open">{{</span></summary>'
        ]
        rows.append('<div class="json-children">')

        items = list(value.items())
        for i, (k, v) in enumerate(items):
            rows.append(render_json_value(v, k, level + 1, comma=(i < len(items) - 1)))

        rows.append("</div>")
        rows.append(f'<div class="json-end">}}{comma_text}</div>')
        rows.append("</details>")

        return "\n".join(rows)

    if isinstance(value, list):
        summary = f'<span class="json-key">"{html_escape(label)}"</span>: ' if label else ""
        rows = [
            f'<details class="json-node"><summary>{summary}<span class="json-closed">[...]</span><span class="json-open">[</span></summary>'
        ]
        rows.append('<div class="json-children">')

        for i, item in enumerate(value):
            rows.append(render_json_value(item, None, level + 1, comma=(i < len(value) - 1)))

        rows.append("</div>")
        rows.append(f'<div class="json-end">]{comma_text}</div>')
        rows.append("</details>")

        return "\n".join(rows)

    primitive = html_escape(json.dumps(value))

    if label:
        return f'<div class="json-line"><span class="json-key">"{html_escape(label)}"</span>: <span class="json-value">{primitive}</span>{comma_text}</div>'

    return f'<div class="json-line"><span class="json-value">{primitive}</span>{comma_text}</div>'


def clipped_cell(content_html, title_text="", cell_class=""):
    return (
        f'<td class="{cell_class}" title="{html_escape(title_text)}">'
        '<details class="cell-details">'
        '<summary>'
        f'<span>{content_html}</span>'
        '</summary>'
        '</details>'
        '</td>'
    )


def render_class_table(class_name, class_def, schema):
    rows = []
    slot_usage = class_def.get("slot_usage", {})

    for slot in class_def.get("slots", []):
        slot_def = schema.get("slots", {}).get(slot, {})
        usage_def = slot_usage.get(slot, {})
        subsets = usage_def.get("in_subset", ["base"])
        slot_range = slot_def.get("range", "")
        description = slot_def.get("description", "")

        if slot_range in schema.get("enums", {}):
            range_html = render_enum_button(slot_range)
        else:
            range_html = f'<code class="primitive-range">{html_escape(slot_range)}</code>' if slot_range else ""

        rows.append(
            f'<tr{subset_attr(subsets)}>'
            f'{clipped_cell(html_escape(slot), slot, "slot-name")}'
            f'{clipped_cell(html_escape(description), description, "slot-description")}'
            f'<td class="slot-range" title="{html_escape(slot_range)}"><span>{range_html}</span></td>'
            '</tr>'
        )

    return (
        '<table class="model-table class-slot-table">'
        '<thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead>'
        '<tbody>'
        + "\n".join(rows)
        + '</tbody>'
        '</table>'
    )


def render_domain_intro(domain, schema):
    docs = schema.get("annotations", {}).get("docs", {})
    domain_docs = docs.get("domains", {}).get(domain, {})
    title = domain_docs.get("title", domain.title())
    description = domain_docs.get("description", "")
    icon = DOMAIN_ICONS.get(domain, "")

    parts = [f'<div class="domain-banner domain-{safe_id(domain)}">']

    if icon:
        parts.append(f'<div class="domain-icon">{icon}</div>')

    parts.append('<div class="domain-banner-text">')
    parts.append(f'<div class="domain-heading">{html_escape(title)}</div>')

    if description:
        parts.append(f'<p class="domain-description">{html_escape(description)}</p>')

    parts.append('</div>')
    parts.append('</div>')

    return "\n".join(parts)


def render_domain_sections(schema):
    domains = {}

    for class_name, class_def in schema.get("classes", {}).items():
        domain = class_def.get("annotations", {}).get("domain")
        if isinstance(domain, dict):
            domain = domain.get("value")
        if not domain:
            raise ValueError(f"Class is missing required domain annotation: {class_name}")
        if domain not in domains:
            domains[domain] = []
        domains[domain].append((class_name, class_def))

    comps = []

    for domain in domains.keys():
        if domain == "internal":
            continue 
        domain_id = "domain-" + safe_id(domain)
        comps.append(f'<section id="{domain_id}" class="domain-section" data-domain="{safe_id(domain)}" markdown="1">')
        comps.append(render_domain_intro(domain, schema))

        for class_name, class_def in domains[domain]:
            comps.append(render_class_section(class_name, class_def, schema))

        comps.append("</section>")

    return "\n\n".join(comps)


def render_raw_schema_payload(schema):
    raw_schemas = {}

    for subset in schema["subsets"].keys():
        raw_schemas[subset] = filter_schema_by_subset(schema, subset)

    raw = json.dumps(raw_schemas)
    raw = raw.replace("</", "<\\/")

    return f'<script id="raw-schema-payload" type="application/json">{raw}</script>'


def render_view_metadata_payload(schema):
    view_metadata = {}

    for subset, subset_def in schema.get("subsets", {}).items():
        view_metadata[subset] = {
            "title": subset_def.get("title", subset),
            "name": subset_def.get("name", subset),
            "description": subset_def.get("description", "")
        }

    raw = json.dumps(view_metadata)
    raw = raw.replace("</", "<\\/")

    return f'<script id="view-metadata-payload" type="application/json">{raw}</script>'


def version_sort_key(value):
    return tuple(int(part) if part.isdigit() else part for part in str(value).split("."))

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
            "notes": ""
        })

    releases.sort(key=lambda r: version_sort_key(r["version"]), reverse=True)
    return releases


def render_model(schema):
    comps = []
    comps.append('<div id="model-loading" class="raw-loading" style="display:none;">Loading…</div>')

    comps.append('<div id="docs-model-view" markdown="1">')
    comps.append('<div class="model-main" markdown="1">')
    comps.append(render_domain_sections(schema))
    comps.append(render_enum_modals(schema))
    comps.append("</div>")
    comps.append("</div>")

    comps.append(render_model_toc(schema))

    comps.append('<div id="raw-model-view" style="display:none;" markdown="1">')
    comps.append('<div id="raw-loading" class="raw-loading" style="display:none;">Loading raw schema…</div>')
    comps.append('<div id="raw-schema-renderer" class="json-renderer"></div>')
    comps.append("</div>")

    comps.append(render_view_metadata_payload(schema))
    comps.append(render_raw_schema_payload(schema))

    return "\n\n".join([c for c in comps if c])


def assemble_view(schema, notes, commons, page_context):
    view_comps = []
    view_comps.append(init_view_front_matter(schema, commons, page_context))

    view_comps.append('<div class="model-header" markdown="1">')
    view_comps.append(render_view_header(schema, notes))
    view_comps.append(
        '<details class="scope-matrix-details">\n'
        '<summary class="text-delta">Scope Matrix</summary>\n\n'
        + render_view_matrix(schema) +
        '\n\n</details>'
    )
    view_comps.append(render_view_mode_toggle())
    view_comps.append("</div>")

    view_comps.append(render_model(schema))

    return "\n\n".join([c for c in view_comps if c])


def main(commons, schema_path, notes_path):
    schema = load_json(schema_path, required=True)
    notes = load_json(notes_path, required=False)
    version = str(schema["version"])
    commons_folder = COMMONS[commons]["folder"]
    pages = []

    current_view = assemble_view(schema, notes, commons, "current")
    release_view = assemble_view(schema, notes, commons, "release")

    pages.append((Path(f"{commons_folder}/index.md"), current_view))
    pages.append((Path(f"{commons_folder}/releases/{version}/index.md"), release_view))

    releases = discover_releases(commons_folder, version)

    if not any(r["version"] == version for r in releases):
        releases.append({
            "version": version,
            "status": "Current",
            "url": f"./{version}/",
            "date": "",
            "notes": ""
        })

    releases.sort(key=lambda r: version_sort_key(r["version"]), reverse=True)

    pages.insert(
        0,
        (Path(f"{commons_folder}/releases/index.md"), render_release_archive(commons, releases))
    )

    for path, markdown in pages:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate static D4CG Data Model docs site.")
    parser.add_argument("--commons", required=True, choices=COMMONS.keys(), help="Commons to generate: pcdc or predict.")
    parser.add_argument("--schema", required=True, help="Path to LinkML schema JSON.")
    parser.add_argument("--change_notes", required=False, help="Path to a simple JSON change notes file.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate an existing release folder.")
    args = parser.parse_args()

    commons = args.commons
    schema_path = Path(args.schema)
    notes_path = Path(args.change_notes) if args.change_notes else None

    main(commons, schema_path, notes_path)