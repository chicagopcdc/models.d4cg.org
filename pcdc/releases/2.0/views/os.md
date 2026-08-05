---
layout: default
title: Osteosarcoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*OS View*

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
- [Liver Tumors](lt)
- [Neuroblastoma](nbl)
- [Nasopharyngeal Carcinoma](npc)
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- **Osteosarcoma**
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The OS view of the PCDC data model represents consensus data modeling by an international group of pediatric osteosarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors.


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
| `age_at_end` | `integer` |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |

## OffProtocolTherapyOrStudy

| Slot | Range | Description |
|---|---|---|
| `age_off` | `integer` |  |
| `off_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-offtypeenum')">OffTypeEnum</button> |  |
| `reason_off` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonoffenum')">ReasonOffEnum</button> |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `study_age_precision` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyageprecisionenum')">StudyAgePrecisionEnum</button> |  |
| `data_source` | `DataSourceEnum` |  |

## StudySubgroupAssignment

| Slot | Range | Description |
|---|---|---|
| `subgroup_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgrouptypeenum')">SubgroupTypeEnum</button> |  |
| `subgroup_name` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgroupnameenum')">SubgroupNameEnum</button> |  |
| `subgroup_assignment_order` | `integer` |  |
| `age_at_subgroup_assignment` | `integer` |  |
| `randomized` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-randomizedenum')">RandomizedEnum</button> |  |

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

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histology_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologygradeenum')">HistologyGradeEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `depth` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-depthenum')">DepthEnum</button> |  |
| `tumor_volume` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorvolumeenum')">TumorVolumeEnum</button> |  |
| `fracture` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `site_within_bone` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sitewithinboneenum')">SiteWithinBoneEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `disease_extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseaseextentenum')">DiseaseExtentEnum</button> |  |
| `skip_lesion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-skiplesionenum')">SkipLesionEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `medication_other` | `string` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure_performed` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-extentenum')">ExtentEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |
| `distance_from_margin` | `decimal` |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `ae_code` | `string` |  |
| `ae_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aecodesystemenum')">AeCodeSystemEnum</button> |  |
| `ae_system_version` | `string` |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `ae_attribution` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeattributionenum')">AeAttributionEnum</button> |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `necrosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-necrosisenum')">NecrosisEnum</button> |  |
| `necrosis_pct` | `decimal` |  |

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

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |

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

