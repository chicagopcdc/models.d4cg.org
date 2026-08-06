---
layout: default
title: Liver Tumors
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*LT View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- [Central Nervous System Tumors](cns)
- [Ewing Sarcoma](ews)
- [Fanconi Anemia](fa)
- [Fertility Preservation and Reproductive Health](fprh)
- [Germ Cell Tumors](gct)
- [Hodgkin Lymphoma](hl)
- [Lynch Syndrome](ls)
- **Liver Tumors**
- [Neuroblastoma](nbl)
- [Nasopharyngeal Carcinoma](npc)
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The LT view of the PCDC data model represents consensus data modeling by an international group of pediatric liver tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Children's Hepatic Tumors International Collaboration (CHIC). It is based on the collective requirements of its contributors.


<div class="view-mode-toggle">
  <span class="toggle-label">Docs</span>
  <label class="switch">
    <input type="checkbox" onchange="
      document.getElementById('docs-model-view').style.display = this.checked ? 'none' : 'block';
      document.getElementById('raw-model-view').style.display = this.checked ? 'block' : 'none';
    ">
    <span class="slider"></span>
  </label>
  <span class="toggle-label">Raw</span>
</div>


<div id="docs-model-view" markdown="1">

<div class="domain-heading">Demographics</div>

## ClinicalEpisode

