---
layout: default
title: Germ Cell Tumors
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*GCT View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- [Central Nervous System Tumors](cns)
- [Ewing Sarcoma](ews)
- [Fanconi Anemia](fa)
- [Fertility Preservation and Reproductive Health](fprh)
- **Germ Cell Tumors**
- [Hodgkin Lymphoma](hl)
- [Lynch Syndrome](ls)
- [Liver Tumors](lt)
- [Neuroblastoma](nbl)
- [Nasopharyngeal Carcinoma](npc)
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The GCT view of the PCDC data model represents consensus data modeling by an international group of pediatric germ cell tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Malignant Germ Cell International Consortium (MaGIC). It is based on the collective requirements of its contributors.


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
| `age_at_start` | `integer` |  |
| `year_at_start` | `integer` |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |
| `urls` | `string` |  |

## StudySubgroupAssignment

| Slot | Range | Description |
|---|---|---|
| `subgroup_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgrouptypeenum')">SubgroupTypeEnum</button> |  |
| `subgroup_name` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgroupnameenum')">SubgroupNameEnum</button> |  |
| `subgroup_assignment_order` | `integer` |  |

## Subject

| Slot | Range | Description |
|---|---|---|
| `consortium` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-consortiumenum')">ConsortiumEnum</button> |  |
| `disease_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasegroupenum')">DiseaseGroupEnum</button> |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |
| `race` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button> |  |
| `ethnicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button> |  |
| `efs_censor_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-efscensorstatusenum')">EfsCensorStatusEnum</button> |  |
| `age_at_censor_status` | `integer` |  |

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
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `morph_code` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `mature_glial_implants` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `somatic_malignancy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-somaticmalignancytypeenum')">SomaticMalignancyTypeEnum</button> |  |
| `histology_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologygradeenum')">HistologyGradeEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `risk_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-riskgroupenum')">RiskGroupEnum</button> |  |
| `gts_treatment` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gtstreatmentenum')">GtsTreatmentEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `tumor_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `top_code` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `medication_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationcategoryenum')">MedicationCategoryEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | `TechniqueEnum` |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | `FractionDoseUnitEnum` |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `total_cycles` | `decimal` |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-extentenum')">ExtentEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |
| `outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-outcomeenum')">OutcomeEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-outcomeenum')">OutcomeEnum</button> |  |
| `ae_attribution` | `AeAttributionEnum` |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsemethodenum')">ResponseMethodEnum</button> |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsesystemenum')">ResponseSystemEnum</button> |  |
| `response_system_version` | `string` |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `morph_code` | `string` |  |
| `morph_code_text` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |

<div class="domain-heading">Testing</div>

## Biospecimen

| Slot | Range | Description |
|---|---|---|
| `biospecimen_container_type` | `string` |  |
| `biospecimen_media` | `string` |  |
| `biospecimen_type` | `string` |  |
| `current_qty_unit` | `string` |  |
| `current_qty_value` | `string` |  |

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `alteration` | `AlterationEnum` |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `karyotype_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-karyotypestatusenum')">KaryotypeStatusEnum</button> |  |
| `total_chromosomes` | `decimal` |  |
| `independent_aberrations` | `decimal` |  |

## Immunohistochemistry

| Slot | Range | Description |
|---|---|---|
| `age_at_ihc` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `markers` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-markersenum')">MarkersEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `ihc_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ihcresultunitenum')">IhcResultUnitEnum</button> |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestmethodenum')">LaboratoryTestMethodEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |
| `quantification_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-quantificationtypeenum')">QuantificationTypeEnum</button> |  |
| `threshold_high` | `decimal` |  |
| `threshold_low` | `decimal` |  |
| `pmid_ref` | `decimal` |  |

## VitalsAndAnthropometrics

| Slot | Range | Description |
|---|---|---|
| `age_at_measurement` | `integer` |  |
| `anthropometric_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementtypeenum')">AnthropometricMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `anthropometric_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">AnthropometricMeasurementResultUnitEnum</button> |  |

