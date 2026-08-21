# models.d4cg.org

This repository contains the source files and generated content for the D4CG data model documentation website.

The site is built with Jekyll and the Just the Docs theme. Model reference pages are generated from LinkML schemas and published through GitHub Pages.

## Creating a New Release

1. Create a new folder in the releases folder of the data commons:

   `/{commons}/releases/{version}`

2. Initialize the release with a `model` folder containing the LinkML source files and a `change_notes.yaml` file:

   ```text
   /{commons}/releases/{version}/
   ├── model/
   │   ├── schema.yaml
   │   ├── slots.yaml
   │   ├── enums.yaml
   │   └── terminology.yaml
   └── change_notes.yaml
   ```

3. Updates to this version of the schema should be made via feature branches and pull requests.

    Detailed changes are tracked by Git, but user-facing summaries should also be recorded in  `change_notes.yaml` in order to justify and present changes each quarter to stakeholders:

   ```yaml
   release_date: 2026-10-01 
   changes:
     - Used "Present/Absent" instead of "Positive/Negative" for the presence of alterations in GeneticAnalysis.
     - Combined procedures into either resection and reconstruction groups.
   ```

4. To initialize or update the model site, run:

   ```bash
   python scripts/generate_docs.py {commons}/releases/{version}/model
   ```

   This will generate the documentation for the release. Review the generated site locally, then commit and push the generated files via pull request.

## Running Locally

The documentation site is built with Jekyll.

From the repository root, install the dependencies if needed:

```bash
bundle install
```

Then start the local site:

```bash
bundle exec jekyll serve --port 4000
```

The site will be available at:

http://localhost:4000

Jekyll will watch the repository for changes and rebuild the site while the local server is running.

## Exports

Data dictionaries can be exported to Google Sheets using `scripts/export.py`.

Run the exporter from the repository root:

```bash
python scripts/export.py {model_dir} {subset}
```

For example:

```bash
python scripts/export.py pcdc/releases/2.0/model fprh
```

The directory passed to the script must contain:

```text
schema.yaml
slots.yaml
enums.yaml
terminology.yaml
```

Exports are written to the shared [D4CG model export folder](https://drive.google.com/drive/folders/15MY_hV4Jz1KSmYT2tgLVr-meaDuvfAvj?usp=drive_link).



The exporter creates a new Google Spreadsheet, with formatting drawn from a [standard formatting template](https://docs.google.com/spreadsheets/d/1UDTMiw0LnLwqUBNc4O2_FAAX5UylCy-VXXRxEojK4IA/edit).



### Exports Are Temporary Artifacts

Exported spreadsheets are derived artifacts for modeling workflows. They are **not sources of truth.**

Modeling work may temporarily occur in an exported spreadsheet when that is useful for collaboration, but any resulting model changes should be translated into the LinkML source, recorded in `change_notes.yaml`, and submitted through a pull request as quickly as possible.