<div id="enum-modal-aeattributionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aeattributionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aeattributionenum')">×</button>
<h3><code>AeAttributionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Definite</code></td><td><code>ncit:C53260</code></td><td></td></tr>
<tr><td><code>Possible</code></td><td><code>ncit:C53258</code></td><td></td></tr>
<tr><td><code>Probable</code></td><td><code>ncit:C41357</code></td><td></td></tr>
<tr><td><code>Unlikely</code></td><td><code>ncit:C53257</code></td><td></td></tr>
<tr><td><code>Unrelated</code></td><td><code>ncit:C53256</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aecodesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aecodesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aecodesystemenum')">×</button>
<h3><code>AeCodeSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CTCAE</code></td><td><code>ncit:C49704</code></td><td></td></tr>
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
<tr><td><code>CTCAE &gt;&gt; Grade 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 5</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>m2</code></td><td><code>ncit:C42569</code></td><td></td></tr>
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
<tr><td><code>BMI</code></td><td><code>ncit:C138901</code></td><td></td></tr>
<tr><td><code>BSA</code></td><td><code>ncit:C25157</code></td><td></td></tr>
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
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
<tr><td><code>HIBiSCus</code></td><td><code>ncit:C192763</code></td><td></td></tr>
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
<tr><td><code>Consolidation</code></td><td><code>ncit:C15679</code></td><td></td></tr>
<tr><td><code>Induction</code></td><td><code>ncit:C158876</code></td><td></td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-depthenum" class="enum-modal" onclick="closeEnumModal('enum-modal-depthenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-depthenum')">×</button>
<h3><code>DepthEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cortical</code></td><td><code>ncit:C52714</code></td><td></td></tr>
<tr><td><code>Deep</code></td><td><code>ncit:C25240</code></td><td></td></tr>
<tr><td><code>Intra-Medullary</code></td><td><code>ncit:C96266</code></td><td></td></tr>
<tr><td><code>Superficial</code></td><td><code>ncit:C25239</code></td><td></td></tr>
<tr><td><code>Surface</code></td><td><code>ncit:C25245</code></td><td></td></tr>
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
<tr><td><code>Chondroblastic osteosarcoma</code></td><td><code>icdo:9181/3</code></td><td></td></tr>
<tr><td><code>Conventional Osteosarcoma</code></td><td><code>ncit:C35870</code></td><td></td></tr>
<tr><td><code>Fibroblastic Osteosarcoma</code></td><td><code>ncit:C4020</code></td><td></td></tr>
<tr><td><code>Giant Cell Rich Osteosarcoma</code></td><td><code>ncit:C179410</code></td><td></td></tr>
<tr><td><code>Osteoblastic Osteosarcoma</code></td><td><code>ncit:C53953</code></td><td></td></tr>
<tr><td><code>Osteosarcoma, NOS</code></td><td><code>icdo:9180/3</code></td><td></td></tr>
<tr><td><code>Parosteal Osteosarcoma</code></td><td><code>icdo:9192/3</code></td><td></td></tr>
<tr><td><code>Periosteal Osteosarcoma</code></td><td><code>icdo:9193/3</code></td><td></td></tr>
<tr><td><code>Surface Osteosarcoma</code></td><td><code>ncit:C7134</code></td><td></td></tr>
<tr><td><code>Telangiectatic Osteosarcoma</code></td><td><code>icdo:9183/3</code></td><td></td></tr>
<tr><td><code>Small Cell Osteosarcoma</code></td><td><code>icdo:9185/3</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diseaseextentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diseaseextentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diseaseextentenum')">×</button>
<h3><code>DiseaseExtentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Localized</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metastatic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Indeterminant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>OS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Relapse/Progression</code></td><td><code>ncit:C174991</code></td><td></td></tr>
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
<tr><td><code>Femur</code></td><td><code>ncit:C12717</code></td><td></td></tr>
<tr><td><code>Fibula</code></td><td><code>ncit:C12718</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hilum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Humerus</code></td><td><code>ncit:C12731</code></td><td></td></tr>
<tr><td><code>Jaw, NOS</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Lower Limb, NOS</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Maxilla</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C6634</code></td><td></td></tr>
<tr><td><code>Pelvis, Ilium</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Pelvis, Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Pelvis, Pubis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, Sacrum</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Radius</code></td><td><code>ncit:C12777</code></td><td></td></tr>
<tr><td><code>Rib</code></td><td><code>ncit:C12782</code></td><td></td></tr>
<tr><td><code>Skull, NOS</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Tibia</code></td><td><code>ncit:C12800</code></td><td></td></tr>
<tr><td><code>Ulna</code></td><td><code>ncit:C12809</code></td><td></td></tr>
<tr><td><code>Upper Limb, NOS</code></td><td><code>ncit:C12671</code></td><td></td></tr>
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
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fractiondoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">×</button>
<h3><code>FractionDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Gy</code></td><td><code>ncit:C18063</code></td><td></td></tr>
<tr><td><code>cGy</code></td><td><code>ncit:C64693</code></td><td></td></tr>
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
<tr><td><code>System NOS &gt;&gt; Grade 1</code></td><td><code>ncit:C41338</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 2</code></td><td><code>ncit:C41339</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 3</code></td><td><code>ncit:C41340</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(nbl) ConsortiumNote: Use for 'Cannot be determined'</td></tr>
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
<tr><td><code>ALP</code></td><td><code>ncit:C64432</code></td><td></td></tr>
<tr><td><code>CRP</code></td><td><code>ncit:C64548</code></td><td></td></tr>
<tr><td><code>ESR</code></td><td><code>ncit:C74611</code></td><td></td></tr>
<tr><td><code>LDH</code></td><td><code>ncit:C64855</code></td><td></td></tr>
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
<tr><td><code>Unilateral</code></td><td><code>ncit:C28012</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lesionmeasurementunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lesionmeasurementunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lesionmeasurementunitenum')">×</button>
<h3><code>LesionMeasurementUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cm</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>R0 - Complete Resection, Negative Margins</code></td><td><code>ncit:C139578</code></td><td>(lt) ConsortiumNote: sub-procedures have no margins, only the multi-focal procedures</td></tr>
<tr><td><code>R1 - Complete Resection, Positive Margins</code></td><td><code>ncit:C139579</code></td><td></td></tr>
<tr><td><code>R2 - Gross Residual Disease</code></td><td><code>ncit:C139580</code></td><td></td></tr>
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
<tr><td><code>Bloom Syndrome</code></td><td><code>ncit:C2903</code></td><td></td></tr>
<tr><td><code>Cherubism</code></td><td><code>ncit:C84630</code></td><td></td></tr>
<tr><td><code>Diamond-Blackfan Anemia</code></td><td><code>ncit:C61236</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia</code></td><td><code>ncit:C62505</code></td><td></td></tr>
<tr><td><code>Gardner Syndrome</code></td><td><code>ncit:C6728</code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Lynch Syndrome</code></td><td><code>ncit:C8494</code></td><td></td></tr>
<tr><td><code>Maffucci Syndrome</code></td><td><code>ncit:C3213</code></td><td></td></tr>
<tr><td><code>McCune-Albright Syndrome</code></td><td><code>ncit:C48627</code></td><td></td></tr>
<tr><td><code>Multiple Osteochondromas</code></td><td><code>ncit:C53457</code></td><td></td></tr>
<tr><td><code>NF1</code></td><td><code>ncit:C3273</code></td><td></td></tr>
<tr><td><code>NF2</code></td><td><code>ncit:C3274</code></td><td></td></tr>
<tr><td><code>Ollier Disease</code></td><td><code>ncit:C3008</code></td><td></td></tr>
<tr><td><code>Other Cancer</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paget Disease</code></td><td><code>ncit:C7073</code></td><td></td></tr>
<tr><td><code>Parathyroid Carcinoma / Adenoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retinoblastoma Syndrome</code></td><td><code>ncit:C7541</code></td><td></td></tr>
<tr><td><code>Rothmund-Thomson Syndrome</code></td><td><code>ncit:C3335</code></td><td></td></tr>
<tr><td><code>Werner Syndrome</code></td><td><code>ncit:C3447</code></td><td></td></tr>
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
<tr><td><code>mg</code></td><td><code>ncit:C28253</code></td><td></td></tr>
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
<tr><td><code>Cabozantinib</code></td><td><code>ncit:C52200</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Denosumab</code></td><td><code>ncit:C61313</code></td><td></td></tr>
<tr><td><code>Dinutuximab</code></td><td><code>rxcui:1606274</code></td><td></td></tr>
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Glembatumumab</code></td><td><code>ncit:C84520</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Interferon</code></td><td><code>ncit:C20493</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Mifamurtide</code></td><td><code>ncit:C1394</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Regorafenib</code></td><td><code>ncit:C78204</code></td><td></td></tr>
<tr><td><code>Zoledronic Acid</code></td><td><code>ncit:C1699</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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

