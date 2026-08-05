---
layout: default
title: Home
nav_order: 1
---

# Data for the Common Good (D4CG)

[Data for the Common Good (D4CG)](https://commons.cri.uchicago.edu/) is dedicated to building communities, platforms, and ecosystems that maximize the potential of data to drive discovery and improve human health. Headquartered in the Department of Pediatrics at the University of Chicago, our team of experts works with collaborators all over the world to connect and share useful, high-quality data between institutions, groups, and countries to increase opportunities for discovery.

## Data Models

<div class="model-card-grid">

<a class="model-card" href="pcdc/">
  <div class="model-card-kicker">Pediatric Oncology</div>
  <div class="model-card-title">PCDC Data Model</div>
  <p>The Pediatric Cancer Data Commons (PCDC) offers a harmonized collection of pediatric, AYA, and adult cancer clinical data from around the world for researchers to explore and access.</p>
  <div class="model-card-action">Explore model →</div>
</a>

<a class="model-card" href="predict/">
  <div class="model-card-kicker">Precision Diabetes</div>
  <div class="model-card-title">PREDICT Data Model</div>
  <p>The Precision Diabetes Consortium (PREDICT) data commons offers a harmonized collection of monogenic diabetes clinical data for research and discovery.</p>
  <div class="model-card-action">Explore model →</div>
</a>

</div>

## Consensus Modeling

D4CG modeling benefits from the collective expertise of dozens of the world's leading clinical researchers. Since each D4CG data commons consists of line-level harmonized data, modeling strategy and decision-making is shared across all data contributors. This ensures thaat the resulting fields are gold-standard international representations of the most relevant areas of clinical oncology.


## About LinkML

D4CG models are authored using [LinkML (Linked Data Modeling Language)](https://linkml.io/).

LinkML organizes a model into a small set of core concepts:

- **Classes** represent real-world entities or concepts.
- **Slots** represent attributes associated with those entities.
- **Enums** define controlled vocabularies and permissible values for enumerated slots (e.g., not string-based, integer-based, etc.).

### Why a Computable Model?

Through the [LinkML Generator Framework](https://linkml.io/linkml/generators/index.html), any D4CG model can be transformed into numerous implementation artifacts while remaining synchronized with the underlying specification.

### Example Applications

| Category | Example Artifacts |
|-----------|------------------|
| Schema Frameworks | JSON Schema, GraphQL, Protocol Buffers |
| Linked Data | RDF, OWL, SHACL, ShEx, JSON-LD, SPARQL, YARRRML |
| Code Generation | Python, Pydantic, TypeScript, Java, Rust |
| Databases | SQL DDL, SQLAlchemy, TypeDB |
| Documentation | Searchable Documentation, ER Diagrams, Excel / CSV Templates |

This enables a single source-of-truth model to support data validation, software development, database implementation, semantic interoperability, data exchange, and documentation workflows.


### For More Information
Please see our [Documentation](./documentation/) page.