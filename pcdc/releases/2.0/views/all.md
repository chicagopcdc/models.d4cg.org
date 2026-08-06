---
layout: default
title: Acute Lymphoblastic Leukemia
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*ALL View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- **Acute Lymphoblastic Leukemia**
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
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The ALL view of the PCDC data model represents consensus data modeling by an international group of pediatric acute lymphoblastic leukemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago. It is based on the collective requirements of its contributors.


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
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |

## OffProtocolTherapyOrStudy

| Slot | Range | Description |
|---|---|---|
| `age_off` | `integer` |  |
| `off_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-offtypeenum')">OffTypeEnum</button> |  |
| `reason_off` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonoffenum')">ReasonOffEnum</button> |  |
| `another_study` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

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
| `subgroup_name` | `SubgroupNameEnum` |  |
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
| `morph_code` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `prior_steroids_week` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `prior_steroids_month` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `bulk_med_mass` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

<div class="domain-heading">Intervention</div>

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `protocol_radiation_therapy` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `protocol_sct` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `sct_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-scttypeenum')">SctTypeEnum</button> |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `donor_relationship` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-donorrelationshipenum')">DonorRelationshipEnum</button> |  |
| `hla_match` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlamatchenum')">HlaMatchEnum</button> |  |
| `number_hla` | `decimal` |  |
| `number_matches` | `decimal` |  |
| `conditioning_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conditioningtypeenum')">ConditioningTypeEnum</button> |  |
| `prior_tbi` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `ae_detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aedetectionmethodenum')">AeDetectionMethodEnum</button> |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_code` | `string` |  |
| `ae_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aecodesystemenum')">AeCodeSystemEnum</button> |  |
| `ae_system_version` | `string` |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `ae_pathogen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aepathogenenum')">AePathogenEnum</button> |  |
| `infection_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-infectionclassificationenum')">InfectionClassificationEnum</button> |  |
| `grade_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gradesystemenum')">GradeSystemEnum</button> |  |
| `grade_system_version` | `string` |  |
| `ae_attribution` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeattributionenum')">AeAttributionEnum</button> |  |
| `ae_intervention_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_intervention` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeinterventionenum')">AeInterventionEnum</button> |  |
| `avn_joint` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-avnjointenum')">AvnJointEnum</button> |  |
| `avn_joint_laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |

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

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `alteration_region` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationregionenum')">AlterationRegionEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein` | `string` |  |
| `copy_number` | `decimal` |  |
| `dna_index_numeric` | `decimal` |  |
| `karyotype_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-karyotypestatusenum')">KaryotypeStatusEnum</button> |  |
| `total_chromosomes` | `decimal` |  |

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
| `bm_morphology` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-bmmorphologyenum')">BmMorphologyEnum</button> |  |

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
<tr><td><code>Avascular Necrosis</code></td><td><code>ncit:C118385</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-aedetectionmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aedetectionmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aedetectionmethodenum')">×</button>
<h3><code>AeDetectionMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bone Scan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X-ray</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Arthroplasty, Hemi/Resurfacing</code></td><td><code>ncit:C178086</code></td><td></td></tr>
<tr><td><code>Arthroplasty, Total</code></td><td><code>ncit:C178087</code></td><td></td></tr>
<tr><td><code>Bone Graft, Free Vascularized</code></td><td><code>ncit:C178088</code></td><td></td></tr>
<tr><td><code>Bone Graft, Nonvascularized</code></td><td><code>ncit:C178089</code></td><td></td></tr>
<tr><td><code>Chondroplasty</code></td><td><code>ncit:C178090</code></td><td></td></tr>
<tr><td><code>Core Decompression</code></td><td><code>ncit:C157826</code></td><td></td></tr>
<tr><td><code>Osteotomy</code></td><td><code>ncit:C51903</code></td><td></td></tr>
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
<tr><td><code>Chromothripsis</code></td><td><code>ncit:C129355</code></td><td></td></tr>
<tr><td><code>Copy Neutral Loss of Heterozygosity</code></td><td><code>ncit:C18016</code></td><td></td></tr>
<tr><td><code>Frameshift</code></td><td><code>ncit:C17354</code></td><td></td></tr>
<tr><td><code>Gain</code></td><td><code>ncit:C189957</code></td><td></td></tr>
<tr><td><code>Gene Fusion</code></td><td><code>ncit:C20195</code></td><td></td></tr>
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
<tr><td><code>E2A/PBX1 t(1;19)</code></td><td><code>ncit:C128654</code></td><td></td></tr>
<tr><td><code>ETV6-RUNX1 t(12;21)(p13;q22)(formerly TEL-AML1)</code></td><td><code>ncit:C13727</code></td><td></td></tr>
<tr><td><code>MLL Rearrangement (Translocation)</code></td><td><code>ncit:C167144</code></td><td></td></tr>
<tr><td><code>Trisomy 10</code></td><td><code>ncit:C81729</code></td><td></td></tr>
<tr><td><code>Trisomy 17</code></td><td><code>ncit:C37865</code></td><td></td></tr>
<tr><td><code>Trisomy 4</code></td><td><code>ncit:C36530</code></td><td></td></tr>
<tr><td><code>iAMP21</code></td><td><code>ncit:C124874</code></td><td></td></tr>
<tr><td><code>t(4;11)(q21;q23) / MLL-MLLT2(AF4)</code></td><td><code>ncit:C36365</code></td><td></td></tr>
<tr><td><code>t(8;14)(q24;q32) or other variant of B-ALL</code></td><td><code>ncit:C36319</code></td><td></td></tr>
<tr><td><code>t(9;22)(q34;q11.2) / ABL/BCR</code></td><td><code>ncit:C13271</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-alterationregionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationregionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationregionenum')">×</button>
<h3><code>AlterationRegionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>3' UTR</code></td><td><code>ncit:C13373</code></td><td></td></tr>
<tr><td><code>5' UTR</code></td><td><code>ncit:C13371</code></td><td></td></tr>
<tr><td><code>Intronic</code></td><td><code>ncit:C45387</code></td><td></td></tr>
<tr><td><code>Promoter</code></td><td><code>ncit:C13297</code></td><td></td></tr>
<tr><td><code>Splice Site</code></td><td><code>ncit:C45574</code></td><td></td></tr>
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
<tr><td><code>Insertion</code></td><td><code>SO:0000667</code></td><td></td></tr>
<tr><td><code>Inversion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rearrangement, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Substitution</code></td><td><code>SO:1000002</code></td><td></td></tr>
<tr><td><code>Translocation</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-avnjointenum" class="enum-modal" onclick="closeEnumModal('enum-modal-avnjointenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-avnjointenum')">×</button>
<h3><code>AvnJointEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ankle (distal tibia, instrinsic ankle bones)</code></td><td><code>ncit:C32078</code></td><td></td></tr>
<tr><td><code>Elbow (distal humerus, proximal radius, proximal ulna)</code></td><td><code>ncit:C32497</code></td><td></td></tr>
<tr><td><code>Heel (calcaneus)</code></td><td><code>ncit:C161381</code></td><td></td></tr>
<tr><td><code>Hip (proximal femur)</code></td><td><code>ncit:C32742</code></td><td></td></tr>
<tr><td><code>Knee (distal femur, proximal tibia)</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Shoulder (proximal humerus)</code></td><td><code>ncit:C25203</code></td><td></td></tr>
<tr><td><code>Wrist (distal radius, distal ulna, instrinsic wrist bones)</code></td><td><code>ncit:C33894</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-bmmorphologyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-bmmorphologyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-bmmorphologyenum')">×</button>
<h3><code>BmMorphologyEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>M1 (Less Than 5% blasts)</code></td><td><code>ncit:C137698</code></td><td></td></tr>
<tr><td><code>M2 (5-25% Blasts)</code></td><td><code>ncit:C146709</code></td><td></td></tr>
<tr><td><code>M3 (Greater Than 25% Blasts)</code></td><td><code>ncit:C140330</code></td><td></td></tr>
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
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Immunotherapy-Related</code></td><td><code>ncit:C168874</code></td><td></td></tr>
<tr><td><code>Infection, NOS</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Multi-Organ Failure</code></td><td><code>ncit:C75568</code></td><td></td></tr>
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
<tr><td><code>ALLIES</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Continuation</code></td><td><code>ncit:C123452</code></td><td></td></tr>
<tr><td><code>Delayed Intensification</code></td><td><code>ncit:C178270</code></td><td></td></tr>
<tr><td><code>Induction</code></td><td><code>ncit:C158876</code></td><td></td></tr>
<tr><td><code>Intensification</code></td><td><code>ncit:C173105</code></td><td></td></tr>
<tr><td><code>Interim Maintenance</code></td><td><code>ncit:C178069</code></td><td></td></tr>
<tr><td><code>Investigational Agent</code></td><td><code>ncit:C49135</code></td><td>(cns) ConsortiumNote: This value should be used for data that may have 'concomitant' listed in the source.</td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
<tr><td><code>Prephase</code></td><td><code>ncit:C168826</code></td><td></td></tr>
<tr><td><code>Stem Cell Transplant Conditioning</code></td><td><code>ncit:C168794</code></td><td></td></tr>
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
<tr><td><code>Acute Leukemia, ambiguous lineage (mixed or biphenotypic)</code></td><td><code>ncit:C7464</code></td><td></td></tr>
<tr><td><code>B-ALL</code></td><td><code>ncit:C8644</code></td><td></td></tr>
<tr><td><code>CNS1</code></td><td><code>ncit:C116833</code></td><td></td></tr>
<tr><td><code>CNS2</code></td><td><code>ncit:C116834</code></td><td></td></tr>
<tr><td><code>CNS2a</code></td><td><code>ncit:C116836</code></td><td></td></tr>
<tr><td><code>CNS2b</code></td><td><code>ncit:C116837</code></td><td></td></tr>
<tr><td><code>CNS2c</code></td><td><code>ncit:C116838</code></td><td></td></tr>
<tr><td><code>CNS3</code></td><td><code>ncit:C116835</code></td><td></td></tr>
<tr><td><code>CNS3a</code></td><td><code>ncit:C116840</code></td><td></td></tr>
<tr><td><code>CNS3b</code></td><td><code>ncit:C116841</code></td><td></td></tr>
<tr><td><code>CNS3c</code></td><td><code>ncit:C116843</code></td><td></td></tr>
<tr><td><code>MPAL</code></td><td><code>ncit:C82179</code></td><td></td></tr>
<tr><td><code>T-ALL</code></td><td><code>ncit:C3183</code></td><td></td></tr>
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
<tr><td><code>ALL</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Refractory</code></td><td><code>ncit:C38014</code></td><td></td></tr>
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
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
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
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-gradesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-gradesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-gradesystemenum')">×</button>
<h3><code>GradeSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Balis Neuropathy Scale</code></td><td><code>ncit:C178081</code></td><td></td></tr>
<tr><td><code>CTCAE</code></td><td><code>ncit:C49704</code></td><td></td></tr>
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

<div id="enum-modal-infectionclassificationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-infectionclassificationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-infectionclassificationenum')">×</button>
<h3><code>InfectionClassificationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clinically Documented</code></td><td><code>ncit:C178092</code></td><td></td></tr>
<tr><td><code>Microbiologically Documented Non-Sterile Site</code></td><td><code>ncit:C178093</code></td><td></td></tr>
<tr><td><code>Microbiologically Documented Sterile Site</code></td><td><code>ncit:C178094</code></td><td></td></tr>
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
<tr><td><code>Abnormal</code></td><td><code>ncit:C168875</code></td><td></td></tr>
<tr><td><code>Normal</code></td><td><code>ncit:C173277</code></td><td></td></tr>
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
<tr><td><code>ANC</code></td><td><code>ncit:C63321</code></td><td></td></tr>
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
<tr><td><code>U/L</code></td><td><code>ncit:C67456</code></td><td></td></tr>
<tr><td><code>count/mm3</code></td><td><code>ncit:C173275</code></td><td></td></tr>
<tr><td><code>g/dL</code></td><td><code>ncit:C64783</code></td><td></td></tr>
<tr><td><code>mg/L</code></td><td><code>ncit:C64572</code></td><td></td></tr>
<tr><td><code>mm/h</code></td><td><code>ncit:C67419</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-nonprotocoltimingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-nonprotocoltimingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-nonprotocoltimingenum')">×</button>
<h3><code>NonProtocolTimingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>After Study Completion</code></td><td><code>ncit:C175040</code></td><td></td></tr>
<tr><td><code>Prior to Study</code></td><td><code>ncit:C175039</code></td><td></td></tr>
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
<tr><td><code>Completion of Follow-Up</code></td><td><code>ncit:C178071</code></td><td></td></tr>
<tr><td><code>Completion of Planned Therapy</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Death</code></td><td><code>ncit:C28554</code></td><td>(os) ConsortiumNote: If multiple reasons for off 'Protocol Therapy' or off 'Study', include one observation per reason.</td></tr>
<tr><td><code>Development of SMN</code></td><td><code>ncit:C4968</code></td><td></td></tr>
<tr><td><code>Failure to Attain Remission</code></td><td><code>ncit:C178072</code></td><td></td></tr>
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
<tr><td><code>Subject Non-Compliance</code></td><td><code>ncit:C91752</code></td><td></td></tr>
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

<div id="enum-modal-rtsiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-rtsiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-rtsiteenum')">×</button>
<h3><code>RtSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cranium</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Testes</code></td><td><code>ncit:C12412</code></td><td></td></tr>
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
<tr><td><code>AALL0232</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL03B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL08B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Egypt57357-StJudeTotal15</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-trmtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-trmtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-trmtypeenum')">×</button>
<h3><code>TrmTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
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
    "all": {
      "name": "all",
      "title": "Acute Lymphoblastic Leukemia",
      "description": "The ALL view of the PCDC data model represents consensus data modeling by an international group of pediatric acute lymphoblastic leukemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago. It is based on the collective requirements of its contributors."
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
        "age_lost_to_follow_up",
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
        "traumatic_tap",
        "bm_morphology"
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
        "genetic_analysis_specimen",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "alteration_region",
        "chromosome",
        "iscn",
        "gene",
        "gene_fusion_partner",
        "hgvs_coding",
        "hgvs_protein",
        "copy_number",
        "dna_index_numeric",
        "karyotype_status",
        "total_chromosomes"
      ],
      "comments": [
        "D4CGNote: One observation/row per genetic alteration",
        "(fa) ConsortiumNote: This table is tiered as Priority."
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
        "morph_code",
        "morph_code_system"
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
        "disease_site",
        "bulk_med_mass"
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
        "prior_steroids_week",
        "prior_steroids_month"
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
    "RadiationTherapy": {
      "slots": [
        "age_at_rt_start",
        "age_at_rt_end",
        "protocol_radiation_therapy",
        "non_protocol_timing",
        "rt_site"
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
        "non_protocol_timing",
        "protocol_sct",
        "sct_type",
        "stem_cell_source",
        "donor_relationship",
        "hla_match",
        "number_hla",
        "number_matches",
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
    "MinimalResidualDisease": {
      "slots": [
        "age_at_mrd_assessment",
        "mrd_method",
        "result_text",
        "result_numeric",
        "mrd_result_unit",
        "sensitivity",
        "mrd_specimen"
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
        "ae_detection_method",
        "adverse_event",
        "ae_code",
        "ae_code_system",
        "ae_system_version",
        "ae_grade",
        "ae_pathogen",
        "infection_classification",
        "grade_system",
        "grade_system_version",
        "ae_attribution",
        "ae_intervention_status",
        "ae_intervention",
        "avn_joint",
        "avn_joint_laterality"
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
    "prior_steroids_month": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "top_code_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "ls"
      }
    },
    "prior_steroids_week": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "dna_index_numeric": {
      "slot_uri": "ncit:C86972",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "gene_fusion_partner": {
      "slot_uri": "ncit:C171253",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
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
    "avn_joint": {
      "slot_uri": "ncit:C178082",
      "range": "AvnJointEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_disease_site_assessment": {
      "slot_uri": "ncit:C174997",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "protocol_radiation_therapy": {
      "slot_uri": "ncit:C175038",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "age_at_genetic_analysis": {
      "slot_uri": "ncit:C168848",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "grade_system_version": {
      "slot_uri": "ncit:C173314",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "alteration_region": {
      "slot_uri": "",
      "range": "AlterationRegionEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "protocol_sct": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "ae_detection_method": {
      "slot_uri": "ncit:C185658",
      "range": "AeDetectionMethodEnum",
      "comments": [],
      "annotations": {}
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
    "copy_number": {
      "slot_uri": "ncit:C49142",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "bm_morphology": {
      "slot_uri": "ncit:C178079",
      "range": "BmMorphologyEnum",
      "comments": [],
      "annotations": {}
    },
    "non_protocol_timing": {
      "slot_uri": "ncit:C175038",
      "range": "NonProtocolTimingEnum",
      "comments": [],
      "annotations": {}
    },
    "bulk_med_mass": {
      "slot_uri": "ncit:C178075",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "total_chromosomes": {
      "slot_uri": "ncit:C177370",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "avn_joint_laterality": {
      "slot_uri": "ncit:C178083",
      "range": "LateralityEnum",
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
    "karyotype_status": {
      "slot_uri": "ncit:C168871",
      "range": "KaryotypeStatusEnum",
      "comments": [],
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
    "prior_tbi": {
      "slot_uri": "ncit:C15350",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb"
      }
    },
    "grade_system": {
      "slot_uri": "ncit:C168872",
      "range": "GradeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "infection_classification": {
      "slot_uri": "ncit:C178091",
      "range": "InfectionClassificationEnum",
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
        "Continuation": {
          "meaning": "ncit:C123452",
          "comments": []
        },
        "Delayed Intensification": {
          "meaning": "ncit:C178270",
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
        "Interim Maintenance": {
          "meaning": "ncit:C178069",
          "comments": []
        },
        "Investigational Agent": {
          "meaning": "ncit:C49135",
          "comments": [
            "(cns) ConsortiumNote: This value should be used for data that may have 'concomitant' listed in the source."
          ]
        },
        "Maintenance": {
          "meaning": "ncit:C15688",
          "comments": [
            "(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses."
          ]
        },
        "Prephase": {
          "meaning": "ncit:C168826",
          "comments": []
        },
        "Stem Cell Transplant Conditioning": {
          "meaning": "ncit:C168794",
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
        "Arthroplasty, Hemi/Resurfacing": {
          "meaning": "ncit:C178086",
          "comments": []
        },
        "Arthroplasty, Total": {
          "meaning": "ncit:C178087",
          "comments": []
        },
        "Bone Graft, Free Vascularized": {
          "meaning": "ncit:C178088",
          "comments": []
        },
        "Bone Graft, Nonvascularized": {
          "meaning": "ncit:C178089",
          "comments": []
        },
        "Chondroplasty": {
          "meaning": "ncit:C178090",
          "comments": []
        },
        "Core Decompression": {
          "meaning": "ncit:C157826",
          "comments": []
        },
        "Osteotomy": {
          "meaning": "ncit:C51903",
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
    "AvnJointEnum": {
      "permissible_values": {
        "Ankle (distal tibia, instrinsic ankle bones)": {
          "meaning": "ncit:C32078",
          "comments": []
        },
        "Elbow (distal humerus, proximal radius, proximal ulna)": {
          "meaning": "ncit:C32497",
          "comments": []
        },
        "Heel (calcaneus)": {
          "meaning": "ncit:C161381",
          "comments": []
        },
        "Hip (proximal femur)": {
          "meaning": "ncit:C32742",
          "comments": []
        },
        "Knee (distal femur, proximal tibia)": {
          "meaning": "ncit:C32898",
          "comments": []
        },
        "Shoulder (proximal humerus)": {
          "meaning": "ncit:C25203",
          "comments": []
        },
        "Wrist (distal radius, distal ulna, instrinsic wrist bones)": {
          "meaning": "ncit:C33894",
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
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Central Nervous System": {
          "meaning": "ncit:C12438",
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
    "AlterationRegionEnum": {
      "permissible_values": {
        "3' UTR": {
          "meaning": "ncit:C13373",
          "comments": []
        },
        "5' UTR": {
          "meaning": "ncit:C13371",
          "comments": []
        },
        "Intronic": {
          "meaning": "ncit:C45387",
          "comments": []
        },
        "Promoter": {
          "meaning": "ncit:C13297",
          "comments": []
        },
        "Splice Site": {
          "meaning": "ncit:C45574",
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
        "Completion of Follow-Up": {
          "meaning": "ncit:C178071",
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
        "Failure to Attain Remission": {
          "meaning": "ncit:C178072",
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
        "Subject Non-Compliance": {
          "meaning": "ncit:C91752",
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
    "InfectionClassificationEnum": {
      "permissible_values": {
        "Clinically Documented": {
          "meaning": "ncit:C178092",
          "comments": []
        },
        "Microbiologically Documented Non-Sterile Site": {
          "meaning": "ncit:C178093",
          "comments": []
        },
        "Microbiologically Documented Sterile Site": {
          "meaning": "ncit:C178094",
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
    "BmMorphologyEnum": {
      "permissible_values": {
        "M1 (Less Than 5% blasts)": {
          "meaning": "ncit:C137698",
          "comments": []
        },
        "M2 (5-25% Blasts)": {
          "meaning": "ncit:C146709",
          "comments": []
        },
        "M3 (Greater Than 25% Blasts)": {
          "meaning": "ncit:C140330",
          "comments": []
        }
      }
    },
    "AlterationEnum": {
      "permissible_values": {
        "E2A/PBX1 t(1;19)": {
          "meaning": "ncit:C128654",
          "comments": []
        },
        "ETV6-RUNX1 t(12;21)(p13;q22)(formerly TEL-AML1)": {
          "meaning": "ncit:C13727",
          "comments": []
        },
        "MLL Rearrangement (Translocation)": {
          "meaning": "ncit:C167144",
          "comments": []
        },
        "Trisomy 10": {
          "meaning": "ncit:C81729",
          "comments": []
        },
        "Trisomy 17": {
          "meaning": "ncit:C37865",
          "comments": []
        },
        "Trisomy 4": {
          "meaning": "ncit:C36530",
          "comments": []
        },
        "iAMP21": {
          "meaning": "ncit:C124874",
          "comments": []
        },
        "t(4;11)(q21;q23) / MLL-MLLT2(AF4)": {
          "meaning": "ncit:C36365",
          "comments": []
        },
        "t(8;14)(q24;q32) or other variant of B-ALL": {
          "meaning": "ncit:C36319",
          "comments": []
        },
        "t(9;22)(q34;q11.2) / ABL/BCR": {
          "meaning": "ncit:C13271",
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
        "Testes": {
          "meaning": "ncit:C12412",
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
        "AALL0232": {
          "meaning": "",
          "comments": []
        },
        "AALL0331": {
          "meaning": "",
          "comments": []
        },
        "AALL03B1": {
          "meaning": "",
          "comments": []
        },
        "AALL0434": {
          "meaning": "",
          "comments": []
        },
        "AALL08B1": {
          "meaning": "",
          "comments": []
        },
        "Egypt57357-StJudeTotal15": {
          "meaning": "",
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
        "Acute Leukemia, ambiguous lineage (mixed or biphenotypic)": {
          "meaning": "ncit:C7464",
          "comments": []
        },
        "B-ALL": {
          "meaning": "ncit:C8644",
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
        "CNS2a": {
          "meaning": "ncit:C116836",
          "comments": []
        },
        "CNS2b": {
          "meaning": "ncit:C116837",
          "comments": []
        },
        "CNS2c": {
          "meaning": "ncit:C116838",
          "comments": []
        },
        "CNS3": {
          "meaning": "ncit:C116835",
          "comments": []
        },
        "CNS3a": {
          "meaning": "ncit:C116840",
          "comments": []
        },
        "CNS3b": {
          "meaning": "ncit:C116841",
          "comments": []
        },
        "CNS3c": {
          "meaning": "ncit:C116843",
          "comments": []
        },
        "MPAL": {
          "meaning": "ncit:C82179",
          "comments": []
        },
        "T-ALL": {
          "meaning": "ncit:C3183",
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
    "MrdResultUnitEnum": {
      "permissible_values": {
        "%": {
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
        }
      }
    },
    "KaryotypeStatusEnum": {
      "permissible_values": {
        "Abnormal": {
          "meaning": "ncit:C168875",
          "comments": []
        },
        "Normal": {
          "meaning": "ncit:C173277",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "ALL": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AeDetectionMethodEnum": {
      "permissible_values": {
        "Bone Scan": {
          "meaning": "",
          "comments": []
        },
        "CT": {
          "meaning": "",
          "comments": []
        },
        "MRI": {
          "meaning": "",
          "comments": []
        },
        "X-ray": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TrmTypeEnum": {
      "permissible_values": {
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
    "NonProtocolTimingEnum": {
      "permissible_values": {
        "After Study Completion": {
          "meaning": "ncit:C175040",
          "comments": []
        },
        "Prior to Study": {
          "meaning": "ncit:C175039",
          "comments": []
        }
      }
    },
    "AlterationEffectEnum": {
      "permissible_values": {
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
        "Refractory": {
          "meaning": "ncit:C38014",
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
        "Trisomy 21": {
          "meaning": "ncit:C43224",
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
        "ALLIES": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Avascular Necrosis": {
          "meaning": "ncit:C118385",
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
    "GradeSystemEnum": {
      "permissible_values": {
        "Balis Neuropathy Scale": {
          "meaning": "ncit:C178081",
          "comments": []
        },
        "CTCAE": {
          "meaning": "ncit:C49704",
          "comments": []
        }
      }
    },
    "GeneticAnalysisSpecimenEnum": {
      "permissible_values": {
        "Blood": {
          "meaning": "ncit:C17610",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "ANC": {
          "meaning": "ncit:C63321",
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
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "%": {
          "meaning": "ncit:C48570",
          "comments": []
        },
        "U/L": {
          "meaning": "ncit:C67456",
          "comments": []
        },
        "count/mm3": {
          "meaning": "ncit:C173275",
          "comments": []
        },
        "g/dL": {
          "meaning": "ncit:C64783",
          "comments": []
        },
        "mg/L": {
          "meaning": "ncit:C64572",
          "comments": []
        },
        "mm/h": {
          "meaning": "ncit:C67419",
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