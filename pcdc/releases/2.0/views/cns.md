---
layout: default
title: Central Nervous System Tumors
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*CNS View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- **Central Nervous System Tumors**
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

The CNS view of the PCDC data model represents consensus data modeling by an international group of pediatric central nervous system tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Central Nervous System Pediatric Research Consortium (INSPiRE). It is based on the collective requirements of its contributors.


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
| `age_precision` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ageprecisionenum')">AgePrecisionEnum</button> |  |

## OffProtocolTherapyOrStudy

| Slot | Range | Description |
|---|---|---|
| `age_off` | `integer` |  |
| `off_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-offtypeenum')">OffTypeEnum</button> |  |
| `reason_off` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonoffenum')">ReasonOffEnum</button> |  |
| `reason_off_other` | `string` |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `enrolled_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
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
| `country` | `string` |  |
| `efs_censor_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-efscensorstatusenum')">EfsCensorStatusEnum</button> |  |
| `age_at_censor_status` | `integer` |  |

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
| `lkss_with_disease` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |
| `cause_of_death_other` | `string` |  |
| `cause_of_death_ranking` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathrankingenum')">CauseOfDeathRankingEnum</button> |  |

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `determination_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-determinationsourceenum')">DeterminationSourceEnum</button> |  |
| `diagnosis_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosiscategoryenum')">DiagnosisCategoryEnum</button> |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histology_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologygradeenum')">HistologyGradeEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `mri_sequence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mrisequenceenum')">MriSequenceEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |
| `tumor_presentation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorpresentationenum')">TumorPresentationEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `protocol_medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `non_protocol_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocolreasonenum')">NonProtocolReasonEnum</button> |  |
| `route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `medication_other` | `string` |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `protocol_radiation_therapy` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `rt_data_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdatasourceenum')">RtDataSourceEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-boosttypeenum')">BoostTypeEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |
| `rt_margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtmarginsenum')">RtMarginsEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `protocol_procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-extentenum')">ExtentEnum</button> |  |
| `outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-outcomeenum')">OutcomeEnum</button> |  |
| `hydrocephalus` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hydrocephalusenum')">HydrocephalusEnum</button> |  |
| `posterior_fossa_syndrome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `csf_diversion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-csfdiversionenum')">CsfDiversionEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsemethodenum')">ResponseMethodEnum</button> |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsesystemenum')">ResponseSystemEnum</button> |  |
| `response_system_version` | `string` |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `mri_sequence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mrisequenceenum')">MriSequenceEnum</button> |  |
| `neurological_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-neurologicalstatusenum')">NeurologicalStatusEnum</button> |  |

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

<div class="domain-heading">Testing</div>

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `genomic_source_class` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genomicsourceclassenum')">GenomicSourceClassEnum</button> |  |
| `mosaicism` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `mosaicism_percent` | `decimal` |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `alteration_region` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationregionenum')">AlterationRegionEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein` | `string` |  |
| `external_ref_id_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-externalrefidsystemenum')">ExternalRefIdSystemEnum</button> |  |
| `external_ref_id` | `string` |  |
| `copy_number` | `decimal` |  |
| `maf_numeric` | `decimal` |  |
| `allelic_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button> |  |

## VitalsAndAnthropometrics

| Slot | Range | Description |
|---|---|---|
| `age_at_measurement` | `integer` |  |
| `anthropometric_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementtypeenum')">AnthropometricMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `anthropometric_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">AnthropometricMeasurementResultUnitEnum</button> |  |

<div id="enum-modal-ageprecisionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ageprecisionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ageprecisionenum')">×</button>
<h3><code>AgePrecisionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Approximate</code></td><td><code>ncit:C45828</code></td><td></td></tr>
<tr><td><code>Exact</code></td><td><code>ncit:C86021</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-allelicstateenum" class="enum-modal" onclick="closeEnumModal('enum-modal-allelicstateenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-allelicstateenum')">×</button>
<h3><code>AllelicStateEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Heterozygous</code></td><td><code>ncit:C45825</code></td><td></td></tr>
<tr><td><code>Homozygous</code></td><td><code>ncit:C45826</code></td><td></td></tr>
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
<tr><td><code>C19MC Amplification</code></td><td><code>ncit:C129498</code></td><td></td></tr>
<tr><td><code>CTNNB1 Variant</code></td><td><code>ncit:C36659</code></td><td></td></tr>
<tr><td><code>Chromosome 11 Loss</code></td><td><code>ncit:C36549</code></td><td></td></tr>
<tr><td><code>Chromosome 14q Loss</code></td><td><code>ncit:C39795</code></td><td></td></tr>
<tr><td><code>DICER1 Variant</code></td><td><code>ncit:C164287</code></td><td></td></tr>
<tr><td><code>GLI2 Amplification</code></td><td><code>ncit:C199588</code></td><td></td></tr>
<tr><td><code>Isochromosome 17q</code></td><td><code>ncit:C36477</code></td><td></td></tr>
<tr><td><code>MYC Amplification</code></td><td><code>ncit:C36641</code></td><td></td></tr>
<tr><td><code>MYCN Amplification</code></td><td><code>ncit:C36673</code></td><td></td></tr>
<tr><td><code>PTCH1 Variant</code></td><td><code>ncit:C133669</code></td><td></td></tr>
<tr><td><code>RB1 Variant</code></td><td><code>ncit:C169031</code></td><td></td></tr>
<tr><td><code>SMARCB1 Variant</code></td><td><code>ncit:C18394</code></td><td></td></tr>
<tr><td><code>SMO Variant</code></td><td><code>ncit:C124793</code></td><td></td></tr>
<tr><td><code>SUFU Variant</code></td><td><code>ncit:C189843</code></td><td></td></tr>
<tr><td><code>TP53 Variant</code></td><td><code>ncit:C118396</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Head Circumference</code></td><td><code>ncit:C81255</code></td><td>(fa) ConsortiumNote: Prioritize Head Circumference at birth and at other evaluations.</td></tr>
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
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
<tr><td><code>INSPiRE</code></td><td><code>ncit:C192765</code></td><td></td></tr>
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
<tr><td><code>Chemoradiotherapy</code></td><td><code>ncit:C94626</code></td><td>(cns) ConsortiumNote: SIOPE groups should use this value in place of what they may have as 'concommitant'.</td></tr>
<tr><td><code>Chemotherapy Window</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Consolidation</code></td><td><code>ncit:C15679</code></td><td></td></tr>
<tr><td><code>Induction</code></td><td><code>ncit:C158876</code></td><td></td></tr>
<tr><td><code>Investigational Agent</code></td><td><code>ncit:C49135</code></td><td>(cns) ConsortiumNote: This value should be used for data that may have 'concomitant' listed in the source.</td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-csfdiversionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-csfdiversionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-csfdiversionenum')">×</button>
<h3><code>CsfDiversionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Endoscopic Third Ventriculostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No</code></td><td><code>ncit:C49487</code></td><td></td></tr>
<tr><td><code>Shunt, NOS</code></td><td><code>ncit:C50174</code></td><td></td></tr>
<tr><td><code>Ventriculoatrial Shunt</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ventriculoperitoneal Shunt</code></td><td><code>ncit:C168483</code></td><td></td></tr>
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

<div id="enum-modal-detectionmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-detectionmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-detectionmethodenum')">×</button>
<h3><code>DetectionMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cytology</code></td><td><code>ncit:C16491</code></td><td></td></tr>
<tr><td><code>Liquid Biopsy</code></td><td><code>ncit:C135727</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Physical Examination</code></td><td><code>ncit:C20989</code></td><td></td></tr>
<tr><td><code>Surgical Pathology</code></td><td><code>ncit:C16958</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-determinationsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-determinationsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-determinationsourceenum')">×</button>
<h3><code>DeterminationSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clinical Testing</code></td><td><code>ncit:C15791</code></td><td></td></tr>
<tr><td><code>Retrospective Research</code></td><td><code>ncit:C53312</code></td><td></td></tr>
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

<div id="enum-modal-diagnosiscategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosiscategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosiscategoryenum')">×</button>
<h3><code>DiagnosisCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor</code></td><td><code>ncit:C6906</code></td><td></td></tr>
<tr><td><code>CNS Germ Cell Tumors</code></td><td><code>ncit:C5461</code></td><td></td></tr>
<tr><td><code>Choroid Plexus Tumors</code></td><td><code>ncit:C3473</code></td><td></td></tr>
<tr><td><code>Craniopharyngioma</code></td><td><code>ncit:C2964</code></td><td></td></tr>
<tr><td><code>Ependymoma</code></td><td><code>icdo:9391/3</code></td><td>(cns) ConsortiumNote: Includes ependymal tumors</td></tr>
<tr><td><code>Glioneuronal and Neuronal Tumors</code></td><td><code>ncit:C4747</code></td><td></td></tr>
<tr><td><code>High-Grade Glioma</code></td><td><code>ncit:C162993</code></td><td>(cns) ConsortiumNote: Includes adult-type diffuse gliomas, pediatric type diffuse high-grade gliomas, some circumscribed astrocytic gliomas</td></tr>
<tr><td><code>Low-Grade Glioma</code></td><td><code>ncit:C132067</code></td><td>(cns) ConsortiumNote: Includes pediatric type diffuse low-grade gliomas, some circumscribed astrocytic gliomas.</td></tr>
<tr><td><code>Medulloblastoma</code></td><td><code>icdo:9470/3</code></td><td></td></tr>
<tr><td><code>Other CNS Embryonal Tumors</code></td><td><code>ncit:C6990</code></td><td>(cns) ConsortiumNote: Includes pineoblastoma</td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Adamantinomatous Craniopharyngioma</code></td><td><code>ncit:C4726</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'</td></tr>
<tr><td><code>Anaplastic Ganglioglioma</code></td><td><code>ncit:C4717</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Anaplastic Large Cell Lymphoma</code></td><td><code>ncit:C3720</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Anaplastic Oligoastrocytoma</code></td><td><code>ncit:C6959</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Anaplastic Oligodendroglioma</code></td><td><code>ncit:C4326</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Angiocentric Glioma</code></td><td><code>icdo:9431/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Astroblastoma, MN1-Altered</code></td><td><code>ncit:C4324</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Astrocytoma Tumors</code></td><td><code>ncit:C60781</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'</td></tr>
<tr><td><code>Astrocytoma With Piloid Features</code></td><td><code>ncit:C185879</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Astrocytoma, IDH-Mutant</code></td><td><code>ncit:C185167</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Atypical Choroid Plexus Papilloma</code></td><td><code>ncit:C53686</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'</td></tr>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor, MYC Gene (ATRT-MYC)</code></td><td><code>ncit:C200599</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'</td></tr>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor, NOS or NEC</code></td><td><code>ncit:C6906</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'</td></tr>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor, Sonic Hedgehog (ATRT-SHH)</code></td><td><code>ncit:C200598</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'</td></tr>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor, Tyrosinase Gene (ATRT-TYR)</code></td><td><code>ncit:C200600</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'</td></tr>
<tr><td><code>CIC-Rearranged Sarcoma</code></td><td><code>ncit:C120224</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>CNS Germinoma</code></td><td><code>ncit:C7009</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'CNS Germ Cell Tumors'</td></tr>
<tr><td><code>CNS Non-Germinomatous Germ Cell Tumor</code></td><td><code>ncit:C100093</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'CNS Germ Cell Tumors'</td></tr>
<tr><td><code>Central Nervous System B-Cell Non-Hodgkin Lymphoma</code></td><td><code>ncit:C147948</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Central Nervous System Mature T-Cell and NK-Cell Non-Hodgkin Lymphoma</code></td><td><code>ncit:C129600</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Central Neurocytoma</code></td><td><code>ncit:C3791</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Cerebellar Liponeurocytoma</code></td><td><code>ncit:C6905</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Chondrosarcoma</code></td><td><code>ncit:C2946</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Chordoma</code></td><td><code>ncit:C2947</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Choroid Plexus Carcinoma</code></td><td><code>ncit:C4715</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'</td></tr>
<tr><td><code>Choroid Plexus Papilloma</code></td><td><code>ncit:C3698</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'</td></tr>
<tr><td><code>Desmoplastic Myxoid Tumor of the Pineal Region  SMARCB1-Mutant</code></td><td><code>ncit:C178507</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Diffuse Astrocytoma, MYB- Or MYBL1-Altered</code></td><td><code>ncit:C129274</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Diffuse Glioneuronal Tumor with Oligodendroglioma-Like Features and Nuclear Clusters</code></td><td><code>ncit:C185935</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Diffuse Hemispheric Glioma, H3 G34-Mutant</code></td><td><code>ncit:C185371</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Diffuse Leptomeningeal Glioneuronal Tumor</code></td><td><code>icdo:9509/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Diffuse Low-Grade Glioma, MAPK Pathway-Altered</code></td><td><code>ncit:C185218</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Diffuse Midline Glioma, H3 K27-Altered</code></td><td><code>ncit:C185368</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Diffuse Pediatric-Type High-Grade Glioma, H3-Wildtype And IDH-Wildtype</code></td><td><code>ncit:C185467</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Dural Extranodal Marginal Zone Lymphoma of Mucosa-Associated Lymphoid Tissue</code></td><td><code>ncit:C95991</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Dysembryoplastic Neuroepithelial Tumor</code></td><td><code>icdo:9413/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Dysplastic Cerebellar Gangliocytoma</code></td><td><code>ncit:C8419</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Embryonal Tumor with Multilayered Rosettes, C19MC Amplified</code></td><td><code>ncit:C186534</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Embryonal Tumor with Multilayered Rosettes, C19MC Not Amplified</code></td><td><code>ncit:C4915</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Embryonal Tumor with Multilayered Rosettes, NOS or NEC</code></td><td><code>ncit:C186534</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Erdheim-Chester Disease</code></td><td><code>icdo:9749/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Ewing Sarcoma</code></td><td><code>icdo:9260/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Extraventricular Neurocytoma</code></td><td><code>ncit:C92555</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Gangliocytoma</code></td><td><code>icdo:9492/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Ganglioglioma</code></td><td><code>ncit:C3788</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Giant Cell Astrocytoma</code></td><td><code>ncit:C3696</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Glioblastoma, IDH-Wildtype</code></td><td><code>ncit:C39750</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Glioneuronal and Neuronal Tumors</code></td><td><code>ncit:C4747</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Gliosarcoma</code></td><td><code>icdo:9442/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Hemangioblastoma</code></td><td><code>icdo:9161/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hemangiomas and Vascular Malformations</code></td><td><code></code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>High-Grade Glioma, NOS or NEC</code></td><td><code>ncit:C4822</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Histiocytic Sarcoma</code></td><td><code>ncit:C27349</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hybrid Nerve Sheath Tumor</code></td><td><code>ncit:C121686</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Immunodeficiency-Related Central Nervous System Lymphoma</code></td><td><code>ncit:C186658</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Infant-Type Hemispheric Glioma</code></td><td><code>ncit:C185471</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Intracranial Mesenchymal Tumor  FET-CREB Fusion-Positive</code></td><td><code>ncit:C186614</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Intravascular Large B-Cell Lymphoma</code></td><td><code>icdo:9712/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Juvenile Xanthogranuloma</code></td><td><code>icdo:9749/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Langerhans Cell Histiocytosis</code></td><td><code>ncit:C3107</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Low-Grade Glioma, NOS or NEC</code></td><td><code>ncit:C132067</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Lymphomatoid Granulomatosis</code></td><td><code>ncit:C7930</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Malignant Melanotic Nerve Sheath Tumor</code></td><td><code>ncit:C4748</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>icdo:9540/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Medulloblastoma, Classic</code></td><td><code>ncit:C54039</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, Group 3</code></td><td><code>ncit:C129445</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, Group 4</code></td><td><code>ncit:C129446</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, Large Cell/Anaplastic</code></td><td><code>ncit:C129436</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, NOS or NEC</code></td><td><code>ncit:C3222</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, Nodular Desmoplastic</code></td><td><code>ncit:C4956</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, Non-WNT/Non-SHH</code></td><td><code>ncit:C129444</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, SHH-Activated and TP53-Mutant</code></td><td><code>ncit:C129442</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, SHH-Activated and TP53-Wildtype</code></td><td><code>ncit:C129443</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Medulloblastoma, WNT-Activated</code></td><td><code>ncit:C129440</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'</td></tr>
<tr><td><code>Meningioma</code></td><td><code>ncit:C3230</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Mesenchymal Chondrosarcoma</code></td><td><code>icdo:9240/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Multinodular and Vacuolated Neuronal Tumor</code></td><td><code>ncit:C129427</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Myxoid Glioneuronal Tumor</code></td><td><code>ncit:C179229</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Myxopapillary Ependymoma</code></td><td><code>ncit:C3697</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Neurofibroma</code></td><td><code>ncit:C3272</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Oligoastrocytic Tumors</code></td><td><code>ncit:C186217</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'</td></tr>
<tr><td><code>Oligoastrocytoma</code></td><td><code>ncit:C4050</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Oligodendroglial Tumors</code></td><td><code>ncit:C103050</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'</td></tr>
<tr><td><code>Oligodendroglioma, IDH-Mutant, And 1P/19Q-Codeleted</code></td><td><code>ncit:C129318</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Papillary Craniopharyngioma</code></td><td><code>icdo:9352/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'</td></tr>
<tr><td><code>Papillary Glioneuronal Tumor</code></td><td><code>icdo:9509/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Papillary Tumor of the Pineal Region</code></td><td><code>ncit:C92624</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Paraganglioma</code></td><td><code>ncit:C3308</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Perineurioma</code></td><td><code>ncit:C4973</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pilocytic Astrocytoma</code></td><td><code>icdo:9421/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pilomyxoid Astrocytoma</code></td><td><code>icdo:9425/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pineal Parenchymal Tumor of Intermediate Differentiation</code></td><td><code>ncit:C6967</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pineal Tumors</code></td><td><code>ncit:C41834</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineoblastoma, MYC/FOXR2</code></td><td><code>ncit:C201973</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineoblastoma, MiRNA1</code></td><td><code>ncit:C201967</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineoblastoma, MiRNA2</code></td><td><code>ncit:C201968</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineoblastoma, NOS or NEC</code></td><td><code>ncit:C9344</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineoblastoma, RB1</code></td><td><code>ncit:C201969</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'</td></tr>
<tr><td><code>Pineocytoma</code></td><td><code>icdo:9361/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pituitary Gland Blastoma</code></td><td><code>ncit:C155304</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pituitary Neuroendocrine Tumor</code></td><td><code>ncit:C3329</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pleomorphic Xanthoastrocytoma</code></td><td><code>icdo:9424/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Polymorphous Low-Grade Neuroepithelial Tumor Of The Young</code></td><td><code>ncit:C180378</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Posterior Fossa Ependymoma</code></td><td><code>ncit:C186443</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Posterior Fossa Ependymoma, Group PFA</code></td><td><code>ncit:C186450</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Posterior Fossa Ependymoma, Group PFB</code></td><td><code>ncit:C186451</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Posterior Pituitary Gland Neoplasm</code></td><td><code>ncit:C7157</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Primary Diffuse Large B-Cell Lymphoma of the Central Nervous System</code></td><td><code>ncit:C71720</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Primary Intracranial Sarcoma  DICER1-Mutant</code></td><td><code>ncit:C186610</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Primary Meningeal Melanocytic Neoplasm</code></td><td><code>ncit:C4661</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>ncit:C3359</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Rosai-Dorfman Disease</code></td><td><code>ncit:C36075</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Rosette-Forming Glioneuronal Tumor</code></td><td><code>ncit:C129431</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Schwannoma</code></td><td><code>ncit:C3269</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Solitary Fibrous Tumor</code></td><td><code>ncit:C7634</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Spinal Ependymoma</code></td><td><code>ncit:C3875</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Spinal Ependymoma, MYCN-Amplified</code></td><td><code>ncit:C186494</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Subependymal Giant Cell Astrocytoma</code></td><td><code>ncit:C3696</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Subependymoma</code></td><td><code>icdo:9383/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Supratentorial Ependymoma</code></td><td><code>ncit:C186343</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Supratentorial Ependymoma, YAP1 fusion-positive</code></td><td><code>ncit:C186351</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Supratentorial Ependymoma, ZFTA fusion-positive</code></td><td><code>ncit:C186350</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
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
<tr><td><code>CNS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Post-Mortem</code></td><td><code>ncit:C94193</code></td><td></td></tr>
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
<tr><td><code>Basal Ganglia-Thalamus</code></td><td><code>ncit:C158080</code></td><td></td></tr>
<tr><td><code>Cauda Equina Spinal Cord</code></td><td><code>ncit:C12689</code></td><td></td></tr>
<tr><td><code>Cerebellum</code></td><td><code>ncit:C12445</code></td><td></td></tr>
<tr><td><code>Cervical Spine</code></td><td><code>ncit:C69313</code></td><td></td></tr>
<tr><td><code>Extra CNS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fourth Ventricle</code></td><td><code>ncit:C12828</code></td><td></td></tr>
<tr><td><code>Frontal Lobe</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Lateral Ventricle</code></td><td><code>ncit:C12834</code></td><td></td></tr>
<tr><td><code>Leptomeningeal</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Lumbar Spinal Cord</code></td><td><code>ncit:C12895</code></td><td></td></tr>
<tr><td><code>Medulla</code></td><td><code>ncit:C12442</code></td><td></td></tr>
<tr><td><code>Midbrain</code></td><td><code>ncit:C12510</code></td><td></td></tr>
<tr><td><code>Occipital Lobe</code></td><td><code>ncit:C12355</code></td><td></td></tr>
<tr><td><code>Optic Chiasm</code></td><td><code>ncit:C90609</code></td><td></td></tr>
<tr><td><code>Optic Nerve</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Parietal Lobe</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Pons</code></td><td><code>ncit:C12511</code></td><td></td></tr>
<tr><td><code>Suprasellar Pituitary</code></td><td><code>ncit:C95445</code></td><td></td></tr>
<tr><td><code>Temporal Lobe</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Third Ventricle</code></td><td><code>ncit:C12827</code></td><td></td></tr>
<tr><td><code>Thoracic Spinal Cord</code></td><td><code>ncit:C12894</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Biopsy Only</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Gross Total</code></td><td><code>ncit:C131672</code></td><td></td></tr>
<tr><td><code>Gross Total or Near Total Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Near Total Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Resection</code></td><td><code>ncit:C131680</code></td><td></td></tr>
<tr><td><code>Partial or Subtotal Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subtotal Resection</code></td><td><code>ncit:C131680</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-externalrefidsystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">×</button>
<h3><code>ExternalRefIdSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ClinGen</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Cytogenetics, Microarray, SNP Array</code></td><td><code>ncit:C116151</code></td><td></td></tr>
<tr><td><code>Cytogenetics, Microarray, aCGH</code></td><td><code>ncit:C18084</code></td><td></td></tr>
<tr><td><code>DNA Methylation, Array</code></td><td><code>ncit:C165222</code></td><td></td></tr>
<tr><td><code>Expression Profiling, Nanostring</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, NOS</code></td><td><code>ncit:C101293</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Single Gene (DNA)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Targeted DNA Panel</code></td><td><code>ncit:C158253</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Targeted RNA Panel</code></td><td><code>ncit:C158252</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Total RNA</code></td><td><code>ncit:C124261</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Exome</code></td><td><code>ncit:C101295</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Genome</code></td><td><code>ncit:C101294</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-genomicsourceclassenum" class="enum-modal" onclick="closeEnumModal('enum-modal-genomicsourceclassenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-genomicsourceclassenum')">×</button>
<h3><code>GenomicSourceClassEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Germline</code></td><td><code>ncit:C17666</code></td><td></td></tr>
<tr><td><code>Somatic</code></td><td><code>ncit:C18060</code></td><td></td></tr>
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
<tr><td><code>WHO CNS &gt;&gt; Grade 1</code></td><td><code>ncit:C62394</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>WHO CNS &gt;&gt; Grade 2</code></td><td><code>ncit:C62395</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>WHO CNS &gt;&gt; Grade 3</code></td><td><code>ncit:C62396</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>WHO CNS &gt;&gt; Grade 4</code></td><td><code>ncit:C62397</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hydrocephalusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hydrocephalusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hydrocephalusenum')">×</button>
<h3><code>HydrocephalusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Compressed Sulci at the Vertex</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enlarged Ventricles</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No</code></td><td><code>ncit:C49487</code></td><td></td></tr>
<tr><td><code>Papilledema</code></td><td><code>ncit:C3307</code></td><td></td></tr>
<tr><td><code>Periventriculur Edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, NOS</code></td><td><code>ncit:C49488</code></td><td></td></tr>
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