<div id="enum-modal-necrosisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-necrosisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-necrosisenum')">×</button>
<h3><code>NecrosisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;= 90% Necrosis</code></td><td><code>ncit:C180353</code></td><td></td></tr>
<tr><td><code>&gt; 90% Necrosis</code></td><td><code>ncit:C180348</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-offtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-offtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-offtypeenum')">×</button>
<h3><code>OffTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Protocol Therapy</code></td><td><code>ncit:C173257</code></td><td>(ews) ConsortiumNote: In EE99, we only collected the reason for the end of study treatment (for randomized and non randomized patients).</td></tr>
<tr><td><code>Study</code></td><td><code>ncit:C29851</code></td><td></td></tr>
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
<tr><td><code>Allograft and Vascularized Autograft</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure</td></tr>
<tr><td><code>Allograft-Prosthetic</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure</td></tr>
<tr><td><code>Amputation, NOS</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.<br>(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction.</td></tr>
<tr><td><code>Amputation, proximal to involved bone</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.<br>(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction.</td></tr>
<tr><td><code>Amputation, through involved bone</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.<br>(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction.</td></tr>
<tr><td><code>Axial Skeleton Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Core Needle Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Craniofacial Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Disarticulation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endoprosthetic</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Excision</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Excisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>External Hemipelvectomy</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Extra-Articular Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Incisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intercalary Allograft</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Intercalary Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Internal Hemipelvectomy</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Intra-Articular Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Limb Salvage, NOS</code></td><td><code></code></td><td>(ews) ConsortiumNote: Both a resection and reconstruction procedure.<br>(os) ConsortiumNote: Both a resection and reconstruction procedure.</td></tr>
<tr><td><code>Lobectomy</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (for metastatic disease).<br>(os) ConsortiumNote: Resection procedure (for metastatic disease).</td></tr>
<tr><td><code>Non-Vascularized Autograft</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Osteoarticular Allograft</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Pneumonectomy</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (for metastatic disease).<br>(os) ConsortiumNote: Resection procedure (for metastatic disease).</td></tr>
<tr><td><code>Reconstruction, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Resection, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rotationplasty</code></td><td><code></code></td><td>(ews) ConsortiumNote: Both a resection and reconstruction procedure.<br>(os) ConsortiumNote: Both a resection and reconstruction procedure.</td></tr>
<tr><td><code>Vascularized Autograft</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Vascularized Autograft Endoprosthetic Composite</code></td><td><code></code></td><td>(ews) ConsortiumNote: Reconstruction procedure<br>(os) ConsortiumNote: Reconstruction procedure.</td></tr>
<tr><td><code>Wedge Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (for metastatic disease).<br>(os) ConsortiumNote: Resection procedure (for metastatic disease).</td></tr>
<tr><td><code>Wide Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (modifier).<br>(os) ConsortiumNote: Resection procedure (modifier).</td></tr>
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
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Femur</code></td><td><code>ncit:C12717</code></td><td></td></tr>
<tr><td><code>Fibula</code></td><td><code>ncit:C12718</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hilum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Humerus</code></td><td><code>ncit:C12731</code></td><td></td></tr>
<tr><td><code>Jaw, NOS</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Lower Limb, NOS</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lymph Node, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Maxilla</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Pelvis, Ilium</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Pelvis, Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Pelvis, Pubis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, Sacrum</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td></td></tr>
<tr><td><code>Radius</code></td><td><code>ncit:C12777</code></td><td></td></tr>
<tr><td><code>Rib</code></td><td><code>ncit:C12782</code></td><td></td></tr>
<tr><td><code>Skull, NOS</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Tibia</code></td><td><code>ncit:C12800</code></td><td></td></tr>
<tr><td><code>Ulna</code></td><td><code>ncit:C12809</code></td><td></td></tr>
<tr><td><code>Upper Limb, NOS</code></td><td><code>ncit:C12671</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-randomizedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-randomizedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-randomizedenum')">×</button>
<h3><code>RandomizedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Non-Randomized</code></td><td><code>ncit:C93043</code></td><td></td></tr>
<tr><td><code>Randomized</code></td><td><code>ncit:C25196</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-reasonoffenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasonoffenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasonoffenum')">×</button>
<h3><code>ReasonOffEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Adverse Event</code></td><td><code>ncit:C41331</code></td><td></td></tr>
<tr><td><code>Completion of Planned Therapy</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Death</code></td><td><code>ncit:C28554</code></td><td>(os) ConsortiumNote: If multiple reasons for off 'Protocol Therapy' or off 'Study', include one observation per reason.</td></tr>
<tr><td><code>Development of SMN</code></td><td><code>ncit:C4968</code></td><td></td></tr>
<tr><td><code>Disease Progression</code></td><td><code>ncit:C17747</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Subject Non-Compliance</code></td><td><code>ncit:C91752</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Not Evaluable</code></td><td><code>ncit:C62222</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Partial Response</code></td><td><code>ncit:C159547</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Progressive Disease</code></td><td><code>ncit:C159716</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Stable Disease</code></td><td><code>ncit:C159546</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Complete Surgical Remission</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bone, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Femur</code></td><td><code>ncit:C12717</code></td><td></td></tr>
<tr><td><code>Fibula</code></td><td><code>ncit:C12718</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hilum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Humerus</code></td><td><code>ncit:C12731</code></td><td></td></tr>
<tr><td><code>Jaw, NOS</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Lower Limb, NOS</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lymph Node, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Maxilla</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Pelvis, Ilium</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Pelvis, Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Pelvis, Pubis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, Sacrum</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radius</code></td><td><code>ncit:C12777</code></td><td></td></tr>
<tr><td><code>Rib</code></td><td><code>ncit:C12782</code></td><td></td></tr>
<tr><td><code>Skull, NOS</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Tibia</code></td><td><code>ncit:C12800</code></td><td></td></tr>
<tr><td><code>Ulna</code></td><td><code>ncit:C12809</code></td><td></td></tr>
<tr><td><code>Upper Limb, NOS</code></td><td><code>ncit:C12671</code></td><td></td></tr>
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
<tr><td><code>Regional</code></td><td><code></code></td><td>(os) ConsortiumNote: Regional to the local site.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-sitewithinboneenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sitewithinboneenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sitewithinboneenum')">×</button>
<h3><code>SiteWithinBoneEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diaphysis</code></td><td><code>ncit:C32529</code></td><td></td></tr>
<tr><td><code>Distal</code></td><td><code>ncit:C25237</code></td><td></td></tr>
<tr><td><code>Epiphysis</code></td><td><code>ncit:C32460</code></td><td></td></tr>
<tr><td><code>Metaphysis</code></td><td><code>ncit:C52723</code></td><td></td></tr>
<tr><td><code>Proximal</code></td><td><code>ncit:C25236</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-skiplesionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-skiplesionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-skiplesionenum')">×</button>
<h3><code>SkipLesionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>No</code></td><td><code>ncit:C49487</code></td><td></td></tr>
<tr><td><code>Yes, Same Bone</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, Different Bone</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-studyageprecisionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-studyageprecisionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-studyageprecisionenum')">×</button>
<h3><code>StudyAgePrecisionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Approximated from birth year</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>AOST0331/EURAMOS1</code></td><td><code>ncit:C180361</code></td><td>(os) ConsortiumNote: also known by COG study id AOST0331</td></tr>
<tr><td><code>AOST0221</code></td><td><code>ncit:C180360</code></td><td></td></tr>
<tr><td><code>AOST0121</code></td><td><code>ncit:C180358</code></td><td></td></tr>
<tr><td><code>AOST01P1</code></td><td><code>ncit:C180359</code></td><td></td></tr>
<tr><td><code>AOST1321</code></td><td><code>ncit:C180362</code></td><td></td></tr>
<tr><td><code>AOST1421</code></td><td><code>ncit:C180363</code></td><td></td></tr>
<tr><td><code>CCG-782</code></td><td><code>C180364</code></td><td></td></tr>
<tr><td><code>CCG-7942</code></td><td><code>C180365</code></td><td></td></tr>
<tr><td><code>INT133</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OS2 Trial (2011-2018)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REGOBONE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC038</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sarcome-09/OS2006</code></td><td><code>ncit:C180367</code></td><td></td></tr>
<tr><td><code>Sarcome-13/OS2016</code></td><td><code>ncit:C180370</code></td><td></td></tr>
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
<tr><td><code>CHEMO</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHEMO-ZOL</code></td><td><code>ncit:C186777</code></td><td></td></tr>
<tr><td><code>DOX</code></td><td><code>C1326</code></td><td></td></tr>
<tr><td><code>DOX-IFOS</code></td><td><code>C63686</code></td><td></td></tr>
<tr><td><code>MAP</code></td><td><code>ncit:C67339</code></td><td></td></tr>
<tr><td><code>MAP-GR</code></td><td><code>ncit:C186769</code></td><td></td></tr>
<tr><td><code>MAP-IE-PR</code></td><td><code>ncit:C186772</code></td><td></td></tr>
<tr><td><code>MAP-IFN-GR</code></td><td><code>ncit:C186770</code></td><td></td></tr>
<tr><td><code>MAP-NR</code></td><td><code>ncit:C186773</code></td><td></td></tr>
<tr><td><code>MAP-PR</code></td><td><code>ncit:C186771</code></td><td></td></tr>
<tr><td><code>POSTOP-CHEMO</code></td><td><code>ncit:C186775</code></td><td></td></tr>
<tr><td><code>POSTOP-CHEMO-MIF</code></td><td><code>ncit:C1867763</code></td><td></td></tr>
<tr><td><code>REG-ACTIVE</code></td><td><code>C186778</code></td><td></td></tr>
<tr><td><code>REG-PLACEBO</code></td><td><code>C186779</code></td><td></td></tr>
<tr><td><code>SARC038: Experimental: Regorafenib and Nivolumab</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-techniqueenum" class="enum-modal" onclick="closeEnumModal('enum-modal-techniqueenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-techniqueenum')">×</button>
<h3><code>TechniqueEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>EBRT, 3D Conformal</code></td><td><code>ncit:C16035</code></td><td></td></tr>
<tr><td><code>EBRT, Intensity-Modulated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Stereotactic Body</code></td><td><code>ncit:C118286</code></td><td>(npc) ConsortiumNote: Stereotactic ablative body radiotherapy</td></tr>
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

<div id="enum-modal-tumorvolumeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorvolumeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorvolumeenum')">×</button>
<h3><code>TumorVolumeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;200 mL</code></td><td><code>ncit:C175000</code></td><td></td></tr>
<tr><td><code>&gt;=200 mL</code></td><td><code>ncit:C175001</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
    "os": {
      "name": "os",
      "title": "Osteosarcoma",
      "description": "The OS view of the PCDC data model represents consensus data modeling by an international group of pediatric osteosarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors."
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
        "study_age_precision",
        "data_source"
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
        "subgroup_assignment_order",
        "age_at_subgroup_assignment",
        "randomized"
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
        "course",
        "age_at_start",
        "year_at_start",
        "age_at_end"
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
    "OffProtocolTherapyOrStudy": {
      "slots": [
        "age_off",
        "off_type",
        "reason_off"
      ],
      "comments": [
        "D4CGNote: If patient went off protocol therapy or study then include an observation.",
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "SurvivalCharacteristics": {
      "slots": [
        "age_at_lkss",
        "lkss"
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
        "diagnosis_basis",
        "diagnosis",
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
        "disease_extent",
        "skip_lesion"
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
        "laterality",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "depth",
        "tumor_volume",
        "fracture",
        "site_within_bone"
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
        "procedure_performed",
        "site_classification",
        "procedure",
        "procedure_site",
        "laterality",
        "extent",
        "margins",
        "distance_from_margin"
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
        "medication",
        "medication_other",
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
        "site_classification",
        "rt_site",
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
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response",
        "necrosis",
        "necrosis_pct"
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
        "ae_code",
        "ae_code_system",
        "ae_system_version",
        "ae_grade",
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
    "age_off": {
      "slot_uri": "ncit:C168844",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "age_at_end": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "ae_system_version": {
      "slot_uri": "ncit:C173314",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "diagnosis_basis": {
      "slot_uri": "",
      "range": "DiagnosisBasisEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "npc"
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
    "extent": {
      "slot_uri": "ncit:C157443",
      "range": "ExtentEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "site_within_bone": {
      "slot_uri": "ncit:C174998",
      "range": "SiteWithinBoneEnum",
      "comments": [],
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
    "necrosis": {
      "slot_uri": "ncit:C159481",
      "range": "NecrosisEnum",
      "comments": [],
      "annotations": {}
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
    "distance_from_margin": {
      "slot_uri": "ncit:C137815",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "ae_code": {
      "slot_uri": "ncit:C173313",
      "range": "string",
      "comments": [
        "(aml) ConsortiumNote: For AML, include when available if a 1:1 mapping to the ADVERSE_EVENT bucket"
      ],
      "annotations": {
        "tier_mandatory": "hl"
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
    "measurement1": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb",
        "tier_optional": "npc,ls"
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
    "depth": {
      "slot_uri": "ncit:C25333",
      "range": "DepthEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_ae": {
      "slot_uri": "ncit:C172677",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "study_age_precision": {
      "slot_uri": "",
      "range": "StudyAgePrecisionEnum",
      "comments": [
        "(os) ConsortiumNote: this variable should only be used for ISG, to indicate that the AGE_AT variables througout are approximate. This is due to only having the birth year."
      ],
      "annotations": {
        "tier_optional": "os"
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
    "necrosis_pct": {
      "slot_uri": "ncit:C159481",
      "range": "decimal",
      "comments": [
        "(os) ConsortiumNote: This should be the mean, not the min or max.",
        "(ews) ConsortiumNote: Include one decimal place."
      ],
      "annotations": {}
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
    "ae_code_system": {
      "slot_uri": "ncit:C168872",
      "range": "AeCodeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "measurement_unit": {
      "slot_uri": "",
      "range": "LesionMeasurementUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "age_at_smn": {
      "slot_uri": "ncit:C168860",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "consortium": {
      "slot_uri": "ncit:C61538",
      "range": "ConsortiumEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "all_groups,ls"
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
    "procedure_performed": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "off_type": {
      "slot_uri": "ncit:C173256",
      "range": "OffTypeEnum",
      "comments": [
        "(aml) ConsortiumNote: Off protocol therapy means they have stopped protocol treatment, but are still being followed in the study"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "npc,rb",
        "tier_optional": "ls"
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
    "tumor_volume": {
      "slot_uri": "ncit:C94515",
      "range": "TumorVolumeEnum",
      "comments": [
        "(ews) ConsortiumNote: In EICESS 92, the cutoff was 100 ml. Conversion to the 200 cutoff is only possible for patients with a volume <100. For patients with a volume >100, we can only calculate this for those with accurate volume. Assuming some missings"
      ],
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
    "fracture": {
      "slot_uri": "ncit:C3046",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_subgroup_assignment": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "(ews) ConsortiumNote: Date of assignment, regardless of if the treatment was received",
        "(os) ConsortiumNote: use date of randomization, for non-randomized patients use enrollment date."
      ],
      "annotations": {
        "tier_priority": "all_groups"
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
    "randomized": {
      "slot_uri": "ncit:C25196",
      "range": "RandomizedEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "os"
      }
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
    "medication_other": {
      "slot_uri": "",
      "range": "string",
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
    "morph_code_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "measurement3": {
      "slot_uri": "ncit:C16809",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "skip_lesion": {
      "slot_uri": "ncit:C174454",
      "range": "SkipLesionEnum",
      "comments": [],
      "annotations": {}
    },
    "measurement2": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "reason_off": {
      "slot_uri": "ncit:C173519",
      "range": "ReasonOffEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple reasons 'off protocol therapy' or 'off study', include one observation per reason.",
        "(cns) ConsortiumNote: If multiple reasons off 'protocol therapy' or 'study', include one observation per reason.",
        "(ews) ConsortiumNote: If multiple reasons off 'protocol therapy' or 'study', include one observation per reason.",
        "(npc) ConsortiumNote: If multiple reasons off 'protocol therapy' or 'study', include one observation per reason."
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "npc,rb",
        "tier_optional": "ls"
      }
    },
    "disease_extent": {
      "slot_uri": "",
      "range": "DiseaseExtentEnum",
      "comments": [],
      "annotations": {}
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
        }
      }
    },
    "SiteWithinBoneEnum": {
      "permissible_values": {
        "Diaphysis": {
          "meaning": "ncit:C32529",
          "comments": []
        },
        "Distal": {
          "meaning": "ncit:C25237",
          "comments": []
        },
        "Epiphysis": {
          "meaning": "ncit:C32460",
          "comments": []
        },
        "Metaphysis": {
          "meaning": "ncit:C52723",
          "comments": []
        },
        "Proximal": {
          "meaning": "ncit:C25236",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "AnthropometricMeasurementTypeEnum": {
      "permissible_values": {
        "BMI": {
          "meaning": "ncit:C138901",
          "comments": []
        },
        "BSA": {
          "meaning": "ncit:C25157",
          "comments": []
        },
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
    "StudyAgePrecisionEnum": {
      "permissible_values": {
        "Approximated from birth year": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "HistologyGradeEnum": {
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
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": [
            "(nbl) ConsortiumNote: Use for 'Cannot be determined'"
          ]
        }
      }
    },
    "ResponseEnum": {
      "permissible_values": {
        "Not Evaluable": {
          "meaning": "ncit:C62222",
          "comments": []
        },
        "RECIST >> Complete Response": {
          "meaning": "ncit:C4870",
          "comments": []
        },
        "RECIST >> Partial Response": {
          "meaning": "ncit:C159547",
          "comments": []
        },
        "RECIST >> Progressive Disease": {
          "meaning": "ncit:C159716",
          "comments": []
        },
        "RECIST >> Stable Disease": {
          "meaning": "ncit:C159546",
          "comments": []
        },
        "System NOS >> Complete Surgical Remission": {
          "meaning": "",
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
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "CourseEnum": {
      "permissible_values": {
        "Consolidation": {
          "meaning": "ncit:C15679",
          "comments": []
        },
        "Induction": {
          "meaning": "ncit:C158876",
          "comments": []
        },
        "Maintenance": {
          "meaning": "ncit:C15688",
          "comments": [
            "(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses."
          ]
        }
      }
    },
    "NecrosisEnum": {
      "permissible_values": {
        "<= 90% Necrosis": {
          "meaning": "ncit:C180353",
          "comments": []
        },
        "> 90% Necrosis": {
          "meaning": "ncit:C180348",
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
        "Femur": {
          "meaning": "ncit:C12717",
          "comments": []
        },
        "Fibula": {
          "meaning": "ncit:C12718",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hilum": {
          "meaning": "",
          "comments": []
        },
        "Humerus": {
          "meaning": "ncit:C12731",
          "comments": []
        },
        "Jaw, NOS": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Lower Limb, NOS": {
          "meaning": "ncit:C12742",
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
        "Mandible": {
          "meaning": "ncit:C12290",
          "comments": []
        },
        "Maxilla": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C6634",
          "comments": []
        },
        "Pelvis, Ilium": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Pelvis, Ischium": {
          "meaning": "ncit:C32884",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Pelvis, Pubis": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, Sacrum": {
          "meaning": "ncit:C33508",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": [
            "(ews) ConsortiumNote: Included so that pleural effusions can be reported.",
            "(os) ConsortiumNote: Included so that pleural effusions can be reported."
          ]
        },
        "Radius": {
          "meaning": "ncit:C12777",
          "comments": []
        },
        "Rib": {
          "meaning": "ncit:C12782",
          "comments": []
        },
        "Skull, NOS": {
          "meaning": "ncit:C12789",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
          "comments": []
        },
        "Tibia": {
          "meaning": "ncit:C12800",
          "comments": []
        },
        "Ulna": {
          "meaning": "ncit:C12809",
          "comments": []
        },
        "Upper Limb, NOS": {
          "meaning": "ncit:C12671",
          "comments": []
        }
      }
    },
    "OffTypeEnum": {
      "permissible_values": {
        "Protocol Therapy": {
          "meaning": "ncit:C173257",
          "comments": [
            "(ews) ConsortiumNote: In EE99, we only collected the reason for the end of study treatment (for randomized and non randomized patients)."
          ]
        },
        "Study": {
          "meaning": "ncit:C29851",
          "comments": []
        }
      }
    },
    "ReasonOffEnum": {
      "permissible_values": {
        "Adverse Event": {
          "meaning": "ncit:C41331",
          "comments": []
        },
        "Completion of Planned Therapy": {
          "meaning": "ncit:C168935",
          "comments": []
        },
        "Death": {
          "meaning": "ncit:C28554",
          "comments": [
            "(os) ConsortiumNote: If multiple reasons for off 'Protocol Therapy' or off 'Study', include one observation per reason."
          ]
        },
        "Development of SMN": {
          "meaning": "ncit:C4968",
          "comments": []
        },
        "Disease Progression": {
          "meaning": "ncit:C17747",
          "comments": []
        },
        "Physician Decision": {
          "meaning": "ncit:C48250",
          "comments": []
        },
        "Subject Non-Compliance": {
          "meaning": "ncit:C91752",
          "comments": []
        },
        "Subject/Guardian Refused Further Treatment": {
          "meaning": "ncit:C168934",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "DiseaseExtentEnum": {
      "permissible_values": {
        "Localized": {
          "meaning": "",
          "comments": []
        },
        "Metastatic": {
          "meaning": "",
          "comments": []
        },
        "Indeterminant": {
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
    "RtSiteEnum": {
      "permissible_values": {
        "Bone, NOS": {
          "meaning": "",
          "comments": []
        },
        "Femur": {
          "meaning": "ncit:C12717",
          "comments": []
        },
        "Fibula": {
          "meaning": "ncit:C12718",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hilum": {
          "meaning": "",
          "comments": []
        },
        "Humerus": {
          "meaning": "ncit:C12731",
          "comments": []
        },
        "Jaw, NOS": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Lower Limb, NOS": {
          "meaning": "ncit:C12742",
          "comments": []
        },
        "Lymph Node, NOS": {
          "meaning": "",
          "comments": []
        },
        "Mandible": {
          "meaning": "ncit:C12290",
          "comments": []
        },
        "Maxilla": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Pelvis, Ilium": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Pelvis, Ischium": {
          "meaning": "ncit:C32884",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Pelvis, Pubis": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, Sacrum": {
          "meaning": "ncit:C33508",
          "comments": []
        },
        "Pleura": {
          "meaning": "",
          "comments": []
        },
        "Radius": {
          "meaning": "ncit:C12777",
          "comments": []
        },
        "Rib": {
          "meaning": "ncit:C12782",
          "comments": []
        },
        "Skull, NOS": {
          "meaning": "ncit:C12789",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
          "comments": []
        },
        "Tibia": {
          "meaning": "ncit:C12800",
          "comments": []
        },
        "Ulna": {
          "meaning": "ncit:C12809",
          "comments": []
        },
        "Upper Limb, NOS": {
          "meaning": "ncit:C12671",
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
        },
        "m2": {
          "meaning": "ncit:C42569",
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
        "Unilateral": {
          "meaning": "ncit:C28012",
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
        "mg": {
          "meaning": "ncit:C28253",
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
    "DepthEnum": {
      "permissible_values": {
        "Cortical": {
          "meaning": "ncit:C52714",
          "comments": []
        },
        "Deep": {
          "meaning": "ncit:C25240",
          "comments": []
        },
        "Intra-Medullary": {
          "meaning": "ncit:C96266",
          "comments": []
        },
        "Superficial": {
          "meaning": "ncit:C25239",
          "comments": []
        },
        "Surface": {
          "meaning": "ncit:C25245",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "SkipLesionEnum": {
      "permissible_values": {
        "No": {
          "meaning": "ncit:C49487",
          "comments": []
        },
        "Yes, Same Bone": {
          "meaning": "",
          "comments": []
        },
        "Yes, Different Bone": {
          "meaning": "",
          "comments": []
        },
        "Yes, NOS": {
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
    "StudyIdEnum": {
      "permissible_values": {
        "AOST0331/EURAMOS1": {
          "meaning": "ncit:C180361",
          "comments": [
            "(os) ConsortiumNote: also known by COG study id AOST0331"
          ]
        },
        "AOST0221": {
          "meaning": "ncit:C180360",
          "comments": []
        },
        "AOST0121": {
          "meaning": "ncit:C180358",
          "comments": []
        },
        "AOST01P1": {
          "meaning": "ncit:C180359",
          "comments": []
        },
        "AOST1321": {
          "meaning": "ncit:C180362",
          "comments": []
        },
        "AOST1421": {
          "meaning": "ncit:C180363",
          "comments": []
        },
        "CCG-782": {
          "meaning": "C180364",
          "comments": []
        },
        "CCG-7942": {
          "meaning": "C180365",
          "comments": []
        },
        "INT133": {
          "meaning": "",
          "comments": []
        },
        "OS2 Trial (2011-2018)": {
          "meaning": "",
          "comments": []
        },
        "REGOBONE": {
          "meaning": "",
          "comments": []
        },
        "SARC038": {
          "meaning": "",
          "comments": []
        },
        "Sarcome-09/OS2006": {
          "meaning": "ncit:C180367",
          "comments": []
        },
        "Sarcome-13/OS2016": {
          "meaning": "ncit:C180370",
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
        "Chondroblastic osteosarcoma": {
          "meaning": "icdo:9181/3",
          "comments": []
        },
        "Conventional Osteosarcoma": {
          "meaning": "ncit:C35870",
          "comments": []
        },
        "Fibroblastic Osteosarcoma": {
          "meaning": "ncit:C4020",
          "comments": []
        },
        "Giant Cell Rich Osteosarcoma": {
          "meaning": "ncit:C179410",
          "comments": []
        },
        "Osteoblastic Osteosarcoma": {
          "meaning": "ncit:C53953",
          "comments": []
        },
        "Osteosarcoma, NOS": {
          "meaning": "icdo:9180/3",
          "comments": []
        },
        "Parosteal Osteosarcoma": {
          "meaning": "icdo:9192/3",
          "comments": []
        },
        "Periosteal Osteosarcoma": {
          "meaning": "icdo:9193/3",
          "comments": []
        },
        "Surface Osteosarcoma": {
          "meaning": "ncit:C7134",
          "comments": []
        },
        "Telangiectatic Osteosarcoma": {
          "meaning": "icdo:9183/3",
          "comments": []
        },
        "Small Cell Osteosarcoma": {
          "meaning": "icdo:9185/3",
          "comments": []
        }
      }
    },
    "AeAttributionEnum": {
      "permissible_values": {
        "Definite": {
          "meaning": "ncit:C53260",
          "comments": []
        },
        "Possible": {
          "meaning": "ncit:C53258",
          "comments": []
        },
        "Probable": {
          "meaning": "ncit:C41357",
          "comments": []
        },
        "Unlikely": {
          "meaning": "ncit:C53257",
          "comments": []
        },
        "Unrelated": {
          "meaning": "ncit:C53256",
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
    "AeCodeSystemEnum": {
      "permissible_values": {
        "CTCAE": {
          "meaning": "ncit:C49704",
          "comments": []
        }
      }
    },
    "FractionDoseUnitEnum": {
      "permissible_values": {
        "Gy": {
          "meaning": "ncit:C18063",
          "comments": []
        },
        "cGy": {
          "meaning": "ncit:C64693",
          "comments": []
        }
      }
    },
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Bone, NOS": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Femur": {
          "meaning": "ncit:C12717",
          "comments": []
        },
        "Fibula": {
          "meaning": "ncit:C12718",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hilum": {
          "meaning": "",
          "comments": []
        },
        "Humerus": {
          "meaning": "ncit:C12731",
          "comments": []
        },
        "Jaw, NOS": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Ischium": {
          "meaning": "ncit:C32884",
          "comments": []
        },
        "Lower Limb, NOS": {
          "meaning": "ncit:C12742",
          "comments": []
        },
        "Lymph Node, NOS": {
          "meaning": "",
          "comments": []
        },
        "Mandible": {
          "meaning": "ncit:C12290",
          "comments": []
        },
        "Maxilla": {
          "meaning": "ncit:C26470",
          "comments": []
        },
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Pelvis, Ilium": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Pelvis, Ischium": {
          "meaning": "ncit:C32884",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Pelvis, Pubis": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, Sacrum": {
          "meaning": "ncit:C33508",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": []
        },
        "Radius": {
          "meaning": "ncit:C12777",
          "comments": []
        },
        "Rib": {
          "meaning": "ncit:C12782",
          "comments": []
        },
        "Skull, NOS": {
          "meaning": "ncit:C12789",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
          "comments": []
        },
        "Tibia": {
          "meaning": "ncit:C12800",
          "comments": []
        },
        "Ulna": {
          "meaning": "ncit:C12809",
          "comments": []
        },
        "Upper Limb, NOS": {
          "meaning": "ncit:C12671",
          "comments": []
        }
      }
    },
    "RandomizedEnum": {
      "permissible_values": {
        "Non-Randomized": {
          "meaning": "ncit:C93043",
          "comments": []
        },
        "Randomized": {
          "meaning": "ncit:C25196",
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
        "OS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Cabozantinib": {
          "meaning": "ncit:C52200",
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
        "Denosumab": {
          "meaning": "ncit:C61313",
          "comments": []
        },
        "Dinutuximab": {
          "meaning": "rxcui:1606274",
          "comments": []
        },
        "Docetaxel": {
          "meaning": "rxcui:72962",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Glembatumumab": {
          "meaning": "ncit:C84520",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "rxcui:5657",
          "comments": []
        },
        "Interferon": {
          "meaning": "ncit:C20493",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Mifamurtide": {
          "meaning": "ncit:C1394",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Regorafenib": {
          "meaning": "ncit:C78204",
          "comments": []
        },
        "Zoledronic Acid": {
          "meaning": "ncit:C1699",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "TumorVolumeEnum": {
      "permissible_values": {
        "<200 mL": {
          "meaning": "ncit:C175000",
          "comments": []
        },
        ">=200 mL": {
          "meaning": "ncit:C175001",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
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
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "AeGradeEnum": {
      "permissible_values": {
        "CTCAE >> Grade 1": {
          "meaning": "",
          "comments": []
        },
        "CTCAE >> Grade 2": {
          "meaning": "",
          "comments": []
        },
        "CTCAE >> Grade 3": {
          "meaning": "",
          "comments": []
        },
        "CTCAE >> Grade 4": {
          "meaning": "",
          "comments": []
        },
        "CTCAE >> Grade 5": {
          "meaning": "",
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
        "Relapse/Progression": {
          "meaning": "ncit:C174991",
          "comments": []
        }
      }
    },
    "SubgroupNameEnum": {
      "permissible_values": {
        "CHEMO": {
          "meaning": "",
          "comments": []
        },
        "CHEMO-ZOL": {
          "meaning": "ncit:C186777",
          "comments": []
        },
        "DOX": {
          "meaning": "C1326",
          "comments": []
        },
        "DOX-IFOS": {
          "meaning": "C63686",
          "comments": []
        },
        "MAP": {
          "meaning": "ncit:C67339",
          "comments": []
        },
        "MAP-GR": {
          "meaning": "ncit:C186769",
          "comments": []
        },
        "MAP-IE-PR": {
          "meaning": "ncit:C186772",
          "comments": []
        },
        "MAP-IFN-GR": {
          "meaning": "ncit:C186770",
          "comments": []
        },
        "MAP-NR": {
          "meaning": "ncit:C186773",
          "comments": []
        },
        "MAP-PR": {
          "meaning": "ncit:C186771",
          "comments": []
        },
        "POSTOP-CHEMO": {
          "meaning": "ncit:C186775",
          "comments": []
        },
        "POSTOP-CHEMO-MIF": {
          "meaning": "ncit:C1867763",
          "comments": []
        },
        "REG-ACTIVE": {
          "meaning": "C186778",
          "comments": []
        },
        "REG-PLACEBO": {
          "meaning": "C186779",
          "comments": []
        },
        "SARC038: Experimental: Regorafenib and Nivolumab": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Bloom Syndrome": {
          "meaning": "ncit:C2903",
          "comments": []
        },
        "Cherubism": {
          "meaning": "ncit:C84630",
          "comments": []
        },
        "Diamond-Blackfan Anemia": {
          "meaning": "ncit:C61236",
          "comments": []
        },
        "Fanconi Anemia": {
          "meaning": "ncit:C62505",
          "comments": []
        },
        "Gardner Syndrome": {
          "meaning": "ncit:C6728",
          "comments": []
        },
        "Li-Fraumeni Syndrome": {
          "meaning": "ncit:C3476",
          "comments": []
        },
        "Lynch Syndrome": {
          "meaning": "ncit:C8494",
          "comments": []
        },
        "Maffucci Syndrome": {
          "meaning": "ncit:C3213",
          "comments": []
        },
        "McCune-Albright Syndrome": {
          "meaning": "ncit:C48627",
          "comments": []
        },
        "Multiple Osteochondromas": {
          "meaning": "ncit:C53457",
          "comments": []
        },
        "NF1": {
          "meaning": "ncit:C3273",
          "comments": []
        },
        "NF2": {
          "meaning": "ncit:C3274",
          "comments": []
        },
        "Ollier Disease": {
          "meaning": "ncit:C3008",
          "comments": []
        },
        "Other Cancer": {
          "meaning": "",
          "comments": []
        },
        "Paget Disease": {
          "meaning": "ncit:C7073",
          "comments": []
        },
        "Parathyroid Carcinoma / Adenoma": {
          "meaning": "",
          "comments": []
        },
        "Retinoblastoma Syndrome": {
          "meaning": "ncit:C7541",
          "comments": []
        },
        "Rothmund-Thomson Syndrome": {
          "meaning": "ncit:C3335",
          "comments": []
        },
        "Werner Syndrome": {
          "meaning": "ncit:C3447",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "HIBiSCus": {
          "meaning": "ncit:C192763",
          "comments": []
        }
      }
    },
    "TechniqueEnum": {
      "permissible_values": {
        "EBRT, 3D Conformal": {
          "meaning": "ncit:C16035",
          "comments": []
        },
        "EBRT, Intensity-Modulated": {
          "meaning": "",
          "comments": []
        },
        "EBRT, Stereotactic Body": {
          "meaning": "ncit:C118286",
          "comments": [
            "(npc) ConsortiumNote: Stereotactic ablative body radiotherapy"
          ]
        }
      }
    },
    "LesionMeasurementUnitEnum": {
      "permissible_values": {
        "cm": {
          "meaning": "",
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
        "Regional": {
          "meaning": "",
          "comments": [
            "(os) ConsortiumNote: Regional to the local site."
          ]
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "ALP": {
          "meaning": "ncit:C64432",
          "comments": []
        },
        "CRP": {
          "meaning": "ncit:C64548",
          "comments": []
        },
        "ESR": {
          "meaning": "ncit:C74611",
          "comments": []
        },
        "LDH": {
          "meaning": "ncit:C64855",
          "comments": []
        }
      }
    },
    "ProcedureEnum": {
      "permissible_values": {
        "Allograft and Vascularized Autograft": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure"
          ]
        },
        "Allograft-Prosthetic": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure"
          ]
        },
        "Amputation, NOS": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.",
            "(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction."
          ]
        },
        "Amputation, proximal to involved bone": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.",
            "(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction."
          ]
        },
        "Amputation, through involved bone": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (always wide) with no reconstruction.",
            "(os) ConsortiumNote: Resection procedure (always wide) with no reconstruction."
          ]
        },
        "Axial Skeleton Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Core Needle Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Craniofacial Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Disarticulation": {
          "meaning": "",
          "comments": []
        },
        "Endoprosthetic": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Excision": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Excisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "External Hemipelvectomy": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Extra-Articular Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Incisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Intercalary Allograft": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Intercalary Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Internal Hemipelvectomy": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Intra-Articular Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure.",
            "(os) ConsortiumNote: Resection procedure."
          ]
        },
        "Limb Salvage, NOS": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Both a resection and reconstruction procedure.",
            "(os) ConsortiumNote: Both a resection and reconstruction procedure."
          ]
        },
        "Lobectomy": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (for metastatic disease).",
            "(os) ConsortiumNote: Resection procedure (for metastatic disease)."
          ]
        },
        "Non-Vascularized Autograft": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Osteoarticular Allograft": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Pneumonectomy": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (for metastatic disease).",
            "(os) ConsortiumNote: Resection procedure (for metastatic disease)."
          ]
        },
        "Reconstruction, NOS": {
          "meaning": "",
          "comments": []
        },
        "Resection, NOS": {
          "meaning": "",
          "comments": []
        },
        "Rotationplasty": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Both a resection and reconstruction procedure.",
            "(os) ConsortiumNote: Both a resection and reconstruction procedure."
          ]
        },
        "Vascularized Autograft": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Vascularized Autograft Endoprosthetic Composite": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Reconstruction procedure",
            "(os) ConsortiumNote: Reconstruction procedure."
          ]
        },
        "Wedge Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (for metastatic disease).",
            "(os) ConsortiumNote: Resection procedure (for metastatic disease)."
          ]
        },
        "Wide Resection": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (modifier).",
            "(os) ConsortiumNote: Resection procedure (modifier)."
          ]
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