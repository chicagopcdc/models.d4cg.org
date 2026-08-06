---
layout: default
title: Acute Myeloid Leukemia
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*AML View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- **Acute Myeloid Leukemia**
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
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The AML view of the PCDC data model represents consensus data modeling by an international group of pediatric acute myeloid leukemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Acute Myeloid Leukemia Consortium (INTERACT). It is based on the collective requirements of its contributors.


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
| `age_at_course_anc_500` | `integer` |  |

## ExternalReference

| Slot | Range | Description |
|---|---|---|
| `external_links` | `string` |  |
| `external_resource_icon_path` | `string` |  |
| `external_resource_id` | `string` |  |
| `external_resource_name` | `string` |  |
| `external_subject_id` | `string` |  |
| `external_subject_submitter_id` | `string` |  |
| `external_subject_url` | `string` |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
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
| `enrolled_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
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

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `age_lost_to_follow_up` | `integer` |  |
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
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
| `mpal` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `mlds` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `tam` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `secondary_aml` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `myeloid_sarcoma_involvement` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

<div class="domain-heading">Intervention</div>

## CellularImmunotherapy

| Slot | Range | Description |
|---|---|---|
| `cimt_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-cimttypeenum')">CimtTypeEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `sct_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-scttypeenum')">SctTypeEnum</button> |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `donor_relationship` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-donorrelationshipenum')">DonorRelationshipEnum</button> |  |
| `hla_match` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlamatchenum')">HlaMatchEnum</button> |  |
| `number_hla` | `decimal` |  |
| `number_matches` | `decimal` |  |
| `hla_a_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlaaresultenum')">HlaAResultEnum</button> |  |
| `hla_b_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlabresultenum')">HlaBResultEnum</button> |  |
| `hla_c_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlacresultenum')">HlaCResultEnum</button> |  |
| `hla_drb1_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hladrb1resultenum')">HlaDrb1ResultEnum</button> |  |
| `hla_dq_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hladqresultenum')">HlaDqResultEnum</button> |  |
| `conditioning_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conditioningtypeenum')">ConditioningTypeEnum</button> |  |
| `prior_tbi` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## TransfusionMedicineProcedure

| Slot | Range | Description |
|---|---|---|
| `age_at_tmp_start` | `integer` |  |
| `tmp_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmptypeenum')">TmpTypeEnum</button> |  |
| `tmp_product` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmpproductenum')">TmpProductEnum</button> |  |

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
| `outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-outcomeenum')">OutcomeEnum</button> |  |
| `icu` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `supportive_medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_pathogen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aepathogenenum')">AePathogenEnum</button> |  |
| `ae_pathogen_confirmation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aepathogenconfirmationenum')">AePathogenConfirmationEnum</button> |  |
| `gvhd_acuity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gvhdacuityenum')">GvhdAcuityEnum</button> |  |
| `gvhd_organ` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gvhdorganenum')">GvhdOrganEnum</button> |  |
| `ae_attribution` | `AeAttributionEnum` |  |
| `ae_intervention_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_intervention` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeinterventionenum')">AeInterventionEnum</button> |  |

## MinimalResidualDisease

| Slot | Range | Description |
|---|---|---|
| `age_at_mrd_assessment` | `integer` |  |
| `mrd_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mrdmethodenum')">MrdMethodEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `mrd_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mrdresultunitenum')">MrdResultUnitEnum</button> |  |
| `sensitivity` | `decimal` |  |
| `mrd_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mrdspecimenenum')">MrdSpecimenEnum</button> |  |
| `molecular_markers` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-molecularmarkersenum')">MolecularMarkersEnum</button> |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `bm_pct_blasts_at_response` | `decimal` |  |
| `bm_analysis_method_at_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-bmanalysismethodatresponseenum')">BmAnalysisMethodAtResponseEnum</button> |  |
| `anc_at_response` | `decimal` |  |
| `anc_threshold_at_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `platelet_count_at_response` | `decimal` |  |
| `platelet_threshold_at_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `morph_code` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `morph_code_system_version` | `string` |  |
| `top_code` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |

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
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `hgvs_genomic` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein` | `string` |  |
| `reference_genome` | `string` |  |
| `allelic_ratio` | `decimal` |  |
| `independent_aberrations` | `decimal` |  |
| `cells_in_metaphase` | `decimal` |  |

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
| `traumatic_tap` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## VitalsAndAnthropometrics

| Slot | Range | Description |
|---|---|---|
| `age_at_measurement` | `integer` |  |
| `anthropometric_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementtypeenum')">AnthropometricMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `anthropometric_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">AnthropometricMeasurementResultUnitEnum</button> |  |