<div id="enum-modal-activeresolvedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-activeresolvedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-activeresolvedenum')">×</button>
<h3><code>ActiveResolvedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Active</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Resolved</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-adverseeventenum" class="enum-modal" onclick="closeEnumModal('enum-modal-adverseeventenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-adverseeventenum')">×</button>
<h3><code>AdverseEventEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Neuropathy</code></td><td><code>ncit:C4731</code></td><td></td></tr>
<tr><td><code>Ototoxicity</code></td><td><code>ncit:C66929</code></td><td></td></tr>
<tr><td><code>Pulmonary Toxicity</code></td><td><code>ncit:C177374</code></td><td></td></tr>
<tr><td><code>Renal Toxicity</code></td><td><code>ncit:C115459</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aegradeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aegradeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aegradeenum')">×</button>
<h3><code>AeGradeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>System NOS &gt;&gt; Grade 1</code></td><td><code>ncit:C41338</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 2</code></td><td><code>ncit:C41339</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 3</code></td><td><code>ncit:C41340</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 4</code></td><td><code>ncit:C41337</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 5</code></td><td><code>ncit:C48275</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-alterationtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationtypeenum')">×</button>
<h3><code>AlterationTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Deletion</code></td><td><code>ncit:C16606</code></td><td></td></tr>
<tr><td><code>Duplication</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Indel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Insertion</code></td><td><code>SO:0000667</code></td><td></td></tr>
<tr><td><code>Inversion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rearrangement, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Substitution</code></td><td><code>SO:1000002</code></td><td></td></tr>
<tr><td><code>Translocation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-anthropometricmeasurementresultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">×</button>
<h3><code>AnthropometricMeasurementResultUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cm</code></td><td><code>ncit:C49668</code></td><td></td></tr>
<tr><td><code>kg</code></td><td><code>ncit:C28252</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-anthropometricmeasurementtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-anthropometricmeasurementtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-anthropometricmeasurementtypeenum')">×</button>
<h3><code>AnthropometricMeasurementTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
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
<tr><td><code>Secondary Malignancy</code></td><td><code>ncit:C4968</code></td><td>D4CGNote: Use the Subsequent Malignant Neoplasm table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(cns) ConsortiumNote: Deceased-causes unavailable.<br>(fa) ConsortiumNote: Deceased-causes unavailable.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-chromosomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-chromosomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-chromosomeenum')">×</button>
<h3><code>ChromosomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1</code></td><td><code>ncit:C13204</code></td><td></td></tr>
<tr><td><code>10</code></td><td><code>ncit:C13205</code></td><td></td></tr>
<tr><td><code>11</code></td><td><code>ncit:C13206</code></td><td></td></tr>
<tr><td><code>12</code></td><td><code>ncit:C13207</code></td><td></td></tr>
<tr><td><code>13</code></td><td><code>ncit:C13208</code></td><td></td></tr>
<tr><td><code>14</code></td><td><code>ncit:C13209</code></td><td></td></tr>
<tr><td><code>15</code></td><td><code>ncit:C13210</code></td><td></td></tr>
<tr><td><code>16</code></td><td><code>ncit:C13211</code></td><td></td></tr>
<tr><td><code>17</code></td><td><code>ncit:C13212</code></td><td></td></tr>
<tr><td><code>18</code></td><td><code>ncit:C13213</code></td><td></td></tr>
<tr><td><code>19</code></td><td><code>ncit:C13214</code></td><td></td></tr>
<tr><td><code>2</code></td><td><code>ncit:C13215</code></td><td></td></tr>
<tr><td><code>20</code></td><td><code>ncit:C13216</code></td><td></td></tr>
<tr><td><code>21</code></td><td><code>ncit:C13217</code></td><td></td></tr>
<tr><td><code>22</code></td><td><code>ncit:C13218</code></td><td></td></tr>
<tr><td><code>3</code></td><td><code>ncit:C13219</code></td><td></td></tr>
<tr><td><code>4</code></td><td><code>ncit:C13220</code></td><td></td></tr>
<tr><td><code>5</code></td><td><code>ncit:C13221</code></td><td></td></tr>
<tr><td><code>6</code></td><td><code>ncit:C13222</code></td><td></td></tr>
<tr><td><code>7</code></td><td><code>ncit:C13223</code></td><td></td></tr>
<tr><td><code>8</code></td><td><code>ncit:C13224</code></td><td></td></tr>
<tr><td><code>9</code></td><td><code>ncit:C13225</code></td><td></td></tr>
<tr><td><code>X</code></td><td><code>ncit:C13285</code></td><td></td></tr>
<tr><td><code>Y</code></td><td><code>ncit:C13286</code></td><td></td></tr>
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
<tr><td><code>MaGIC</code></td><td><code>ncit:C192759</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-detectionmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-detectionmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-detectionmethodenum')">×</button>
<h3><code>DetectionMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Imaging</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>Imaging, NOS</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>Tumor Marker</code></td><td><code>ncit:C17220</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Integrated</code></td><td><code>ncit:C165682</code></td><td></td></tr>
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
<tr><td><code>Choriocarcinoma</code></td><td><code>ncit:C2948</code></td><td></td></tr>
<tr><td><code>Dysgerminoma</code></td><td><code>icdo:9060/3</code></td><td></td></tr>
<tr><td><code>Embryonal Carcinoma</code></td><td><code>ncit:C3752</code></td><td></td></tr>
<tr><td><code>Germinoma</code></td><td><code>ncit:C3753</code></td><td></td></tr>
<tr><td><code>Immature Teratoma</code></td><td><code>ncit:C4286</code></td><td></td></tr>
<tr><td><code>Malignant Teratoma</code></td><td><code>ncit:C4287</code></td><td></td></tr>
<tr><td><code>Mature Teratoma</code></td><td><code>ncit:C9015</code></td><td></td></tr>
<tr><td><code>Mixed Germ Cell Tumor</code></td><td><code>ncit:C4290</code></td><td></td></tr>
<tr><td><code>Necrotic Tumor</code></td><td><code>ncit:C36029</code></td><td></td></tr>
<tr><td><code>Primitive Neuroectodermal Tumor</code></td><td><code>icdo:9473/3</code></td><td></td></tr>
<tr><td><code>Seminoma</code></td><td><code>ncit:C9309</code></td><td></td></tr>
<tr><td><code>Seminoma/Dysgerminoma/Germinoma</code></td><td><code>ncit:C121618</code></td><td></td></tr>
<tr><td><code>Somatic Malignancy</code></td><td><code>ncit:C18060</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
<tr><td><code>Yolk Sac Tumor</code></td><td><code>icdo:9071/3</code></td><td></td></tr>
<tr><td><code>Teratoma, NOS</code></td><td><code>icdo:9080/1</code></td><td></td></tr>
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
<tr><td><code>GCT</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Ascitic Fluid</code></td><td><code>ncit:C159203</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Cervix Lymph Node</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Frontal Cortex</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mediastinal Lymph Node</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C6634</code></td><td></td></tr>
<tr><td><code>Occipital Cortex</code></td><td><code>ncit:C32250</code></td><td></td></tr>
<tr><td><code>Omentum</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Omentum Lymph Node</code></td><td><code>ncit:C177766</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Parietal Cortex</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Pelvic Lymph Node</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Retroperitoneum Lymph Node</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Sacrococcygeal</code></td><td><code>ncit:C33506</code></td><td></td></tr>
<tr><td><code>Spinal Cord</code></td><td><code>ncit:C12464</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Suprasellar/Neurohypophyseal</code></td><td><code>ncit:C42602</code></td><td></td></tr>
<tr><td><code>Temporal Cortex</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thalamus</code></td><td><code>ncit:C12459</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-efscensorstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-efscensorstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-efscensorstatusenum')">×</button>
<h3><code>EfsCensorStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Subject has had one or more events</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subject is censored (i.e. has had no events(s))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-energytypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-energytypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-energytypeenum')">×</button>
<h3><code>EnergyTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Photon</code></td><td><code>ncit:C88112</code></td><td></td></tr>
<tr><td><code>Proton</code></td><td><code>ncit:C66897</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-ethnicityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ethnicityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ethnicityenum')">×</button>
<h3><code>EthnicityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Hispanic or Latino</code></td><td><code>ncit:C17459</code></td><td></td></tr>
<tr><td><code>Not Hispanic or Latino</code></td><td><code>ncit:C41222</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-extentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-extentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-extentenum')">×</button>
<h3><code>ExtentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Complete Resection</code></td><td><code>ncit:C175027</code></td><td></td></tr>
<tr><td><code>Gross Total</code></td><td><code>ncit:C131672</code></td><td></td></tr>
<tr><td><code>Partial Resection</code></td><td><code>ncit:C131680</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-geneticanalysismethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-geneticanalysismethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-geneticanalysismethodenum')">×</button>
<h3><code>GeneticAnalysisMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cytogenetics, Karyotyping</code></td><td><code>ncit:C25215</code></td><td></td></tr>
<tr><td><code>Cytogenetics, NOS</code></td><td><code>ncit:C16487</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-geneticanalysisspecimenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-geneticanalysisspecimenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-geneticanalysisspecimenenum')">×</button>
<h3><code>GeneticAnalysisSpecimenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Primary Tumor</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Metastatic Tumor</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-gtstreatmentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-gtstreatmentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-gtstreatmentenum')">×</button>
<h3><code>GtsTreatmentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chemotherapy</code></td><td><code>ncit:C15632</code></td><td></td></tr>
<tr><td><code>Surgery</code></td><td><code>ncit:C15329</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-histologygradeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-histologygradeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-histologygradeenum')">×</button>
<h3><code>HistologyGradeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Norris Immature Teratoma Grading System &gt;&gt; Grade 1</code></td><td><code>ncit:C28077</code></td><td>(gct) ConsortiumNote: Only associated with Immature Teratoma.</td></tr>
<tr><td><code>Norris Immature Teratoma Grading System &gt;&gt; Grade 2</code></td><td><code>ncit:C28078</code></td><td></td></tr>
<tr><td><code>Norris Immature Teratoma Grading System &gt;&gt; Grade 3</code></td><td><code>ncit:C28079</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-ihcresultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ihcresultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ihcresultunitenum')">×</button>
<h3><code>IhcResultUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>%</code></td><td><code>ncit:C48570</code></td><td></td></tr>
<tr><td><code>Intensity</code></td><td><code>ncit:C25539</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-karyotypestatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-karyotypestatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-karyotypestatusenum')">×</button>
<h3><code>KaryotypeStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abnormal Karyotype</code></td><td><code>ncit:C168875</code></td><td></td></tr>
<tr><td><code>Normal Karyotype</code></td><td><code>ncit:C173277</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Cytology Malignant Cells</code></td><td><code>ncit:C74660</code></td><td></td></tr>
<tr><td><code>LDH</code></td><td><code>ncit:C64855</code></td><td></td></tr>
<tr><td><code>cfDNA</code></td><td><code>ncit:C128274</code></td><td></td></tr>
<tr><td><code>miR-367-3p</code></td><td><code>ncit:C177302</code></td><td></td></tr>
<tr><td><code>miR-371a-3p</code></td><td><code>ncit:C158711</code></td><td></td></tr>
<tr><td><code>miR-372-3p</code></td><td><code>ncit:C82190</code></td><td></td></tr>
<tr><td><code>miR-373-3p</code></td><td><code>ncit:C82191</code></td><td></td></tr>
<tr><td><code>miR-375-3p</code></td><td><code>ncit:C101665</code></td><td></td></tr>
<tr><td><code>beta-hCG</code></td><td><code>ncit:C64851</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laboratorytestmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorytestmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorytestmethodenum')">×</button>
<h3><code>LaboratoryTestMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cytology</code></td><td><code>ncit:C16491</code></td><td></td></tr>
<tr><td><code>MicroRNA Sequencing</code></td><td><code>ncit:C156057</code></td><td></td></tr>
<tr><td><code>ddPCR</code></td><td><code>ncit:C166064</code></td><td></td></tr>
<tr><td><code>qPCR</code></td><td><code>ncit:C51962</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>U/L</code></td><td><code>ncit:C67456</code></td><td></td></tr>
<tr><td><code>cp/mL</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ng/mL</code></td><td><code>ncit:C67306</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laboratorytestspecimenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorytestspecimenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorytestspecimenenum')">×</button>
<h3><code>LaboratoryTestSpecimenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Peritoneal Fluid</code></td><td><code>ncit:C185197</code></td><td></td></tr>
<tr><td><code>Plasma</code></td><td><code>ncit:C185204</code></td><td></td></tr>
<tr><td><code>Pleural Fluid</code></td><td><code>ncit:C77613</code></td><td></td></tr>
<tr><td><code>Serum</code></td><td><code>ncit:C178987</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Bilateral</code></td><td><code>ncit:C13332</code></td><td></td></tr>
<tr><td><code>Left</code></td><td><code>ncit:C160200</code></td><td></td></tr>
<tr><td><code>Midline</code></td><td><code>ncit:C81170</code></td><td></td></tr>
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
<tr><td><code>R0 - Complete Resection, Negative Margins</code></td><td><code>ncit:C139578</code></td><td>(lt) ConsortiumNote: sub-procedures have no margins, only the multi-focal procedures</td></tr>
<tr><td><code>R1 - Complete Resection, Positive Margins</code></td><td><code>ncit:C139579</code></td><td></td></tr>
<tr><td><code>R2 - Gross Residual Disease</code></td><td><code>ncit:C139580</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-markersenum" class="enum-modal" onclick="closeEnumModal('enum-modal-markersenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-markersenum')">×</button>
<h3><code>MarkersEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CD30</code></td><td><code>ncit:C38906</code></td><td></td></tr>
<tr><td><code>GPC3</code></td><td><code>ncit:C88175</code></td><td></td></tr>
<tr><td><code>beta-catenin</code></td><td><code>ncit:C17478</code></td><td></td></tr>
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
<tr><td><code>Gonadoblastoma</code></td><td><code>ncit:C3754</code></td><td></td></tr>
<tr><td><code>Klinefelter Syndrome</code></td><td><code>ncit:C34752</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-medicationcategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationcategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationcategoryenum')">×</button>
<h3><code>MedicationCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Antineoplastic Agent</code></td><td><code>ncit:C274</code></td><td></td></tr>
<tr><td><code>Supportive Care Agent</code></td><td><code>ncit:C70902</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-medicationdoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">×</button>
<h3><code>MedicationDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>IU</code></td><td><code>ncit:C48579</code></td><td></td></tr>
<tr><td><code>MBq</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mg</code></td><td><code>ncit:C28253</code></td><td></td></tr>
<tr><td><code>mg/kg</code></td><td><code>ncit:C105468</code></td><td></td></tr>
<tr><td><code>mg/m2</code></td><td><code>ncit:C67402</code></td><td></td></tr>
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
<tr><td><code>Amifostine</code></td><td><code>ncit:C488</code></td><td></td></tr>
<tr><td><code>Bleomycin</code></td><td><code>rxcui:1622</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Dactinomycin</code></td><td><code>rxcui:3100</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Etoposide Phosphate</code></td><td><code>ncit:C1093</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Sodium Thiosulfate</code></td><td><code>ncit:C1230</code></td><td>(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'<br>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Vinblastine</code></td><td><code>rxcui:11198</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
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

<div id="enum-modal-outcomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-outcomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-outcomeenum')">×</button>
<h3><code>OutcomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Death, Contributory</code></td><td><code>ncit:C168948</code></td><td></td></tr>
<tr><td><code>Death, Noncontributory</code></td><td><code>ncit:C173315</code></td><td></td></tr>
<tr><td><code>Not Yet Recovered</code></td><td><code>ncit:C49494</code></td><td></td></tr>
<tr><td><code>Recovered</code></td><td><code>ncit:C49498</code></td><td></td></tr>
<tr><td><code>Recovered with Sequelae</code></td><td><code>ncit:C49495</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Not Evaluated</code></td><td><code>ncit:C103424</code></td><td></td></tr>
<tr><td><code>Present</code></td><td><code>ncit:C25566</code></td><td></td></tr>
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
<tr><td><code>Frontal Cortex</code></td><td><code>ncit:C32635</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Occipital Cortex</code></td><td><code>ncit:C12757</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Parietal Cortex</code></td><td><code>ncit:C12766</code></td><td></td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Sacrococcygeal</code></td><td><code>ncit:C33506</code></td><td></td></tr>
<tr><td><code>Spinal Cord</code></td><td><code>ncit:C12464</code></td><td></td></tr>
<tr><td><code>Suprasellar/Neurohypophyseal</code></td><td><code>ncit:C177357</code></td><td></td></tr>
<tr><td><code>Temporal Cortex</code></td><td><code>ncit:C12797</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thalamus</code></td><td><code>ncit:C12459</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-quantificationtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-quantificationtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-quantificationtypeenum')">×</button>
<h3><code>QuantificationTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Absolute</code></td><td><code>ncit:C45829</code></td><td></td></tr>
<tr><td><code>Relative</code></td><td><code>ncit:C45830</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-raceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-raceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-raceenum')">×</button>
<h3><code>RaceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>American Indian or Alaska Native</code></td><td><code>ncit:C41259</code></td><td></td></tr>
<tr><td><code>Asian</code></td><td><code>ncit:C41260</code></td><td></td></tr>
<tr><td><code>Black or African American</code></td><td><code>ncit:C16352</code></td><td></td></tr>
<tr><td><code>Multiracial</code></td><td><code>ncit:C67109</code></td><td></td></tr>
<tr><td><code>Native Hawaiian or Other Pacific Islander</code></td><td><code>ncit:C41219</code></td><td></td></tr>
<tr><td><code>White</code></td><td><code>ncit:C41261</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-responsecategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsecategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsecategoryenum')">×</button>
<h3><code>ResponseCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Overall Response</code></td><td><code>ncit:C96613</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Choi &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Choi &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Choi &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Choi &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PERCIST &gt;&gt; Complete Metabolic Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PERCIST &gt;&gt; Partial Metabolic Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PERCIST &gt;&gt; Progressive Metabolic Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PERCIST &gt;&gt; Stable Metabolic Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Partial Response</code></td><td><code>ncit:C18058</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stable Disease</code></td><td><code>ncit:C18213</code></td><td></td></tr>
<tr><td><code>mRECIST &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mRECIST &gt;&gt; Incomplete Reseponse/Stable Disease</code></td><td><code></code></td><td>ConsortiumNote: Use for non-target lesions.</td></tr>
<tr><td><code>mRECIST &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mRECIST &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mRECIST &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-responsemethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsemethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsemethodenum')">×</button>
<h3><code>ResponseMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Imaging</code></td><td><code>ncit:C17220</code></td><td></td></tr>
<tr><td><code>Pathology</code></td><td><code>ncit:C18189</code></td><td></td></tr>
<tr><td><code>Tumor Marker</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-responsesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsesystemenum')">×</button>
<h3><code>ResponseSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Choi</code></td><td><code>ncit:C122394</code></td><td></td></tr>
<tr><td><code>PERCIST</code></td><td><code>ncit:C126039</code></td><td></td></tr>
<tr><td><code>RECIST</code></td><td><code>ncit:C49164</code></td><td></td></tr>
<tr><td><code>WHO</code></td><td><code>ncit:C75419</code></td><td></td></tr>
<tr><td><code>mRECIST</code></td><td><code>ncit:C126031</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-riskgroupenum" class="enum-modal" onclick="closeEnumModal('enum-modal-riskgroupenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-riskgroupenum')">×</button>
<h3><code>RiskGroupEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>IGCCC &gt;&gt; Good</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IGCCC &gt;&gt; Intermediate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IGCCC &gt;&gt; Poor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MaGIC &gt;&gt; Low</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MaGIC &gt;&gt; Poor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MaGIC &gt;&gt; Standard</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-rtdoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-rtdoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-rtdoseunitenum')">×</button>
<h3><code>RtDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cGy</code></td><td><code>ncit:C64693</code></td><td></td></tr>
<tr><td><code>Gy</code></td><td><code>ncit:C18063</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-rtsiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-rtsiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-rtsiteenum')">×</button>
<h3><code>RtSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Frontal Cortex</code></td><td><code>ncit:C32635</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Occiptial Cortex</code></td><td><code>ncit:C12757</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Parietal Cortex</code></td><td><code>ncit:C12766</code></td><td></td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Sacrococcygeal</code></td><td><code>ncit:C33506</code></td><td></td></tr>
<tr><td><code>Spinal Cord</code></td><td><code>ncit:C12464</code></td><td></td></tr>
<tr><td><code>Suprasellar/Neurohypophyseal</code></td><td><code>ncit:C177357</code></td><td></td></tr>
<tr><td><code>Temporal Cortex</code></td><td><code>ncit:C12797</code></td><td></td></tr>
<tr><td><code>Testes</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thalamus</code></td><td><code>ncit:C12459</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
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
<tr><td><code>Undifferentiated</code></td><td><code>ncit:C41438</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-somaticmalignancytypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-somaticmalignancytypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-somaticmalignancytypeenum')">×</button>
<h3><code>SomaticMalignancyTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Adenocarcinoma</code></td><td><code>ncit:C2852</code></td><td></td></tr>
<tr><td><code>Malignant Histiocytosis</code></td><td><code>ncit:C7202</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>ncit:C3359</code></td><td></td></tr>
<tr><td><code>Sarcoma, NOS</code></td><td><code>ncit:C9118</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma</code></td><td><code>ncit:C2929</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>AJCC &gt;&gt; Stage 0</code></td><td><code>ncit:C4523</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 1</code></td><td><code>ncit:C7901</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 1A</code></td><td><code>ncit:C6361</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 1B</code></td><td><code>ncit:C6362</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 1s</code></td><td><code>ncit:C6363</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 2</code></td><td><code>ncit:C9073</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 2A</code></td><td><code>ncit:C6364</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 2B</code></td><td><code>ncit:C6365</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 2C</code></td><td><code>ncit:C6366</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 3</code></td><td><code>ncit:C9074</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 3A</code></td><td><code>ncit:C6369</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 3B</code></td><td><code>ncit:C6368</code></td><td></td></tr>
<tr><td><code>AJCC &gt;&gt; Stage 3C</code></td><td><code>ncit:C6367</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 1</code></td><td><code>ncit:C27966</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 2</code></td><td><code>ncit:C28054</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 3</code></td><td><code>ncit:C27970</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 4</code></td><td><code>ncit:C27971</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 1</code></td><td><code>ncit:C96244</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 2</code></td><td><code>ncit:C96252</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 3</code></td><td><code>ncit:C96255</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 4</code></td><td><code>ncit:C96261</code></td><td></td></tr>
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
<tr><td><code>AGCT0132</code></td><td><code>ncit:C177343</code></td><td></td></tr>
<tr><td><code>AGCT01P1</code></td><td><code>ncit:C177342</code></td><td></td></tr>
<tr><td><code>AGCT0521</code></td><td><code>ncit:C177344</code></td><td></td></tr>
<tr><td><code>GC1</code></td><td><code>ncit:C177335</code></td><td></td></tr>
<tr><td><code>GC2</code></td><td><code>ncit:C177336</code></td><td></td></tr>
<tr><td><code>GOG0078</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GOG0090</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GOG0116</code></td><td><code>ncit:C177339</code></td><td></td></tr>
<tr><td><code>P9749</code></td><td><code>ncit:C177340</code></td><td></td></tr>
<tr><td><code>POG9049</code></td><td><code>ncit:C177341</code></td><td></td></tr>
<tr><td><code>TCGM2004</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE04</code></td><td><code>ncit:C177345</code></td><td></td></tr>
<tr><td><code>TE05</code></td><td><code>ncit:C177346</code></td><td></td></tr>
<tr><td><code>TE08</code></td><td><code>ncit:C177347</code></td><td></td></tr>
<tr><td><code>TE09</code></td><td><code>ncit:C177349</code></td><td></td></tr>
<tr><td><code>TE13</code></td><td><code>ncit:C177350</code></td><td></td></tr>
<tr><td><code>TE20</code></td><td><code>ncit:C177351</code></td><td></td></tr>
<tr><td><code>TE22</code></td><td><code>ncit:C177348</code></td><td></td></tr>
<tr><td><code>TGM85</code></td><td><code>ncit:C177332</code></td><td></td></tr>
<tr><td><code>TGM90</code></td><td><code>ncit:C177333</code></td><td></td></tr>
<tr><td><code>TGM95</code></td><td><code>ncit:C177334</code></td><td></td></tr>
<tr><td><code>TIP</code></td><td><code>ncit:C177352</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-subgroupnameenum" class="enum-modal" onclick="closeEnumModal('enum-modal-subgroupnameenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-subgroupnameenum')">×</button>
<h3><code>SubgroupNameEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>TE09:BEP (Cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE09:CEP (Carboplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE13:BEP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE13:BEP + GCSF</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE13:BOP/VIP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE13:BOP/VIP + GCSF</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 3 Cycle/3 Day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 3 Cycle/5 Day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 3 Cycle/Selected 3 Day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 4 Cycle/3 Day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 4 Cycle/5 Day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TE20:BEP 4 Cycle/Selected 3 Day</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-subgrouptypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-subgrouptypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-subgrouptypeenum')">×</button>
<h3><code>SubgroupTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Treatment Arm</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-yesnoenum" class="enum-modal" onclick="closeEnumModal('enum-modal-yesnoenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-yesnoenum')">×</button>
<h3><code>YesNoEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>No</code></td><td><code>ncit:C49487</code></td><td></td></tr>
<tr><td><code>Yes</code></td><td><code>ncit:C49488</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
    "gct": {
      "name": "gct",
      "title": "Germ Cell Tumors",
      "description": "The GCT view of the PCDC data model represents consensus data modeling by an international group of pediatric germ cell tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Malignant Germ Cell International Consortium (MaGIC). It is based on the collective requirements of its contributors."
    }
  },
  "classes": {
    "Subject": {
      "slots": [
        "consortium",
        "disease_group",
        "sex",
        "race",
        "ethnicity",
        "efs_censor_status",
        "age_at_censor_status"
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
    "StudySubgroupAssignment": {
      "slots": [
        "subgroup_type",
        "subgroup_name",
        "subgroup_assignment_order"
      ],
      "comments": [
        "D4CGNote: One observation/row per Subject",
        "(npc) ConsortiumNote: This table is tiered as Mandatory."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "ClinicalEpisode": {
      "slots": [
        "disease_phase",
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
        "condition_state",
        "medical_history_condition"
      ],
      "comments": [
        "(os) ConsortiumNote: No AOST0331/EURAMOS1 data"
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "VitalsAndAnthropometrics": {
      "slots": [
        "age_at_measurement",
        "anthropometric_measurement_type",
        "result_text",
        "result_numeric",
        "anthropometric_measurement_result_unit"
      ],
      "comments": [
        "D4CGNote: One observation/row per measurement when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "testing"
      }
    },
    "LaboratoryTest": {
      "slots": [
        "age_at_lab",
        "laboratory_test",
        "laboratory_test_method",
        "laboratory_test_specimen",
        "result_text",
        "result_numeric",
        "laboratory_test_result_unit",
        "quantification_type",
        "threshold_high",
        "threshold_low",
        "pmid_ref"
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
    "GeneticAnalysis": {
      "slots": [
        "age_at_genetic_analysis",
        "review_source",
        "genetic_analysis_method",
        "genetic_analysis_specimen",
        "alteration",
        "alteration_type",
        "chromosome",
        "iscn",
        "gene",
        "gene_fusion_partner",
        "karyotype_status",
        "total_chromosomes",
        "independent_aberrations"
      ],
      "comments": [
        "D4CGNote: One observation/row per genetic alteration",
        "(fa) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "testing"
      }
    },
    "Biospecimen": {
      "slots": [
        "biospecimen_container_type",
        "biospecimen_media",
        "biospecimen_type",
        "current_qty_unit",
        "current_qty_value"
      ],
      "comments": [
        "D4CGNote: One observation/row per biospecimen when instantiated"
      ],
      "annotations": {
        "domain": "testing"
      }
    },
    "Immunohistochemistry": {
      "slots": [
        "age_at_ihc",
        "review_source",
        "markers",
        "result_text",
        "result_numeric",
        "ihc_result_unit"
      ],
      "comments": [
        "D4CGNote: One observation/row per result when instantiated."
      ],
      "annotations": {
        "domain": "testing"
      }
    },
    "Diagnosis": {
      "slots": [
        "age_at_diag_assessment",
        "review_source",
        "diagnosis_basis",
        "diagnosis",
        "result_text",
        "result_numeric",
        "morph_code",
        "morph_code_system",
        "mature_glial_implants",
        "somatic_malignancy_type",
        "histology_grade"
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
        "stage"
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
        "review_source",
        "tumor_state",
        "detection_method",
        "site_classification",
        "disease_site",
        "laterality",
        "top_code",
        "top_code_system"
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
    "DiseaseCharacteristics": {
      "slots": [
        "risk_group",
        "gts_treatment"
      ],
      "comments": [
        "D4CGNote: One observation/row per characteristic when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "disease_attributes"
      }
    },
    "SurgicalProcedures": {
      "slots": [
        "age_at_procedure",
        "site_classification",
        "procedure_site",
        "laterality",
        "extent",
        "margins",
        "outcome"
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
        "age_at_medication_end",
        "medication_category",
        "medication",
        "medication_dose_administered",
        "medication_dose_unit"
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
    "RadiationTherapy": {
      "slots": [
        "age_at_rt_start",
        "age_at_rt_end",
        "site_classification",
        "rt_site",
        "laterality",
        "energy_type",
        "technique",
        "rt_dose",
        "rt_dose_unit",
        "boost_dose",
        "num_fraction",
        "fraction_dose",
        "fraction_dose_unit"
      ],
      "comments": [
        "D4CGNote: One observation/row per cycle OR course when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "StemCellTransplant": {
      "slots": [
        "age_at_sct",
        "total_cycles"
      ],
      "comments": [
        "D4CGNote: One observation/row per SCT when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response_method",
        "response_category",
        "response_system",
        "response_system_version",
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
        "adverse_event",
        "ae_grade",
        "outcome",
        "ae_attribution"
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
        "morph_code",
        "morph_code_text",
        "morph_code_system",
        "top_code",
        "top_code_text",
        "top_code_system"
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
    "alteration_type": {
      "slot_uri": "ncit:C13202",
      "range": "AlterationTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb,ls"
      }
    },
    "response_system": {
      "slot_uri": "ncit:C125932",
      "range": "ResponseSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,rb"
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
    "age_at_rt_start": {
      "slot_uri": "ncit:C172695",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: If TECHNIQUE == 'Brachytherapy', this should be the plaque insertion date"
      ],
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
    "histology_grade": {
      "slot_uri": "ncit:C18000",
      "range": "HistologyGradeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
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
    "rt_site": {
      "slot_uri": "ncit:C173281",
      "range": "RtSiteEnum",
      "comments": [],
      "annotations": {}
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
    "total_cycles": {
      "slot_uri": "ncit:C177373",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "genetic_analysis_specimen": {
      "slot_uri": "ncit:C70713",
      "range": "GeneticAnalysisSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "current_qty_value": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "extent": {
      "slot_uri": "ncit:C157443",
      "range": "ExtentEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
      }
    },
    "response_method": {
      "slot_uri": "ncit:C178148",
      "range": "ResponseMethodEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb"
      }
    },
    "current_qty_unit": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "morph_code": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "lt"
      }
    },
    "fraction_dose": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,npc,rb"
      }
    },
    "somatic_malignancy_type": {
      "slot_uri": "ncit:C177364",
      "range": "SomaticMalignancyTypeEnum",
      "comments": [
        "(gct) ConsortiumNote: Only associated with Somatic Malignancy"
      ],
      "annotations": {}
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
    "age_at_censor_status": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "(ews) ConsortiumNote: ConditionalStatement: if 'EFS_CENSOR_STATUS' not null"
      ],
      "annotations": {
        "tier_priority": "npc,os"
      }
    },
    "age_at_response": {
      "slot_uri": "ncit:C168856",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "subgroup_assignment_order": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "D4CGNote: <mandatory_if>subgroup_name not null</mandatory_if>"
      ],
      "annotations": {
        "tier_mandatory": "all_groups"
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
    "rt_dose": {
      "slot_uri": "ncit:C173282",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Total dose of radiation over the period encompassed by AGE_AT_RT_START to _AGE_AT_RT_END"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,npc",
        "tier_optional": "rb,fprh"
      }
    },
    "gene_fusion_partner": {
      "slot_uri": "ncit:C171253",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "ls"
      }
    },
    "medication_dose_administered": {
      "slot_uri": "ncit:C94394",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Total dose of the chemotherapy agent administered to the subject over the indicated start and end time points. Note: Only fill in this variable if this information is available.",
        "(gct) ConsortiumNote: Total dose of the chemotherapy agent administered to the subject over the indicated start and end time points.",
        "(hl) ConsortiumNote: Total dose of the chemotherapy agent administered to the subject over the indicated start and end time points. Note: Only fill in this variable if this information is available.",
        "(rb) ConsortiumNote: Total dose of the chemotherapy agent administered to the subject over the indicated start and end time points. Note: Only fill in this variable if this information is available."
      ],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc"
      }
    },
    "ae_attribution": {
      "slot_uri": "ncit:C41358",
      "range": "AeAttributionEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa"
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
    "genetic_analysis_method": {
      "slot_uri": "ncit:C158954",
      "range": "GeneticAnalysisMethodEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,aml"
      }
    },
    "age_at_genetic_analysis": {
      "slot_uri": "ncit:C168848",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "num_fraction": {
      "slot_uri": "ncit:C175034",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: Only applies to external beam"
      ],
      "annotations": {
        "tier_optional": "npc,rb"
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
    "response_category": {
      "slot_uri": "ncit:C173306",
      "range": "ResponseCategoryEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb",
        "tier_optional": "npc"
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
    "alteration": {
      "slot_uri": "ncit:C3910",
      "range": "AlterationEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple molecular abnormalities, include one observation per molecular abnormality.",
        "(nbl) ConsortiumNote: If multiple molecular abnormalities, include one observation per molecular abnormality."
      ],
      "annotations": {
        "tier_priority": "rb,aml"
      }
    },
    "age_at_medication_end": {
      "slot_uri": "ncit:C172686",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc"
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
    "ihc_result_unit": {
      "slot_uri": "",
      "range": "IhcResultUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_sct": {
      "slot_uri": "ncit:C168853",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "quantification_type": {
      "slot_uri": "ncit:C49142",
      "range": "QuantificationTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "tumor_state": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "efs_censor_status": {
      "slot_uri": "",
      "range": "EfsCensorStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,os"
      }
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
    "boost_dose": {
      "slot_uri": "ncit:C185679",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "chromosome": {
      "slot_uri": "ncit:C13202",
      "range": "ChromosomeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb,aml",
        "tier_optional": "ls"
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
    "age_at_lkss": {
      "slot_uri": "ncit:C168844",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "energy_type": {
      "slot_uri": "ncit:C15313",
      "range": "EnergyTypeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,rb",
        "tier_optional": "npc"
      }
    },
    "ae_grade": {
      "slot_uri": "ncit:C166200",
      "range": "AeGradeEnum",
      "comments": [
        "(aml) ConsortiumNote: Only applicable for CTCAE- or EBMT-coded AEs",
        "(all) ConsortiumNote: Only applicable for CTCAE- or EBMT-coded AEs"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,rb",
        "tier_optional": "npc"
      }
    },
    "threshold_low": {
      "slot_uri": "ncit:C177366",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "result_text": {
      "slot_uri": "ncit:C36292",
      "range": "string",
      "comments": [
        "D4CGNote: Note: String result should include anything that is not a purely numeric result, i.e. 'Positive', 'Negative', 'Present', 'Absent', 'Yes', 'No', 'Elevated,' 'Depressed', 'Above threshold', 'Below threshold', '>30', 'Greater than 30', etc.",
        "(rb) ConsortiumNote: For Visual Acuity tests, report specifically these results: 'Blinks to Light', 'Fix and Follow', 'Central Steady Maintained', 'Counting Fingers', 'Hand Motion', 'Light Perception', 'No Light Perception'",
        "D4CGNote: Note: String result can include anything that is not a single numeric result, i.e. 'Positive', 'Negative', 'Present', 'Absent', 'Yes', 'No', 'Elevated,' 'Depressed', 'Above threshold', 'Below threshold', ranges, as well as bucketed categories, etc... Note: Only fill in this variable when the available data is anything EXCEPT a single numeric value, and include the entire available data as a string, including units if applicable",
        "D4CGNote: modifier note",
        "(ls) ConsortiumNote: Positive/Negative or Her2 Scores: 0, 1+, 2+, 3+"
      ],
      "annotations": {
        "tier_priority": "aml,fa,npc,rb",
        "tier_optional": "ls"
      }
    },
    "gene": {
      "slot_uri": "ncit:C173595",
      "range": "string",
      "comments": [
        "(fa) ConsortiumNote: Prioritize reporting the following Genes: FANCA, FANCB, FANCC, FANCD1/BRCA2, FANCD2, FANCD3, FANCE, FANCF, FANCG, FANCI, FANCJ/PALB2, FANCO/RAD51C, FANCP/SLCX4, FANCQ/ERCC4/XPF, FANCR/RAD51, FANCS/BRCA1, FANCT/UBE2T, FANCU/XRCC2, FANCV/REV7/MAD2L2, FANCW/RFWD3, and FANCX/FAAP100."
      ],
      "annotations": {
        "tier_priority": "fa,aml",
        "tier_optional": "rb,ls"
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
    "age_at_rt_end": {
      "slot_uri": "ncit:C172696",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: If TECHNIQUE == 'Brachytherapy', this should be the plaque removal date"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb",
        "tier_optional": "npc"
      }
    },
    "age_at_measurement": {
      "slot_uri": "ncit:C154628",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "biospecimen_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "anthropometric_measurement_result_unit": {
      "slot_uri": "",
      "range": "AnthropometricMeasurementResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
      }
    },
    "medication_category": {
      "slot_uri": "ncit:C459",
      "range": "MedicationCategoryEnum",
      "comments": [],
      "annotations": {}
    },
    "race": {
      "slot_uri": "ncit:C17049",
      "range": "RaceEnum",
      "comments": [
        "(fa) ConsortiumNote: US-based patients only"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb,aml",
        "tier_optional": "fa,npc,ls"
      }
    },
    "biospecimen_media": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "medication_dose_unit": {
      "slot_uri": "ncit:C17395",
      "range": "MedicationDoseUnitEnum",
      "comments": [
        "(aml) ConsortiumNote: Unit for TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED must be the same.",
        "(hl) ConsortiumNote: Unit for TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED must be the same.",
        "(rb) ConsortiumNote: Unit for TOTAL_DOSE_ADMINISTERED and TOTAL_DOSE_INTENDED must be the same."
      ],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc"
      }
    },
    "laboratory_test_method": {
      "slot_uri": "ncit:C83312",
      "range": "LaboratoryTestMethodEnum",
      "comments": [
        "(hl) ConsortiumNote: Only fill in this variable only when relevant, for example if the LAB_TEST is 'blasts' and the LAB_SAMPLE_SOURCE is 'Bone Marrow' - ie bone marrow blasts"
      ],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "mature_glial_implants": {
      "slot_uri": "ncit:C177363",
      "range": "YesNoEnum",
      "comments": [
        "(gct) ConsortiumNote: Only associated with Mature and Immature Teratoma"
      ],
      "annotations": {}
    },
    "biospecimen_container_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "pmid_ref": {
      "slot_uri": "ncit:C127797",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "total_chromosomes": {
      "slot_uri": "ncit:C177370",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "outcome": {
      "slot_uri": "ncit:C49489",
      "range": "OutcomeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "subgroup_name": {
      "slot_uri": "ncit:C15538",
      "range": "SubgroupNameEnum",
      "comments": [
        "(ews) ConsortiumNote: Assigned at the time of randomization"
      ],
      "annotations": {
        "tier_mandatory": "hl,npc",
        "tier_priority": "os,aml"
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
    "threshold_high": {
      "slot_uri": "ncit:C177365",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "technique": {
      "slot_uri": "ncit:C15313",
      "range": "TechniqueEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc",
        "tier_priority": "rb"
      }
    },
    "markers": {
      "slot_uri": "ncit:C51944",
      "range": "MarkersEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "rt_dose_unit": {
      "slot_uri": "ncit:C18068",
      "range": "RtDoseUnitEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,npc",
        "tier_optional": "rb,fprh"
      }
    },
    "detection_method": {
      "slot_uri": "ncit:C173262",
      "range": "DetectionMethodEnum",
      "comments": [
        "(aml) ConsortiumNote: If there were multiple detection methods, include one observation per detection method. If disease site provided, detection method should be linked to each disease site. If no disease sites provided, detection method should be linked to overall disease.",
        "(hl) ConsortiumNote: If there were multiple detection methods, include one observation per detection method. If disease site provided, detection method should be linked to each disease site. If no disease sites provided, detection method should be linked to overall disease."
      ],
      "annotations": {
        "tier_priority": "fa,rb",
        "tier_optional": "npc,ls"
      }
    },
    "karyotype_status": {
      "slot_uri": "ncit:C168871",
      "range": "KaryotypeStatusEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_procedure": {
      "slot_uri": "ncit:C175008",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "fraction_dose_unit": {
      "slot_uri": "ncit:C18068",
      "range": "FractionDoseUnitEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,rb"
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
    "gts_treatment": {
      "slot_uri": "ncit:C177376",
      "range": "GtsTreatmentEnum",
      "comments": [],
      "annotations": {}
    },
    "morph_code_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "age_at_ihc": {
      "slot_uri": "ncit:C175006",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "response_system_version": {
      "slot_uri": "ncit:C175042",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "independent_aberrations": {
      "slot_uri": "ncit:C173279",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "iscn": {
      "slot_uri": "ncit:C156450",
      "range": "string",
      "comments": [
        "(aml) ConsortiumNote: Only fill in this variable if MOLECULAR_ANALYSIS_METHOD is 'Karyotype'"
      ],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb,ls"
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
    "condition_state": {
      "slot_uri": "",
      "range": "ActiveResolvedEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,npc",
        "tier_priority": "rb",
        "tier_optional": "hl,rb,ls"
      }
    },
    "laboratory_test_specimen": {
      "slot_uri": "ncit:C70713",
      "range": "LaboratoryTestSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa",
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
      }
    },
    "risk_group": {
      "slot_uri": "",
      "range": "RiskGroupEnum",
      "comments": [],
      "annotations": {}
    },
    "subgroup_type": {
      "slot_uri": "",
      "range": "SubgroupTypeEnum",
      "comments": [
        "D4CGNote: <mandatory_if>subgroup_name not null</mandatory_if>"
      ],
      "annotations": {
        "tier_mandatory": "all_groups"
      }
    },
    "anthropometric_measurement_type": {
      "slot_uri": "ncit:C219071",
      "range": "AnthropometricMeasurementTypeEnum",
      "comments": [
        "(cns) ConsortiumNote: BMI should only be what is reported on CRF, not calculated from weight and height when submitting data to the PCDC",
        "(ews) ConsortiumNote: BMI should only be what is reported on CRF, not calculated from weight and height when submitting data to the PCDC",
        "(hl) ConsortiumNote: BMI should only be what is reported on CRF, not calculated from weight and height when submitting data to the PCDC"
      ],
      "annotations": {
        "tier_mandatory": "fa,npc",
        "tier_optional": "ls"
      }
    },
    "ethnicity": {
      "slot_uri": "ncit:C16564",
      "range": "EthnicityEnum",
      "comments": [
        "(fa) ConsortiumNote: US-based patients only"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb,aml",
        "tier_optional": "fa,ls"
      }
    },
    "age_at_staging": {
      "slot_uri": "ncit:C177359",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    }
  },
  "enums": {
    "DiagnosisBasisEnum": {
      "permissible_values": {
        "Histological": {
          "meaning": "ncit:C25526",
          "comments": []
        },
        "Integrated": {
          "meaning": "ncit:C165682",
          "comments": []
        }
      }
    },
    "AnthropometricMeasurementTypeEnum": {
      "permissible_values": {
        "Height": {
          "meaning": "ncit:C164634",
          "comments": []
        },
        "Weight": {
          "meaning": "ncit:C81328",
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
    "HistologyGradeEnum": {
      "permissible_values": {
        "Norris Immature Teratoma Grading System >> Grade 1": {
          "meaning": "ncit:C28077",
          "comments": [
            "(gct) ConsortiumNote: Only associated with Immature Teratoma."
          ]
        },
        "Norris Immature Teratoma Grading System >> Grade 2": {
          "meaning": "ncit:C28078",
          "comments": []
        },
        "Norris Immature Teratoma Grading System >> Grade 3": {
          "meaning": "ncit:C28079",
          "comments": []
        }
      }
    },
    "ResponseEnum": {
      "permissible_values": {
        "Choi >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "Choi >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "Choi >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "Choi >> Stable Disease": {
          "meaning": "",
          "comments": []
        },
        "PERCIST >> Complete Metabolic Response": {
          "meaning": "",
          "comments": []
        },
        "PERCIST >> Partial Metabolic Response": {
          "meaning": "",
          "comments": []
        },
        "PERCIST >> Progressive Metabolic Disease": {
          "meaning": "",
          "comments": []
        },
        "PERCIST >> Stable Metabolic Disease": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Complete Response": {
          "meaning": "ncit:C4870",
          "comments": [
            "(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response."
          ]
        },
        "System NOS >> Partial Response": {
          "meaning": "ncit:C18058",
          "comments": []
        },
        "System NOS >> Progressive Disease": {
          "meaning": "ncit:C35571",
          "comments": []
        },
        "System NOS >> Stable Disease": {
          "meaning": "ncit:C18213",
          "comments": []
        },
        "mRECIST >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "mRECIST >> Incomplete Reseponse/Stable Disease": {
          "meaning": "",
          "comments": [
            "ConsortiumNote: Use for non-target lesions."
          ]
        },
        "mRECIST >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "mRECIST >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "mRECIST >> Stable Disease": {
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
    "SubgroupTypeEnum": {
      "permissible_values": {
        "Treatment Arm": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AlterationTypeEnum": {
      "permissible_values": {
        "Deletion": {
          "meaning": "ncit:C16606",
          "comments": []
        },
        "Duplication": {
          "meaning": "",
          "comments": []
        },
        "Indel": {
          "meaning": "",
          "comments": []
        },
        "Insertion": {
          "meaning": "SO:0000667",
          "comments": []
        },
        "Inversion": {
          "meaning": "",
          "comments": []
        },
        "Rearrangement, NOS": {
          "meaning": "",
          "comments": []
        },
        "Substitution": {
          "meaning": "SO:1000002",
          "comments": []
        },
        "Translocation": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "RiskGroupEnum": {
      "permissible_values": {
        "IGCCC >> Good": {
          "meaning": "",
          "comments": []
        },
        "IGCCC >> Intermediate": {
          "meaning": "",
          "comments": []
        },
        "IGCCC >> Poor": {
          "meaning": "",
          "comments": []
        },
        "MaGIC >> Low": {
          "meaning": "",
          "comments": []
        },
        "MaGIC >> Poor": {
          "meaning": "",
          "comments": []
        },
        "MaGIC >> Standard": {
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
        "Ascitic Fluid": {
          "meaning": "ncit:C159203",
          "comments": []
        },
        "Bone, NOS": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Cervix Lymph Node": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Frontal Cortex": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "",
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
        "Lymph Node": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Mediastinal Lymph Node": {
          "meaning": "ncit:C32628",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C6634",
          "comments": []
        },
        "Occipital Cortex": {
          "meaning": "ncit:C32250",
          "comments": []
        },
        "Omentum": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Omentum Lymph Node": {
          "meaning": "ncit:C177766",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Parietal Cortex": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Pelvic Lymph Node": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": [
            "(ews) ConsortiumNote: Included so that peritoneal effusions can be reported."
          ]
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Retroperitoneum Lymph Node": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Sacrococcygeal": {
          "meaning": "ncit:C33506",
          "comments": []
        },
        "Spinal Cord": {
          "meaning": "ncit:C12464",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
          "comments": []
        },
        "Suprasellar/Neurohypophyseal": {
          "meaning": "ncit:C42602",
          "comments": []
        },
        "Temporal Cortex": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Testis": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Thalamus": {
          "meaning": "ncit:C12459",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
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
    "YesNoEnum": {
      "permissible_values": {
        "No": {
          "meaning": "ncit:C49487",
          "comments": []
        },
        "Yes": {
          "meaning": "ncit:C49488",
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
    "LaboratoryTestSpecimenEnum": {
      "permissible_values": {
        "Blood": {
          "meaning": "ncit:C17610",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Peritoneal Fluid": {
          "meaning": "ncit:C185197",
          "comments": []
        },
        "Plasma": {
          "meaning": "ncit:C185204",
          "comments": []
        },
        "Pleural Fluid": {
          "meaning": "ncit:C77613",
          "comments": []
        },
        "Serum": {
          "meaning": "ncit:C178987",
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
    "EfsCensorStatusEnum": {
      "permissible_values": {
        "Subject has had one or more events": {
          "meaning": "",
          "comments": []
        },
        "Subject is censored (i.e. has had no events(s))": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ResponseMethodEnum": {
      "permissible_values": {
        "Imaging": {
          "meaning": "ncit:C17220",
          "comments": []
        },
        "Pathology": {
          "meaning": "ncit:C18189",
          "comments": []
        },
        "Tumor Marker": {
          "meaning": "ncit:C17369",
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
    "RtSiteEnum": {
      "permissible_values": {
        "Frontal Cortex": {
          "meaning": "ncit:C32635",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Occiptial Cortex": {
          "meaning": "ncit:C12757",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Parietal Cortex": {
          "meaning": "ncit:C12766",
          "comments": []
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C28256",
          "comments": []
        },
        "Sacrococcygeal": {
          "meaning": "ncit:C33506",
          "comments": []
        },
        "Spinal Cord": {
          "meaning": "ncit:C12464",
          "comments": []
        },
        "Suprasellar/Neurohypophyseal": {
          "meaning": "ncit:C177357",
          "comments": []
        },
        "Temporal Cortex": {
          "meaning": "ncit:C12797",
          "comments": []
        },
        "Testes": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Thalamus": {
          "meaning": "ncit:C12459",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
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
    "ResponseSystemEnum": {
      "permissible_values": {
        "Choi": {
          "meaning": "ncit:C122394",
          "comments": []
        },
        "PERCIST": {
          "meaning": "ncit:C126039",
          "comments": []
        },
        "RECIST": {
          "meaning": "ncit:C49164",
          "comments": []
        },
        "WHO": {
          "meaning": "ncit:C75419",
          "comments": []
        },
        "mRECIST": {
          "meaning": "ncit:C126031",
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
    "AnthropometricMeasurementResultUnitEnum": {
      "permissible_values": {
        "cm": {
          "meaning": "ncit:C49668",
          "comments": []
        },
        "kg": {
          "meaning": "ncit:C28252",
          "comments": []
        }
      }
    },
    "LateralityEnum": {
      "permissible_values": {
        "Bilateral": {
          "meaning": "ncit:C13332",
          "comments": []
        },
        "Left": {
          "meaning": "ncit:C160200",
          "comments": []
        },
        "Midline": {
          "meaning": "ncit:C81170",
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
        "AJCC >> Stage 0": {
          "meaning": "ncit:C4523",
          "comments": []
        },
        "AJCC >> Stage 1": {
          "meaning": "ncit:C7901",
          "comments": []
        },
        "AJCC >> Stage 1A": {
          "meaning": "ncit:C6361",
          "comments": []
        },
        "AJCC >> Stage 1B": {
          "meaning": "ncit:C6362",
          "comments": []
        },
        "AJCC >> Stage 1s": {
          "meaning": "ncit:C6363",
          "comments": []
        },
        "AJCC >> Stage 2": {
          "meaning": "ncit:C9073",
          "comments": []
        },
        "AJCC >> Stage 2A": {
          "meaning": "ncit:C6364",
          "comments": []
        },
        "AJCC >> Stage 2B": {
          "meaning": "ncit:C6365",
          "comments": []
        },
        "AJCC >> Stage 2C": {
          "meaning": "ncit:C6366",
          "comments": []
        },
        "AJCC >> Stage 3": {
          "meaning": "ncit:C9074",
          "comments": []
        },
        "AJCC >> Stage 3A": {
          "meaning": "ncit:C6369",
          "comments": []
        },
        "AJCC >> Stage 3B": {
          "meaning": "ncit:C6368",
          "comments": []
        },
        "AJCC >> Stage 3C": {
          "meaning": "ncit:C6367",
          "comments": []
        },
        "COG >> Stage 1": {
          "meaning": "ncit:C27966",
          "comments": []
        },
        "COG >> Stage 2": {
          "meaning": "ncit:C28054",
          "comments": []
        },
        "COG >> Stage 3": {
          "meaning": "ncit:C27970",
          "comments": []
        },
        "COG >> Stage 4": {
          "meaning": "ncit:C27971",
          "comments": []
        },
        "FIGO >> Stage 1": {
          "meaning": "ncit:C96244",
          "comments": []
        },
        "FIGO >> Stage 2": {
          "meaning": "ncit:C96252",
          "comments": []
        },
        "FIGO >> Stage 3": {
          "meaning": "ncit:C96255",
          "comments": []
        },
        "FIGO >> Stage 4": {
          "meaning": "ncit:C96261",
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
    "QuantificationTypeEnum": {
      "permissible_values": {
        "Absolute": {
          "meaning": "ncit:C45829",
          "comments": []
        },
        "Relative": {
          "meaning": "ncit:C45830",
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
    "MedicationDoseUnitEnum": {
      "permissible_values": {
        "IU": {
          "meaning": "ncit:C48579",
          "comments": []
        },
        "MBq": {
          "meaning": "",
          "comments": []
        },
        "mg": {
          "meaning": "ncit:C28253",
          "comments": []
        },
        "mg/kg": {
          "meaning": "ncit:C105468",
          "comments": []
        },
        "mg/m2": {
          "meaning": "ncit:C67402",
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
    "SexEnum": {
      "permissible_values": {
        "Female": {
          "meaning": "ncit:C16576",
          "comments": []
        },
        "Male": {
          "meaning": "ncit:C20197",
          "comments": []
        },
        "Undifferentiated": {
          "meaning": "ncit:C41438",
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
    "ActiveResolvedEnum": {
      "permissible_values": {
        "Active": {
          "meaning": "",
          "comments": []
        },
        "Resolved": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ChromosomeEnum": {
      "permissible_values": {
        "1": {
          "meaning": "ncit:C13204",
          "comments": []
        },
        "10": {
          "meaning": "ncit:C13205",
          "comments": []
        },
        "11": {
          "meaning": "ncit:C13206",
          "comments": []
        },
        "12": {
          "meaning": "ncit:C13207",
          "comments": []
        },
        "13": {
          "meaning": "ncit:C13208",
          "comments": []
        },
        "14": {
          "meaning": "ncit:C13209",
          "comments": []
        },
        "15": {
          "meaning": "ncit:C13210",
          "comments": []
        },
        "16": {
          "meaning": "ncit:C13211",
          "comments": []
        },
        "17": {
          "meaning": "ncit:C13212",
          "comments": []
        },
        "18": {
          "meaning": "ncit:C13213",
          "comments": []
        },
        "19": {
          "meaning": "ncit:C13214",
          "comments": []
        },
        "2": {
          "meaning": "ncit:C13215",
          "comments": []
        },
        "20": {
          "meaning": "ncit:C13216",
          "comments": []
        },
        "21": {
          "meaning": "ncit:C13217",
          "comments": []
        },
        "22": {
          "meaning": "ncit:C13218",
          "comments": []
        },
        "3": {
          "meaning": "ncit:C13219",
          "comments": []
        },
        "4": {
          "meaning": "ncit:C13220",
          "comments": []
        },
        "5": {
          "meaning": "ncit:C13221",
          "comments": []
        },
        "6": {
          "meaning": "ncit:C13222",
          "comments": []
        },
        "7": {
          "meaning": "ncit:C13223",
          "comments": []
        },
        "8": {
          "meaning": "ncit:C13224",
          "comments": []
        },
        "9": {
          "meaning": "ncit:C13225",
          "comments": []
        },
        "X": {
          "meaning": "ncit:C13285",
          "comments": []
        },
        "Y": {
          "meaning": "ncit:C13286",
          "comments": []
        }
      }
    },
    "IhcResultUnitEnum": {
      "permissible_values": {
        "%": {
          "meaning": "ncit:C48570",
          "comments": []
        },
        "Intensity": {
          "meaning": "ncit:C25539",
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
        "Secondary Malignancy": {
          "meaning": "ncit:C4968",
          "comments": [
            "D4CGNote: Use the Subsequent Malignant Neoplasm table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL."
          ]
        },
        "Treatment-Related Mortality": {
          "meaning": "ncit:C166165",
          "comments": [
            "D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL."
          ]
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
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
    "SomaticMalignancyTypeEnum": {
      "permissible_values": {
        "Adenocarcinoma": {
          "meaning": "ncit:C2852",
          "comments": []
        },
        "Malignant Histiocytosis": {
          "meaning": "ncit:C7202",
          "comments": []
        },
        "Rhabdomyosarcoma": {
          "meaning": "ncit:C3359",
          "comments": []
        },
        "Sarcoma, NOS": {
          "meaning": "ncit:C9118",
          "comments": []
        },
        "Squamous Cell Carcinoma": {
          "meaning": "ncit:C2929",
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
    "StudyIdEnum": {
      "permissible_values": {
        "AGCT0132": {
          "meaning": "ncit:C177343",
          "comments": []
        },
        "AGCT01P1": {
          "meaning": "ncit:C177342",
          "comments": []
        },
        "AGCT0521": {
          "meaning": "ncit:C177344",
          "comments": []
        },
        "GC1": {
          "meaning": "ncit:C177335",
          "comments": []
        },
        "GC2": {
          "meaning": "ncit:C177336",
          "comments": []
        },
        "GOG0078": {
          "meaning": "",
          "comments": []
        },
        "GOG0090": {
          "meaning": "",
          "comments": []
        },
        "GOG0116": {
          "meaning": "ncit:C177339",
          "comments": []
        },
        "P9749": {
          "meaning": "ncit:C177340",
          "comments": []
        },
        "POG9049": {
          "meaning": "ncit:C177341",
          "comments": []
        },
        "TCGM2004": {
          "meaning": "",
          "comments": []
        },
        "TE04": {
          "meaning": "ncit:C177345",
          "comments": []
        },
        "TE05": {
          "meaning": "ncit:C177346",
          "comments": []
        },
        "TE08": {
          "meaning": "ncit:C177347",
          "comments": []
        },
        "TE09": {
          "meaning": "ncit:C177349",
          "comments": []
        },
        "TE13": {
          "meaning": "ncit:C177350",
          "comments": []
        },
        "TE20": {
          "meaning": "ncit:C177351",
          "comments": []
        },
        "TE22": {
          "meaning": "ncit:C177348",
          "comments": []
        },
        "TGM85": {
          "meaning": "ncit:C177332",
          "comments": []
        },
        "TGM90": {
          "meaning": "ncit:C177333",
          "comments": []
        },
        "TGM95": {
          "meaning": "ncit:C177334",
          "comments": []
        },
        "TIP": {
          "meaning": "ncit:C177352",
          "comments": []
        }
      }
    },
    "MedicationCategoryEnum": {
      "permissible_values": {
        "Antineoplastic Agent": {
          "meaning": "ncit:C274",
          "comments": []
        },
        "Supportive Care Agent": {
          "meaning": "ncit:C70902",
          "comments": []
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
    "EnergyTypeEnum": {
      "permissible_values": {
        "Photon": {
          "meaning": "ncit:C88112",
          "comments": []
        },
        "Proton": {
          "meaning": "ncit:C66897",
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
    "DiagnosisEnum": {
      "permissible_values": {
        "Choriocarcinoma": {
          "meaning": "ncit:C2948",
          "comments": []
        },
        "Dysgerminoma": {
          "meaning": "icdo:9060/3",
          "comments": []
        },
        "Embryonal Carcinoma": {
          "meaning": "ncit:C3752",
          "comments": []
        },
        "Germinoma": {
          "meaning": "ncit:C3753",
          "comments": []
        },
        "Immature Teratoma": {
          "meaning": "ncit:C4286",
          "comments": []
        },
        "Malignant Teratoma": {
          "meaning": "ncit:C4287",
          "comments": []
        },
        "Mature Teratoma": {
          "meaning": "ncit:C9015",
          "comments": []
        },
        "Mixed Germ Cell Tumor": {
          "meaning": "ncit:C4290",
          "comments": []
        },
        "Necrotic Tumor": {
          "meaning": "ncit:C36029",
          "comments": []
        },
        "Primitive Neuroectodermal Tumor": {
          "meaning": "icdo:9473/3",
          "comments": []
        },
        "Seminoma": {
          "meaning": "ncit:C9309",
          "comments": []
        },
        "Seminoma/Dysgerminoma/Germinoma": {
          "meaning": "ncit:C121618",
          "comments": []
        },
        "Somatic Malignancy": {
          "meaning": "ncit:C18060",
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
        },
        "Yolk Sac Tumor": {
          "meaning": "icdo:9071/3",
          "comments": []
        },
        "Teratoma, NOS": {
          "meaning": "icdo:9080/1",
          "comments": []
        }
      }
    },
    "PresentAbsentEnum": {
      "permissible_values": {
        "Absent": {
          "meaning": "ncit:C25567",
          "comments": []
        },
        "Not Evaluated": {
          "meaning": "ncit:C103424",
          "comments": []
        },
        "Present": {
          "meaning": "ncit:C25566",
          "comments": []
        }
      }
    },
    "RaceEnum": {
      "permissible_values": {
        "American Indian or Alaska Native": {
          "meaning": "ncit:C41259",
          "comments": []
        },
        "Asian": {
          "meaning": "ncit:C41260",
          "comments": []
        },
        "Black or African American": {
          "meaning": "ncit:C16352",
          "comments": []
        },
        "Multiracial": {
          "meaning": "ncit:C67109",
          "comments": []
        },
        "Native Hawaiian or Other Pacific Islander": {
          "meaning": "ncit:C41219",
          "comments": []
        },
        "White": {
          "meaning": "ncit:C41261",
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
    "DetectionMethodEnum": {
      "permissible_values": {
        "Imaging": {
          "meaning": "ncit:C17369",
          "comments": []
        },
        "Imaging, NOS": {
          "meaning": "ncit:C17369",
          "comments": []
        },
        "PET Scan": {
          "meaning": "ncit:C17007",
          "comments": []
        },
        "Tumor Marker": {
          "meaning": "ncit:C17220",
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
    "GtsTreatmentEnum": {
      "permissible_values": {
        "Chemotherapy": {
          "meaning": "ncit:C15632",
          "comments": []
        },
        "Surgery": {
          "meaning": "ncit:C15329",
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
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Frontal Cortex": {
          "meaning": "ncit:C32635",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Occipital Cortex": {
          "meaning": "ncit:C12757",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Parietal Cortex": {
          "meaning": "ncit:C12766",
          "comments": []
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Sacrococcygeal": {
          "meaning": "ncit:C33506",
          "comments": []
        },
        "Spinal Cord": {
          "meaning": "ncit:C12464",
          "comments": []
        },
        "Suprasellar/Neurohypophyseal": {
          "meaning": "ncit:C177357",
          "comments": []
        },
        "Temporal Cortex": {
          "meaning": "ncit:C12797",
          "comments": []
        },
        "Testis": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Thalamus": {
          "meaning": "ncit:C12459",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
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
    "GeneticAnalysisMethodEnum": {
      "permissible_values": {
        "Cytogenetics, Karyotyping": {
          "meaning": "ncit:C25215",
          "comments": []
        },
        "Cytogenetics, NOS": {
          "meaning": "ncit:C16487",
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
    "KaryotypeStatusEnum": {
      "permissible_values": {
        "Abnormal Karyotype": {
          "meaning": "ncit:C168875",
          "comments": []
        },
        "Normal Karyotype": {
          "meaning": "ncit:C173277",
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
    "DiseaseGroupEnum": {
      "permissible_values": {
        "GCT": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Amifostine": {
          "meaning": "ncit:C488",
          "comments": []
        },
        "Bleomycin": {
          "meaning": "rxcui:1622",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Cyclophosphamide": {
          "meaning": "rxcui:3002",
          "comments": []
        },
        "Dactinomycin": {
          "meaning": "rxcui:3100",
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
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "rxcui:5657",
          "comments": []
        },
        "Melphalan": {
          "meaning": "rxcui:6718",
          "comments": []
        },
        "Paclitaxel": {
          "meaning": "ncit:C1411",
          "comments": []
        },
        "Sodium Thiosulfate": {
          "meaning": "ncit:C1230",
          "comments": [
            "(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'",
            "(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention"
          ]
        },
        "Vinblastine": {
          "meaning": "rxcui:11198",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
          "comments": []
        }
      }
    },
    "EthnicityEnum": {
      "permissible_values": {
        "Hispanic or Latino": {
          "meaning": "ncit:C17459",
          "comments": []
        },
        "Not Hispanic or Latino": {
          "meaning": "ncit:C41222",
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
    "LaboratoryTestMethodEnum": {
      "permissible_values": {
        "Cytology": {
          "meaning": "ncit:C16491",
          "comments": []
        },
        "MicroRNA Sequencing": {
          "meaning": "ncit:C156057",
          "comments": []
        },
        "ddPCR": {
          "meaning": "ncit:C166064",
          "comments": []
        },
        "qPCR": {
          "meaning": "ncit:C51962",
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
    "OutcomeEnum": {
      "permissible_values": {
        "Death, Contributory": {
          "meaning": "ncit:C168948",
          "comments": []
        },
        "Death, Noncontributory": {
          "meaning": "ncit:C173315",
          "comments": []
        },
        "Not Yet Recovered": {
          "meaning": "ncit:C49494",
          "comments": []
        },
        "Recovered": {
          "meaning": "ncit:C49498",
          "comments": []
        },
        "Recovered with Sequelae": {
          "meaning": "ncit:C49495",
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
    "MarkersEnum": {
      "permissible_values": {
        "CD30": {
          "meaning": "ncit:C38906",
          "comments": []
        },
        "GPC3": {
          "meaning": "ncit:C88175",
          "comments": []
        },
        "beta-catenin": {
          "meaning": "ncit:C17478",
          "comments": []
        }
      }
    },
    "MarginsEnum": {
      "permissible_values": {
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
    "AeGradeEnum": {
      "permissible_values": {
        "System NOS >> Grade 1": {
          "meaning": "ncit:C41338",
          "comments": []
        },
        "System NOS >> Grade 2": {
          "meaning": "ncit:C41339",
          "comments": []
        },
        "System NOS >> Grade 3": {
          "meaning": "ncit:C41340",
          "comments": []
        },
        "System NOS >> Grade 4": {
          "meaning": "ncit:C41337",
          "comments": []
        },
        "System NOS >> Grade 5": {
          "meaning": "ncit:C48275",
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
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        }
      }
    },
    "SubgroupNameEnum": {
      "permissible_values": {
        "TE09:BEP (Cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "TE09:CEP (Carboplatin)": {
          "meaning": "",
          "comments": []
        },
        "TE13:BEP": {
          "meaning": "",
          "comments": []
        },
        "TE13:BEP + GCSF": {
          "meaning": "",
          "comments": []
        },
        "TE13:BOP/VIP": {
          "meaning": "",
          "comments": []
        },
        "TE13:BOP/VIP + GCSF": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 3 Cycle/3 Day": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 3 Cycle/5 Day": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 3 Cycle/Selected 3 Day": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 4 Cycle/3 Day": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 4 Cycle/5 Day": {
          "meaning": "",
          "comments": []
        },
        "TE20:BEP 4 Cycle/Selected 3 Day": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ResponseCategoryEnum": {
      "permissible_values": {
        "Overall Response": {
          "meaning": "ncit:C96613",
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
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Gonadoblastoma": {
          "meaning": "ncit:C3754",
          "comments": []
        },
        "Klinefelter Syndrome": {
          "meaning": "ncit:C34752",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "MaGIC": {
          "meaning": "ncit:C192759",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Neuropathy": {
          "meaning": "ncit:C4731",
          "comments": []
        },
        "Ototoxicity": {
          "meaning": "ncit:C66929",
          "comments": []
        },
        "Pulmonary Toxicity": {
          "meaning": "ncit:C177374",
          "comments": []
        },
        "Renal Toxicity": {
          "meaning": "ncit:C115459",
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
    "GeneticAnalysisSpecimenEnum": {
      "permissible_values": {
        "Primary Tumor": {
          "meaning": "ncit:C8509",
          "comments": []
        },
        "Metastatic Tumor": {
          "meaning": "ncit:C3261",
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
        "Regional Nodes": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'"
          ]
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
        "Cytology Malignant Cells": {
          "meaning": "ncit:C74660",
          "comments": []
        },
        "LDH": {
          "meaning": "ncit:C64855",
          "comments": []
        },
        "cfDNA": {
          "meaning": "ncit:C128274",
          "comments": []
        },
        "miR-367-3p": {
          "meaning": "ncit:C177302",
          "comments": []
        },
        "miR-371a-3p": {
          "meaning": "ncit:C158711",
          "comments": []
        },
        "miR-372-3p": {
          "meaning": "ncit:C82190",
          "comments": []
        },
        "miR-373-3p": {
          "meaning": "ncit:C82191",
          "comments": []
        },
        "miR-375-3p": {
          "meaning": "ncit:C101665",
          "comments": []
        },
        "beta-hCG": {
          "meaning": "ncit:C64851",
          "comments": []
        }
      }
    },
    "ExtentEnum": {
      "permissible_values": {
        "Complete Resection": {
          "meaning": "ncit:C175027",
          "comments": []
        },
        "Gross Total": {
          "meaning": "ncit:C131672",
          "comments": []
        },
        "Partial Resection": {
          "meaning": "ncit:C131680",
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
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "U/L": {
          "meaning": "ncit:C67456",
          "comments": []
        },
        "cp/mL": {
          "meaning": "",
          "comments": []
        },
        "ng/mL": {
          "meaning": "ncit:C67306",
          "comments": []
        }
      }
    },
    "RtDoseUnitEnum": {
      "permissible_values": {
        "cGy": {
          "meaning": "ncit:C64693",
          "comments": []
        },
        "Gy": {
          "meaning": "ncit:C18063",
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
    }
  }
}
```

</div>