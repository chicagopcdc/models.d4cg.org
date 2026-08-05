# models.d4cg.org

This repository contains the source files and generated content for the D4CG data model documentation website.

The site is built with Jekyll and the Just the Docs theme. Model reference pages are generated from LinkML schemas and published through GitHub Pages.

## Repository Structure

```text
assets/
    Images and other static website assets

documentation/
    D4CG-wide modeling and implementation guidance

pcdc/
    Pediatric Oncology model documentation and releases

predict/
    Monogenic Diabetes model documentation and releases

scripts/
    Release-generation and maintenance scripts
```

Each model is organized into current and archived releases. For example:

```text
pcdc/
├── index.md
└── releases/
    ├── index.md
    └── 2.0/
        ├── views/
        │   └── ...
        ├── index.md
        ├── manifest.json
        └── schema.json
```

Within a release:

- `schema.json` contains the released LinkML schema.
- `manifest.json` contains release metadata.
- `index.md` contains the generated model reference page.
- `views/` contains generated reference pages for model subsets or views.

The model-level `index.md` always represents the current release, while prior versions remain available under `releases/`.

## Generating a Release

See [`RELEASING.md`](RELEASING.md) for the quarterly release process.