<div id="enum-modal-adverseeventenum" class="enum-modal" onclick="closeEnumModal('enum-modal-adverseeventenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-adverseeventenum')">×</button>
<h3><code>AdverseEventEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td></td></tr>
<tr><td><code>Hyperbilirubinemia</code></td><td><code>ncit:C27088</code></td><td></td></tr>
<tr><td><code>Infection</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Left Ventricular Systolic Dysfunction</code></td><td><code>ncit:C64251</code></td><td></td></tr>
<tr><td><code>Multi Organ Failure</code></td><td><code>ncit:C75568</code></td><td></td></tr>
<tr><td><code>Neurotoxicity Syndrome</code></td><td><code>ncit:C27961</code></td><td></td></tr>
<tr><td><code>Sinusoidal Obstruction Syndrome</code></td><td><code>ncit:C26793</code></td><td></td></tr>
<tr><td><code>Typhlitis</code></td><td><code>ncit:C38043</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>European Society for Blood and Marrow Transplantation (EBMT)</code></td><td><code>ncit:C168842</code></td><td></td></tr>
<tr><td><code>ICD</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SNOMED</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-aeinterventionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aeinterventionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aeinterventionenum')">×</button>
<h3><code>AeInterventionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ACE-Inhibitor</code></td><td><code>ncit:C247</code></td><td></td></tr>
<tr><td><code>Heart Transplant</code></td><td><code>ncit:C15246</code></td><td></td></tr>
<tr><td><code>Inotropic Support</code></td><td><code>ncit:C168966</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aepathogenconfirmationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aepathogenconfirmationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aepathogenconfirmationenum')">×</button>
<h3><code>AePathogenConfirmationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Confirmed</code></td><td><code>ncit:C25458</code></td><td></td></tr>
<tr><td><code>Suspected</code></td><td><code>ncit:C71458</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aepathogenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aepathogenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aepathogenenum')">×</button>
<h3><code>AePathogenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bacteria</code></td><td><code>ncit:C14187</code></td><td>(hl) ConsortiumNote: If multiple pathogens involved, include one observation per pathogen.</td></tr>
<tr><td><code>Fungus</code></td><td><code>ncit:C14209</code></td><td></td></tr>
<tr><td><code>Virus</code></td><td><code>ncit:C14283</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-alterationeffectenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationeffectenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationeffectenum')">×</button>
<h3><code>AlterationEffectEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Amplification</code></td><td><code>ncit:C16605</code></td><td></td></tr>
<tr><td><code>Chromothripsis</code></td><td><code>ncit:C129355</code></td><td></td></tr>
<tr><td><code>Copy Neutral Loss of Heterozygosity</code></td><td><code>ncit:C18016</code></td><td></td></tr>
<tr><td><code>Frameshift</code></td><td><code>ncit:C17354</code></td><td></td></tr>
<tr><td><code>Gain</code></td><td><code>ncit:C189957</code></td><td></td></tr>
<tr><td><code>Gene Fusion</code></td><td><code>ncit:C20195</code></td><td></td></tr>
<tr><td><code>Inframe</code></td><td><code>ncit:C62199</code></td><td></td></tr>
<tr><td><code>Isochromosome</code></td><td><code>ncit:C3897</code></td><td></td></tr>
<tr><td><code>Loss</code></td><td><code>ncit:C189958</code></td><td></td></tr>
<tr><td><code>Missense</code></td><td><code>ncit:C18133</code></td><td></td></tr>
<tr><td><code>Monosomy</code></td><td><code>ncit:C3239</code></td><td></td></tr>
<tr><td><code>No Gain/Loss/Amplification</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nonsense</code></td><td><code>ncit:C62198</code></td><td></td></tr>
<tr><td><code>Nullisomy</code></td><td><code>ncit:C198674</code></td><td></td></tr>
<tr><td><code>Splice Acceptor</code></td><td><code>ncit:C45389</code></td><td></td></tr>
<tr><td><code>Splice Donor</code></td><td><code>ncit:C45390</code></td><td></td></tr>
<tr><td><code>Start Lost</code></td><td><code>ncit:C148649</code></td><td></td></tr>
<tr><td><code>Stop Gained</code></td><td><code>ncit:C62198</code></td><td></td></tr>
<tr><td><code>Stop Lost</code></td><td><code>ncit:C148650</code></td><td></td></tr>
<tr><td><code>Synonymous</code></td><td><code>ncit:C20629</code></td><td></td></tr>
<tr><td><code>Trisomy</code></td><td><code>ncit:C3421</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-alterationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationenum')">×</button>
<h3><code>AlterationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>16q Loss</code></td><td><code>ncit:C36515</code></td><td></td></tr>
<tr><td><code>17q Gain</code></td><td><code>ncit:C36484</code></td><td></td></tr>
<tr><td><code>46XX</code></td><td><code>ncit:C120197</code></td><td></td></tr>
<tr><td><code>46XY</code></td><td><code>ncit:C120198</code></td><td></td></tr>
<tr><td><code>47XXX</code></td><td><code>ncit:C129718</code></td><td></td></tr>
<tr><td><code>8q Gain</code></td><td><code>ncit:C36488</code></td><td></td></tr>
<tr><td><code>CEBPA Mutation - Biallelic</code></td><td><code>ncit:C157569</code></td><td></td></tr>
<tr><td><code>CEBPA Mutation - Monoallelic</code></td><td><code>ncit:C168774</code></td><td></td></tr>
<tr><td><code>CEBPA Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Ex17</code></td><td><code>ncit:C116396</code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Ex8</code></td><td><code>ncit:C128660</code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Unspecified</code></td><td><code>ncit:C39712</code></td><td></td></tr>
<tr><td><code>ETV6 Rearranged</code></td><td><code>ncit:C155992</code></td><td></td></tr>
<tr><td><code>ETV6-MN1 Fusion</code></td><td><code>ncit:C99678</code></td><td></td></tr>
<tr><td><code>FLT3 D835N Pathogenic Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FLT3 Internal Tandem Duplication (ITD)</code></td><td><code>ncit:C67494</code></td><td></td></tr>
<tr><td><code>FLT3 Tyrosine Kinase Domain (TKD)</code></td><td><code>ncit:C67495</code></td><td></td></tr>
<tr><td><code>GATA1 Mutation</code></td><td><code>ncit:C82340</code></td><td></td></tr>
<tr><td><code>K-RAS Mutation</code></td><td><code>ncit:C41361</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 11q</code></td><td><code>ncit:C37312</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 1p</code></td><td><code>ncit:C36501</code></td><td></td></tr>
<tr><td><code>MLL Other Partner</code></td><td><code>ncit:C36517</code></td><td></td></tr>
<tr><td><code>MLL Rearrangement (Translocation)</code></td><td><code>ncit:C167144</code></td><td></td></tr>
<tr><td><code>Monosomy 5</code></td><td><code>ncit:C36523</code></td><td></td></tr>
<tr><td><code>Monosomy 7</code></td><td><code>ncit:c36411</code></td><td></td></tr>
<tr><td><code>N-RAS Mutation</code></td><td><code>ncit:C41381</code></td><td></td></tr>
<tr><td><code>NPM1 Mutation</code></td><td><code>ncit:C168774</code></td><td></td></tr>
<tr><td><code>Non-KMT2A MLLT10</code></td><td><code>ncit:C168771</code></td><td></td></tr>
<tr><td><code>PTPN11 Mutation</code></td><td><code>ncit:C82612</code></td><td></td></tr>
<tr><td><code>RUNX1 Mutation</code></td><td><code>ncit:C38362</code></td><td></td></tr>
<tr><td><code>RUNX1-RUNX1T1 Fusion</code></td><td><code>ncit:C99294</code></td><td></td></tr>
<tr><td><code>TCF3-PBX1 Fusion</code></td><td><code>ncit:C99291</code></td><td></td></tr>
<tr><td><code>TP53 Variant</code></td><td><code>ncit:C118396</code></td><td></td></tr>
<tr><td><code>Trisomy 10</code></td><td><code>ncit:C81729</code></td><td></td></tr>
<tr><td><code>Trisomy 21</code></td><td><code>ncit:43224</code></td><td></td></tr>
<tr><td><code>Trisomy 3</code></td><td><code>ncit:C36425</code></td><td></td></tr>
<tr><td><code>Trisomy 4</code></td><td><code>ncit:C36530</code></td><td></td></tr>
<tr><td><code>Trisomy 8</code></td><td><code>ncit:C36396</code></td><td></td></tr>
<tr><td><code>WT1 Mutation</code></td><td><code>ncit:C146726</code></td><td></td></tr>
<tr><td><code>Wild Type</code></td><td><code>ncit:C62195</code></td><td></td></tr>
<tr><td><code>del(13q)</code></td><td><code>ncit:C36497</code></td><td></td></tr>
<tr><td><code>del(13q)(13q 14 - 21)</code></td><td><code>ncit:C168770</code></td><td></td></tr>
<tr><td><code>del(17p)</code></td><td><code>ncit:C36499</code></td><td></td></tr>
<tr><td><code>del(5q)(5q31-q32)</code></td><td><code>ncit:C168769</code></td><td></td></tr>
<tr><td><code>der.12p</code></td><td><code>ncit:C173542</code></td><td></td></tr>
<tr><td><code>iAMP21</code></td><td><code>ncit:C124874</code></td><td></td></tr>
<tr><td><code>inv(16)(p13.3q24.3) / CBFA2T3-GLIS2</code></td><td><code>ncit:C167195</code></td><td></td></tr>
<tr><td><code>inv(16)(p13q22)</code></td><td><code>ncit:C36373</code></td><td></td></tr>
<tr><td><code>inv(3)(q21.3;q26.2)</code></td><td><code>ncit:C36407</code></td><td></td></tr>
<tr><td><code>t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)</code></td><td><code>ncit:C168759</code></td><td></td></tr>
<tr><td><code>t(1;22)(RBM15-MKL1)</code></td><td><code>ncit:C36417</code></td><td></td></tr>
<tr><td><code>t(3;3)(q21;q26.2)</code></td><td><code>ncit:C36406</code></td><td></td></tr>
<tr><td><code>t(3;5)(q25;q34) / NPM1/MLF1</code></td><td><code>ncit:C36415</code></td><td></td></tr>
<tr><td><code>t(4;11)(q21;q23) / MLL-MLLT2(AF4)</code></td><td><code>ncit:C36365</code></td><td></td></tr>
<tr><td><code>t(5;11)(q35;p15) / NSD1/NUP98</code></td><td><code>ncit:C131503</code></td><td></td></tr>
<tr><td><code>t(6;11)(q27;q23) / MLL-MLLT4(AF6)</code></td><td><code>ncit:C36610</code></td><td></td></tr>
<tr><td><code>t(6;9)(p23;q34) DEK/NUP214</code></td><td><code>ncit:C36532</code></td><td></td></tr>
<tr><td><code>t(7;12)(q36;p13) / HLXB9(MNX1)/ETV6(TEL)</code></td><td><code>ncit:C122689</code></td><td></td></tr>
<tr><td><code>t(8;16)MOZ/CBP</code></td><td><code>ncit:C167194</code></td><td></td></tr>
<tr><td><code>t(8;21)(q22;q22) RUNX1/ETO</code></td><td><code></code></td><td></td></tr>
<tr><td><code>t(9;22)(q34;q11.2) / ABL/BCR</code></td><td><code>ncit:C13271</code></td><td></td></tr>
<tr><td><code>t(v;q23.3); KMT2A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>kg/m2</code></td><td><code>ncit:C49671</code></td><td></td></tr>
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
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-bmanalysismethodatresponseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-bmanalysismethodatresponseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-bmanalysismethodatresponseenum')">×</button>
<h3><code>BmAnalysisMethodAtResponseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Flow Cytometry</code></td><td><code>ncit:C16585</code></td><td></td></tr>
<tr><td><code>Morphology</code></td><td><code>ncit:C35867</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Acute Respiratory Distress Syndrome</code></td><td><code>ncit:C3353</code></td><td></td></tr>
<tr><td><code>Bacterial Infection</code></td><td><code>ncit:C2890</code></td><td></td></tr>
<tr><td><code>Cardiac Failure</code></td><td><code>ncit:C50577</code></td><td></td></tr>
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Infection, Not Otherwise Specified</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Multi-Organ Failure</code></td><td><code>ncit:C75568</code></td><td></td></tr>
<tr><td><code>Pulmonary Disease</code></td><td><code>ncit:C3198</code></td><td></td></tr>
<tr><td><code>Sinusoidal Obstruction Syndrome</code></td><td><code>ncit:C26793</code></td><td></td></tr>
<tr><td><code>Viral Infection</code></td><td><code>ncit:C3439</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Post-Treatment Disease Complications</code></td><td><code>ncit:C168877</code></td><td></td></tr>
<tr><td><code>Pre-Treatment Disease Complications</code></td><td><code>ncit:C168876</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-cimttypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-cimttypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-cimttypeenum')">×</button>
<h3><code>CimtTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chimeric Antigen Receptor T-cell Therapy</code></td><td><code>ncit:C126102</code></td><td></td></tr>
<tr><td><code>Donor Lymphocyte Infusion</code></td><td><code>ncit:C16145</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-conditioningtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-conditioningtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-conditioningtypeenum')">×</button>
<h3><code>ConditioningTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Myeloablative</code></td><td><code>ncit:C131679</code></td><td></td></tr>
<tr><td><code>Non-Myeloablative</code></td><td><code>ncit:C62714</code></td><td></td></tr>
<tr><td><code>Reduced Intensity Conditioning/Reduced Toxicity Conditioning</code></td><td><code>ncit:C116471</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>INTERACT</code></td><td><code>ncit:C192762</code></td><td></td></tr>
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
<tr><td><code>Intensification</code></td><td><code>ncit:C173105</code></td><td></td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
<tr><td><code>Palliative Treatment</code></td><td><code>ncit:C15292</code></td><td></td></tr>
<tr><td><code>Prephase</code></td><td><code>ncit:C168826</code></td><td></td></tr>
<tr><td><code>Stem Cell Transplant Conditioning</code></td><td><code>ncit:C168794</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow Results</code></td><td><code>ncit:C190021</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid Results</code></td><td><code>ncit:C168884</code></td><td></td></tr>
<tr><td><code>Clinical Signs or Symptoms</code></td><td><code>ncit:C100104</code></td><td></td></tr>
<tr><td><code>Imaging</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>AML, NOS</code></td><td><code>ncit:C27753</code></td><td></td></tr>
<tr><td><code>CNS1</code></td><td><code>ncit:C116833</code></td><td></td></tr>
<tr><td><code>CNS2</code></td><td><code>ncit:C116834</code></td><td></td></tr>
<tr><td><code>CNS3</code></td><td><code>ncit:C116835</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M0</code></td><td><code>ncit:C8460</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M1</code></td><td><code>ncit:C3249</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M2</code></td><td><code>ncit:C3250</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M3</code></td><td><code>ncit:C3182</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M3 Variant</code></td><td><code>ncit:C27757</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M4</code></td><td><code>ncit:C7463</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M4eo</code></td><td><code>ncit:C9020</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M5</code></td><td><code>ncit:C4861</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M6</code></td><td><code>ncit:C8923</code></td><td></td></tr>
<tr><td><code>FAB &gt;&gt; Version NOS &gt;&gt; M7</code></td><td><code>ncit:C3170</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1</code></td><td><code>ncit:C82427</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with Biallelic Mutations of CEBPA</code></td><td><code>ncit:C129782</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with Maturation</code></td><td><code>ncit:C3250</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with Minimal Differentiation</code></td><td><code>ncit:C8460</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with Mutated NPM1</code></td><td><code>ncit:C82431</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with Myelodysplasia-related Changes</code></td><td><code>ncit:C7600</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11</code></td><td><code>ncit:C9287</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM</code></td><td><code>ncit:C82426</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with t(6;9)(p23;q34.1);DEK-NUP214</code></td><td><code>ncit:C82423</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1</code></td><td><code>ncit:C9288</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3</code></td><td><code>ncit:C82403</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; AML without Maturation</code></td><td><code>ncit:C3249</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; APL with PML-RARA</code></td><td><code>ncit:C7968</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Acute Basophilic Leukemia</code></td><td><code>ncit:C3164</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Acute Megakaryoblastic Leukemia</code></td><td><code>ncit:C3170</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Acute Monoblastic/Monocytic Leukemia</code></td><td><code>ncit:C7318</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Acute Myelomonocytic Leukemia</code></td><td><code>ncit:C7463</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Acute Panmyelosis with Myelofibrosis</code></td><td><code>ncit:C4344</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Myeloid Leukemia Associated with Down Syndrome</code></td><td><code>ncit:C43223</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Myeloid Proliferations Related to Down Syndrome</code></td><td><code>ncit:C82338</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Myeloid Sarcoma</code></td><td><code>ncit:C3520</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Provisional Entity: AML with BCR-ABL1</code></td><td><code>ncit:C129785</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Provisional Entity: AML with Mutated RUNX1</code></td><td><code>ncit:C129786</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Pure Erythroid Leukemia</code></td><td><code>ncit:C7467</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Therapy-Related Myeloid Neoplasms</code></td><td><code>ncit:C27912</code></td><td></td></tr>
<tr><td><code>WHO, Version 4 &gt;&gt; Transient Abnormal Myelopoiesis (TAM)</code></td><td><code>ncit:C82339</code></td><td></td></tr>
<tr><td><code>WHO, Version 5 &gt;&gt; AML with KMT2A Rearrangement</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>AML</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
<tr><td><code>Orbit</code></td><td><code>ncit:C12347</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-donorrelationshipenum" class="enum-modal" onclick="closeEnumModal('enum-modal-donorrelationshipenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-donorrelationshipenum')">×</button>
<h3><code>DonorRelationshipEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Biological Parent</code></td><td><code>ncit:C166114</code></td><td></td></tr>
<tr><td><code>Biological Relative</code></td><td><code>ncit:C71384</code></td><td></td></tr>
<tr><td><code>Biological Sibling</code></td><td><code>ncit:C100809</code></td><td></td></tr>
<tr><td><code>Biologically Unrelated</code></td><td><code>ncit:C130053</code></td><td></td></tr>
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

