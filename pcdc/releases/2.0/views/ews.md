---
layout: default
title: Ewing Sarcoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*EWS View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- [Central Nervous System Tumors](cns)
- **Ewing Sarcoma**
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

The EWS view of the PCDC data model represents consensus data modeling by an international group of pediatric Ewing sarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors.


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

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_characteristic` | `integer` |  |
| `performance_score` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-performancescoreenum')">PerformanceScoreEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `tumor_size` | `TumorSizeEnum` |  |
| `multiplicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-multiplicityenum')">MultiplicityEnum</button> |  |
| `tumor_volume` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorvolumeenum')">TumorVolumeEnum</button> |  |
| `estimated_volume` | `decimal` |  |
| `fracture` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ipsilateral_nodules` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `joint_involvement` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
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
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
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
| `transposition_organ` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-transpositionorganenum')">TranspositionOrganEnum</button> |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `age_at_sct_harvest` | `integer` |  |
| `age_at_recovery` | `integer` |  |
| `sct_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-scttypeenum')">SctTypeEnum</button> |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `recovery_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-recoverytypeenum')">RecoveryTypeEnum</button> |  |
| `recovery_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `cd34_collected` | `decimal` |  |
| `cd34_transplant` | `decimal` |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure_performed` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |
| `procedure_extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureextentenum')">ProcedureExtentEnum</button> |  |
| `distance_from_margin` | `decimal` |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `ae_code` | `string` |  |
| `ae_code_system` | `AeCodeSystemEnum` |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `grade_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gradesystemenum')">GradeSystemEnum</button> |  |
| `grade_system_version` | `string` |  |
| `ae_attribution` | `AeAttributionEnum` |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsesystemenum')">ResponseSystemEnum</button> |  |
| `response_system_version` | `string` |  |
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
| `morph_code_system_version` | `string` |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |
| `smn_field` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smnfieldenum')">SmnFieldEnum</button> |  |

