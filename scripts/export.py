import argparse
import datetime
import pickle
from pathlib import Path

import yaml
from googleapiclient.discovery import build


AUTH_DIR = Path(__file__).resolve().parent / "auth"
TOKEN_PATH = AUTH_DIR / "token-sheets.pickle"
FORMAT_SHEET_ID = "1UDTMiw0LnLwqUBNc4O2_FAAX5UylCy-VXXRxEojK4IA"
EXPORT_FOLDER_ID = "15MY_hV4Jz1KSmYT2tgLVr-meaDuvfAvj"
DICTIONARY_SHEET_NAME = "Data Dictionary"


def load_yaml(path):
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")

    with open(path, "r", encoding="utf-8") as file_in:
        return yaml.safe_load(file_in) or {}


def load_model(model_dir):
    schema = load_yaml(model_dir / "schema.yaml")
    slots = load_yaml(model_dir / "slots.yaml").get("slots", {})
    enums = load_yaml(model_dir / "enums.yaml").get("enums", {})
    terminology = load_yaml(model_dir / "terminology.yaml")

    return schema, slots, enums, terminology


def annotation_value(item_def, name, default=None):
    value = item_def.get("annotations", {}).get(name, default)

    if isinstance(value, dict) and "value" in value:
        return value["value"]

    return value


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

    for source_def in terminology.values():
        if not isinstance(source_def, dict):
            continue

        for curie, concept_def in source_def.get("concepts", {}).items():
            if not isinstance(concept_def, dict):
                continue

            index[normalize_curie(curie)] = concept_def

    return index


def get_description(meaning, terminology_index):
    if not meaning:
        return ""

    concept_def = terminology_index.get(normalize_curie(meaning), {})

    return concept_def.get("description", "")


def get_notes(item_def):
    comments = item_def.get("comments", [])

    if not comments:
        return ""

    if not isinstance(comments, list):
        comments = [comments]

    return "\n".join(str(comment) for comment in comments)


def get_cardinality(class_def):
    cardinality = annotation_value(class_def, "cardinality", "")

    if cardinality is None:
        return ""

    return str(cardinality)


def get_priority_subsets(usage_def):
    priority = annotation_value(usage_def, "priority", [])

    if priority is None:
        return []

    if not isinstance(priority, list):
        priority = [priority]

    return [str(subset) for subset in priority]


def get_tier(usage_def, subset):
    if usage_def.get("required") is True:
        return "required"

    if subset != "base" and subset in get_priority_subsets(usage_def):
        return "priority"

    return "optional"


def get_data_type(slot_def, enums):
    slot_range = slot_def.get("range", "")

    if slot_range in enums:
        return "enum"

    return slot_range


def class_in_view(class_def, subset):
    if subset == "base":
        return True

    return subset in class_def.get("in_subset", [])


def slot_in_view(class_def, slot_name, subset):
    if subset == "base":
        return True

    usage_def = class_def.get("slot_usage", {}).get(slot_name, {})

    return subset in usage_def.get("in_subset", [])


def pv_in_view(pv_def, subset):
    if subset == "base":
        return True

    return subset in pv_def.get("in_subset", [])


def class_is_internal(class_def):
    domain = annotation_value(class_def, "domain", "")

    return str(domain).lower() == "internal"


def get_subset_title(schema, subset):
    subset_def = schema.get("subsets", {}).get(subset, {})

    return subset_def.get("title", subset_def.get("name", subset))


