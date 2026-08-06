---
layout: default
title: Nasopharyngeal Carcinoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*NPC View*

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
- **Nasopharyngeal Carcinoma**
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The NPC view of the PCDC data model represents consensus data modeling by an international group of pediatric nasopharyngeal carcinoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Nasopharyngeal Carcinoma Global Partnership (NOBLE). It is based on the collective requirements of its contributors.


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

## OffProtocolTherapyOrStudy

| Slot | Range | Description |
|---|---|---|
| `age_off` | `integer` |  |
| `off_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-offtypeenum')">OffTypeEnum</button> |  |
| `reason_off` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonoffenum')">ReasonOffEnum</button> |  |
| `reason_off_other` | `string` |  |
| `another_study` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `enrolled_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |
| `data_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-datasourceenum')">DataSourceEnum</button> |  |
| `urls` | `string` |  |

## StudySubgroupAssignment

| Slot | Range | Description |
|---|---|---|
| `subgroup_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgrouptypeenum')">SubgroupTypeEnum</button> |  |
| `subgroup_name` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subgroupnameenum')">SubgroupNameEnum</button> |  |
| `subgroup_assignment_order` | `integer` |  |
| `age_at_subgroup_assignment` | `integer` |  |

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
| `lkss_with_disease` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |
| `trm_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-trmtypeenum')">TrmTypeEnum</button> |  |
| `cause_of_death_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathdetailenum')">CauseOfDeathDetailEnum</button> |  |
| `cause_of_death_ranking` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathrankingenum')">CauseOfDeathRankingEnum</button> |  |

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histologic_features` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologicfeaturesenum')">HistologicFeaturesEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `multiplicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-multiplicityenum')">MultiplicityEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `tnm_tumor_t` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmtumortenum')">TnmTumorTEnum</button> |  |
| `tnm_node_n` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmnodenenum')">TnmNodeNEnum</button> |  |
| `tnm_metastasis_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmmetastasismenum')">TnmMetastasisMEnum</button> |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage_system_version` | `string` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `administration_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-administrationstatusenum')">AdministrationStatusEnum</button> |  |
| `cycles_planned` | `decimal` |  |
| `cycle_number` | `decimal` |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `number_doses` | `decimal` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_intended` | `decimal` |  |
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
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-boosttypeenum')">BoostTypeEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |
| `treatment_volume` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-treatmentvolumeenum')">TreatmentVolumeEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_other` | `string` |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `procedure_extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureextentenum')">ProcedureExtentEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_code` | `string` |  |
| `ae_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aecodesystemenum')">AeCodeSystemEnum</button> |  |
| `ae_system_version` | `string` |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `ae_attribution` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeattributionenum')">AeAttributionEnum</button> |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsesystemenum')">ResponseSystemEnum</button> |  |
| `response_system_version` | `string` |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `smn_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smnsiteenum')">SmnSiteEnum</button> |  |
| `smn_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smntypeenum')">SmnTypeEnum</button> |  |
| `morph_code` | `string` |  |
| `morph_code_text` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `morph_code_system_version` | `string` |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |
| `smn_field` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smnfieldenum')">SmnFieldEnum</button> |  |

<div class="domain-heading">Testing</div>

## FunctionTest

| Slot | Range | Description |
|---|---|---|
| `age_at_function_test` | `integer` |  |
| `function_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functiontestenum')">FunctionTestEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `functional_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functionalmeasurementresultunitenum')">FunctionalMeasurementResultUnitEnum</button> |  |
| `function_test_laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functiontestlateralityenum')">FunctionTestLateralityEnum</button> |  |
| `hz_frequency` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hzfrequencyenum')">HzFrequencyEnum</button> |  |
| `average_loss_low` | `decimal` |  |
| `average_loss_high` | `decimal` |  |
| `function_test_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functiontestgradeenum')">FunctionTestGradeEnum</button> |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |

<div id="enum-modal-administrationstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-administrationstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-administrationstatusenum')">×</button>
<h3><code>AdministrationStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Medication Administered</code></td><td><code>ncit:C173298</code></td><td></td></tr>
<tr><td><code>Medication Not Administered</code></td><td><code>ncit:C173299</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Anemia</code></td><td><code>ncit:C2869</code></td><td></td></tr>
<tr><td><code>CNS Necrosis</code></td><td><code>ncit:C55367</code></td><td></td></tr>
<tr><td><code>Cataract</code></td><td><code>ncit:C26713</code></td><td></td></tr>
<tr><td><code>Cranial Nerve Palsy</code></td><td><code>ncit:C26941</code></td><td></td></tr>
<tr><td><code>Paresthesia</code></td><td><code>ncit:C143736</code></td><td></td></tr>
<tr><td><code>Dental Developmental Abnormality</code></td><td><code>ncit:C35596</code></td><td></td></tr>
<tr><td><code>Dermatitis</code></td><td><code>ncit:C2983</code></td><td></td></tr>
<tr><td><code>Dysphagia</code></td><td><code>ncit:C57795</code></td><td></td></tr>
<tr><td><code>Febrile Neutropenia</code></td><td><code>ncit:C35665</code></td><td></td></tr>
<tr><td><code>Growth Hormone Deficiency</code></td><td><code>ncit:C112835</code></td><td></td></tr>
<tr><td><code>Hearing Impaired</code></td><td><code>ncit:C143528</code></td><td></td></tr>
<tr><td><code>Hematuria</code></td><td><code>ncit:C3090</code></td><td></td></tr>
<tr><td><code>Hoarseness</code></td><td><code>ncit:C47813</code></td><td></td></tr>
<tr><td><code>Hypopituitarism</code></td><td><code>ncit:C143194</code></td><td></td></tr>
<tr><td><code>Hypothyroidism</code></td><td><code>ncit:C143576</code></td><td></td></tr>
<tr><td><code>Mucositis</code></td><td><code>ncit:C115965</code></td><td></td></tr>
<tr><td><code>Neck Fibrosis</code></td><td><code>ncit:C55368</code></td><td></td></tr>
<tr><td><code>Neutropenia</code></td><td><code>ncit:C80520</code></td><td></td></tr>
<tr><td><code>Optic Nerve Disorder</code></td><td><code>ncit:C143714</code></td><td></td></tr>
<tr><td><code>Osteoradionecrosis</code></td><td><code>ncit:C115459</code></td><td></td></tr>
<tr><td><code>Ototoxicity</code></td><td><code>ncit:C66929</code></td><td></td></tr>
<tr><td><code>Proteinuria</code></td><td><code>ncit:C38012</code></td><td></td></tr>
<tr><td><code>Psychiatric Toxicity</code></td><td><code>ncit:C185648</code></td><td></td></tr>
<tr><td><code>Pulmonary Toxicity</code></td><td><code>ncit:C177374</code></td><td></td></tr>
<tr><td><code>Radiation Caries</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal Toxicity</code></td><td><code>ncit:C115459</code></td><td></td></tr>
<tr><td><code>Retinopathy</code></td><td><code>ncit:C55891</code></td><td></td></tr>
<tr><td><code>Spinal Cord Toxicity</code></td><td><code>ncit:C55369</code></td><td></td></tr>
<tr><td><code>Stroke</code></td><td><code>ncit:C143862</code></td><td></td></tr>
<tr><td><code>Thrombocytopenia</code></td><td><code>ncit:C3408</code></td><td></td></tr>
<tr><td><code>Tinnitus</code></td><td><code>ncit:C146690</code></td><td></td></tr>
<tr><td><code>Trismus</code></td><td><code>ncit:C58404</code></td><td></td></tr>
<tr><td><code>Vertigo</code></td><td><code>ncit:C143935</code></td><td></td></tr>
<tr><td><code>Vision Decreased</code></td><td><code>ncit:C143196</code></td><td></td></tr>
<tr><td><code>Weight Loss</code></td><td><code>ncit:C55339</code></td><td></td></tr>
<tr><td><code>Xerostomia</code></td><td><code>ncit:C26917</code></td><td></td></tr>
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
<tr><td><code>RTOG</code></td><td><code>ncit:C19778</code></td><td></td></tr>
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
<tr><td><code>CTCAE &gt;&gt; Grade 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG &gt;&gt; Grade 3/Grade 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG &gt;&gt; Grade1/Grade2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-boosttypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-boosttypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-boosttypeenum')">×</button>
<h3><code>BoostTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>None</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequential</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Simultaneous Integrated</code></td><td><code>ncit:C121139</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-causeofdeathdetailenum" class="enum-modal" onclick="closeEnumModal('enum-modal-causeofdeathdetailenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-causeofdeathdetailenum')">×</button>
<h3><code>CauseOfDeathDetailEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bacterial Infection</code></td><td><code>ncit:C2890</code></td><td></td></tr>
<tr><td><code>Cardiac Disease</code></td><td><code>ncit:C3079</code></td><td></td></tr>
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Immunotherapy-Related</code></td><td><code>ncit:C168874</code></td><td></td></tr>
<tr><td><code>Infection, NOS</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Multi-Organ Failure</code></td><td><code>ncit:C75568</code></td><td></td></tr>
<tr><td><code>Pulmonary Disease</code></td><td><code>ncit:C3198</code></td><td></td></tr>
<tr><td><code>Surgical Complication</code></td><td><code>ncit:C164157</code></td><td></td></tr>
<tr><td><code>Viral Infection</code></td><td><code>ncit:C3439</code></td><td></td></tr>
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
<tr><td><code>Post-Treatment Disease Complications</code></td><td><code>ncit:C168877</code></td><td></td></tr>
<tr><td><code>Secondary Malignancy</code></td><td><code>ncit:C4968</code></td><td>D4CGNote: Use the Subsequent Malignant Neoplasm table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Unrelated to Disease or Treatment</code></td><td><code>ncit:C17649</code></td><td>(cns) ConsortiumNote: Deceased-due to other causes.<br>(fa) ConsortiumNote: Deceased-due to other causes.</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(cns) ConsortiumNote: Deceased-causes unavailable.<br>(fa) ConsortiumNote: Deceased-causes unavailable.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-causeofdeathrankingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-causeofdeathrankingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-causeofdeathrankingenum')">×</button>
<h3><code>CauseOfDeathRankingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Contributory</code></td><td><code>ncit:C168948</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C99531</code></td><td>(os) ConsortiumNote: There may be multiple contributory causes of death, but only one primary cause of death. Note: Only fill in this variable if LKSS is 'Dead'.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>NOBLE</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Chemotherapy, NOS</code></td><td><code>ncit:C15632</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
<tr><td><code>Concomitant Chemoradiation Therapy</code></td><td><code></code></td><td>(npc) ConsortiumNotes: Specifically for TROD data.</td></tr>
<tr><td><code>Immunotherapy</code></td><td><code>ncit:C15262</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
<tr><td><code>Induction</code></td><td><code>ncit:C158876</code></td><td></td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code>ncit:C15313</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
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
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Endoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Imaging, NOS</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>Technetium Bone Scan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X-Ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
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
<tr><td><code>Basaloid squamous cell carcinoma</code></td><td><code>icdo:8083/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, Keratinizing, NOS</code></td><td><code>icdo:8071/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, Large Cell, Nonkeratinizing, NOS</code></td><td><code>icdo:8072/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, NOS</code></td><td><code>icdo:8070/3</code></td><td></td></tr>
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
<tr><td><code>NPC</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Refractory/Progression</code></td><td><code>ncit:C174991</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
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
<tr><td><code>Electron</code></td><td><code>ncit:C40428</code></td><td></td></tr>
<tr><td><code>Photon</code></td><td><code>ncit:C88112</code></td><td></td></tr>
<tr><td><code>Proton</code></td><td><code>ncit:C66897</code></td><td></td></tr>
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

<div id="enum-modal-fractiondoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">×</button>
<h3><code>FractionDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CGE</code></td><td><code>ncit:C128269</code></td><td></td></tr>
<tr><td><code>Gy</code></td><td><code>ncit:C18063</code></td><td></td></tr>
<tr><td><code>cGy</code></td><td><code>ncit:C64693</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-functiontestenum" class="enum-modal" onclick="closeEnumModal('enum-modal-functiontestenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-functiontestenum')">×</button>
<h3><code>FunctionTestEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Audiogram, NOS</code></td><td><code>ncit:C92448</code></td><td></td></tr>
<tr><td><code>Cochlear, OEAP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cochlear, PEAP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vestibular, VHIT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vestibular, cVEMP</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-functiontestgradeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-functiontestgradeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-functiontestgradeenum')">×</button>
<h3><code>FunctionTestGradeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chang &gt;&gt; Grade 0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 1a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 1b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 2a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 2b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chang &gt;&gt; Grade 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP Boston &gt;&gt; Grade 0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP Boston &gt;&gt; Grade 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP Boston &gt;&gt; Grade 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP Boston &gt;&gt; Grade 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP Boston &gt;&gt; Grade 4</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-functiontestlateralityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-functiontestlateralityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-functiontestlateralityenum')">×</button>
<h3><code>FunctionTestLateralityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bilateral</code></td><td><code>ncit:C13332</code></td><td></td></tr>
<tr><td><code>Left</code></td><td><code>ncit:C160200</code></td><td></td></tr>
<tr><td><code>Right</code></td><td><code>ncit:C160199</code></td><td></td></tr>
<tr><td><code>Unilateral</code></td><td><code>ncit:C28012</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-functionalmeasurementresultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-functionalmeasurementresultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-functionalmeasurementresultunitenum')">×</button>
<h3><code>FunctionalMeasurementResultUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>%</code></td><td><code></code></td><td></td></tr>
<tr><td><code>dB</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>With Lymphoid Infiltration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Without Lymphoid Infiltration</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hzfrequencyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hzfrequencyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hzfrequencyenum')">×</button>
<h3><code>HzFrequencyEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>16000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>2000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>4000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>500</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8000</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>EBER</code></td><td><code>ncit:C96602</code></td><td></td></tr>
<tr><td><code>EBV DNA</code></td><td><code>ncit:C166035</code></td><td></td></tr>
<tr><td><code>EBV IgG</code></td><td><code>ncit:C184675</code></td><td></td></tr>
<tr><td><code>EBV-PCR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBV-VCA-IgA-IFT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Free T3</code></td><td><code>ncit:C74787</code></td><td></td></tr>
<tr><td><code>Free T4</code></td><td><code>ncit:C74786</code></td><td></td></tr>
<tr><td><code>TSH</code></td><td><code>ncit:C64813</code></td><td></td></tr>
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
<tr><td><code>IU/mL</code></td><td><code>ncit:C67378</code></td><td></td></tr>
<tr><td><code>U/L</code></td><td><code>ncit:C67456</code></td><td></td></tr>
<tr><td><code>U/mL</code></td><td><code>ncit:C77607</code></td><td></td></tr>
<tr><td><code>cp/mL</code></td><td><code></code></td><td></td></tr>
<tr><td><code>g/dL</code></td><td><code>ncit:C64783</code></td><td></td></tr>
<tr><td><code>mg/dL</code></td><td><code>ncit:C67015</code></td><td></td></tr>
<tr><td><code>mmol/L</code></td><td><code>ncit:C64387</code></td><td></td></tr>
<tr><td><code>pmol/L</code></td><td><code>ncit:C67434</code></td><td></td></tr>
<tr><td><code>ng/mL</code></td><td><code>ncit:C67306</code></td><td></td></tr>
<tr><td><code>ng/dL</code></td><td><code>ncit:C67326</code></td><td></td></tr>
<tr><td><code>ng/L</code></td><td><code>ncit:C67327</code></td><td></td></tr>
<tr><td><code>uIU/mL</code></td><td><code>ncit:C67405</code></td><td></td></tr>
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
<tr><td><code>Serum</code></td><td><code>ncit:C178987</code></td><td></td></tr>
<tr><td><code>Tumor</code></td><td><code>ncit:C18009</code></td><td></td></tr>
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