| Slot | Range | Description |
|---|---|---|
| `disease_phase` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasephaseenum')">DiseasePhaseEnum</button> |  |
| `course` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-courseenum')">CourseEnum</button> |  |
| `age_at_start` | `integer` |  |
| `year_at_start` | `integer` |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `age_at_condition` | `integer` |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |
| `condition_other` | `string` |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |
| `data_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-datasourceenum')">DataSourceEnum</button> |  |
| `urls` | `string` |  |

## Subject

| Slot | Range | Description |
|---|---|---|
| `consortium` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-consortiumenum')">ConsortiumEnum</button> |  |
| `disease_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasegroupenum')">DiseaseGroupEnum</button> |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `diagnosis_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosiscategoryenum')">DiagnosisCategoryEnum</button> |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histologic_features` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologicfeaturesenum')">HistologicFeaturesEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage_system_version` | `string` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |
| `pretext_mod_v` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `pretext_mod_p` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `pretext_mod_e` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `pretext_mod_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `pretext_mod_f` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `pretext_mod_r` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `cycles_planned` | `decimal` |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `smn_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smntypeenum')">SmnTypeEnum</button> |  |
| `morph_code` | `string` |  |
| `morph_code_text` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `morph_code_system_version` | `string` |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |

<div class="domain-heading">Testing</div>

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |

<div id="enum-modal-adverseeventenum" class="enum-modal" onclick="closeEnumModal('enum-modal-adverseeventenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-adverseeventenum')">×</button>
<h3><code>AdverseEventEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ototoxicity</code></td><td><code>ncit:C66929</code></td><td></td></tr>
<tr><td><code>Surgical Complications, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Surgical Death within 30 days</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-causeofdeathenum" class="enum-modal" onclick="closeEnumModal('enum-modal-causeofdeathenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-causeofdeathenum')">×</button>
<h3><code>CauseOfDeathEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Disease Progression</code></td><td><code>ncit:C168970</code></td><td>(cns) ConsortiumNote: Deceased-due to disease.<br>(fa) ConsortiumNote: Cancer-related disease progression. Deceased-due to disease.<br>(gct) ConsortiumNote: If multiple causes of death, include one observation per cause of death.<br>(hl) ConsortiumNote: If multiple causes of death, include one observation per cause of death.<br>(nrsts) ConsortiumNote: If multiple causes of death, include one observation per cause of death. There can only be one record where CAUSE_OF_DEATH_RANKING=Primary.<br>(os) ConsortiumNote: If multiple causes of death, include one observation per cause of death. However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary. Note: Only fill in this variable if LKSS is 'Dead'.<br>(rms) ConsortiumNote: If multiple causes of death, include one observation per cause of death.  However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary.</td></tr>
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(cns) ConsortiumNote: Deceased-causes unavailable.<br>(fa) ConsortiumNote: Deceased-causes unavailable.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-consortiumenum" class="enum-modal" onclick="closeEnumModal('enum-modal-consortiumenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-consortiumenum')">×</button>
<h3><code>ConsortiumEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CHIC</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-courseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-courseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-courseenum')">×</button>
<h3><code>CourseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Postoperative Chemotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Preoperative Chemotherapy</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-datasourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-datasourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-datasourceenum')">×</button>
<h3><code>DataSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Registry</code></td><td><code>ncit:C129000</code></td><td>(npc) ConsortiumNotes: For TROD, use Registry only.</td></tr>
<tr><td><code>Therapeutic Trial</code></td><td><code>ncit:C39536</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diagnosisbasisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosisbasisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosisbasisenum')">×</button>
<h3><code>DiagnosisBasisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Histological</code></td><td><code>ncit:C25526</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diagnosiscategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosiscategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosiscategoryenum')">×</button>
<h3><code>DiagnosisCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fibrolamellar carcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic Tumor, Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatoblastoma (HB)</code></td><td><code>ncit:C3728</code></td><td></td></tr>
<tr><td><code>Hepatocelluar Carcinoma (HCC)</code></td><td><code>ncit:C3099</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diagnosisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosisenum')">×</button>
<h3><code>DiagnosisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cholangiocarcinoma</code></td><td><code>icdo:8160/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Combined hepatocellular-cholangiocarcinoma</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Epithelial, Cholangioblastic</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Embryonal</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Epithelial mixed</code></td><td><code></code></td><td>(lt) ConsortiumNote: Retrospective only</td></tr>
<tr><td><code>Epithelial, Fetal, crowded, mitotically active</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Fetal, well-differentiated, mitotically inactive</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Glandular</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Macrotrabecular</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Pleomorphic, poorly differentiated</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Primitive, small cell undifferentiated or blastemal</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Pure Fetal, well-differentiated, mitotically inactive</code></td><td><code></code></td><td>(lt) ConsortiumNote: Examination of whole tumor is required for this diagnosis.<br>(lt) ConsortiumNote:  Note: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Epithelial, Squamous</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Hepatocellular adenoma (expand?)</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Hepatocellular carcinoma, associated with hepatocellular adenoma</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'</td></tr>
<tr><td><code>Hepatocellular carcinoma, associated with hepatocellular adenoma, with underlying liver disease</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'</td></tr>
<tr><td><code>Hepatocellular carcinoma, classic</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'</td></tr>
<tr><td><code>Hepatocellular carcinoma, classic, with underlying liver disease</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'</td></tr>
<tr><td><code>Hepatocellular carcinoma, fibrolamellar</code></td><td><code>icdo:8171/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular malignancy, NOS</code></td><td><code></code></td><td>(lt) ConsortiumNote: Includes transitional cell liver tumor. DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Malignant hepatocellular neoplasm, NOS, with carcinoma features</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Malignant rhabdoid tumor</code></td><td><code>icdo:8963/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Mesenchymal hamartoma</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Cholangioblastic</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Embryonal</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Fetal, crowded, mitotically active</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Fetal, well-differentiated, mitotically inactive</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Glandular</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Macrotrabecular</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Mesenchymal, non-teratoid</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Pleomorphic, poorly differentiated</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Primitive (small cell undifferentiated or blastemal)</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, Squamous</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, with teratoid features</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'</td></tr>
<tr><td><code>Mixed epithelial-mesenchymal, without teratoid features</code></td><td><code></code></td><td>(lt) ConsortiumNote: Retrospective only</td></tr>
<tr><td><code>Nested stromal-epithelial tumor</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Undifferentiated embryonal sarcoma</code></td><td><code></code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diseasegroupenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diseasegroupenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diseasegroupenum')">×</button>
<h3><code>DiseaseGroupEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>LT</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diseasephaseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diseasephaseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diseasephaseenum')">×</button>
<h3><code>DiseasePhaseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Initial Diagnosis</code></td><td><code>ncit:C156813</code></td><td>(gct) ConsortiumNote: Disease phase could be 'Initial Diagnosis' phase, 'Relapse' phase, etc...<br>(hl) ConsortiumNote: Disease phase could be 'Initial Diagnosis' phase, a 'Relapse' phase, etc...</td></tr>
<tr><td><code>Progression</code></td><td><code>ncit:C17747</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diseasesiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diseasesiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diseasesiteenum')">×</button>
<h3><code>DiseaseSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-histologicfeaturesenum" class="enum-modal" onclick="closeEnumModal('enum-modal-histologicfeaturesenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-histologicfeaturesenum')">×</button>
<h3><code>HistologicFeaturesEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Teratoid Feature, Melanin-producing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Teratoid Feature, Neuroendocrine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Teratoid Feature, Neuroepithelial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Teratoid Feature, Other e.g., Yolk sac tumor-like</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laboratorytestenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorytestenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorytestenum')">×</button>
<h3><code>LaboratoryTestEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>AFP</code></td><td><code>ncit:C21577</code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laboratorytestresultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorytestresultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorytestresultunitenum')">×</button>
<h3><code>LaboratoryTestResultUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>count/mm3</code></td><td><code>ncit:C173275</code></td><td></td></tr>
<tr><td><code>ng/mL</code></td><td><code>ncit:C67306</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lateralityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lateralityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lateralityenum')">×</button>
<h3><code>LateralityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Left</code></td><td><code>ncit:C160200</code></td><td></td></tr>
<tr><td><code>Right</code></td><td><code>ncit:C160199</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lkssenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lkssenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lkssenum')">×</button>
<h3><code>LkssEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alive</code></td><td><code>ncit:C37987</code></td><td></td></tr>
<tr><td><code>Dead</code></td><td><code>ncit:C28554</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-marginsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-marginsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-marginsenum')">×</button>
<h3><code>MarginsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Biopsy Only</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>No Viable Tumor Identified</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No lung metastases remain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R0 - Complete Resection, Negative Margins</code></td><td><code>ncit:C139578</code></td><td>(lt) ConsortiumNote: sub-procedures have no margins, only the multi-focal procedures</td></tr>
<tr><td><code>R1 - Complete Resection, Positive Margins</code></td><td><code>ncit:C139579</code></td><td></td></tr>
<tr><td><code>R2 - Gross Residual Disease</code></td><td><code>ncit:C139580</code></td><td></td></tr>
<tr><td><code>Some lung metastases remain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unresectable</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3><code>MedicalHistoryConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia</code></td><td><code>ncit:C34415</code></td><td></td></tr>
<tr><td><code>Familial Adenomatous Polyposis</code></td><td><code>ncit:C3339</code></td><td></td></tr>
<tr><td><code>Hemihypertrophy</code></td><td><code>ncit:C88541</code></td><td></td></tr>
<tr><td><code>Low Birth Weight</code></td><td><code>ncit:C34724</code></td><td></td></tr>
<tr><td><code>Preterm Birth</code></td><td><code>ncit:92861</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-medicationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationenum')">×</button>
<h3><code>MedicationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ALRN 6924</code></td><td><code>ncit:C118669</code></td><td></td></tr>
<tr><td><code>Anti-AFP CART</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anti-GPC3 CART</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Atezolizumab</code></td><td><code>ncit:C106250</code></td><td></td></tr>
<tr><td><code>Azathioprine</code></td><td><code>rxcui:1256</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Bevacizumab</code></td><td><code>rxcui:253337</code></td><td></td></tr>
<tr><td><code>Bortezomib</code></td><td><code>ncit:C1851</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Cabozantinib</code></td><td><code>ncit:C52200</code></td><td></td></tr>
<tr><td><code>Capecitabine</code></td><td><code>rxcui:194000</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cellcept (MMF)</code></td><td><code>ncit:C1468</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Codrituzumab</code></td><td><code>ncit:C80043</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cyclosporine</code></td><td><code>rxcui:3008</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>DNAJB1-PRKACA Vaccine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DT 2216</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dendritic Cell Therapy</code></td><td><code>ncit:C28976</code></td><td></td></tr>
<tr><td><code>Dexrazoxane</code></td><td><code>ncit:C1333</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Durvalumab</code></td><td><code>ncit:C103194</code></td><td></td></tr>
<tr><td><code>ENMD 2076</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Erlotinib</code></td><td><code>ncit:C65530</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Etoposide Phosphate</code></td><td><code>ncit:C1093</code></td><td></td></tr>
<tr><td><code>Everolimus</code></td><td><code>rxcui:141704</code></td><td></td></tr>
<tr><td><code>Fluorouracil (5FU)</code></td><td><code>rxcui:4492</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Indocyanine green</code></td><td><code></code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Pre-surgical Medication</td></tr>
<tr><td><code>Interferon</code></td><td><code>ncit:C20493</code></td><td></td></tr>
<tr><td><code>Ipililumab</code></td><td><code>ncit:C2654</code></td><td></td></tr>
<tr><td><code>Irinotecan</code></td><td><code>ncit:C62040</code></td><td></td></tr>
<tr><td><code>Lenvatinib</code></td><td><code>rxcui:1603296</code></td><td></td></tr>
<tr><td><code>Leuprolide Acetate</code></td><td><code>rxcui:203217</code></td><td></td></tr>
<tr><td><code>Liposomal Doxorubicin</code></td><td><code>ncit:C160080</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Methylprednisone</code></td><td><code></code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Neratinib</code></td><td><code>ncit:C49094</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Oxaliplatin</code></td><td><code>rxcui:32592</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Pazopanib</code></td><td><code>rxcui:714438</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Pirarubicin</code></td><td><code>ncit:C1197</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Quercetin</code></td><td><code>ncit:C792</code></td><td></td></tr>
<tr><td><code>Ramucirumab</code></td><td><code>ncit:C70792</code></td><td></td></tr>
<tr><td><code>Regorafenib</code></td><td><code>ncit:C78204</code></td><td></td></tr>
<tr><td><code>Sirolimus</code></td><td><code>rxcui:35302</code></td><td></td></tr>
<tr><td><code>Sirpiglenastat</code></td><td><code>ncit:C174038</code></td><td></td></tr>
<tr><td><code>Sodium Thiosulfate</code></td><td><code>ncit:C1230</code></td><td>(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'<br>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Sorafenib</code></td><td><code>ncit:C61948</code></td><td></td></tr>
<tr><td><code>Tacrolimus</code></td><td><code>ncit:C1311</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Tazemetostat</code></td><td><code>ncit:C107506</code></td><td></td></tr>
<tr><td><code>Tegavivint</code></td><td><code>ncit:C155885</code></td><td></td></tr>
<tr><td><code>Temozolomide</code></td><td><code>rxcui:37776</code></td><td></td></tr>
<tr><td><code>Temsirolimus</code></td><td><code>ncit:C1244</code></td><td></td></tr>
<tr><td><code>Tocilizumab</code></td><td><code>ncit:C84217</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Trametinib</code></td><td><code>ncit:C1413</code></td><td></td></tr>
<tr><td><code>Tremelimumab</code></td><td><code>ncit:C49085</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>Vorinostat</code></td><td><code>ncit:C74038</code></td><td></td></tr>
<tr><td><code>Zoledronic Acid</code></td><td><code>ncit:C1699</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-morphcodesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-morphcodesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-morphcodesystemenum')">×</button>
<h3><code>MorphCodeSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ICD-O</code></td><td><code>ncit:C160903</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-presentabsentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-presentabsentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-presentabsentenum')">×</button>
<h3><code>PresentAbsentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Absent</code></td><td><code>ncit:C25567</code></td><td></td></tr>
<tr><td><code>Present</code></td><td><code>ncit:C25566</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-procedureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-procedureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-procedureenum')">×</button>
<h3><code>ProcedureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Core Needle Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Core Needle, Laparscopic Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Core Needle, Percutaneous Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Excisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Extreme Hepatectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fine Needle Aspiration</code></td><td><code>ncit:C15361</code></td><td></td></tr>
<tr><td><code>Hepatectomy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intra-Operative Ablation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparscopic Biopsy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparscopic, Incisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mesohepatectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metastasectomy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Multi-focal Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-Anatomic Wedge</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Open Biopsy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Open, Incisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Orthotopic Transplant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Orthotopic Transplant, Multivisceral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Hepatectomy / Hemi-hepatectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Portal lymphadenectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Segmentectomy / Sectionectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sternotomy, Lobectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sternotomy, Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sternotomy, Pneumonectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sternotomy, Wedge Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thoracotomy, Lobectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thoracotomy, Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thoracotomy, Pneumonectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thoracotomy, Wedge Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trisegmentectomy / Trisectionectomy / Extended Hepatectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Video-Assisted Thoroscopic Surgery, Lobectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Video-Assisted Thoroscopic Surgery, Wedge Resection</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-proceduresiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-proceduresiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-proceduresiteenum')">×</button>
<h3><code>ProcedureSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abdominal Wall</code></td><td><code>ncit:C77608</code></td><td></td></tr>
<tr><td><code>Adrenal Gland</code></td><td><code>ncit:C12666</code></td><td></td></tr>
<tr><td><code>Bone / Skeletal</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain/Leptomeninges</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Colon</code></td><td><code>ncit:C12382</code></td><td></td></tr>
<tr><td><code>Diaphragm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C160424</code></td><td></td></tr>
<tr><td><code>Duodenum</code></td><td><code>ncit:C12263</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Tract</code></td><td><code>ncit:C34082</code></td><td></td></tr>
<tr><td><code>Hilar Nodes</code></td><td><code>ncit:C102330</code></td><td></td></tr>
<tr><td><code>Intra-Abdominal, Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Liver, Segment 1 (Caudate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 4a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 4b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 6</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 7</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver, Segment 8</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Mesenteric Nodes</code></td><td><code>ncit:C77641</code></td><td></td></tr>
<tr><td><code>Pancreas</code></td><td><code>ncit:C12393</code></td><td></td></tr>
<tr><td><code>Pericardium</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Small Intestine</code></td><td><code>ncit:C12386</code></td><td></td></tr>
<tr><td><code>Spleen</code></td><td><code>ncit:C7295</code></td><td></td></tr>
<tr><td><code>Splenic Hilar Nodes</code></td><td><code>ncit:C33600</code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code>ncit:C12391</code></td><td></td></tr>
<tr><td><code>Supraclavicular Nodes</code></td><td><code>ncit:C12903</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-responseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responseenum')">×</button>
<h3><code>ResponseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CHIC &gt;&gt; Disease Free</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-reviewsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reviewsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reviewsourceenum')">×</button>
<h3><code>ReviewSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Central</code></td><td><code>ncit:C191951</code></td><td></td></tr>
<tr><td><code>Institutional</code></td><td><code>ncit:C185325</code></td><td></td></tr>
<tr><td><code>Consensus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-sexenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sexenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sexenum')">×</button>
<h3><code>SexEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Female</code></td><td><code>ncit:C16576</code></td><td></td></tr>
<tr><td><code>Male</code></td><td><code>ncit:C20197</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-siteclassificationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-siteclassificationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-siteclassificationenum')">×</button>
<h3><code>SiteClassificationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Metastatic</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-smntypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-smntypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-smntypeenum')">×</button>
<h3><code>SmnTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ALL</code></td><td><code>ncit:C3167</code></td><td></td></tr>
<tr><td><code>AML</code></td><td><code>ncit:C3171</code></td><td></td></tr>
<tr><td><code>Solid Tumor, NOS</code></td><td><code>ncit:C9292</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stageenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stageenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stageenum')">×</button>
<h3><code>StageEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Evans Surgical Staging System &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans Surgical Staging System &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans Surgical Staging System &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans Surgical Staging System &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stagesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stagesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stagesystemenum')">×</button>
<h3><code>StageSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Evans Surgical Staging System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PRETEXT Staging System</code></td><td><code>ncit:C141133</code></td><td></td></tr>
<tr><td><code>Staging System, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-studyidenum" class="enum-modal" onclick="closeEnumModal('enum-modal-studyidenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-studyidenum')">×</button>
<h3><code>StudyIdEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>AHEP0731</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'COG'</td></tr>
<tr><td><code>German Liver Tumor Registry</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'GPOH'</td></tr>
<tr><td><code>HB89</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'GPOH'</td></tr>
<tr><td><code>HB99</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'GPOH'</td></tr>
<tr><td><code>INT0098</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'COG'</td></tr>
<tr><td><code>JPLT1</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'JCCG'</td></tr>
<tr><td><code>JPLT2</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'JCCG'</td></tr>
<tr><td><code>JPLT3</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'JCCG'</td></tr>
<tr><td><code>P9645</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'COG'</td></tr>
<tr><td><code>SIOPEL2</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'</td></tr>
<tr><td><code>SIOPEL3</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'</td></tr>
<tr><td><code>SIOPEL4</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'</td></tr>
<tr><td><code>SIOPEL6</code></td><td><code></code></td><td>D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-topcodesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-topcodesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-topcodesystemenum')">×</button>
<h3><code>TopCodeSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ICD-O</code></td><td><code>ncit:C160903</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>


<script>
function openEnumModal(enumId) {
  document.getElementById(enumId).classList.add("enum-modal-open");
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
</script>


</div>

<div id="raw-model-view" style="display:none;" markdown="1">

```json
{
  "id": "https://example.org/pcdc/schema",
  "name": "pcdc-prod",
  "title": "PCDC Data Model",
  "description": "Each disease consortium associated with the PCDC uses a disease-specific data dictionary as the target schema for their data harmonization efforts. The PCDC data model is the full collection of these consensus data elements.",
  "license": "CC BY-NC 4.0",
  "version": "pcdc-2.0",
  "prefixes": {
    "pcdc": "https://example.org/pcdc/",
    "linkml": "https://w3id.org/linkml/",
    "ncit": "http://purl.obolibrary.org/obo/NCIT_"
  },
  "default_prefix": "pcdc",
  "default_range": "string",
  "imports": [
    "linkml:types"
  ],
  "subsets": {
    "lt": {
      "name": "lt",
      "title": "Liver Tumors",
      "description": "The LT view of the PCDC data model represents consensus data modeling by an international group of pediatric liver tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Children's Hepatic Tumors International Collaboration (CHIC). It is based on the collective requirements of its contributors."
    }
  },
  "classes": {
    "Subject": {
      "slots": [
        "consortium",
        "disease_group",
        "sex"
      ],
      "comments": [
        "D4CGNote: One observation/row per instance of a DataContributorPerson being enrolled on a study",
        "(fa) ConsortiumNote: This table is tiered as Mandatory.",
        "(fprh) ConsortiumNote: This table is tiered as Mandatory.",
        "(npc) ConsortiumNote: This table is tiered as Mandatory."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "StudyMetadata": {
      "slots": [
        "study_id",
        "age_at_enrollment",
        "year_at_enrollment",
        "data_source",
        "urls"
      ],
      "comments": [
        "D4CGNote: One observation/row per study",
        "(fa) ConsortiumNote: This table is tiered as Mandatory.",
        "(fprh) ConsortiumNote: This table is tiered as Mandatory.",
        "(npc) ConsortiumNote: This table is tiered as Mandatory."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "ClinicalEpisode": {
      "slots": [
        "disease_phase",
        "course",
        "age_at_start",
        "year_at_start"
      ],
      "comments": [
        "D4CGNote: One observation/row per time period when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Mandatory.",
        "(npc) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "SurvivalCharacteristics": {
      "slots": [
        "age_at_lkss",
        "lkss",
        "cause_of_death"
      ],
      "comments": [
        "D4CGNote: One observation/row per LKSS when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Mandatory.",
        "(fprh) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "MedicalHistory": {
      "slots": [
        "age_at_condition",
        "medical_history_condition",
        "condition_other"
      ],
      "comments": [
        "(os) ConsortiumNote: No AOST0331/EURAMOS1 data"
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "LaboratoryTest": {
      "slots": [
        "age_at_lab",
        "laboratory_test",
        "result_numeric",
        "laboratory_test_result_unit"
      ],
      "comments": [
        "D4CGNote: One observation/row per result when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "testing"
      }
    },
    "Diagnosis": {
      "slots": [
        "age_at_diag_assessment",
        "review_source",
        "diagnosis_category",
        "diagnosis_basis",
        "diagnosis",
        "histologic_features"
      ],
      "comments": [
        "D4CGNote: One observation/row per DIAGNOSIS",
        "(fa) ConsortiumNote: This table is tiered as Mandatory.",
        "(fprh) ConsortiumNote: This table is tiered as Mandatory.",
        "(npc) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "disease_attributes"
      }
    },
    "Staging": {
      "slots": [
        "age_at_staging",
        "review_source",
        "stage_system",
        "stage_system_version",
        "stage",
        "pretext_mod_v",
        "pretext_mod_p",
        "pretext_mod_e",
        "pretext_mod_m",
        "pretext_mod_f",
        "pretext_mod_r"
      ],
      "comments": [
        "D4CGNote: One observation/row per STAGE when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "disease_attributes"
      }
    },
    "DiseaseSiteAssessment": {
      "slots": [
        "age_at_disease_site_assessment",
        "site_classification",
        "disease_site",
        "site_other"
      ],
      "comments": [
        "D4CGNote: One observation/row per tumor or lesion when instantiated. Multiple tumors or lesions can be reported in a single obvservation/row if no individual characteristics (e.g. different sites, individual classifications or measurements, etc.) need to be included.",
        "(cns) ConsortiumNote: Not sure COG data will have anything for this table",
        "(ews) ConsortiumNote: For EE99, we will report here only the baseline evaluation. For further disease evaluation, we do not have the description of the detailed lesions",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Optional.",
        "(fprh) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "disease_attributes"
      }
    },
    "SurgicalProcedures": {
      "slots": [
        "age_at_procedure",
        "site_classification",
        "procedure",
        "procedure_site",
        "site_other",
        "laterality",
        "margins"
      ],
      "comments": [
        "D4CGNote: One observation/row per procedure when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Optional.",
        "(fprh) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "Medication": {
      "slots": [
        "age_at_medication_start",
        "cycles_planned",
        "medication"
      ],
      "comments": [
        "D4CGNote: One observation/row per medication administration when instantiated.",
        "(lt) ConsortiumNote: If multiple, include only 5 most recent",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response"
      ],
      "comments": [
        "D4CGNote: One observation/row per result when instantiated.",
        "(cns) ConsortiumNote: Will have COG response data for ACNS0334",
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "monitoring"
      }
    },
    "AdverseEvents": {
      "slots": [
        "age_at_ae",
        "adverse_event"
      ],
      "comments": [
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "monitoring"
      }
    },
    "SubsequentMalignantNeoplasm": {
      "slots": [
        "age_at_smn",
        "smn_type",
        "morph_code",
        "morph_code_text",
        "morph_code_system",
        "morph_code_system_version",
        "top_code",
        "top_code_text",
        "top_code_system",
        "top_code_system_version"
      ],
      "comments": [
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "monitoring"
      }
    }
  },
  "slots": {
    "year_at_start": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: Year in which exam occured"
      ],
      "annotations": {
        "tier_priority": "npc,aml",
        "tier_optional": "fa,lt,rb,ls"
      }
    },
    "medical_history_condition": {
      "slot_uri": "ncit:C18772",
      "range": "MedicalHistoryConditionEnum",
      "comments": [
        "(aml) ConsortiumNote: If subject had multiple prior medical conditions, include one observation per condition.",
        "(pre) ConsortiumNote: If subject had multiple prior medical conditions, include one observation per condition.",
        "(ews) ConsortiumNote: If subject had multiple prior medical conditions, include one observation per condition.",
        "(rb) ConsortiumNote: If subject had multiple prior medical conditions, include one observation per condition."
      ],
      "annotations": {
        "tier_mandatory": "fa,rb",
        "tier_priority": "lt,npc,rb",
        "tier_optional": "hl,ls"
      }
    },
    "top_code_system": {
      "slot_uri": "",
      "range": "TopCodeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "ls"
      }
    },
    "diagnosis_category": {
      "slot_uri": "",
      "range": "DiagnosisCategoryEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "ls"
      }
    },
    "disease_site": {
      "slot_uri": "ncit:C166232",
      "range": "DiseaseSiteEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "npc",
        "tier_priority": "fa",
        "tier_optional": "ls,fprh"
      }
    },
    "study_id": {
      "slot_uri": "ncit:C83082",
      "range": "StudyIdEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "all_groups,ls"
      }
    },
    "pretext_mod_p": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "smn_type": {
      "slot_uri": "",
      "range": "SmnTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,npc"
      }
    },
    "morph_code_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "disease_phase": {
      "slot_uri": "ncit:C168878",
      "range": "DiseasePhaseEnum",
      "comments": [
        "D4CGNote: <mandatory_if>'TIME_PERIOD_TYPE' == 'Disease Phase'</mandatory_if>",
        "(aml) ConsortiumNote: Disease Phase could be 'Initial Diagnosis' phase, or a 'Relapse' phase, etc...",
        "(cns) ConsortiumNote: For COG initial MB data, all will be initial diagnosis.",
        "(ews) ConsortiumNote: Disease Phase could be 'Initial Diagnosis' phase, or a 'Relapse' phase, etc...",
        "(npc) D4CGNote: <mandatory_if>'TIME_PERIOD_TYPE' == 'Disease Phase'</mandatory_if> \n ConsortiumNote: For COG initial MB data, all will be initial diagnosis."
      ],
      "annotations": {
        "tier_mandatory": "fa,hl,npc",
        "tier_priority": "lt,rb,aml",
        "tier_optional": "ls"
      }
    },
    "urls": {
      "slot_uri": "",
      "range": "string",
      "comments": [
        "D4CGNote: Mapping from a URL label (key) to a URL string"
      ],
      "multivalued": true,
      "inlined_as_list": false,
      "annotations": {}
    },
    "laboratory_test_result_unit": {
      "slot_uri": "",
      "range": "LaboratoryTestResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt",
        "tier_optional": "ls"
      }
    },
    "age_at_diag_assessment": {
      "slot_uri": "ncit:C175004",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "adverse_event": {
      "slot_uri": "ncit:C41331",
      "range": "AdverseEventEnum",
      "comments": [
        "(aml) ConsortiumNote: For AML, COG will omit multiorgan failure, hemorrhage, and neurotoxcity. Infection for AML COG will be CRF question about sterile site"
      ],
      "annotations": {
        "tier_mandatory": "hl,npc",
        "tier_priority": "fa,lt,rb"
      }
    },
    "age_at_smn": {
      "slot_uri": "ncit:C168860",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "cause_of_death": {
      "slot_uri": "ncit:C81239",
      "range": "CauseOfDeathEnum",
      "comments": [
        "D4CGNote: If multiple causes of death, include one observation per cause of death. However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary.\nD4CGNote: Only fill in this variable if LKSS is \"Dead\".",
        "D4CGNote: If multiple causes of death, include one observation per cause of death. However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary.",
        "D4CGNote: Only fill in this variable if LKSS is 'Dead'."
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "npc,lt,rb,fa,aml",
        "tier_optional": "ls"
      }
    },
    "procedure": {
      "slot_uri": "ncit:C161601",
      "range": "ProcedureEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt,rb",
        "tier_mandatory": "npc",
        "tier_optional": "rb,ls"
      }
    },
    "review_source": {
      "slot_uri": "ncit:C185324",
      "range": "ReviewSourceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "npc,ls"
      }
    },
    "age_at_medication_start": {
      "slot_uri": "ncit:C172698",
      "range": "integer",
      "comments": [
        "(aml) ConsortiumNote: In the case of 'Intrathecal Chemotherapy,' the age at the start is based on intention-to-treat."
      ],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "lkss": {
      "slot_uri": "ncit:C168931",
      "range": "LkssEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,hl,npc",
        "tier_priority": "lt,rb,aml",
        "tier_optional": "ls"
      }
    },
    "consortium": {
      "slot_uri": "ncit:C61538",
      "range": "ConsortiumEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "all_groups,ls"
      }
    },
    "pretext_mod_r": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "age_at_lkss": {
      "slot_uri": "ncit:C168844",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "response": {
      "slot_uri": "ncit:C50995",
      "range": "ResponseEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl,npc",
        "tier_priority": "rb"
      }
    },
    "age_at_procedure": {
      "slot_uri": "ncit:C175008",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "disease_group": {
      "slot_uri": "",
      "range": "DiseaseGroupEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "all_groups,ls"
      }
    },
    "top_code_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "ls"
      }
    },
    "age_at_disease_site_assessment": {
      "slot_uri": "ncit:C174997",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "age_at_lab": {
      "slot_uri": "ncit:C172691",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "age_at_start": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: Age at time of exam"
      ],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "stage_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt,npc"
      }
    },
    "top_code": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "lt",
        "tier_optional": "ls"
      }
    },
    "morph_code_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "diagnosis_basis": {
      "slot_uri": "",
      "range": "DiagnosisBasisEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "npc"
      }
    },
    "site_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "lt"
      }
    },
    "laboratory_test": {
      "slot_uri": "ncit:C117142",
      "range": "LaboratoryTestEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,npc",
        "tier_priority": "lt,rb",
        "tier_optional": "ls"
      }
    },
    "diagnosis": {
      "slot_uri": "ncit:C15220",
      "range": "DiagnosisEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,npc",
        "tier_priority": "aml,lt,rb,os",
        "tier_optional": "ls"
      }
    },
    "age_at_ae": {
      "slot_uri": "ncit:C172677",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "year_at_enrollment": {
      "slot_uri": "ncit:C177353",
      "range": "integer",
      "comments": [
        "(fa) ConsortiumNote: ConditionalStatement: if 'ENROLLED_STATUS' == 'Enrolled'"
      ],
      "annotations": {
        "tier_priority": "fa,lt",
        "tier_optional": "npc,ls"
      }
    },
    "age_at_condition": {
      "slot_uri": "ncit:C18772",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "result_numeric": {
      "slot_uri": "ncit:C185629",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Only fill in this variable if the available data is a single numeric value.",
        "(pre) ConsortiumNote: Only fill in this variable if the available data is a single numeric value.",
        "(cns) ConsortiumNote: Only fill in this variable if the available data is a single numeric value.",
        "(ews) ConsortiumNote: Only fill in this variable if the available data is a single numeric value.",
        "(hl) ConsortiumNote: Only fill in this variable if the available data is a single numeric value."
      ],
      "annotations": {
        "tier_mandatory": "npc",
        "tier_priority": "aml,fa,lt,npc,rb",
        "tier_optional": "ls"
      }
    },
    "condition_other": {
      "slot_uri": "ncit:C53263",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "lt,rb"
      }
    },
    "pretext_mod_e": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "margins": {
      "slot_uri": "ncit:C41227",
      "range": "MarginsEnum",
      "comments": [
        "(ews) ConsortiumNote: Should be the result of a the pathologic assessment"
      ],
      "annotations": {
        "tier_priority": "fa,lt",
        "tier_optional": "npc"
      }
    },
    "stage_system": {
      "slot_uri": "ncit:C18004",
      "range": "StageSystemEnum",
      "comments": [
        "(pre) ConsortiumNote: If there were multiple staging systems used, include one observation per staging system"
      ],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "ls"
      }
    },
    "age_at_enrollment": {
      "slot_uri": "ncit:C168843",
      "range": "integer",
      "comments": [
        "(ews) ConsortiumNote: ConditionalStatement: if 'ENROLLED_STATUS' == 'Enrolled'",
        "(ews) ConsortiumNote:  ConditionalStatement: Mandatory if 'AGE_AT_DIAG_ASSESSMENT' is null",
        "(fa) ConsortiumNote: Includes patients in a registry, trial, institutional databases, or other sources."
      ],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "stage": {
      "slot_uri": "ncit:C16899",
      "range": "StageEnum",
      "comments": [
        "(nbl) ConsortiumNote: Tied to stage system."
      ],
      "annotations": {
        "tier_mandatory": "fa,hl,npc",
        "tier_priority": "lt,rb",
        "tier_optional": "ls"
      }
    },
    "morph_code_system": {
      "slot_uri": "",
      "range": "MorphCodeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "sex": {
      "slot_uri": "ncit:C28421",
      "range": "SexEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl,npc",
        "tier_priority": "fa,lt,rb,aml",
        "tier_optional": "ls"
      }
    },
    "data_source": {
      "slot_uri": "ncit:C16493",
      "range": "DataSourceEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "lt",
        "tier_optional": "npc",
        "tier_priority": "os,rb"
      }
    },
    "morph_code": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "lt"
      }
    },
    "medication": {
      "slot_uri": "ncit:C459",
      "range": "MedicationEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,npc",
        "tier_priority": "lt,rb"
      }
    },
    "course": {
      "slot_uri": "ncit:C168807",
      "range": "CourseEnum",
      "comments": [
        "D4CGNote: <mandatory_if>'TIME_PERIOD_TYPE' == 'Course'</mandatory_if>"
      ],
      "annotations": {
        "tier_mandatory": "hl,npc",
        "tier_priority": "lt,rb,aml",
        "tier_optional": "ls"
      }
    },
    "cycles_planned": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: For RB, this field should be used to designate the anticipated number of cycles of systemic chemotherapy that will be administered to the patient,"
      ],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "npc,rb"
      }
    },
    "procedure_site": {
      "slot_uri": "ncit:C157120",
      "range": "ProcedureSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt",
        "tier_optional": "ls"
      }
    },
    "histologic_features": {
      "slot_uri": "",
      "range": "HistologicFeaturesEnum",
      "comments": [
        "(lt) ConsortiumNote: Use for Teratoid Features."
      ],
      "annotations": {
        "tier_priority": "lt,rb"
      }
    },
    "pretext_mod_f": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "pretext_mod_v": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "age_at_staging": {
      "slot_uri": "ncit:C177359",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "laterality": {
      "slot_uri": "ncit:C164550",
      "range": "LateralityEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,lt,npc,rb",
        "tier_optional": "npc,rb,ls"
      }
    },
    "top_code_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "ls"
      }
    },
    "pretext_mod_m": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "site_classification": {
      "slot_uri": "ncit:C174459",
      "range": "SiteClassificationEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "npc",
        "tier_priority": "fa,lt,rb",
        "tier_optional": "npc,ls"
      }
    },
    "age_at_response": {
      "slot_uri": "ncit:C168856",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    }
  },
  "enums": {
    "DiagnosisBasisEnum": {
      "permissible_values": {
        "Histological": {
          "meaning": "ncit:C25526",
          "comments": []
        }
      }
    },
    "MorphCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
          "comments": []
        }
      }
    },
    "ResponseEnum": {
      "permissible_values": {
        "CHIC >> Disease Free": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LkssEnum": {
      "permissible_values": {
        "Alive": {
          "meaning": "ncit:C37987",
          "comments": []
        },
        "Dead": {
          "meaning": "ncit:C28554",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "CourseEnum": {
      "permissible_values": {
        "Postoperative Chemotherapy": {
          "meaning": "",
          "comments": []
        },
        "Preoperative Chemotherapy": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ReviewSourceEnum": {
      "permissible_values": {
        "Central": {
          "meaning": "ncit:C191951",
          "comments": []
        },
        "Institutional": {
          "meaning": "ncit:C185325",
          "comments": []
        },
        "Consensus": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Bone, NOS": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Central Nervous System": {
          "meaning": "ncit:C12438",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": [
            "(ews) ConsortiumNote: Included so that peritoneal effusions can be reported."
          ]
        },
        "Soft Tissue": {
          "meaning": "ncit:C12471",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "DataSourceEnum": {
      "permissible_values": {
        "Registry": {
          "meaning": "ncit:C129000",
          "comments": [
            "(npc) ConsortiumNotes: For TROD, use Registry only."
          ]
        },
        "Therapeutic Trial": {
          "meaning": "ncit:C39536",
          "comments": []
        }
      }
    },
    "LateralityEnum": {
      "permissible_values": {
        "Left": {
          "meaning": "ncit:C160200",
          "comments": []
        },
        "Right": {
          "meaning": "ncit:C160199",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "StageEnum": {
      "permissible_values": {
        "Evans Surgical Staging System >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "Evans Surgical Staging System >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "Evans Surgical Staging System >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "Evans Surgical Staging System >> Stage 4": {
          "meaning": "",
          "comments": []
        },
        "PRETEXT, 1992 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "System NOS >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Stage 4": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SexEnum": {
      "permissible_values": {
        "Female": {
          "meaning": "ncit:C16576",
          "comments": []
        },
        "Male": {
          "meaning": "ncit:C20197",
          "comments": []
        }
      }
    },
    "StageSystemEnum": {
      "permissible_values": {
        "Evans Surgical Staging System": {
          "meaning": "",
          "comments": []
        },
        "PRETEXT Staging System": {
          "meaning": "ncit:C141133",
          "comments": []
        },
        "Staging System, NOS": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "CauseOfDeathEnum": {
      "permissible_values": {
        "Disease Progression": {
          "meaning": "ncit:C168970",
          "comments": [
            "(cns) ConsortiumNote: Deceased-due to disease.",
            "(fa) ConsortiumNote: Cancer-related disease progression. Deceased-due to disease.",
            "(gct) ConsortiumNote: If multiple causes of death, include one observation per cause of death.",
            "(hl) ConsortiumNote: If multiple causes of death, include one observation per cause of death.",
            "(nrsts) ConsortiumNote: If multiple causes of death, include one observation per cause of death. There can only be one record where CAUSE_OF_DEATH_RANKING=Primary.",
            "(os) ConsortiumNote: If multiple causes of death, include one observation per cause of death. However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary. Note: Only fill in this variable if LKSS is 'Dead'.",
            "(rms) ConsortiumNote: If multiple causes of death, include one observation per cause of death.  However, only one cause of death can have the varaiable CAUSE_OF_DEATH_RANKING=Primary."
          ]
        },
        "Treatment-Related Mortality": {
          "meaning": "ncit:C166165",
          "comments": [
            "D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL."
          ]
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": [
            "(cns) ConsortiumNote: Deceased-due to unknown causes.",
            "(fa) ConsortiumNote: Deceased-due to unknown causes."
          ]
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": [
            "(cns) ConsortiumNote: Deceased-causes unavailable.",
            "(fa) ConsortiumNote: Deceased-causes unavailable."
          ]
        }
      }
    },
    "StudyIdEnum": {
      "permissible_values": {
        "AHEP0731": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'COG'"
          ]
        },
        "German Liver Tumor Registry": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'GPOH'"
          ]
        },
        "HB89": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'GPOH'"
          ]
        },
        "HB99": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'GPOH'"
          ]
        },
        "INT0098": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'COG'"
          ]
        },
        "JPLT1": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'JCCG'"
          ]
        },
        "JPLT2": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'JCCG'"
          ]
        },
        "JPLT3": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'JCCG'"
          ]
        },
        "P9645": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'COG'"
          ]
        },
        "SIOPEL2": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'"
          ]
        },
        "SIOPEL3": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'"
          ]
        },
        "SIOPEL4": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'"
          ]
        },
        "SIOPEL6": {
          "meaning": "",
          "comments": [
            "D4CGNote: DATA_CONTRIBUTOR = 'SIOPEL'"
          ]
        }
      }
    },
    "TopCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
          "comments": []
        }
      }
    },
    "HistologicFeaturesEnum": {
      "permissible_values": {
        "Teratoid Feature, Melanin-producing": {
          "meaning": "",
          "comments": []
        },
        "Teratoid Feature, Neuroendocrine": {
          "meaning": "",
          "comments": []
        },
        "Teratoid Feature, Neuroepithelial": {
          "meaning": "",
          "comments": []
        },
        "Teratoid Feature, Other e.g., Yolk sac tumor-like": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Cholangiocarcinoma": {
          "meaning": "icdo:8160/3",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Combined hepatocellular-cholangiocarcinoma": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Epithelial, Cholangioblastic": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Embryonal": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Epithelial mixed": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Retrospective only"
          ]
        },
        "Epithelial, Fetal, crowded, mitotically active": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Fetal, well-differentiated, mitotically inactive": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Glandular": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Macrotrabecular": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Pleomorphic, poorly differentiated": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Primitive, small cell undifferentiated or blastemal": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Pure Fetal, well-differentiated, mitotically inactive": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Examination of whole tumor is required for this diagnosis.",
            "(lt) ConsortiumNote:  Note: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Epithelial, Squamous": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Hepatocellular adenoma (expand?)": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Hepatocellular carcinoma, associated with hepatocellular adenoma": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'"
          ]
        },
        "Hepatocellular carcinoma, associated with hepatocellular adenoma, with underlying liver disease": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'"
          ]
        },
        "Hepatocellular carcinoma, classic": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'"
          ]
        },
        "Hepatocellular carcinoma, classic, with underlying liver disease": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatocellular Carcinoma'"
          ]
        },
        "Hepatocellular carcinoma, fibrolamellar": {
          "meaning": "icdo:8171/3",
          "comments": []
        },
        "Hepatocellular malignancy, NOS": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Includes transitional cell liver tumor. DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Malignant hepatocellular neoplasm, NOS, with carcinoma features": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Malignant rhabdoid tumor": {
          "meaning": "icdo:8963/3",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Mesenchymal hamartoma": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Mixed epithelial-mesenchymal, Cholangioblastic": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Embryonal": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Fetal, crowded, mitotically active": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Fetal, well-differentiated, mitotically inactive": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Glandular": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Macrotrabecular": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Mesenchymal, non-teratoid": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Pleomorphic, poorly differentiated": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Primitive (small cell undifferentiated or blastemal)": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, Squamous": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, with teratoid features": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatoblastoma'"
          ]
        },
        "Mixed epithelial-mesenchymal, without teratoid features": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Retrospective only"
          ]
        },
        "Nested stromal-epithelial tumor": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Undifferentiated embryonal sarcoma": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        }
      }
    },
    "PresentAbsentEnum": {
      "permissible_values": {
        "Absent": {
          "meaning": "ncit:C25567",
          "comments": []
        },
        "Present": {
          "meaning": "ncit:C25566",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "SmnTypeEnum": {
      "permissible_values": {
        "ALL": {
          "meaning": "ncit:C3167",
          "comments": []
        },
        "AML": {
          "meaning": "ncit:C3171",
          "comments": []
        },
        "Solid Tumor, NOS": {
          "meaning": "ncit:C9292",
          "comments": []
        }
      }
    },
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Abdominal Wall": {
          "meaning": "ncit:C77608",
          "comments": []
        },
        "Adrenal Gland": {
          "meaning": "ncit:C12666",
          "comments": []
        },
        "Bone / Skeletal": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Brain/Leptomeninges": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Colon": {
          "meaning": "ncit:C12382",
          "comments": []
        },
        "Diaphragm": {
          "meaning": "",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C160424",
          "comments": []
        },
        "Duodenum": {
          "meaning": "ncit:C12263",
          "comments": []
        },
        "Gastrointestinal Tract": {
          "meaning": "ncit:C34082",
          "comments": []
        },
        "Hilar Nodes": {
          "meaning": "ncit:C102330",
          "comments": []
        },
        "Intra-Abdominal, Other": {
          "meaning": "",
          "comments": []
        },
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Liver, Segment 1 (Caudate)": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 2": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 3": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 4a": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 4b": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 5": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 6": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 7": {
          "meaning": "",
          "comments": []
        },
        "Liver, Segment 8": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Lymph Nodes": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Mesenteric Nodes": {
          "meaning": "ncit:C77641",
          "comments": []
        },
        "Pancreas": {
          "meaning": "ncit:C12393",
          "comments": []
        },
        "Pericardium": {
          "meaning": "",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Small Intestine": {
          "meaning": "ncit:C12386",
          "comments": []
        },
        "Spleen": {
          "meaning": "ncit:C7295",
          "comments": []
        },
        "Splenic Hilar Nodes": {
          "meaning": "ncit:C33600",
          "comments": []
        },
        "Stomach": {
          "meaning": "ncit:C12391",
          "comments": []
        },
        "Supraclavicular Nodes": {
          "meaning": "ncit:C12903",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "LT": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "ALRN 6924": {
          "meaning": "ncit:C118669",
          "comments": []
        },
        "Anti-AFP CART": {
          "meaning": "",
          "comments": []
        },
        "Anti-GPC3 CART": {
          "meaning": "",
          "comments": []
        },
        "Atezolizumab": {
          "meaning": "ncit:C106250",
          "comments": []
        },
        "Azathioprine": {
          "meaning": "rxcui:1256",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Bevacizumab": {
          "meaning": "rxcui:253337",
          "comments": []
        },
        "Bortezomib": {
          "meaning": "ncit:C1851",
          "comments": []
        },
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Cabozantinib": {
          "meaning": "ncit:C52200",
          "comments": []
        },
        "Capecitabine": {
          "meaning": "rxcui:194000",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Cellcept (MMF)": {
          "meaning": "ncit:C1468",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Codrituzumab": {
          "meaning": "ncit:C80043",
          "comments": []
        },
        "Cyclophosphamide": {
          "meaning": "rxcui:3002",
          "comments": []
        },
        "Cyclosporine": {
          "meaning": "rxcui:3008",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "DNAJB1-PRKACA Vaccine": {
          "meaning": "",
          "comments": []
        },
        "DT 2216": {
          "meaning": "",
          "comments": []
        },
        "Dendritic Cell Therapy": {
          "meaning": "ncit:C28976",
          "comments": []
        },
        "Dexrazoxane": {
          "meaning": "ncit:C1333",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention"
          ]
        },
        "Docetaxel": {
          "meaning": "rxcui:72962",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
          "comments": []
        },
        "Durvalumab": {
          "meaning": "ncit:C103194",
          "comments": []
        },
        "ENMD 2076": {
          "meaning": "",
          "comments": []
        },
        "Erlotinib": {
          "meaning": "ncit:C65530",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Etoposide Phosphate": {
          "meaning": "ncit:C1093",
          "comments": []
        },
        "Everolimus": {
          "meaning": "rxcui:141704",
          "comments": []
        },
        "Fluorouracil (5FU)": {
          "meaning": "rxcui:4492",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "rxcui:5657",
          "comments": []
        },
        "Indocyanine green": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Pre-surgical Medication"
          ]
        },
        "Interferon": {
          "meaning": "ncit:C20493",
          "comments": []
        },
        "Ipililumab": {
          "meaning": "ncit:C2654",
          "comments": []
        },
        "Irinotecan": {
          "meaning": "ncit:C62040",
          "comments": []
        },
        "Lenvatinib": {
          "meaning": "rxcui:1603296",
          "comments": []
        },
        "Leuprolide Acetate": {
          "meaning": "rxcui:203217",
          "comments": []
        },
        "Liposomal Doxorubicin": {
          "meaning": "ncit:C160080",
          "comments": []
        },
        "Melphalan": {
          "meaning": "rxcui:6718",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Methylprednisone": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Neratinib": {
          "meaning": "ncit:C49094",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Oxaliplatin": {
          "meaning": "rxcui:32592",
          "comments": []
        },
        "Paclitaxel": {
          "meaning": "ncit:C1411",
          "comments": []
        },
        "Pazopanib": {
          "meaning": "rxcui:714438",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
          "comments": []
        },
        "Pirarubicin": {
          "meaning": "ncit:C1197",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Quercetin": {
          "meaning": "ncit:C792",
          "comments": []
        },
        "Ramucirumab": {
          "meaning": "ncit:C70792",
          "comments": []
        },
        "Regorafenib": {
          "meaning": "ncit:C78204",
          "comments": []
        },
        "Sirolimus": {
          "meaning": "rxcui:35302",
          "comments": []
        },
        "Sirpiglenastat": {
          "meaning": "ncit:C174038",
          "comments": []
        },
        "Sodium Thiosulfate": {
          "meaning": "ncit:C1230",
          "comments": [
            "(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'",
            "(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention"
          ]
        },
        "Sorafenib": {
          "meaning": "ncit:C61948",
          "comments": []
        },
        "Tacrolimus": {
          "meaning": "ncit:C1311",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Tazemetostat": {
          "meaning": "ncit:C107506",
          "comments": []
        },
        "Tegavivint": {
          "meaning": "ncit:C155885",
          "comments": []
        },
        "Temozolomide": {
          "meaning": "rxcui:37776",
          "comments": []
        },
        "Temsirolimus": {
          "meaning": "ncit:C1244",
          "comments": []
        },
        "Tocilizumab": {
          "meaning": "ncit:C84217",
          "comments": []
        },
        "Topotecan": {
          "meaning": "rxcui:57308",
          "comments": []
        },
        "Trametinib": {
          "meaning": "ncit:C1413",
          "comments": []
        },
        "Tremelimumab": {
          "meaning": "ncit:C49085",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
          "comments": []
        },
        "Vorinostat": {
          "meaning": "ncit:C74038",
          "comments": []
        },
        "Zoledronic Acid": {
          "meaning": "ncit:C1699",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "MarginsEnum": {
      "permissible_values": {
        "Biopsy Only": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "No Viable Tumor Identified": {
          "meaning": "",
          "comments": []
        },
        "No lung metastases remain": {
          "meaning": "",
          "comments": []
        },
        "R0 - Complete Resection, Negative Margins": {
          "meaning": "ncit:C139578",
          "comments": [
            "(lt) ConsortiumNote: sub-procedures have no margins, only the multi-focal procedures"
          ]
        },
        "R1 - Complete Resection, Positive Margins": {
          "meaning": "ncit:C139579",
          "comments": []
        },
        "R2 - Gross Residual Disease": {
          "meaning": "ncit:C139580",
          "comments": []
        },
        "Some lung metastases remain": {
          "meaning": "",
          "comments": []
        },
        "Unresectable": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "DiseasePhaseEnum": {
      "permissible_values": {
        "Initial Diagnosis": {
          "meaning": "ncit:C156813",
          "comments": [
            "(gct) ConsortiumNote: Disease phase could be 'Initial Diagnosis' phase, 'Relapse' phase, etc...",
            "(hl) ConsortiumNote: Disease phase could be 'Initial Diagnosis' phase, a 'Relapse' phase, etc..."
          ]
        },
        "Progression": {
          "meaning": "ncit:C17747",
          "comments": []
        },
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        }
      }
    },
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia": {
          "meaning": "ncit:C34415",
          "comments": []
        },
        "Familial Adenomatous Polyposis": {
          "meaning": "ncit:C3339",
          "comments": []
        },
        "Hemihypertrophy": {
          "meaning": "ncit:C88541",
          "comments": []
        },
        "Low Birth Weight": {
          "meaning": "ncit:C34724",
          "comments": []
        },
        "Preterm Birth": {
          "meaning": "ncit:92861",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "CHIC": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Ototoxicity": {
          "meaning": "ncit:C66929",
          "comments": []
        },
        "Surgical Complications, NOS": {
          "meaning": "",
          "comments": []
        },
        "Surgical Death within 30 days": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "DiagnosisCategoryEnum": {
      "permissible_values": {
        "Fibrolamellar carcinoma": {
          "meaning": "",
          "comments": []
        },
        "Hepatic Tumor, Other": {
          "meaning": "",
          "comments": []
        },
        "Hepatoblastoma (HB)": {
          "meaning": "ncit:C3728",
          "comments": []
        },
        "Hepatocelluar Carcinoma (HCC)": {
          "meaning": "ncit:C3099",
          "comments": []
        }
      }
    },
    "SiteClassificationEnum": {
      "permissible_values": {
        "Metastatic": {
          "meaning": "ncit:C3261",
          "comments": []
        },
        "Primary": {
          "meaning": "ncit:C8509",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "AFP": {
          "meaning": "ncit:C21577",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        }
      }
    },
    "ProcedureEnum": {
      "permissible_values": {
        "Core Needle Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Core Needle, Laparscopic Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Core Needle, Percutaneous Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Excisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Extreme Hepatectomy": {
          "meaning": "",
          "comments": []
        },
        "Fine Needle Aspiration": {
          "meaning": "ncit:C15361",
          "comments": []
        },
        "Hepatectomy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Intra-Operative Ablation": {
          "meaning": "",
          "comments": []
        },
        "Laparscopic Biopsy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Laparscopic, Incisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Mesohepatectomy": {
          "meaning": "",
          "comments": []
        },
        "Metastasectomy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Multi-focal Resection": {
          "meaning": "",
          "comments": []
        },
        "Non-Anatomic Wedge": {
          "meaning": "",
          "comments": []
        },
        "Open Biopsy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Open, Incisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Orthotopic Transplant": {
          "meaning": "",
          "comments": []
        },
        "Orthotopic Transplant, Multivisceral": {
          "meaning": "",
          "comments": []
        },
        "Partial Hepatectomy / Hemi-hepatectomy": {
          "meaning": "",
          "comments": []
        },
        "Portal lymphadenectomy": {
          "meaning": "",
          "comments": []
        },
        "Segmentectomy / Sectionectomy": {
          "meaning": "",
          "comments": []
        },
        "Sternotomy, Lobectomy": {
          "meaning": "",
          "comments": []
        },
        "Sternotomy, Other": {
          "meaning": "",
          "comments": []
        },
        "Sternotomy, Pneumonectomy": {
          "meaning": "",
          "comments": []
        },
        "Sternotomy, Wedge Resection": {
          "meaning": "",
          "comments": []
        },
        "Thoracotomy, Lobectomy": {
          "meaning": "",
          "comments": []
        },
        "Thoracotomy, Other": {
          "meaning": "",
          "comments": []
        },
        "Thoracotomy, Pneumonectomy": {
          "meaning": "",
          "comments": []
        },
        "Thoracotomy, Wedge Resection": {
          "meaning": "",
          "comments": []
        },
        "Trisegmentectomy / Trisectionectomy / Extended Hepatectomy": {
          "meaning": "",
          "comments": []
        },
        "Video-Assisted Thoroscopic Surgery, Lobectomy": {
          "meaning": "",
          "comments": []
        },
        "Video-Assisted Thoroscopic Surgery, Wedge Resection": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "count/mm3": {
          "meaning": "ncit:C173275",
          "comments": []
        },
        "ng/mL": {
          "meaning": "ncit:C67306",
          "comments": []
        }
      }
    }
  }
}
```

</div>