def assemble_dictionary(schema, slots, enums, terminology_index, subset):

    rows = [
        ["info", "Title", schema.get("title", schema.get("name", "")), "", "", "", "", ""],
        ["info", "Subset", get_subset_title(schema, subset), "", "", "", "", "", ""],
        ["info", "Version", schema.get("version", ""), "", "", "", "", "", ""],
        ["info", "License", "CC BY-NC 4.0", "", "", "", "", "", ""],
        ["info", "Export Date", datetime.date.today().isoformat(), "", "", "", "", "", ""],
        [],
        ["RowType", "Name", "Data Type", "Cardinality/Tier", "Permissible Value", "Meaning", "Description", "Implementation Notes"],
    ]
   
    first_class = True
    current_domain = ""

    for class_name, class_def in schema.get("classes", {}).items():
        if not class_in_view(class_def, subset):
            continue

        if class_is_internal(class_def):
            continue

        class_slots = []

        for slot_name in class_def.get("slots", []):
            if slot_in_view(class_def, slot_name, subset):
                class_slots.append(slot_name)

        if not class_slots:
            continue

        if not first_class:
            rows.append([])

        first_class = False

        domain = annotation_value(class_def, "domain", "")

        if domain and domain != current_domain:
            rows.append(["domain", str(domain), "", "", "", "", "", ""])
            current_domain = domain

        rows.append([
            "class",
            class_name,
            "class",
            get_cardinality(class_def),
            "",
            "",
            class_def.get("description", ""),
            get_notes(class_def),
        ])

        slot_usage = class_def.get("slot_usage", {})

        for slot_name in class_slots:
            slot_def = slots.get(slot_name)

            if slot_def is None:
                raise ValueError(
                    f"Slot is used by {class_name} but missing from slots.yaml: {slot_name}"
                )

            usage_def = slot_usage.get(slot_name, {})
            slot_range = slot_def.get("range", "")
            meaning = slot_def.get("slot_uri", "")

            rows.append([
                "slot",
                slot_name,
                get_data_type(slot_def, enums),
                get_tier(usage_def, subset),
                "",
                meaning,
                get_description(meaning, terminology_index),
                get_notes(slot_def),
            ])

            enum_def = enums.get(slot_range)

            if not enum_def:
                continue

            for pv_name, pv_def in enum_def.get("permissible_values", {}).items():
                if not pv_in_view(pv_def, subset):
                    continue

                pv_meaning = pv_def.get("meaning", "")

                rows.append([
                    "pv",
                    "",
                    "",
                    "",
                    pv_name,
                    pv_meaning,
                    get_description(pv_meaning, terminology_index),
                    get_notes(pv_def),
                ])

    return rows


def get_credentials():
    if not TOKEN_PATH.exists():
        raise FileNotFoundError(f"Google token not found: {TOKEN_PATH}")

    with open(TOKEN_PATH, "rb") as file_in:
        return pickle.load(file_in)


def get_services():
    credentials = get_credentials()

    sheets_service = build(
        "sheets",
        "v4",
        credentials=credentials,
    )

    drive_service = build(
        "drive",
        "v3",
        credentials=credentials,
    )

    return sheets_service, drive_service


def escape_drive_query(value):
    return str(value).replace("\\", "\\\\").replace("'", "\\'")


def delete_existing_export(drive_service, title):
    query_title = escape_drive_query(title)

    query = (
        f"name = '{query_title}' and "
        f"'{EXPORT_FOLDER_ID}' in parents and "
        "mimeType = 'application/vnd.google-apps.spreadsheet' and "
        "trashed = false"
    )

    response = drive_service.files().list(
        q=query,
        fields="files(id, name)",
        corpora="allDrives",
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
    ).execute()

    for file in response.get("files", []):
        print(f"...trashing existing export: {file['name']}")

        drive_service.files().update(
            fileId=file["id"],
            body={"trashed": True},
            fields="id, trashed",
            supportsAllDrives=True,
        ).execute()


def create_spreadsheet(sheets_service, title):
    response = sheets_service.spreadsheets().create(
        body={
            "properties": {
                "title": title
            }
        }
    ).execute()

    spreadsheet_id = response["spreadsheetId"]
    default_sheet_id = response["sheets"][0]["properties"]["sheetId"]

    return spreadsheet_id, default_sheet_id


def move_spreadsheet_to_export_folder(drive_service, spreadsheet_id):
    metadata = drive_service.files().get(
        fileId=spreadsheet_id,
        fields="parents",
        supportsAllDrives=True,
    ).execute()

    previous_parents = ",".join(metadata.get("parents", []))

    request = {
        "fileId": spreadsheet_id,
        "addParents": EXPORT_FOLDER_ID,
        "fields": "id, parents",
        "supportsAllDrives": True,
    }

    if previous_parents:
        request["removeParents"] = previous_parents

    drive_service.files().update(**request).execute()


def get_formatting_sheet_id(sheets_service):
    source_meta = sheets_service.spreadsheets().get(
        spreadsheetId=FORMAT_SHEET_ID
    ).execute()

    for sheet in source_meta.get("sheets", []):
        properties = sheet.get("properties", {})

        if properties.get("title") == "FORMATTING":
            return properties["sheetId"]

    raise ValueError(
        f"Template sheet 'FORMATTING' not found in spreadsheet {FORMAT_SHEET_ID}"
    )