<div id="enum-modal-medicationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationenum')">×</button>
<h3><code>MedicationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abemaciclib</code></td><td><code>ncit:C97660</code></td><td></td></tr>
<tr><td><code>Akt Inhibitor MK2206</code></td><td><code>ncit:C90581</code></td><td></td></tr>
<tr><td><code>Antineoplaston A10</code></td><td><code>ncit:C1004</code></td><td></td></tr>
<tr><td><code>Antineoplaston AS2-1</code></td><td><code>ncit:C1613</code></td><td></td></tr>
<tr><td><code>Arsenic Trioxide</code></td><td><code>ncit:C1005</code></td><td></td></tr>
<tr><td><code>Atorvastatin</code></td><td><code>ncit:C61527</code></td><td></td></tr>
<tr><td><code>BXQ-350 Nanovesicle Formulation</code></td><td><code>ncit:C131491</code></td><td></td></tr>
<tr><td><code>Belinostat</code></td><td><code>ncit:C48812</code></td><td></td></tr>
<tr><td><code>Bevacizumab</code></td><td><code>rxcui:253337</code></td><td></td></tr>
<tr><td><code>Bismaleimide sulfoxide (BMSO)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bortezomib</code></td><td><code>ncit:C1851</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Cabazitaxel</code></td><td><code>ncit:C66937</code></td><td></td></tr>
<tr><td><code>Cabozantinib</code></td><td><code>ncit:C52200</code></td><td></td></tr>
<tr><td><code>Capecitabine</code></td><td><code>rxcui:194000</code></td><td></td></tr>
<tr><td><code>Carbogen</code></td><td><code>ncit:C1038</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cediranib</code></td><td><code>ncit:C80867</code></td><td></td></tr>
<tr><td><code>Celecoxib</code></td><td><code>ncit:C1728</code></td><td></td></tr>
<tr><td><code>Cetuximab</code></td><td><code>rxcui:318341</code></td><td></td></tr>
<tr><td><code>Cilengitide</code></td><td><code>ncit:C1834</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Corticorelin Acetate</code></td><td><code>ncit:C76112</code></td><td></td></tr>
<tr><td><code>Crenolanib</code></td><td><code>ncit:C64639</code></td><td></td></tr>
<tr><td><code>Crizotinib</code></td><td><code>ncit:C74061</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cyclosporine</code></td><td><code>rxcui:3008</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Dabrafenib</code></td><td><code>rxcui:1424911</code></td><td></td></tr>
<tr><td><code>Dasatinib</code></td><td><code>ncit:C38713</code></td><td></td></tr>
<tr><td><code>Dordaviprone</code></td><td><code>ncit:C113792</code></td><td></td></tr>
<tr><td><code>Doxycycline Hyclate</code></td><td><code>ncit:C29007</code></td><td></td></tr>
<tr><td><code>Erlotinib</code></td><td><code>ncit:C65530</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Everolimus</code></td><td><code>rxcui:141704</code></td><td></td></tr>
<tr><td><code>Fenofibrate</code></td><td><code>ncit:C29047</code></td><td></td></tr>
<tr><td><code>Firtecan Pegol</code></td><td><code>ncit:C70651</code></td><td></td></tr>
<tr><td><code>Gadolinium</code></td><td><code>ncit:C39765</code></td><td></td></tr>
<tr><td><code>Gefitinib</code></td><td><code>ncit:C1855</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Imatinib Mesylate</code></td><td><code>ncit:C1687</code></td><td></td></tr>
<tr><td><code>Imetelstat</code></td><td><code>ncit:C49084</code></td><td></td></tr>
<tr><td><code>Indoximod</code></td><td><code>ncit:C71535</code></td><td></td></tr>
<tr><td><code>Intron</code></td><td><code>ncit:C13249</code></td><td></td></tr>
<tr><td><code>Ipilimumab</code></td><td><code>ncit:C2654</code></td><td></td></tr>
<tr><td><code>Irinotecan</code></td><td><code>ncit:C62040</code></td><td></td></tr>
<tr><td><code>Isotretinoin</code></td><td><code>ncit:C603</code></td><td></td></tr>
<tr><td><code>Itacnosertib</code></td><td><code>ncit:C156729</code></td><td></td></tr>
<tr><td><code>Labradimil</code></td><td><code>ncit:C1606</code></td><td></td></tr>
<tr><td><code>Lapatinib</code></td><td><code>ncit:C26653</code></td><td></td></tr>
<tr><td><code>Laromustine</code></td><td><code>ncit:C2653</code></td><td></td></tr>
<tr><td><code>Larotrectinib</code></td><td><code>rxcui:2105628</code></td><td></td></tr>
<tr><td><code>Lenalidomide</code></td><td><code>ncit:C2668</code></td><td></td></tr>
<tr><td><code>Lomustine</code></td><td><code>rxcui:6466</code></td><td></td></tr>
<tr><td><code>Lonafarnib</code></td><td><code>ncit:C1829</code></td><td></td></tr>
<tr><td><code>Mebendazole</code></td><td><code>ncit:C47595</code></td><td></td></tr>
<tr><td><code>Mechlorethamine</code></td><td><code>rxcui:6674</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Metformin</code></td><td><code>ncit:C61612</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Mitoxantrone</code></td><td><code>rxcui:7005</code></td><td></td></tr>
<tr><td><code>Motexafin Gadolinium</code></td><td><code>ncit:C1881</code></td><td></td></tr>
<tr><td><code>Nimotuzumab</code></td><td><code>ncit:C2733</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>O6-Benzylguanine</code></td><td><code>ncit:C1306</code></td><td></td></tr>
<tr><td><code>Oxaliplatin</code></td><td><code>rxcui:32592</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Palbociclib</code></td><td><code>ncit:C49176</code></td><td></td></tr>
<tr><td><code>Panobinostat</code></td><td><code>ncit:C66948</code></td><td></td></tr>
<tr><td><code>Pazopanib</code></td><td><code>rxcui:714438</code></td><td></td></tr>
<tr><td><code>Pemetrexed</code></td><td><code>ncit:C61614</code></td><td></td></tr>
<tr><td><code>Perifosine</code></td><td><code>ncit:C1727</code></td><td></td></tr>
<tr><td><code>Pomalidomide</code></td><td><code>ncit:C72560</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Prexasertib</code></td><td><code>ncit:C91392</code></td><td></td></tr>
<tr><td><code>Procarbazine</code></td><td><code>rxcui:8702</code></td><td></td></tr>
<tr><td><code>Procarbazine Hydrochloride</code></td><td><code>ncit:C773</code></td><td></td></tr>
<tr><td><code>Pseudomonas Exotoxin Immunoconjugate</code></td><td><code>ncit:C78532</code></td><td></td></tr>
<tr><td><code>Rebeccamycin</code></td><td><code>ncit:C1213</code></td><td></td></tr>
<tr><td><code>Recombinant Human Hyaluronidase and Pembrolizumab</code></td><td><code>ncit:C200181</code></td><td></td></tr>
<tr><td><code>Ribociclib</code></td><td><code>rxcui:1873986</code></td><td></td></tr>
<tr><td><code>Ridaforolimus</code></td><td><code>ncit:C49061</code></td><td></td></tr>
<tr><td><code>Satraplatin</code></td><td><code>ncit:C1493</code></td><td></td></tr>
<tr><td><code>Savolitinib</code></td><td><code>ncit:C104732</code></td><td></td></tr>
<tr><td><code>Semaxanib</code></td><td><code>ncit:C11778</code></td><td></td></tr>
<tr><td><code>Sirolimus</code></td><td><code>rxcui:35302</code></td><td></td></tr>
<tr><td><code>Sodium Phenylbutyrate</code></td><td><code>ncit:C1440</code></td><td></td></tr>
<tr><td><code>Sorafenib</code></td><td><code>ncit:C61948</code></td><td></td></tr>
<tr><td><code>Sunitinib</code></td><td><code>rxcui:357977</code></td><td></td></tr>
<tr><td><code>Tamoxifen</code></td><td><code>rxcui:10324</code></td><td></td></tr>
<tr><td><code>Temozolomide</code></td><td><code>rxcui:37776</code></td><td></td></tr>
<tr><td><code>Temsirolimus</code></td><td><code>ncit:C1244</code></td><td></td></tr>
<tr><td><code>Thalidomide</code></td><td><code>ncit:C1844</code></td><td></td></tr>
<tr><td><code>Thioguanine</code></td><td><code>ncit:C876</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>rxcui:10473</code></td><td></td></tr>
<tr><td><code>Tipifarnib</code></td><td><code>ncit:C1703</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Toxin</code></td><td><code>ncit:C894</code></td><td></td></tr>
<tr><td><code>Trametinib</code></td><td><code>ncit:C1413</code></td><td></td></tr>
<tr><td><code>Trastuzumab</code></td><td><code>rxcui:224905</code></td><td></td></tr>
<tr><td><code>Tretinoin</code></td><td><code>ncit:C900</code></td><td></td></tr>
<tr><td><code>Valproate</code></td><td><code>ncit:C181410</code></td><td></td></tr>
<tr><td><code>Valproic Acid</code></td><td><code>ncit:C29536</code></td><td></td></tr>
<tr><td><code>Vandetanib</code></td><td><code>ncit:C2737</code></td><td></td></tr>
<tr><td><code>Vinblastine</code></td><td><code>rxcui:11198</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>rxcui:39541</code></td><td></td></tr>
<tr><td><code>Vismodegib</code></td><td><code>ncit:C933</code></td><td></td></tr>
<tr><td><code>Vorinostat</code></td><td><code>ncit:C74038</code></td><td></td></tr>
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

<div id="enum-modal-mrisequenceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mrisequenceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mrisequenceenum')">×</button>
<h3><code>MriSequenceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diffusion Weighted Imaging</code></td><td><code>ncit:C111116</code></td><td></td></tr>
<tr><td><code>FLAIR</code></td><td><code>ncit:C82392</code></td><td></td></tr>
<tr><td><code>MRI T1 with Gadolinium</code></td><td><code>ncit:C180728</code></td><td></td></tr>
<tr><td><code>MRI T2</code></td><td><code>ncit:C180729</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-neurologicalstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-neurologicalstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-neurologicalstatusenum')">×</button>
<h3><code>NeurologicalStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Deterioration</code></td><td><code>ncit:C25751</code></td><td></td></tr>
<tr><td><code>Improved</code></td><td><code>ncit:C125459</code></td><td></td></tr>
<tr><td><code>Stable</code></td><td><code>ncit:C30103</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-nonprotocolreasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-nonprotocolreasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-nonprotocolreasonenum')">×</button>
<h3><code>NonProtocolReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Prevention of Adverse Event</code></td><td><code>ncit:C185654</code></td><td></td></tr>
<tr><td><code>Stem Cell Mobilization</code></td><td><code>ncit:C62604</code></td><td></td></tr>
<tr><td><code>Treatment for Adverse Event</code></td><td><code>ncit:C88082</code></td><td></td></tr>
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

<div id="enum-modal-outcomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-outcomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-outcomeenum')">×</button>
<h3><code>OutcomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Indeterminate</code></td><td><code>ncit:C48658</code></td><td></td></tr>
<tr><td><code>Non-Viable Tumor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Viable Tumor</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Basal Ganglia-Thalamus</code></td><td><code>ncit:C158080</code></td><td></td></tr>
<tr><td><code>Cauda Equina Spinal Cord</code></td><td><code>ncit:C12689</code></td><td></td></tr>
<tr><td><code>Cerebellum</code></td><td><code>ncit:C12445</code></td><td></td></tr>
<tr><td><code>Cervical Spine</code></td><td><code>ncit:C69313</code></td><td></td></tr>
<tr><td><code>Extra CNS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fourth Ventricle</code></td><td><code>ncit:C12828</code></td><td></td></tr>
<tr><td><code>Frontal Lobe</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Lateral Ventricle</code></td><td><code>ncit:C12834</code></td><td></td></tr>
<tr><td><code>Leptomeningeal</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Lumbar Spinal Cord</code></td><td><code>ncit:C12895</code></td><td></td></tr>
<tr><td><code>Medulla</code></td><td><code>ncit:C12442</code></td><td></td></tr>
<tr><td><code>Midbrain</code></td><td><code>ncit:C12510</code></td><td></td></tr>
<tr><td><code>Occipital Lobe</code></td><td><code>ncit:C12355</code></td><td></td></tr>
<tr><td><code>Optic Chiasm</code></td><td><code>ncit:C90609</code></td><td></td></tr>
<tr><td><code>Optic Nerve</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Parietal Lobe</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Pons</code></td><td><code>ncit:C12511</code></td><td></td></tr>
<tr><td><code>Suprasellar Pituitary</code></td><td><code>ncit:C95445</code></td><td></td></tr>
<tr><td><code>Temporal Lobe</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Third Ventricle</code></td><td><code>ncit:C12827</code></td><td></td></tr>
<tr><td><code>Thoracic Spinal Cord</code></td><td><code>ncit:C12894</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Disease Progression</code></td><td><code>ncit:C17747</code></td><td></td></tr>
<tr><td><code>Failure to Attain Remission</code></td><td><code>ncit:C178072</code></td><td></td></tr>
<tr><td><code>Ineligible</code></td><td><code>ncit:C40412</code></td><td></td></tr>
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
<tr><td><code>Study Discontinuation</code></td><td><code>ncit:C142444</code></td><td></td></tr>
<tr><td><code>Subject Non-Compliance</code></td><td><code>ncit:C91752</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Withdrawal of Consent</code></td><td><code>ncit:C48271</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Non-Target Lesions</code></td><td><code>ncit:C94535</code></td><td></td></tr>
<tr><td><code>Overall Response</code></td><td><code>ncit:C96613</code></td><td></td></tr>
<tr><td><code>Target Lesions</code></td><td><code>ncit:C94534</code></td><td></td></tr>
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
<tr><td><code>Modified MacDonald &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified MacDonald &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified MacDonald &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Macdonald &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Evaluable</code></td><td><code>ncit:C62222</code></td><td></td></tr>
<tr><td><code>RANO &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RANO &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RANO &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RANO &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAPNO &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAPNO &gt;&gt; Major Response</code></td><td><code></code></td><td>(cns_v1.2approved) ConsortiumNote: Only use for RAPNO low-grade gliomas</td></tr>
<tr><td><code>RAPNO &gt;&gt; Minor Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAPNO &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAPNO &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Major Response</code></td><td><code>ncit:C123590</code></td><td>(cns) ConsortiumNote: Only use for RAPNO low-grade gliomas</td></tr>
<tr><td><code>System NOS &gt;&gt; Minor Response</code></td><td><code>ncit:C123598</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Partial Response</code></td><td><code>ncit:C18058</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stable Disease</code></td><td><code>ncit:C18213</code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>iRANO &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>iRANO &gt;&gt; Minor Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>iRANO &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>iRANO &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>iRANO &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Biopsy</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Cytology</code></td><td><code>ncit:C16491</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Physical Examination</code></td><td><code>ncit:C20989</code></td><td></td></tr>
<tr><td><code>Surgical Resection</code></td><td><code>ncit:C158758</code></td><td></td></tr>
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
<tr><td><code>Modified MacDonald</code></td><td><code>ncit:C198862</code></td><td></td></tr>
<tr><td><code>RANO</code></td><td><code>ncit:C114879</code></td><td></td></tr>
<tr><td><code>RAPNO</code></td><td><code>ncit:C198863</code></td><td></td></tr>
<tr><td><code>WHO</code></td><td><code>ncit:C75419</code></td><td></td></tr>
<tr><td><code>iRANO</code></td><td><code>ncit:C131131</code></td><td></td></tr>
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