<div id="enum-modal-fractiondoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fractiondoseunitenum')">×</button>
<h3><code>FractionDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cGy</code></td><td><code>ncit:C64693</code></td><td></td></tr>
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
<tr><td><code>Cytogenetics, FISH</code></td><td><code>ncit:C17563</code></td><td></td></tr>
<tr><td><code>Cytogenetics, Karyotyping</code></td><td><code>ncit:C25215</code></td><td></td></tr>
<tr><td><code>PCR, RT-PCR</code></td><td><code>ncit:C18136</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, NOS</code></td><td><code>ncit:C101293</code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, Capillary Electrophoresis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, Gel Electrophoresis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-gvhdacuityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-gvhdacuityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-gvhdacuityenum')">×</button>
<h3><code>GvhdAcuityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Acute</code></td><td><code>ncit:C4980</code></td><td></td></tr>
<tr><td><code>Chronic</code></td><td><code>ncit:C4981</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-gvhdorganenum" class="enum-modal" onclick="closeEnumModal('enum-modal-gvhdorganenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-gvhdorganenum')">×</button>
<h3><code>GvhdOrganEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Gastrointestinal Tract</code></td><td><code>ncit:C34082</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hlaaresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hlaaresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hlaaresultenum')">×</button>
<h3><code>HlaAResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Both Alleles Matched</code></td><td><code>ncit:C168821</code></td><td></td></tr>
<tr><td><code>One Allele Mismatched</code></td><td><code>ncit:C168819</code></td><td></td></tr>
<tr><td><code>Two Alleles Mismatched</code></td><td><code>ncit:C168820</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hlabresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hlabresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hlabresultenum')">×</button>
<h3><code>HlaBResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Both Alleles Matched</code></td><td><code>ncit:C168821</code></td><td></td></tr>
<tr><td><code>One Allele Mismatched</code></td><td><code>ncit:C168819</code></td><td></td></tr>
<tr><td><code>Two Alleles Mismatched</code></td><td><code>ncit:C168820</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hlacresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hlacresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hlacresultenum')">×</button>
<h3><code>HlaCResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Both Alleles Matched</code></td><td><code>ncit:C168821</code></td><td></td></tr>
<tr><td><code>One Allele Mismatched</code></td><td><code>ncit:C168819</code></td><td></td></tr>
<tr><td><code>Two Alleles Mismatched</code></td><td><code>ncit:C168820</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hladqresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hladqresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hladqresultenum')">×</button>
<h3><code>HlaDqResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Both Alleles Matched</code></td><td><code>ncit:C168821</code></td><td></td></tr>
<tr><td><code>One Allele Mismatched</code></td><td><code>ncit:C168819</code></td><td></td></tr>
<tr><td><code>Two Alleles Mismatched</code></td><td><code>ncit:C168820</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hladrb1resultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hladrb1resultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hladrb1resultenum')">×</button>
<h3><code>HlaDrb1ResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Both Alleles Matched</code></td><td><code>ncit:C168821</code></td><td></td></tr>
<tr><td><code>One Allele Mismatched</code></td><td><code>ncit:C168819</code></td><td></td></tr>
<tr><td><code>Two Alleles Mismatched</code></td><td><code>ncit:C168820</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hlamatchenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hlamatchenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hlamatchenum')">×</button>
<h3><code>HlaMatchEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Match</code></td><td><code>ncit:C129972</code></td><td></td></tr>
<tr><td><code>Non-Match</code></td><td><code>ncit:C126298</code></td><td></td></tr>
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
<tr><td><code>Auer Rods</code></td><td><code>ncit:C74657</code></td><td></td></tr>
<tr><td><code>Blasts</code></td><td><code>ncit:C74605</code></td><td></td></tr>
<tr><td><code>Hemoglobin</code></td><td><code>ncit:C64848</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C51946</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>WBC</code></td><td><code>ncit:C51948</code></td><td></td></tr>
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
<tr><td><code>Flow Cytometry</code></td><td><code>ncit:C16585</code></td><td></td></tr>
<tr><td><code>Morphology Method</code></td><td><code>ncit:C117624</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>%</code></td><td><code>ncit:C48570</code></td><td></td></tr>
<tr><td><code>count/mm3</code></td><td><code>ncit:C173275</code></td><td></td></tr>
<tr><td><code>g/dL</code></td><td><code>ncit:C64783</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
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

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3><code>MedicalHistoryConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Trisomy 21</code></td><td><code>ncit:C43224</code></td><td></td></tr>
<tr><td><code>Trisomy 21 Mosaicism</code></td><td><code>ncit:C142099</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-molecularmarkersenum" class="enum-modal" onclick="closeEnumModal('enum-modal-molecularmarkersenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-molecularmarkersenum')">×</button>
<h3><code>MolecularMarkersEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CEBPA Mutation - Biallelic</code></td><td><code>ncit:C157569</code></td><td></td></tr>
<tr><td><code>CEBPA Mutation - Monoallelic</code></td><td><code>ncit:C168774</code></td><td></td></tr>
<tr><td><code>CEBPA Variant</code></td><td><code>ncit:C38372</code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Ex17</code></td><td><code>ncit:C116396</code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Ex8</code></td><td><code>ncit:C128660</code></td><td></td></tr>
<tr><td><code>CKIT Mutation - Unspecified</code></td><td><code>ncit:C39712</code></td><td></td></tr>
<tr><td><code>FLT3 Internal Tandem Duplication (ITD)</code></td><td><code>ncit:C67494</code></td><td></td></tr>
<tr><td><code>FLT3 Tyrosine Kinase Domain (TKD)</code></td><td><code>ncit:C67495</code></td><td></td></tr>
<tr><td><code>GATA1 Mutation</code></td><td><code>ncit:C82340</code></td><td></td></tr>
<tr><td><code>K-RAS Mutation</code></td><td><code>ncit:C41361</code></td><td></td></tr>
<tr><td><code>MLL Other Partner</code></td><td><code>ncit:C36517</code></td><td></td></tr>
<tr><td><code>MLL Rearrangement (Translocation)</code></td><td><code>ncit:C122623</code></td><td></td></tr>
<tr><td><code>Monosomy 5</code></td><td><code>ncit:C36523</code></td><td></td></tr>
<tr><td><code>Monosomy 7</code></td><td><code>ncit:C36411</code></td><td></td></tr>
<tr><td><code>N-RAS Mutation</code></td><td><code>ncit:C41381</code></td><td></td></tr>
<tr><td><code>NPM1 Mutation</code></td><td><code>ncit:C82429</code></td><td></td></tr>
<tr><td><code>Non-KMT2A MLLT10</code></td><td><code>ncit:C168771</code></td><td></td></tr>
<tr><td><code>PTPN11 Mutation</code></td><td><code>ncit:C82612</code></td><td></td></tr>
<tr><td><code>RUNX1 Mutation</code></td><td><code>ncit:C38362</code></td><td></td></tr>
<tr><td><code>RUNX1-RUNX1T1 Fusion</code></td><td><code>ncit:C99294</code></td><td></td></tr>
<tr><td><code>Trisomy 8</code></td><td><code>ncit:C36396</code></td><td></td></tr>
<tr><td><code>WT1 Mutation</code></td><td><code>ncit:C146726</code></td><td></td></tr>
<tr><td><code>del(13q)</code></td><td><code>ncit:C36497</code></td><td></td></tr>
<tr><td><code>del(13q)(13q 14 - 21)</code></td><td><code>ncit:C168770</code></td><td></td></tr>
<tr><td><code>del(17p)</code></td><td><code>ncit:C36499</code></td><td></td></tr>
<tr><td><code>del(5q)(5q31-q32)</code></td><td><code>ncit:C168769</code></td><td></td></tr>
<tr><td><code>der.12p</code></td><td><code>ncit:C173542</code></td><td></td></tr>
<tr><td><code>inv(16)(p13.3q24.3) / CBFA2T3-GLIS2</code></td><td><code>ncit:C167195</code></td><td></td></tr>
<tr><td><code>inv(16)(p13q22)</code></td><td><code>ncit:C36373</code></td><td></td></tr>
<tr><td><code>inv(3)(q21;q21.2)</code></td><td><code>ncit:C36407</code></td><td></td></tr>
<tr><td><code>t(10;11)(p11.2;q23)</code></td><td><code>ncit:C168758</code></td><td></td></tr>
<tr><td><code>t(10;11)(p12;q23) / MLL-MLLT10(AF10)</code></td><td><code>ncit:C132102</code></td><td></td></tr>
<tr><td><code>t(11;15)(p15;q35) / NUP98/JARID1A</code></td><td><code>ncit:C131505</code></td><td></td></tr>
<tr><td><code>t(11;17)(AF17)</code></td><td><code>ncit:C168760</code></td><td></td></tr>
<tr><td><code>t(11;19)(q23;p13) / (MLL-ENL)/(MLL-ELL)</code></td><td><code>ncit:C168764</code></td><td></td></tr>
<tr><td><code>t(11;19)(q23;p13.1)(MLL-ELL)</code></td><td><code>ncit:C36371</code></td><td></td></tr>
<tr><td><code>t(11;19)(q23;p13.3)(MLL-ENL)</code></td><td><code>ncit:C36372</code></td><td></td></tr>
<tr><td><code>t(15;17)(q24;q21)</code></td><td><code>ncit:C27758</code></td><td></td></tr>
<tr><td><code>t(16;16)(p13.1;q22)</code></td><td><code>ncit:C27759</code></td><td></td></tr>
<tr><td><code>t(16;21)(p11;q22) / FUS/ERG</code></td><td><code>ncit:C36616</code></td><td></td></tr>
<tr><td><code>t(16;21)(q24;q22) / RUNX1-CBFA2T3</code></td><td><code>ncit:C168773</code></td><td></td></tr>
<tr><td><code>t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)</code></td><td><code>ncit:C168759</code></td><td></td></tr>
<tr><td><code>t(1;22)(RBM15-MKL1)</code></td><td><code>ncit:C36417</code></td><td></td></tr>
<tr><td><code>t(2;12)</code></td><td><code>ncit:C173543</code></td><td></td></tr>
<tr><td><code>t(3;12)(q23;p12.3)(ETV6/EVI1)</code></td><td><code>ncit:C168766</code></td><td></td></tr>
<tr><td><code>t(3;3)(q21;q26.2)</code></td><td><code>ncit:C36406</code></td><td></td></tr>
<tr><td><code>t(3;5)(q25;q34) / NPM1/MLF1</code></td><td><code>ncit:C36415</code></td><td></td></tr>
<tr><td><code>t(3;5)(q25;q34)NPM1/MLF2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>t(3;5)(q25;q34)NPM1/MLF3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>t(4;11)(q21;q23) / MLL-MLLT2(AF4)</code></td><td><code>ncit:C36365</code></td><td></td></tr>
<tr><td><code>t(5;11)(q35;p15) / NSD1/NUP98</code></td><td><code>ncit:C131503</code></td><td></td></tr>
<tr><td><code>t(6;11)(q27;q23) / MLL-MLLT4(AF6)</code></td><td><code>ncit:C36610</code></td><td></td></tr>
<tr><td><code>t(6;9)(p23;q34) DEK/NUP214</code></td><td><code>ncit:C36532</code></td><td></td></tr>
<tr><td><code>t(7;12)(q36;p13) / HLXB9(MNX1)/ETV6(TEL)</code></td><td><code>ncit:C122689</code></td><td></td></tr>
<tr><td><code>t(8;16)MOZ/CBP</code></td><td><code>ncit:C167194</code></td><td></td></tr>
<tr><td><code>t(8;21)</code></td><td><code>ncit:C119608</code></td><td></td></tr>
<tr><td><code>t(9;11)(p22;q23) / MLL-MLLT3(AF9)</code></td><td><code>ncit:C36370</code></td><td></td></tr>
<tr><td><code>t(9;22)(q34;q11.2) ABL/BCR</code></td><td><code>ncit:C13271</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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