<div class="domain-heading">Testing</div>

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein` | `string` |  |
| `copy_number` | `decimal` |  |

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
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |
| `threshold_level` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-thresholdlevelenum')">ThresholdLevelEnum</button> |  |
| `threshold_high` | `decimal` |  |
| `threshold_low` | `decimal` |  |

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
<tr><td><code>12q Gain</code></td><td><code>ncit:C36441</code></td><td></td></tr>
<tr><td><code>16q Loss</code></td><td><code>ncit:C36515</code></td><td></td></tr>
<tr><td><code>1q Gain</code></td><td><code>ncit:C36482</code></td><td></td></tr>
<tr><td><code>8q Gain</code></td><td><code>ncit:C36488</code></td><td></td></tr>
<tr><td><code>BCOR Rearranged</code></td><td><code>ncit:C174461</code></td><td></td></tr>
<tr><td><code>BCOR-MAML3</code></td><td><code>ncit:C174487</code></td><td></td></tr>
<tr><td><code>CCNB3-BCOR</code></td><td><code>ncit:C139666</code></td><td></td></tr>
<tr><td><code>CDKN2A</code></td><td><code>ncit:C128817</code></td><td></td></tr>
<tr><td><code>CIC Rearranged</code></td><td><code>ncit:C165668</code></td><td></td></tr>
<tr><td><code>CIC-DUX4</code></td><td><code>ncit:C139663</code></td><td></td></tr>
<tr><td><code>CIC-DUX4L10</code></td><td><code>ncit:C174463</code></td><td></td></tr>
<tr><td><code>EWSR1 Rearranged</code></td><td><code>ncit:C165667</code></td><td></td></tr>
<tr><td><code>EWSR1-ATF1</code></td><td><code>ncit:C99216</code></td><td></td></tr>
<tr><td><code>EWSR1-CREB1</code></td><td><code>ncit:C99249</code></td><td></td></tr>
<tr><td><code>EWSR1-DDIT3</code></td><td><code>ncit:C99200</code></td><td></td></tr>
<tr><td><code>EWSR1-ERG</code></td><td><code>ncit:C99211</code></td><td></td></tr>
<tr><td><code>EWSR1-ETV1</code></td><td><code>ncit:C99259</code></td><td></td></tr>
<tr><td><code>EWSR1-ETV4</code></td><td><code>ncit:C99262</code></td><td></td></tr>
<tr><td><code>EWSR1-FEV</code></td><td><code>ncit:C99226</code></td><td></td></tr>
<tr><td><code>EWSR1-FLI1</code></td><td><code>ncit:C99202</code></td><td></td></tr>
<tr><td><code>EWSR1-KLF17</code></td><td><code>ncit:C174474</code></td><td></td></tr>
<tr><td><code>EWSR1-NR4A3</code></td><td><code>ncit:C99252</code></td><td></td></tr>
<tr><td><code>EWSR1-PBX1</code></td><td><code>ncit:C139668</code></td><td></td></tr>
<tr><td><code>EWSR1-POU5F1</code></td><td><code>ncit:C99256</code></td><td></td></tr>
<tr><td><code>EWSR1-WT1</code></td><td><code>ncit:C99213</code></td><td></td></tr>
<tr><td><code>EWSR1-ZNF444</code></td><td><code>ncit:C139731</code></td><td></td></tr>
<tr><td><code>FUS Rearranged</code></td><td><code>ncit:C174462</code></td><td></td></tr>
<tr><td><code>FUS Translocation Present</code></td><td><code>ncit:C25626</code></td><td></td></tr>
<tr><td><code>FUS-DDIT3</code></td><td><code>ncit:C99279</code></td><td></td></tr>
<tr><td><code>FUS-ERG</code></td><td><code>ncit:C99281</code></td><td></td></tr>
<tr><td><code>FUS-FEV</code></td><td><code>ncit:C174466</code></td><td></td></tr>
<tr><td><code>FUS-KLF17</code></td><td><code>ncit:C174473</code></td><td></td></tr>
<tr><td><code>STAG2</code></td><td><code>ncit:C153513</code></td><td></td></tr>
<tr><td><code>TAF15-NR4A3</code></td><td><code>ncit:C99501</code></td><td></td></tr>
<tr><td><code>TP53</code></td><td><code>ncit:C118396</code></td><td></td></tr>
<tr><td><code>ZC3H7B-BCOR</code></td><td><code>ncit:C174491</code></td><td></td></tr>
<tr><td><code>inv(X)(p11.4;p11.22)</code></td><td><code>ncit:C174489</code></td><td></td></tr>
<tr><td><code>t(10;19)(q26;q13)</code></td><td><code>ncit:C120223</code></td><td></td></tr>
<tr><td><code>t(11;22)</code></td><td><code>ncit:C128642</code></td><td></td></tr>
<tr><td><code>t(11;22)(p13;q12)</code></td><td><code>ncit:C36375</code></td><td></td></tr>
<tr><td><code>t(11;22)(q24;q12)</code></td><td><code>ncit:C27214</code></td><td></td></tr>
<tr><td><code>t(12;16)(q13;p11)</code></td><td><code>ncit:C36317</code></td><td></td></tr>
<tr><td><code>t(12;22)(q13.12;q12)</code></td><td><code>ncit:C174478</code></td><td></td></tr>
<tr><td><code>t(12;22)(q13.3;q12)</code></td><td><code>ncit:C174479</code></td><td></td></tr>
<tr><td><code>t(16;21)(p11;q22)</code></td><td><code>ncit:C36616</code></td><td></td></tr>
<tr><td><code>t(17;22)(q21;q12)</code></td><td><code>ncit:C36369</code></td><td></td></tr>
<tr><td><code>t(19;22)(q13;q12)</code></td><td><code>ncit:C174480</code></td><td></td></tr>
<tr><td><code>t(1;16)(p34;p11)</code></td><td><code>ncit:C174475</code></td><td></td></tr>
<tr><td><code>t(1;22)(p34;q12)</code></td><td><code>ncit:C174476</code></td><td></td></tr>
<tr><td><code>t(1;22)(q23;q12)</code></td><td><code>ncit:C174477</code></td><td></td></tr>
<tr><td><code>t(21;22)(q22;q12)</code></td><td><code>ncit:C36367</code></td><td></td></tr>
<tr><td><code>t(2;16)(q35;p11)</code></td><td><code>ncit:C174465</code></td><td></td></tr>
<tr><td><code>t(2;22)(q33;q12)</code></td><td><code>ncit:C37249</code></td><td></td></tr>
<tr><td><code>t(2;22)(q34;q12)</code></td><td><code>ncit:C174481</code></td><td></td></tr>
<tr><td><code>t(4;19)(q25;q13)</code></td><td><code>ncit:C174482</code></td><td></td></tr>
<tr><td><code>t(4;19)(q35;q13)</code></td><td><code>ncit:C120222</code></td><td></td></tr>
<tr><td><code>t(6;22)(p21;q12)</code></td><td><code>ncit:C174483</code></td><td></td></tr>
<tr><td><code>t(7;22)(p22;q12)</code></td><td><code>ncit:C36368</code></td><td></td></tr>
<tr><td><code>t(9;17)(q22;q11)</code></td><td><code>ncit:C36393</code></td><td></td></tr>
<tr><td><code>t(9;22)(q22;q12)</code></td><td><code>ncit:C174484</code></td><td></td></tr>
<tr><td><code>t(X;22)(p11;q13)</code></td><td><code>ncit:C174495</code></td><td></td></tr>
<tr><td><code>t(X;4)(p11;q31)</code></td><td><code>ncit:C174490</code></td><td></td></tr>
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

<div id="enum-modal-detectionmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-detectionmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-detectionmethodenum')">×</button>
<h3><code>DetectionMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bone Marrow Aspirates</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow Trephine Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Imaging, NOS</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Technetium Bone Scan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X-Ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
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
<tr><td><code>Ewing Sarcoma</code></td><td><code>icdo:9260/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Large Cell Ewing Tumor</code></td><td><code>ncit:C174456</code></td><td></td></tr>
<tr><td><code>Neuro-differentiated Ewing Tumor</code></td><td><code>ncit:C9341</code></td><td></td></tr>
<tr><td><code>Round Blue Cell Tumor/Sarcoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Undifferentiated Ewing Tumor</code></td><td><code>ncit:C121799</code></td><td></td></tr>
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
<tr><td><code>EWS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
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
<tr><td><code>Electron</code></td><td><code>ncit:C40428</code></td><td></td></tr>
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
<tr><td><code>Cytogenetics, NOS</code></td><td><code>ncit:C16487</code></td><td></td></tr>
<tr><td><code>Genotyping, NOS</code></td><td><code>ncit:C45447</code></td><td></td></tr>
<tr><td><code>PCR, NOS</code></td><td><code>ncit:C17003</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, NOS</code></td><td><code>ncit:C101293</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>CTCAE</code></td><td><code>ncit:C49704</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-laboratorytestenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorytestenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorytestenum')">×</button>
<h3><code>LaboratoryTestEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alkaline Phophatase</code></td><td><code>ncit:C64432</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Cytology Malignant Cells</code></td><td><code>ncit:C74660</code></td><td></td></tr>
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
<tr><td><code>mm/h</code></td><td><code>ncit:C67419</code></td><td></td></tr>
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
<tr><td><code>Pleural Fluid</code></td><td><code>ncit:C77613</code></td><td></td></tr>
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
<tr><td><code>CD45</code></td><td><code>ncit:C17282</code></td><td></td></tr>
<tr><td><code>CD99/Cell Surface Antigen O13/Cell Surface Antigen HBA-71</code></td><td><code>ncit:C102941</code></td><td></td></tr>
<tr><td><code>Desmin</code></td><td><code>ncit:C96450</code></td><td></td></tr>
<tr><td><code>FLI-1</code></td><td><code>ncit:C18566</code></td><td></td></tr>
<tr><td><code>NSE</code></td><td><code>ncit:C62216</code></td><td></td></tr>
<tr><td><code>PAS</code></td><td><code>ncit:C23019</code></td><td></td></tr>
<tr><td><code>S100</code></td><td><code>ncit:C29924</code></td><td></td></tr>
<tr><td><code>Vimentin</code></td><td><code>ncit:C48797</code></td><td></td></tr>
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
<tr><td><code>Breast and Ovarian Cancer</code></td><td><code>ncit:C8493</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia</code></td><td><code>ncit:C62505</code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Lynch Syndrome</code></td><td><code>ncit:C8494</code></td><td></td></tr>
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
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Cabozantinib</code></td><td><code>ncit:C52200</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Celecoxib</code></td><td><code>ncit:C1728</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Dactinomycin</code></td><td><code>rxcui:3100</code></td><td></td></tr>
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>GCSF</code></td><td><code>ncit:C26078</code></td><td></td></tr>
<tr><td><code>GMCSF</code></td><td><code>ncit:C20545</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Irinotecan</code></td><td><code>ncit:C62040</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Pazopanib</code></td><td><code>rxcui:714438</code></td><td></td></tr>
<tr><td><code>Plerixafor</code></td><td><code>ncit:C1777</code></td><td></td></tr>
<tr><td><code>Regorafenib</code></td><td><code>ncit:C78204</code></td><td></td></tr>
<tr><td><code>Temozolomide</code></td><td><code>rxcui:37776</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Trabectedin</code></td><td><code>ncit:C1691</code></td><td></td></tr>
<tr><td><code>Treosulfan</code></td><td><code>rxcui:38508</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>Zoledronic Acid</code></td><td><code>ncit:C1699</code></td><td></td></tr>
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
<tr><td><code>Multiple Tumors</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Single Tumor</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-performancescoreenum" class="enum-modal" onclick="closeEnumModal('enum-modal-performancescoreenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-performancescoreenum')">×</button>
<h3><code>PerformanceScoreEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>GPOH &gt;&gt; 1</code></td><td><code>ncit:C174992</code></td><td></td></tr>
<tr><td><code>GPOH &gt;&gt; 2</code></td><td><code>ncit:C174993</code></td><td></td></tr>
<tr><td><code>GPOH &gt;&gt; 3</code></td><td><code>ncit:C174994</code></td><td></td></tr>
<tr><td><code>GPOH &gt;&gt; 4</code></td><td><code>ncit:C174995</code></td><td></td></tr>
<tr><td><code>GPOH &gt;&gt; 5</code></td><td><code>ncit:C174996</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 0</code></td><td><code>ncit:C105720</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 10</code></td><td><code>ncit:C105718</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 100</code></td><td><code>ncit:C105707</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 20</code></td><td><code>ncit:C105716</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 30</code></td><td><code>ncit:C105715</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 40</code></td><td><code>ncit:C105714</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 50</code></td><td><code>ncit:C105713</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 60</code></td><td><code>ncit:C105712</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 70</code></td><td><code>ncit:C105711</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 80</code></td><td><code>ncit:C105710</code></td><td></td></tr>
<tr><td><code>Karnofsky &gt;&gt; 90</code></td><td><code>ncit:C105709</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 0</code></td><td><code>ncit:C70538</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 10</code></td><td><code>ncit:C70539</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 100</code></td><td><code>ncit:C69426</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 20</code></td><td><code>ncit:C70540</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 30</code></td><td><code>ncit:C70541</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 40</code></td><td><code>ncit:C70542</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 50</code></td><td><code>ncit:C69421</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 60</code></td><td><code>ncit:C69422</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 70</code></td><td><code>ncit:C69423</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 80</code></td><td><code>ncit:C69424</code></td><td></td></tr>
<tr><td><code>Lansky &gt;&gt; 90</code></td><td><code>ncit:C69425</code></td><td></td></tr>
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

<div id="enum-modal-procedureextentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-procedureextentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-procedureextentenum')">×</button>
<h3><code>ProcedureExtentEnum</code></h3>
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

<div id="enum-modal-reasonoffenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasonoffenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasonoffenum')">×</button>
<h3><code>ReasonOffEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Completion of Follow-Up</code></td><td><code>ncit:C178071</code></td><td></td></tr>
<tr><td><code>Completion of Planned Therapy</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Death</code></td><td><code>ncit:C28554</code></td><td>(os) ConsortiumNote: If multiple reasons for off 'Protocol Therapy' or off 'Study', include one observation per reason.</td></tr>
<tr><td><code>Development of SMN</code></td><td><code>ncit:C4968</code></td><td></td></tr>
<tr><td><code>Disease Progression</code></td><td><code>ncit:C17747</code></td><td></td></tr>
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Toxicity</code></td><td><code>ncit:C27990</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-recoverytypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-recoverytypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-recoverytypeenum')">×</button>
<h3><code>RecoveryTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Anemia</code></td><td><code>ncit:C2869</code></td><td></td></tr>
<tr><td><code>Neutrophil</code></td><td><code>ncit:C12533</code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C12520</code></td><td></td></tr>
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
<tr><td><code>RECIST</code></td><td><code>ncit:C49164</code></td><td></td></tr>
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
<tr><td><code>Local Extension</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>AEWS0031</code></td><td><code>ncit:C174970</code></td><td></td></tr>
<tr><td><code>AEWS0331</code></td><td><code>ncit:C174969</code></td><td></td></tr>
<tr><td><code>AEWS07P1</code></td><td><code>ncit:C174974</code></td><td></td></tr>
<tr><td><code>AEWS1031</code></td><td><code>ncit:C174971</code></td><td></td></tr>
<tr><td><code>AEWS1221</code></td><td><code>ncit:C174968</code></td><td></td></tr>
<tr><td><code>EE99</code></td><td><code>ncit:C174972</code></td><td>(ews) ConsortiumNote: COG not submitting any EE99</td></tr>
<tr><td><code>EICESS92</code></td><td><code>ncit:C174973</code></td><td></td></tr>
<tr><td><code>EWS2008</code></td><td><code></code></td><td>(ews) ConsortiumNote: EE99 data should not include patients from Ewing2008</td></tr>
<tr><td><code>EWS2012</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ISG/AIEOP Ew1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ISG/AIEOP Ew2</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>AEWS0031:2W-VDC-MESNA+IFO-GCSF</code></td><td><code>ncit:C174976</code></td><td></td></tr>
<tr><td><code>AEWS0031:3W-VDC-MESNA+IFO-GCSF</code></td><td><code>ncit:C174975</code></td><td></td></tr>
<tr><td><code>AEWS0331:VIDE-Surgery-R1-VAI-VAC/VAI</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS0331:VIDE-Surgery-R2-VAI-VAI/BuMel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS0331:VIDE-Surgery-R3-VAI-MEME/TreoMel/BuMel/P2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS07P1:EVAIA-EVAIA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS07P1:VAIA-VACA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS07P1:VAIA-VAIA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS1031:VIDEC</code></td><td><code>ncit:C174982</code></td><td></td></tr>
<tr><td><code>AEWS1031:VIDEC+Topotecan</code></td><td><code>ncit:C174983</code></td><td></td></tr>
<tr><td><code>AEWS1221:VDC-IE</code></td><td><code>ncit:C174977</code></td><td></td></tr>
<tr><td><code>AEWS1221:VDC-IE+Ganitumab</code></td><td><code>ncit:C174978</code></td><td></td></tr>
<tr><td><code>EE99:Not Randomized</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R1-VAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R1-VAI</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R2Loc-BuMel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R2Loc-VAI</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R2Pulm-BuMel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EE99:R2Pulm-VAI + lung RT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EICESS92:HR-EVAIA</code></td><td><code>ncit:C174987</code></td><td></td></tr>
<tr><td><code>EICESS92:HR-VAIA</code></td><td><code>ncit:C174986</code></td><td></td></tr>
<tr><td><code>EICESS92:SR-VACA</code></td><td><code>ncit:C174985</code></td><td></td></tr>
<tr><td><code>EICESS92:SR-VAIA</code></td><td><code>ncit:C174984</code></td><td></td></tr>
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
<tr><td><code>EBRT, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Stereotactic Radiosurgery</code></td><td><code>ncit:C15358</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-thresholdlevelenum" class="enum-modal" onclick="closeEnumModal('enum-modal-thresholdlevelenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-thresholdlevelenum')">×</button>
<h3><code>ThresholdLevelEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>High</code></td><td><code>ncit:C177365</code></td><td></td></tr>
<tr><td><code>Low</code></td><td><code>ncit:C177366</code></td><td></td></tr>
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

<div id="enum-modal-transpositionorganenum" class="enum-modal" onclick="closeEnumModal('enum-modal-transpositionorganenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-transpositionorganenum')">×</button>
<h3><code>TranspositionOrganEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ovaries</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
    "ews": {
      "name": "ews",
      "title": "Ewing Sarcoma",
      "description": "The EWS view of the PCDC data model represents consensus data modeling by an international group of pediatric Ewing sarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Harmonization International Bone Sarcoma Consortium (HIBiSCus). It is based on the collective requirements of its contributors."
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
        "age_at_enrollment"
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
        "laboratory_test_specimen",
        "result_text",
        "result_numeric",
        "laboratory_test_result_unit",
        "threshold_level",
        "threshold_high",
        "threshold_low"
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
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "chromosome",
        "iscn",
        "gene",
        "gene_fusion_partner",
        "hgvs_coding",
        "hgvs_protein",
        "copy_number"
      ],
      "comments": [
        "D4CGNote: One observation/row per genetic alteration",
        "(fa) ConsortiumNote: This table is tiered as Priority."
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
        "diagnosis"
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
        "review_source",
        "detection_method",
        "site_classification",
        "disease_presence",
        "disease_site",
        "laterality",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "tumor_size",
        "multiplicity",
        "tumor_volume",
        "estimated_volume",
        "fracture",
        "ipsilateral_nodules",
        "joint_involvement",
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
    "DiseaseCharacteristics": {
      "slots": [
        "age_at_disease_characteristic",
        "performance_score"
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
        "procedure_performed",
        "site_classification",
        "procedure",
        "procedure_site",
        "laterality",
        "margins",
        "procedure_extent",
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
        "energy_type",
        "technique",
        "rt_dose",
        "rt_dose_unit",
        "boost_dose",
        "num_fraction",
        "fraction_dose",
        "fraction_dose_unit",
        "transposition_organ"
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
        "age_at_sct_harvest",
        "age_at_recovery",
        "sct_type",
        "stem_cell_source",
        "recovery_type",
        "recovery_status",
        "cd34_collected",
        "cd34_transplant"
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
        "response_system",
        "response_system_version",
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
        "age_at_ae_resolved",
        "ae_code",
        "ae_code_system",
        "ae_grade",
        "grade_system",
        "grade_system_version",
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
    "alteration_type": {
      "slot_uri": "ncit:C13202",
      "range": "AlterationTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb,ls"
      }
    },
    "threshold_level": {
      "slot_uri": "",
      "range": "ThresholdLevelEnum",
      "comments": [],
      "annotations": {}
    },
    "response_system": {
      "slot_uri": "ncit:C125932",
      "range": "ResponseSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,rb"
      }
    },
    "transposition_organ": {
      "slot_uri": "ncit:C175035",
      "range": "TranspositionOrganEnum",
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
    "recovery_type": {
      "slot_uri": "",
      "range": "RecoveryTypeEnum",
      "comments": [],
      "annotations": {}
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
    "age_at_recovery": {
      "slot_uri": "ncit:C113053",
      "range": "integer",
      "comments": [
        "(ews) ConsortiumNote: Only fill in when answered 'Yes' for RECOVERY_STATUS. The first day you reach the recovery level per RECOVERY_TYPE."
      ],
      "annotations": {}
    },
    "age_at_sct_harvest": {
      "slot_uri": "ncit:C198866",
      "range": "integer",
      "comments": [],
      "annotations": {}
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
    "performance_score": {
      "slot_uri": "",
      "range": "PerformanceScoreEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc,ls"
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
    "cd34_collected": {
      "slot_uri": "ncit:C175036",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "fa"
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
    "ipsilateral_nodules": {
      "slot_uri": "ncit:C174455",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "cd34_transplant": {
      "slot_uri": "ncit:C175037",
      "range": "decimal",
      "comments": [],
      "annotations": {
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
    "recovery_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "smn_field": {
      "slot_uri": "ncit:C175044",
      "range": "SmnFieldEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "procedure_performed": {
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
    "joint_involvement": {
      "slot_uri": "ncit:C174453",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "copy_number": {
      "slot_uri": "ncit:C49142",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "threshold_high": {
      "slot_uri": "ncit:C177365",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "estimated_volume": {
      "slot_uri": "",
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
    "disease_presence": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "grade_system": {
      "slot_uri": "ncit:C168872",
      "range": "GradeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "age_at_ihc": {
      "slot_uri": "ncit:C175006",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "age_at_disease_characteristic": {
      "slot_uri": "",
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
    },
    "sct_type": {
      "slot_uri": "ncit:C168864",
      "range": "SctTypeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "fa,hl",
        "tier_priority": "aml"
      }
    },
    "tumor_size": {
      "slot_uri": "",
      "range": "TumorSizeEnum",
      "comments": [
        "(ews) ConsortiumNote: For EE99, this is only applicable to lung mets"
      ],
      "annotations": {
        "tier_priority": "rb"
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
    "StemCellSourceEnum": {
      "permissible_values": {
        "Bone Marrow": {
          "meaning": "ncit:C12431",
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
        "Maintenance": {
          "meaning": "ncit:C15688",
          "comments": [
            "(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses."
          ]
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
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": [
            "(ews) ConsortiumNote: Included so that peritoneal effusions can be reported."
          ]
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
    "LaboratoryTestSpecimenEnum": {
      "permissible_values": {
        "Blood": {
          "meaning": "ncit:C17610",
          "comments": []
        },
        "Pleural Fluid": {
          "meaning": "ncit:C77613",
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
    "AlterationEnum": {
      "permissible_values": {
        "12q Gain": {
          "meaning": "ncit:C36441",
          "comments": []
        },
        "16q Loss": {
          "meaning": "ncit:C36515",
          "comments": []
        },
        "1q Gain": {
          "meaning": "ncit:C36482",
          "comments": []
        },
        "8q Gain": {
          "meaning": "ncit:C36488",
          "comments": []
        },
        "BCOR Rearranged": {
          "meaning": "ncit:C174461",
          "comments": []
        },
        "BCOR-MAML3": {
          "meaning": "ncit:C174487",
          "comments": []
        },
        "CCNB3-BCOR": {
          "meaning": "ncit:C139666",
          "comments": []
        },
        "CDKN2A": {
          "meaning": "ncit:C128817",
          "comments": []
        },
        "CIC Rearranged": {
          "meaning": "ncit:C165668",
          "comments": []
        },
        "CIC-DUX4": {
          "meaning": "ncit:C139663",
          "comments": []
        },
        "CIC-DUX4L10": {
          "meaning": "ncit:C174463",
          "comments": []
        },
        "EWSR1 Rearranged": {
          "meaning": "ncit:C165667",
          "comments": []
        },
        "EWSR1-ATF1": {
          "meaning": "ncit:C99216",
          "comments": []
        },
        "EWSR1-CREB1": {
          "meaning": "ncit:C99249",
          "comments": []
        },
        "EWSR1-DDIT3": {
          "meaning": "ncit:C99200",
          "comments": []
        },
        "EWSR1-ERG": {
          "meaning": "ncit:C99211",
          "comments": []
        },
        "EWSR1-ETV1": {
          "meaning": "ncit:C99259",
          "comments": []
        },
        "EWSR1-ETV4": {
          "meaning": "ncit:C99262",
          "comments": []
        },
        "EWSR1-FEV": {
          "meaning": "ncit:C99226",
          "comments": []
        },
        "EWSR1-FLI1": {
          "meaning": "ncit:C99202",
          "comments": []
        },
        "EWSR1-KLF17": {
          "meaning": "ncit:C174474",
          "comments": []
        },
        "EWSR1-NR4A3": {
          "meaning": "ncit:C99252",
          "comments": []
        },
        "EWSR1-PBX1": {
          "meaning": "ncit:C139668",
          "comments": []
        },
        "EWSR1-POU5F1": {
          "meaning": "ncit:C99256",
          "comments": []
        },
        "EWSR1-WT1": {
          "meaning": "ncit:C99213",
          "comments": []
        },
        "EWSR1-ZNF444": {
          "meaning": "ncit:C139731",
          "comments": []
        },
        "FUS Rearranged": {
          "meaning": "ncit:C174462",
          "comments": []
        },
        "FUS Translocation Present": {
          "meaning": "ncit:C25626",
          "comments": []
        },
        "FUS-DDIT3": {
          "meaning": "ncit:C99279",
          "comments": []
        },
        "FUS-ERG": {
          "meaning": "ncit:C99281",
          "comments": []
        },
        "FUS-FEV": {
          "meaning": "ncit:C174466",
          "comments": []
        },
        "FUS-KLF17": {
          "meaning": "ncit:C174473",
          "comments": []
        },
        "STAG2": {
          "meaning": "ncit:C153513",
          "comments": []
        },
        "TAF15-NR4A3": {
          "meaning": "ncit:C99501",
          "comments": []
        },
        "TP53": {
          "meaning": "ncit:C118396",
          "comments": []
        },
        "ZC3H7B-BCOR": {
          "meaning": "ncit:C174491",
          "comments": []
        },
        "inv(X)(p11.4;p11.22)": {
          "meaning": "ncit:C174489",
          "comments": []
        },
        "t(10;19)(q26;q13)": {
          "meaning": "ncit:C120223",
          "comments": []
        },
        "t(11;22)": {
          "meaning": "ncit:C128642",
          "comments": []
        },
        "t(11;22)(p13;q12)": {
          "meaning": "ncit:C36375",
          "comments": []
        },
        "t(11;22)(q24;q12)": {
          "meaning": "ncit:C27214",
          "comments": []
        },
        "t(12;16)(q13;p11)": {
          "meaning": "ncit:C36317",
          "comments": []
        },
        "t(12;22)(q13.12;q12)": {
          "meaning": "ncit:C174478",
          "comments": []
        },
        "t(12;22)(q13.3;q12)": {
          "meaning": "ncit:C174479",
          "comments": []
        },
        "t(16;21)(p11;q22)": {
          "meaning": "ncit:C36616",
          "comments": []
        },
        "t(17;22)(q21;q12)": {
          "meaning": "ncit:C36369",
          "comments": []
        },
        "t(19;22)(q13;q12)": {
          "meaning": "ncit:C174480",
          "comments": []
        },
        "t(1;16)(p34;p11)": {
          "meaning": "ncit:C174475",
          "comments": []
        },
        "t(1;22)(p34;q12)": {
          "meaning": "ncit:C174476",
          "comments": []
        },
        "t(1;22)(q23;q12)": {
          "meaning": "ncit:C174477",
          "comments": []
        },
        "t(21;22)(q22;q12)": {
          "meaning": "ncit:C36367",
          "comments": []
        },
        "t(2;16)(q35;p11)": {
          "meaning": "ncit:C174465",
          "comments": []
        },
        "t(2;22)(q33;q12)": {
          "meaning": "ncit:C37249",
          "comments": []
        },
        "t(2;22)(q34;q12)": {
          "meaning": "ncit:C174481",
          "comments": []
        },
        "t(4;19)(q25;q13)": {
          "meaning": "ncit:C174482",
          "comments": []
        },
        "t(4;19)(q35;q13)": {
          "meaning": "ncit:C120222",
          "comments": []
        },
        "t(6;22)(p21;q12)": {
          "meaning": "ncit:C174483",
          "comments": []
        },
        "t(7;22)(p22;q12)": {
          "meaning": "ncit:C36368",
          "comments": []
        },
        "t(9;17)(q22;q11)": {
          "meaning": "ncit:C36393",
          "comments": []
        },
        "t(9;22)(q22;q12)": {
          "meaning": "ncit:C174484",
          "comments": []
        },
        "t(X;22)(p11;q13)": {
          "meaning": "ncit:C174495",
          "comments": []
        },
        "t(X;4)(p11;q31)": {
          "meaning": "ncit:C174490",
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
    "ResponseSystemEnum": {
      "permissible_values": {
        "RECIST": {
          "meaning": "ncit:C49164",
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
    "MultiplicityEnum": {
      "permissible_values": {
        "Multiple Tumors": {
          "meaning": "",
          "comments": []
        },
        "Single Tumor": {
          "meaning": "",
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
        },
        "m2": {
          "meaning": "ncit:C42569",
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
    "ThresholdLevelEnum": {
      "permissible_values": {
        "High": {
          "meaning": "ncit:C177365",
          "comments": []
        },
        "Low": {
          "meaning": "ncit:C177366",
          "comments": []
        }
      }
    },
    "StudyIdEnum": {
      "permissible_values": {
        "AEWS0031": {
          "meaning": "ncit:C174970",
          "comments": []
        },
        "AEWS0331": {
          "meaning": "ncit:C174969",
          "comments": []
        },
        "AEWS07P1": {
          "meaning": "ncit:C174974",
          "comments": []
        },
        "AEWS1031": {
          "meaning": "ncit:C174971",
          "comments": []
        },
        "AEWS1221": {
          "meaning": "ncit:C174968",
          "comments": []
        },
        "EE99": {
          "meaning": "ncit:C174972",
          "comments": [
            "(ews) ConsortiumNote: COG not submitting any EE99"
          ]
        },
        "EICESS92": {
          "meaning": "ncit:C174973",
          "comments": []
        },
        "EWS2008": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: EE99 data should not include patients from Ewing2008"
          ]
        },
        "EWS2012": {
          "meaning": "",
          "comments": []
        },
        "ISG/AIEOP Ew1": {
          "meaning": "",
          "comments": []
        },
        "ISG/AIEOP Ew2": {
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
        "Ewing Sarcoma": {
          "meaning": "icdo:9260/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Large Cell Ewing Tumor": {
          "meaning": "ncit:C174456",
          "comments": []
        },
        "Neuro-differentiated Ewing Tumor": {
          "meaning": "ncit:C9341",
          "comments": []
        },
        "Round Blue Cell Tumor/Sarcoma": {
          "meaning": "",
          "comments": []
        },
        "Undifferentiated Ewing Tumor": {
          "meaning": "ncit:C121799",
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
        "Bone Marrow Aspirates": {
          "meaning": "",
          "comments": []
        },
        "Bone Marrow Trephine Biopsy": {
          "meaning": "",
          "comments": []
        },
        "CT Scan": {
          "meaning": "ncit:C17204",
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
        "Technetium Bone Scan": {
          "meaning": "",
          "comments": []
        },
        "X-Ray": {
          "meaning": "ncit:C38101",
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
    "TranspositionOrganEnum": {
      "permissible_values": {
        "Ovaries": {
          "meaning": "ncit:C12404",
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
        "Cytogenetics, NOS": {
          "meaning": "ncit:C16487",
          "comments": []
        },
        "Genotyping, NOS": {
          "meaning": "ncit:C45447",
          "comments": []
        },
        "PCR, NOS": {
          "meaning": "ncit:C17003",
          "comments": []
        },
        "Sequencing, NGS, NOS": {
          "meaning": "ncit:C101293",
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
    "DiseaseGroupEnum": {
      "permissible_values": {
        "EWS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Cabozantinib": {
          "meaning": "ncit:C52200",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Celecoxib": {
          "meaning": "ncit:C1728",
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
        "GCSF": {
          "meaning": "ncit:C26078",
          "comments": []
        },
        "GMCSF": {
          "meaning": "ncit:C20545",
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
        "Irinotecan": {
          "meaning": "ncit:C62040",
          "comments": []
        },
        "Melphalan": {
          "meaning": "rxcui:6718",
          "comments": []
        },
        "Pazopanib": {
          "meaning": "rxcui:714438",
          "comments": []
        },
        "Plerixafor": {
          "meaning": "ncit:C1777",
          "comments": []
        },
        "Regorafenib": {
          "meaning": "ncit:C78204",
          "comments": []
        },
        "Temozolomide": {
          "meaning": "rxcui:37776",
          "comments": []
        },
        "Topotecan": {
          "meaning": "rxcui:57308",
          "comments": []
        },
        "Trabectedin": {
          "meaning": "ncit:C1691",
          "comments": []
        },
        "Treosulfan": {
          "meaning": "rxcui:38508",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
          "comments": []
        },
        "Zoledronic Acid": {
          "meaning": "ncit:C1699",
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
    "RecoveryTypeEnum": {
      "permissible_values": {
        "Anemia": {
          "meaning": "ncit:C2869",
          "comments": []
        },
        "Neutrophil": {
          "meaning": "ncit:C12533",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C12520",
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
    "MarkersEnum": {
      "permissible_values": {
        "CD45": {
          "meaning": "ncit:C17282",
          "comments": []
        },
        "CD99/Cell Surface Antigen O13/Cell Surface Antigen HBA-71": {
          "meaning": "ncit:C102941",
          "comments": []
        },
        "Desmin": {
          "meaning": "ncit:C96450",
          "comments": []
        },
        "FLI-1": {
          "meaning": "ncit:C18566",
          "comments": []
        },
        "NSE": {
          "meaning": "ncit:C62216",
          "comments": []
        },
        "PAS": {
          "meaning": "ncit:C23019",
          "comments": []
        },
        "S100": {
          "meaning": "ncit:C29924",
          "comments": []
        },
        "Vimentin": {
          "meaning": "ncit:C48797",
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
        },
        "Relapse/Progression": {
          "meaning": "ncit:C174991",
          "comments": []
        }
      }
    },
    "SubgroupNameEnum": {
      "permissible_values": {
        "AEWS0031:2W-VDC-MESNA+IFO-GCSF": {
          "meaning": "ncit:C174976",
          "comments": []
        },
        "AEWS0031:3W-VDC-MESNA+IFO-GCSF": {
          "meaning": "ncit:C174975",
          "comments": []
        },
        "AEWS0331:VIDE-Surgery-R1-VAI-VAC/VAI": {
          "meaning": "",
          "comments": []
        },
        "AEWS0331:VIDE-Surgery-R2-VAI-VAI/BuMel": {
          "meaning": "",
          "comments": []
        },
        "AEWS0331:VIDE-Surgery-R3-VAI-MEME/TreoMel/BuMel/P2": {
          "meaning": "",
          "comments": []
        },
        "AEWS07P1:EVAIA-EVAIA": {
          "meaning": "",
          "comments": []
        },
        "AEWS07P1:VAIA-VACA": {
          "meaning": "",
          "comments": []
        },
        "AEWS07P1:VAIA-VAIA": {
          "meaning": "",
          "comments": []
        },
        "AEWS1031:VIDEC": {
          "meaning": "ncit:C174982",
          "comments": []
        },
        "AEWS1031:VIDEC+Topotecan": {
          "meaning": "ncit:C174983",
          "comments": []
        },
        "AEWS1221:VDC-IE": {
          "meaning": "ncit:C174977",
          "comments": []
        },
        "AEWS1221:VDC-IE+Ganitumab": {
          "meaning": "ncit:C174978",
          "comments": []
        },
        "EE99:Not Randomized": {
          "meaning": "",
          "comments": []
        },
        "EE99:R1-VAC": {
          "meaning": "",
          "comments": []
        },
        "EE99:R1-VAI": {
          "meaning": "",
          "comments": []
        },
        "EE99:R2Loc-BuMel": {
          "meaning": "",
          "comments": []
        },
        "EE99:R2Loc-VAI": {
          "meaning": "",
          "comments": []
        },
        "EE99:R2Pulm-BuMel": {
          "meaning": "",
          "comments": []
        },
        "EE99:R2Pulm-VAI + lung RT": {
          "meaning": "",
          "comments": []
        },
        "EICESS92:HR-EVAIA": {
          "meaning": "ncit:C174987",
          "comments": []
        },
        "EICESS92:HR-VAIA": {
          "meaning": "ncit:C174986",
          "comments": []
        },
        "EICESS92:SR-VACA": {
          "meaning": "ncit:C174985",
          "comments": []
        },
        "EICESS92:SR-VAIA": {
          "meaning": "ncit:C174984",
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
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Breast and Ovarian Cancer": {
          "meaning": "ncit:C8493",
          "comments": []
        },
        "Fanconi Anemia": {
          "meaning": "ncit:C62505",
          "comments": []
        },
        "Li-Fraumeni Syndrome": {
          "meaning": "ncit:C3476",
          "comments": []
        },
        "Lynch Syndrome": {
          "meaning": "ncit:C8494",
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
        "EBRT, NOS": {
          "meaning": "",
          "comments": []
        },
        "EBRT, Stereotactic Radiosurgery": {
          "meaning": "ncit:C15358",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        "CTCAE": {
          "meaning": "ncit:C49704",
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
        "Alkaline Phophatase": {
          "meaning": "ncit:C64432",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "Cytology Malignant Cells": {
          "meaning": "ncit:C74660",
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
        }
      }
    },
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "U/L": {
          "meaning": "ncit:C67456",
          "comments": []
        },
        "mm/h": {
          "meaning": "ncit:C67419",
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
    },
    "PerformanceScoreEnum": {
      "permissible_values": {
        "GPOH >> 1": {
          "meaning": "ncit:C174992",
          "comments": []
        },
        "GPOH >> 2": {
          "meaning": "ncit:C174993",
          "comments": []
        },
        "GPOH >> 3": {
          "meaning": "ncit:C174994",
          "comments": []
        },
        "GPOH >> 4": {
          "meaning": "ncit:C174995",
          "comments": []
        },
        "GPOH >> 5": {
          "meaning": "ncit:C174996",
          "comments": []
        },
        "Karnofsky >> 0": {
          "meaning": "ncit:C105720",
          "comments": []
        },
        "Karnofsky >> 10": {
          "meaning": "ncit:C105718",
          "comments": []
        },
        "Karnofsky >> 100": {
          "meaning": "ncit:C105707",
          "comments": []
        },
        "Karnofsky >> 20": {
          "meaning": "ncit:C105716",
          "comments": []
        },
        "Karnofsky >> 30": {
          "meaning": "ncit:C105715",
          "comments": []
        },
        "Karnofsky >> 40": {
          "meaning": "ncit:C105714",
          "comments": []
        },
        "Karnofsky >> 50": {
          "meaning": "ncit:C105713",
          "comments": []
        },
        "Karnofsky >> 60": {
          "meaning": "ncit:C105712",
          "comments": []
        },
        "Karnofsky >> 70": {
          "meaning": "ncit:C105711",
          "comments": []
        },
        "Karnofsky >> 80": {
          "meaning": "ncit:C105710",
          "comments": []
        },
        "Karnofsky >> 90": {
          "meaning": "ncit:C105709",
          "comments": []
        },
        "Lansky >> 0": {
          "meaning": "ncit:C70538",
          "comments": []
        },
        "Lansky >> 10": {
          "meaning": "ncit:C70539",
          "comments": []
        },
        "Lansky >> 100": {
          "meaning": "ncit:C69426",
          "comments": []
        },
        "Lansky >> 20": {
          "meaning": "ncit:C70540",
          "comments": []
        },
        "Lansky >> 30": {
          "meaning": "ncit:C70541",
          "comments": []
        },
        "Lansky >> 40": {
          "meaning": "ncit:C70542",
          "comments": []
        },
        "Lansky >> 50": {
          "meaning": "ncit:C69421",
          "comments": []
        },
        "Lansky >> 60": {
          "meaning": "ncit:C69422",
          "comments": []
        },
        "Lansky >> 70": {
          "meaning": "ncit:C69423",
          "comments": []
        },
        "Lansky >> 80": {
          "meaning": "ncit:C69424",
          "comments": []
        },
        "Lansky >> 90": {
          "meaning": "ncit:C69425",
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