<div id="enum-modal-routeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-routeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-routeenum')">×</button>
<h3><code>RouteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Intraarterial</code></td><td><code>ncit:C38222</code></td><td></td></tr>
<tr><td><code>Intracerebral, Convection-Enhanced Delivery</code></td><td><code>ncit:C116566</code></td><td></td></tr>
<tr><td><code>Intrathecal</code></td><td><code>ncit:C173292</code></td><td></td></tr>
<tr><td><code>Systemic</code></td><td><code>ncit:C173291</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-rtdatasourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-rtdatasourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-rtdatasourceenum')">×</button>
<h3><code>RtDataSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Protocol Prescribed</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Treatment Summary</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-rtmarginsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-rtmarginsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-rtmarginsenum')">×</button>
<h3><code>RtMarginsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>0.5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>1 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>2 cm</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Craniospinal</code></td><td><code>ncit:C84352</code></td><td></td></tr>
<tr><td><code>Exact Volume Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Focal</code></td><td><code>ncit:C28224</code></td><td></td></tr>
<tr><td><code>Posterior Fossa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tumor Bed Plus Margin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Whole Brain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Whole Spinal Cord</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Whole Ventricle</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Whole Ventricular With Spine</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Modified Chang Staging &gt;&gt; M+</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M0</code></td><td><code>ncit:C48699</code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M0 / M1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M1</code></td><td><code>ncit:C48700</code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M4</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Modified Chang Staging</code></td><td><code>ncit:C198826</code></td><td></td></tr>
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
<tr><td><code>02-294 DFCI</code></td><td><code></code></td><td></td></tr>
<tr><td><code>10-C-0219</code></td><td><code></code></td><td></td></tr>
<tr><td><code>11-C-0161</code></td><td><code></code></td><td></td></tr>
<tr><td><code>15-C-0093</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3961</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3973</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A9952</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML03P1</code></td><td><code>ncit:C168936</code></td><td></td></tr>
<tr><td><code>AAML0531</code></td><td><code>ncit:C168937</code></td><td></td></tr>
<tr><td><code>ACNS0121</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0122</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0126</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0222</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0223</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0224</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0232</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0333</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0334</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0423</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0621</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0821</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0927</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1021</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1022</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1123</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1221</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1422</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1721</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1723</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1821</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1831</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1833</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1931</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS2021</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0012</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0414</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0416</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0515</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0612</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0815</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0819</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0912</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1111</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1112</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1217</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1312</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1411</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1414</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1513</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1514</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1515</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1615</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1622</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1711</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS0031</code></td><td><code>ncit:C174970</code></td><td></td></tr>
<tr><td><code>AEWS1031</code></td><td><code>ncit:C174971</code></td><td></td></tr>
<tr><td><code>AFLACST1501</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AG881-C-004</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT0132</code></td><td><code>ncit:C177343</code></td><td></td></tr>
<tr><td><code>AGCT1531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1532</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AIEOP EP II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0532</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL09P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL12P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL0131</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL01P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AREN1921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0321</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ad-RTS-hIL-12</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Antineoplaston Therapy protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BIOMEDE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-01</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-02</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-03</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRF116013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BXQ-350 AD</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Baby POG-1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CA209908</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-9921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-9942</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-99701</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-99703</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9952</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9961</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-D9803</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-P9970</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG09712</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG945</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG9941</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG99703</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-RMS-2005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCMC1411</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDRB436G2201</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CERN-08-01</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHMC-6006</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP455</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP693</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP719</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP735</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CLEE011XUS17T</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CNS1100</code></td><td><code></code></td><td></td></tr>
<tr><td><code>COG A09712</code></td><td><code></code></td><td></td></tr>
<tr><td><code>COJEC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CONNECT 1701</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CONNECT 1702</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CONNECT1701</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CONNECT1702</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2009</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ChildrenHLA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DART Clinical Trial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DFMO</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DIPG-BATS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ECREST study</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ETMR One</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EZH-102</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EZH-202</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GemPOx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HERBY</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HGG-01</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HGG-BAT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HIT-GBM-C</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HIT-HGG-2013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HIT-SIOP PNET 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HSPPC-96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HUMC 1612</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start III</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ICE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INCB7839</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INDIGO</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS-III</code></td><td><code></code></td><td></td></tr>
<tr><td><code>JET Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LGG 14C03</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK162</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEMMAT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>METRICS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MIN-001P-1501</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSKCC 09-014</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSKCC 11-011</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSKCC-03077</code></td><td><code></code></td><td></td></tr>
<tr><td><code>N2012-01</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI 02-C-0193</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01185964</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01222754</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01502917</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT02924038</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT03696355</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT04196413</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT04264143</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NF105</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NF106</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NMTRC V0706</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NMTRC009</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC028</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-063</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-075</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-077</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC 029</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC-029</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC-039</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC-50</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC001</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC004</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC0056</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC006</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC007</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC014</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC016</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC017</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC018</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC020</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC021</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC023</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC024</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC025</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC026</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC027</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC030</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC031</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC033</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC042</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC043</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC045</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC047</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC048</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC049</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC050</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC051</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC053</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC056</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PEDSCCT6005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PEG-Intron</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNET 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC001</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0015</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0016</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0018</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC002</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0022</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC0023</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC003</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC007</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC008</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC009</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC010</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC014</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC015</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC016</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC023</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC026</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC027</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POE08-01</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG 9239</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG 9631</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG 9836</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG 9879</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-9905</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-P9934</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9048</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PRO13110086</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pittsburgh Vaccine Trial Cycle</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Protocol BT-55</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R115777-INT-11</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAD001</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REMATCH</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REMIND</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Re-MATCH</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC006</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC031</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC037</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC-9006</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC9005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SCH52365</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SDT-201</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SEL-TH-1601</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP LGG 2004</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-CNS-GCT-96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-LGG-2004</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-PNET-4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJBG07</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJDAWN</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJHG12</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJHG98</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB-96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB03</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJPDGF</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJREFU</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJYC07</code></td><td><code></code></td><td></td></tr>
<tr><td><code>STRIvE-02</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SU5416</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Study # 2014-0135</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stupp Protocol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TB-403</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TK216</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TOPNOC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TOPNOC-001</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TOTEM</code></td><td><code></code></td><td></td></tr>
<tr><td><code>VINILO study</code></td><td><code></code></td><td></td></tr>
<tr><td><code>VITAC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>VOIT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>VP-16</code></td><td><code></code></td><td></td></tr>
<tr><td><code>YMB 1000 013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ZD-1839</code></td><td><code></code></td><td></td></tr>
<tr><td><code>rHSC-DIPGVax</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>11-C-0161:Arm 1 (AZD6244)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>11-C-0161:Arm 2 (AZD6244)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>15-C-0093:Phase I (Turalio)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>15-C-0093:Phase II (Turalio)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3973:Arm I (unpurged PBSC collection) (carboplatin, cisplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, isotretinoin, melphalan, topotecan hydrochloride, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3973:Arm II (unpurged PBSC collection) (carboplatin, cisplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, isotretinoin, melphalan, topotecan hydrochloride, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group 0 Induction Therapy (Cytarabine, Daunorubicin Hydrochloride, Methotrexate, Pegaspargase, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group 1 Arm IV (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Mercaptopurine, Methotrexate, Nelarabine, Pegaspargase,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm I (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Leucovorin Calcium, Mercaptopurine, Methotrexate, Pegaspargase, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm I (Delayed intensification chemotherapy (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm I (Interim maintenance chemotherapy) (Leucovorin Calcium, Methotrexate, Pegaspargase, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm I (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm II (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Mercaptopurine, Methotrexate, Nelarabine, Pegaspargase, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm II (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Nelarabine, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm II (Interim maintenance chemotherapy) (Asparaginase, Methotrexate, Pegaspargase, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm II (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Nelarabine, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm III (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Leucovorin Calcium, Mercaptopurine, Methotrexate, Pegaspargase, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm III (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm III (Interim maintenance chemotherapy) (Leucovorin Calcium, Mercaptopurine, Methotrexate, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm III (Maintenance chemotherapy) (Methotrexate, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm IV (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Methotrexate, Nelarabine, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm IV (Interim maintenance chemotherapy) (Leucovorin Calcium, Mercaptopurine, Methotrexate, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434:Group I Arm IV (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Nelarabine, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:Arm A (SR-Avg control) (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisone, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:Arm B (SR-Avg experimental) (Asparaginase Erwinia chrysanthemi, Blinatumomab, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:Arm C (SR-High Control) (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:Arm D (SR-High experimental) (Asparaginase Erwinia chrysanthemi, Blinatumomab, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:B-LLy (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:DS B-ALL (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL1731:NCI SR or HR DS B-ALL (Asparaginase Erwinia chrysanthemi, Blinatumomab, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML03P1:N/A (asparaginase, busulfan, cyclophosphamide, cyclosporine, cytarabine, daunorubicin hydrochloride, etoposide, gemtuzumab ozogamicin, methotrexate, mitoxantrone hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm A: Standard Arm - No GMTZ, AML Patients with Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, mitoxantrone hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm A: Standard Arm - No GMTZ, AML Pts w/out Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, mitoxantrone hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML0531:Arm B: Experimental - with GMTZ, AML Pts w/out Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, gemtuzumab ozogamicin, gemtuzumab ozogamicin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0121:GTR (radiation only)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0121:GTR Supratentorial Differentiated (observation)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0121:STR (interim chemotherapy/second look surgery) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0122:Induction and Consolidation (High dose chemotherapy) (carboplatin, etoposide, ifosfamide, Thiotepa)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0122:Induction only (No high-dose therapy) (carboplatin, etoposide, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0232:Regimen A (Radiotherapy Alone)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0232:Regimen B (Cycles 1 and 2 only) (Carboplatin, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0232:Regimen B (MRD/PR/SD = 4 cycles) (Carboplatin, Etoposide, Cisplatin, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm I (3-7 years of age, LDCSI, IFRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm I (3-7 years of age, LDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm II (3-7 years of age, LDCSI, PFRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm II (3-7 years of age, LDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm III (3-7 years of age, SDCSI, IFRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm III (3-7 years of age, SDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm IV (3-7 years of age, SDCSI, PFRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm IV (3-7 years of age, SDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm V (8-21 years of age, SDCSI, IFRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm V (8-21 years of age, SDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm VI (8-21 years of age, SDCSI, PFRT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0331:Arm VI (8-21 years of age, SDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Arm A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Arm B (Carboplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Arm C (Isotretinoin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Arm D (Carboplatin and Isotretinoin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Regimen A (no carboplatin, no isotretinoin) (Cisplatin, Cyclophosphamide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Regimen B (carboplatin, no isotretinoin) (Carboplatin, Cisplatin, Cyclophosphamide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Regimen C (no carboplatin, isotretinoin) (Cisplatin, Cyclophosphamide, Vincristine, Isotretinoin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0332:Regimen D (carboplatin, isotretinoin) (Carboplatin, Cisplatin, Cyclophosphamide, Vincristine, Isotretinoin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0333:Arm I (Chemotherapy, Autologous PBSC, 3D-CRT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0333:Arm I (chemotherapy, autologous PBSC, 3D-CRT) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Filgrastim, Leucovorin Calcium, Methotrexate, Thiotepa, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0333:Arm II (Chemotherapy, 3D-CRT, Autologous PBSC)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0333:Arm II (chemotherapy, 3D-CRT, autologous PBSC) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Filgrastim, Leucovorin Calcium, Methotrexate, Thiotepa, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0334:Arm A (Induction+Consolidation Chemotherapy, Autologous PBSC)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0334:Arm B (Induction+Consolidation Chemotherapy, Autologous PBSC)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0334:Regimen A (Cisplatin, Cyclophosphamide, Vincristine, Etoposide, Carboplatin, Thiotepa, ASCR)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0334:Regimen B (Methotrexate, Cisplatin, Cyclophosphamide, Vincristine, Etoposide, Carboplatin, Thiotepa, ASCR)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0821:TEMO+IRIN (Temozolomide, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0821:TEMO+IRIN+BEVA (Temozolomide, Irinotecan, Bevacizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Arm I (Vorinostat) (Vorinostat, Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Arm II (Temozolomide) (Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Arm III (Bevacizumab) (Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Arm IV (temozolomide) (Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Arm V (vorinostat/bevacizumab (Vorinostat, Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0822:Feasibility (vorinostat) (Vorinostat, Bevacizumab, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:Arm I (radiotherapy, chemotherapy) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:Arm II (radiotherapy, chemotherapy) (Vincristine, Cyclophosphamide, Etoposide, Cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:Arm III (radiotherapy, observation)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:GTR (Randomized to Maintenance Chemotherapy) (Vincristine, Cisplatin, Cyclophosphamide, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:GTR (Randomized to No Chemotherapy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:STR (Induction only) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS0831:STR Differentiated (observation)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1022:Arm I (low-dose lenalidomide) (Lenalidomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1022:Arm II (high-dose lenalidomide) (Lenalidomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1123:Stratum 1 (NGGCT) (carboplatin, etoposide, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1123:Stratum 2 (Germinoma) (carboplatin, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1831:Arm 1 (Carboplatin, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1831:Arm 2 (Selumetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1833:Arm 1 (Carboplatin, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1833:Arm 2 (Selumetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1931:Active Comparator: Efficacy Phase Arm II (selumetinib) (Selumetinib Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS1931:Experimental: Feasibility &amp; Efficacy Phase Arm I (selumetinib, vinblastine) (Selumetinib, Vinblastine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS2021:Plan A (WVSCI - whole ventricular and spinal canal radiation) (Carboplatin, Etoposide, Ifosfamide, Mesna)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS2021:Plan B (HDCSCR- high dose chemotherapy with stem cell rescue) (Carboplatin, Etoposide, Ifosfamide, Mesna, Thiotepa)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0416:ARM I (vorinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0416:ARM II (vorinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0416:ARM III (vorinostat, isotretinoin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0612:PART A (sunitinib malate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0612:PART B (sunitinib malate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm I (neuroblastoma- measurable) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm II (Neuroblastoma- MIBG evaluable) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm III (rhabdomyosarcoma) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm IV (osteosarcoma) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm IX (Wilms tumor) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm V (Ewing sarcoma/peripheral PNET) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm VI (non-RMS soft tissue sarcoma) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm VII (hepatoblastoma) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm VIII (malignant germ cell tumor) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm X (acute lymphoblastic leukemia) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm XI (acute myelogenous leukemia) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921:Arm XII (rhabdoid malignancy) (Alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1411:Phase 1 (talazoparib, temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1411:Phase 2 (talazoparib, temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS0031:Regimen A (cyclophosphamide, doxorubicin hydrochloride, etoposide, ifosfamide, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS0031:Regimen B (cyclophosphamide, doxorubicin hydrochloride, etoposide, ifosfamide, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS1031:Arm A (combination chemotherapy) (Cyclophosphamide, Dexrazoxane, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS1031:Arm B (combination chemotherapy, topotecan hydrochloride) (Cyclophosphamide, Dexrazoxane, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Topotecan Hydrochloride, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AG881-C-004:Experimental: Vorasidenib (Vorasidenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AG881-C-004:Placebo Comparator: Matching Placebo (Matching Placebo)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT0132:Arm 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT0132:Arm I (cisplatin, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531:Arm I (bleomycin, carboplatin, etoposide) (Carboplatin, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531:Arm II (bleomycin, etoposide, cisplatin) (Cisplatin, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531:Arm III (bleomycin, etoposide, carboplatin) (Carboplatin, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531:Arm IV (bleomycin, etoposide, cisplatin) (Cisplatin, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531:Low-Risk (observation)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1532:Arm A: TIP (paclitaxel, ifosfamide, cisplatin, pegylated G-CSF, G-CSF)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1532:Arm B: TI-CE (paclitaxel, ifosfamide, pegylated G-CSF, G-CSF, carboplatin, etoposide phosphate,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531:Group 2 (chemotherapy, surgery) (carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531:Group 3 (chemotherapy, surgery) (carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531:Group 4 (chemotherapy, surgery, antineoplastic therapy) (Isotretinoin, carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531:Non-intermediate risk enrolled on intermediate risk trial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0532:Consolidation Arm A: single myeloablative consolidation (Carboplatin, Cisplatin, Cyclophosphamide, Doxorubicin Hydrochloride, Etoposide, Filgrastim, Isotretinoin, Melphalan, Topotecan Hydrochloride, Vincristine Sulfate Liposome)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0532:Consolidation Arm B: tandem myeloablative consolidation (Carboplatin, Cisplatin, Cyclophosphamide, Doxorubicin Hydrochloride, Etoposide, Filgrastim, Isotretinoin, Melphalan, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate Liposome)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531:Arm A (chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531:Arm B (Iobenguane I-131, chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531:Arm C (Iobenguane I-131, chemotherapy, BuMel, HSCT, EBRT) (Busulfan, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Melphalan Hydrochloride, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531:Arm D (chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531:Arm E (crizotinib, chemotherapy, HSCT, EBRT) (Crizotinib, Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL0131:Experimental: Consolidation with Vinblastine (doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL0131:Standard APO with Vincristine (Arm I) (doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL01P1:Group B (chemotherapy, protective therapy, monoclonal antib.) (doxorubicin hydrochloride, cyclophosphamide, methotrexate, rasburicase, leucovorin calcium, prednisone, methylprednisolone, cytarabine, vincristine sulfate, hydrocortisone sodium succinate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANHL01P1:Group C (Chemotherapy, monoclonal antibody therapy) (doxorubicin hydrochloride, cyclophosphamide, methotrexate, leucovorin calcium, prednisone, methylprednisolone, cytarabine, etoposide, vincristine sulfate, hydrocortisone sodium succinate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST0331:Maintenance therapy group 1 arm I (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST0331:Maintenance therapy group 1 arm II (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST0331:Maintenance therapy group 2 arm I (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST0331:Maintenance therapy group 2 arm II (Cisplatin, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotcol M (HRAS gene alterations) (Tipifarnib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol A (NTRK1, NTRK2, or NTRK3 gene fusion) (Larotrectinib Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol B (FGFR1, FGFR2, FGFR3, or FGFR4 gene mutation) (Erdafitinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol C (EZH2, SMARCB1, or SMARCA4 gene mutation) (Tazemetostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol D (TSC1, TSC2, or PI3K/mTOR gene mutation) (Samotolisib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol E (activating MAPK pathway gene mutation) (Selumetinib Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol F (ALK or ROS1 gene alteration) (Ensartinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol G (BRAF V600 gene mutation) (Vemurafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol H (ATM, BRCA1, BRCA2, RAD51C, RAD51D mutations) (Olaparib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol I (Rb positive, alterations in cell cycle genes) (Palbociclib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol J (MAPK pathway mutations) (Ulixertinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621:Subprotocol N (activating RET mutations) (Selpercatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AREN1921:Arm I (Regimen UH-3) (Carboplatin, Cyclophosphamide, Doxorubicin, Etoposide, Irinotecan, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AREN1921:Arm II (Regimen ICE/Cyclo/Topo) (Carboplatin, Cyclophosphamide, Etoposide, Ifosfamide, Topotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0321:Treatment (chemotherapy, radiotherapy, autologous SCI) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Thiotepa, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531:Arm I (chemotherapy, radiotherapy) (Cyclophosphamide, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531:Arm II (chemotherapy, radiotherapy) (Cyclophosphamide, Irinotecan Hydrochloride, Vincristine Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-01:Arm A (tumor cavity delivery) (HER2-specific chimeric antigen receptor (CAR) T cell)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-01:Arm B (intraventricular delivery) (HER2-specific chimeric antigen receptor (CAR) T cell)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-02:Arm A (tumor cavity delivery) (EGFR806-specific chimeric antigen receptor (CAR) T cell)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-02:Arm B (intraventricular delivery) (EGFR806-specific chimeric antigen receptor (CAR) T cell)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-03:Arm A (tumor cavity delivery) (CAR-T cell targeting B7H3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-03:Arm B (intraventricular delivery) (CAR-T cell targeting B7H3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAINCHILD-03:Arm C (DIPG, intraventricular delivery) (CAR-T cell targeting B7H3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRF116013: (Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-921:Regimen A (VCR, lomustine, prednisone)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-921:Regimen B (VCR, methylprednisone, lomustine, hydroxyurea, procarbazine, cisplatin, cyclophosphamide, cytarabine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-9921:Regimen A (vincristine, cisplatin, cyclophosphamide, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-9921:Regimen B (vincristine, carboplatin, ifosfamide, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-99701:Regimen A (carboplatin, vincristine, cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-99701:Regimen B (carboplatin, vincristine, cyclophosphamide, cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:A0 (localized disease Stg I/II) Modified CCG BFM (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:A1 (Disseminated, No CNS - CCG mod BFM w/out intens (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:A2 (Disseminated, No CNS - CCG mod BFM w/ intens (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:B1 (Disseminated CNS- &lt;Amend 7B) NHL/BFM-95 w/out intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:B1 (Disseminated CNS-) NHL/BFM-95 w/out intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:B2 (CNS+) NHL/BFM-95 w/intens delayed radiation therapy (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A5971:B2 (Disseminated,CNS- (&lt; Amend 7B)) NHL/BFM-95 w/intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9952:Regimen A (CV Chemotherapy) (carboplatin, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9952:Regimen B (TPCV Chemotherapy) (lomustine, procarbazine hydrochloride, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9961:Regimen A (cisplatin, lomustine, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-A9961:Regimen B (cisplatin, cyclophosphamide, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-D9803:Arm I (dactinomycin, vincristine sulfate, cyclophosphamide,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCG-D9803:Arm II (vincristine sulfate, cyclophosphamide, topotecan hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005:Group 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005:Group 2 (ifosfamide , IFO-DOX)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005:Group 3 (IFO-DOX)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005:Group 4 (IFO-DOX, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-NRSTS-2005:Group 5 (IFO-DOX)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCLG-EPSSG-RMS-2005: ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCMC1411:High-grade Glioma/Pontine Glioma (Mebendazole, Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CCMC1411:Low-grade Glioma (Mebendazole, Vincristine, Carboplatin, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDRB436G2201:HGG cohort: Dabrafenib and trametinib (dabrafenib, Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDRB436G2201:LGG cohort: Carboplatin with vincristine (Carboplatin, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDRB436G2201:LGG cohort: Dabrafenib and trametinib (dabrafenib, Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP735:Consolidation (Thiotepa, Etoposide, Carboplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHP735:Induction (Methrotrexate, Vincristine, Etoposide, Cyclophosphamide, Cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CNS1100:Experimental (Busulfan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2000:Carboplatin + Etoposide + Vincristine (Carboplatin, Etoposide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2000:Cyclophosphamide + Etoposide + Vincristine (Cyclophosphamide, Etoposide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2009:Doxorubicin/cisplatin arm (2) (Carboplatin, Cisplatin, Cyclophosphamide, Dactinomycin, Doxorubicin, Etoposide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2009:Methotrexate Arm (3) (Carboplatin, cyclophosphamide, etoposide, Leucovorin, Methotrexate, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2009:Standard Arm (1) (Carboplatin, Cyclophosphamide, etoposide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPT-SIOP-2009:Temozolomide Irinotecan arm (4) (Carboplatin, Cyclophosphamide, Etoposide, Irinotecan, Temozolomide, Vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ChildrenHLA:Phase 1 (MEK162)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ChildrenHLA:Phase 2 (MEK162)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ChildrenHLA:Target Validation (MEK162)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DIPG-BATS:radiation + bevacizumab (Bevacizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DIPG-BATS:radiation + bevacizumab + erlotinib (Bevacizumab, Erlotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DIPG-BATS:radiation + bevacizumab + erlotinib + temozolomide (Bevacizumab, erlotinib, temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DIPG-BATS:radiation + bevacizumab + temozolomide (Bevacizumab, Temozolomide,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EZH-102:Open-label Tazemetostat (Tazemetostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EZH-202:Open-label Tazemetostat (Tazemetostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949:Core Regimen, sub-cohort A (indoximod with oral temozolomide) (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949:Core Regimen, sub-cohort B (low-dose radiation or not all disease sites included, indoximod with oral temozolomide) (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949:Core Regimen, sub-cohort C (palliative full-dose radiation, (indoximod with oral temozolomide)) (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949:Salvage Regimen 1 (Cross-over to indoximod with oral metronomic cyclophosphamide and etoposide) (Indoximod, Cyclophosphamide, Etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GCC1949:Salvage Regimen 2 (Cross-over to indoximod with oral lomustine and temozolomide) (Indoximod, Temozolomide, Lomustine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HGG-01:Active Comparator: Main Cohort: Chemoradiation + TMZ (Temozolomide (TMZ))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HGG-01:Experimental: Bevacizumab + TMZ Young Patient Cohort (YPC) (Bevacizumab, Temozolomide (TMZ))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HGG-01:Experimental: Main Cohort: Chemoradiation + Bevacizumab + TMZ (Bevacizumab, Temozolomide (TMZ))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HIT-SIOP PNET 4: Hyperfractionated radiotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HIT-SIOP PNET 4: Standard Fractionation Regimen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HSPPC-96:Newly Diagnosed High Grade Glioma (HGG)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HSPPC-96:Recurrent HGG and Ependymoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start 4:Induction (vincristine, cisplatin, cyclophosphamide, etoposide, high-dose methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start 4:Single Cycle Intensive Chemotherapy (Carboplatin, thiotepa, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start 4:Tandem 3 Cycle Intensive Chemotherapy (Carboplatin, thiotepa)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start II:Submyeloablative/consolidation chemotherapy (Carboplatin, thiotepa, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start II:induction (vincristine, cisplatin, cyclophosphamide, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start III:induction (vincristine, cisplatin, cyclophosphamide, etoposide, and high dose methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head Start III:myeloablative chemotherapy (thiotepa, carboplatin and etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INDIGO:Experimental: Vorasidenib (Vorasidenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INDIGO:Placebo Comparator: Matching Placebo (Matching Placebo)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS-III:Group 1 (vincristine (V), dactinomycin (A), cyclophosphamide (C) or standard VA)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS-III:Group 2 (intensive VA or repetitive-pulse VAC)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS-III:Group 3 (repetitive-pulse VAC or repetitivepulse VAdrC-VAC (Adr, Adriamycin [doxorubicin]))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 1 dose escalation: Dose expansion (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 1 dose escalation: Dose level 1_Cohort 1 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 1 dose escalation: Dose level 2_Cohort 2 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 1 dose escalation: Dose level 3_Cohort 3 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 2 expansion: Other extra-cranial solid tumors_Cohort 2 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 2 expansion: Patients with tumors bearing NTRK fusions (IFS)_Cohort 1 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 2 expansion: Primary CNS tumors_Cohort 3 (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LOXO-TRK 15003:Phase 2 expansion: bone health assessment_sub-cohort (Larotrectinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part A - TMT 0.0125 mg/kg/day (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part A - TMT 0.025 mg/kg/day (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part A - TMT 0.032 mg/kg/day (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part A - TMT 0.04 mg/kg/day (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part B - BRAF V600 mutant solid tumor (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part B - LGG fusion (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part B - NF-1 with PN (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part B - Neuroblastoma (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part C - TMT 0.025 mg/kg/day + 100% DRB RP2D (Trametinib, Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part C - TMT 0.025 mg/kg/day + 50% DRB RP2D (Trametinib, Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part C - TMT 0.032 mg/kg/day + 100% DRB RP2D (Trametinib, Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part D - LCH (Trametinib, Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEK116540:Part D - LGG (Trametinib, Dabrafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:MEL: Pembrolizumab 10 mg/kg Q2W (Part B) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:MEL: Pembrolizumab 10 mg/kg Q3W (Parts B+D) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:MEL: Pembrolizumab 2 mg/kg Q3W (Parts B+D) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q2W (Part F) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q3W (Parts C+F) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 2 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 2 mg/kg Q3W (Part F) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:NSCLC: Pembrolizumab 5 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab 1 mg/kg Q2W (Part A) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab 10 mg/kg Q2W (Parts A+A1) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab 3 mg/kg Q2W (Part A) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 1 Q3W (Part A2) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 2 Q3W (Part A2) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 3 Q3W (Part A2) (Pembrolizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSKCC-03077:patients have no evidence of disease (anti-GD2 murine IgG3 monoclonal antibody 3F8)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSKCC-03077:patients have refractory bone marrow disease (anti-GD2 murine IgG3 monoclonal antibody 3F8)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol A (EGFR activating mutation) (Afatinib, Afatinib Dimaleate,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol B (HER2 activating mutation) (Afatinib, Afatinib Dimaleate,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol C1 (MET amplification) (Crizotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol C2 (MET exon 14 deletion/mutation) (Crizotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol E (EGFR T790M or rare activating mutation) (Osimertinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol F (ALK translocation) (Crizotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol G (ROS1 translocation or inversion) (Crizotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol H (BRAF V600E/R/K/D mutation) (Dabrafenib, Dabrafenib Mesylate, Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol I (PIK3CA mutation) (Taselisib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol J (HER2 amplification &gt;= 7 copy numbers</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol K1 (FGFR amplification) (Erdafitinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol K2 (FGFR mutation or fusion) (Erdafitinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol L (mTOR mutation) (Sapanisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol M (TSC1 or TSC2 mutation) (Sapanisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol N (PTEN mutation or deletion and PTEN expression) (PI3K-beta Inhibitor GSK2636771)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol P (PTEN loss) (PI3K-beta Inhibitor GSK2636771)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Q (HER2 amplification) (Trastuzumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol R (BRAF fusion or BRAF non-V600 mutation) (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol S1 (NF1 mutation) (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol S2 (GNAQ or GNA11 mutation) (Trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol T (SMO or PTCH1 mutation) (Vismodegib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol U (NF2 inactivating mutation) (Defactinib, Defactinib,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol V (cKIT exon 9, 11, 13, or 14 mutation) (Sunitinib Malate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol W (FGFR pathway aberrations) (FGFR Inhibitor AZD4547)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol X (DDR2 S768R, I638F, or L239R mutation) (Dasatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Y (Akt mutation) (Capivasertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1A (NRAS mutation in codon 12, 13, or 61) (Binimetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1B (CCND1, 2, or 3 amplification with Rb by IHC) (Palbociclib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1C (CDK4 or CDK6 amplification and Rb protein) (Palbociclib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1D (Loss of MLH1 or MSH2 by IHC) (Nivolumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1E (NTRK1, NTRK2 or NTRK3 gene fusion) (Larotrectinib, Larotrectinib Sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1F (PIK3CA mutation) (Copanlisib, Copanlisib Hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1G (PTEN loss) (Copanlisib, Copanlisib Hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1H (PTEN mutation) (Copanlisib, Copanlisib Hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1I (BRCA1 or BRCA2 gene mutation) (Adavosertib, Irinotecan Hydrochloride)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1K (AKT mutation) (Ipatasertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1L (BRAF fusion, aberration or non-V600 mutation) (Ulixertinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCI-MATCH:Subprotocol Z1M (LAG-3 expression &gt;= 1%) (Nivolumab, Relatlimab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01185964:Phase 1b: Olaratumab + doxorubicin (Doxorubicin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01185964:Phase 2: Doxorubicin: Optional Olaratumab After Progression (Doxorubicin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT01185964:Phase 2: Olaratumab and doxorubicin (Doxorubicin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT02924038:IMA950/poly-ICLC subQ only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT02924038:IMA950/poly-ICLC subcutaneous (subQ) + Varlilumab IV</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT03696355:Stratum A1 (GDC0084)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NCT03696355:Stratum A2 (GDC0084)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105:Group 1 (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105:Group 2 (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105:Group 3 (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105:Group 3b (Indoximod, Temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NLG2105:Group 4 (Indoximod, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm A (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm B (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm C (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm D (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm E (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm F (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ONC201:Arm G (ONC201)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-063:ARM A (Vinblastine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-063:ARM B (Vinblastine, Bevacizumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-077:Phase I Dose-escalation (5 Azacytidine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-077:Posterior Fossa Ependymoma Expansion Arm (5 Azacytidine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OZM-077:Recurrent Brain and Solid Tumour Expansion Arm (5 Azacytidine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC-029:Treatment (selumetinib) (Selumetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC-039:Treatment (peginterferon alfa-2b) ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC005:Stratum 1a: patients previously not treated with RT or only focal RT (Temozolomide, O-benzylguanine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC005:Stratum 1b: patients previously not treated with RT or only focal RT (Temozolomide, O-benzylguanine, G-CSF)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC005:Stratum 2a: patients with prior craniospinal irradiation or myeloblative therapy. (Temozolomide, O-benzylguanine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC005:Stratum 2b: patients with prior craniospinal irradiation or myeloblative therapy. (Temozolomide, O-benzylguanine, G-CSF)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC006:Stratum 1: newly diagnosed localized brainstem tumors (imatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC006:Stratum 2A: recurrent intracranial malignant gliomas - not using EIACD (imatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC006:Stratum 2B: recurrent intracranial malignant gliomas - using EIACD (imatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC007:Stratum 1: Newly diagnosed intrinsic brain stem glioma or incompletely resected supratentorial malignant gliomas not receiving enzyme-inducing anti-convulsant drugs (ZD1839 (Iressa™))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC007:Stratum 2: Incompletely resected supratentorial malignant gliomas receiving enzyme-inducing anticonvulsant drugs (ZD1839 (Iressa™))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC016:Stratum 1: those who are not receiving steroids (Lapatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC016:Stratum 2: those who are receiving steroids (Lapatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022:Stratum A: Recurrent, progressive or refractory high-grade gliomas (Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022:Stratum B: Recurrent, progressive or refractory Intrinsic brain stem tumors (Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022:Stratum C: Recurrent or progressive Medulloblastomas (Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022:Stratum D: Recurrent or progressive Ependymomas (Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC022:Stratum E: Recurrent low grade gliomas (Bevacizumab, Irinotecan)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC043:Treatment (pomalidomide) (Pomalidomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC047:Stratum 1 (Panobinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC047:Stratum 2 (Panobinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC048:Newly Diagnosed (Concurrent Optune/focal radiation therapy followed by Optune-only therapy) ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC048:Recurrent, Progressive or Refractory (Optune System) ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 1: BRAF V600E LGG or HGG (Dabrafenib, Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 2: BRAF fusion/duplication or NF1- associated LGG (Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 3: LGGs with V600E (Dabrafenib, Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 4: HGGs with V600E (Dabrafenib, Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 5 LGG with BRAF duplication or fusion with any partner (Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PBTC055:Stratum 6 LGG with neurofibromatosis type 1 (Trametinib, Hydroxychloroquine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC005:Stratum A (Locally recurrent ATRT/medullo (delivery into tumor bed))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC005:Stratum B (disseminated ATRT/medullo (delivery via LP x 1 dose))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC005:Stratum C (disseminated medullo (delivery via LP x 2 doses))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC007:Stratum A- DIPG treated with vaccine (K27M peptide vaccine, combined with Tetanus Toxoid peptide, emulsified in montanide. Poly-ICLC will be given concurrently)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC007:Stratum B-non-DIPG DMG treated with vaccine; (K27M peptide vaccine, combined with Tetanus Toxoid peptide, emulsified in montanide. Poly-ICLC will be given concurrently)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC007:Stratum C- DIPG/DMG treated with vaccine and nivolumab (Nivolumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC008:Stratum A-Hemispheric HGG; (A combination of up to four FDA approved drugs based)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC008:Stratum B-non-DIPG DMG (A combination of up to four FDA approved drugs based)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 1 (ONC201, Panobinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 2 (ONC201, Paxalisib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 3 (ONC201, Panobinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 4 (ONC201, Paxalisib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 5 (ONC201, Panobinostat)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC022:Arm 6 (ONC201, Paxalisib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC023:Arm A: ONC206 for participants with diffuse midline gliomas + prior therapy (ONC206)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC023:Arm B: ONC206 + radiation therapy for newly diagnosed participants (ONC206)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC023:Arm C: ONC206 + radiation therapy, DMGs with evidence of first progression but previously untreated (ONC206)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC023:Arm D: ONC206 Therapy, Primary malignant CNS tumors with progression (ONC206)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC026:Arm 1 - LGG (DAY101)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC026:Arm 2 - LGG extension (DAY101)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC026:Arm 3 - Solid tumor (DAY101)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PNOC027:Individualized Treatment Recommendation ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-9905:Arm I (dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-9905:Arm II (dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-9905:Arm III (cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, pegaspargase, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-9905:Arm IV (cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, pegaspargase, thioguanine, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Chemotherapy, surgery, radiation therapy (cisplatin, cyclophosphamide, vincristine sulfate, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Regimen A: Cycle A (cyclophosphamide, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Regimen A: Cycle A' (vincristine, cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Regimen A: Cycle B (cisplatin, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Regimen B: Cycle X (cyclophosphamide, vincristine,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG9233:Regimen B: Cycle Y (cisplatin, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R115777-INT-11:1 (Gemcitabine with R115777)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R115777-INT-11:2 (Gemcitabine with Placebo)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REMATCH:Left ventricular assist device (Left ventricular assist device)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REMATCH:Optimal medical therapy (Optimal medical therapy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase I: Dose Level 1 (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase I: Dose Level 2a (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase I: Dose Level 2b (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase I: Dose Level 3 (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase II: Arm 1/BEV-FAILURE (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase II: Arm 1/BEV-NAIVE (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase II: Arm 2/BEV-FAILURE (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTOG-0929:Phase II: Arm 2/BEV-NAIVE (temozolomide, ABT-888)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Re-MATCH:Group A ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Re-MATCH:Group B ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC006:Chemotherapy and local control by radiotherapy and surgery (doxorubicin hydrochloride, etoposide, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC006:Chemotherapy and local control by surgery (doxorubicin hydrochloride, etoposide, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 1: Ewings Sarcoma Primary Cohort (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 2: Ewings Sarcoma Secondary Cohort (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 3: Ewings Sarcoma Expanded Cohort (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 4: Osteosarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 5: Synovial Sarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 6: Rhabdomyosarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 7a: Alveolar Soft Part Sarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 7b: Desmoplastic Small Round Cell Tumors. (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 7c: Extraskeletal Myxoid Chondrosarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 7d: Clear Cell Sarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 7e: Myxoid Liposarcoma (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SARC011:Cohort 8: Diagnosis Not Specified (RG1507)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC-9006:Regimen A (Temozolomide, Etoposide, Sorafenib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC-9006:Regimen B (Temozolomide, Etoposide, Everolimus)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC-9006:Regimen C (Temozolomide, Etoposide, Erlotinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SC-9006:Regimen D (Temozolomide, Etoposide, Dasatinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SEL-TH-1601:Stratum 1 - NF2 related vestibular schwannomas (Selumetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SEL-TH-1601:Stratum 2: other NF2 related tumors (meningiomas and ependymoma) (Selumetinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Germinoma metastatic (none)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Germinoma non-metastatic (Carboplatin, Etoposide, Ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:No Intervention: Teratoma ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Non-Germinoma metastatic high risk (Cisplatin, Etoposide, Ifosfamide (high dose))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Non-Germinoma metastatic standard risk (Cisplatin, etoposide, Ifosfamide (standard))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Non-germinoma non-metastatic high risk (Cisplatin, Etoposide, Ifosfamide (high dose))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP CNS GCT II:Non-germinoma non-metastatic standard risk (Cisplatin, etoposide, Ifosfamide (standard))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-CNS-GCT-96:Stratum I: Option 1 (see notes) (carboplatin, cisplatin, etoposide phosphate, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-CNS-GCT-96:Stratum I: Option 2 (see notes) (carboplatin, cisplatin, etoposide phosphate, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-CNS-GCT-96:Stratum II: (secreting tumors and embryonal carcinoma) (cisplatin, etoposide phosphate, ifosfamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 1 arm A (Vincristine, Etoposide, Cyclophosphamide, Cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 1 arm B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 2 arm A (Vincristine, Etoposide, Cyclophosphamide, Methotrexate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 2 arm B (Vincristine, Etoposide, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 3 arm A (Vincristine, Carboplatin, Methotrexate, Cyclophosphamide, Cisplatin, Valproate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-EP-II:Stratum 3 arm B (Vincristine, Carboplatin, Methotrexate Cyclophosphamide, Cisplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-LGG-2004:Control group</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-LGG-2004:intensified induction chemotherapy group (vincristine, carboplatin, etoposide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-LGG-2004:radiation therapy group</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-LGG-2004:standard chemotherapy group (vincristine, carboplatin)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-PNET-4:Hyperfractionated radiotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOP-PNET-4:Standard Fractionation Regimen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART:Intervenion B2 (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART:Intervention B1 (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART:Stratum A (alisertib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART:Stratum B (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJATART:Stratum C (alisertib, cisplatin, cyclophosphamide, vincristine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJDAWN:A: ribociclib + gemcitabine (ribociclib, gemcitabine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJDAWN:B: ribociclib + trametinib (ribociclib, trametinib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJDAWN:C: ribociclib + sonidegib (ribociclib, sonidegib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB-96:Average-risk (filgrastim, amifostine trihydrate, cisplatin, cyclophosphamide, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB-96:High-risk (filgrastim, amifostine trihydrate, cisplatin, cyclophosphamide, vincristine sulfate)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB03:Stratum 1 (high-risk group) (Vincristine, Cisplatin, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB03:Stratum 2 (average-risk group) (Vincristine, Cisplatin, Cyclophosphamide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum N1: Standard Risk (Cyclophosphamide, Cisplatin, Vincristine,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum N2: Intermediate Risk (Cyclophosphamide, Cisplatin, Vincristine, Pemetrexed, Gemcitabine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum N3: High Risk (Cyclophosphamide, Cisplatin, Vincristine, Pemetrexed, Gemcitabine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum S1: Standard Risk (Cyclophosphamide, Cisplatin, Vincristine, Vismodegib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum S2: High Risk (Cyclophosphamide, Cisplatin, Vincristine, Vismodegib)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum W1: Low Risk (Cyclophosphamide, Cisplatin, Vincristine,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum W2: Atypical (Cyclophosphamide, Cisplatin, Vincristine,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJMB12:Stratum W3: High Risk (Cyclophosphamide, Cisplatin, Vincristine,)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJYC07:High-Risk Patients (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Velban(R) (vinblastine), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib), Vepesid(R), VP-16 (etoposide))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJYC07:Intermediate-Risk Therapy (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Velban(R) (vinblastine), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib), Vepesid(R), VP-16 (etoposide))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SJYC07:Low-Risk Patients (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Paraplatin(R) (carboplatin), Vepesid(R), VP-16 (etoposide), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib))</code></td><td><code></code></td><td></td></tr>
<tr><td><code>STRIvE-02:SCRI-CARB7H3(s) ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>STRIvE-02:SCRI-CARB7H3(s)x19 ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>STRIvE-02:SCRI-CARB7H3(s)x19 plus pembrolizumab ()</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stupp Protocol:Radiotherapy with concomitant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stupp Protocol:adjuvant chemotherapy with temozolomide (temozolomide)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TB-403:TB-403 100mg/kg (TB-403)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TB-403:TB-403 175mg/kg (TB-403)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TB-403:TB-403 20mg/kg (TB-403)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TB-403:TB-403 50mg/kg (TB-403)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TOTEM:Intensive follow up</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TOTEM:Minimalist follow up</code></td><td><code></code></td><td></td></tr>
<tr><td><code>rHSC-DIPGVax:&quot;Lead In&quot;: rHSC-DIPGVax Monotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>rHSC-DIPGVax:Part A: rHSC-DIPGVax in Combination with BALSTILIMAB (Anti-PD1) (Balstilimab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>rHSC-DIPGVax:Part B: Dose Escalation of ZALIFRELIMAB (Anti-CTLA4) (Balstilimab, Zalifrelimab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>rHSC-DIPGVax:Part C: Dose Expansion (Balstilimab, Zalifrelimab)</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-tumorpresentationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorpresentationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorpresentationenum')">×</button>
<h3><code>TumorPresentationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diffuse</code></td><td><code>ncit:C14175</code></td><td></td></tr>
<tr><td><code>Nodular</code></td><td><code>ncit:C36012</code></td><td></td></tr>
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
    "cns": {
      "name": "cns",
      "title": "Central Nervous System Tumors",
      "description": "The CNS view of the PCDC data model represents consensus data modeling by an international group of pediatric central nervous system tumor experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Central Nervous System Pediatric Research Consortium (INSPiRE). It is based on the collective requirements of its contributors."
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
        "country",
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
        "age_at_end",
        "age_precision"
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
        "reason_off_other"
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
        "cause_of_death_other",
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
    "GeneticAnalysis": {
      "slots": [
        "age_at_genetic_analysis",
        "genetic_analysis_method",
        "genomic_source_class",
        "mosaicism",
        "mosaicism_percent",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "alteration_region",
        "chromosome",
        "iscn",
        "gene",
        "hgvs_coding",
        "hgvs_protein",
        "external_ref_id_system",
        "external_ref_id",
        "copy_number",
        "maf_numeric",
        "allelic_state"
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
        "determination_source",
        "diagnosis_category",
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
        "stage_system",
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
        "detection_method",
        "mri_sequence",
        "site_classification",
        "disease_site",
        "site_other",
        "tumor_presentation"
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
        "protocol_procedure",
        "non_protocol_timing",
        "site_classification",
        "procedure_site",
        "site_other",
        "extent",
        "outcome",
        "hydrocephalus",
        "posterior_fossa_syndrome",
        "csf_diversion"
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
        "protocol_medication",
        "non_protocol_timing",
        "non_protocol_reason",
        "route",
        "medication",
        "medication_other"
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
        "protocol_radiation_therapy",
        "rt_data_source",
        "site_classification",
        "rt_site",
        "energy_type",
        "technique",
        "rt_dose",
        "rt_dose_unit",
        "boost_type",
        "boost_dose",
        "num_fraction",
        "fraction_dose",
        "fraction_dose_unit",
        "rt_margins"
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
        "response_method",
        "response_category",
        "response_system",
        "response_system_version",
        "response",
        "mri_sequence",
        "neurological_status"
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
    "hydrocephalus": {
      "slot_uri": "ncit:C3111",
      "range": "HydrocephalusEnum",
      "comments": [],
      "annotations": {}
    },
    "csf_diversion": {
      "slot_uri": "",
      "range": "CsfDiversionEnum",
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
    "route": {
      "slot_uri": "ncit:C186559",
      "range": "RouteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "maf_numeric": {
      "slot_uri": "ncit:C173545",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "response_method": {
      "slot_uri": "ncit:C178148",
      "range": "ResponseMethodEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "rb"
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
    "external_ref_id_system": {
      "slot_uri": "",
      "range": "ExternalRefIdSystemEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "posterior_fossa_syndrome": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "rt_margins": {
      "slot_uri": "ncit:C41227",
      "range": "RtMarginsEnum",
      "comments": [],
      "annotations": {}
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
    "tumor_presentation": {
      "slot_uri": "",
      "range": "TumorPresentationEnum",
      "comments": [
        "(cns) ConsortiumNote: Only use if the presentation is clearly reported in the source data, otherwise use 'Not Reported'."
      ],
      "annotations": {}
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
    "non_protocol_reason": {
      "slot_uri": "",
      "range": "NonProtocolReasonEnum",
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
    "determination_source": {
      "slot_uri": "",
      "range": "DeterminationSourceEnum",
      "comments": [
        "(cns) ConsortiumNote: For current MB data, this will all be research/retrospective. For future COG MB, will be prospective/clinical."
      ],
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
    "genomic_source_class": {
      "slot_uri": "",
      "range": "GenomicSourceClassEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb",
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
    "country": {
      "slot_uri": "",
      "range": "string",
      "comments": [
        "(cns) ConsortiumNote: Might have to manually extract from site for COG data if needed."
      ],
      "annotations": {
        "tier_optional": "fa",
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
    "neurological_status": {
      "slot_uri": "",
      "range": "NeurologicalStatusEnum",
      "comments": [],
      "annotations": {}
    },
    "efs_censor_status": {
      "slot_uri": "",
      "range": "EfsCensorStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,os"
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
    "rt_data_source": {
      "slot_uri": "",
      "range": "RtDataSourceEnum",
      "comments": [
        "(cns) ConsortiumNote: All XRT data for COG will be intended dose."
      ],
      "annotations": {}
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
    "age_precision": {
      "slot_uri": "ncit:C48045",
      "range": "AgePrecisionEnum",
      "comments": [
        "(cns) ConsortiumNote: PNOC uses more general dates to avoid PHI"
      ],
      "annotations": {}
    },
    "mri_sequence": {
      "slot_uri": "",
      "range": "MriSequenceEnum",
      "comments": [
        "(cns) ConsortiumNote: Only use if the sequence is clearly reported in the source data, otherwise use 'Not Reported'"
      ],
      "annotations": {}
    },
    "age_at_measurement": {
      "slot_uri": "ncit:C154628",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "anthropometric_measurement_result_unit": {
      "slot_uri": "",
      "range": "AnthropometricMeasurementResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
      }
    },
    "mosaicism": {
      "slot_uri": "ncit:C92976",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "copy_number": {
      "slot_uri": "ncit:C49142",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "non_protocol_timing": {
      "slot_uri": "ncit:C175038",
      "range": "NonProtocolTimingEnum",
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
    "diagnosis_category": {
      "slot_uri": "",
      "range": "DiagnosisCategoryEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "ls"
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
    "mosaicism_percent": {
      "slot_uri": "ncit:C92976",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "morph_code_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
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
    "cause_of_death_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "external_ref_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "protocol_medication": {
      "slot_uri": "ncit:C175038",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
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
    "protocol_procedure": {
      "slot_uri": "ncit:C175038",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "allelic_state": {
      "slot_uri": "",
      "range": "AllelicStateEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
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
        "BMI": {
          "meaning": "ncit:C138901",
          "comments": []
        },
        "BSA": {
          "meaning": "ncit:C25157",
          "comments": []
        },
        "Head Circumference": {
          "meaning": "ncit:C81255",
          "comments": [
            "(fa) ConsortiumNote: Prioritize Head Circumference at birth and at other evaluations."
          ]
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
    "HydrocephalusEnum": {
      "permissible_values": {
        "Compressed Sulci at the Vertex": {
          "meaning": "",
          "comments": []
        },
        "Enlarged Ventricles": {
          "meaning": "",
          "comments": []
        },
        "No": {
          "meaning": "ncit:C49487",
          "comments": []
        },
        "Papilledema": {
          "meaning": "ncit:C3307",
          "comments": []
        },
        "Periventriculur Edema": {
          "meaning": "",
          "comments": []
        },
        "Yes, NOS": {
          "meaning": "ncit:C49488",
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
        "WHO CNS >> Grade 1": {
          "meaning": "ncit:C62394",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "WHO CNS >> Grade 2": {
          "meaning": "ncit:C62395",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "WHO CNS >> Grade 3": {
          "meaning": "ncit:C62396",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "WHO CNS >> Grade 4": {
          "meaning": "ncit:C62397",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        }
      }
    },
    "ResponseEnum": {
      "permissible_values": {
        "Modified MacDonald >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "Modified MacDonald >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "Modified MacDonald >> Stable Disease": {
          "meaning": "",
          "comments": []
        },
        "Modified Macdonald >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "Not Evaluable": {
          "meaning": "ncit:C62222",
          "comments": []
        },
        "RANO >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "RANO >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "RANO >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "RANO >> Stable Disease": {
          "meaning": "",
          "comments": []
        },
        "RAPNO >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "RAPNO >> Major Response": {
          "meaning": "",
          "comments": [
            "(cns_v1.2approved) ConsortiumNote: Only use for RAPNO low-grade gliomas"
          ]
        },
        "RAPNO >> Minor Response": {
          "meaning": "",
          "comments": []
        },
        "RAPNO >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "RAPNO >> Stable Disease": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Complete Response": {
          "meaning": "ncit:C4870",
          "comments": [
            "(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response."
          ]
        },
        "System NOS >> Major Response": {
          "meaning": "ncit:C123590",
          "comments": [
            "(cns) ConsortiumNote: Only use for RAPNO low-grade gliomas"
          ]
        },
        "System NOS >> Minor Response": {
          "meaning": "ncit:C123598",
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
        },
        "iRANO >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "iRANO >> Minor Response": {
          "meaning": "",
          "comments": []
        },
        "iRANO >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "iRANO >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "iRANO >> Stable Disease": {
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
        "Chemoradiotherapy": {
          "meaning": "ncit:C94626",
          "comments": [
            "(cns) ConsortiumNote: SIOPE groups should use this value in place of what they may have as 'concommitant'."
          ]
        },
        "Chemotherapy Window": {
          "meaning": "",
          "comments": []
        },
        "Consolidation": {
          "meaning": "ncit:C15679",
          "comments": []
        },
        "Induction": {
          "meaning": "ncit:C158876",
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
    "DeterminationSourceEnum": {
      "permissible_values": {
        "Clinical Testing": {
          "meaning": "ncit:C15791",
          "comments": []
        },
        "Retrospective Research": {
          "meaning": "ncit:C53312",
          "comments": []
        }
      }
    },
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Basal Ganglia-Thalamus": {
          "meaning": "ncit:C158080",
          "comments": []
        },
        "Cauda Equina Spinal Cord": {
          "meaning": "ncit:C12689",
          "comments": []
        },
        "Cerebellum": {
          "meaning": "ncit:C12445",
          "comments": []
        },
        "Cervical Spine": {
          "meaning": "ncit:C69313",
          "comments": []
        },
        "Extra CNS": {
          "meaning": "",
          "comments": []
        },
        "Fourth Ventricle": {
          "meaning": "ncit:C12828",
          "comments": []
        },
        "Frontal Lobe": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Lateral Ventricle": {
          "meaning": "ncit:C12834",
          "comments": []
        },
        "Leptomeningeal": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Lumbar Spinal Cord": {
          "meaning": "ncit:C12895",
          "comments": []
        },
        "Medulla": {
          "meaning": "ncit:C12442",
          "comments": []
        },
        "Midbrain": {
          "meaning": "ncit:C12510",
          "comments": []
        },
        "Occipital Lobe": {
          "meaning": "ncit:C12355",
          "comments": []
        },
        "Optic Chiasm": {
          "meaning": "ncit:C90609",
          "comments": []
        },
        "Optic Nerve": {
          "meaning": "ncit:C12761",
          "comments": []
        },
        "Parietal Lobe": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Pons": {
          "meaning": "ncit:C12511",
          "comments": []
        },
        "Suprasellar Pituitary": {
          "meaning": "ncit:C95445",
          "comments": []
        },
        "Temporal Lobe": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Third Ventricle": {
          "meaning": "ncit:C12827",
          "comments": []
        },
        "Thoracic Spinal Cord": {
          "meaning": "ncit:C12894",
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
        "Disease Progression": {
          "meaning": "ncit:C17747",
          "comments": []
        },
        "Failure to Attain Remission": {
          "meaning": "ncit:C178072",
          "comments": []
        },
        "Ineligible": {
          "meaning": "ncit:C40412",
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
        "Study Discontinuation": {
          "meaning": "ncit:C142444",
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
        }
      }
    },
    "NeurologicalStatusEnum": {
      "permissible_values": {
        "Deterioration": {
          "meaning": "ncit:C25751",
          "comments": []
        },
        "Improved": {
          "meaning": "ncit:C125459",
          "comments": []
        },
        "Stable": {
          "meaning": "ncit:C30103",
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
    "TumorPresentationEnum": {
      "permissible_values": {
        "Diffuse": {
          "meaning": "ncit:C14175",
          "comments": []
        },
        "Nodular": {
          "meaning": "ncit:C36012",
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
        }
      }
    },
    "CsfDiversionEnum": {
      "permissible_values": {
        "Endoscopic Third Ventriculostomy": {
          "meaning": "",
          "comments": []
        },
        "No": {
          "meaning": "ncit:C49487",
          "comments": []
        },
        "Shunt, NOS": {
          "meaning": "ncit:C50174",
          "comments": []
        },
        "Ventriculoatrial Shunt": {
          "meaning": "",
          "comments": []
        },
        "Ventriculoperitoneal Shunt": {
          "meaning": "ncit:C168483",
          "comments": []
        }
      }
    },
    "RtMarginsEnum": {
      "permissible_values": {
        "0.5 cm": {
          "meaning": "",
          "comments": []
        },
        "1 cm": {
          "meaning": "",
          "comments": []
        },
        "2 cm": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ResponseMethodEnum": {
      "permissible_values": {
        "Biopsy": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Cytology": {
          "meaning": "ncit:C16491",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "Physical Examination": {
          "meaning": "ncit:C20989",
          "comments": []
        },
        "Surgical Resection": {
          "meaning": "ncit:C158758",
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
        "C19MC Amplification": {
          "meaning": "ncit:C129498",
          "comments": []
        },
        "CTNNB1 Variant": {
          "meaning": "ncit:C36659",
          "comments": []
        },
        "Chromosome 11 Loss": {
          "meaning": "ncit:C36549",
          "comments": []
        },
        "Chromosome 14q Loss": {
          "meaning": "ncit:C39795",
          "comments": []
        },
        "DICER1 Variant": {
          "meaning": "ncit:C164287",
          "comments": []
        },
        "GLI2 Amplification": {
          "meaning": "ncit:C199588",
          "comments": []
        },
        "Isochromosome 17q": {
          "meaning": "ncit:C36477",
          "comments": []
        },
        "MYC Amplification": {
          "meaning": "ncit:C36641",
          "comments": []
        },
        "MYCN Amplification": {
          "meaning": "ncit:C36673",
          "comments": []
        },
        "PTCH1 Variant": {
          "meaning": "ncit:C133669",
          "comments": []
        },
        "RB1 Variant": {
          "meaning": "ncit:C169031",
          "comments": []
        },
        "SMARCB1 Variant": {
          "meaning": "ncit:C18394",
          "comments": []
        },
        "SMO Variant": {
          "meaning": "ncit:C124793",
          "comments": []
        },
        "SUFU Variant": {
          "meaning": "ncit:C189843",
          "comments": []
        },
        "TP53 Variant": {
          "meaning": "ncit:C118396",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "RtSiteEnum": {
      "permissible_values": {
        "Craniospinal": {
          "meaning": "ncit:C84352",
          "comments": []
        },
        "Exact Volume Unknown": {
          "meaning": "",
          "comments": []
        },
        "Focal": {
          "meaning": "ncit:C28224",
          "comments": []
        },
        "Posterior Fossa": {
          "meaning": "",
          "comments": []
        },
        "Tumor Bed Plus Margin": {
          "meaning": "",
          "comments": []
        },
        "Whole Brain": {
          "meaning": "",
          "comments": []
        },
        "Whole Spinal Cord": {
          "meaning": "",
          "comments": []
        },
        "Whole Ventricle": {
          "meaning": "",
          "comments": []
        },
        "Whole Ventricular With Spine": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AgePrecisionEnum": {
      "permissible_values": {
        "Approximate": {
          "meaning": "ncit:C45828",
          "comments": []
        },
        "Exact": {
          "meaning": "ncit:C86021",
          "comments": []
        }
      }
    },
    "ResponseSystemEnum": {
      "permissible_values": {
        "Modified MacDonald": {
          "meaning": "ncit:C198862",
          "comments": []
        },
        "RANO": {
          "meaning": "ncit:C114879",
          "comments": []
        },
        "RAPNO": {
          "meaning": "ncit:C198863",
          "comments": []
        },
        "WHO": {
          "meaning": "ncit:C75419",
          "comments": []
        },
        "iRANO": {
          "meaning": "ncit:C131131",
          "comments": []
        }
      }
    },
    "NonProtocolReasonEnum": {
      "permissible_values": {
        "Prevention of Adverse Event": {
          "meaning": "ncit:C185654",
          "comments": []
        },
        "Stem Cell Mobilization": {
          "meaning": "ncit:C62604",
          "comments": []
        },
        "Treatment for Adverse Event": {
          "meaning": "ncit:C88082",
          "comments": []
        }
      }
    },
    "MriSequenceEnum": {
      "permissible_values": {
        "Diffusion Weighted Imaging": {
          "meaning": "ncit:C111116",
          "comments": []
        },
        "FLAIR": {
          "meaning": "ncit:C82392",
          "comments": []
        },
        "MRI T1 with Gadolinium": {
          "meaning": "ncit:C180728",
          "comments": []
        },
        "MRI T2": {
          "meaning": "ncit:C180729",
          "comments": []
        }
      }
    },
    "RouteEnum": {
      "permissible_values": {
        "Intraarterial": {
          "meaning": "ncit:C38222",
          "comments": []
        },
        "Intracerebral, Convection-Enhanced Delivery": {
          "meaning": "ncit:C116566",
          "comments": []
        },
        "Intrathecal": {
          "meaning": "ncit:C173292",
          "comments": []
        },
        "Systemic": {
          "meaning": "ncit:C173291",
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
        "Modified Chang Staging >> M+": {
          "meaning": "",
          "comments": []
        },
        "Modified Chang Staging >> M0": {
          "meaning": "ncit:C48699",
          "comments": []
        },
        "Modified Chang Staging >> M0 / M1": {
          "meaning": "",
          "comments": []
        },
        "Modified Chang Staging >> M1": {
          "meaning": "ncit:C48700",
          "comments": []
        },
        "Modified Chang Staging >> M2": {
          "meaning": "",
          "comments": []
        },
        "Modified Chang Staging >> M3": {
          "meaning": "",
          "comments": []
        },
        "Modified Chang Staging >> M4": {
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
        "Undifferentiated": {
          "meaning": "ncit:C41438",
          "comments": []
        }
      }
    },
    "GenomicSourceClassEnum": {
      "permissible_values": {
        "Germline": {
          "meaning": "ncit:C17666",
          "comments": []
        },
        "Somatic": {
          "meaning": "ncit:C18060",
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
    "ExternalRefIdSystemEnum": {
      "permissible_values": {
        "ClinGen": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "StageSystemEnum": {
      "permissible_values": {
        "Modified Chang Staging": {
          "meaning": "ncit:C198826",
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
        "02-294 DFCI": {
          "meaning": "",
          "comments": []
        },
        "10-C-0219": {
          "meaning": "",
          "comments": []
        },
        "11-C-0161": {
          "meaning": "",
          "comments": []
        },
        "15-C-0093": {
          "meaning": "",
          "comments": []
        },
        "A3961": {
          "meaning": "",
          "comments": []
        },
        "A3973": {
          "meaning": "",
          "comments": []
        },
        "A9952": {
          "meaning": "",
          "comments": []
        },
        "AALL0434": {
          "meaning": "",
          "comments": []
        },
        "AALL1731": {
          "meaning": "",
          "comments": []
        },
        "AAML03P1": {
          "meaning": "ncit:C168936",
          "comments": []
        },
        "AAML0531": {
          "meaning": "ncit:C168937",
          "comments": []
        },
        "ACNS0121": {
          "meaning": "",
          "comments": []
        },
        "ACNS0122": {
          "meaning": "",
          "comments": []
        },
        "ACNS0126": {
          "meaning": "",
          "comments": []
        },
        "ACNS0222": {
          "meaning": "",
          "comments": []
        },
        "ACNS0223": {
          "meaning": "",
          "comments": []
        },
        "ACNS0224": {
          "meaning": "",
          "comments": []
        },
        "ACNS0232": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332": {
          "meaning": "",
          "comments": []
        },
        "ACNS0333": {
          "meaning": "",
          "comments": []
        },
        "ACNS0334": {
          "meaning": "",
          "comments": []
        },
        "ACNS0423": {
          "meaning": "",
          "comments": []
        },
        "ACNS0621": {
          "meaning": "",
          "comments": []
        },
        "ACNS0821": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831": {
          "meaning": "",
          "comments": []
        },
        "ACNS0927": {
          "meaning": "",
          "comments": []
        },
        "ACNS1021": {
          "meaning": "",
          "comments": []
        },
        "ACNS1022": {
          "meaning": "",
          "comments": []
        },
        "ACNS1123": {
          "meaning": "",
          "comments": []
        },
        "ACNS1221": {
          "meaning": "",
          "comments": []
        },
        "ACNS1422": {
          "meaning": "",
          "comments": []
        },
        "ACNS1721": {
          "meaning": "",
          "comments": []
        },
        "ACNS1723": {
          "meaning": "",
          "comments": []
        },
        "ACNS1821": {
          "meaning": "",
          "comments": []
        },
        "ACNS1831": {
          "meaning": "",
          "comments": []
        },
        "ACNS1833": {
          "meaning": "",
          "comments": []
        },
        "ACNS1931": {
          "meaning": "",
          "comments": []
        },
        "ACNS2021": {
          "meaning": "",
          "comments": []
        },
        "ADVL0012": {
          "meaning": "",
          "comments": []
        },
        "ADVL0414": {
          "meaning": "",
          "comments": []
        },
        "ADVL0416": {
          "meaning": "",
          "comments": []
        },
        "ADVL0515": {
          "meaning": "",
          "comments": []
        },
        "ADVL0612": {
          "meaning": "",
          "comments": []
        },
        "ADVL0815": {
          "meaning": "",
          "comments": []
        },
        "ADVL0819": {
          "meaning": "",
          "comments": []
        },
        "ADVL0912": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921": {
          "meaning": "",
          "comments": []
        },
        "ADVL1013": {
          "meaning": "",
          "comments": []
        },
        "ADVL1111": {
          "meaning": "",
          "comments": []
        },
        "ADVL1112": {
          "meaning": "",
          "comments": []
        },
        "ADVL1217": {
          "meaning": "",
          "comments": []
        },
        "ADVL1312": {
          "meaning": "",
          "comments": []
        },
        "ADVL1411": {
          "meaning": "",
          "comments": []
        },
        "ADVL1414": {
          "meaning": "",
          "comments": []
        },
        "ADVL1513": {
          "meaning": "",
          "comments": []
        },
        "ADVL1514": {
          "meaning": "",
          "comments": []
        },
        "ADVL1515": {
          "meaning": "",
          "comments": []
        },
        "ADVL1615": {
          "meaning": "",
          "comments": []
        },
        "ADVL1622": {
          "meaning": "",
          "comments": []
        },
        "ADVL1711": {
          "meaning": "",
          "comments": []
        },
        "AEWS0031": {
          "meaning": "ncit:C174970",
          "comments": []
        },
        "AEWS1031": {
          "meaning": "ncit:C174971",
          "comments": []
        },
        "AFLACST1501": {
          "meaning": "",
          "comments": []
        },
        "AG881-C-004": {
          "meaning": "",
          "comments": []
        },
        "AGCT0132": {
          "meaning": "ncit:C177343",
          "comments": []
        },
        "AGCT1531": {
          "meaning": "",
          "comments": []
        },
        "AGCT1532": {
          "meaning": "",
          "comments": []
        },
        "AIEOP EP II": {
          "meaning": "",
          "comments": []
        },
        "ANBL00B1": {
          "meaning": "",
          "comments": []
        },
        "ANBL00P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL0531": {
          "meaning": "",
          "comments": []
        },
        "ANBL0532": {
          "meaning": "",
          "comments": []
        },
        "ANBL09P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL12P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531": {
          "meaning": "",
          "comments": []
        },
        "ANHL0131": {
          "meaning": "",
          "comments": []
        },
        "ANHL01P1": {
          "meaning": "",
          "comments": []
        },
        "AOST0331": {
          "meaning": "",
          "comments": []
        },
        "APEC1621": {
          "meaning": "",
          "comments": []
        },
        "AREN1921": {
          "meaning": "",
          "comments": []
        },
        "ARET0321": {
          "meaning": "",
          "comments": []
        },
        "ARST0531": {
          "meaning": "",
          "comments": []
        },
        "Ad-RTS-hIL-12": {
          "meaning": "",
          "comments": []
        },
        "Antineoplaston Therapy protocol": {
          "meaning": "",
          "comments": []
        },
        "BIOMEDE": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-01": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-02": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-03": {
          "meaning": "",
          "comments": []
        },
        "BRF116013": {
          "meaning": "",
          "comments": []
        },
        "BXQ-350 AD": {
          "meaning": "",
          "comments": []
        },
        "Baby POG-1": {
          "meaning": "",
          "comments": []
        },
        "CA209908": {
          "meaning": "",
          "comments": []
        },
        "CCG-921": {
          "meaning": "",
          "comments": []
        },
        "CCG-9921": {
          "meaning": "",
          "comments": []
        },
        "CCG-9942": {
          "meaning": "",
          "comments": []
        },
        "CCG-99701": {
          "meaning": "",
          "comments": []
        },
        "CCG-99703": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9952": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9961": {
          "meaning": "",
          "comments": []
        },
        "CCG-D9803": {
          "meaning": "",
          "comments": []
        },
        "CCG-P9970": {
          "meaning": "",
          "comments": []
        },
        "CCG09712": {
          "meaning": "",
          "comments": []
        },
        "CCG945": {
          "meaning": "",
          "comments": []
        },
        "CCG9941": {
          "meaning": "",
          "comments": []
        },
        "CCG99703": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-RMS-2005": {
          "meaning": "",
          "comments": []
        },
        "CCMC1411": {
          "meaning": "",
          "comments": []
        },
        "CDRB436G2201": {
          "meaning": "",
          "comments": []
        },
        "CERN-08-01": {
          "meaning": "",
          "comments": []
        },
        "CHMC-6006": {
          "meaning": "",
          "comments": []
        },
        "CHP455": {
          "meaning": "",
          "comments": []
        },
        "CHP693": {
          "meaning": "",
          "comments": []
        },
        "CHP719": {
          "meaning": "",
          "comments": []
        },
        "CHP735": {
          "meaning": "",
          "comments": []
        },
        "CLEE011XUS17T": {
          "meaning": "",
          "comments": []
        },
        "CNS1100": {
          "meaning": "",
          "comments": []
        },
        "COG A09712": {
          "meaning": "",
          "comments": []
        },
        "COJEC": {
          "meaning": "",
          "comments": []
        },
        "CONNECT 1701": {
          "meaning": "",
          "comments": []
        },
        "CONNECT 1702": {
          "meaning": "",
          "comments": []
        },
        "CONNECT1701": {
          "meaning": "",
          "comments": []
        },
        "CONNECT1702": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2000": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2009": {
          "meaning": "",
          "comments": []
        },
        "ChildrenHLA": {
          "meaning": "",
          "comments": []
        },
        "DART Clinical Trial": {
          "meaning": "",
          "comments": []
        },
        "DFMO": {
          "meaning": "",
          "comments": []
        },
        "DIPG-BATS": {
          "meaning": "",
          "comments": []
        },
        "ECREST study": {
          "meaning": "",
          "comments": []
        },
        "ETMR One": {
          "meaning": "",
          "comments": []
        },
        "EZH-102": {
          "meaning": "",
          "comments": []
        },
        "EZH-202": {
          "meaning": "",
          "comments": []
        },
        "GCC1949": {
          "meaning": "",
          "comments": []
        },
        "GemPOx": {
          "meaning": "",
          "comments": []
        },
        "HERBY": {
          "meaning": "",
          "comments": []
        },
        "HGG-01": {
          "meaning": "",
          "comments": []
        },
        "HGG-BAT": {
          "meaning": "",
          "comments": []
        },
        "HIT-GBM-C": {
          "meaning": "",
          "comments": []
        },
        "HIT-HGG-2013": {
          "meaning": "",
          "comments": []
        },
        "HIT-SIOP PNET 4": {
          "meaning": "",
          "comments": []
        },
        "HSPPC-96": {
          "meaning": "",
          "comments": []
        },
        "HUMC 1612": {
          "meaning": "",
          "comments": []
        },
        "Head Start 4": {
          "meaning": "",
          "comments": []
        },
        "Head Start II": {
          "meaning": "",
          "comments": []
        },
        "Head Start III": {
          "meaning": "",
          "comments": []
        },
        "ICE": {
          "meaning": "",
          "comments": []
        },
        "INCB7839": {
          "meaning": "",
          "comments": []
        },
        "INDIGO": {
          "meaning": "",
          "comments": []
        },
        "IRS-III": {
          "meaning": "",
          "comments": []
        },
        "JET Protocol": {
          "meaning": "",
          "comments": []
        },
        "LGG 14C03": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003": {
          "meaning": "",
          "comments": []
        },
        "MEK116540": {
          "meaning": "",
          "comments": []
        },
        "MEK162": {
          "meaning": "",
          "comments": []
        },
        "MEMMAT": {
          "meaning": "",
          "comments": []
        },
        "METRICS": {
          "meaning": "",
          "comments": []
        },
        "MIN-001P-1501": {
          "meaning": "",
          "comments": []
        },
        "MK-3475": {
          "meaning": "",
          "comments": []
        },
        "MSKCC 09-014": {
          "meaning": "",
          "comments": []
        },
        "MSKCC 11-011": {
          "meaning": "",
          "comments": []
        },
        "MSKCC-03077": {
          "meaning": "",
          "comments": []
        },
        "N2012-01": {
          "meaning": "",
          "comments": []
        },
        "NCI 02-C-0193": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH": {
          "meaning": "",
          "comments": []
        },
        "NCT01185964": {
          "meaning": "",
          "comments": []
        },
        "NCT01222754": {
          "meaning": "",
          "comments": []
        },
        "NCT01502917": {
          "meaning": "",
          "comments": []
        },
        "NCT02924038": {
          "meaning": "",
          "comments": []
        },
        "NCT03696355": {
          "meaning": "",
          "comments": []
        },
        "NCT04196413": {
          "meaning": "",
          "comments": []
        },
        "NCT04264143": {
          "meaning": "",
          "comments": []
        },
        "NF105": {
          "meaning": "",
          "comments": []
        },
        "NF106": {
          "meaning": "",
          "comments": []
        },
        "NLG2105": {
          "meaning": "",
          "comments": []
        },
        "NMTRC V0706": {
          "meaning": "",
          "comments": []
        },
        "NMTRC009": {
          "meaning": "",
          "comments": []
        },
        "ONC028": {
          "meaning": "",
          "comments": []
        },
        "ONC201": {
          "meaning": "",
          "comments": []
        },
        "OZM-063": {
          "meaning": "",
          "comments": []
        },
        "OZM-075": {
          "meaning": "",
          "comments": []
        },
        "OZM-077": {
          "meaning": "",
          "comments": []
        },
        "PBTC 029": {
          "meaning": "",
          "comments": []
        },
        "PBTC-029": {
          "meaning": "",
          "comments": []
        },
        "PBTC-039": {
          "meaning": "",
          "comments": []
        },
        "PBTC-50": {
          "meaning": "",
          "comments": []
        },
        "PBTC001": {
          "meaning": "",
          "comments": []
        },
        "PBTC004": {
          "meaning": "",
          "comments": []
        },
        "PBTC005": {
          "meaning": "",
          "comments": []
        },
        "PBTC0056": {
          "meaning": "",
          "comments": []
        },
        "PBTC006": {
          "meaning": "",
          "comments": []
        },
        "PBTC007": {
          "meaning": "",
          "comments": []
        },
        "PBTC014": {
          "meaning": "",
          "comments": []
        },
        "PBTC016": {
          "meaning": "",
          "comments": []
        },
        "PBTC017": {
          "meaning": "",
          "comments": []
        },
        "PBTC018": {
          "meaning": "",
          "comments": []
        },
        "PBTC020": {
          "meaning": "",
          "comments": []
        },
        "PBTC021": {
          "meaning": "",
          "comments": []
        },
        "PBTC022": {
          "meaning": "",
          "comments": []
        },
        "PBTC023": {
          "meaning": "",
          "comments": []
        },
        "PBTC024": {
          "meaning": "",
          "comments": []
        },
        "PBTC025": {
          "meaning": "",
          "comments": []
        },
        "PBTC026": {
          "meaning": "",
          "comments": []
        },
        "PBTC027": {
          "meaning": "",
          "comments": []
        },
        "PBTC030": {
          "meaning": "",
          "comments": []
        },
        "PBTC031": {
          "meaning": "",
          "comments": []
        },
        "PBTC033": {
          "meaning": "",
          "comments": []
        },
        "PBTC042": {
          "meaning": "",
          "comments": []
        },
        "PBTC043": {
          "meaning": "",
          "comments": []
        },
        "PBTC045": {
          "meaning": "",
          "comments": []
        },
        "PBTC047": {
          "meaning": "",
          "comments": []
        },
        "PBTC048": {
          "meaning": "",
          "comments": []
        },
        "PBTC049": {
          "meaning": "",
          "comments": []
        },
        "PBTC050": {
          "meaning": "",
          "comments": []
        },
        "PBTC051": {
          "meaning": "",
          "comments": []
        },
        "PBTC053": {
          "meaning": "",
          "comments": []
        },
        "PBTC055": {
          "meaning": "",
          "comments": []
        },
        "PBTC056": {
          "meaning": "",
          "comments": []
        },
        "PEDSCCT6005": {
          "meaning": "",
          "comments": []
        },
        "PEG-Intron": {
          "meaning": "",
          "comments": []
        },
        "PNET 3": {
          "meaning": "",
          "comments": []
        },
        "PNOC001": {
          "meaning": "",
          "comments": []
        },
        "PNOC0013": {
          "meaning": "",
          "comments": []
        },
        "PNOC0015": {
          "meaning": "",
          "comments": []
        },
        "PNOC0016": {
          "meaning": "",
          "comments": []
        },
        "PNOC0018": {
          "meaning": "",
          "comments": []
        },
        "PNOC002": {
          "meaning": "",
          "comments": []
        },
        "PNOC0022": {
          "meaning": "",
          "comments": []
        },
        "PNOC0023": {
          "meaning": "",
          "comments": []
        },
        "PNOC003": {
          "meaning": "",
          "comments": []
        },
        "PNOC005": {
          "meaning": "",
          "comments": []
        },
        "PNOC007": {
          "meaning": "",
          "comments": []
        },
        "PNOC008": {
          "meaning": "",
          "comments": []
        },
        "PNOC009": {
          "meaning": "",
          "comments": []
        },
        "PNOC010": {
          "meaning": "",
          "comments": []
        },
        "PNOC013": {
          "meaning": "",
          "comments": []
        },
        "PNOC014": {
          "meaning": "",
          "comments": []
        },
        "PNOC015": {
          "meaning": "",
          "comments": []
        },
        "PNOC016": {
          "meaning": "",
          "comments": []
        },
        "PNOC022": {
          "meaning": "",
          "comments": []
        },
        "PNOC023": {
          "meaning": "",
          "comments": []
        },
        "PNOC026": {
          "meaning": "",
          "comments": []
        },
        "PNOC027": {
          "meaning": "",
          "comments": []
        },
        "POE08-01": {
          "meaning": "",
          "comments": []
        },
        "POG 9239": {
          "meaning": "",
          "comments": []
        },
        "POG 9631": {
          "meaning": "",
          "comments": []
        },
        "POG 9836": {
          "meaning": "",
          "comments": []
        },
        "POG 9879": {
          "meaning": "",
          "comments": []
        },
        "POG-9905": {
          "meaning": "",
          "comments": []
        },
        "POG-P9934": {
          "meaning": "",
          "comments": []
        },
        "POG9048": {
          "meaning": "",
          "comments": []
        },
        "POG9233": {
          "meaning": "",
          "comments": []
        },
        "PRO13110086": {
          "meaning": "",
          "comments": []
        },
        "Pittsburgh Vaccine Trial Cycle": {
          "meaning": "",
          "comments": []
        },
        "Protocol BT-55": {
          "meaning": "",
          "comments": []
        },
        "R115777-INT-11": {
          "meaning": "",
          "comments": []
        },
        "RAD001": {
          "meaning": "",
          "comments": []
        },
        "REMATCH": {
          "meaning": "",
          "comments": []
        },
        "REMIND": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929": {
          "meaning": "",
          "comments": []
        },
        "Re-MATCH": {
          "meaning": "",
          "comments": []
        },
        "SARC006": {
          "meaning": "",
          "comments": []
        },
        "SARC011": {
          "meaning": "",
          "comments": []
        },
        "SARC031": {
          "meaning": "",
          "comments": []
        },
        "SARC037": {
          "meaning": "",
          "comments": []
        },
        "SC-9006": {
          "meaning": "",
          "comments": []
        },
        "SC9005": {
          "meaning": "",
          "comments": []
        },
        "SCH52365": {
          "meaning": "",
          "comments": []
        },
        "SDT-201": {
          "meaning": "",
          "comments": []
        },
        "SEL-TH-1601": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II": {
          "meaning": "",
          "comments": []
        },
        "SIOP LGG 2004": {
          "meaning": "",
          "comments": []
        },
        "SIOP-CNS-GCT-96": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II": {
          "meaning": "",
          "comments": []
        },
        "SIOP-LGG-2004": {
          "meaning": "",
          "comments": []
        },
        "SIOP-PNET-4": {
          "meaning": "",
          "comments": []
        },
        "SJATART": {
          "meaning": "",
          "comments": []
        },
        "SJBG07": {
          "meaning": "",
          "comments": []
        },
        "SJDAWN": {
          "meaning": "",
          "comments": []
        },
        "SJHG12": {
          "meaning": "",
          "comments": []
        },
        "SJHG98": {
          "meaning": "",
          "comments": []
        },
        "SJMB-96": {
          "meaning": "",
          "comments": []
        },
        "SJMB03": {
          "meaning": "",
          "comments": []
        },
        "SJMB12": {
          "meaning": "",
          "comments": []
        },
        "SJPDGF": {
          "meaning": "",
          "comments": []
        },
        "SJREFU": {
          "meaning": "",
          "comments": []
        },
        "SJYC07": {
          "meaning": "",
          "comments": []
        },
        "STRIvE-02": {
          "meaning": "",
          "comments": []
        },
        "SU5416": {
          "meaning": "",
          "comments": []
        },
        "Study # 2014-0135": {
          "meaning": "",
          "comments": []
        },
        "Stupp Protocol": {
          "meaning": "",
          "comments": []
        },
        "TB-403": {
          "meaning": "",
          "comments": []
        },
        "TK216": {
          "meaning": "",
          "comments": []
        },
        "TOPNOC": {
          "meaning": "",
          "comments": []
        },
        "TOPNOC-001": {
          "meaning": "",
          "comments": []
        },
        "TOTEM": {
          "meaning": "",
          "comments": []
        },
        "VINILO study": {
          "meaning": "",
          "comments": []
        },
        "VITAC": {
          "meaning": "",
          "comments": []
        },
        "VOIT": {
          "meaning": "",
          "comments": []
        },
        "VP-16": {
          "meaning": "",
          "comments": []
        },
        "YMB 1000 013": {
          "meaning": "",
          "comments": []
        },
        "ZD-1839": {
          "meaning": "",
          "comments": []
        },
        "rHSC-DIPGVax": {
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
        "Photon": {
          "meaning": "ncit:C88112",
          "comments": []
        },
        "Proton": {
          "meaning": "ncit:C66897",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Adamantinomatous Craniopharyngioma": {
          "meaning": "ncit:C4726",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'"
          ]
        },
        "Anaplastic Ganglioglioma": {
          "meaning": "ncit:C4717",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Anaplastic Large Cell Lymphoma": {
          "meaning": "ncit:C3720",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Anaplastic Oligoastrocytoma": {
          "meaning": "ncit:C6959",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Anaplastic Oligodendroglioma": {
          "meaning": "ncit:C4326",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Angiocentric Glioma": {
          "meaning": "icdo:9431/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Astroblastoma, MN1-Altered": {
          "meaning": "ncit:C4324",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Astrocytoma Tumors": {
          "meaning": "ncit:C60781",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'"
          ]
        },
        "Astrocytoma With Piloid Features": {
          "meaning": "ncit:C185879",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Astrocytoma, IDH-Mutant": {
          "meaning": "ncit:C185167",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Atypical Choroid Plexus Papilloma": {
          "meaning": "ncit:C53686",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'"
          ]
        },
        "Atypical Teratoid/Rhabdoid Tumor, MYC Gene (ATRT-MYC)": {
          "meaning": "ncit:C200599",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'"
          ]
        },
        "Atypical Teratoid/Rhabdoid Tumor, NOS or NEC": {
          "meaning": "ncit:C6906",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'"
          ]
        },
        "Atypical Teratoid/Rhabdoid Tumor, Sonic Hedgehog (ATRT-SHH)": {
          "meaning": "ncit:C200598",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'"
          ]
        },
        "Atypical Teratoid/Rhabdoid Tumor, Tyrosinase Gene (ATRT-TYR)": {
          "meaning": "ncit:C200600",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Atypical Teratoid/Rhabdoid Tumor'"
          ]
        },
        "CIC-Rearranged Sarcoma": {
          "meaning": "ncit:C120224",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "CNS Germinoma": {
          "meaning": "ncit:C7009",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'CNS Germ Cell Tumors'"
          ]
        },
        "CNS Non-Germinomatous Germ Cell Tumor": {
          "meaning": "ncit:C100093",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'CNS Germ Cell Tumors'"
          ]
        },
        "Central Nervous System B-Cell Non-Hodgkin Lymphoma": {
          "meaning": "ncit:C147948",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Central Nervous System Mature T-Cell and NK-Cell Non-Hodgkin Lymphoma": {
          "meaning": "ncit:C129600",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Central Neurocytoma": {
          "meaning": "ncit:C3791",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Cerebellar Liponeurocytoma": {
          "meaning": "ncit:C6905",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Chondrosarcoma": {
          "meaning": "ncit:C2946",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Chordoma": {
          "meaning": "ncit:C2947",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Choroid Plexus Carcinoma": {
          "meaning": "ncit:C4715",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'"
          ]
        },
        "Choroid Plexus Papilloma": {
          "meaning": "ncit:C3698",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'"
          ]
        },
        "Desmoplastic Myxoid Tumor of the Pineal Region  SMARCB1-Mutant": {
          "meaning": "ncit:C178507",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Diffuse Astrocytoma,\u00a0MYB- Or\u00a0MYBL1-Altered": {
          "meaning": "ncit:C129274",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Diffuse Glioneuronal Tumor with Oligodendroglioma-Like Features and Nuclear Clusters": {
          "meaning": "ncit:C185935",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Diffuse Hemispheric Glioma, H3 G34-Mutant": {
          "meaning": "ncit:C185371",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Diffuse Leptomeningeal Glioneuronal Tumor": {
          "meaning": "icdo:9509/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Diffuse Low-Grade Glioma, MAPK Pathway-Altered": {
          "meaning": "ncit:C185218",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Diffuse Midline Glioma, H3 K27-Altered": {
          "meaning": "ncit:C185368",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Diffuse Pediatric-Type High-Grade Glioma, H3-Wildtype And IDH-Wildtype": {
          "meaning": "ncit:C185467",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Dural Extranodal Marginal Zone Lymphoma of Mucosa-Associated Lymphoid Tissue": {
          "meaning": "ncit:C95991",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Dysembryoplastic Neuroepithelial Tumor": {
          "meaning": "icdo:9413/0",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Dysplastic Cerebellar Gangliocytoma": {
          "meaning": "ncit:C8419",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Embryonal Tumor with Multilayered Rosettes, C19MC Amplified": {
          "meaning": "ncit:C186534",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Embryonal Tumor with Multilayered Rosettes, C19MC Not Amplified": {
          "meaning": "ncit:C4915",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Embryonal Tumor with Multilayered Rosettes, NOS or NEC": {
          "meaning": "ncit:C186534",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Erdheim-Chester Disease": {
          "meaning": "icdo:9749/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Ewing Sarcoma": {
          "meaning": "icdo:9260/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Extraventricular Neurocytoma": {
          "meaning": "ncit:C92555",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Gangliocytoma": {
          "meaning": "icdo:9492/0",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Ganglioglioma": {
          "meaning": "ncit:C3788",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Giant Cell Astrocytoma": {
          "meaning": "ncit:C3696",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Glioblastoma, IDH-Wildtype": {
          "meaning": "ncit:C39750",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Glioneuronal and Neuronal Tumors": {
          "meaning": "ncit:C4747",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Gliosarcoma": {
          "meaning": "icdo:9442/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Hemangioblastoma": {
          "meaning": "icdo:9161/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Hemangiomas and Vascular Malformations": {
          "meaning": "",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "High-Grade Glioma, NOS or NEC": {
          "meaning": "ncit:C4822",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Histiocytic Sarcoma": {
          "meaning": "ncit:C27349",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Hybrid Nerve Sheath Tumor": {
          "meaning": "ncit:C121686",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Immunodeficiency-Related Central Nervous System Lymphoma": {
          "meaning": "ncit:C186658",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Infant-Type Hemispheric Glioma": {
          "meaning": "ncit:C185471",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Intracranial Mesenchymal Tumor  FET-CREB Fusion-Positive": {
          "meaning": "ncit:C186614",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Intravascular Large B-Cell Lymphoma": {
          "meaning": "icdo:9712/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Juvenile Xanthogranuloma": {
          "meaning": "icdo:9749/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Langerhans Cell Histiocytosis": {
          "meaning": "ncit:C3107",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Low-Grade Glioma, NOS or NEC": {
          "meaning": "ncit:C132067",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Lymphomatoid Granulomatosis": {
          "meaning": "ncit:C7930",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Malignant Melanotic Nerve Sheath Tumor": {
          "meaning": "ncit:C4748",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "icdo:9540/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Medulloblastoma, Classic": {
          "meaning": "ncit:C54039",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, Group 3": {
          "meaning": "ncit:C129445",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, Group 4": {
          "meaning": "ncit:C129446",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, Large Cell/Anaplastic": {
          "meaning": "ncit:C129436",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, NOS or NEC": {
          "meaning": "ncit:C3222",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, Nodular Desmoplastic": {
          "meaning": "ncit:C4956",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, Non-WNT/Non-SHH": {
          "meaning": "ncit:C129444",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, SHH-Activated and\u00a0TP53-Mutant": {
          "meaning": "ncit:C129442",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, SHH-Activated and\u00a0TP53-Wildtype": {
          "meaning": "ncit:C129443",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Medulloblastoma, WNT-Activated": {
          "meaning": "ncit:C129440",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Medulloblastoma'"
          ]
        },
        "Meningioma": {
          "meaning": "ncit:C3230",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Mesenchymal Chondrosarcoma": {
          "meaning": "icdo:9240/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Multinodular and Vacuolated Neuronal Tumor": {
          "meaning": "ncit:C129427",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Myxoid Glioneuronal Tumor": {
          "meaning": "ncit:C179229",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Myxopapillary Ependymoma": {
          "meaning": "ncit:C3697",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Neurofibroma": {
          "meaning": "ncit:C3272",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Oligoastrocytic Tumors": {
          "meaning": "ncit:C186217",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'"
          ]
        },
        "Oligoastrocytoma": {
          "meaning": "ncit:C4050",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Oligodendroglial Tumors": {
          "meaning": "ncit:C103050",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma' OR 'Low-Grade Glioma'"
          ]
        },
        "Oligodendroglioma, IDH-Mutant, And 1P/19Q-Codeleted": {
          "meaning": "ncit:C129318",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Papillary Craniopharyngioma": {
          "meaning": "icdo:9352/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'"
          ]
        },
        "Papillary Glioneuronal Tumor": {
          "meaning": "icdo:9509/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Papillary Tumor of the Pineal Region": {
          "meaning": "ncit:C92624",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Paraganglioma": {
          "meaning": "ncit:C3308",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Perineurioma": {
          "meaning": "ncit:C4973",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pilocytic Astrocytoma": {
          "meaning": "icdo:9421/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Pilomyxoid Astrocytoma": {
          "meaning": "icdo:9425/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Pineal Parenchymal Tumor of Intermediate Differentiation": {
          "meaning": "ncit:C6967",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pineal Tumors": {
          "meaning": "ncit:C41834",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineoblastoma, MYC/FOXR2": {
          "meaning": "ncit:C201973",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineoblastoma, MiRNA1": {
          "meaning": "ncit:C201967",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineoblastoma, MiRNA2": {
          "meaning": "ncit:C201968",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineoblastoma, NOS or NEC": {
          "meaning": "ncit:C9344",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineoblastoma, RB1": {
          "meaning": "ncit:C201969",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other CNS Embryonal tumors'"
          ]
        },
        "Pineocytoma": {
          "meaning": "icdo:9361/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pituitary Gland Blastoma": {
          "meaning": "ncit:C155304",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pituitary Neuroendocrine Tumor": {
          "meaning": "ncit:C3329",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pleomorphic Xanthoastrocytoma": {
          "meaning": "icdo:9424/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Polymorphous Low-Grade Neuroepithelial Tumor Of The Young": {
          "meaning": "ncit:C180378",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Posterior Fossa Ependymoma": {
          "meaning": "ncit:C186443",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Posterior Fossa Ependymoma, Group PFA": {
          "meaning": "ncit:C186450",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Posterior Fossa Ependymoma, Group PFB": {
          "meaning": "ncit:C186451",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Posterior Pituitary Gland Neoplasm": {
          "meaning": "ncit:C7157",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Primary Diffuse Large B-Cell Lymphoma of the Central Nervous System": {
          "meaning": "ncit:C71720",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Primary Intracranial Sarcoma  DICER1-Mutant": {
          "meaning": "ncit:C186610",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Primary Meningeal Melanocytic Neoplasm": {
          "meaning": "ncit:C4661",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Rhabdomyosarcoma": {
          "meaning": "ncit:C3359",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Rosai-Dorfman Disease": {
          "meaning": "ncit:C36075",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Rosette-Forming Glioneuronal Tumor": {
          "meaning": "ncit:C129431",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Schwannoma": {
          "meaning": "ncit:C3269",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Solitary Fibrous Tumor": {
          "meaning": "ncit:C7634",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Spinal Ependymoma": {
          "meaning": "ncit:C3875",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Spinal Ependymoma,\u00a0MYCN-Amplified": {
          "meaning": "ncit:C186494",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Subependymal Giant Cell Astrocytoma": {
          "meaning": "ncit:C3696",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Subependymoma": {
          "meaning": "icdo:9383/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Supratentorial Ependymoma": {
          "meaning": "ncit:C186343",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Supratentorial Ependymoma, YAP1 fusion-positive": {
          "meaning": "ncit:C186351",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Supratentorial Ependymoma, ZFTA fusion-positive": {
          "meaning": "ncit:C186350",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Cytology": {
          "meaning": "ncit:C16491",
          "comments": []
        },
        "Liquid Biopsy": {
          "meaning": "ncit:C135727",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "Physical Examination": {
          "meaning": "ncit:C20989",
          "comments": []
        },
        "Surgical Pathology": {
          "meaning": "ncit:C16958",
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
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Basal Ganglia-Thalamus": {
          "meaning": "ncit:C158080",
          "comments": []
        },
        "Cauda Equina Spinal Cord": {
          "meaning": "ncit:C12689",
          "comments": []
        },
        "Cerebellum": {
          "meaning": "ncit:C12445",
          "comments": []
        },
        "Cervical Spine": {
          "meaning": "ncit:C69313",
          "comments": []
        },
        "Extra CNS": {
          "meaning": "",
          "comments": []
        },
        "Fourth Ventricle": {
          "meaning": "ncit:C12828",
          "comments": []
        },
        "Frontal Lobe": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Lateral Ventricle": {
          "meaning": "ncit:C12834",
          "comments": []
        },
        "Leptomeningeal": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Lumbar Spinal Cord": {
          "meaning": "ncit:C12895",
          "comments": []
        },
        "Medulla": {
          "meaning": "ncit:C12442",
          "comments": []
        },
        "Midbrain": {
          "meaning": "ncit:C12510",
          "comments": []
        },
        "Occipital Lobe": {
          "meaning": "ncit:C12355",
          "comments": []
        },
        "Optic Chiasm": {
          "meaning": "ncit:C90609",
          "comments": []
        },
        "Optic Nerve": {
          "meaning": "ncit:C12761",
          "comments": []
        },
        "Parietal Lobe": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Pons": {
          "meaning": "ncit:C12511",
          "comments": []
        },
        "Suprasellar Pituitary": {
          "meaning": "ncit:C95445",
          "comments": []
        },
        "Temporal Lobe": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Third Ventricle": {
          "meaning": "ncit:C12827",
          "comments": []
        },
        "Thoracic Spinal Cord": {
          "meaning": "ncit:C12894",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "RtDataSourceEnum": {
      "permissible_values": {
        "Protocol Prescribed": {
          "meaning": "",
          "comments": []
        },
        "Treatment Summary": {
          "meaning": "",
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
        "Cytogenetics, Microarray, SNP Array": {
          "meaning": "ncit:C116151",
          "comments": []
        },
        "Cytogenetics, Microarray, aCGH": {
          "meaning": "ncit:C18084",
          "comments": []
        },
        "DNA Methylation, Array": {
          "meaning": "ncit:C165222",
          "comments": []
        },
        "Expression Profiling, Nanostring": {
          "meaning": "",
          "comments": []
        },
        "Sequencing, NGS, NOS": {
          "meaning": "ncit:C101293",
          "comments": []
        },
        "Sequencing, NGS, Single Gene (DNA)": {
          "meaning": "",
          "comments": []
        },
        "Sequencing, NGS, Targeted DNA Panel": {
          "meaning": "ncit:C158253",
          "comments": []
        },
        "Sequencing, NGS, Targeted RNA Panel": {
          "meaning": "ncit:C158252",
          "comments": []
        },
        "Sequencing, NGS, Total RNA": {
          "meaning": "ncit:C124261",
          "comments": []
        },
        "Sequencing, NGS, Whole Exome": {
          "meaning": "ncit:C101295",
          "comments": []
        },
        "Sequencing, NGS, Whole Genome": {
          "meaning": "ncit:C101294",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "CNS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Abemaciclib": {
          "meaning": "ncit:C97660",
          "comments": []
        },
        "Akt Inhibitor MK2206": {
          "meaning": "ncit:C90581",
          "comments": []
        },
        "Antineoplaston A10": {
          "meaning": "ncit:C1004",
          "comments": []
        },
        "Antineoplaston AS2-1": {
          "meaning": "ncit:C1613",
          "comments": []
        },
        "Arsenic Trioxide": {
          "meaning": "ncit:C1005",
          "comments": []
        },
        "Atorvastatin": {
          "meaning": "ncit:C61527",
          "comments": []
        },
        "BXQ-350 Nanovesicle Formulation": {
          "meaning": "ncit:C131491",
          "comments": []
        },
        "Belinostat": {
          "meaning": "ncit:C48812",
          "comments": []
        },
        "Bevacizumab": {
          "meaning": "rxcui:253337",
          "comments": []
        },
        "Bismaleimide sulfoxide (BMSO)": {
          "meaning": "",
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
        "Cabazitaxel": {
          "meaning": "ncit:C66937",
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
        "Carbogen": {
          "meaning": "ncit:C1038",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Cediranib": {
          "meaning": "ncit:C80867",
          "comments": []
        },
        "Celecoxib": {
          "meaning": "ncit:C1728",
          "comments": []
        },
        "Cetuximab": {
          "meaning": "rxcui:318341",
          "comments": []
        },
        "Cilengitide": {
          "meaning": "ncit:C1834",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Corticorelin Acetate": {
          "meaning": "ncit:C76112",
          "comments": []
        },
        "Crenolanib": {
          "meaning": "ncit:C64639",
          "comments": []
        },
        "Crizotinib": {
          "meaning": "ncit:C74061",
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
        "Dabrafenib": {
          "meaning": "rxcui:1424911",
          "comments": []
        },
        "Dasatinib": {
          "meaning": "ncit:C38713",
          "comments": []
        },
        "Dordaviprone": {
          "meaning": "ncit:C113792",
          "comments": []
        },
        "Doxycycline Hyclate": {
          "meaning": "ncit:C29007",
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
        "Everolimus": {
          "meaning": "rxcui:141704",
          "comments": []
        },
        "Fenofibrate": {
          "meaning": "ncit:C29047",
          "comments": []
        },
        "Firtecan Pegol": {
          "meaning": "ncit:C70651",
          "comments": []
        },
        "Gadolinium": {
          "meaning": "ncit:C39765",
          "comments": []
        },
        "Gefitinib": {
          "meaning": "ncit:C1855",
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
        "Imatinib Mesylate": {
          "meaning": "ncit:C1687",
          "comments": []
        },
        "Imetelstat": {
          "meaning": "ncit:C49084",
          "comments": []
        },
        "Indoximod": {
          "meaning": "ncit:C71535",
          "comments": []
        },
        "Intron": {
          "meaning": "ncit:C13249",
          "comments": []
        },
        "Ipilimumab": {
          "meaning": "ncit:C2654",
          "comments": []
        },
        "Irinotecan": {
          "meaning": "ncit:C62040",
          "comments": []
        },
        "Isotretinoin": {
          "meaning": "ncit:C603",
          "comments": []
        },
        "Itacnosertib": {
          "meaning": "ncit:C156729",
          "comments": []
        },
        "Labradimil": {
          "meaning": "ncit:C1606",
          "comments": []
        },
        "Lapatinib": {
          "meaning": "ncit:C26653",
          "comments": []
        },
        "Laromustine": {
          "meaning": "ncit:C2653",
          "comments": []
        },
        "Larotrectinib": {
          "meaning": "rxcui:2105628",
          "comments": []
        },
        "Lenalidomide": {
          "meaning": "ncit:C2668",
          "comments": []
        },
        "Lomustine": {
          "meaning": "rxcui:6466",
          "comments": []
        },
        "Lonafarnib": {
          "meaning": "ncit:C1829",
          "comments": []
        },
        "Mebendazole": {
          "meaning": "ncit:C47595",
          "comments": []
        },
        "Mechlorethamine": {
          "meaning": "rxcui:6674",
          "comments": []
        },
        "Melphalan": {
          "meaning": "rxcui:6718",
          "comments": []
        },
        "Metformin": {
          "meaning": "ncit:C61612",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Mitoxantrone": {
          "meaning": "rxcui:7005",
          "comments": []
        },
        "Motexafin Gadolinium": {
          "meaning": "ncit:C1881",
          "comments": []
        },
        "Nimotuzumab": {
          "meaning": "ncit:C2733",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "O6-Benzylguanine": {
          "meaning": "ncit:C1306",
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
        "Palbociclib": {
          "meaning": "ncit:C49176",
          "comments": []
        },
        "Panobinostat": {
          "meaning": "ncit:C66948",
          "comments": []
        },
        "Pazopanib": {
          "meaning": "rxcui:714438",
          "comments": []
        },
        "Pemetrexed": {
          "meaning": "ncit:C61614",
          "comments": []
        },
        "Perifosine": {
          "meaning": "ncit:C1727",
          "comments": []
        },
        "Pomalidomide": {
          "meaning": "ncit:C72560",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Prexasertib": {
          "meaning": "ncit:C91392",
          "comments": []
        },
        "Procarbazine": {
          "meaning": "rxcui:8702",
          "comments": []
        },
        "Procarbazine Hydrochloride": {
          "meaning": "ncit:C773",
          "comments": []
        },
        "Pseudomonas Exotoxin Immunoconjugate": {
          "meaning": "ncit:C78532",
          "comments": []
        },
        "Rebeccamycin": {
          "meaning": "ncit:C1213",
          "comments": []
        },
        "Recombinant Human Hyaluronidase and Pembrolizumab": {
          "meaning": "ncit:C200181",
          "comments": []
        },
        "Ribociclib": {
          "meaning": "rxcui:1873986",
          "comments": []
        },
        "Ridaforolimus": {
          "meaning": "ncit:C49061",
          "comments": []
        },
        "Satraplatin": {
          "meaning": "ncit:C1493",
          "comments": []
        },
        "Savolitinib": {
          "meaning": "ncit:C104732",
          "comments": []
        },
        "Semaxanib": {
          "meaning": "ncit:C11778",
          "comments": []
        },
        "Sirolimus": {
          "meaning": "rxcui:35302",
          "comments": []
        },
        "Sodium Phenylbutyrate": {
          "meaning": "ncit:C1440",
          "comments": []
        },
        "Sorafenib": {
          "meaning": "ncit:C61948",
          "comments": []
        },
        "Sunitinib": {
          "meaning": "rxcui:357977",
          "comments": []
        },
        "Tamoxifen": {
          "meaning": "rxcui:10324",
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
        "Thalidomide": {
          "meaning": "ncit:C1844",
          "comments": []
        },
        "Thioguanine": {
          "meaning": "ncit:C876",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "rxcui:10473",
          "comments": []
        },
        "Tipifarnib": {
          "meaning": "ncit:C1703",
          "comments": []
        },
        "Topotecan": {
          "meaning": "rxcui:57308",
          "comments": []
        },
        "Toxin": {
          "meaning": "ncit:C894",
          "comments": []
        },
        "Trametinib": {
          "meaning": "ncit:C1413",
          "comments": []
        },
        "Trastuzumab": {
          "meaning": "rxcui:224905",
          "comments": []
        },
        "Tretinoin": {
          "meaning": "ncit:C900",
          "comments": []
        },
        "Valproate": {
          "meaning": "ncit:C181410",
          "comments": []
        },
        "Valproic Acid": {
          "meaning": "ncit:C29536",
          "comments": []
        },
        "Vandetanib": {
          "meaning": "ncit:C2737",
          "comments": []
        },
        "Vinblastine": {
          "meaning": "rxcui:11198",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
          "comments": []
        },
        "Vinorelbine": {
          "meaning": "rxcui:39541",
          "comments": []
        },
        "Vismodegib": {
          "meaning": "ncit:C933",
          "comments": []
        },
        "Vorinostat": {
          "meaning": "ncit:C74038",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        }
      }
    },
    "OutcomeEnum": {
      "permissible_values": {
        "Indeterminate": {
          "meaning": "ncit:C48658",
          "comments": []
        },
        "Non-Viable Tumor": {
          "meaning": "",
          "comments": []
        },
        "Viable Tumor": {
          "meaning": "",
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
        "11-C-0161:Arm 1 (AZD6244)": {
          "meaning": "",
          "comments": []
        },
        "11-C-0161:Arm 2 (AZD6244)": {
          "meaning": "",
          "comments": []
        },
        "15-C-0093:Phase I (Turalio)": {
          "meaning": "",
          "comments": []
        },
        "15-C-0093:Phase II (Turalio)": {
          "meaning": "",
          "comments": []
        },
        "A3973:Arm I (unpurged PBSC collection) (carboplatin, cisplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, isotretinoin, melphalan, topotecan hydrochloride, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "A3973:Arm II (unpurged PBSC collection) (carboplatin, cisplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, isotretinoin, melphalan, topotecan hydrochloride, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group 0 Induction Therapy (Cytarabine, Daunorubicin Hydrochloride, Methotrexate, Pegaspargase, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group 1 Arm IV (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Mercaptopurine, Methotrexate, Nelarabine, Pegaspargase,)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm I (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Leucovorin Calcium, Mercaptopurine, Methotrexate, Pegaspargase, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm I (Delayed intensification chemotherapy (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm I (Interim maintenance chemotherapy) (Leucovorin Calcium, Methotrexate, Pegaspargase, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm I (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm II (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Mercaptopurine, Methotrexate, Nelarabine, Pegaspargase, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm II (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Nelarabine, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm II (Interim maintenance chemotherapy) (Asparaginase, Methotrexate, Pegaspargase, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm II (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Nelarabine, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm III (Consolidation chemotherapy) (Cyclophosphamide, Cytarabine, Leucovorin Calcium, Mercaptopurine, Methotrexate, Pegaspargase, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm III (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm III (Interim maintenance chemotherapy) (Leucovorin Calcium, Mercaptopurine, Methotrexate, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm III (Maintenance chemotherapy) (Methotrexate, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm IV (Delayed intensification chemotherapy) (Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Methotrexate, Nelarabine, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm IV (Interim maintenance chemotherapy) (Leucovorin Calcium, Mercaptopurine, Methotrexate, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL0434:Group I Arm IV (Maintenance chemotherapy) (Mercaptopurine, Methotrexate, Nelarabine, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:Arm A (SR-Avg control) (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisone, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:Arm B (SR-Avg experimental) (Asparaginase Erwinia chrysanthemi, Blinatumomab, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:Arm C (SR-High Control) (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:Arm D (SR-High experimental) (Asparaginase Erwinia chrysanthemi, Blinatumomab, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:B-LLy (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Thioguanine, Vincristine Sulfate,)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:DS B-ALL (Asparaginase Erwinia chrysanthemi, Cyclophosphamide, Cytarabine, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Thioguanine, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AALL1731:NCI SR or HR DS B-ALL (Asparaginase Erwinia chrysanthemi, Blinatumomab, Dexamethasone, Doxorubicin Hydrochloride, Leucovorin Calcium, Mercaptopurine, Mercaptopurine Oral Suspension, Methotrexate, Pegaspargase, Prednisolone, Prednisone, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AAML03P1:N/A (asparaginase, busulfan, cyclophosphamide, cyclosporine, cytarabine, daunorubicin hydrochloride, etoposide, gemtuzumab ozogamicin, methotrexate, mitoxantrone hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm A: Standard Arm - No GMTZ, AML Patients with Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, mitoxantrone hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm A: Standard Arm - No GMTZ, AML Pts w/out Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, mitoxantrone hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "AAML0531:Arm B: Experimental - with GMTZ, AML Pts w/out Down Syndrome (asparaginase, cytarabine, daunorubicin hydrochloride, etoposide, gemtuzumab ozogamicin, gemtuzumab ozogamicin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0121:GTR (radiation only)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0121:GTR Supratentorial Differentiated (observation)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0121:STR (interim chemotherapy/second look surgery) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0122:Induction and Consolidation (High dose chemotherapy) (carboplatin, etoposide, ifosfamide, Thiotepa)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0122:Induction only (No high-dose therapy) (carboplatin, etoposide, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0232:Regimen A (Radiotherapy Alone)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0232:Regimen B (Cycles 1 and 2 only) (Carboplatin, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0232:Regimen B (MRD/PR/SD = 4 cycles) (Carboplatin, Etoposide, Cisplatin, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm I (3-7 years of age, LDCSI, IFRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm I (3-7 years of age, LDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm II (3-7 years of age, LDCSI, PFRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm II (3-7 years of age, LDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm III (3-7 years of age, SDCSI, IFRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm III (3-7 years of age, SDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm IV (3-7 years of age, SDCSI, PFRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm IV (3-7 years of age, SDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm V (8-21 years of age, SDCSI, IFRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm V (8-21 years of age, SDCSI, IFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm VI (8-21 years of age, SDCSI, PFRT": {
          "meaning": "",
          "comments": []
        },
        "ACNS0331:Arm VI (8-21 years of age, SDCSI, PFRT) (Cisplatin, Lomustine, Vincristine, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Arm A": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Arm B (Carboplatin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Arm C (Isotretinoin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Arm D (Carboplatin and Isotretinoin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Regimen A (no carboplatin, no isotretinoin) (Cisplatin, Cyclophosphamide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Regimen B (carboplatin, no isotretinoin) (Carboplatin, Cisplatin, Cyclophosphamide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Regimen C (no carboplatin, isotretinoin) (Cisplatin, Cyclophosphamide, Vincristine, Isotretinoin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0332:Regimen D (carboplatin, isotretinoin) (Carboplatin, Cisplatin, Cyclophosphamide, Vincristine, Isotretinoin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0333:Arm I (Chemotherapy, Autologous PBSC, 3D-CRT)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0333:Arm I (chemotherapy, autologous PBSC, 3D-CRT) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Filgrastim, Leucovorin Calcium, Methotrexate, Thiotepa, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0333:Arm II (Chemotherapy, 3D-CRT, Autologous PBSC)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0333:Arm II (chemotherapy, 3D-CRT, autologous PBSC) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Filgrastim, Leucovorin Calcium, Methotrexate, Thiotepa, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0334:Arm A (Induction+Consolidation Chemotherapy, Autologous PBSC)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0334:Arm B (Induction+Consolidation Chemotherapy, Autologous PBSC)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0334:Regimen A (Cisplatin, Cyclophosphamide, Vincristine, Etoposide, Carboplatin, Thiotepa, ASCR)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0334:Regimen B (Methotrexate, Cisplatin, Cyclophosphamide, Vincristine, Etoposide, Carboplatin, Thiotepa, ASCR)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0821:TEMO+IRIN (Temozolomide, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0821:TEMO+IRIN+BEVA (Temozolomide, Irinotecan, Bevacizumab)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Arm I (Vorinostat) (Vorinostat, Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Arm II (Temozolomide) (Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Arm III (Bevacizumab) (Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Arm IV (temozolomide) (Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Arm V (vorinostat/bevacizumab (Vorinostat, Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0822:Feasibility (vorinostat) (Vorinostat, Bevacizumab, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:Arm I (radiotherapy, chemotherapy) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:Arm II (radiotherapy, chemotherapy) (Vincristine, Cyclophosphamide, Etoposide, Cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:Arm III (radiotherapy, observation)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:GTR (Randomized to Maintenance Chemotherapy) (Vincristine, Cisplatin, Cyclophosphamide, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:GTR (Randomized to No Chemotherapy)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:STR (Induction only) (Vincristine, Carboplatin, Cyclophosphamide, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS0831:STR Differentiated (observation)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1022:Arm I (low-dose lenalidomide) (Lenalidomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1022:Arm II (high-dose lenalidomide) (Lenalidomide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1123:Stratum 1 (NGGCT) (carboplatin, etoposide, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1123:Stratum 2 (Germinoma) (carboplatin, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1831:Arm 1 (Carboplatin, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1831:Arm 2 (Selumetinib)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1833:Arm 1 (Carboplatin, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1833:Arm 2 (Selumetinib)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1931:Active Comparator: Efficacy Phase Arm II (selumetinib) (Selumetinib Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ACNS1931:Experimental: Feasibility & Efficacy Phase Arm I (selumetinib, vinblastine) (Selumetinib, Vinblastine)": {
          "meaning": "",
          "comments": []
        },
        "ACNS2021:Plan A (WVSCI - whole ventricular and spinal canal radiation) (Carboplatin, Etoposide, Ifosfamide, Mesna)": {
          "meaning": "",
          "comments": []
        },
        "ACNS2021:Plan B (HDCSCR- high dose chemotherapy with stem cell rescue) (Carboplatin, Etoposide, Ifosfamide, Mesna, Thiotepa)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0416:ARM I (vorinostat)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0416:ARM II (vorinostat)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0416:ARM III (vorinostat, isotretinoin)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0612:PART A (sunitinib malate)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0612:PART B (sunitinib malate)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm I (neuroblastoma- measurable) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm II (Neuroblastoma- MIBG evaluable) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm III (rhabdomyosarcoma) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm IV (osteosarcoma) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm IX (Wilms tumor) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm V (Ewing sarcoma/peripheral PNET) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm VI (non-RMS soft tissue sarcoma) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm VII (hepatoblastoma) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm VIII (malignant germ cell tumor) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm X (acute lymphoblastic leukemia) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm XI (acute myelogenous leukemia) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921:Arm XII (rhabdoid malignancy) (Alisertib)": {
          "meaning": "",
          "comments": []
        },
        "ADVL1411:Phase 1 (talazoparib, temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "ADVL1411:Phase 2 (talazoparib, temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "AEWS0031:Regimen A (cyclophosphamide, doxorubicin hydrochloride, etoposide, ifosfamide, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AEWS0031:Regimen B (cyclophosphamide, doxorubicin hydrochloride, etoposide, ifosfamide, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AEWS1031:Arm A (combination chemotherapy) (Cyclophosphamide, Dexrazoxane, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AEWS1031:Arm B (combination chemotherapy, topotecan hydrochloride) (Cyclophosphamide, Dexrazoxane, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Topotecan Hydrochloride, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "AG881-C-004:Experimental: Vorasidenib (Vorasidenib)": {
          "meaning": "",
          "comments": []
        },
        "AG881-C-004:Placebo Comparator: Matching Placebo (Matching Placebo)": {
          "meaning": "",
          "comments": []
        },
        "AGCT0132:Arm 2": {
          "meaning": "",
          "comments": []
        },
        "AGCT0132:Arm I (cisplatin, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531:Arm I (bleomycin, carboplatin, etoposide) (Carboplatin, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531:Arm II (bleomycin, etoposide, cisplatin) (Cisplatin, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531:Arm III (bleomycin, etoposide, carboplatin) (Carboplatin, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531:Arm IV (bleomycin, etoposide, cisplatin) (Cisplatin, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531:Low-Risk (observation)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1532:Arm A: TIP (paclitaxel, ifosfamide, cisplatin, pegylated G-CSF, G-CSF)": {
          "meaning": "",
          "comments": []
        },
        "AGCT1532:Arm B: TI-CE (paclitaxel, ifosfamide, pegylated G-CSF, G-CSF, carboplatin, etoposide phosphate,)": {
          "meaning": "",
          "comments": []
        },
        "ANBL0531:Group 2 (chemotherapy, surgery) (carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)": {
          "meaning": "",
          "comments": []
        },
        "ANBL0531:Group 3 (chemotherapy, surgery) (carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)": {
          "meaning": "",
          "comments": []
        },
        "ANBL0531:Group 4 (chemotherapy, surgery, antineoplastic therapy) (Isotretinoin, carboplatin, cyclophosphamide, doxorubicin hydrochloride, etoposide, topotecan hydrochloride, Filgrastim)": {
          "meaning": "",
          "comments": []
        },
        "ANBL0531:Non-intermediate risk enrolled on intermediate risk trial": {
          "meaning": "",
          "comments": []
        },
        "ANBL0532:Consolidation Arm A: single myeloablative consolidation (Carboplatin, Cisplatin, Cyclophosphamide, Doxorubicin Hydrochloride, Etoposide, Filgrastim, Isotretinoin, Melphalan, Topotecan Hydrochloride, Vincristine Sulfate Liposome)": {
          "meaning": "",
          "comments": []
        },
        "ANBL0532:Consolidation Arm B: tandem myeloablative consolidation (Carboplatin, Cisplatin, Cyclophosphamide, Doxorubicin Hydrochloride, Etoposide, Filgrastim, Isotretinoin, Melphalan, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate Liposome)": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531:Arm A (chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531:Arm B (Iobenguane I-131, chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531:Arm C (Iobenguane I-131, chemotherapy, BuMel, HSCT, EBRT) (Busulfan, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Melphalan Hydrochloride, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531:Arm D (chemotherapy, HSCT, EBRT) (Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride, Vincristine Sulfate,)": {
          "meaning": "",
          "comments": []
        },
        "ANBL1531:Arm E (crizotinib, chemotherapy, HSCT, EBRT) (Crizotinib, Carboplatin, Cisplatin, Cyclophosphamide, Dexrazoxane Hydrochloride, Dinutuximab, Doxorubicin Hydrochloride, Etoposide Phosphate, Isotretinoin, Sargramostim, Thiotepa, Topotecan Hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "ANHL0131:Experimental: Consolidation with Vinblastine (doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ANHL0131:Standard APO with Vincristine (Arm I) (doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ANHL01P1:Group B (chemotherapy, protective therapy, monoclonal antib.) (doxorubicin hydrochloride, cyclophosphamide, methotrexate, rasburicase, leucovorin calcium, prednisone, methylprednisolone, cytarabine, vincristine sulfate, hydrocortisone sodium succinate)": {
          "meaning": "",
          "comments": []
        },
        "ANHL01P1:Group C (Chemotherapy, monoclonal antibody therapy) (doxorubicin hydrochloride, cyclophosphamide, methotrexate, leucovorin calcium, prednisone, methylprednisolone, cytarabine, etoposide, vincristine sulfate, hydrocortisone sodium succinate)": {
          "meaning": "",
          "comments": []
        },
        "AOST0331:Maintenance therapy group 1 arm I (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "AOST0331:Maintenance therapy group 1 arm II (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "AOST0331:Maintenance therapy group 2 arm I (Cisplatin, Doxorubicin Hydrochloride, Methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "AOST0331:Maintenance therapy group 2 arm II (Cisplatin, Doxorubicin Hydrochloride, Etoposide, Ifosfamide, Methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotcol M (HRAS gene alterations) (Tipifarnib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol A (NTRK1, NTRK2, or NTRK3 gene fusion) (Larotrectinib Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol B (FGFR1, FGFR2, FGFR3, or FGFR4 gene mutation) (Erdafitinib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol C (EZH2, SMARCB1, or SMARCA4 gene mutation) (Tazemetostat)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol D (TSC1, TSC2, or PI3K/mTOR gene mutation) (Samotolisib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol E (activating MAPK pathway gene mutation) (Selumetinib Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol F (ALK or ROS1 gene alteration) (Ensartinib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol G (BRAF V600 gene mutation) (Vemurafenib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol H (ATM, BRCA1, BRCA2, RAD51C, RAD51D mutations) (Olaparib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol I (Rb positive, alterations in cell cycle genes) (Palbociclib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol J (MAPK pathway mutations) (Ulixertinib)": {
          "meaning": "",
          "comments": []
        },
        "APEC1621:Subprotocol N (activating RET mutations) (Selpercatinib)": {
          "meaning": "",
          "comments": []
        },
        "AREN1921:Arm I (Regimen UH-3) (Carboplatin, Cyclophosphamide, Doxorubicin, Etoposide, Irinotecan, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "AREN1921:Arm II (Regimen ICE/Cyclo/Topo) (Carboplatin, Cyclophosphamide, Etoposide, Ifosfamide, Topotecan)": {
          "meaning": "",
          "comments": []
        },
        "ARET0321:Treatment (chemotherapy, radiotherapy, autologous SCI) (Carboplatin, Cisplatin, Cyclophosphamide, Etoposide, Thiotepa, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ARST0531:Arm I (chemotherapy, radiotherapy) (Cyclophosphamide, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "ARST0531:Arm II (chemotherapy, radiotherapy) (Cyclophosphamide, Irinotecan Hydrochloride, Vincristine Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-01:Arm A (tumor cavity delivery) (HER2-specific chimeric antigen receptor (CAR) T cell)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-01:Arm B (intraventricular delivery) (HER2-specific chimeric antigen receptor (CAR) T cell)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-02:Arm A (tumor cavity delivery) (EGFR806-specific chimeric antigen receptor (CAR) T cell)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-02:Arm B (intraventricular delivery) (EGFR806-specific chimeric antigen receptor (CAR) T cell)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-03:Arm A (tumor cavity delivery) (CAR-T cell targeting B7H3)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-03:Arm B (intraventricular delivery) (CAR-T cell targeting B7H3)": {
          "meaning": "",
          "comments": []
        },
        "BRAINCHILD-03:Arm C (DIPG, intraventricular delivery) (CAR-T cell targeting B7H3)": {
          "meaning": "",
          "comments": []
        },
        "BRF116013: (Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "CCG-921:Regimen A (VCR, lomustine, prednisone)": {
          "meaning": "",
          "comments": []
        },
        "CCG-921:Regimen B (VCR, methylprednisone, lomustine, hydroxyurea, procarbazine, cisplatin, cyclophosphamide, cytarabine)": {
          "meaning": "",
          "comments": []
        },
        "CCG-9921:Regimen A (vincristine, cisplatin, cyclophosphamide, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "CCG-9921:Regimen B (vincristine, carboplatin, ifosfamide, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "CCG-99701:Regimen A (carboplatin, vincristine, cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "CCG-99701:Regimen B (carboplatin, vincristine, cyclophosphamide, cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:A0 (localized disease Stg I/II) Modified CCG BFM (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:A1 (Disseminated, No CNS - CCG mod BFM w/out intens (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:A2 (Disseminated, No CNS - CCG mod BFM w/ intens (asparaginase, cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:B1 (Disseminated CNS- <Amend 7B) NHL/BFM-95 w/out intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium,)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:B1 (Disseminated CNS-) NHL/BFM-95 w/out intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:B2 (CNS+) NHL/BFM-95 w/intens delayed radiation therapy (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium,)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A5971:B2 (Disseminated,CNS- (< Amend 7B)) NHL/BFM-95 w/intens (asparaginase, cyclophosphamide, cyt mercaptopurine, methotrexate, prednisone, thioguanine, vincristine sulfatearabine, daunorubicin hydrochloride, dexamethasone, doxorubicin hydrochloride, leucovorin calcium)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9952:Regimen A (CV Chemotherapy) (carboplatin, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9952:Regimen B (TPCV Chemotherapy) (lomustine, procarbazine hydrochloride, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9961:Regimen A (cisplatin, lomustine, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CCG-A9961:Regimen B (cisplatin, cyclophosphamide, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CCG-D9803:Arm I (dactinomycin, vincristine sulfate, cyclophosphamide,)": {
          "meaning": "",
          "comments": []
        },
        "CCG-D9803:Arm II (vincristine sulfate, cyclophosphamide, topotecan hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005:Group 1": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005:Group 2 (ifosfamide , IFO-DOX)": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005:Group 3 (IFO-DOX)": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005:Group 4 (IFO-DOX, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-NRSTS-2005:Group 5 (IFO-DOX)": {
          "meaning": "",
          "comments": []
        },
        "CCLG-EPSSG-RMS-2005: ()": {
          "meaning": "",
          "comments": []
        },
        "CCMC1411:High-grade Glioma/Pontine Glioma (Mebendazole, Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "CCMC1411:Low-grade Glioma (Mebendazole, Vincristine, Carboplatin, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "CDRB436G2201:HGG cohort: Dabrafenib and trametinib (dabrafenib, Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "CDRB436G2201:LGG cohort: Carboplatin with vincristine (Carboplatin, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CDRB436G2201:LGG cohort: Dabrafenib and trametinib (dabrafenib, Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "CHP735:Consolidation (Thiotepa, Etoposide, Carboplatin)": {
          "meaning": "",
          "comments": []
        },
        "CHP735:Induction (Methrotrexate, Vincristine, Etoposide, Cyclophosphamide, Cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "CNS1100:Experimental (Busulfan)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2000:Carboplatin + Etoposide + Vincristine (Carboplatin, Etoposide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2000:Cyclophosphamide + Etoposide + Vincristine (Cyclophosphamide, Etoposide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2009:Doxorubicin/cisplatin arm (2) (Carboplatin, Cisplatin, Cyclophosphamide, Dactinomycin, Doxorubicin, Etoposide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2009:Methotrexate Arm (3) (Carboplatin, cyclophosphamide, etoposide, Leucovorin, Methotrexate, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2009:Standard Arm (1) (Carboplatin, Cyclophosphamide, etoposide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "CPT-SIOP-2009:Temozolomide Irinotecan arm (4) (Carboplatin, Cyclophosphamide, Etoposide, Irinotecan, Temozolomide, Vincristine)": {
          "meaning": "",
          "comments": []
        },
        "ChildrenHLA:Phase 1 (MEK162)": {
          "meaning": "",
          "comments": []
        },
        "ChildrenHLA:Phase 2 (MEK162)": {
          "meaning": "",
          "comments": []
        },
        "ChildrenHLA:Target Validation (MEK162)": {
          "meaning": "",
          "comments": []
        },
        "DIPG-BATS:radiation + bevacizumab (Bevacizumab)": {
          "meaning": "",
          "comments": []
        },
        "DIPG-BATS:radiation + bevacizumab + erlotinib (Bevacizumab, Erlotinib)": {
          "meaning": "",
          "comments": []
        },
        "DIPG-BATS:radiation + bevacizumab + erlotinib + temozolomide (Bevacizumab, erlotinib, temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "DIPG-BATS:radiation + bevacizumab + temozolomide (Bevacizumab, Temozolomide,)": {
          "meaning": "",
          "comments": []
        },
        "EZH-102:Open-label Tazemetostat (Tazemetostat)": {
          "meaning": "",
          "comments": []
        },
        "EZH-202:Open-label Tazemetostat (Tazemetostat)": {
          "meaning": "",
          "comments": []
        },
        "GCC1949:Core Regimen, sub-cohort A (indoximod with oral temozolomide) (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "GCC1949:Core Regimen, sub-cohort B (low-dose radiation or not all disease sites included, indoximod with oral temozolomide) (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "GCC1949:Core Regimen, sub-cohort C (palliative full-dose radiation, (indoximod with oral temozolomide)) (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "GCC1949:Salvage Regimen 1 (Cross-over to indoximod with oral metronomic cyclophosphamide and etoposide) (Indoximod, Cyclophosphamide, Etoposide)": {
          "meaning": "",
          "comments": []
        },
        "GCC1949:Salvage Regimen 2 (Cross-over to indoximod with oral lomustine and temozolomide) (Indoximod, Temozolomide, Lomustine)": {
          "meaning": "",
          "comments": []
        },
        "HGG-01:Active Comparator: Main Cohort: Chemoradiation + TMZ (Temozolomide (TMZ))": {
          "meaning": "",
          "comments": []
        },
        "HGG-01:Experimental: Bevacizumab + TMZ Young Patient Cohort (YPC) (Bevacizumab, Temozolomide (TMZ))": {
          "meaning": "",
          "comments": []
        },
        "HGG-01:Experimental: Main Cohort: Chemoradiation + Bevacizumab + TMZ (Bevacizumab, Temozolomide (TMZ))": {
          "meaning": "",
          "comments": []
        },
        "HIT-SIOP PNET 4: Hyperfractionated radiotherapy": {
          "meaning": "",
          "comments": []
        },
        "HIT-SIOP PNET 4: Standard Fractionation Regimen": {
          "meaning": "",
          "comments": []
        },
        "HSPPC-96:Newly Diagnosed High Grade Glioma (HGG)": {
          "meaning": "",
          "comments": []
        },
        "HSPPC-96:Recurrent HGG and Ependymoma": {
          "meaning": "",
          "comments": []
        },
        "Head Start 4:Induction (vincristine, cisplatin, cyclophosphamide, etoposide, high-dose methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "Head Start 4:Single Cycle Intensive Chemotherapy (Carboplatin, thiotepa, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "Head Start 4:Tandem 3 Cycle Intensive Chemotherapy (Carboplatin, thiotepa)": {
          "meaning": "",
          "comments": []
        },
        "Head Start II:Submyeloablative/consolidation chemotherapy (Carboplatin, thiotepa, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "Head Start II:induction (vincristine, cisplatin, cyclophosphamide, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "Head Start III:induction (vincristine, cisplatin, cyclophosphamide, etoposide, and high dose methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "Head Start III:myeloablative chemotherapy (thiotepa, carboplatin and etoposide)": {
          "meaning": "",
          "comments": []
        },
        "INDIGO:Experimental: Vorasidenib (Vorasidenib)": {
          "meaning": "",
          "comments": []
        },
        "INDIGO:Placebo Comparator: Matching Placebo (Matching Placebo)": {
          "meaning": "",
          "comments": []
        },
        "IRS-III:Group 1 (vincristine (V), dactinomycin (A), cyclophosphamide (C) or standard VA)": {
          "meaning": "",
          "comments": []
        },
        "IRS-III:Group 2 (intensive VA or repetitive-pulse VAC)": {
          "meaning": "",
          "comments": []
        },
        "IRS-III:Group 3 (repetitive-pulse VAC or repetitivepulse VAdrC-VAC (Adr, Adriamycin [doxorubicin]))": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 1 dose escalation: Dose expansion (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 1 dose escalation: Dose level 1_Cohort 1 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 1 dose escalation: Dose level 2_Cohort 2 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 1 dose escalation: Dose level 3_Cohort 3 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 2 expansion: Other extra-cranial solid tumors_Cohort 2 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 2 expansion: Patients with tumors bearing NTRK fusions (IFS)_Cohort 1 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 2 expansion: Primary CNS tumors_Cohort 3 (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "LOXO-TRK 15003:Phase 2 expansion: bone health assessment_sub-cohort (Larotrectinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part A - TMT 0.0125 mg/kg/day (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part A - TMT 0.025 mg/kg/day (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part A - TMT 0.032 mg/kg/day (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part A - TMT 0.04 mg/kg/day (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part B - BRAF V600 mutant solid tumor (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part B - LGG fusion (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part B - NF-1 with PN (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part B - Neuroblastoma (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part C - TMT 0.025 mg/kg/day + 100% DRB RP2D (Trametinib, Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part C - TMT 0.025 mg/kg/day + 50% DRB RP2D (Trametinib, Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part C - TMT 0.032 mg/kg/day + 100% DRB RP2D (Trametinib, Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part D - LCH (Trametinib, Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "MEK116540:Part D - LGG (Trametinib, Dabrafenib)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:MEL: Pembrolizumab 10 mg/kg Q2W (Part B) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:MEL: Pembrolizumab 10 mg/kg Q3W (Parts B+D) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:MEL: Pembrolizumab 2 mg/kg Q3W (Parts B+D) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q2W (Part F) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 10 mg/kg Q3W (Parts C+F) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 2 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 2 mg/kg Q3W (Part F) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:NSCLC: Pembrolizumab 5 mg/kg Q3W (Part E-Not Enrolled) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab 1 mg/kg Q2W (Part A) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab 10 mg/kg Q2W (Parts A+A1) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab 3 mg/kg Q2W (Part A) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 1 Q3W (Part A2) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 2 Q3W (Part A2) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MK-3475:Solid Tumors: Pembrolizumab Titration Cohort 3 Q3W (Part A2) (Pembrolizumab)": {
          "meaning": "",
          "comments": []
        },
        "MSKCC-03077:patients have no evidence of disease (anti-GD2 murine IgG3 monoclonal antibody 3F8)": {
          "meaning": "",
          "comments": []
        },
        "MSKCC-03077:patients have refractory bone marrow disease (anti-GD2 murine IgG3 monoclonal antibody 3F8)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol A (EGFR activating mutation) (Afatinib, Afatinib Dimaleate,)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol B (HER2 activating mutation) (Afatinib, Afatinib Dimaleate,)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol C1 (MET amplification) (Crizotinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol C2 (MET exon 14 deletion/mutation) (Crizotinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol E (EGFR T790M or rare activating mutation) (Osimertinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol F (ALK translocation) (Crizotinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol G (ROS1 translocation or inversion) (Crizotinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol H (BRAF V600E/R/K/D mutation) (Dabrafenib, Dabrafenib Mesylate, Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol I (PIK3CA mutation) (Taselisib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol J (HER2 amplification >= 7 copy numbers": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol K1 (FGFR amplification) (Erdafitinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol K2 (FGFR mutation or fusion) (Erdafitinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol L (mTOR mutation) (Sapanisertib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol M (TSC1 or TSC2 mutation) (Sapanisertib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol N (PTEN mutation or deletion and PTEN expression) (PI3K-beta Inhibitor GSK2636771)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol P (PTEN loss) (PI3K-beta Inhibitor GSK2636771)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Q (HER2 amplification) (Trastuzumab)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol R (BRAF fusion or BRAF non-V600 mutation) (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol S1 (NF1 mutation) (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol S2 (GNAQ or GNA11 mutation) (Trametinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol T (SMO or PTCH1 mutation) (Vismodegib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol U (NF2 inactivating mutation) (Defactinib, Defactinib,)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol V (cKIT exon 9, 11, 13, or 14 mutation) (Sunitinib Malate)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol W (FGFR pathway aberrations) (FGFR Inhibitor AZD4547)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol X (DDR2 S768R, I638F, or L239R mutation) (Dasatinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Y (Akt mutation) (Capivasertib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1A (NRAS mutation in codon 12, 13, or 61) (Binimetinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1B (CCND1, 2, or 3 amplification with Rb by IHC) (Palbociclib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1C (CDK4 or CDK6 amplification and Rb protein) (Palbociclib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1D (Loss of MLH1 or MSH2 by IHC) (Nivolumab)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1E (NTRK1, NTRK2 or NTRK3 gene fusion) (Larotrectinib, Larotrectinib Sulfate)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1F (PIK3CA mutation) (Copanlisib, Copanlisib Hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1G (PTEN loss) (Copanlisib, Copanlisib Hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1H (PTEN mutation) (Copanlisib, Copanlisib Hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1I (BRCA1 or BRCA2 gene mutation) (Adavosertib, Irinotecan Hydrochloride)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1K (AKT mutation) (Ipatasertib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1L (BRAF fusion, aberration or non-V600 mutation) (Ulixertinib)": {
          "meaning": "",
          "comments": []
        },
        "NCI-MATCH:Subprotocol Z1M (LAG-3 expression >= 1%) (Nivolumab, Relatlimab)": {
          "meaning": "",
          "comments": []
        },
        "NCT01185964:Phase 1b: Olaratumab + doxorubicin (Doxorubicin)": {
          "meaning": "",
          "comments": []
        },
        "NCT01185964:Phase 2: Doxorubicin: Optional Olaratumab After Progression (Doxorubicin)": {
          "meaning": "",
          "comments": []
        },
        "NCT01185964:Phase 2: Olaratumab and doxorubicin (Doxorubicin)": {
          "meaning": "",
          "comments": []
        },
        "NCT02924038:IMA950/poly-ICLC subQ only": {
          "meaning": "",
          "comments": []
        },
        "NCT02924038:IMA950/poly-ICLC subcutaneous (subQ) + Varlilumab IV": {
          "meaning": "",
          "comments": []
        },
        "NCT03696355:Stratum A1 (GDC0084)": {
          "meaning": "",
          "comments": []
        },
        "NCT03696355:Stratum A2 (GDC0084)": {
          "meaning": "",
          "comments": []
        },
        "NLG2105:Group 1 (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "NLG2105:Group 2 (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "NLG2105:Group 3 (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "NLG2105:Group 3b (Indoximod, Temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "NLG2105:Group 4 (Indoximod, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm A (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm B (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm C (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm D (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm E (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm F (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "ONC201:Arm G (ONC201)": {
          "meaning": "",
          "comments": []
        },
        "OZM-063:ARM A (Vinblastine)": {
          "meaning": "",
          "comments": []
        },
        "OZM-063:ARM B (Vinblastine, Bevacizumab)": {
          "meaning": "",
          "comments": []
        },
        "OZM-077:Phase I Dose-escalation (5 Azacytidine)": {
          "meaning": "",
          "comments": []
        },
        "OZM-077:Posterior Fossa Ependymoma Expansion Arm (5 Azacytidine)": {
          "meaning": "",
          "comments": []
        },
        "OZM-077:Recurrent Brain and Solid Tumour Expansion Arm (5 Azacytidine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC-029:Treatment (selumetinib) (Selumetinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC-039:Treatment (peginterferon alfa-2b) ()": {
          "meaning": "",
          "comments": []
        },
        "PBTC005:Stratum 1a: patients previously not treated with RT or only focal RT (Temozolomide, O-benzylguanine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC005:Stratum 1b: patients previously not treated with RT or only focal RT (Temozolomide, O-benzylguanine, G-CSF)": {
          "meaning": "",
          "comments": []
        },
        "PBTC005:Stratum 2a: patients with prior craniospinal irradiation or myeloblative therapy. (Temozolomide, O-benzylguanine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC005:Stratum 2b: patients with prior craniospinal irradiation or myeloblative therapy. (Temozolomide, O-benzylguanine, G-CSF)": {
          "meaning": "",
          "comments": []
        },
        "PBTC006:Stratum 1: newly diagnosed localized brainstem tumors (imatinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC006:Stratum 2A: recurrent intracranial malignant gliomas - not using EIACD (imatinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC006:Stratum 2B: recurrent intracranial malignant gliomas - using EIACD (imatinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC007:Stratum 1: Newly diagnosed intrinsic brain stem glioma or incompletely resected supratentorial malignant gliomas not receiving enzyme-inducing anti-convulsant drugs (ZD1839 (Iressa\u2122))": {
          "meaning": "",
          "comments": []
        },
        "PBTC007:Stratum 2: Incompletely resected supratentorial malignant gliomas receiving enzyme-inducing anticonvulsant drugs (ZD1839 (Iressa\u2122))": {
          "meaning": "",
          "comments": []
        },
        "PBTC016:Stratum 1: those who are not receiving steroids (Lapatinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC016:Stratum 2: those who are receiving steroids (Lapatinib)": {
          "meaning": "",
          "comments": []
        },
        "PBTC022:Stratum A: Recurrent, progressive or refractory high-grade gliomas (Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "PBTC022:Stratum B: Recurrent, progressive or refractory Intrinsic brain stem tumors (Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "PBTC022:Stratum C: Recurrent or progressive Medulloblastomas (Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "PBTC022:Stratum D: Recurrent or progressive Ependymomas (Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "PBTC022:Stratum E: Recurrent low grade gliomas (Bevacizumab, Irinotecan)": {
          "meaning": "",
          "comments": []
        },
        "PBTC043:Treatment (pomalidomide) (Pomalidomide)": {
          "meaning": "",
          "comments": []
        },
        "PBTC047:Stratum 1 (Panobinostat)": {
          "meaning": "",
          "comments": []
        },
        "PBTC047:Stratum 2 (Panobinostat)": {
          "meaning": "",
          "comments": []
        },
        "PBTC048:Newly Diagnosed (Concurrent Optune/focal radiation therapy followed by Optune-only therapy) ()": {
          "meaning": "",
          "comments": []
        },
        "PBTC048:Recurrent, Progressive or Refractory (Optune System) ()": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 1: BRAF V600E LGG or HGG (Dabrafenib, Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 2: BRAF fusion/duplication or NF1- associated LGG (Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 3: LGGs with V600E (Dabrafenib, Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 4: HGGs with V600E (Dabrafenib, Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 5 LGG with BRAF duplication or fusion with any partner (Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PBTC055:Stratum 6 LGG with neurofibromatosis type 1 (Trametinib, Hydroxychloroquine)": {
          "meaning": "",
          "comments": []
        },
        "PNOC005:Stratum A (Locally recurrent ATRT/medullo (delivery into tumor bed))": {
          "meaning": "",
          "comments": []
        },
        "PNOC005:Stratum B (disseminated ATRT/medullo (delivery via LP x 1 dose))": {
          "meaning": "",
          "comments": []
        },
        "PNOC005:Stratum C (disseminated medullo (delivery via LP x 2 doses))": {
          "meaning": "",
          "comments": []
        },
        "PNOC007:Stratum A- DIPG treated with vaccine (K27M peptide vaccine, combined with Tetanus Toxoid peptide, emulsified in montanide. Poly-ICLC will be given concurrently)": {
          "meaning": "",
          "comments": []
        },
        "PNOC007:Stratum B-non-DIPG DMG treated with vaccine; (K27M peptide vaccine, combined with Tetanus Toxoid peptide, emulsified in montanide. Poly-ICLC will be given concurrently)": {
          "meaning": "",
          "comments": []
        },
        "PNOC007:Stratum C- DIPG/DMG treated with vaccine and nivolumab (Nivolumab)": {
          "meaning": "",
          "comments": []
        },
        "PNOC008:Stratum A-Hemispheric HGG; (A combination of up to four FDA approved drugs based)": {
          "meaning": "",
          "comments": []
        },
        "PNOC008:Stratum B-non-DIPG DMG (A combination of up to four FDA approved drugs based)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 1 (ONC201, Panobinostat)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 2 (ONC201, Paxalisib)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 3 (ONC201, Panobinostat)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 4 (ONC201, Paxalisib)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 5 (ONC201, Panobinostat)": {
          "meaning": "",
          "comments": []
        },
        "PNOC022:Arm 6 (ONC201, Paxalisib)": {
          "meaning": "",
          "comments": []
        },
        "PNOC023:Arm A: ONC206 for participants with diffuse midline gliomas + prior therapy (ONC206)": {
          "meaning": "",
          "comments": []
        },
        "PNOC023:Arm B: ONC206 + radiation therapy for newly diagnosed participants (ONC206)": {
          "meaning": "",
          "comments": []
        },
        "PNOC023:Arm C: ONC206 + radiation therapy, DMGs with evidence of first progression but previously untreated (ONC206)": {
          "meaning": "",
          "comments": []
        },
        "PNOC023:Arm D: ONC206 Therapy, Primary malignant CNS tumors with progression (ONC206)": {
          "meaning": "",
          "comments": []
        },
        "PNOC026:Arm 1 - LGG (DAY101)": {
          "meaning": "",
          "comments": []
        },
        "PNOC026:Arm 2 - LGG extension (DAY101)": {
          "meaning": "",
          "comments": []
        },
        "PNOC026:Arm 3 - Solid tumor (DAY101)": {
          "meaning": "",
          "comments": []
        },
        "PNOC027:Individualized Treatment Recommendation ()": {
          "meaning": "",
          "comments": []
        },
        "POG-9905:Arm I (dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "POG-9905:Arm II (dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "POG-9905:Arm III (cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, pegaspargase, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "POG-9905:Arm IV (cyclophosphamide, cytarabine, daunorubicin hydrochloride, dexamethasone, leucovorin calcium, mercaptopurine, methotrexate, pegaspargase, thioguanine, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Chemotherapy, surgery, radiation therapy (cisplatin, cyclophosphamide, vincristine sulfate, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Regimen A: Cycle A (cyclophosphamide, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Regimen A: Cycle A' (vincristine, cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Regimen A: Cycle B (cisplatin, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Regimen B: Cycle X (cyclophosphamide, vincristine,)": {
          "meaning": "",
          "comments": []
        },
        "POG9233:Regimen B: Cycle Y (cisplatin, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "R115777-INT-11:1 (Gemcitabine with R115777)": {
          "meaning": "",
          "comments": []
        },
        "R115777-INT-11:2 (Gemcitabine with Placebo)": {
          "meaning": "",
          "comments": []
        },
        "REMATCH:Left ventricular assist device (Left ventricular assist device)": {
          "meaning": "",
          "comments": []
        },
        "REMATCH:Optimal medical therapy (Optimal medical therapy)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase I: Dose Level 1 (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase I: Dose Level 2a (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase I: Dose Level 2b (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase I: Dose Level 3 (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase II: Arm 1/BEV-FAILURE (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase II: Arm 1/BEV-NAIVE (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase II: Arm 2/BEV-FAILURE (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "RTOG-0929:Phase II: Arm 2/BEV-NAIVE (temozolomide, ABT-888)": {
          "meaning": "",
          "comments": []
        },
        "Re-MATCH:Group A ()": {
          "meaning": "",
          "comments": []
        },
        "Re-MATCH:Group B ()": {
          "meaning": "",
          "comments": []
        },
        "SARC006:Chemotherapy and local control by radiotherapy and surgery (doxorubicin hydrochloride, etoposide, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SARC006:Chemotherapy and local control by surgery (doxorubicin hydrochloride, etoposide, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 1: Ewings Sarcoma Primary Cohort (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 2: Ewings Sarcoma Secondary Cohort (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 3: Ewings Sarcoma Expanded Cohort (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 4: Osteosarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 5: Synovial Sarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 6: Rhabdomyosarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 7a: Alveolar Soft Part Sarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 7b: Desmoplastic Small Round Cell Tumors. (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 7c: Extraskeletal Myxoid Chondrosarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 7d: Clear Cell Sarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 7e: Myxoid Liposarcoma (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SARC011:Cohort 8: Diagnosis Not Specified (RG1507)": {
          "meaning": "",
          "comments": []
        },
        "SC-9006:Regimen A (Temozolomide, Etoposide, Sorafenib)": {
          "meaning": "",
          "comments": []
        },
        "SC-9006:Regimen B (Temozolomide, Etoposide, Everolimus)": {
          "meaning": "",
          "comments": []
        },
        "SC-9006:Regimen C (Temozolomide, Etoposide, Erlotinib)": {
          "meaning": "",
          "comments": []
        },
        "SC-9006:Regimen D (Temozolomide, Etoposide, Dasatinib)": {
          "meaning": "",
          "comments": []
        },
        "SEL-TH-1601:Stratum 1 - NF2 related vestibular schwannomas (Selumetinib)": {
          "meaning": "",
          "comments": []
        },
        "SEL-TH-1601:Stratum 2: other NF2 related tumors (meningiomas and ependymoma) (Selumetinib)": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Germinoma metastatic (none)": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Germinoma non-metastatic (Carboplatin, Etoposide, Ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:No Intervention: Teratoma ()": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Non-Germinoma metastatic high risk (Cisplatin, Etoposide, Ifosfamide (high dose))": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Non-Germinoma metastatic standard risk (Cisplatin, etoposide, Ifosfamide (standard))": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Non-germinoma non-metastatic high risk (Cisplatin, Etoposide, Ifosfamide (high dose))": {
          "meaning": "",
          "comments": []
        },
        "SIOP CNS GCT II:Non-germinoma non-metastatic standard risk (Cisplatin, etoposide, Ifosfamide (standard))": {
          "meaning": "",
          "comments": []
        },
        "SIOP-CNS-GCT-96:Stratum I: Option 1 (see notes) (carboplatin, cisplatin, etoposide phosphate, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-CNS-GCT-96:Stratum I: Option 2 (see notes) (carboplatin, cisplatin, etoposide phosphate, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-CNS-GCT-96:Stratum II: (secreting tumors and embryonal carcinoma) (cisplatin, etoposide phosphate, ifosfamide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 1 arm A (Vincristine, Etoposide, Cyclophosphamide, Cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 1 arm B": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 2 arm A (Vincristine, Etoposide, Cyclophosphamide, Methotrexate)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 2 arm B (Vincristine, Etoposide, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 3 arm A (Vincristine, Carboplatin, Methotrexate, Cyclophosphamide, Cisplatin, Valproate)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-EP-II:Stratum 3 arm B (Vincristine, Carboplatin, Methotrexate Cyclophosphamide, Cisplatin)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-LGG-2004:Control group": {
          "meaning": "",
          "comments": []
        },
        "SIOP-LGG-2004:intensified induction chemotherapy group (vincristine, carboplatin, etoposide)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-LGG-2004:radiation therapy group": {
          "meaning": "",
          "comments": []
        },
        "SIOP-LGG-2004:standard chemotherapy group (vincristine, carboplatin)": {
          "meaning": "",
          "comments": []
        },
        "SIOP-PNET-4:Hyperfractionated radiotherapy": {
          "meaning": "",
          "comments": []
        },
        "SIOP-PNET-4:Standard Fractionation Regimen": {
          "meaning": "",
          "comments": []
        },
        "SJATART:Intervenion B2 (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "SJATART:Intervention B1 (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "SJATART:Stratum A (alisertib)": {
          "meaning": "",
          "comments": []
        },
        "SJATART:Stratum B (alisertib, methotrexate, cisplatin, carboplatin, cyclophosphamide, etoposide, topotecan, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "SJATART:Stratum C (alisertib, cisplatin, cyclophosphamide, vincristine)": {
          "meaning": "",
          "comments": []
        },
        "SJDAWN:A: ribociclib + gemcitabine (ribociclib, gemcitabine)": {
          "meaning": "",
          "comments": []
        },
        "SJDAWN:B: ribociclib + trametinib (ribociclib, trametinib)": {
          "meaning": "",
          "comments": []
        },
        "SJDAWN:C: ribociclib + sonidegib (ribociclib, sonidegib)": {
          "meaning": "",
          "comments": []
        },
        "SJMB-96:Average-risk (filgrastim, amifostine trihydrate, cisplatin, cyclophosphamide, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "SJMB-96:High-risk (filgrastim, amifostine trihydrate, cisplatin, cyclophosphamide, vincristine sulfate)": {
          "meaning": "",
          "comments": []
        },
        "SJMB03:Stratum 1 (high-risk group) (Vincristine, Cisplatin, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "SJMB03:Stratum 2 (average-risk group) (Vincristine, Cisplatin, Cyclophosphamide)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum N1: Standard Risk (Cyclophosphamide, Cisplatin, Vincristine,)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum N2: Intermediate Risk (Cyclophosphamide, Cisplatin, Vincristine, Pemetrexed, Gemcitabine)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum N3: High Risk (Cyclophosphamide, Cisplatin, Vincristine, Pemetrexed, Gemcitabine)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum S1: Standard Risk (Cyclophosphamide, Cisplatin, Vincristine, Vismodegib)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum S2: High Risk (Cyclophosphamide, Cisplatin, Vincristine, Vismodegib)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum W1: Low Risk (Cyclophosphamide, Cisplatin, Vincristine,)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum W2: Atypical (Cyclophosphamide, Cisplatin, Vincristine,)": {
          "meaning": "",
          "comments": []
        },
        "SJMB12:Stratum W3: High Risk (Cyclophosphamide, Cisplatin, Vincristine,)": {
          "meaning": "",
          "comments": []
        },
        "SJYC07:High-Risk Patients (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Velban(R) (vinblastine), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib), Vepesid(R), VP-16 (etoposide))": {
          "meaning": "",
          "comments": []
        },
        "SJYC07:Intermediate-Risk Therapy (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Velban(R) (vinblastine), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib), Vepesid(R), VP-16 (etoposide))": {
          "meaning": "",
          "comments": []
        },
        "SJYC07:Low-Risk Patients (MTX (methotrexate), Oncovin(R) (vincristine), Platinol-AQ(R) (cisplatin), Cytoxan(R) (cyclophosphamide), Paraplatin(R) (carboplatin), Vepesid(R), VP-16 (etoposide), Hycamptin(R) (topotecan), Tarceva(TM) (erlotinib))": {
          "meaning": "",
          "comments": []
        },
        "STRIvE-02:SCRI-CARB7H3(s) ()": {
          "meaning": "",
          "comments": []
        },
        "STRIvE-02:SCRI-CARB7H3(s)x19 ()": {
          "meaning": "",
          "comments": []
        },
        "STRIvE-02:SCRI-CARB7H3(s)x19 plus pembrolizumab ()": {
          "meaning": "",
          "comments": []
        },
        "Stupp Protocol:Radiotherapy with concomitant": {
          "meaning": "",
          "comments": []
        },
        "Stupp Protocol:adjuvant chemotherapy with temozolomide (temozolomide)": {
          "meaning": "",
          "comments": []
        },
        "TB-403:TB-403 100mg/kg (TB-403)": {
          "meaning": "",
          "comments": []
        },
        "TB-403:TB-403 175mg/kg (TB-403)": {
          "meaning": "",
          "comments": []
        },
        "TB-403:TB-403 20mg/kg (TB-403)": {
          "meaning": "",
          "comments": []
        },
        "TB-403:TB-403 50mg/kg (TB-403)": {
          "meaning": "",
          "comments": []
        },
        "TOTEM:Intensive follow up": {
          "meaning": "",
          "comments": []
        },
        "TOTEM:Minimalist follow up": {
          "meaning": "",
          "comments": []
        },
        "rHSC-DIPGVax:\"Lead In\": rHSC-DIPGVax Monotherapy": {
          "meaning": "",
          "comments": []
        },
        "rHSC-DIPGVax:Part A: rHSC-DIPGVax in Combination with BALSTILIMAB (Anti-PD1) (Balstilimab)": {
          "meaning": "",
          "comments": []
        },
        "rHSC-DIPGVax:Part B: Dose Escalation of ZALIFRELIMAB (Anti-CTLA4) (Balstilimab, Zalifrelimab)": {
          "meaning": "",
          "comments": []
        },
        "rHSC-DIPGVax:Part C: Dose Expansion (Balstilimab, Zalifrelimab)": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AllelicStateEnum": {
      "permissible_values": {
        "Heterozygous": {
          "meaning": "ncit:C45825",
          "comments": []
        },
        "Homozygous": {
          "meaning": "ncit:C45826",
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
        "Post-Mortem": {
          "meaning": "ncit:C94193",
          "comments": []
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
    "ResponseCategoryEnum": {
      "permissible_values": {
        "Non-Target Lesions": {
          "meaning": "ncit:C94535",
          "comments": []
        },
        "Overall Response": {
          "meaning": "ncit:C96613",
          "comments": []
        },
        "Target Lesions": {
          "meaning": "ncit:C94534",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "INSPiRE": {
          "meaning": "ncit:C192765",
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
        }
      }
    },
    "DiagnosisCategoryEnum": {
      "permissible_values": {
        "Atypical Teratoid/Rhabdoid Tumor": {
          "meaning": "ncit:C6906",
          "comments": []
        },
        "CNS Germ Cell Tumors": {
          "meaning": "ncit:C5461",
          "comments": []
        },
        "Choroid Plexus Tumors": {
          "meaning": "ncit:C3473",
          "comments": []
        },
        "Craniopharyngioma": {
          "meaning": "ncit:C2964",
          "comments": []
        },
        "Ependymoma": {
          "meaning": "icdo:9391/3",
          "comments": [
            "(cns) ConsortiumNote: Includes ependymal tumors"
          ]
        },
        "Glioneuronal and Neuronal Tumors": {
          "meaning": "ncit:C4747",
          "comments": []
        },
        "High-Grade Glioma": {
          "meaning": "ncit:C162993",
          "comments": [
            "(cns) ConsortiumNote: Includes adult-type diffuse gliomas, pediatric type diffuse high-grade gliomas, some circumscribed astrocytic gliomas"
          ]
        },
        "Low-Grade Glioma": {
          "meaning": "ncit:C132067",
          "comments": [
            "(cns) ConsortiumNote: Includes pediatric type diffuse low-grade gliomas, some circumscribed astrocytic gliomas."
          ]
        },
        "Medulloblastoma": {
          "meaning": "icdo:9470/3",
          "comments": []
        },
        "Other CNS Embryonal Tumors": {
          "meaning": "ncit:C6990",
          "comments": [
            "(cns) ConsortiumNote: Includes pineoblastoma"
          ]
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        }
      }
    },
    "ExtentEnum": {
      "permissible_values": {
        "Biopsy Only": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Gross Total": {
          "meaning": "ncit:C131672",
          "comments": []
        },
        "Gross Total or Near Total Resection": {
          "meaning": "",
          "comments": []
        },
        "Near Total Resection": {
          "meaning": "",
          "comments": []
        },
        "Partial Resection": {
          "meaning": "ncit:C131680",
          "comments": []
        },
        "Partial or Subtotal Resection": {
          "meaning": "",
          "comments": []
        },
        "Subtotal Resection": {
          "meaning": "ncit:C131680",
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