<div id="enum-modal-lesionmeasurementunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lesionmeasurementunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lesionmeasurementunitenum')">×</button>
<h3><code>LesionMeasurementUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mm</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-medicationdoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">×</button>
<h3><code>MedicationDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>IU</code></td><td><code>ncit:C48579</code></td><td></td></tr>
<tr><td><code>IU/m2</code></td><td><code>ncit:C67378</code></td><td></td></tr>
<tr><td><code>mg</code></td><td><code>ncit:C28253</code></td><td></td></tr>
<tr><td><code>mg/kg</code></td><td><code>ncit:C105468</code></td><td></td></tr>
<tr><td><code>mg/m2</code></td><td><code>ncit:C67402</code></td><td></td></tr>
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
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Fluorouracil (5FU)</code></td><td><code>rxcui:4492</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Interferon</code></td><td><code>ncit:C20493</code></td><td></td></tr>
<tr><td><code>Ipilimumab</code></td><td><code>ncit:C2654</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Sodium Thiosulfate</code></td><td><code>ncit:C1230</code></td><td>(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'<br>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Tetrathiomolybdate (TM)</code></td><td><code>ncit:C160684</code></td><td></td></tr>
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

<div id="enum-modal-multiplicityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-multiplicityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-multiplicityenum')">×</button>
<h3><code>MultiplicityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Multiple</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Single</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Craniofacial Resection</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure.<br>(os) ConsortiumNote: Resection procedure.</td></tr>
<tr><td><code>Excisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Incisional Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung Resection, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymph Node Dissection, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-procedureextentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-procedureextentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-procedureextentenum')">×</button>
<h3><code>ProcedureExtentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Complete Resection</code></td><td><code>ncit:C175027</code></td><td></td></tr>
<tr><td><code>Equivocal</code></td><td><code>ncit:C178921</code></td><td></td></tr>
<tr><td><code>Gross Total</code></td><td><code>ncit:C131672</code></td><td></td></tr>
<tr><td><code>Partial Resection</code></td><td><code>ncit:C131680</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cervical Nodes</code></td><td><code>ncit:C32298</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
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

<div id="enum-modal-reasonoffenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasonoffenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasonoffenum')">×</button>
<h3><code>ReasonOffEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Completion of Planned Therapy</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Death</code></td><td><code>ncit:C28554</code></td><td>(os) ConsortiumNote: If multiple reasons for off 'Protocol Therapy' or off 'Study', include one observation per reason.</td></tr>
<tr><td><code>Development of SMN</code></td><td><code>ncit:C4968</code></td><td></td></tr>
<tr><td><code>Disease Progression</code></td><td><code>ncit:C17747</code></td><td></td></tr>
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Toxicity</code></td><td><code>ncit:C27990</code></td><td></td></tr>
<tr><td><code>Withdrawal of Consent</code></td><td><code>ncit:C48271</code></td><td></td></tr>
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
<tr><td><code>Lymph Node Response</code></td><td><code>ncit:C159957</code></td><td></td></tr>
<tr><td><code>Metastatic Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Overall Response</code></td><td><code>ncit:C96613</code></td><td></td></tr>
<tr><td><code>Primary Site Response</code></td><td><code>ncit:C200253</code></td><td></td></tr>
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
<tr><td><code>EXPeRT &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EXPeRT &gt;&gt; Minor Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EXPeRT &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EXPeRT &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EXPeRT &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EXPeRT &gt;&gt; Very Good Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Not Evaluable</code></td><td><code>ncit:C62222</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Partial Response</code></td><td><code>ncit:C159547</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Progressive Disease</code></td><td><code>ncit:C159716</code></td><td></td></tr>
<tr><td><code>RECIST &gt;&gt; Stable Disease</code></td><td><code>ncit:C159546</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Partial Response</code></td><td><code>ncit:C18058</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stable Disease</code></td><td><code>ncit:C18213</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Very Good Partial Response</code></td><td><code>ncit:C123618</code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>EXPeRT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RECIST</code></td><td><code>ncit:C49164</code></td><td></td></tr>
<tr><td><code>WHO</code></td><td><code>ncit:C75419</code></td><td></td></tr>
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
<tr><td><code>CGE</code></td><td><code>ncit:C128269</code></td><td></td></tr>
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
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level I Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level II Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level III Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level IV Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level V Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Regional Lymph Nodes, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retropharyngeal Nodes</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Local Extension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metastatic</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-smnfieldenum" class="enum-modal" onclick="closeEnumModal('enum-modal-smnfieldenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-smnfieldenum')">×</button>
<h3><code>SmnFieldEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>In XRT Field</code></td><td><code>ncit:C175045</code></td><td></td></tr>
<tr><td><code>Margin of XRT Field</code></td><td><code>ncit:C185695</code></td><td></td></tr>
<tr><td><code>Out of XRT Field</code></td><td><code>ncit:C175046</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-smnsiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-smnsiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-smnsiteenum')">×</button>
<h3><code>SmnSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abdomen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Limbs</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Carcinoma</code></td><td><code>ncit:C2916</code></td><td></td></tr>
<tr><td><code>Leukemia</code></td><td><code>ncit:C3161</code></td><td></td></tr>
<tr><td><code>Lymphoma</code></td><td><code>ncit:C3208</code></td><td></td></tr>
<tr><td><code>Soft Tissue Sarcoma</code></td><td><code>ncit:C9306</code></td><td></td></tr>
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
<tr><td><code>AJCC</code></td><td><code>ncit:C39315</code></td><td></td></tr>
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
<tr><td><code>ARAR0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GPOH-NPC 2016 Registry</code></td><td><code></code></td><td>(npc) ConsortiumNote: data_contributor_id == 'GPOH'</td></tr>
<tr><td><code>ISPHO</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GPOH-NPC-2003 Study</code></td><td><code></code></td><td>(npc) ConsortiumNote: data_contributor_id == 'GPOH'</td></tr>
<tr><td><code>GPOH-NPC-91 Study</code></td><td><code></code></td><td>(npc) ConsortiumNote: data_contributor_id == 'GPOH'</td></tr>
<tr><td><code>TATA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TROD1</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bleomycin + Doxurubicin + Cisplatin (BAC)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cisplatin + Docetaxel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cisplatin + Gemcitabine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cisplatine + 5FU</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Docetaxel + Cisplatin + 5FU</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Brachytherapy</code></td><td><code>ncit:C15195</code></td><td></td></tr>
<tr><td><code>EBRT, 3D Conformal</code></td><td><code>ncit:C16035</code></td><td></td></tr>
<tr><td><code>EBRT, Double Scattering</code></td><td><code></code></td><td>(npc) ConsortiumNote: ENERGY_TYPE = Proton</td></tr>
<tr><td><code>EBRT, Intensity-Modulated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Pencil Beam Scanning</code></td><td><code>ncit:C165502</code></td><td>(npc) ConsortiumNote: ENERGY_TYPE = Proton</td></tr>
<tr><td><code>EBRT, Stereotactic Body</code></td><td><code>ncit:C118286</code></td><td>(npc) ConsortiumNote: Stereotactic ablative body radiotherapy</td></tr>
<tr><td><code>EBRT, Stereotactic Radiosurgery</code></td><td><code>ncit:C15358</code></td><td></td></tr>
<tr><td><code>EBRT, Tomotherapy</code></td><td><code>ncit:C62731</code></td><td>(npc) ConsortiumNote: Helical IMRT</td></tr>
<tr><td><code>EBRT, Volume Modulated Arc Therapy</code></td><td><code>ncit:C104933</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tnmmetastasismenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tnmmetastasismenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tnmmetastasismenum')">×</button>
<h3><code>TnmMetastasisMEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>M0</code></td><td><code>ncit:C48699</code></td><td></td></tr>
<tr><td><code>M1</code></td><td><code>ncit:C48700</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tnmnodenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tnmnodenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tnmnodenenum')">×</button>
<h3><code>TnmNodeNEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>N0</code></td><td><code>ncit:C48705</code></td><td></td></tr>
<tr><td><code>N1</code></td><td><code>ncit:C48706</code></td><td></td></tr>
<tr><td><code>N2</code></td><td><code>ncit:C48786</code></td><td></td></tr>
<tr><td><code>N3</code></td><td><code>ncit:C48714</code></td><td></td></tr>
<tr><td><code>N3a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>N3b</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tnmtumortenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tnmtumortenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tnmtumortenum')">×</button>
<h3><code>TnmTumorTEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>T0</code></td><td><code>ncit:C48719</code></td><td></td></tr>
<tr><td><code>T1</code></td><td><code>ncit:C48720</code></td><td></td></tr>
<tr><td><code>T2</code></td><td><code>ncit:C48724</code></td><td></td></tr>
<tr><td><code>T2a</code></td><td><code>ncit:C48725</code></td><td></td></tr>
<tr><td><code>T2b</code></td><td><code>ncit:C48726</code></td><td></td></tr>
<tr><td><code>T3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T4</code></td><td><code>ncit:C48732</code></td><td></td></tr>
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

<div id="enum-modal-treatmentvolumeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-treatmentvolumeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-treatmentvolumeenum')">×</button>
<h3><code>TreatmentVolumeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>PTV High Risk</code></td><td><code></code></td><td>(npc) ConsortiumNote: Use for PTV1</td></tr>
<tr><td><code>PTV Intermediate Risk</code></td><td><code></code></td><td>(npc) ConsortiumNote: Use for PTV2</td></tr>
<tr><td><code>PTV Low Risk</code></td><td><code></code></td><td>(npc) ConsortiumNote: Use for PTV3</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-trmtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-trmtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-trmtypeenum')">×</button>
<h3><code>TrmTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chemotherapy</code></td><td><code>ncit:C15632</code></td><td></td></tr>
<tr><td><code>Immunotherapy</code></td><td><code>ncit:C15262</code></td><td></td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code></code></td><td></td></tr>
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
    "npc": {
      "name": "npc",
      "title": "Nasopharyngeal Carcinoma",
      "description": "The NPC view of the PCDC data model represents consensus data modeling by an international group of pediatric nasopharyngeal carcinoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Nasopharyngeal Carcinoma Global Partnership (NOBLE). It is based on the collective requirements of its contributors."
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
        "enrolled_status",
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
    "StudySubgroupAssignment": {
      "slots": [
        "subgroup_type",
        "subgroup_name",
        "subgroup_assignment_order",
        "age_at_subgroup_assignment"
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
        "reason_off",
        "reason_off_other",
        "another_study"
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
        "lkss",
        "lkss_with_disease",
        "cause_of_death",
        "trm_type",
        "cause_of_death_detail",
        "cause_of_death_ranking"
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
    "LaboratoryTest": {
      "slots": [
        "age_at_lab",
        "laboratory_test",
        "laboratory_test_specimen",
        "result_text",
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
    "FunctionTest": {
      "slots": [
        "age_at_function_test",
        "function_test",
        "result_text",
        "result_numeric",
        "functional_measurement_result_unit",
        "function_test_laterality",
        "hz_frequency",
        "average_loss_low",
        "average_loss_high",
        "function_test_grade"
      ],
      "comments": [
        "D4CGNote: One observation/row per result when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Optional.",
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
        "tnm_tumor_t",
        "tnm_node_n",
        "tnm_metastasis_m",
        "stage_system",
        "stage_system_version",
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
        "detection_method",
        "site_classification",
        "disease_site",
        "laterality",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "multiplicity"
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
        "procedure",
        "procedure_other",
        "procedure_site",
        "laterality",
        "procedure_extent"
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
        "administration_status",
        "cycles_planned",
        "cycle_number",
        "medication",
        "number_doses",
        "medication_dose_administered",
        "medication_dose_intended",
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
        "boost_type",
        "boost_dose",
        "num_fraction",
        "fraction_dose",
        "fraction_dose_unit",
        "treatment_volume"
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
        "age_at_ae_resolved",
        "adverse_event",
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
        "smn_site",
        "smn_type",
        "morph_code",
        "morph_code_text",
        "morph_code_system",
        "morph_code_system_version",
        "top_code",
        "top_code_text",
        "top_code_system",
        "top_code_system_version",
        "smn_field"
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
    "another_study": {
      "slot_uri": "ncit:C178073",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb",
        "tier_optional": "npc"
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
    "response_system": {
      "slot_uri": "ncit:C125932",
      "range": "ResponseSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,rb"
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
    "tnm_tumor_t": {
      "slot_uri": "",
      "range": "TnmTumorTEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,ls",
        "tier_priority": "fa,rb"
      }
    },
    "age_at_function_test": {
      "slot_uri": "ncit:C185624",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "procedure_other": {
      "slot_uri": "",
      "range": "string",
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
    "multiplicity": {
      "slot_uri": "",
      "range": "MultiplicityEnum",
      "comments": [
        "(ews) ConsortiumNote: Only if the 'multiple' tumors/lesions don't have individual characteristics to report. Otherwise, report as multiple rows."
      ],
      "annotations": {
        "tier_optional": "npc"
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
    "top_code_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "ls"
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
    "average_loss_high": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
      }
    },
    "enrolled_status": {
      "slot_uri": "ncit:C168928",
      "range": "YesNoEnum",
      "comments": [
        "(aml) ConsortiumNote: This variable indicates if the subject was enrolled in the study, or if the subject was not enrolled in the study but received treatment per the study's protocol."
      ],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "npc,ls"
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
    "stage_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt,npc"
      }
    },
    "smn_site": {
      "slot_uri": "",
      "range": "SmnSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc"
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
    "function_test_grade": {
      "slot_uri": "",
      "range": "FunctionTestGradeEnum",
      "comments": [],
      "annotations": {}
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
    "smn_field": {
      "slot_uri": "ncit:C175044",
      "range": "SmnFieldEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "cause_of_death_ranking": {
      "slot_uri": "ncit:C168932",
      "range": "CauseOfDeathRankingEnum",
      "comments": [
        "D4CGNote: There may be multiple contributory causes of death, but only one primary cause of death.\nD4CGNote: Only fill in this variable if LKSS is \"Dead\"",
        "(aml) ConsortiumNote: There may be multiple contributory causes of death, but only one primary cause of death.",
        "(aml) ConsortiumNote:  Only fill in this variable if LKSS is 'Dead'",
        "(cns) ConsortiumNote: There may be multiple contributory causes of death, but only one primary cause of death. Note: Only fill in this variable if LKSS is 'Dead'.",
        "(ews) ConsortiumNote: There may be multiple contributory causes of death, but only one primary cause of death. Note: Only fill in this variable if LKSS is 'Dead'",
        "D4CGNote: There may be multiple contributory causes of death, but only one primary cause of death.\\n D4CGNote: Only fill in this variable if 'LKSS' = 'Dead'."
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "aml",
        "tier_optional": "npc,rb"
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
    "cycle_number": {
      "slot_uri": "ncit:C166208",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: For RB, this field should be used to designate the cycle of systemic chemotherapy being described in the observation"
      ],
      "annotations": {
        "tier_optional": "npc",
        "tier_priority": "rb"
      }
    },
    "trm_type": {
      "slot_uri": "ncit:C173260",
      "range": "TrmTypeEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple treatment types, include one observation per treatment type.",
        "(aml) ConsortiumNote:  Only fill in this variable if LKSS is 'Dead' and CAUSE_OF_DEATH is 'Treatment-related mortality'"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb,fa,aml",
        "tier_optional": "npc"
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
    "tnm_metastasis_m": {
      "slot_uri": "",
      "range": "TnmMetastasisMEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,ls",
        "tier_priority": "fa,rb"
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
    "number_doses": {
      "slot_uri": "ncit:C173293",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Number of doses of chemotherapy agent administered over the indicated start and end time points Note: Only fill in this variable if this information is available.",
        "(hl) ConsortiumNote: Number of doses of chemotherapy agent administered over the indicated start and end time points Note: Only fill in this variable if this information is available.",
        "(rb) ConsortiumNote: Number of doses of chemotherapy agent administered over the indicated start and end time points Note: Only fill in this variable if this information is available."
      ],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc"
      }
    },
    "hz_frequency": {
      "slot_uri": "",
      "range": "HzFrequencyEnum",
      "comments": [],
      "annotations": {
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
    "reason_off_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "npc",
        "tier_priority": "rb"
      }
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
    "cause_of_death_detail": {
      "slot_uri": "ncit:C168868",
      "range": "CauseOfDeathDetailEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.",
        "(aml) ConsortiumNote:  Only fill in this variable if LKSS is 'Dead'",
        "(fa) ConsortiumNote: Multi-select"
      ],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa,aml",
        "tier_optional": "npc,rb"
      }
    },
    "function_test": {
      "slot_uri": "ncit:C186304",
      "range": "FunctionTestEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa",
        "tier_priority": "npc"
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
    "treatment_volume": {
      "slot_uri": "",
      "range": "TreatmentVolumeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
      }
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
    "tnm_node_n": {
      "slot_uri": "",
      "range": "TnmNodeNEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,ls",
        "tier_priority": "fa,rb"
      }
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
    "average_loss_low": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
      }
    },
    "lkss_with_disease": {
      "slot_uri": "ncit:C178074",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb",
        "tier_optional": "fa,npc"
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
    "functional_measurement_result_unit": {
      "slot_uri": "",
      "range": "FunctionalMeasurementResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
      }
    },
    "boost_type": {
      "slot_uri": "ncit:C137812",
      "range": "BoostTypeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,rb"
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
    "procedure_extent": {
      "slot_uri": "ncit:C157443",
      "range": "ProcedureExtentEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,ls"
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
    "age_at_ae_resolved": {
      "slot_uri": "ncit:C175043",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "hl,rb"
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
    "response_system_version": {
      "slot_uri": "ncit:C175042",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "administration_status": {
      "slot_uri": "ncit:C173297",
      "range": "AdministrationStatusEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "npc",
        "tier_priority": "rb"
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
    "measurement2": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "function_test_laterality": {
      "slot_uri": "",
      "range": "FunctionTestLateralityEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,fa"
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
    "medication_dose_intended": {
      "slot_uri": "ncit:C173294",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Intention-to-treat total dose of the chemotherapy agent over the indicated start and end time points. Note: Only fill in this variable if this information is available.",
        "(hl) ConsortiumNote: Intention-to-treat total dose of the chemotherapy agent over the indicated start and end time points. Note: Only fill in this variable if this information is available.",
        "(rb) ConsortiumNote: Intention-to-treat total dose of the chemotherapy agent over the indicated start and end time points. Note: Only fill in this variable if this information is available."
      ],
      "annotations": {
        "tier_optional": "npc,rb"
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
    "MorphCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
          "comments": []
        }
      }
    },
    "FunctionTestGradeEnum": {
      "permissible_values": {
        "Chang >> Grade 0": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 1a": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 1b": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 2a": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 2b": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 3": {
          "meaning": "",
          "comments": []
        },
        "Chang >> Grade 4": {
          "meaning": "",
          "comments": []
        },
        "SIOP Boston >> Grade 0": {
          "meaning": "",
          "comments": []
        },
        "SIOP Boston >> Grade 1": {
          "meaning": "",
          "comments": []
        },
        "SIOP Boston >> Grade 2": {
          "meaning": "",
          "comments": []
        },
        "SIOP Boston >> Grade 3": {
          "meaning": "",
          "comments": []
        },
        "SIOP Boston >> Grade 4": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ResponseEnum": {
      "permissible_values": {
        "EXPeRT >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "EXPeRT >> Minor Response": {
          "meaning": "",
          "comments": []
        },
        "EXPeRT >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "EXPeRT >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "EXPeRT >> Stable Disease": {
          "meaning": "",
          "comments": []
        },
        "EXPeRT >> Very Good Partial Response": {
          "meaning": "",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
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
        "System NOS >> Very Good Partial Response": {
          "meaning": "ncit:C123618",
          "comments": []
        },
        "WHO >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "WHO >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "WHO >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "WHO >> Stable Disease": {
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
        "Chemotherapy, NOS": {
          "meaning": "ncit:C15632",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
        },
        "Concomitant Chemoradiation Therapy": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNotes: Specifically for TROD data."
          ]
        },
        "Immunotherapy": {
          "meaning": "ncit:C15262",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
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
        },
        "Radiation Therapy": {
          "meaning": "ncit:C15313",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
        }
      }
    },
    "TnmTumorTEnum": {
      "permissible_values": {
        "T0": {
          "meaning": "ncit:C48719",
          "comments": []
        },
        "T1": {
          "meaning": "ncit:C48720",
          "comments": []
        },
        "T2": {
          "meaning": "ncit:C48724",
          "comments": []
        },
        "T2a": {
          "meaning": "ncit:C48725",
          "comments": []
        },
        "T2b": {
          "meaning": "ncit:C48726",
          "comments": []
        },
        "T3": {
          "meaning": "",
          "comments": []
        },
        "T4": {
          "meaning": "ncit:C48732",
          "comments": []
        }
      }
    },
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Bone Marrow": {
          "meaning": "ncit:C12431",
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
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        },
        "Soft Tissue": {
          "meaning": "ncit:C12471",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
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
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "TnmMetastasisMEnum": {
      "permissible_values": {
        "M0": {
          "meaning": "ncit:C48699",
          "comments": []
        },
        "M1": {
          "meaning": "ncit:C48700",
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
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "ReasonOffEnum": {
      "permissible_values": {
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
        "Lost to Follow-Up": {
          "meaning": "ncit:C70740",
          "comments": []
        },
        "Physician Decision": {
          "meaning": "ncit:C48250",
          "comments": []
        },
        "Subject/Guardian Refused Further Treatment": {
          "meaning": "ncit:C168934",
          "comments": []
        },
        "Toxicity": {
          "meaning": "ncit:C27990",
          "comments": []
        },
        "Withdrawal of Consent": {
          "meaning": "ncit:C48271",
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
    "CauseOfDeathRankingEnum": {
      "permissible_values": {
        "Contributory": {
          "meaning": "ncit:C168948",
          "comments": []
        },
        "Primary": {
          "meaning": "ncit:C99531",
          "comments": [
            "(os) ConsortiumNote: There may be multiple contributory causes of death, but only one primary cause of death. Note: Only fill in this variable if LKSS is 'Dead'."
          ]
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
        "Serum": {
          "meaning": "ncit:C178987",
          "comments": []
        },
        "Tumor": {
          "meaning": "ncit:C18009",
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
    "HzFrequencyEnum": {
      "permissible_values": {
        "1000": {
          "meaning": "",
          "comments": []
        },
        "16000": {
          "meaning": "",
          "comments": []
        },
        "2000": {
          "meaning": "",
          "comments": []
        },
        "4000": {
          "meaning": "",
          "comments": []
        },
        "500": {
          "meaning": "",
          "comments": []
        },
        "8000": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TnmNodeNEnum": {
      "permissible_values": {
        "N0": {
          "meaning": "ncit:C48705",
          "comments": []
        },
        "N1": {
          "meaning": "ncit:C48706",
          "comments": []
        },
        "N2": {
          "meaning": "ncit:C48786",
          "comments": []
        },
        "N3": {
          "meaning": "ncit:C48714",
          "comments": []
        },
        "N3a": {
          "meaning": "",
          "comments": []
        },
        "N3b": {
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
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "",
          "comments": []
        },
        "Level I Nodes": {
          "meaning": "",
          "comments": []
        },
        "Level II Nodes": {
          "meaning": "",
          "comments": []
        },
        "Level III Nodes": {
          "meaning": "",
          "comments": []
        },
        "Level IV Nodes": {
          "meaning": "",
          "comments": []
        },
        "Level V Nodes": {
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
        "Nasopharynx": {
          "meaning": "",
          "comments": []
        },
        "Regional Lymph Nodes, NOS": {
          "meaning": "",
          "comments": []
        },
        "Retropharyngeal Nodes": {
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
    "ResponseSystemEnum": {
      "permissible_values": {
        "EXPeRT": {
          "meaning": "",
          "comments": []
        },
        "RECIST": {
          "meaning": "ncit:C49164",
          "comments": []
        },
        "WHO": {
          "meaning": "ncit:C75419",
          "comments": []
        }
      }
    },
    "MultiplicityEnum": {
      "permissible_values": {
        "Multiple": {
          "meaning": "",
          "comments": []
        },
        "Single": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
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
    "BoostTypeEnum": {
      "permissible_values": {
        "None": {
          "meaning": "",
          "comments": []
        },
        "Sequential": {
          "meaning": "",
          "comments": []
        },
        "Simultaneous Integrated": {
          "meaning": "ncit:C121139",
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
        }
      }
    },
    "FunctionTestLateralityEnum": {
      "permissible_values": {
        "Bilateral": {
          "meaning": "ncit:C13332",
          "comments": []
        },
        "Left": {
          "meaning": "ncit:C160200",
          "comments": []
        },
        "Right": {
          "meaning": "ncit:C160199",
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
        "IU": {
          "meaning": "ncit:C48579",
          "comments": []
        },
        "IU/m2": {
          "meaning": "ncit:C67378",
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
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "CauseOfDeathDetailEnum": {
      "permissible_values": {
        "Bacterial Infection": {
          "meaning": "ncit:C2890",
          "comments": []
        },
        "Cardiac Disease": {
          "meaning": "ncit:C3079",
          "comments": []
        },
        "Fungal Infection": {
          "meaning": "ncit:C3245",
          "comments": []
        },
        "Graft Versus Host Disease": {
          "meaning": "ncit:C3063",
          "comments": []
        },
        "Hemorrhage": {
          "meaning": "ncit:C26791",
          "comments": [
            "(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail."
          ]
        },
        "Immunotherapy-Related": {
          "meaning": "ncit:C168874",
          "comments": []
        },
        "Infection, NOS": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Multi-Organ Failure": {
          "meaning": "ncit:C75568",
          "comments": []
        },
        "Pulmonary Disease": {
          "meaning": "ncit:C3198",
          "comments": []
        },
        "Surgical Complication": {
          "meaning": "ncit:C164157",
          "comments": []
        },
        "Viral Infection": {
          "meaning": "ncit:C3439",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "SmnSiteEnum": {
      "permissible_values": {
        "Abdomen": {
          "meaning": "",
          "comments": []
        },
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Limbs": {
          "meaning": "",
          "comments": []
        },
        "Pelvis": {
          "meaning": "",
          "comments": []
        },
        "Thorax": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "StageSystemEnum": {
      "permissible_values": {
        "AJCC": {
          "meaning": "ncit:C39315",
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
        "Post-Treatment Disease Complications": {
          "meaning": "ncit:C168877",
          "comments": []
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
        "Unrelated to Disease or Treatment": {
          "meaning": "ncit:C17649",
          "comments": [
            "(cns) ConsortiumNote: Deceased-due to other causes.",
            "(fa) ConsortiumNote: Deceased-due to other causes."
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
        "ARAR0331": {
          "meaning": "",
          "comments": []
        },
        "GPOH-NPC 2016 Registry": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: data_contributor_id == 'GPOH'"
          ]
        },
        "ISPHO": {
          "meaning": "",
          "comments": []
        },
        "GPOH-NPC-2003 Study": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: data_contributor_id == 'GPOH'"
          ]
        },
        "GPOH-NPC-91 Study": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: data_contributor_id == 'GPOH'"
          ]
        },
        "TATA": {
          "meaning": "",
          "comments": []
        },
        "TROD1": {
          "meaning": "",
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
    "HistologicFeaturesEnum": {
      "permissible_values": {
        "With Lymphoid Infiltration": {
          "meaning": "",
          "comments": []
        },
        "Without Lymphoid Infiltration": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Basaloid squamous cell carcinoma": {
          "meaning": "icdo:8083/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, Keratinizing, NOS": {
          "meaning": "icdo:8071/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, Large Cell, Nonkeratinizing, NOS": {
          "meaning": "icdo:8072/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, NOS": {
          "meaning": "icdo:8070/3",
          "comments": []
        }
      }
    },
    "EnergyTypeEnum": {
      "permissible_values": {
        "Electron": {
          "meaning": "ncit:C40428",
          "comments": []
        },
        "Photon": {
          "meaning": "ncit:C88112",
          "comments": []
        },
        "Proton": {
          "meaning": "ncit:C66897",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
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
    "SmnTypeEnum": {
      "permissible_values": {
        "Carcinoma": {
          "meaning": "ncit:C2916",
          "comments": []
        },
        "Leukemia": {
          "meaning": "ncit:C3161",
          "comments": []
        },
        "Lymphoma": {
          "meaning": "ncit:C3208",
          "comments": []
        },
        "Soft Tissue Sarcoma": {
          "meaning": "ncit:C9306",
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
    "DetectionMethodEnum": {
      "permissible_values": {
        "CT Scan": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "Endoscopy": {
          "meaning": "",
          "comments": []
        },
        "Imaging, NOS": {
          "meaning": "ncit:C17369",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "PET Scan": {
          "meaning": "ncit:C17007",
          "comments": []
        },
        "PET-CT": {
          "meaning": "ncit:C103512",
          "comments": []
        },
        "Technetium Bone Scan": {
          "meaning": "",
          "comments": []
        },
        "X-Ray": {
          "meaning": "ncit:C38101",
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
        },
        "RTOG": {
          "meaning": "ncit:C19778",
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
    "FractionDoseUnitEnum": {
      "permissible_values": {
        "CGE": {
          "meaning": "ncit:C128269",
          "comments": []
        },
        "Gy": {
          "meaning": "ncit:C18063",
          "comments": []
        },
        "cGy": {
          "meaning": "ncit:C64693",
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
        "Bone, NOS": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Cervical Nodes": {
          "meaning": "ncit:C32298",
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
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "NPC": {
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
        "Docetaxel": {
          "meaning": "rxcui:72962",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
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
        "Interferon": {
          "meaning": "ncit:C20493",
          "comments": []
        },
        "Ipilimumab": {
          "meaning": "ncit:C2654",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Paclitaxel": {
          "meaning": "ncit:C1411",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
          "comments": []
        },
        "Sodium Thiosulfate": {
          "meaning": "ncit:C1230",
          "comments": [
            "(gct) ConsortiumNote: CATEGORY == 'Supportive Care Agent'",
            "(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention"
          ]
        },
        "Tetrathiomolybdate (TM)": {
          "meaning": "ncit:C160684",
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
    "TrmTypeEnum": {
      "permissible_values": {
        "Chemotherapy": {
          "meaning": "ncit:C15632",
          "comments": []
        },
        "Immunotherapy": {
          "meaning": "ncit:C15262",
          "comments": []
        },
        "Radiation Therapy": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "TreatmentVolumeEnum": {
      "permissible_values": {
        "PTV High Risk": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: Use for PTV1"
          ]
        },
        "PTV Intermediate Risk": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: Use for PTV2"
          ]
        },
        "PTV Low Risk": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: Use for PTV3"
          ]
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
    "FunctionalMeasurementResultUnitEnum": {
      "permissible_values": {
        "%": {
          "meaning": "",
          "comments": []
        },
        "dB": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SubgroupNameEnum": {
      "permissible_values": {
        "Bleomycin + Doxurubicin + Cisplatin (BAC)": {
          "meaning": "",
          "comments": []
        },
        "Cisplatin + Docetaxel": {
          "meaning": "",
          "comments": []
        },
        "Cisplatin + Gemcitabine": {
          "meaning": "",
          "comments": []
        },
        "Cisplatine + 5FU": {
          "meaning": "",
          "comments": []
        },
        "Docetaxel + Cisplatin + 5FU": {
          "meaning": "",
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
        },
        "RTOG >> Grade 3/Grade 4": {
          "meaning": "",
          "comments": []
        },
        "RTOG >> Grade1/Grade2": {
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
        "Refractory/Progression": {
          "meaning": "ncit:C174991",
          "comments": []
        },
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        }
      }
    },
    "ProcedureExtentEnum": {
      "permissible_values": {
        "Complete Resection": {
          "meaning": "ncit:C175027",
          "comments": []
        },
        "Equivocal": {
          "meaning": "ncit:C178921",
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
    "ResponseCategoryEnum": {
      "permissible_values": {
        "Lymph Node Response": {
          "meaning": "ncit:C159957",
          "comments": []
        },
        "Metastatic Response": {
          "meaning": "",
          "comments": []
        },
        "Overall Response": {
          "meaning": "ncit:C96613",
          "comments": []
        },
        "Primary Site Response": {
          "meaning": "ncit:C200253",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "NOBLE": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TechniqueEnum": {
      "permissible_values": {
        "Brachytherapy": {
          "meaning": "ncit:C15195",
          "comments": []
        },
        "EBRT, 3D Conformal": {
          "meaning": "ncit:C16035",
          "comments": []
        },
        "EBRT, Double Scattering": {
          "meaning": "",
          "comments": [
            "(npc) ConsortiumNote: ENERGY_TYPE = Proton"
          ]
        },
        "EBRT, Intensity-Modulated": {
          "meaning": "",
          "comments": []
        },
        "EBRT, NOS": {
          "meaning": "",
          "comments": []
        },
        "EBRT, Pencil Beam Scanning": {
          "meaning": "ncit:C165502",
          "comments": [
            "(npc) ConsortiumNote: ENERGY_TYPE = Proton"
          ]
        },
        "EBRT, Stereotactic Body": {
          "meaning": "ncit:C118286",
          "comments": [
            "(npc) ConsortiumNote: Stereotactic ablative body radiotherapy"
          ]
        },
        "EBRT, Stereotactic Radiosurgery": {
          "meaning": "ncit:C15358",
          "comments": []
        },
        "EBRT, Tomotherapy": {
          "meaning": "ncit:C62731",
          "comments": [
            "(npc) ConsortiumNote: Helical IMRT"
          ]
        },
        "EBRT, Volume Modulated Arc Therapy": {
          "meaning": "ncit:C104933",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Anemia": {
          "meaning": "ncit:C2869",
          "comments": []
        },
        "CNS Necrosis": {
          "meaning": "ncit:C55367",
          "comments": []
        },
        "Cataract": {
          "meaning": "ncit:C26713",
          "comments": []
        },
        "Cranial Nerve Palsy": {
          "meaning": "ncit:C26941",
          "comments": []
        },
        "Paresthesia": {
          "meaning": "ncit:C143736",
          "comments": []
        },
        "Dental Developmental Abnormality": {
          "meaning": "ncit:C35596",
          "comments": []
        },
        "Dermatitis": {
          "meaning": "ncit:C2983",
          "comments": []
        },
        "Dysphagia": {
          "meaning": "ncit:C57795",
          "comments": []
        },
        "Febrile Neutropenia": {
          "meaning": "ncit:C35665",
          "comments": []
        },
        "Growth Hormone Deficiency": {
          "meaning": "ncit:C112835",
          "comments": []
        },
        "Hearing Impaired": {
          "meaning": "ncit:C143528",
          "comments": []
        },
        "Hematuria": {
          "meaning": "ncit:C3090",
          "comments": []
        },
        "Hoarseness": {
          "meaning": "ncit:C47813",
          "comments": []
        },
        "Hypopituitarism": {
          "meaning": "ncit:C143194",
          "comments": []
        },
        "Hypothyroidism": {
          "meaning": "ncit:C143576",
          "comments": []
        },
        "Mucositis": {
          "meaning": "ncit:C115965",
          "comments": []
        },
        "Neck Fibrosis": {
          "meaning": "ncit:C55368",
          "comments": []
        },
        "Neutropenia": {
          "meaning": "ncit:C80520",
          "comments": []
        },
        "Optic Nerve Disorder": {
          "meaning": "ncit:C143714",
          "comments": []
        },
        "Osteoradionecrosis": {
          "meaning": "ncit:C115459",
          "comments": []
        },
        "Ototoxicity": {
          "meaning": "ncit:C66929",
          "comments": []
        },
        "Proteinuria": {
          "meaning": "ncit:C38012",
          "comments": []
        },
        "Psychiatric Toxicity": {
          "meaning": "ncit:C185648",
          "comments": []
        },
        "Pulmonary Toxicity": {
          "meaning": "ncit:C177374",
          "comments": []
        },
        "Radiation Caries": {
          "meaning": "",
          "comments": []
        },
        "Renal Toxicity": {
          "meaning": "ncit:C115459",
          "comments": []
        },
        "Retinopathy": {
          "meaning": "ncit:C55891",
          "comments": []
        },
        "Spinal Cord Toxicity": {
          "meaning": "ncit:C55369",
          "comments": []
        },
        "Stroke": {
          "meaning": "ncit:C143862",
          "comments": []
        },
        "Thrombocytopenia": {
          "meaning": "ncit:C3408",
          "comments": []
        },
        "Tinnitus": {
          "meaning": "ncit:C146690",
          "comments": []
        },
        "Trismus": {
          "meaning": "ncit:C58404",
          "comments": []
        },
        "Vertigo": {
          "meaning": "ncit:C143935",
          "comments": []
        },
        "Vision Decreased": {
          "meaning": "ncit:C143196",
          "comments": []
        },
        "Weight Loss": {
          "meaning": "ncit:C55339",
          "comments": []
        },
        "Xerostomia": {
          "meaning": "ncit:C26917",
          "comments": []
        }
      }
    },
    "LesionMeasurementUnitEnum": {
      "permissible_values": {
        "cm": {
          "meaning": "",
          "comments": []
        },
        "mm": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SiteClassificationEnum": {
      "permissible_values": {
        "Local Extension": {
          "meaning": "",
          "comments": []
        },
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
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "FunctionTestEnum": {
      "permissible_values": {
        "Audiogram, NOS": {
          "meaning": "ncit:C92448",
          "comments": []
        },
        "Cochlear, OEAP": {
          "meaning": "",
          "comments": []
        },
        "Cochlear, PEAP": {
          "meaning": "",
          "comments": []
        },
        "Vestibular, VHIT": {
          "meaning": "",
          "comments": []
        },
        "Vestibular, cVEMP": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "EBER": {
          "meaning": "ncit:C96602",
          "comments": []
        },
        "EBV DNA": {
          "meaning": "ncit:C166035",
          "comments": []
        },
        "EBV IgG": {
          "meaning": "ncit:C184675",
          "comments": []
        },
        "EBV-PCR": {
          "meaning": "",
          "comments": []
        },
        "EBV-VCA-IgA-IFT": {
          "meaning": "",
          "comments": []
        },
        "Free T3": {
          "meaning": "ncit:C74787",
          "comments": []
        },
        "Free T4": {
          "meaning": "ncit:C74786",
          "comments": []
        },
        "TSH": {
          "meaning": "ncit:C64813",
          "comments": []
        }
      }
    },
    "AdministrationStatusEnum": {
      "permissible_values": {
        "Medication Administered": {
          "meaning": "ncit:C173298",
          "comments": []
        },
        "Medication Not Administered": {
          "meaning": "ncit:C173299",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "ProcedureEnum": {
      "permissible_values": {
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
        "Excisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Incisional Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Lung Resection, NOS": {
          "meaning": "",
          "comments": []
        },
        "Lymph Node Dissection, NOS": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "SmnFieldEnum": {
      "permissible_values": {
        "In XRT Field": {
          "meaning": "ncit:C175045",
          "comments": []
        },
        "Margin of XRT Field": {
          "meaning": "ncit:C185695",
          "comments": []
        },
        "Out of XRT Field": {
          "meaning": "ncit:C175046",
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
        "IU/mL": {
          "meaning": "ncit:C67378",
          "comments": []
        },
        "U/L": {
          "meaning": "ncit:C67456",
          "comments": []
        },
        "U/mL": {
          "meaning": "ncit:C77607",
          "comments": []
        },
        "cp/mL": {
          "meaning": "",
          "comments": []
        },
        "g/dL": {
          "meaning": "ncit:C64783",
          "comments": []
        },
        "mg/dL": {
          "meaning": "ncit:C67015",
          "comments": []
        },
        "mmol/L": {
          "meaning": "ncit:C64387",
          "comments": []
        },
        "pmol/L": {
          "meaning": "ncit:C67434",
          "comments": []
        },
        "ng/mL": {
          "meaning": "ncit:C67306",
          "comments": []
        },
        "ng/dL": {
          "meaning": "ncit:C67326",
          "comments": []
        },
        "ng/L": {
          "meaning": "ncit:C67327",
          "comments": []
        },
        "uIU/mL": {
          "meaning": "ncit:C67405",
          "comments": []
        }
      }
    },
    "RtDoseUnitEnum": {
      "permissible_values": {
        "CGE": {
          "meaning": "ncit:C128269",
          "comments": []
        },
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