def copy_formatting(sheets_service, spreadsheet_id):
    formatting_sheet_id = get_formatting_sheet_id(sheets_service)

    response = sheets_service.spreadsheets().sheets().copyTo(
        spreadsheetId=FORMAT_SHEET_ID,
        sheetId=formatting_sheet_id,
        body={
            "destinationSpreadsheetId": spreadsheet_id
        },
    ).execute()

    return response["sheetId"]


def prepare_dictionary_sheet(sheets_service, spreadsheet_id, default_sheet_id):
    sheet_id = copy_formatting(
        sheets_service,
        spreadsheet_id,
    )

    requests = [
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "title": DICTIONARY_SHEET_NAME,
                    "index": 0,
                },
                "fields": "title,index",
            }
        },
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "TEXT"
                        }
                    }
                },
                "fields": "userEnteredFormat.numberFormat",
            }
        },
        {
            "deleteSheet": {
                "sheetId": default_sheet_id
            }
        },
    ]

    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "requests": requests
        },
    ).execute()

    # Clear values only. Formatting inherited from the template remains.
    sheets_service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=f"'{DICTIONARY_SHEET_NAME}'",
        body={},
    ).execute()


def write_rows(sheets_service, spreadsheet_id, rows):
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"'{DICTIONARY_SHEET_NAME}'!A1",
        valueInputOption="RAW",
        body={
            "values": rows
        },
    ).execute()


def get_export_title(schema, subset):
    model_title = schema.get(
        "title",
        schema.get("name", "D4CG Data Model"),
    )

    version = schema.get("version", "")
    subset_title = get_subset_title(schema, subset)
    export_date = datetime.datetime.now().strftime("%Y%m%d")

    title = f"{export_date} {model_title}"

    if version:
        title += f" {version}"

    title += f" - {subset_title}"

    return title


def export(model_dir, subset):
    model_dir = Path(model_dir)

    schema, slots, enums, terminology = load_model(model_dir)

    if subset not in schema.get("subsets", {}):
        raise ValueError(
            f"Subset is not defined in schema.yaml: {subset}"
        )

    terminology_index = build_terminology_index(terminology)

    rows = assemble_dictionary(
        schema,
        slots,
        enums,
        terminology_index,
        subset,
    )

    title = get_export_title(
        schema,
        subset,
    )

    sheets_service, drive_service = get_services()

    print(f"Exporting: {get_subset_title(schema, subset)}")
    print(f"Version: {schema.get('version', '')}")
    print(f"Rows: {len(rows)}")

    delete_existing_export(
        drive_service,
        title,
    )

    print("...creating spreadsheet")

    spreadsheet_id, default_sheet_id = create_spreadsheet(
        sheets_service,
        title,
    )

    print("...copying formatting template")

    prepare_dictionary_sheet(
        sheets_service,
        spreadsheet_id,
        default_sheet_id,
    )

    print("...writing data dictionary")

    write_rows(
        sheets_service,
        spreadsheet_id,
        rows,
    )

    print("...moving spreadsheet to export folder")

    move_spreadsheet_to_export_folder(
        drive_service,
        spreadsheet_id,
    )

    print(
        f"...complete: https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
    )


if __name__ == "__main__":
    print(
        r"""
    ▛▀▖▞▀▖▙▗▌   ▛▀▘▌ ▌▛▀▖▞▀▖▛▀▖▀▛▘
    ▌ ▌▚▄ ▌▘▌▄▄▖▙▄ ▝▞ ▙▄▘▌ ▌▙▄▘ ▌
    ▌ ▌▖ ▌▌ ▌   ▌  ▞▝▖▌  ▌ ▌▌▚  ▌
    ▀▀ ▝▀ ▘ ▘   ▀▀▘▘ ▘▘  ▝▀ ▘ ▘ ▘

    D4CG DATA MODEL EXPORT
    ______________________________________________
    """
    )

    parser = argparse.ArgumentParser(
        description="Export a D4CG model subset to Google Sheets."
    )

    parser = argparse.ArgumentParser(
        description="Export a D4CG model subset to Google Sheets."
    )

    parser.add_argument(
        "model_dir",
        help=(
            "Directory containing schema.yaml, slots.yaml, "
            "enums.yaml, and terminology.yaml."
        ),
    )

    parser.add_argument(
        "subset",
        help="Subset/view to export, for example base, aml, or fprh.",
    )

    args = parser.parse_args()

    export(
        args.model_dir,
        args.subset,
    )