<div id="enum-modal-mrdmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mrdmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mrdmethodenum')">×</button>
<h3><code>MrdMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Flow Cytometry, Different-From-Normal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flow Cytometry, Leukemia-Associated Immunophenotypes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flow Cytometry, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Molecular Real-time Quantitative PCR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Next Generation Sequencing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-mrdresultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mrdresultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mrdresultunitenum')">×</button>
<h3><code>MrdResultUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>%</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCN</code></td><td><code></code></td><td></td></tr>
<tr><td><code>copies per ngDNA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>copies per uL</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-mrdspecimenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mrdspecimenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mrdspecimenenum')">×</button>
<h3><code>MrdSpecimenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Not Recovered</code></td><td><code>ncit:C49494</code></td><td></td></tr>
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
<tr><td><code>Present</code></td><td><code>ncit:C25566</code></td><td></td></tr>
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
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Withdrawal of Consent</code></td><td><code>ncit:C48271</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow Response</code></td><td><code>ncit:C173307</code></td><td></td></tr>
<tr><td><code>Central Nervous System Response</code></td><td><code>ncit:C168952</code></td><td></td></tr>
<tr><td><code>Myeloid Sarcoma Response</code></td><td><code>ncit:C168965</code></td><td></td></tr>
<tr><td><code>Overall Response</code></td><td><code>ncit:C96613</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Non-Response</code></td><td><code>ncit:C173526</code></td><td></td></tr>
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
<tr><td><code>Cranium</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-scttypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-scttypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-scttypeenum')">×</button>
<h3><code>SctTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Allogeneic</code></td><td><code>ncit:C46089</code></td><td></td></tr>
<tr><td><code>Autologous, NOS</code></td><td><code>ncit:C201465</code></td><td></td></tr>
<tr><td><code>Autologous, Single</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autologous, Tandem</code></td><td><code>ncit:C116466</code></td><td></td></tr>
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
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stemcellsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stemcellsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stemcellsourceenum')">×</button>
<h3><code>StemCellSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Cord Blood</code></td><td><code>ncit:C15640</code></td><td></td></tr>
<tr><td><code>Peripheral Blood</code></td><td><code>ncit:C15430</code></td><td></td></tr>
<tr><td><code>Stem Cell Mixture</code></td><td><code>ncit:C168886</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>AAML03P1</code></td><td><code>ncit:C168936</code></td><td></td></tr>
<tr><td><code>AAML0531</code></td><td><code>ncit:C168937</code></td><td></td></tr>
<tr><td><code>AAML1031</code></td><td><code>ncit:C168938</code></td><td></td></tr>
<tr><td><code>AEIOPAML2002</code></td><td><code>ncit:C168942</code></td><td></td></tr>
<tr><td><code>AIEOPLAM92</code></td><td><code>ncit:C173254</code></td><td></td></tr>
<tr><td><code>AML-BFM Registry2012</code></td><td><code>ncit:C173251</code></td><td></td></tr>
<tr><td><code>AML-BFM Registry2017</code></td><td><code>ncit:C182031</code></td><td></td></tr>
<tr><td><code>AML-BFM1998</code></td><td><code>ncit:C182032</code></td><td></td></tr>
<tr><td><code>AML-BFM2004</code></td><td><code>ncit:C168939</code></td><td></td></tr>
<tr><td><code>AML-BFM2004 Interim</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM2012</code></td><td><code>ncit:C173250</code></td><td></td></tr>
<tr><td><code>AML-BFM2019</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM2020</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM83/87</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM87/93</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM93</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM98</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM98 Interim 2003</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APL</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DBAML01</code></td><td><code>ncit:C168944</code></td><td></td></tr>
<tr><td><code>Egypt57357-AML</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JACLSAML99</code></td><td><code>ncit:C168943</code></td><td></td></tr>
<tr><td><code>JPLSGAML05</code></td><td><code>ncit:C168941</code></td><td></td></tr>
<tr><td><code>ML-DS-2006</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRCAML12</code></td><td><code>ncit:C168945</code></td><td></td></tr>
<tr><td><code>MRCAML15</code></td><td><code>ncit:C173252</code></td><td></td></tr>
<tr><td><code>NOPHOAML1993</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHOAML2004</code></td><td><code>ncit:C168946</code></td><td></td></tr>
<tr><td><code>NOPHOAML2012</code></td><td><code>ncit:C173253</code></td><td></td></tr>
<tr><td><code>PPLLSGAML98</code></td><td><code>ncit:C168947</code></td><td></td></tr>
<tr><td><code>SCFEELAM02</code></td><td><code>ncit:C173255</code></td><td></td></tr>
<tr><td><code>SJCRHAML02</code></td><td><code>ncit:C168940</code></td><td></td></tr>
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
<tr><td><code>AAML0531:Arm A HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm A LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm B HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm B LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031:Arm A HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031:Arm A LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031:Arm B HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031:Arm B LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031:Arm C</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEIOP LAM 2002:ICE-ICE-AVE-HAM- HD-AraC/SR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEIOP LAM 2002:ICE-ICE-AVE-HAM-SCT/HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + AUTO/ALLO SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation + AUTO/ALLO SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + AUTO/ALLO SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation + AUTO/ALLO SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE - AI-haM, AI- HAE - Standard Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE - AI-haM, AI- HAE -Short Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE - HAM- AI- haM-HAE -Short Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE - HAM- AI- haM-HAE -Standard Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE- HAM, AI, haM, Stem Cell Transplantation (High Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE- HAM- AI-haM- HAE-Short Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:ADxE- HAM- AI-haM- HAE-Standard Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- AI-haM, AI- HAE - Standard Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- AI-haM, AI- HAE -Short Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Short Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Standard Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- HAM- AI- haM-HAE -Short Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA- HAM- AI- haM-HAE -Standard Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA-HAM, AI, haM, Stem Cell Transplantation(High Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA-HAM- AI-haM- HAE -Standard Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM 2012:CDxA-HAM- AI-haM- HAE-Short Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM Registry 2012:ADxE- AI-haM-HAE- Standard Maintenance (Standard Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM Registry 2012:ADxE-HAM- AI-haM, HAE- Standard Maintenance (Intermediate Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML BFM Registry 2012:ADxE-HAM- AI-haM, SCT (High Risk Arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 18 Gy (Standard Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI-haM, SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI-haM, SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AML-BFM 2004:AIE-HAM- AI/2CDA-haM, SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Immediate  AM-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Immediate  FLA/Dnx-HA2E+HA3+HA2E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Immediate  FLA/Dnx-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Immediate AM-HA2E+HA3+HA2E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Post Recovery AM-HA2E+HA3+HA2E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Post Recovery AM-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Post Recovery FLA/Dnx-HA2E+HA3+HA2E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DB - AML01:AIET-Post Recovery FLA/Dnx-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JACLS AML99:HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JACLS AML99:IR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JACLS AML99:LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JPLSG AML05:JACLS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:ADE-ADE-MACE-CLASP-MidAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:ADE-ADE-MACE-CLASP-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:ADE-ADE-MACE-MidAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:ADE-ADE-MACE-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:ADE-ADE-off trial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:MAE-MAE-MACE-CLASP-MidAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:MAE-MAE-MACE-CLASP-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:MAE-MAE-MACE-MidAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:MAE-MAE-MACE-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML12:MAE-MAE-Off Trial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-AraC3g-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-AraC3g-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-MACE-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-MACE-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-AraC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + Gemtuzumab Ozagamicin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + No Further Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -ADE-HA3E-FLA (Low Risk)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -ADE-HAM + SCT (High Risk 1)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -ADE-HAM-HA3E+ SCT (High Risk 2)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -ADE-HAM-HA3E-FLA + SCT (High Risk 3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -ADE-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-HA3E-FLA (Low Risk)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-HAM + SCT (High Risk 1)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-HAM-HA3E+ SCT (High Risk 2)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA + SCT (High Risk 3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC -FLAD-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:DEC-ADE-HAM-HA3E-FLA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-HA3E-FLA (Low Risk)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-HAM + SCT (High Risk 1)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-HAM-HA3E + SCT (High Risk 2)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA + SCT (High Risk 3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-ADE-Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD- Off Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD-HA3E-FLA (Low Risk)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD-HAM + SCT (High Risk 1)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD-HAM-HA3E+ SCT (High Risk 2)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA + SCT (High Risk 3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PPLLSG AML-98:HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PPLLSG AML-98:SR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SCFE ELAM02:Induction + Consolidation 1 + Allo HSCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SCFE ELAM02:Induction + Consolidation 1 + Consolidation 2 + Consolidation 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SCFE ELAM02:Induction + Consolidation 1 + Consolidation 2 + Consolidation 3 + IL2 Maintenance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:HDAC-ADE+GO-C1-C2-C3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:HDAC-ADE+GO-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:HDAC-ADE-C1-C2-C3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:HDAC-ADE-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:LDAC-ADE+GO-C1-C2-C3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:LDAC-ADE+GO-SCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:LDAC-ADE-C1-C2-C3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJCRH AML02:LDAC-ADE-SCT</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>EBRT, NOS</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tmpproductenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tmpproductenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tmpproductenum')">×</button>
<h3><code>TmpProductEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Platelets</code></td><td><code>ncit:C133278</code></td><td></td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C133280</code></td><td></td></tr>
<tr><td><code>WBC</code></td><td><code>ncit:C133281</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tmptypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tmptypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tmptypeenum')">×</button>
<h3><code>TmpTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Exchange Transfusion</code></td><td><code>ncit:C173284</code></td><td></td></tr>
<tr><td><code>Simple Transfusion</code></td><td><code>ncit:C173285</code></td><td></td></tr>
<tr><td><code>Therapeutic Apheresis</code></td><td><code>ncit:C173286</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Stem Cell Transplant</code></td><td><code>ncit:C15431</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
    "aml": {
      "name": "aml",
      "title": "Acute Myeloid Leukemia",
      "description": "The AML view of the PCDC data model represents consensus data modeling by an international group of pediatric acute myeloid leukemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Acute Myeloid Leukemia Consortium (INTERACT). It is based on the collective requirements of its contributors."
    }
  },
  "classes": {
    "Subject": {
      "slots": [
        "consortium",
        "disease_group",
        "sex",
        "race",
        "ethnicity"
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
    "ExternalReference": {
      "slots": [
        "external_links",
        "external_resource_icon_path",
        "external_resource_id",
        "external_resource_name",
        "external_subject_id",
        "external_subject_submitter_id",
        "external_subject_url"
      ],
      "comments": [
        "D4CGNote: One observation/row per ___ when instantiated"
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
        "course",
        "age_at_start",
        "year_at_start",
        "age_at_end",
        "age_at_course_anc_500"
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
        "age_lost_to_follow_up",
        "lkss",
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
    "MedicalHistory": {
      "slots": [
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
        "traumatic_tap"
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
        "genetic_analysis_method",
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "chromosome",
        "iscn",
        "gene",
        "gene_fusion_partner",
        "hgvs_genomic",
        "hgvs_coding",
        "hgvs_protein",
        "reference_genome",
        "allelic_ratio",
        "independent_aberrations",
        "cells_in_metaphase"
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
    "Diagnosis": {
      "slots": [
        "age_at_diag_assessment",
        "diagnosis_basis",
        "diagnosis",
        "mpal",
        "mlds",
        "tam",
        "secondary_aml"
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
    "DiseaseSiteAssessment": {
      "slots": [
        "age_at_disease_site_assessment",
        "detection_method",
        "disease_site",
        "myeloid_sarcoma_involvement"
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
    "RadiationTherapy": {
      "slots": [
        "age_at_rt_start",
        "age_at_rt_end",
        "rt_site",
        "laterality",
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
        "sct_type",
        "stem_cell_source",
        "donor_relationship",
        "hla_match",
        "number_hla",
        "number_matches",
        "hla_a_result",
        "hla_b_result",
        "hla_c_result",
        "hla_drb1_result",
        "hla_dq_result",
        "conditioning_type",
        "prior_tbi"
      ],
      "comments": [
        "D4CGNote: One observation/row per SCT when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "TransfusionMedicineProcedure": {
      "slots": [
        "age_at_tmp_start",
        "tmp_type",
        "tmp_product"
      ],
      "comments": [
        "D4CGNote: One observation/row per transfusion when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "CellularImmunotherapy": {
      "slots": [
        "cimt_type"
      ],
      "comments": [
        "D4CGNote: One observation/row per infusion when instantiated."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response_category",
        "response",
        "bm_pct_blasts_at_response",
        "bm_analysis_method_at_response",
        "anc_at_response",
        "anc_threshold_at_response",
        "platelet_count_at_response",
        "platelet_threshold_at_response"
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
    "MinimalResidualDisease": {
      "slots": [
        "age_at_mrd_assessment",
        "mrd_method",
        "result_text",
        "result_numeric",
        "mrd_result_unit",
        "sensitivity",
        "mrd_specimen",
        "molecular_markers"
      ],
      "comments": [
        "D4CGNote: One observation/row per result when instantiated."
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
        "outcome",
        "icu",
        "supportive_medication",
        "ae_pathogen",
        "ae_pathogen_confirmation",
        "gvhd_acuity",
        "gvhd_organ",
        "ae_attribution",
        "ae_intervention_status",
        "ae_intervention"
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
        "morph_code_system",
        "morph_code_system_version",
        "top_code",
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
    "alteration_type": {
      "slot_uri": "ncit:C13202",
      "range": "AlterationTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb,ls"
      }
    },
    "myeloid_sarcoma_involvement": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "external_resource_name": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "allelic_ratio": {
      "slot_uri": "ncit:C173545",
      "range": "decimal",
      "comments": [
        "(aml) ConsortiumNote: Only fill in this variable if the information is available.",
        "(nbl) ConsortiumNote: Only fill in this variable if the information is available."
      ],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "ls"
      }
    },
    "ae_intervention_status": {
      "slot_uri": "ncit:C173318",
      "range": "YesNoEnum",
      "comments": [
        "(aml) ConsortiumNote: changed to general INTERVENTION variable (was previously SOS_INTERVENTION)"
      ],
      "annotations": {
        "tier_mandatory": "hl"
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
    "hla_c_result": {
      "slot_uri": "ncit:C168925",
      "range": "HlaCResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "ae_pathogen": {
      "slot_uri": "ncit:C185665",
      "range": "AePathogenEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple pathogens involved, include one observation per pathogen.",
        "(aml) ConsortiumNote:  Only fill in this variable if ADVERSE_EVENT is 'Infection.'",
        "(all) ConsortiumNote: If multiple pathogens involved, include one observation per pathogen.",
        "(all) ConsortiumNote:  Only fill in this variable if ADVERSE_EVENT is 'Infection.'"
      ],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "age_at_tmp_start": {
      "slot_uri": "ncit:C172697",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "external_resource_icon_path": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "reference_genome": {
      "slot_uri": "ncit:C164815",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,aml",
        "tier_optional": "ls"
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
    "age_at_response": {
      "slot_uri": "ncit:C168856",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "external_links": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "external_resource_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "age_lost_to_follow_up": {
      "slot_uri": "ncit:C172679",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb"
      }
    },
    "ae_intervention": {
      "slot_uri": "ncit:C173319",
      "range": "AeInterventionEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple medications or interventions performed, include one observation per medication or intervention",
        "(aml) ConsortiumNote:  Only fill in this variable if MEDICATION and/or INTERVENTION are marker as 'Yes'",
        "(all) ConsortiumNote: If multiple medications or interventions performed, include one observation per medication or intervention",
        "(all) ConsortiumNote:  Only fill in this variable if MEDICATION and/or INTERVENTION are marker as 'Yes'"
      ],
      "annotations": {}
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
    "hgvs_genomic": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
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
    "hla_match": {
      "slot_uri": "ncit:C169009",
      "range": "HlaMatchEnum",
      "comments": [
        "(aml) ConsortiumNote: the term should be about the HLA matching result (ie match status), not the process - NCI will massage this term's definition (HLA Match status)"
      ],
      "annotations": {
        "tier_priority": "aml,fa"
      }
    },
    "secondary_aml": {
      "slot_uri": "ncit:C25765",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "mrd_result_unit": {
      "slot_uri": "",
      "range": "MrdResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "number_hla": {
      "slot_uri": "ncit:C173301",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
      }
    },
    "hla_dq_result": {
      "slot_uri": "ncit:C168927",
      "range": "HlaDqResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "stem_cell_source": {
      "slot_uri": "ncit:C168870",
      "range": "StemCellSourceEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "aml,fa",
        "tier_optional": "rb"
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
    "alteration_effect": {
      "slot_uri": "ncit:C204195",
      "range": "AlterationEffectEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "mlds": {
      "slot_uri": "ncit:C43223",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "hla_drb1_result": {
      "slot_uri": "ncit:C168926",
      "range": "HlaDrb1ResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
      }
    },
    "hgvs_coding": {
      "slot_uri": "ncit:C198546",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb",
        "tier_optional": "ls"
      }
    },
    "hgvs_protein": {
      "slot_uri": "ncit:C97928",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,aml",
        "tier_optional": "rb,ls"
      }
    },
    "mpal": {
      "slot_uri": "ncit:C82179",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "platelet_threshold_at_response": {
      "slot_uri": "ncit:C168964",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "molecular_markers": {
      "slot_uri": "ncit:C168895",
      "range": "MolecularMarkersEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple MRD markers, include one observation per marker."
      ],
      "annotations": {
        "tier_priority": "aml"
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
    "bm_analysis_method_at_response": {
      "slot_uri": "ncit:C168960",
      "range": "BmAnalysisMethodAtResponseEnum",
      "comments": [
        "(aml) ConsortiumNote: Only fill in the variable if a value is available for BM_PCT_BLASTS_AT_RESPONSE"
      ],
      "annotations": {}
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
    "age_at_sct": {
      "slot_uri": "ncit:C168853",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "sensitivity": {
      "slot_uri": "ncit:C168957",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "conditioning_type": {
      "slot_uri": "ncit:C169014",
      "range": "ConditioningTypeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "aml,fa",
        "tier_optional": "rb"
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
    "bm_pct_blasts_at_response": {
      "slot_uri": "ncit:C168959",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "hla_b_result": {
      "slot_uri": "ncit:C168924",
      "range": "HlaBResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "traumatic_tap": {
      "slot_uri": "ncit:C168879",
      "range": "YesNoEnum",
      "comments": [
        "(aml) ConsortiumNote: Traumatic tap is defined as cerebrospinal fluid with greater than 10 RBC/mm3. Note: Only fill in this variable if LAB_SAMPLE_SOURCE is 'CSF'",
        "(all) ConsortiumNote: Traumatic tap is defined as cerebrospinal fluid with greater than 10 RBC/mm3. Note: Only fill in this variable if LAB_SAMPLE_SOURCE is 'CSF'"
      ],
      "annotations": {}
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
    "age_at_mrd_assessment": {
      "slot_uri": "ncit:C168855",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "biospecimen_media": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "tmp_product": {
      "slot_uri": "ncit:C173287",
      "range": "TmpProductEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "hl"
      }
    },
    "icu": {
      "slot_uri": "ncit:C173316",
      "range": "YesNoEnum",
      "comments": [],
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
    "mrd_specimen": {
      "slot_uri": "ncit:C168958",
      "range": "MrdSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
      }
    },
    "age_at_course_anc_500": {
      "slot_uri": "ncit:C168852",
      "range": "integer",
      "comments": [
        "(aml) ConsortiumNote: This variable is used as a proxy for the age at course end, when appropriate."
      ],
      "annotations": {
        "tier_priority": "aml"
      }
    },
    "external_subject_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "outcome": {
      "slot_uri": "ncit:C49489",
      "range": "OutcomeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "supportive_medication": {
      "slot_uri": "ncit:C173317",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "mrd_method": {
      "slot_uri": "ncit:C168933",
      "range": "MrdMethodEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "anc_threshold_at_response": {
      "slot_uri": "ncit:C168962",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "external_subject_submitter_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "platelet_count_at_response": {
      "slot_uri": "ncit:C168963",
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
    "cells_in_metaphase": {
      "slot_uri": "ncit:C168918",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
      }
    },
    "gvhd_organ": {
      "slot_uri": "ncit:C168883",
      "range": "GvhdOrganEnum",
      "comments": [
        "(aml) ConsortiumNote: If multiple organs involved in GVHD, include one observation per organ.",
        "(aml) ConsortiumNote:  Only fill in this variable if ADVERSE_EVENT is 'GVHD.'"
      ],
      "annotations": {
        "tier_priority": "fa"
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
    "anc_at_response": {
      "slot_uri": "ncit:C168961",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "fraction_dose_unit": {
      "slot_uri": "ncit:C18068",
      "range": "FractionDoseUnitEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,rb"
      }
    },
    "ae_pathogen_confirmation": {
      "slot_uri": "ncit:C168955",
      "range": "AePathogenConfirmationEnum",
      "comments": [
        "(aml) ConsortiumNote: Only fill in this variable if ADVERSE_EVENT is 'Infection' and there is a value filled in for PATHOGEN."
      ],
      "annotations": {}
    },
    "age_at_lab": {
      "slot_uri": "ncit:C172691",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "number_matches": {
      "slot_uri": "ncit:C173302",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "gvhd_acuity": {
      "slot_uri": "ncit:C168861",
      "range": "GvhdAcuityEnum",
      "comments": [
        "(aml) ConsortiumNote: Only fill in this variable if ADVERSE_EVENT is 'GVHD.'"
      ],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "prior_tbi": {
      "slot_uri": "ncit:C15350",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb"
      }
    },
    "tmp_type": {
      "slot_uri": "ncit:C173057",
      "range": "TmpTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "hl"
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
    "external_subject_url": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "donor_relationship": {
      "slot_uri": "ncit:C168869",
      "range": "DonorRelationshipEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "aml"
      }
    },
    "cimt_type": {
      "slot_uri": "ncit:C173057",
      "range": "CimtTypeEnum",
      "comments": [],
      "annotations": {}
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
    "alteration_presence": {
      "slot_uri": "ncit:C173596",
      "range": "PresentAbsentEnum",
      "comments": [
        "(aml) ConsortiumNote: This variable indicates the result of testing for the molecular abnormality listed in alteration."
      ],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "ls"
      }
    },
    "hla_a_result": {
      "slot_uri": "ncit:C168923",
      "range": "HlaAResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml"
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
    "tam": {
      "slot_uri": "ncit:C82339",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "sct_type": {
      "slot_uri": "ncit:C168864",
      "range": "SctTypeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,hl",
        "tier_priority": "aml"
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
        "BMI": {
          "meaning": "ncit:C138901",
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
    "StemCellSourceEnum": {
      "permissible_values": {
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Cord Blood": {
          "meaning": "ncit:C15640",
          "comments": []
        },
        "Peripheral Blood": {
          "meaning": "ncit:C15430",
          "comments": []
        },
        "Stem Cell Mixture": {
          "meaning": "ncit:C168886",
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
    "ResponseEnum": {
      "permissible_values": {
        "System NOS >> Complete Response": {
          "meaning": "ncit:C4870",
          "comments": [
            "(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response."
          ]
        },
        "System NOS >> Non-Response": {
          "meaning": "ncit:C173526",
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
        "Intensification": {
          "meaning": "ncit:C173105",
          "comments": []
        },
        "Maintenance": {
          "meaning": "ncit:C15688",
          "comments": [
            "(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses."
          ]
        },
        "Palliative Treatment": {
          "meaning": "ncit:C15292",
          "comments": []
        },
        "Prephase": {
          "meaning": "ncit:C168826",
          "comments": []
        },
        "Stem Cell Transplant Conditioning": {
          "meaning": "ncit:C168794",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "DonorRelationshipEnum": {
      "permissible_values": {
        "Biological Parent": {
          "meaning": "ncit:C166114",
          "comments": []
        },
        "Biological Relative": {
          "meaning": "ncit:C71384",
          "comments": []
        },
        "Biological Sibling": {
          "meaning": "ncit:C100809",
          "comments": []
        },
        "Biologically Unrelated": {
          "meaning": "ncit:C130053",
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
    "AePathogenEnum": {
      "permissible_values": {
        "Bacteria": {
          "meaning": "ncit:C14187",
          "comments": [
            "(hl) ConsortiumNote: If multiple pathogens involved, include one observation per pathogen."
          ]
        },
        "Fungus": {
          "meaning": "ncit:C14209",
          "comments": []
        },
        "Virus": {
          "meaning": "ncit:C14283",
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
    "AeInterventionEnum": {
      "permissible_values": {
        "ACE-Inhibitor": {
          "meaning": "ncit:C247",
          "comments": []
        },
        "Heart Transplant": {
          "meaning": "ncit:C15246",
          "comments": []
        },
        "Inotropic Support": {
          "meaning": "ncit:C168966",
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
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Bone, NOS": {
          "meaning": "ncit:C12366",
          "comments": []
        },
        "Central Nervous System": {
          "meaning": "ncit:C12438",
          "comments": []
        },
        "Orbit": {
          "meaning": "ncit:C12347",
          "comments": []
        },
        "Skin": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Testis": {
          "meaning": "ncit:C12412",
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
        "Lost to Follow-Up": {
          "meaning": "ncit:C70740",
          "comments": []
        },
        "Physician Decision": {
          "meaning": "ncit:C48250",
          "comments": []
        },
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        },
        "Subject/Guardian Refused Further Treatment": {
          "meaning": "ncit:C168934",
          "comments": []
        },
        "Withdrawal of Consent": {
          "meaning": "ncit:C48271",
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
    "TmpTypeEnum": {
      "permissible_values": {
        "Exchange Transfusion": {
          "meaning": "ncit:C173284",
          "comments": []
        },
        "Simple Transfusion": {
          "meaning": "ncit:C173285",
          "comments": []
        },
        "Therapeutic Apheresis": {
          "meaning": "ncit:C173286",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
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
    "AlterationEnum": {
      "permissible_values": {
        "16q Loss": {
          "meaning": "ncit:C36515",
          "comments": []
        },
        "17q Gain": {
          "meaning": "ncit:C36484",
          "comments": []
        },
        "46XX": {
          "meaning": "ncit:C120197",
          "comments": []
        },
        "46XY": {
          "meaning": "ncit:C120198",
          "comments": []
        },
        "47XXX": {
          "meaning": "ncit:C129718",
          "comments": []
        },
        "8q Gain": {
          "meaning": "ncit:C36488",
          "comments": []
        },
        "CEBPA Mutation - Biallelic": {
          "meaning": "ncit:C157569",
          "comments": []
        },
        "CEBPA Mutation - Monoallelic": {
          "meaning": "ncit:C168774",
          "comments": []
        },
        "CEBPA Variant": {
          "meaning": "",
          "comments": []
        },
        "CKIT Mutation - Ex17": {
          "meaning": "ncit:C116396",
          "comments": []
        },
        "CKIT Mutation - Ex8": {
          "meaning": "ncit:C128660",
          "comments": []
        },
        "CKIT Mutation - Unspecified": {
          "meaning": "ncit:C39712",
          "comments": []
        },
        "ETV6 Rearranged": {
          "meaning": "ncit:C155992",
          "comments": []
        },
        "ETV6-MN1 Fusion": {
          "meaning": "ncit:C99678",
          "comments": []
        },
        "FLT3 D835N Pathogenic Variant": {
          "meaning": "",
          "comments": []
        },
        "FLT3 Internal Tandem Duplication (ITD)": {
          "meaning": "ncit:C67494",
          "comments": []
        },
        "FLT3 Tyrosine Kinase Domain (TKD)": {
          "meaning": "ncit:C67495",
          "comments": []
        },
        "GATA1 Mutation": {
          "meaning": "ncit:C82340",
          "comments": []
        },
        "K-RAS Mutation": {
          "meaning": "ncit:C41361",
          "comments": []
        },
        "Loss of Chromosome 11q": {
          "meaning": "ncit:C37312",
          "comments": []
        },
        "Loss of Chromosome 1p": {
          "meaning": "ncit:C36501",
          "comments": []
        },
        "MLL Other Partner": {
          "meaning": "ncit:C36517",
          "comments": []
        },
        "MLL Rearrangement (Translocation)": {
          "meaning": "ncit:C167144",
          "comments": []
        },
        "Monosomy 5": {
          "meaning": "ncit:C36523",
          "comments": []
        },
        "Monosomy 7": {
          "meaning": "ncit:c36411",
          "comments": []
        },
        "N-RAS Mutation": {
          "meaning": "ncit:C41381",
          "comments": []
        },
        "NPM1 Mutation": {
          "meaning": "ncit:C168774",
          "comments": []
        },
        "Non-KMT2A MLLT10": {
          "meaning": "ncit:C168771",
          "comments": []
        },
        "PTPN11 Mutation": {
          "meaning": "ncit:C82612",
          "comments": []
        },
        "RUNX1 Mutation": {
          "meaning": "ncit:C38362",
          "comments": []
        },
        "RUNX1-RUNX1T1 Fusion": {
          "meaning": "ncit:C99294",
          "comments": []
        },
        "TCF3-PBX1 Fusion": {
          "meaning": "ncit:C99291",
          "comments": []
        },
        "TP53 Variant": {
          "meaning": "ncit:C118396",
          "comments": []
        },
        "Trisomy 10": {
          "meaning": "ncit:C81729",
          "comments": []
        },
        "Trisomy 21": {
          "meaning": "ncit:43224",
          "comments": []
        },
        "Trisomy 3": {
          "meaning": "ncit:C36425",
          "comments": []
        },
        "Trisomy 4": {
          "meaning": "ncit:C36530",
          "comments": []
        },
        "Trisomy 8": {
          "meaning": "ncit:C36396",
          "comments": []
        },
        "WT1 Mutation": {
          "meaning": "ncit:C146726",
          "comments": []
        },
        "Wild Type": {
          "meaning": "ncit:C62195",
          "comments": []
        },
        "del(13q)": {
          "meaning": "ncit:C36497",
          "comments": []
        },
        "del(13q)(13q 14 - 21)": {
          "meaning": "ncit:C168770",
          "comments": []
        },
        "del(17p)": {
          "meaning": "ncit:C36499",
          "comments": []
        },
        "del(5q)(5q31-q32)": {
          "meaning": "ncit:C168769",
          "comments": []
        },
        "der.12p": {
          "meaning": "ncit:C173542",
          "comments": []
        },
        "iAMP21": {
          "meaning": "ncit:C124874",
          "comments": []
        },
        "inv(16)(p13.3q24.3) / CBFA2T3-GLIS2": {
          "meaning": "ncit:C167195",
          "comments": []
        },
        "inv(16)(p13q22)": {
          "meaning": "ncit:C36373",
          "comments": []
        },
        "inv(3)(q21.3;q26.2)": {
          "meaning": "ncit:C36407",
          "comments": []
        },
        "t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)": {
          "meaning": "ncit:C168759",
          "comments": []
        },
        "t(1;22)(RBM15-MKL1)": {
          "meaning": "ncit:C36417",
          "comments": []
        },
        "t(3;3)(q21;q26.2)": {
          "meaning": "ncit:C36406",
          "comments": []
        },
        "t(3;5)(q25;q34) / NPM1/MLF1": {
          "meaning": "ncit:C36415",
          "comments": []
        },
        "t(4;11)(q21;q23) / MLL-MLLT2(AF4)": {
          "meaning": "ncit:C36365",
          "comments": []
        },
        "t(5;11)(q35;p15) / NSD1/NUP98": {
          "meaning": "ncit:C131503",
          "comments": []
        },
        "t(6;11)(q27;q23) / MLL-MLLT4(AF6)": {
          "meaning": "ncit:C36610",
          "comments": []
        },
        "t(6;9)(p23;q34) DEK/NUP214": {
          "meaning": "ncit:C36532",
          "comments": []
        },
        "t(7;12)(q36;p13) / HLXB9(MNX1)/ETV6(TEL)": {
          "meaning": "ncit:C122689",
          "comments": []
        },
        "t(8;16)MOZ/CBP": {
          "meaning": "ncit:C167194",
          "comments": []
        },
        "t(8;21)(q22;q22) RUNX1/ETO": {
          "meaning": "",
          "comments": []
        },
        "t(9;22)(q34;q11.2) / ABL/BCR": {
          "meaning": "ncit:C13271",
          "comments": []
        },
        "t(v;q23.3); KMT2A": {
          "meaning": "",
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
    "RtSiteEnum": {
      "permissible_values": {
        "Cranium": {
          "meaning": "ncit:C12789",
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
        "kg/m2": {
          "meaning": "ncit:C49671",
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
    "BmAnalysisMethodAtResponseEnum": {
      "permissible_values": {
        "Flow Cytometry": {
          "meaning": "ncit:C16585",
          "comments": []
        },
        "Morphology": {
          "meaning": "ncit:C35867",
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
    "MrdMethodEnum": {
      "permissible_values": {
        "Flow Cytometry, Different-From-Normal": {
          "meaning": "",
          "comments": []
        },
        "Flow Cytometry, Leukemia-Associated Immunophenotypes": {
          "meaning": "",
          "comments": []
        },
        "Flow Cytometry, NOS": {
          "meaning": "",
          "comments": []
        },
        "Molecular Real-time Quantitative PCR": {
          "meaning": "",
          "comments": []
        },
        "Next Generation Sequencing": {
          "meaning": "",
          "comments": []
        },
        "Other": {
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
    "CauseOfDeathDetailEnum": {
      "permissible_values": {
        "Acute Respiratory Distress Syndrome": {
          "meaning": "ncit:C3353",
          "comments": []
        },
        "Bacterial Infection": {
          "meaning": "ncit:C2890",
          "comments": []
        },
        "Cardiac Failure": {
          "meaning": "ncit:C50577",
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
        "Infection, Not Otherwise Specified": {
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
        "Sinusoidal Obstruction Syndrome": {
          "meaning": "ncit:C26793",
          "comments": []
        },
        "Viral Infection": {
          "meaning": "ncit:C3439",
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
    "GvhdOrganEnum": {
      "permissible_values": {
        "Gastrointestinal Tract": {
          "meaning": "ncit:C34082",
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
        "Skin": {
          "meaning": "ncit:C12470",
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
    "AePathogenConfirmationEnum": {
      "permissible_values": {
        "Confirmed": {
          "meaning": "ncit:C25458",
          "comments": []
        },
        "Suspected": {
          "meaning": "ncit:C71458",
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
        "Post-Treatment Disease Complications": {
          "meaning": "ncit:C168877",
          "comments": []
        },
        "Pre-Treatment Disease Complications": {
          "meaning": "ncit:C168876",
          "comments": []
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
    "HlaBResultEnum": {
      "permissible_values": {
        "Both Alleles Matched": {
          "meaning": "ncit:C168821",
          "comments": []
        },
        "One Allele Mismatched": {
          "meaning": "ncit:C168819",
          "comments": []
        },
        "Two Alleles Mismatched": {
          "meaning": "ncit:C168820",
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
    "MolecularMarkersEnum": {
      "permissible_values": {
        "CEBPA Mutation - Biallelic": {
          "meaning": "ncit:C157569",
          "comments": []
        },
        "CEBPA Mutation - Monoallelic": {
          "meaning": "ncit:C168774",
          "comments": []
        },
        "CEBPA Variant": {
          "meaning": "ncit:C38372",
          "comments": []
        },
        "CKIT Mutation - Ex17": {
          "meaning": "ncit:C116396",
          "comments": []
        },
        "CKIT Mutation - Ex8": {
          "meaning": "ncit:C128660",
          "comments": []
        },
        "CKIT Mutation - Unspecified": {
          "meaning": "ncit:C39712",
          "comments": []
        },
        "FLT3 Internal Tandem Duplication (ITD)": {
          "meaning": "ncit:C67494",
          "comments": []
        },
        "FLT3 Tyrosine Kinase Domain (TKD)": {
          "meaning": "ncit:C67495",
          "comments": []
        },
        "GATA1 Mutation": {
          "meaning": "ncit:C82340",
          "comments": []
        },
        "K-RAS Mutation": {
          "meaning": "ncit:C41361",
          "comments": []
        },
        "MLL Other Partner": {
          "meaning": "ncit:C36517",
          "comments": []
        },
        "MLL Rearrangement (Translocation)": {
          "meaning": "ncit:C122623",
          "comments": []
        },
        "Monosomy 5": {
          "meaning": "ncit:C36523",
          "comments": []
        },
        "Monosomy 7": {
          "meaning": "ncit:C36411",
          "comments": []
        },
        "N-RAS Mutation": {
          "meaning": "ncit:C41381",
          "comments": []
        },
        "NPM1 Mutation": {
          "meaning": "ncit:C82429",
          "comments": []
        },
        "Non-KMT2A MLLT10": {
          "meaning": "ncit:C168771",
          "comments": []
        },
        "PTPN11 Mutation": {
          "meaning": "ncit:C82612",
          "comments": []
        },
        "RUNX1 Mutation": {
          "meaning": "ncit:C38362",
          "comments": []
        },
        "RUNX1-RUNX1T1 Fusion": {
          "meaning": "ncit:C99294",
          "comments": []
        },
        "Trisomy 8": {
          "meaning": "ncit:C36396",
          "comments": []
        },
        "WT1 Mutation": {
          "meaning": "ncit:C146726",
          "comments": []
        },
        "del(13q)": {
          "meaning": "ncit:C36497",
          "comments": []
        },
        "del(13q)(13q 14 - 21)": {
          "meaning": "ncit:C168770",
          "comments": []
        },
        "del(17p)": {
          "meaning": "ncit:C36499",
          "comments": []
        },
        "del(5q)(5q31-q32)": {
          "meaning": "ncit:C168769",
          "comments": []
        },
        "der.12p": {
          "meaning": "ncit:C173542",
          "comments": []
        },
        "inv(16)(p13.3q24.3) / CBFA2T3-GLIS2": {
          "meaning": "ncit:C167195",
          "comments": []
        },
        "inv(16)(p13q22)": {
          "meaning": "ncit:C36373",
          "comments": []
        },
        "inv(3)(q21;q21.2)": {
          "meaning": "ncit:C36407",
          "comments": []
        },
        "t(10;11)(p11.2;q23)": {
          "meaning": "ncit:C168758",
          "comments": []
        },
        "t(10;11)(p12;q23) / MLL-MLLT10(AF10)": {
          "meaning": "ncit:C132102",
          "comments": []
        },
        "t(11;15)(p15;q35) / NUP98/JARID1A": {
          "meaning": "ncit:C131505",
          "comments": []
        },
        "t(11;17)(AF17)": {
          "meaning": "ncit:C168760",
          "comments": []
        },
        "t(11;19)(q23;p13) / (MLL-ENL)/(MLL-ELL)": {
          "meaning": "ncit:C168764",
          "comments": []
        },
        "t(11;19)(q23;p13.1)(MLL-ELL)": {
          "meaning": "ncit:C36371",
          "comments": []
        },
        "t(11;19)(q23;p13.3)(MLL-ENL)": {
          "meaning": "ncit:C36372",
          "comments": []
        },
        "t(15;17)(q24;q21)": {
          "meaning": "ncit:C27758",
          "comments": []
        },
        "t(16;16)(p13.1;q22)": {
          "meaning": "ncit:C27759",
          "comments": []
        },
        "t(16;21)(p11;q22) / FUS/ERG": {
          "meaning": "ncit:C36616",
          "comments": []
        },
        "t(16;21)(q24;q22) / RUNX1-CBFA2T3": {
          "meaning": "ncit:C168773",
          "comments": []
        },
        "t(1;11)(q21;q23) / MLL-MLLT11(AF1Q)": {
          "meaning": "ncit:C168759",
          "comments": []
        },
        "t(1;22)(RBM15-MKL1)": {
          "meaning": "ncit:C36417",
          "comments": []
        },
        "t(2;12)": {
          "meaning": "ncit:C173543",
          "comments": []
        },
        "t(3;12)(q23;p12.3)(ETV6/EVI1)": {
          "meaning": "ncit:C168766",
          "comments": []
        },
        "t(3;3)(q21;q26.2)": {
          "meaning": "ncit:C36406",
          "comments": []
        },
        "t(3;5)(q25;q34) / NPM1/MLF1": {
          "meaning": "ncit:C36415",
          "comments": []
        },
        "t(3;5)(q25;q34)NPM1/MLF2": {
          "meaning": "",
          "comments": []
        },
        "t(3;5)(q25;q34)NPM1/MLF3": {
          "meaning": "",
          "comments": []
        },
        "t(4;11)(q21;q23) / MLL-MLLT2(AF4)": {
          "meaning": "ncit:C36365",
          "comments": []
        },
        "t(5;11)(q35;p15) / NSD1/NUP98": {
          "meaning": "ncit:C131503",
          "comments": []
        },
        "t(6;11)(q27;q23) / MLL-MLLT4(AF6)": {
          "meaning": "ncit:C36610",
          "comments": []
        },
        "t(6;9)(p23;q34) DEK/NUP214": {
          "meaning": "ncit:C36532",
          "comments": []
        },
        "t(7;12)(q36;p13) / HLXB9(MNX1)/ETV6(TEL)": {
          "meaning": "ncit:C122689",
          "comments": []
        },
        "t(8;16)MOZ/CBP": {
          "meaning": "ncit:C167194",
          "comments": []
        },
        "t(8;21)": {
          "meaning": "ncit:C119608",
          "comments": []
        },
        "t(9;11)(p22;q23) / MLL-MLLT3(AF9)": {
          "meaning": "ncit:C36370",
          "comments": []
        },
        "t(9;22)(q34;q11.2) ABL/BCR": {
          "meaning": "ncit:C13271",
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
        "AAML03P1": {
          "meaning": "ncit:C168936",
          "comments": []
        },
        "AAML0531": {
          "meaning": "ncit:C168937",
          "comments": []
        },
        "AAML1031": {
          "meaning": "ncit:C168938",
          "comments": []
        },
        "AEIOPAML2002": {
          "meaning": "ncit:C168942",
          "comments": []
        },
        "AIEOPLAM92": {
          "meaning": "ncit:C173254",
          "comments": []
        },
        "AML-BFM Registry2012": {
          "meaning": "ncit:C173251",
          "comments": []
        },
        "AML-BFM Registry2017": {
          "meaning": "ncit:C182031",
          "comments": []
        },
        "AML-BFM1998": {
          "meaning": "ncit:C182032",
          "comments": []
        },
        "AML-BFM2004": {
          "meaning": "ncit:C168939",
          "comments": []
        },
        "AML-BFM2004 Interim": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM2012": {
          "meaning": "ncit:C173250",
          "comments": []
        },
        "AML-BFM2019": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM2020": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM83/87": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM87/93": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM93": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM98": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM98 Interim 2003": {
          "meaning": "",
          "comments": []
        },
        "APL": {
          "meaning": "",
          "comments": []
        },
        "DBAML01": {
          "meaning": "ncit:C168944",
          "comments": []
        },
        "Egypt57357-AML": {
          "meaning": "",
          "comments": []
        },
        "JACLSAML99": {
          "meaning": "ncit:C168943",
          "comments": []
        },
        "JPLSGAML05": {
          "meaning": "ncit:C168941",
          "comments": []
        },
        "ML-DS-2006": {
          "meaning": "",
          "comments": []
        },
        "MRCAML12": {
          "meaning": "ncit:C168945",
          "comments": []
        },
        "MRCAML15": {
          "meaning": "ncit:C173252",
          "comments": []
        },
        "NOPHOAML1993": {
          "meaning": "",
          "comments": []
        },
        "NOPHOAML2004": {
          "meaning": "ncit:C168946",
          "comments": []
        },
        "NOPHOAML2012": {
          "meaning": "ncit:C173253",
          "comments": []
        },
        "PPLLSGAML98": {
          "meaning": "ncit:C168947",
          "comments": []
        },
        "SCFEELAM02": {
          "meaning": "ncit:C173255",
          "comments": []
        },
        "SJCRHAML02": {
          "meaning": "ncit:C168940",
          "comments": []
        }
      }
    },
    "MrdSpecimenEnum": {
      "permissible_values": {
        "Blood": {
          "meaning": "ncit:C17610",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "ncit:C12431",
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
    "TopCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "AML, NOS": {
          "meaning": "ncit:C27753",
          "comments": []
        },
        "CNS1": {
          "meaning": "ncit:C116833",
          "comments": []
        },
        "CNS2": {
          "meaning": "ncit:C116834",
          "comments": []
        },
        "CNS3": {
          "meaning": "ncit:C116835",
          "comments": []
        },
        "FAB >> Version NOS >> M0": {
          "meaning": "ncit:C8460",
          "comments": []
        },
        "FAB >> Version NOS >> M1": {
          "meaning": "ncit:C3249",
          "comments": []
        },
        "FAB >> Version NOS >> M2": {
          "meaning": "ncit:C3250",
          "comments": []
        },
        "FAB >> Version NOS >> M3": {
          "meaning": "ncit:C3182",
          "comments": []
        },
        "FAB >> Version NOS >> M3 Variant": {
          "meaning": "ncit:C27757",
          "comments": []
        },
        "FAB >> Version NOS >> M4": {
          "meaning": "ncit:C7463",
          "comments": []
        },
        "FAB >> Version NOS >> M4eo": {
          "meaning": "ncit:C9020",
          "comments": []
        },
        "FAB >> Version NOS >> M5": {
          "meaning": "ncit:C4861",
          "comments": []
        },
        "FAB >> Version NOS >> M6": {
          "meaning": "ncit:C8923",
          "comments": []
        },
        "FAB >> Version NOS >> M7": {
          "meaning": "ncit:C3170",
          "comments": []
        },
        "WHO, Version 4 >> AML (megakaryoblastic) with t(1;22)(p13.3;q13.3); RBM15-MKL1": {
          "meaning": "ncit:C82427",
          "comments": []
        },
        "WHO, Version 4 >> AML with Biallelic Mutations of CEBPA": {
          "meaning": "ncit:C129782",
          "comments": []
        },
        "WHO, Version 4 >> AML with Maturation": {
          "meaning": "ncit:C3250",
          "comments": []
        },
        "WHO, Version 4 >> AML with Minimal Differentiation": {
          "meaning": "ncit:C8460",
          "comments": []
        },
        "WHO, Version 4 >> AML with Mutated NPM1": {
          "meaning": "ncit:C82431",
          "comments": []
        },
        "WHO, Version 4 >> AML with Myelodysplasia-related Changes": {
          "meaning": "ncit:C7600",
          "comments": []
        },
        "WHO, Version 4 >> AML with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11": {
          "meaning": "ncit:C9287",
          "comments": []
        },
        "WHO, Version 4 >> AML with inv(3)(q21.3q26.2) or t(3;3)(q21.3;q26.2); GATA2, MECOM": {
          "meaning": "ncit:C82426",
          "comments": []
        },
        "WHO, Version 4 >> AML with t(6;9)(p23;q34.1);DEK-NUP214": {
          "meaning": "ncit:C82423",
          "comments": []
        },
        "WHO, Version 4 >> AML with t(8;21)(q22;q22.1); RUNX1-RUNX1T1": {
          "meaning": "ncit:C9288",
          "comments": []
        },
        "WHO, Version 4 >> AML with t(9;11)(p21.3;q23.3); KMT2A-MLLT3": {
          "meaning": "ncit:C82403",
          "comments": []
        },
        "WHO, Version 4 >> AML without Maturation": {
          "meaning": "ncit:C3249",
          "comments": []
        },
        "WHO, Version 4 >> APL with PML-RARA": {
          "meaning": "ncit:C7968",
          "comments": []
        },
        "WHO, Version 4 >> Acute Basophilic Leukemia": {
          "meaning": "ncit:C3164",
          "comments": []
        },
        "WHO, Version 4 >> Acute Megakaryoblastic Leukemia": {
          "meaning": "ncit:C3170",
          "comments": []
        },
        "WHO, Version 4 >> Acute Monoblastic/Monocytic Leukemia": {
          "meaning": "ncit:C7318",
          "comments": []
        },
        "WHO, Version 4 >> Acute Myelomonocytic Leukemia": {
          "meaning": "ncit:C7463",
          "comments": []
        },
        "WHO, Version 4 >> Acute Panmyelosis with Myelofibrosis": {
          "meaning": "ncit:C4344",
          "comments": []
        },
        "WHO, Version 4 >> Myeloid Leukemia Associated with Down Syndrome": {
          "meaning": "ncit:C43223",
          "comments": []
        },
        "WHO, Version 4 >> Myeloid Proliferations Related to Down Syndrome": {
          "meaning": "ncit:C82338",
          "comments": []
        },
        "WHO, Version 4 >> Myeloid Sarcoma": {
          "meaning": "ncit:C3520",
          "comments": []
        },
        "WHO, Version 4 >> Provisional Entity: AML with BCR-ABL1": {
          "meaning": "ncit:C129785",
          "comments": []
        },
        "WHO, Version 4 >> Provisional Entity: AML with Mutated RUNX1": {
          "meaning": "ncit:C129786",
          "comments": []
        },
        "WHO, Version 4 >> Pure Erythroid Leukemia": {
          "meaning": "ncit:C7467",
          "comments": []
        },
        "WHO, Version 4 >> Therapy-Related Myeloid Neoplasms": {
          "meaning": "ncit:C27912",
          "comments": []
        },
        "WHO, Version 4 >> Transient Abnormal Myelopoiesis (TAM)": {
          "meaning": "ncit:C82339",
          "comments": []
        },
        "WHO, Version 5 >> AML with KMT2A Rearrangement": {
          "meaning": "",
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
    "HlaDqResultEnum": {
      "permissible_values": {
        "Both Alleles Matched": {
          "meaning": "ncit:C168821",
          "comments": []
        },
        "One Allele Mismatched": {
          "meaning": "ncit:C168819",
          "comments": []
        },
        "Two Alleles Mismatched": {
          "meaning": "ncit:C168820",
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
        "Bone Marrow Results": {
          "meaning": "ncit:C190021",
          "comments": []
        },
        "Cerebrospinal Fluid Results": {
          "meaning": "ncit:C168884",
          "comments": []
        },
        "Clinical Signs or Symptoms": {
          "meaning": "ncit:C100104",
          "comments": []
        },
        "Imaging": {
          "meaning": "ncit:C17369",
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
    "PresentAbsentEnum": {
      "permissible_values": {
        "Absent": {
          "meaning": "ncit:C25567",
          "comments": []
        },
        "Present": {
          "meaning": "ncit:C25566",
          "comments": []
        }
      }
    },
    "MrdResultUnitEnum": {
      "permissible_values": {
        "%": {
          "meaning": "",
          "comments": []
        },
        "NCN": {
          "meaning": "",
          "comments": []
        },
        "copies per ngDNA": {
          "meaning": "",
          "comments": []
        },
        "copies per uL": {
          "meaning": "",
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
        "European Society for Blood and Marrow Transplantation (EBMT)": {
          "meaning": "ncit:C168842",
          "comments": []
        },
        "ICD": {
          "meaning": "",
          "comments": []
        },
        "SNOMED": {
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
    "ConditioningTypeEnum": {
      "permissible_values": {
        "Myeloablative": {
          "meaning": "ncit:C131679",
          "comments": []
        },
        "Non-Myeloablative": {
          "meaning": "ncit:C62714",
          "comments": []
        },
        "Reduced Intensity Conditioning/Reduced Toxicity Conditioning": {
          "meaning": "ncit:C116471",
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
    "FractionDoseUnitEnum": {
      "permissible_values": {
        "cGy": {
          "meaning": "ncit:C64693",
          "comments": []
        }
      }
    },
    "HlaMatchEnum": {
      "permissible_values": {
        "Match": {
          "meaning": "ncit:C129972",
          "comments": []
        },
        "Non-Match": {
          "meaning": "ncit:C126298",
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
        "Cytogenetics, FISH": {
          "meaning": "ncit:C17563",
          "comments": []
        },
        "Cytogenetics, Karyotyping": {
          "meaning": "ncit:C25215",
          "comments": []
        },
        "PCR, RT-PCR": {
          "meaning": "ncit:C18136",
          "comments": []
        },
        "Sequencing, NGS, NOS": {
          "meaning": "ncit:C101293",
          "comments": []
        },
        "Sequencing, Sanger, Capillary Electrophoresis": {
          "meaning": "",
          "comments": []
        },
        "Sequencing, Sanger, Gel Electrophoresis": {
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
    "GvhdAcuityEnum": {
      "permissible_values": {
        "Acute": {
          "meaning": "ncit:C4980",
          "comments": []
        },
        "Chronic": {
          "meaning": "ncit:C4981",
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
        "AML": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "HlaAResultEnum": {
      "permissible_values": {
        "Both Alleles Matched": {
          "meaning": "ncit:C168821",
          "comments": []
        },
        "One Allele Mismatched": {
          "meaning": "ncit:C168819",
          "comments": []
        },
        "Two Alleles Mismatched": {
          "meaning": "ncit:C168820",
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
        "Stem Cell Transplant": {
          "meaning": "ncit:C15431",
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
    "HlaCResultEnum": {
      "permissible_values": {
        "Both Alleles Matched": {
          "meaning": "ncit:C168821",
          "comments": []
        },
        "One Allele Mismatched": {
          "meaning": "ncit:C168819",
          "comments": []
        },
        "Two Alleles Mismatched": {
          "meaning": "ncit:C168820",
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
        "Flow Cytometry": {
          "meaning": "ncit:C16585",
          "comments": []
        },
        "Morphology Method": {
          "meaning": "ncit:C117624",
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
        "Not Recovered": {
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
    "AlterationEffectEnum": {
      "permissible_values": {
        "Amplification": {
          "meaning": "ncit:C16605",
          "comments": []
        },
        "Chromothripsis": {
          "meaning": "ncit:C129355",
          "comments": []
        },
        "Copy Neutral Loss of Heterozygosity": {
          "meaning": "ncit:C18016",
          "comments": []
        },
        "Frameshift": {
          "meaning": "ncit:C17354",
          "comments": []
        },
        "Gain": {
          "meaning": "ncit:C189957",
          "comments": []
        },
        "Gene Fusion": {
          "meaning": "ncit:C20195",
          "comments": []
        },
        "Inframe": {
          "meaning": "ncit:C62199",
          "comments": []
        },
        "Isochromosome": {
          "meaning": "ncit:C3897",
          "comments": []
        },
        "Loss": {
          "meaning": "ncit:C189958",
          "comments": []
        },
        "Missense": {
          "meaning": "ncit:C18133",
          "comments": []
        },
        "Monosomy": {
          "meaning": "ncit:C3239",
          "comments": []
        },
        "No Gain/Loss/Amplification": {
          "meaning": "",
          "comments": []
        },
        "Nonsense": {
          "meaning": "ncit:C62198",
          "comments": []
        },
        "Nullisomy": {
          "meaning": "ncit:C198674",
          "comments": []
        },
        "Splice Acceptor": {
          "meaning": "ncit:C45389",
          "comments": []
        },
        "Splice Donor": {
          "meaning": "ncit:C45390",
          "comments": []
        },
        "Start Lost": {
          "meaning": "ncit:C148649",
          "comments": []
        },
        "Stop Gained": {
          "meaning": "ncit:C62198",
          "comments": []
        },
        "Stop Lost": {
          "meaning": "ncit:C148650",
          "comments": []
        },
        "Synonymous": {
          "meaning": "ncit:C20629",
          "comments": []
        },
        "Trisomy": {
          "meaning": "ncit:C3421",
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
    "SubgroupNameEnum": {
      "permissible_values": {
        "AAML0531:Arm A HR": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm A LR": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm B HR": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm B LR": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:HR": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:LR": {
          "meaning": "",
          "comments": []
        },
        "AAML1031:Arm A HR": {
          "meaning": "",
          "comments": []
        },
        "AAML1031:Arm A LR": {
          "meaning": "",
          "comments": []
        },
        "AAML1031:Arm B HR": {
          "meaning": "",
          "comments": []
        },
        "AAML1031:Arm B LR": {
          "meaning": "",
          "comments": []
        },
        "AAML1031:Arm C": {
          "meaning": "",
          "comments": []
        },
        "AEIOP LAM 2002:ICE-ICE-AVE-HAM- HD-AraC/SR": {
          "meaning": "",
          "comments": []
        },
        "AEIOP LAM 2002:ICE-ICE-AVE-HAM-SCT/HR": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + AUTO/ALLO SCT": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(2+3+7) + Consolidation + AUTO/ALLO SCT": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + AUTO/ALLO SCT": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation": {
          "meaning": "",
          "comments": []
        },
        "AIEOP LAM 92:ICE(3+5+10) + ICE(3+5+10) + Consolidation + AUTO/ALLO SCT": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE - AI-haM, AI- HAE - Standard Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE - AI-haM, AI- HAE -Short Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE - HAM- AI- haM-HAE -Short Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE - HAM- AI- haM-HAE -Standard Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE- HAM, AI, haM, Stem Cell Transplantation (High Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE- HAM- AI-haM- HAE-Short Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:ADxE- HAM- AI-haM- HAE-Standard Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- AI-haM, AI- HAE - Standard Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- AI-haM, AI- HAE -Short Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Short Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Standard Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- HAM Sorafenib, AI Sorafenib, haM Sorafenib, Stem Cell Transplantation (High Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- HAM- AI- haM-HAE -Short Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA- HAM- AI- haM-HAE -Standard Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA-HAM, AI, haM, Stem Cell Transplantation(High Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA-HAM- AI-haM- HAE -Standard Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM 2012:CDxA-HAM- AI-haM- HAE-Short Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM Registry 2012:ADxE- AI-haM-HAE- Standard Maintenance (Standard Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM Registry 2012:ADxE-HAM- AI-haM, HAE- Standard Maintenance (Intermediate Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML BFM Registry 2012:ADxE-HAM- AI-haM, SCT (High Risk Arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE- AI-haM-HAE- Standard maintenance, 18 Gy (Standard Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI-haM, SCT": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:ADxE-HAM- AI/2CDA-haM, SCT": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 12 Gy (Standard Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE- AI-haM-HAE- Standard maintenance, 18 Gy(Standard Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI-haM, SCT": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 12 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, HAE- Standard maintenance, 18 Gy (High Risk arm)": {
          "meaning": "",
          "comments": []
        },
        "AML-BFM 2004:AIE-HAM- AI/2CDA-haM, SCT": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Immediate  AM-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Immediate  FLA/Dnx-HA2E+HA3+HA2E": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Immediate  FLA/Dnx-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Immediate AM-HA2E+HA3+HA2E": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Post Recovery AM-HA2E+HA3+HA2E": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Post Recovery AM-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Post Recovery FLA/Dnx-HA2E+HA3+HA2E": {
          "meaning": "",
          "comments": []
        },
        "DB - AML01:AIET-Post Recovery FLA/Dnx-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "JACLS AML99:HR": {
          "meaning": "",
          "comments": []
        },
        "JACLS AML99:IR": {
          "meaning": "",
          "comments": []
        },
        "JACLS AML99:LR": {
          "meaning": "",
          "comments": []
        },
        "JPLSG AML05:JACLS": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:ADE-ADE-MACE-CLASP-MidAC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:ADE-ADE-MACE-CLASP-SCT": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:ADE-ADE-MACE-MidAC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:ADE-ADE-MACE-SCT": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:ADE-ADE-off trial": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:MAE-MAE-MACE-CLASP-MidAC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:MAE-MAE-MACE-CLASP-SCT": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:MAE-MAE-MACE-MidAC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:MAE-MAE-MACE-SCT": {
          "meaning": "",
          "comments": []
        },
        "MRC AML12:MAE-MAE-Off Trial": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-AraC3g-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-AraC3g-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-AraC3g/Mytolarg-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-MACE-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-MACE-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE-ADE-MACE/Mytolarg-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-AraC3g-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-AraC3g/Mytolarg-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-MACE-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:ADE/Mytolarg-ADE-MACE/Mytolarg-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-AraC3g-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-AraC3g/Mytolarg-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-MACE-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda-FLAGIda-MACE/Mytolarg-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-AraC3g/Mytolarg-AraC3g-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-AraC": {
          "meaning": "",
          "comments": []
        },
        "MRC AML15:FLAGIda/Mytolarg-FLAGIda-MACE/Mytolarg-MidAC-No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + Gemtuzumab Ozagamicin": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2004:AIET-AM-HA1M-HA2E-HA3-HA2E + No Further Therapy": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -ADE-HA3E-FLA (Low Risk)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -ADE-HAM + SCT (High Risk 1)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -ADE-HAM-HA3E+ SCT (High Risk 2)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -ADE-HAM-HA3E-FLA + SCT (High Risk 3)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -ADE-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-HA3E-FLA (Low Risk)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-HAM + SCT (High Risk 1)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-HAM-HA3E+ SCT (High Risk 2)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-HAM-HA3E-FLA + SCT (High Risk 3)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC -FLAD-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:DEC-ADE-HAM-HA3E-FLA": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-HA3E-FLA (Low Risk)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-HAM + SCT (High Risk 1)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-HAM-HA3E + SCT (High Risk 2)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-HAM-HA3E-FLA + SCT (High Risk 3)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-ADE-Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD- Off Protocol": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD-HA3E-FLA (Low Risk)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD-HAM + SCT (High Risk 1)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD-HAM-HA3E+ SCT (High Risk 2)": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA": {
          "meaning": "",
          "comments": []
        },
        "NOPHO AML 2012:MEC-FLAD-HAM-HA3E-FLA + SCT (High Risk 3)": {
          "meaning": "",
          "comments": []
        },
        "PPLLSG AML-98:HR": {
          "meaning": "",
          "comments": []
        },
        "PPLLSG AML-98:SR": {
          "meaning": "",
          "comments": []
        },
        "SCFE ELAM02:Induction + Consolidation 1 + Allo HSCT": {
          "meaning": "",
          "comments": []
        },
        "SCFE ELAM02:Induction + Consolidation 1 + Consolidation 2 + Consolidation 3": {
          "meaning": "",
          "comments": []
        },
        "SCFE ELAM02:Induction + Consolidation 1 + Consolidation 2 + Consolidation 3 + IL2 Maintenance": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:HDAC-ADE+GO-C1-C2-C3": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:HDAC-ADE+GO-SCT": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:HDAC-ADE-C1-C2-C3": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:HDAC-ADE-SCT": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:LDAC-ADE+GO-C1-C2-C3": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:LDAC-ADE+GO-SCT": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:LDAC-ADE-C1-C2-C3": {
          "meaning": "",
          "comments": []
        },
        "SJCRH AML02:LDAC-ADE-SCT": {
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
    "ResponseCategoryEnum": {
      "permissible_values": {
        "Bone Marrow Response": {
          "meaning": "ncit:C173307",
          "comments": []
        },
        "Central Nervous System Response": {
          "meaning": "ncit:C168952",
          "comments": []
        },
        "Myeloid Sarcoma Response": {
          "meaning": "ncit:C168965",
          "comments": []
        },
        "Overall Response": {
          "meaning": "ncit:C96613",
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
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Trisomy 21": {
          "meaning": "ncit:C43224",
          "comments": []
        },
        "Trisomy 21 Mosaicism": {
          "meaning": "ncit:C142099",
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
        "INTERACT": {
          "meaning": "ncit:C192762",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Graft Versus Host Disease": {
          "meaning": "ncit:C3063",
          "comments": []
        },
        "Hemorrhage": {
          "meaning": "ncit:C26791",
          "comments": []
        },
        "Hyperbilirubinemia": {
          "meaning": "ncit:C27088",
          "comments": []
        },
        "Infection": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Left Ventricular Systolic Dysfunction": {
          "meaning": "ncit:C64251",
          "comments": []
        },
        "Multi Organ Failure": {
          "meaning": "ncit:C75568",
          "comments": []
        },
        "Neurotoxicity Syndrome": {
          "meaning": "ncit:C27961",
          "comments": []
        },
        "Sinusoidal Obstruction Syndrome": {
          "meaning": "ncit:C26793",
          "comments": []
        },
        "Typhlitis": {
          "meaning": "ncit:C38043",
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
    "TechniqueEnum": {
      "permissible_values": {
        "EBRT, NOS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "Auer Rods": {
          "meaning": "ncit:C74657",
          "comments": []
        },
        "Blasts": {
          "meaning": "ncit:C74605",
          "comments": []
        },
        "Hemoglobin": {
          "meaning": "ncit:C64848",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "RBC": {
          "meaning": "ncit:C51946",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "WBC": {
          "meaning": "ncit:C51948",
          "comments": []
        }
      }
    },
    "TmpProductEnum": {
      "permissible_values": {
        "Platelets": {
          "meaning": "ncit:C133278",
          "comments": []
        },
        "RBC": {
          "meaning": "ncit:C133280",
          "comments": []
        },
        "WBC": {
          "meaning": "ncit:C133281",
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
    "SctTypeEnum": {
      "permissible_values": {
        "Allogeneic": {
          "meaning": "ncit:C46089",
          "comments": []
        },
        "Autologous, NOS": {
          "meaning": "ncit:C201465",
          "comments": []
        },
        "Autologous, Single": {
          "meaning": "",
          "comments": []
        },
        "Autologous, Tandem": {
          "meaning": "ncit:C116466",
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
    "CimtTypeEnum": {
      "permissible_values": {
        "Chimeric Antigen Receptor T-cell Therapy": {
          "meaning": "ncit:C126102",
          "comments": []
        },
        "Donor Lymphocyte Infusion": {
          "meaning": "ncit:C16145",
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
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "%": {
          "meaning": "ncit:C48570",
          "comments": []
        },
        "count/mm3": {
          "meaning": "ncit:C173275",
          "comments": []
        },
        "g/dL": {
          "meaning": "ncit:C64783",
          "comments": []
        }
      }
    },
    "HlaDrb1ResultEnum": {
      "permissible_values": {
        "Both Alleles Matched": {
          "meaning": "ncit:C168821",
          "comments": []
        },
        "One Allele Mismatched": {
          "meaning": "ncit:C168819",
          "comments": []
        },
        "Two Alleles Mismatched": {
          "meaning": "ncit:C168820",
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