---
layout: default
title: Lynch Syndrome
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*LS View*

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
- **Lynch Syndrome**
- [Liver Tumors](lt)
- [Neuroblastoma](nbl)
- [Nasopharyngeal Carcinoma](npc)
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The LS view of the PCDC data model represents consensus data modeling by an international group of Lynch Syndrome experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Lynch Syndrome Integrative Epidemiology and Genetics Consortium (LINEAGE). It is based on the collective requirements of its contributors.


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

## FamilyMedicalHistory

| Slot | Range | Description |
|---|---|---|
| `family_medical_history_condition` | `string` |  |
| `relation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-relationenum')">RelationEnum</button> |  |
| `relation_lineage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-relationlineageenum')">RelationLineageEnum</button> |  |
| `lkss_of_relative` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssofrelativeenum')">LkssOfRelativeEnum</button> |  |
| `age_at_lkss_of_relative` | `integer` |  |
| `proband_generation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-probandgenerationenum')">ProbandGenerationEnum</button> |  |
| `age_at_condition` | `integer` |  |
| `sex_at_birth` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexatbirthenum')">SexAtBirthEnum</button> |  |
| `age_at_time_of_pedigree_creation` | `integer` |  |
| `year_at_pedigree_creation` | `integer` |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `age_at_condition` | `integer` |  |
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |

## OffProtocolTherapyOrStudy

| Slot | Range | Description |
|---|---|---|
| `age_off` | `integer` |  |
| `off_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-offtypeenum')">OffTypeEnum</button> |  |
| `reason_off` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonoffenum')">ReasonOffEnum</button> |  |

## SocialAndBehavioralDeterminantsOfHealth

| Slot | Range | Description |
|---|---|---|
| `age_at_status` | `integer` |  |
| `gender_identity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genderidentityenum')">GenderIdentityEnum</button> |  |
| `exposure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposureenum')">ExposureEnum</button> |  |
| `exposure_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposurestatusenum')">ExposureStatusEnum</button> |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `enrolled_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |

## Subject

| Slot | Range | Description |
|---|---|---|
| `consortium` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-consortiumenum')">ConsortiumEnum</button> |  |
| `disease_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasegroupenum')">DiseaseGroupEnum</button> |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |
| `race` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button> |  |
| `race_other` | `string` |  |
| `race_specified` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-racespecifiedenum')">RaceSpecifiedEnum</button> |  |
| `ethnicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button> |  |
| `ethnicity_other` | `string` |  |
| `ethnicity_specified` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityspecifiedenum')">EthnicitySpecifiedEnum</button> |  |
| `ashkenazi_jewish_ancestry` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `proband_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

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
| `year_at_diagnosis` | `integer` |  |
| `age_at_diag_resolved` | `integer` |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histology_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologygradeenum')">HistologyGradeEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_characteristic` | `integer` |  |
| `performance_score` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-performancescoreenum')">PerformanceScoreEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `tumor_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `sedation_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sedationtypeenum')">SedationTypeEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement1_axis` | `LesionMeasurementAxisEnum` |  |
| `measurement2` | `decimal` |  |
| `measurement2_axis` | `LesionMeasurementAxisEnum` |  |
| `measurement3` | `decimal` |  |
| `measurement3_axis` | `LesionMeasurementAxisEnum` |  |
| `measurement_unit` | `LesionMeasurementUnitEnum` |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |
| `finding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-findingenum')">FindingEnum</button> |  |
| `colon_polyp_max_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-colonpolypmaxsizeenum')">ColonPolypMaxSizeEnum</button> |  |
| `colon_polyp_min_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-colonpolypminsizeenum')">ColonPolypMinSizeEnum</button> |  |
| `barretts_esophagus` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-barrettsesophagusenum')">BarrettsEsophagusEnum</button> |  |
| `bowel_preparation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-bowelpreparationenum')">BowelPreparationEnum</button> |  |
| `bbps_score` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-bbpsscoreenum')">BbpsScoreEnum</button> |  |
| `bbps_score_total` | `decimal` |  |
| `tumor_budding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorbuddingenum')">TumorBuddingEnum</button> |  |
| `number_nodes_numeric` | `decimal` |  |
| `colon_polyps_total` | `decimal` |  |
| `gastric_polyps_total` | `decimal` |  |
| `small_bowel_polyps_total` | `decimal` |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `tnm_tumor_t` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmtumortenum')">TnmTumorTEnum</button> |  |
| `tnm_node_n` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmnodenenum')">TnmNodeNEnum</button> |  |
| `tnm_metastasis_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmmetastasismenum')">TnmMetastasisMEnum</button> |  |
| `tnm_overall` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmoverallenum')">TnmOverallEnum</button> |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## LocoregionalTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_locoregional_therapy` | `integer` |  |
| `administration_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-administrationstatusenum')">AdministrationStatusEnum</button> |  |
| `locoregional_therapy_technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-locoregionaltherapytechniqueenum')">LocoregionalTherapyTechniqueEnum</button> |  |

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `administration_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-administrationstatusenum')">AdministrationStatusEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `regimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-regimenenum')">RegimenEnum</button> |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `procedure_extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureextentenum')">ProcedureExtentEnum</button> |  |
| `remaining_colon` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-remainingcolonenum')">RemainingColonEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |

<div class="domain-heading">Testing</div>

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `genomic_source_class` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genomicsourceclassenum')">GenomicSourceClassEnum</button> |  |
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `alteration_region` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationregionenum')">AlterationRegionEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `chromosomal_translocation_partner` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomaltranslocationpartnerenum')">ChromosomalTranslocationPartnerEnum</button> |  |
| `cytoband` | `string` |  |
| `iscn` | `string` |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `exon_number` | `decimal` |  |
| `hgvs_genomic_transcript` | `string` |  |
| `hgvs_genomic` | `string` |  |
| `hgvs_coding_transcript` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein_transcript` | `string` |  |
| `hgvs_protein` | `string` |  |
| `reference_genome` | `string` |  |
| `reference_genome_accession` | `string` |  |
| `reported_significance` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reportedsignificanceenum')">ReportedSignificanceEnum</button> |  |
| `reported_significance_other` | `string` |  |
| `external_ref_id_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-externalrefidsystemenum')">ExternalRefIdSystemEnum</button> |  |
| `external_ref_id` | `string` |  |
| `copy_number` | `decimal` |  |
| `maf_numeric` | `decimal` |  |
| `vaf_numeric` | `decimal` |  |
| `dna_index_numeric` | `decimal` |  |
| `allelic_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button> |  |
| `allelic_ratio` | `decimal` |  |

## Immunohistochemistry

| Slot | Range | Description |
|---|---|---|
| `age_at_ihc` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `markers` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-markersenum')">MarkersEnum</button> |  |
| `result_text` | `string` |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `result_text` | `string` |  |
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Compound Heterozygous</code></td><td><code>ncit:C198518</code></td><td></td></tr>
<tr><td><code>Hemizygous</code></td><td><code>ncit:C64346</code></td><td></td></tr>
<tr><td><code>Heterozygous</code></td><td><code>ncit:C45825</code></td><td></td></tr>
<tr><td><code>Homozygous</code></td><td><code>ncit:C45826</code></td><td></td></tr>
<tr><td><code>Mosaic</code></td><td><code>ncit:C88144</code></td><td></td></tr>
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
<tr><td><code>Mutated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wild Type</code></td><td><code>ncit:C62195</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Intronic</code></td><td><code>ncit:C45387</code></td><td></td></tr>
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
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-barrettsesophagusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-barrettsesophagusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-barrettsesophagusenum')">×</button>
<h3><code>BarrettsEsophagusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>High Grade Dysplasia</code></td><td><code>ncit:C156083</code></td><td></td></tr>
<tr><td><code>Indeterminate for Dysplasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low Grade Dysplasia</code></td><td><code>ncit:C156084</code></td><td></td></tr>
<tr><td><code>No Dysplasia</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-bbpsscoreenum" class="enum-modal" onclick="closeEnumModal('enum-modal-bbpsscoreenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-bbpsscoreenum')">×</button>
<h3><code>BbpsScoreEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Segment Score 0</code></td><td><code>ncit:C138207</code></td><td></td></tr>
<tr><td><code>Segment Score 1</code></td><td><code>ncit:C138208</code></td><td></td></tr>
<tr><td><code>Segment Score 2</code></td><td><code>ncit:C138209</code></td><td></td></tr>
<tr><td><code>Segment Score 3</code></td><td><code>ncit:C138210</code></td><td></td></tr>
<tr><td><code>Surgically Absent</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-bowelpreparationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-bowelpreparationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-bowelpreparationenum')">×</button>
<h3><code>BowelPreparationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Adequate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Excellent</code></td><td><code>ncit:C82488</code></td><td></td></tr>
<tr><td><code>Fair</code></td><td><code>ncit:C82489</code></td><td></td></tr>
<tr><td><code>Good</code></td><td><code>ncit:C64975</code></td><td></td></tr>
<tr><td><code>Inadequate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Documented</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Poor</code></td><td><code>ncit:C77959</code></td><td></td></tr>
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

<div id="enum-modal-chromosomaltranslocationpartnerenum" class="enum-modal" onclick="closeEnumModal('enum-modal-chromosomaltranslocationpartnerenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-chromosomaltranslocationpartnerenum')">×</button>
<h3><code>ChromosomalTranslocationPartnerEnum</code></h3>
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

<div id="enum-modal-colonpolypmaxsizeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-colonpolypmaxsizeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-colonpolypmaxsizeenum')">×</button>
<h3><code>ColonPolypMaxSizeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1-5 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>20+ mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>6-9 mm</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-colonpolypminsizeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-colonpolypminsizeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-colonpolypminsizeenum')">×</button>
<h3><code>ColonPolypMinSizeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1-5 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>10-19 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>20+ mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>6-9 mm</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>LINEAGE</code></td><td><code>ncit:C192767</code></td><td></td></tr>
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
<tr><td><code>Curative Intent, No Surgery Planned</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
<tr><td><code>Palliative Treatment</code></td><td><code>ncit:C15292</code></td><td></td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code>ncit:C15313</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
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
<tr><td><code>Attachment Device (Cap, Endocuff, etc.)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CT</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Computer Aided Diagnosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dye Chromoendoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flexible Sigmoidoscopy</code></td><td><code>ncit:C51588</code></td><td></td></tr>
<tr><td><code>High Definition Equipment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy (colonoscopy)</code></td><td><code>ncit:C16450</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>Rectal Retroflexion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Right Colon Retroflexion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Serum Antigen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stool Antigen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>Upper Endoscopy (Colonscope)</code></td><td><code>ncit:C16604</code></td><td></td></tr>
<tr><td><code>Upper Endoscopy (Gastroscope)</code></td><td><code>ncit:C16604</code></td><td></td></tr>
<tr><td><code>Urea Breath Test</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Video Capsule Endoscopy</code></td><td><code>ncit:C16546</code></td><td></td></tr>
<tr><td><code>Virtual Chromoendoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Attachment Device (Cap, Endocuff, etc.)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Computer Aided Diagnosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Dye Chromoendoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Flexible Sigmoidoscopy</code></td><td><code>ncit:C51588</code></td><td></td></tr>
<tr><td><code>Upper Endoscopy, High Definition Equipment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, High Defnition Equipment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Rectal Retroflexion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Right Colon Retroflexion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Endoscopy, Virtual Chromoendoscopy</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Acute lymphoblastic leukemia</code></td><td><code>icdo:9828/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia</code></td><td><code>icdo:9861/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma</code></td><td><code>icdo:8140/3</code></td><td></td></tr>
<tr><td><code>Adenosquamous carcinoma</code></td><td><code>icdo:8560/3</code></td><td></td></tr>
<tr><td><code>Adrenal cortical carcinoma</code></td><td><code>icdo:8370/3</code></td><td></td></tr>
<tr><td><code>Astrocytoma</code></td><td><code>icdo:9400/3</code></td><td></td></tr>
<tr><td><code>Basal cell carcinoma</code></td><td><code>icdo:8090/3</code></td><td></td></tr>
<tr><td><code>Borderline tumor</code></td><td><code></code></td><td>(ls) ConsortiumNote: Use for Ovarian/Fallopian Tube/Primary Peritoneal Histology</td></tr>
<tr><td><code>Carcinoma, NOS</code></td><td><code>icdo:8010/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma</code></td><td><code>icdo:8980/3</code></td><td></td></tr>
<tr><td><code>Cholangiocarcinoma</code></td><td><code>icdo:8160/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Chordoma</code></td><td><code>ncit:C2947</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Chronic lymphocytic leukemia</code></td><td><code>icdo:9823/3</code></td><td></td></tr>
<tr><td><code>Chronic myeloid leukemia</code></td><td><code>icdo:9863/3</code></td><td></td></tr>
<tr><td><code>Clear cell carcinoma</code></td><td><code>icdo:9863/3</code></td><td></td></tr>
<tr><td><code>Cutaneous T-cell lymphoma</code></td><td><code>icdo:9709/3</code></td><td></td></tr>
<tr><td><code>Ductal carcinoma in situ</code></td><td><code>icdo:9709/3</code></td><td></td></tr>
<tr><td><code>Endometrioid adenocarcinoma</code></td><td><code>icdo:8380/3</code></td><td></td></tr>
<tr><td><code>Ewing Sarcoma</code></td><td><code>icdo:9260/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Gastrointestinal stromal tumor</code></td><td><code>icdo:8936/3</code></td><td></td></tr>
<tr><td><code>Germ cell tumor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glioma, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hairy cell leukemia</code></td><td><code>icdo:9940/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma</code></td><td><code>icdo:8170/3</code></td><td></td></tr>
<tr><td><code>High-grade serous carcinoma</code></td><td><code>icdo:8461/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma</code></td><td><code>icdo:9650/3</code></td><td></td></tr>
<tr><td><code>Hyperplastic polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infiltrating ductular carcinoma</code></td><td><code>icdo:8521/3</code></td><td></td></tr>
<tr><td><code>Invasive ductal carcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Invasive lobular carcinoma</code></td><td><code>icdo:8520/3</code></td><td></td></tr>
<tr><td><code>Kaposi Sarcoma</code></td><td><code>icdo:9140/3</code></td><td></td></tr>
<tr><td><code>Keratoacanthoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low-grade dysplasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphoma, NOS</code></td><td><code>icdo:9590/3</code></td><td></td></tr>
<tr><td><code>MDS/MPN, NOS</code></td><td><code>icdo:9989/3</code></td><td></td></tr>
<tr><td><code>Medullary carcinoma</code></td><td><code>icdo:8510/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma</code></td><td><code>icdo:9473/3</code></td><td></td></tr>
<tr><td><code>Melanoma</code></td><td><code>icdo:8720/3</code></td><td></td></tr>
<tr><td><code>Mesothelioma</code></td><td><code>icdo:9050/3</code></td><td></td></tr>
<tr><td><code>Metaplastic carcinoma</code></td><td><code>icdo:8575/3</code></td><td></td></tr>
<tr><td><code>Mucinous adenocarcinoma</code></td><td><code>icdo:8480/3</code></td><td></td></tr>
<tr><td><code>Mullerian carcinoma</code></td><td><code>icdo:8950/3</code></td><td></td></tr>
<tr><td><code>Multiple myeloma</code></td><td><code>icdo:9732/3</code></td><td></td></tr>
<tr><td><code>Neuroblastoma</code></td><td><code>icdo:9500/3</code></td><td></td></tr>
<tr><td><code>Neuroendocrine tumor</code></td><td><code>icdo:8249/3</code></td><td></td></tr>
<tr><td><code>Non-Hodgkin lymphoma</code></td><td><code>icdo:9591/3</code></td><td></td></tr>
<tr><td><code>Non-small cell carcinoma</code></td><td><code>icdo:8046/3</code></td><td></td></tr>
<tr><td><code>Oligodendroglioma, NOS</code></td><td><code>icdo:9450/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma</code></td><td><code>icdo:9180/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma</code></td><td><code>icdo:8050/3</code></td><td></td></tr>
<tr><td><code>Paraganglioma, malignant</code></td><td><code>icdo:8680/3</code></td><td></td></tr>
<tr><td><code>Pituitary adenoma</code></td><td><code>icdo:8272/0</code></td><td></td></tr>
<tr><td><code>Renal cell carcinoma</code></td><td><code>icdo:8312/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma</code></td><td><code>icdo:9510/3</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>ncit:C3359</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Sarcoma, NOS</code></td><td><code>icdo:8800/3</code></td><td></td></tr>
<tr><td><code>Serous carcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sessile serrated lesion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Signet ring cell carcinoma</code></td><td><code>icdo:8490/3</code></td><td></td></tr>
<tr><td><code>Small cell carcinoma</code></td><td><code>icdo:8041/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, NOS</code></td><td><code>icdo:8070/3</code></td><td></td></tr>
<tr><td><code>Traditional serrated adenoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tubular adenoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tubulovillous adenoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urothelial carcinoma</code></td><td><code>icdo:8120/3</code></td><td></td></tr>
<tr><td><code>Villous adenoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Condyloma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hamartoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inflammatory Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inflammation (neutrophils, lymphocytes, eosinophils)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Juvenile Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lipoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphoid Aggregate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Normal Colonic Mucosa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oligodendroglial-astrocytic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scar</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>LS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Predisposed Disease Surveillance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Refractory/Progression</code></td><td><code>ncit:C174991</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
<tr><td><code>Relapse/Refractory</code></td><td><code>ncit:C203382</code></td><td></td></tr>
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
<tr><td><code>Adrenal Cortex</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Adrenal medulla</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ampulla</code></td><td><code>ncit:C93230</code></td><td></td></tr>
<tr><td><code>Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anus</code></td><td><code>ncit:C43362</code></td><td></td></tr>
<tr><td><code>Appendiceal Orifice</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Appendix</code></td><td><code>ncit:C12380</code></td><td></td></tr>
<tr><td><code>Ascending</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bile duct</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Cecum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cerebellum</code></td><td><code>ncit:C12445</code></td><td></td></tr>
<tr><td><code>Cervix Uteri</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colon</code></td><td><code>ncit:C12382</code></td><td></td></tr>
<tr><td><code>Descending</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Distal Cholangiocarcinoma</code></td><td><code>ncit:C7976</code></td><td></td></tr>
<tr><td><code>Distal Esophagus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Duodenal Bulb (D1)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Duodenum</code></td><td><code>ncit:C12263</code></td><td></td></tr>
<tr><td><code>Endometrium</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Esophagus, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Extrahepatic</code></td><td><code>ncit:C28358</code></td><td></td></tr>
<tr><td><code>Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fallopian Tube</code></td><td><code>ncit:C12403</code></td><td></td></tr>
<tr><td><code>Fourth Portion of Duodenum (D4)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GE Junction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder</code></td><td><code>ncit:C12377</code></td><td></td></tr>
<tr><td><code>Gastric Antrum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric Body</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric Cardia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric Fundus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic flexure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hilar Cholangiocarcinoma</code></td><td><code>ncit:C36077</code></td><td></td></tr>
<tr><td><code>Ileocecal Valve</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ileum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrahepatic Cholangiocarcinoma</code></td><td><code>ncit:C35417</code></td><td></td></tr>
<tr><td><code>Jejunum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Ligament of Treitz</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mid Esophagus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Ovarian</code></td><td><code>ncit:C28047</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Pancreas</code></td><td><code>ncit:C12393</code></td><td></td></tr>
<tr><td><code>Pancreas Body</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pancreas Head</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pancreas Tail</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paraganglia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parathyroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Penis</code></td><td><code>ncit:C12409</code></td><td></td></tr>
<tr><td><code>Pituitary gland</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Pouch</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Primary Peritoneal</code></td><td><code>ncit:C40022</code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Proximal Esophagus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rectosigmoid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Retina</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Second Portion of Duodenum (D2)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sigmoid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
<tr><td><code>Splenic flexure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code>ncit:C12391</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Third Portion of Duodenum (D3)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thyroid</code></td><td><code>ncit:C12400</code></td><td></td></tr>
<tr><td><code>Transverse</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transverse Colon</code></td><td><code>ncit:C12385</code></td><td></td></tr>
<tr><td><code>Unknown Primary</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ureter</code></td><td><code>ncit:C12416</code></td><td></td></tr>
<tr><td><code>Urethra</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary bladder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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

<div id="enum-modal-ethnicityspecifiedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ethnicityspecifiedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ethnicityspecifiedenum')">×</button>
<h3><code>EthnicitySpecifiedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Not Specified</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spanish/Spaniard</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Argentinean/Argentine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bolivian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Central American Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chilean</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colombian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Costa Rican</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cuban</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ecuadorian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Guatemalan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Honduran</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mexican</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mexican American Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nicaraguan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Panamanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paraguayan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peruvian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Puerto Rican</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Salvadoran</code></td><td><code></code></td><td></td></tr>
<tr><td><code>South American Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uruguayan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Venezuelan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-exposureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-exposureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-exposureenum')">×</button>
<h3><code>ExposureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alcohol</code></td><td><code>ncit:C168296</code></td><td></td></tr>
<tr><td><code>Drug Use</code></td><td><code></code></td><td></td></tr>
<tr><td><code>E-Cigarettes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Second-Hand Smoke</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tobacco</code></td><td><code>ncit:C18059</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-exposurestatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-exposurestatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-exposurestatusenum')">×</button>
<h3><code>ExposureStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Current</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ever</code></td><td><code>ncit:C159710</code></td><td></td></tr>
<tr><td><code>Never</code></td><td><code>ncit:C70543</code></td><td></td></tr>
<tr><td><code>Past</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>ClinVar</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-findingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-findingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-findingenum')">×</button>
<h3><code>FindingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Blunting Atrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Diverticulosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Duodenitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Excavated (III) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Extranodal Tumor Deposit</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flat (IIb) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric Atrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric Ulcer(s)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastritis / Inflammation/ Erythema/ Edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastropathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Jejunitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphatic Vascular Invasion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Macroscopic Tumor Perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pedunculated (Ip) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Perineural Invasion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Semi-Pedunculated (Isp) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sessile (Is) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Slightly Depressed (IIc) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Slightly Elevated (IIa) Polyp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small Bowel Ulcer(s)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Visual Ampulla</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Visualized Mucosa</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-genderidentityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-genderidentityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-genderidentityenum')">×</button>
<h3><code>GenderIdentityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Identifies As Female Gender</code></td><td><code>SCTID:446141000124107</code></td><td></td></tr>
<tr><td><code>Identifies As Male Gender</code></td><td><code>SCTID:446151000124109</code></td><td></td></tr>
<tr><td><code>Transgender, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Unknown Genomic Origin</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Gleason &gt;&gt; Grade Group 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gleason &gt;&gt; Grade Group 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gleason &gt;&gt; Grade Group 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gleason &gt;&gt; Grade Group 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gleason &gt;&gt; Grade Group 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 1</code></td><td><code>ncit:C41338</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 2</code></td><td><code>ncit:C41339</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Grade 3</code></td><td><code>ncit:C41340</code></td><td></td></tr>
<tr><td><code>WHO Glioma &gt;&gt; Grade I</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO Glioma &gt;&gt; Grade II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO Glioma &gt;&gt; Grade III</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WHO Glioma &gt;&gt; Grade IV</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>ALC</code></td><td><code>ncit:C113237</code></td><td></td></tr>
<tr><td><code>ALP</code></td><td><code>ncit:C64432</code></td><td></td></tr>
<tr><td><code>ALT</code></td><td><code>ncit:C64433</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>AST</code></td><td><code>ncit:C64467</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Albumin</code></td><td><code>ncit:C64431</code></td><td></td></tr>
<tr><td><code>Calcium</code></td><td><code>ncit:C64488</code></td><td></td></tr>
<tr><td><code>Chloride</code></td><td><code>ncit:C64495</code></td><td></td></tr>
<tr><td><code>Creatinine</code></td><td><code>ncit:C64547</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>Creatinine Clearance</code></td><td><code>ncit:C25747</code></td><td></td></tr>
<tr><td><code>Direct Bilirubin</code></td><td><code>ncit:C64481</code></td><td></td></tr>
<tr><td><code>Estrogen Receptor Test</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glucose</code></td><td><code>ncit:C105585</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>HCT</code></td><td><code>ncit:C64796</code></td><td></td></tr>
<tr><td><code>Hemoglobin</code></td><td><code>ncit:C64848</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Hemoglobin A1c Measurement</code></td><td><code>ncit:C64849</code></td><td></td></tr>
<tr><td><code>Microsatellite Instability Test</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Potassium</code></td><td><code>ncit:C64853</code></td><td></td></tr>
<tr><td><code>Progesterone Receptor Test</code></td><td><code>ncit:C74791</code></td><td></td></tr>
<tr><td><code>Protein Total</code></td><td><code>ncit:C64858</code></td><td></td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C51946</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Sodium</code></td><td><code>ncit:C64809</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>Total Bilirubin</code></td><td><code>ncit:C38037</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Urine Cytology</code></td><td><code>ncit:C94473</code></td><td></td></tr>
<tr><td><code>WBC</code></td><td><code>ncit:C51948</code></td><td></td></tr>
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
<tr><td><code>IU/mL</code></td><td><code>ncit:C67378</code></td><td></td></tr>
<tr><td><code>U/L</code></td><td><code>ncit:C67456</code></td><td></td></tr>
<tr><td><code>count/mm3</code></td><td><code>ncit:C173275</code></td><td></td></tr>
<tr><td><code>cp/mL</code></td><td><code></code></td><td></td></tr>
<tr><td><code>g/dL</code></td><td><code>ncit:C64783</code></td><td></td></tr>
<tr><td><code>mg/L</code></td><td><code>ncit:C64572</code></td><td></td></tr>
<tr><td><code>mg/dL</code></td><td><code>ncit:C67015</code></td><td></td></tr>
<tr><td><code>mm/h</code></td><td><code>ncit:C67419</code></td><td></td></tr>
<tr><td><code>mmHg</code></td><td><code>ncit:C49670</code></td><td></td></tr>
<tr><td><code>mmol/L</code></td><td><code>ncit:C64387</code></td><td></td></tr>
<tr><td><code>ng/mL</code></td><td><code>ncit:C67306</code></td><td></td></tr>
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
<tr><td><code>Saliva</code></td><td><code>ncit:C174119</code></td><td></td></tr>
<tr><td><code>Stool Sample</code></td><td><code>ncit:C189125</code></td><td></td></tr>
<tr><td><code>Tumor Sample</code></td><td><code>ncit:C18009</code></td><td></td></tr>
<tr><td><code>Urine</code></td><td><code>ncit:C13283</code></td><td></td></tr>
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
<tr><td><code>Unilateral</code></td><td><code>ncit:C28012</code></td><td></td></tr>
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

<div id="enum-modal-lkssofrelativeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lkssofrelativeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lkssofrelativeenum')">×</button>
<h3><code>LkssOfRelativeEnum</code></h3>
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

<div id="enum-modal-locoregionaltherapytechniqueenum" class="enum-modal" onclick="closeEnumModal('enum-modal-locoregionaltherapytechniqueenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-locoregionaltherapytechniqueenum')">×</button>
<h3><code>LocoregionalTherapyTechniqueEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chemoembolization (TACE)</code></td><td><code>ncit:C101513</code></td><td></td></tr>
<tr><td><code>Radioembolization</code></td><td><code>ncit:C116649</code></td><td></td></tr>
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
<tr><td><code>Her2 FISH</code></td><td><code>ncit:C38906</code></td><td></td></tr>
<tr><td><code>Her2 Protein</code></td><td><code>ncit:C38896</code></td><td></td></tr>
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
<tr><td><code>Acoustic Neuroma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia</code></td><td><code>ncit:C3167</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia</code></td><td><code>ncit:C3171</code></td><td></td></tr>
<tr><td><code>Angiosarcoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Appendiceal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Astrocytoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Basal Cell Carcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Cancer</code></td><td><code>ncit:C131533</code></td><td></td></tr>
<tr><td><code>Brain Cancer</code></td><td><code>ncit:C131533</code></td><td></td></tr>
<tr><td><code>Ewing Sarcoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraocular Melanoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney (Renal Cell)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Melanoma</code></td><td><code>ncit:C3224</code></td><td></td></tr>
<tr><td><code>Multiple Myeloma / Plasma Cell</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myelodysplastic / Myeloproliferative Cancers</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neuroblastoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-Hodgkin Lymphoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Osteosarcoma</code></td><td><code>ncit:C9145</code></td><td></td></tr>
<tr><td><code>Ovarian Cancer</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Primary Peritoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retinoblastoma</code></td><td><code>ncit:C7541</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>ncit:C3359</code></td><td></td></tr>
<tr><td><code>Sarcoma, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Salivary Gland</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sebaceous Adenocarcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small Bowel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soft Tissue Sarcoma</code></td><td><code>ncit:C9306</code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thymoma / Thymic Carcinoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urethral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary Tract, NOS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Alemtuzumab</code></td><td><code>rxcui:117055</code></td><td></td></tr>
<tr><td><code>Aleve</code></td><td><code>rxcui:215101</code></td><td></td></tr>
<tr><td><code>Anastrazole (Arimidex)</code></td><td><code>rxcui:84857</code></td><td></td></tr>
<tr><td><code>Azathioprine</code></td><td><code>rxcui:1256</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Bevacizumab</code></td><td><code>rxcui:253337</code></td><td></td></tr>
<tr><td><code>Camizestrant</code></td><td><code>ncit:C160603</code></td><td></td></tr>
<tr><td><code>Capecitabine</code></td><td><code>rxcui:194000</code></td><td></td></tr>
<tr><td><code>CapeOx</code></td><td><code>ncit:C63597</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Celebrex</code></td><td><code>rxcui:215927</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cyclosporine</code></td><td><code>rxcui:3008</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Dacarbazine</code></td><td><code>rxcui:3098</code></td><td></td></tr>
<tr><td><code>Deruxtecan</code></td><td><code>rxcui:2657010</code></td><td></td></tr>
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxil</code></td><td><code>rxcui:80773</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Elacestrant</code></td><td><code>rxcui:2628483</code></td><td></td></tr>
<tr><td><code>Epirubicin</code></td><td><code>rxcui:3995</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Everolimus</code></td><td><code>rxcui:141704</code></td><td></td></tr>
<tr><td><code>Faslodex</code></td><td><code>rxcui:203870</code></td><td></td></tr>
<tr><td><code>Fluorouracil (5FU)</code></td><td><code>rxcui:4492</code></td><td></td></tr>
<tr><td><code>Futibatinib</code></td><td><code>rxcui:2628190</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ibuprofen</code></td><td><code>rxcui:5640</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Immune Checkpoint Inhibitors</code></td><td><code>ncit:C143250</code></td><td></td></tr>
<tr><td><code>Infliximab</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Irinotecan</code></td><td><code>ncit:C62040</code></td><td></td></tr>
<tr><td><code>Ivosidenib</code></td><td><code>rxcui:2049873</code></td><td></td></tr>
<tr><td><code>Leflunomide</code></td><td><code>rxcui:27169</code></td><td></td></tr>
<tr><td><code>Lenvatinib</code></td><td><code>rxcui:1603296</code></td><td></td></tr>
<tr><td><code>Letrozole</code></td><td><code>rxcui:72965</code></td><td></td></tr>
<tr><td><code>Leucovorin</code></td><td><code>rxcui:6313</code></td><td></td></tr>
<tr><td><code>Leuprolide Acetate</code></td><td><code>rxcui:203217</code></td><td></td></tr>
<tr><td><code>Medroxyprogesterone</code></td><td><code>rxcui:6691</code></td><td></td></tr>
<tr><td><code>Metformin</code></td><td><code>ncit:C61612</code></td><td></td></tr>
<tr><td><code>Mizoribine</code></td><td><code>ncit:C66172</code></td><td></td></tr>
<tr><td><code>Mobic</code></td><td><code>rxcui:152699</code></td><td></td></tr>
<tr><td><code>Mycophenolate</code></td><td><code>rxcui:265323</code></td><td></td></tr>
<tr><td><code>Nab-Paclitaxel</code></td><td><code>ncit:C2688</code></td><td></td></tr>
<tr><td><code>Naproxen</code></td><td><code>ncit:C680</code></td><td></td></tr>
<tr><td><code>Niraparib</code></td><td><code>rxcui:1918231</code></td><td></td></tr>
<tr><td><code>Olaparib</code></td><td><code>rxcui:1597582</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Palbociclib</code></td><td><code>ncit:C49176</code></td><td></td></tr>
<tr><td><code>Pazopanib</code></td><td><code>rxcui:714438</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Pemigatinib</code></td><td><code>rxcui:2359268</code></td><td></td></tr>
<tr><td><code>Pertuzumab</code></td><td><code>ncit:C38692</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Ramucirumab</code></td><td><code>ncit:C70792</code></td><td></td></tr>
<tr><td><code>Rapamune</code></td><td><code>rxcui:258355</code></td><td></td></tr>
<tr><td><code>Ribociclib</code></td><td><code>rxcui:1873986</code></td><td></td></tr>
<tr><td><code>Rucaparib</code></td><td><code>rxcui:1862579</code></td><td></td></tr>
<tr><td><code>Sirolimus</code></td><td><code>rxcui:35302</code></td><td></td></tr>
<tr><td><code>Tacrolimus</code></td><td><code>ncit:C1311</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Talazoparib</code></td><td><code>rxcui:2099949</code></td><td></td></tr>
<tr><td><code>Tamoxifen</code></td><td><code>rxcui:10324</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Trastuzumab</code></td><td><code>rxcui:224905</code></td><td></td></tr>
<tr><td><code>Trastuzumab Deruxtecan</code></td><td><code>ncit:C128799</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>rxcui:39541</code></td><td></td></tr>
<tr><td><code>Voltaren</code></td><td><code>rxcui:202976</code></td><td></td></tr>
<tr><td><code>Ziv-Aflibercept</code></td><td><code>rxcui:1946825</code></td><td></td></tr>
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

<div id="enum-modal-performancescoreenum" class="enum-modal" onclick="closeEnumModal('enum-modal-performancescoreenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-performancescoreenum')">×</button>
<h3><code>PerformanceScoreEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ASA &gt;&gt; 1</code></td><td><code>ncit:C174992</code></td><td></td></tr>
<tr><td><code>ASA &gt;&gt; 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ASA &gt;&gt; 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ASA &gt;&gt; 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ASA &gt;&gt; 5</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-probandgenerationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-probandgenerationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-probandgenerationenum')">×</button>
<h3><code>ProbandGenerationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Children's Generation (including nieces and nephews)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Grandchildren's Generation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Grandparents' Generation (including great aunts and uncles)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Great Grandparents' Generation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parents' Generation (including aunts and uncles)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Same Generation (including siblings and cousins)</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdominoperineal Resection</code></td><td><code>ncit:C91826</code></td><td></td></tr>
<tr><td><code>Appendectomy</code></td><td><code>ncit:C51687</code></td><td></td></tr>
<tr><td><code>Bilateral Salpingo-Oophorectomy</code></td><td><code>ncit:C51765</code></td><td></td></tr>
<tr><td><code>Bile Duct</code></td><td><code>ncit:C12376</code></td><td></td></tr>
<tr><td><code>Biopsy, NOS</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Cecectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cholangiocarcinoma</code></td><td><code>ncit:C4436</code></td><td></td></tr>
<tr><td><code>Cold Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cold Snare</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colectomy</code></td><td><code>ncit:C15209</code></td><td></td></tr>
<tr><td><code>Cystectomy</code></td><td><code>ncit:C15217</code></td><td></td></tr>
<tr><td><code>Cystoprostatectomy</code></td><td><code>ncit:C94464</code></td><td></td></tr>
<tr><td><code>Distal Pancreatoduodenectomy (Distal Pancreatectomy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endoscopic Mucosal Resection</code></td><td><code>ncit:C103242</code></td><td></td></tr>
<tr><td><code>Endoscopic Submucosal Dissection</code></td><td><code>ncit:C157837</code></td><td></td></tr>
<tr><td><code>Esophagectomy</code></td><td><code>ncit:C15357</code></td><td></td></tr>
<tr><td><code>Gallbladder Surgery</code></td><td><code>ncit:C157797</code></td><td></td></tr>
<tr><td><code>Gastrectomy</code></td><td><code>ncit:C15236</code></td><td></td></tr>
<tr><td><code>Hemicolectomy</code></td><td><code>ncit:C86074</code></td><td></td></tr>
<tr><td><code>Hot Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hot Snare</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hysterectomy</code></td><td><code>ncit:C15256</code></td><td></td></tr>
<tr><td><code>Ileocolonic Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ileorectal Anastamosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ileosigmoid Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low Anterior Resection</code></td><td><code>ncit:C113716</code></td><td></td></tr>
<tr><td><code>Lumpectomy</code></td><td><code>ncit:C15755</code></td><td></td></tr>
<tr><td><code>Mastectomy</code></td><td><code>ncit:C15277</code></td><td></td></tr>
<tr><td><code>Nephrectomy</code></td><td><code>ncit:C15284</code></td><td></td></tr>
<tr><td><code>Nephroureterectomy/Ureterectomy</code></td><td><code>ncit:C51646</code></td><td></td></tr>
<tr><td><code>Oophorectomy, NOS</code></td><td><code>ncit:C15291</code></td><td></td></tr>
<tr><td><code>Partial Gastrectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostatectomy</code></td><td><code>ncit:C15307</code></td><td></td></tr>
<tr><td><code>Random Gastric Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Roux-En-Y</code></td><td><code>ncit:C51758</code></td><td></td></tr>
<tr><td><code>Salpingectomy</code></td><td><code>ncit:C51605</code></td><td></td></tr>
<tr><td><code>Sigmoid Colectomy</code></td><td><code>ncit:C91838</code></td><td></td></tr>
<tr><td><code>Sleeve Gastrectomy</code></td><td><code>ncit:C167213</code></td><td></td></tr>
<tr><td><code>Small Bowel Resection</code></td><td><code>ncit:C51510</code></td><td></td></tr>
<tr><td><code>Total Abdominal Hysterectomy</code></td><td><code>ncit:C51695</code></td><td></td></tr>
<tr><td><code>Total Abdominal Hysterectomy With A Bilateral Salpingo-Oophorectomy</code></td><td><code>ncit:C51761</code></td><td></td></tr>
<tr><td><code>Total Colectomy with End Ileostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Colectomy with Ileorectal Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Colectomy with Ileosigmoid Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Gastrectomy</code></td><td><code>ncit:C185240</code></td><td></td></tr>
<tr><td><code>Total Pancreatectomy</code></td><td><code>ncit:C51933</code></td><td></td></tr>
<tr><td><code>Total Proctocolectomy with End Ileostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Proctocolectomy with Ileal Pouch</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transverse Hemicolectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Whipple Pancreaticoduodenectomy</code></td><td><code>ncit:C15356</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Appendiceal Orifice</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ascending Colon</code></td><td><code>ncit:C12265</code></td><td></td></tr>
<tr><td><code>Cecum</code></td><td><code>ncit:C12381</code></td><td></td></tr>
<tr><td><code>Descending Colon</code></td><td><code>ncit:C12268</code></td><td></td></tr>
<tr><td><code>Hepatic Flexure</code></td><td><code>ncit:C12266</code></td><td></td></tr>
<tr><td><code>Ileocecal Valve</code></td><td><code>ncit:C13066</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Sigmoid Colon</code></td><td><code>ncit:C12384</code></td><td></td></tr>
<tr><td><code>Sigmoid Flexure</code></td><td><code>ncit:C33550</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Splenic Flexure</code></td><td><code>ncit:C12267</code></td><td></td></tr>
<tr><td><code>Terminal Ileum</code></td><td><code>ncit:C33757</code></td><td></td></tr>
<tr><td><code>Transverse Colon</code></td><td><code>ncit:C12385</code></td><td></td></tr>
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

<div id="enum-modal-racespecifiedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-racespecifiedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-racespecifiedenum')">×</button>
<h3><code>RaceSpecifiedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Asian Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bangladeshi</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Baram/Burman</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bengali</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bhutanese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Burmese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cambodian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chinese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Filipino</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hmong</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hongkonger</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Indonesian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Japanese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kazakh/Qazaq</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kazakhstani</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Korean</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laotian/Lao</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Malay</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Malaysian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nepalese/Nepali</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Okinawan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pakistani</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Singaporean</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sri Lankan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tagalog</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Taiwanese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thai</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vietnamese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Agikuyu/Kikuyu</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Akan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Amara/Amhara</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Australian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bahamian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bantu</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Barbadian/Bajan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cameroonian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Congolese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eritrean</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ethiopian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fijian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Grenadian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Guamanian or Chamorro</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Haitian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ivoirian/Cote d'Ivoire</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Jamaican</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kenyan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liberian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Libyan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mende</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Native Hawaiian/Hawaiian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nevis Islander/ Kittitian/Nevisian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>New Zealander</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nigerian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oromo</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Polynesian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Samoan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Shona</code></td><td><code></code></td><td></td></tr>
<tr><td><code>St Lucia Islander/ Saint Lucian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tahitian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tanzanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Temne/Temme/Themne</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tigrinya/Tigray/Tigraway</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Togolese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tongan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>U.S. Virgin Islander</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ugandan</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Part Hawaiian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acadian/Cajun</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Afghanistani/Afghan/ Afghani</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Albanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Algerian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alsatian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arab/Arabic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Armenian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Assyrian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Austrian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Azerbaijani</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Azeri</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Belgian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Belorussian/Belarusian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Berber/Amazigh/ Imazighen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bosniak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>British Isles/ British Isles origin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>British/Briton</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bulgarian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Canadian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Celtic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chaldean</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Croatian/Croat</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cypriot</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Czech</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Czechoslovakian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Danish/Dane</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dutch</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dutch West Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Egyptian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>English</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Estonian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Finnish/Finn</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flemish/Fleming</code></td><td><code></code></td><td></td></tr>
<tr><td><code>French</code></td><td><code></code></td><td></td></tr>
<tr><td><code>French Canadian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Georgian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>German</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Greek</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Herzegovinian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hungarian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Icelander</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iranian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iraqi</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Irish</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Israeli</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Italian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Jordanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Karelian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kurdish/Kurd</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kuwaiti</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Latvian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lebanese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lithuanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Luxemburger</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Macedonian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Maltese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Norwegian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Palestinian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pennsylvania German</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Persian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Polish/Pole</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Portuguese</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Romanian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Russian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Saudi/Saudi Arabian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scandinavian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scotch Irish</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scottish</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Serbian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Slavic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Slovak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Slovene</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soviet</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Swedish/Swede</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Swiss</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Syriac</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Syrian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Turkish/Turk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ukrainian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>United Arab Emirates/ Emirati</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uzbeg/Uzbek</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uzbekistani</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Welsh</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yemeni</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yugoslavian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Native American</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alaska Native</code></td><td><code></code></td><td></td></tr>
<tr><td><code>First Nation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inuit</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Specified</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Left System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lost to Follow-Up</code></td><td><code>ncit:C70740</code></td><td></td></tr>
<tr><td><code>Withdrawal of Consent</code></td><td><code>ncit:C48271</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-regimenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-regimenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-regimenenum')">×</button>
<h3><code>RegimenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CapeOx</code></td><td><code>ncit:C63597</code></td><td></td></tr>
<tr><td><code>Carboplatin/Paclitaxel</code></td><td><code>ncit:C63402</code></td><td></td></tr>
<tr><td><code>Cisplatin/Gemcitabine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cisplatin/Gemcitabine + Immune Checkpoint Inhibitor (Durvalumab, Pembrolizumab, etc)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cisplatin/Gemcitabine/Nab-paclitaxel</code></td><td><code>ncit:C188462</code></td><td></td></tr>
<tr><td><code>FLOT</code></td><td><code>ncit:C160565</code></td><td></td></tr>
<tr><td><code>FOLFIRI</code></td><td><code>ncit:C63593</code></td><td></td></tr>
<tr><td><code>FOLFIRINOX</code></td><td><code>ncit:C11764</code></td><td></td></tr>
<tr><td><code>FOLFOX</code></td><td><code>ncit:C63594</code></td><td></td></tr>
<tr><td><code>Futibatinib/Pemigatinib</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-relationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-relationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-relationenum')">×</button>
<h3><code>RelationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Father</code></td><td><code>ncit:C96572</code></td><td></td></tr>
<tr><td><code>Mother</code></td><td><code>ncit:C96580</code></td><td></td></tr>
<tr><td><code>Sibling</code></td><td><code>ncit:C96586</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
<tr><td><code>Half-Sibling</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Child</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Grandmother</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Grandfather</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Niece or Nephew</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Great Grandfather</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Great Grandmother</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Great Uncle</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Great Aunt</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-relationlineageenum" class="enum-modal" onclick="closeEnumModal('enum-modal-relationlineageenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-relationlineageenum')">×</button>
<h3><code>RelationLineageEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Maternal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paternal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unspecified</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-remainingcolonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-remainingcolonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-remainingcolonenum')">×</button>
<h3><code>RemainingColonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ascending Colon</code></td><td><code>ncit:C12265</code></td><td></td></tr>
<tr><td><code>Cecum</code></td><td><code>ncit:C12381</code></td><td></td></tr>
<tr><td><code>Descending Colon</code></td><td><code>ncit:C12268</code></td><td></td></tr>
<tr><td><code>Hepatic Flexure</code></td><td><code>ncit:C12266</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Sigmoid Colon</code></td><td><code>ncit:C33550</code></td><td></td></tr>
<tr><td><code>Sigmoid Flexure</code></td><td><code>ncit:C12384</code></td><td></td></tr>
<tr><td><code>Splenic Flexure</code></td><td><code>ncit:C12267</code></td><td></td></tr>
<tr><td><code>Transverse Colon</code></td><td><code>ncit:C12385</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-reportedsignificanceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reportedsignificanceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reportedsignificanceenum')">×</button>
<h3><code>ReportedSignificanceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Benign</code></td><td><code>ncit:C168802</code></td><td></td></tr>
<tr><td><code>Likely Benign</code></td><td><code>ncit:C168801</code></td><td></td></tr>
<tr><td><code>Likely Pathogenic</code></td><td><code>ncit:C168800</code></td><td></td></tr>
<tr><td><code>Pathogenic</code></td><td><code>ncit:C168799</code></td><td></td></tr>
<tr><td><code>Uncertain Significance</code></td><td><code>ncit:C94187</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Non-Response</code></td><td><code>ncit:C173526</code></td><td></td></tr>
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

<div id="enum-modal-sedationtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sedationtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sedationtypeenum')">×</button>
<h3><code>SedationTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Moderate Sedation (Fentanyl, Midazolam, Diphenhydramine, Meperidine)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Monitored Anesthesia Care (Propofol)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No Sedation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-sexatbirthenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sexatbirthenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sexatbirthenum')">×</button>
<h3><code>SexAtBirthEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Male</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Benign</code></td><td><code>ncit:C14172</code></td><td></td></tr>
<tr><td><code>Local Extension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metastatic</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Premalignant</code></td><td><code>ncit:C25624</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
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
<tr><td><code>Group 1</code></td><td><code>ncit:C137992</code></td><td></td></tr>
<tr><td><code>Group 2</code></td><td><code>ncit:C137993</code></td><td></td></tr>
<tr><td><code>Group 3</code></td><td><code>ncit:C137994</code></td><td></td></tr>
<tr><td><code>Group 4</code></td><td><code>ncit:C137995</code></td><td></td></tr>
<tr><td><code>Group 5</code></td><td><code>ncit:C137996</code></td><td></td></tr>
<tr><td><code>Stage IIa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stage IIb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stage IIc</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stage IIIa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stage IIIb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stage IIIc</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Gleason Grading System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TNM Staging System</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>LINEAGE</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>M2</code></td><td><code>ncit:C48704</code></td><td></td></tr>
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
<tr><td><code>NX</code></td><td><code>ncit:C48718</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tnmoverallenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tnmoverallenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tnmoverallenum')">×</button>
<h3><code>TnmOverallEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>I</code></td><td><code></code></td><td></td></tr>
<tr><td><code>II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>III</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>T3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T4</code></td><td><code>ncit:C48732</code></td><td></td></tr>
<tr><td><code>TX</code></td><td><code>ncit:C48737</code></td><td></td></tr>
<tr><td><code>Tis</code></td><td><code>ncit:C48738</code></td><td></td></tr>
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

<div id="enum-modal-tumorbuddingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorbuddingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorbuddingenum')">×</button>
<h3><code>TumorBuddingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>High Budding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intermediate Budding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low Budding</code></td><td><code></code></td><td></td></tr>
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
    "ls": {
      "name": "ls",
      "title": "Lynch Syndrome",
      "description": "The LS view of the PCDC data model represents consensus data modeling by an international group of Lynch Syndrome experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Lynch Syndrome Integrative Epidemiology and Genetics Consortium (LINEAGE). It is based on the collective requirements of its contributors."
    }
  },
  "classes": {
    "Subject": {
      "slots": [
        "consortium",
        "disease_group",
        "sex",
        "race",
        "race_other",
        "race_specified",
        "ethnicity",
        "ethnicity_other",
        "ethnicity_specified",
        "ashkenazi_jewish_ancestry",
        "proband_status"
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
        "year_at_enrollment"
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
    "FamilyMedicalHistory": {
      "slots": [
        "family_medical_history_condition",
        "relation",
        "relation_lineage",
        "lkss_of_relative",
        "age_at_lkss_of_relative",
        "proband_generation",
        "age_at_condition",
        "sex_at_birth",
        "age_at_time_of_pedigree_creation",
        "year_at_pedigree_creation"
      ],
      "comments": [
        "D4CGNote: One observation/row per CONDITION when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Priority."
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "MedicalHistory": {
      "slots": [
        "age_at_condition",
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
    "SocialAndBehavioralDeterminantsOfHealth": {
      "slots": [
        "age_at_status",
        "gender_identity",
        "exposure",
        "exposure_status"
      ],
      "comments": [
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(fprh) ConsortiumNote: This table is tiered as Optional."
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
    "GeneticAnalysis": {
      "slots": [
        "age_at_genetic_analysis",
        "genomic_source_class",
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "alteration_region",
        "chromosome",
        "chromosomal_translocation_partner",
        "cytoband",
        "iscn",
        "gene",
        "gene_fusion_partner",
        "exon_number",
        "hgvs_genomic_transcript",
        "hgvs_genomic",
        "hgvs_coding_transcript",
        "hgvs_coding",
        "hgvs_protein_transcript",
        "hgvs_protein",
        "reference_genome",
        "reference_genome_accession",
        "reported_significance",
        "reported_significance_other",
        "external_ref_id_system",
        "external_ref_id",
        "copy_number",
        "maf_numeric",
        "vaf_numeric",
        "dna_index_numeric",
        "allelic_state",
        "allelic_ratio"
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
        "result_text"
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
        "year_at_diagnosis",
        "age_at_diag_resolved",
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
        "tnm_tumor_t",
        "tnm_node_n",
        "tnm_metastasis_m",
        "tnm_overall",
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
        "tumor_state",
        "detection_method",
        "sedation_type",
        "site_classification",
        "disease_site",
        "laterality",
        "measurement1",
        "measurement1_axis",
        "measurement2",
        "measurement2_axis",
        "measurement3",
        "measurement3_axis",
        "measurement_unit",
        "top_code",
        "top_code_text",
        "top_code_system",
        "top_code_system_version",
        "finding",
        "colon_polyp_max_size",
        "colon_polyp_min_size",
        "barretts_esophagus",
        "bowel_preparation",
        "bbps_score",
        "bbps_score_total",
        "tumor_budding",
        "number_nodes_numeric",
        "colon_polyps_total",
        "gastric_polyps_total",
        "small_bowel_polyps_total"
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
        "site_classification",
        "procedure",
        "procedure_site",
        "laterality",
        "procedure_extent",
        "remaining_colon"
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
        "medication",
        "regimen",
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
    "LocoregionalTherapy": {
      "slots": [
        "age_at_locoregional_therapy",
        "administration_status",
        "locoregional_therapy_technique"
      ],
      "comments": [
        "D4CGNote: One observation/row per locoregional therapy when instantiated."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response_category",
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
    "age_at_status": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "relation": {
      "slot_uri": "ncit:C21480",
      "range": "RelationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,rb",
        "tier_optional": "fa,hl,ls"
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
    "histology_grade": {
      "slot_uri": "ncit:C18000",
      "range": "HistologyGradeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
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
    "review_source": {
      "slot_uri": "ncit:C185324",
      "range": "ReviewSourceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "npc,ls"
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
    "measurement3_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "regimen": {
      "slot_uri": "ncit:C15697",
      "range": "RegimenEnum",
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
    "ethnicity_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "external_resource_icon_path": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "relation_lineage": {
      "slot_uri": "",
      "range": "RelationLineageEnum",
      "comments": [],
      "annotations": {}
    },
    "sedation_type": {
      "slot_uri": "",
      "range": "SedationTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "measurement2_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    },
    "external_links": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "race_other": {
      "slot_uri": "",
      "range": "string",
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
    "external_resource_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "gender_identity": {
      "slot_uri": "",
      "range": "GenderIdentityEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,ls"
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
    "hgvs_genomic": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
      }
    },
    "hgvs_genomic_transcript": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "colon_polyp_min_size": {
      "slot_uri": "",
      "range": "ColonPolypMinSizeEnum",
      "comments": [],
      "annotations": {}
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
    "age_at_locoregional_therapy": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "age_at_genetic_analysis": {
      "slot_uri": "ncit:C168848",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "cytoband": {
      "slot_uri": "ncit:C13202",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "colon_polyps_total": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "remaining_colon": {
      "slot_uri": "",
      "range": "RemainingColonEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "proband_generation": {
      "slot_uri": "",
      "range": "ProbandGenerationEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "bbps_score": {
      "slot_uri": "ncit:C138206",
      "range": "BbpsScoreEnum",
      "comments": [],
      "annotations": {}
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
    "exposure": {
      "slot_uri": "ncit:C17941",
      "range": "ExposureEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
      }
    },
    "family_medical_history_condition": {
      "slot_uri": "ncit:C18772",
      "range": "string",
      "comments": [
        "(fa) ConsortiumNote: Prioritize the following conditions: Fanconi Anemia, Squamous Cell Carcinoma, Breast Cancer, Ovarian Cancer, Leukemia, Cancer, NOS, Vertebral Anomaly, Anal Anomaly, Cardiac Structure Anomaly, Esophageal or Duodenal Atresia, Renal Anomaly, Upper Limb Anomaly, Hydrocephalus, Skin Pigmentation, Small Head, Small Eyes, Nervous System Abnormality, Otological Abnormality, and Short Stature."
      ],
      "annotations": {
        "tier_mandatory": "fa",
        "tier_priority": "npc,rb",
        "tier_optional": "hl,ls"
      }
    },
    "proband_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "reference_genome_accession": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
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
    "measurement1_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "exon_number": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "ethnicity_specified": {
      "slot_uri": "",
      "range": "EthnicitySpecifiedEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "finding": {
      "slot_uri": "",
      "range": "FindingEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "bbps_score_total": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
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
    "year_at_pedigree_creation": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "sex_at_birth": {
      "slot_uri": "",
      "range": "SexAtBirthEnum",
      "comments": [],
      "annotations": {}
    },
    "hgvs_protein_transcript": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "locoregional_therapy_technique": {
      "slot_uri": "",
      "range": "LocoregionalTherapyTechniqueEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_time_of_pedigree_creation": {
      "slot_uri": "",
      "range": "integer",
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
    "age_at_lkss_of_relative": {
      "slot_uri": "ncit:C168844",
      "range": "integer",
      "comments": [],
      "annotations": {
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
    "vaf_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "year_at_diagnosis": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
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
    "tumor_budding": {
      "slot_uri": "",
      "range": "TumorBuddingEnum",
      "comments": [],
      "annotations": {}
    },
    "reported_significance_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "chromosomal_translocation_partner": {
      "slot_uri": "",
      "range": "ChromosomalTranslocationPartnerEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "lkss_of_relative": {
      "slot_uri": "",
      "range": "LkssOfRelativeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,ls",
        "tier_priority": "rb"
      }
    },
    "bowel_preparation": {
      "slot_uri": "ncit:C62659",
      "range": "BowelPreparationEnum",
      "comments": [],
      "annotations": {}
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
    "external_subject_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "tnm_overall": {
      "slot_uri": "",
      "range": "TnmOverallEnum",
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
    "markers": {
      "slot_uri": "ncit:C51944",
      "range": "MarkersEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "age_at_lab": {
      "slot_uri": "ncit:C172691",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "race_specified": {
      "slot_uri": "",
      "range": "RaceSpecifiedEnum",
      "comments": [],
      "annotations": {}
    },
    "hgvs_coding_transcript": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "barretts_esophagus": {
      "slot_uri": "",
      "range": "BarrettsEsophagusEnum",
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
    "external_subject_url": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
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
    "reported_significance": {
      "slot_uri": "",
      "range": "ReportedSignificanceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "ls"
      }
    },
    "gastric_polyps_total": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "ashkenazi_jewish_ancestry": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
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
    "age_at_diag_resolved": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
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
    "exposure_status": {
      "slot_uri": "",
      "range": "ExposureStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
      }
    },
    "colon_polyp_max_size": {
      "slot_uri": "",
      "range": "ColonPolypMaxSizeEnum",
      "comments": [],
      "annotations": {}
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
    },
    "small_bowel_polyps_total": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "number_nodes_numeric": {
      "slot_uri": "ncit:C124446",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
      }
    }
  },
  "enums": {
    "ColonPolypMinSizeEnum": {
      "permissible_values": {
        "1-5 mm": {
          "meaning": "",
          "comments": []
        },
        "10-19 mm": {
          "meaning": "",
          "comments": []
        },
        "20+ mm": {
          "meaning": "",
          "comments": []
        },
        "6-9 mm": {
          "meaning": "",
          "comments": []
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
        "T3": {
          "meaning": "",
          "comments": []
        },
        "T4": {
          "meaning": "ncit:C48732",
          "comments": []
        },
        "TX": {
          "meaning": "ncit:C48737",
          "comments": []
        },
        "Tis": {
          "meaning": "ncit:C48738",
          "comments": []
        }
      }
    },
    "TnmOverallEnum": {
      "permissible_values": {
        "I": {
          "meaning": "",
          "comments": []
        },
        "II": {
          "meaning": "",
          "comments": []
        },
        "III": {
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
    "ReasonOffEnum": {
      "permissible_values": {
        "Left System": {
          "meaning": "",
          "comments": []
        },
        "Lost to Follow-Up": {
          "meaning": "ncit:C70740",
          "comments": []
        },
        "Withdrawal of Consent": {
          "meaning": "ncit:C48271",
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
    "AllelicStateEnum": {
      "permissible_values": {
        "Compound Heterozygous": {
          "meaning": "ncit:C198518",
          "comments": []
        },
        "Hemizygous": {
          "meaning": "ncit:C64346",
          "comments": []
        },
        "Heterozygous": {
          "meaning": "ncit:C45825",
          "comments": []
        },
        "Homozygous": {
          "meaning": "ncit:C45826",
          "comments": []
        },
        "Mosaic": {
          "meaning": "ncit:C88144",
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
    "RegimenEnum": {
      "permissible_values": {
        "CapeOx": {
          "meaning": "ncit:C63597",
          "comments": []
        },
        "Carboplatin/Paclitaxel": {
          "meaning": "ncit:C63402",
          "comments": []
        },
        "Cisplatin/Gemcitabine": {
          "meaning": "",
          "comments": []
        },
        "Cisplatin/Gemcitabine + Immune Checkpoint Inhibitor (Durvalumab, Pembrolizumab, etc)": {
          "meaning": "",
          "comments": []
        },
        "Cisplatin/Gemcitabine/Nab-paclitaxel": {
          "meaning": "ncit:C188462",
          "comments": []
        },
        "FLOT": {
          "meaning": "ncit:C160565",
          "comments": []
        },
        "FOLFIRI": {
          "meaning": "ncit:C63593",
          "comments": []
        },
        "FOLFIRINOX": {
          "meaning": "ncit:C11764",
          "comments": []
        },
        "FOLFOX": {
          "meaning": "ncit:C63594",
          "comments": []
        },
        "Futibatinib/Pemigatinib": {
          "meaning": "",
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
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Acoustic Neuroma": {
          "meaning": "",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia": {
          "meaning": "ncit:C3167",
          "comments": []
        },
        "Acute Myeloid Leukemia": {
          "meaning": "ncit:C3171",
          "comments": []
        },
        "Angiosarcoma": {
          "meaning": "",
          "comments": []
        },
        "Appendiceal": {
          "meaning": "",
          "comments": []
        },
        "Astrocytoma": {
          "meaning": "",
          "comments": []
        },
        "Basal Cell Carcinoma": {
          "meaning": "",
          "comments": []
        },
        "Bone Cancer": {
          "meaning": "ncit:C131533",
          "comments": []
        },
        "Brain Cancer": {
          "meaning": "ncit:C131533",
          "comments": []
        },
        "Ewing Sarcoma": {
          "meaning": "",
          "comments": []
        },
        "Intraocular Melanoma": {
          "meaning": "",
          "comments": []
        },
        "Kidney (Renal Cell)": {
          "meaning": "",
          "comments": []
        },
        "Melanoma": {
          "meaning": "ncit:C3224",
          "comments": []
        },
        "Multiple Myeloma / Plasma Cell": {
          "meaning": "",
          "comments": []
        },
        "Myelodysplastic / Myeloproliferative Cancers": {
          "meaning": "",
          "comments": []
        },
        "Neuroblastoma": {
          "meaning": "",
          "comments": []
        },
        "Non-Hodgkin Lymphoma": {
          "meaning": "",
          "comments": []
        },
        "Osteosarcoma": {
          "meaning": "ncit:C9145",
          "comments": []
        },
        "Ovarian Cancer": {
          "meaning": "",
          "comments": []
        },
        "Primary Peritoneal": {
          "meaning": "",
          "comments": []
        },
        "Retinoblastoma": {
          "meaning": "ncit:C7541",
          "comments": []
        },
        "Rhabdomyosarcoma": {
          "meaning": "ncit:C3359",
          "comments": []
        },
        "Sarcoma, NOS": {
          "meaning": "",
          "comments": []
        },
        "Salivary Gland": {
          "meaning": "",
          "comments": []
        },
        "Sebaceous Adenocarcinoma": {
          "meaning": "",
          "comments": []
        },
        "Skin, NOS": {
          "meaning": "",
          "comments": []
        },
        "Small Bowel": {
          "meaning": "",
          "comments": []
        },
        "Soft Tissue Sarcoma": {
          "meaning": "ncit:C9306",
          "comments": []
        },
        "Stomach": {
          "meaning": "",
          "comments": []
        },
        "Testicular": {
          "meaning": "",
          "comments": []
        },
        "Thymoma / Thymic Carcinoma": {
          "meaning": "",
          "comments": []
        },
        "Urethral": {
          "meaning": "",
          "comments": []
        },
        "Urinary Tract, NOS": {
          "meaning": "",
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
    "ExposureStatusEnum": {
      "permissible_values": {
        "Current": {
          "meaning": "",
          "comments": []
        },
        "Ever": {
          "meaning": "ncit:C159710",
          "comments": []
        },
        "Never": {
          "meaning": "ncit:C70543",
          "comments": []
        },
        "Past": {
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
    "BbpsScoreEnum": {
      "permissible_values": {
        "Segment Score 0": {
          "meaning": "ncit:C138207",
          "comments": []
        },
        "Segment Score 1": {
          "meaning": "ncit:C138208",
          "comments": []
        },
        "Segment Score 2": {
          "meaning": "ncit:C138209",
          "comments": []
        },
        "Segment Score 3": {
          "meaning": "ncit:C138210",
          "comments": []
        },
        "Surgically Absent": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "HistologyGradeEnum": {
      "permissible_values": {
        "Gleason >> Grade Group 1": {
          "meaning": "",
          "comments": []
        },
        "Gleason >> Grade Group 2": {
          "meaning": "",
          "comments": []
        },
        "Gleason >> Grade Group 3": {
          "meaning": "",
          "comments": []
        },
        "Gleason >> Grade Group 4": {
          "meaning": "",
          "comments": []
        },
        "Gleason >> Grade Group 5": {
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
        "WHO Glioma >> Grade I": {
          "meaning": "",
          "comments": []
        },
        "WHO Glioma >> Grade II": {
          "meaning": "",
          "comments": []
        },
        "WHO Glioma >> Grade III": {
          "meaning": "",
          "comments": []
        },
        "WHO Glioma >> Grade IV": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
    "FindingEnum": {
      "permissible_values": {
        "Blunting Atrophy": {
          "meaning": "",
          "comments": []
        },
        "Diverticulosis": {
          "meaning": "",
          "comments": []
        },
        "Duodenitis": {
          "meaning": "",
          "comments": []
        },
        "Excavated (III) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Extranodal Tumor Deposit": {
          "meaning": "",
          "comments": []
        },
        "Flat (IIb) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Gastric Atrophy": {
          "meaning": "",
          "comments": []
        },
        "Gastric Ulcer(s)": {
          "meaning": "",
          "comments": []
        },
        "Gastritis / Inflammation/ Erythema/ Edema": {
          "meaning": "",
          "comments": []
        },
        "Gastropathy": {
          "meaning": "",
          "comments": []
        },
        "Jejunitis": {
          "meaning": "",
          "comments": []
        },
        "Lymphatic Vascular Invasion": {
          "meaning": "",
          "comments": []
        },
        "Macroscopic Tumor Perforation": {
          "meaning": "",
          "comments": []
        },
        "Pedunculated (Ip) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Perineural Invasion": {
          "meaning": "",
          "comments": []
        },
        "Semi-Pedunculated (Isp) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Sessile (Is) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Slightly Depressed (IIc) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Slightly Elevated (IIa) Polyp": {
          "meaning": "",
          "comments": []
        },
        "Small Bowel Ulcer(s)": {
          "meaning": "",
          "comments": []
        },
        "Visual Ampulla": {
          "meaning": "",
          "comments": []
        },
        "Visualized Mucosa": {
          "meaning": "",
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
        "Saliva": {
          "meaning": "ncit:C174119",
          "comments": []
        },
        "Stool Sample": {
          "meaning": "ncit:C189125",
          "comments": []
        },
        "Tumor Sample": {
          "meaning": "ncit:C18009",
          "comments": []
        },
        "Urine": {
          "meaning": "ncit:C13283",
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
        "Mutated": {
          "meaning": "",
          "comments": []
        },
        "Wild Type": {
          "meaning": "ncit:C62195",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "StageSystemEnum": {
      "permissible_values": {
        "Gleason Grading System": {
          "meaning": "",
          "comments": []
        },
        "TNM Staging System": {
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
        "LINEAGE": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Acute lymphoblastic leukemia": {
          "meaning": "icdo:9828/3",
          "comments": []
        },
        "Acute myeloid leukemia": {
          "meaning": "icdo:9861/3",
          "comments": []
        },
        "Adenocarcinoma": {
          "meaning": "icdo:8140/3",
          "comments": []
        },
        "Adenosquamous carcinoma": {
          "meaning": "icdo:8560/3",
          "comments": []
        },
        "Adrenal cortical carcinoma": {
          "meaning": "icdo:8370/3",
          "comments": []
        },
        "Astrocytoma": {
          "meaning": "icdo:9400/3",
          "comments": []
        },
        "Basal cell carcinoma": {
          "meaning": "icdo:8090/3",
          "comments": []
        },
        "Borderline tumor": {
          "meaning": "",
          "comments": [
            "(ls) ConsortiumNote: Use for Ovarian/Fallopian Tube/Primary Peritoneal Histology"
          ]
        },
        "Carcinoma, NOS": {
          "meaning": "icdo:8010/3",
          "comments": []
        },
        "Carcinosarcoma": {
          "meaning": "icdo:8980/3",
          "comments": []
        },
        "Cholangiocarcinoma": {
          "meaning": "icdo:8160/3",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Chordoma": {
          "meaning": "ncit:C2947",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Chronic lymphocytic leukemia": {
          "meaning": "icdo:9823/3",
          "comments": []
        },
        "Chronic myeloid leukemia": {
          "meaning": "icdo:9863/3",
          "comments": []
        },
        "Clear cell carcinoma": {
          "meaning": "icdo:9863/3",
          "comments": []
        },
        "Cutaneous T-cell lymphoma": {
          "meaning": "icdo:9709/3",
          "comments": []
        },
        "Ductal carcinoma in situ": {
          "meaning": "icdo:9709/3",
          "comments": []
        },
        "Endometrioid adenocarcinoma": {
          "meaning": "icdo:8380/3",
          "comments": []
        },
        "Ewing Sarcoma": {
          "meaning": "icdo:9260/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Gastrointestinal stromal tumor": {
          "meaning": "icdo:8936/3",
          "comments": []
        },
        "Germ cell tumor": {
          "meaning": "",
          "comments": []
        },
        "Glioma, NOS": {
          "meaning": "",
          "comments": []
        },
        "Hairy cell leukemia": {
          "meaning": "icdo:9940/3",
          "comments": []
        },
        "Hepatocellular carcinoma": {
          "meaning": "icdo:8170/3",
          "comments": []
        },
        "High-grade serous carcinoma": {
          "meaning": "icdo:8461/3",
          "comments": []
        },
        "Hodgkin lymphoma": {
          "meaning": "icdo:9650/3",
          "comments": []
        },
        "Hyperplastic polyp": {
          "meaning": "",
          "comments": []
        },
        "Infiltrating ductular carcinoma": {
          "meaning": "icdo:8521/3",
          "comments": []
        },
        "Invasive ductal carcinoma": {
          "meaning": "",
          "comments": []
        },
        "Invasive lobular carcinoma": {
          "meaning": "icdo:8520/3",
          "comments": []
        },
        "Kaposi Sarcoma": {
          "meaning": "icdo:9140/3",
          "comments": []
        },
        "Keratoacanthoma": {
          "meaning": "",
          "comments": []
        },
        "Low-grade dysplasia": {
          "meaning": "",
          "comments": []
        },
        "Lymphoma, NOS": {
          "meaning": "icdo:9590/3",
          "comments": []
        },
        "MDS/MPN, NOS": {
          "meaning": "icdo:9989/3",
          "comments": []
        },
        "Medullary carcinoma": {
          "meaning": "icdo:8510/3",
          "comments": []
        },
        "Medulloblastoma": {
          "meaning": "icdo:9473/3",
          "comments": []
        },
        "Melanoma": {
          "meaning": "icdo:8720/3",
          "comments": []
        },
        "Mesothelioma": {
          "meaning": "icdo:9050/3",
          "comments": []
        },
        "Metaplastic carcinoma": {
          "meaning": "icdo:8575/3",
          "comments": []
        },
        "Mucinous adenocarcinoma": {
          "meaning": "icdo:8480/3",
          "comments": []
        },
        "Mullerian carcinoma": {
          "meaning": "icdo:8950/3",
          "comments": []
        },
        "Multiple myeloma": {
          "meaning": "icdo:9732/3",
          "comments": []
        },
        "Neuroblastoma": {
          "meaning": "icdo:9500/3",
          "comments": []
        },
        "Neuroendocrine tumor": {
          "meaning": "icdo:8249/3",
          "comments": []
        },
        "Non-Hodgkin lymphoma": {
          "meaning": "icdo:9591/3",
          "comments": []
        },
        "Non-small cell carcinoma": {
          "meaning": "icdo:8046/3",
          "comments": []
        },
        "Oligodendroglioma, NOS": {
          "meaning": "icdo:9450/3",
          "comments": []
        },
        "Osteosarcoma": {
          "meaning": "icdo:9180/3",
          "comments": []
        },
        "Papillary carcinoma": {
          "meaning": "icdo:8050/3",
          "comments": []
        },
        "Paraganglioma, malignant": {
          "meaning": "icdo:8680/3",
          "comments": []
        },
        "Pituitary adenoma": {
          "meaning": "icdo:8272/0",
          "comments": []
        },
        "Renal cell carcinoma": {
          "meaning": "icdo:8312/3",
          "comments": []
        },
        "Retinoblastoma": {
          "meaning": "icdo:9510/3",
          "comments": []
        },
        "Rhabdomyosarcoma": {
          "meaning": "ncit:C3359",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Sarcoma, NOS": {
          "meaning": "icdo:8800/3",
          "comments": []
        },
        "Serous carcinoma": {
          "meaning": "",
          "comments": []
        },
        "Sessile serrated lesion": {
          "meaning": "",
          "comments": []
        },
        "Signet ring cell carcinoma": {
          "meaning": "icdo:8490/3",
          "comments": []
        },
        "Small cell carcinoma": {
          "meaning": "icdo:8041/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, NOS": {
          "meaning": "icdo:8070/3",
          "comments": []
        },
        "Traditional serrated adenoma": {
          "meaning": "",
          "comments": []
        },
        "Tubular adenoma": {
          "meaning": "",
          "comments": []
        },
        "Tubulovillous adenoma": {
          "meaning": "",
          "comments": []
        },
        "Urothelial carcinoma": {
          "meaning": "icdo:8120/3",
          "comments": []
        },
        "Villous adenoma": {
          "meaning": "",
          "comments": []
        },
        "Condyloma": {
          "meaning": "",
          "comments": []
        },
        "Hamartoma": {
          "meaning": "",
          "comments": []
        },
        "Inflammatory Polyp": {
          "meaning": "",
          "comments": []
        },
        "Inflammation (neutrophils, lymphocytes, eosinophils)": {
          "meaning": "",
          "comments": []
        },
        "Juvenile Polyp": {
          "meaning": "",
          "comments": []
        },
        "Lipoma": {
          "meaning": "",
          "comments": []
        },
        "Lymphoid Aggregate": {
          "meaning": "",
          "comments": []
        },
        "Normal Colonic Mucosa": {
          "meaning": "",
          "comments": []
        },
        "Oligodendroglial-astrocytic": {
          "meaning": "",
          "comments": []
        },
        "Scar": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Attachment Device (Cap, Endocuff, etc.)": {
          "meaning": "",
          "comments": []
        },
        "CT": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "Computer Aided Diagnosis": {
          "meaning": "",
          "comments": []
        },
        "Dye Chromoendoscopy": {
          "meaning": "",
          "comments": []
        },
        "Flexible Sigmoidoscopy": {
          "meaning": "ncit:C51588",
          "comments": []
        },
        "High Definition Equipment": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy (colonoscopy)": {
          "meaning": "ncit:C16450",
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
        "Rectal Retroflexion": {
          "meaning": "",
          "comments": []
        },
        "Right Colon Retroflexion": {
          "meaning": "",
          "comments": []
        },
        "Serum Antigen": {
          "meaning": "",
          "comments": []
        },
        "Stool Antigen": {
          "meaning": "",
          "comments": []
        },
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        },
        "Upper Endoscopy (Colonscope)": {
          "meaning": "ncit:C16604",
          "comments": []
        },
        "Upper Endoscopy (Gastroscope)": {
          "meaning": "ncit:C16604",
          "comments": []
        },
        "Urea Breath Test": {
          "meaning": "",
          "comments": []
        },
        "Video Capsule Endoscopy": {
          "meaning": "ncit:C16546",
          "comments": []
        },
        "Virtual Chromoendoscopy": {
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
        },
        "Lower Endoscopy, Attachment Device (Cap, Endocuff, etc.)": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Computer Aided Diagnosis": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Dye Chromoendoscopy": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Flexible Sigmoidoscopy": {
          "meaning": "ncit:C51588",
          "comments": []
        },
        "Upper Endoscopy, High Definition Equipment": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, High Defnition Equipment": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Rectal Retroflexion": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Right Colon Retroflexion": {
          "meaning": "",
          "comments": []
        },
        "Lower Endoscopy, Virtual Chromoendoscopy": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Appendiceal Orifice": {
          "meaning": "",
          "comments": []
        },
        "Ascending Colon": {
          "meaning": "ncit:C12265",
          "comments": []
        },
        "Cecum": {
          "meaning": "ncit:C12381",
          "comments": []
        },
        "Descending Colon": {
          "meaning": "ncit:C12268",
          "comments": []
        },
        "Hepatic Flexure": {
          "meaning": "ncit:C12266",
          "comments": []
        },
        "Ileocecal Valve": {
          "meaning": "ncit:C13066",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Sigmoid Colon": {
          "meaning": "ncit:C12384",
          "comments": []
        },
        "Sigmoid Flexure": {
          "meaning": "ncit:C33550",
          "comments": []
        },
        "Skin": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Splenic Flexure": {
          "meaning": "ncit:C12267",
          "comments": []
        },
        "Terminal Ileum": {
          "meaning": "ncit:C33757",
          "comments": []
        },
        "Transverse Colon": {
          "meaning": "ncit:C12385",
          "comments": []
        }
      }
    },
    "GenderIdentityEnum": {
      "permissible_values": {
        "Identifies As Female Gender": {
          "meaning": "SCTID:446141000124107",
          "comments": []
        },
        "Identifies As Male Gender": {
          "meaning": "SCTID:446151000124109",
          "comments": []
        },
        "Transgender, NOS": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "LS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MarkersEnum": {
      "permissible_values": {
        "Her2 FISH": {
          "meaning": "ncit:C38906",
          "comments": []
        },
        "Her2 Protein": {
          "meaning": "ncit:C38896",
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
    "EthnicitySpecifiedEnum": {
      "permissible_values": {
        "Not Specified": {
          "meaning": "",
          "comments": []
        },
        "Spanish/Spaniard": {
          "meaning": "",
          "comments": []
        },
        "Argentinean/Argentine": {
          "meaning": "",
          "comments": []
        },
        "Bolivian": {
          "meaning": "",
          "comments": []
        },
        "Central American Indian": {
          "meaning": "",
          "comments": []
        },
        "Chilean": {
          "meaning": "",
          "comments": []
        },
        "Colombian": {
          "meaning": "",
          "comments": []
        },
        "Costa Rican": {
          "meaning": "",
          "comments": []
        },
        "Cuban": {
          "meaning": "",
          "comments": []
        },
        "Ecuadorian": {
          "meaning": "",
          "comments": []
        },
        "Guatemalan": {
          "meaning": "",
          "comments": []
        },
        "Honduran": {
          "meaning": "",
          "comments": []
        },
        "Mexican": {
          "meaning": "",
          "comments": []
        },
        "Mexican American Indian": {
          "meaning": "",
          "comments": []
        },
        "Nicaraguan": {
          "meaning": "",
          "comments": []
        },
        "Panamanian": {
          "meaning": "",
          "comments": []
        },
        "Paraguayan": {
          "meaning": "",
          "comments": []
        },
        "Peruvian": {
          "meaning": "",
          "comments": []
        },
        "Puerto Rican": {
          "meaning": "",
          "comments": []
        },
        "Salvadoran": {
          "meaning": "",
          "comments": []
        },
        "South American Indian": {
          "meaning": "",
          "comments": []
        },
        "Uruguayan": {
          "meaning": "",
          "comments": []
        },
        "Venezuelan": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SexAtBirthEnum": {
      "permissible_values": {
        "Male": {
          "meaning": "",
          "comments": []
        },
        "Female": {
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
        "Adrenal Cortex": {
          "meaning": "",
          "comments": []
        },
        "Adrenal medulla": {
          "meaning": "",
          "comments": []
        },
        "Ampulla": {
          "meaning": "ncit:C93230",
          "comments": []
        },
        "Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Anus": {
          "meaning": "ncit:C43362",
          "comments": []
        },
        "Appendiceal Orifice": {
          "meaning": "",
          "comments": []
        },
        "Appendix": {
          "meaning": "ncit:C12380",
          "comments": []
        },
        "Ascending": {
          "meaning": "",
          "comments": []
        },
        "Bile duct": {
          "meaning": "",
          "comments": []
        },
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
        "Breast": {
          "meaning": "ncit:C12971",
          "comments": []
        },
        "Cecum": {
          "meaning": "",
          "comments": []
        },
        "Cerebellum": {
          "meaning": "ncit:C12445",
          "comments": []
        },
        "Cervix Uteri": {
          "meaning": "",
          "comments": []
        },
        "Colon": {
          "meaning": "ncit:C12382",
          "comments": []
        },
        "Descending": {
          "meaning": "",
          "comments": []
        },
        "Distal Cholangiocarcinoma": {
          "meaning": "ncit:C7976",
          "comments": []
        },
        "Distal Esophagus": {
          "meaning": "",
          "comments": []
        },
        "Duodenal Bulb (D1)": {
          "meaning": "",
          "comments": []
        },
        "Duodenum": {
          "meaning": "ncit:C12263",
          "comments": []
        },
        "Endometrium": {
          "meaning": "",
          "comments": []
        },
        "Esophagus, NOS": {
          "meaning": "",
          "comments": []
        },
        "Extrahepatic": {
          "meaning": "ncit:C28358",
          "comments": []
        },
        "Eye": {
          "meaning": "",
          "comments": []
        },
        "Fallopian Tube": {
          "meaning": "ncit:C12403",
          "comments": []
        },
        "Fourth Portion of Duodenum (D4)": {
          "meaning": "",
          "comments": []
        },
        "GE Junction": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder": {
          "meaning": "ncit:C12377",
          "comments": []
        },
        "Gastric Antrum": {
          "meaning": "",
          "comments": []
        },
        "Gastric Body": {
          "meaning": "",
          "comments": []
        },
        "Gastric Cardia": {
          "meaning": "",
          "comments": []
        },
        "Gastric Fundus": {
          "meaning": "",
          "comments": []
        },
        "Gastric, NOS": {
          "meaning": "",
          "comments": []
        },
        "Hepatic flexure": {
          "meaning": "",
          "comments": []
        },
        "Hilar Cholangiocarcinoma": {
          "meaning": "ncit:C36077",
          "comments": []
        },
        "Ileocecal Valve": {
          "meaning": "",
          "comments": []
        },
        "Ileum": {
          "meaning": "",
          "comments": []
        },
        "Intrahepatic Cholangiocarcinoma": {
          "meaning": "ncit:C35417",
          "comments": []
        },
        "Jejunum": {
          "meaning": "",
          "comments": []
        },
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Larynx": {
          "meaning": "ncit:C12420",
          "comments": []
        },
        "Ligament of Treitz": {
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
        "Mid Esophagus": {
          "meaning": "",
          "comments": []
        },
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        },
        "Oropharynx": {
          "meaning": "ncit:C12762",
          "comments": []
        },
        "Ovarian": {
          "meaning": "ncit:C28047",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Pancreas": {
          "meaning": "ncit:C12393",
          "comments": []
        },
        "Pancreas Body": {
          "meaning": "",
          "comments": []
        },
        "Pancreas Head": {
          "meaning": "",
          "comments": []
        },
        "Pancreas Tail": {
          "meaning": "",
          "comments": []
        },
        "Paraganglia": {
          "meaning": "",
          "comments": []
        },
        "Parathyroid": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Penis": {
          "meaning": "ncit:C12409",
          "comments": []
        },
        "Pituitary gland": {
          "meaning": "",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": [
            "(ews) ConsortiumNote: Included so that pleural effusions can be reported.",
            "(os) ConsortiumNote: Included so that pleural effusions can be reported."
          ]
        },
        "Pouch": {
          "meaning": "",
          "comments": []
        },
        "Primary Peritoneal": {
          "meaning": "ncit:C40022",
          "comments": []
        },
        "Prostate": {
          "meaning": "ncit:C12410",
          "comments": []
        },
        "Proximal Esophagus": {
          "meaning": "",
          "comments": []
        },
        "Rectosigmoid": {
          "meaning": "",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Retina": {
          "meaning": "",
          "comments": []
        },
        "Second Portion of Duodenum (D2)": {
          "meaning": "",
          "comments": []
        },
        "Sigmoid": {
          "meaning": "",
          "comments": []
        },
        "Skin": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Soft Tissue": {
          "meaning": "ncit:C12471",
          "comments": []
        },
        "Splenic flexure": {
          "meaning": "",
          "comments": []
        },
        "Stoma": {
          "meaning": "",
          "comments": []
        },
        "Stomach": {
          "meaning": "ncit:C12391",
          "comments": []
        },
        "Testis": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Third Portion of Duodenum (D3)": {
          "meaning": "",
          "comments": []
        },
        "Thyroid": {
          "meaning": "ncit:C12400",
          "comments": []
        },
        "Transverse": {
          "meaning": "",
          "comments": []
        },
        "Transverse Colon": {
          "meaning": "ncit:C12385",
          "comments": []
        },
        "Unknown Primary": {
          "meaning": "",
          "comments": []
        },
        "Ureter": {
          "meaning": "ncit:C12416",
          "comments": []
        },
        "Urethra": {
          "meaning": "",
          "comments": []
        },
        "Urinary bladder": {
          "meaning": "",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
          "comments": []
        },
        "Vulva": {
          "meaning": "ncit:C12408",
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
        },
        "M2": {
          "meaning": "ncit:C48704",
          "comments": []
        }
      }
    },
    "SedationTypeEnum": {
      "permissible_values": {
        "Moderate Sedation (Fentanyl, Midazolam, Diphenhydramine, Meperidine)": {
          "meaning": "",
          "comments": []
        },
        "Monitored Anesthesia Care (Propofol)": {
          "meaning": "",
          "comments": []
        },
        "No Sedation": {
          "meaning": "",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "TumorBuddingEnum": {
      "permissible_values": {
        "High Budding": {
          "meaning": "",
          "comments": []
        },
        "Intermediate Budding": {
          "meaning": "",
          "comments": []
        },
        "Low Budding": {
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
    "ChromosomalTranslocationPartnerEnum": {
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
    "GenomicSourceClassEnum": {
      "permissible_values": {
        "Germline": {
          "meaning": "ncit:C17666",
          "comments": []
        },
        "Somatic": {
          "meaning": "ncit:C18060",
          "comments": []
        },
        "Unknown Genomic Origin": {
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
    "LkssOfRelativeEnum": {
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
    "ReportedSignificanceEnum": {
      "permissible_values": {
        "Benign": {
          "meaning": "ncit:C168802",
          "comments": []
        },
        "Likely Benign": {
          "meaning": "ncit:C168801",
          "comments": []
        },
        "Likely Pathogenic": {
          "meaning": "ncit:C168800",
          "comments": []
        },
        "Pathogenic": {
          "meaning": "ncit:C168799",
          "comments": []
        },
        "Uncertain Significance": {
          "meaning": "ncit:C94187",
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
    "MedicationEnum": {
      "permissible_values": {
        "Alemtuzumab": {
          "meaning": "rxcui:117055",
          "comments": []
        },
        "Aleve": {
          "meaning": "rxcui:215101",
          "comments": []
        },
        "Anastrazole (Arimidex)": {
          "meaning": "rxcui:84857",
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
        "Camizestrant": {
          "meaning": "ncit:C160603",
          "comments": []
        },
        "Capecitabine": {
          "meaning": "rxcui:194000",
          "comments": []
        },
        "CapeOx": {
          "meaning": "ncit:C63597",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Celebrex": {
          "meaning": "rxcui:215927",
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
        "Cyclosporine": {
          "meaning": "rxcui:3008",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Dacarbazine": {
          "meaning": "rxcui:3098",
          "comments": []
        },
        "Deruxtecan": {
          "meaning": "rxcui:2657010",
          "comments": []
        },
        "Docetaxel": {
          "meaning": "rxcui:72962",
          "comments": []
        },
        "Doxil": {
          "meaning": "rxcui:80773",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
          "comments": []
        },
        "Elacestrant": {
          "meaning": "rxcui:2628483",
          "comments": []
        },
        "Epirubicin": {
          "meaning": "rxcui:3995",
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
        "Faslodex": {
          "meaning": "rxcui:203870",
          "comments": []
        },
        "Fluorouracil (5FU)": {
          "meaning": "rxcui:4492",
          "comments": []
        },
        "Futibatinib": {
          "meaning": "rxcui:2628190",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Ibuprofen": {
          "meaning": "rxcui:5640",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "rxcui:5657",
          "comments": []
        },
        "Immune Checkpoint Inhibitors": {
          "meaning": "ncit:C143250",
          "comments": []
        },
        "Infliximab": {
          "meaning": "",
          "comments": []
        },
        "Irinotecan": {
          "meaning": "ncit:C62040",
          "comments": []
        },
        "Ivosidenib": {
          "meaning": "rxcui:2049873",
          "comments": []
        },
        "Leflunomide": {
          "meaning": "rxcui:27169",
          "comments": []
        },
        "Lenvatinib": {
          "meaning": "rxcui:1603296",
          "comments": []
        },
        "Letrozole": {
          "meaning": "rxcui:72965",
          "comments": []
        },
        "Leucovorin": {
          "meaning": "rxcui:6313",
          "comments": []
        },
        "Leuprolide Acetate": {
          "meaning": "rxcui:203217",
          "comments": []
        },
        "Medroxyprogesterone": {
          "meaning": "rxcui:6691",
          "comments": []
        },
        "Metformin": {
          "meaning": "ncit:C61612",
          "comments": []
        },
        "Mizoribine": {
          "meaning": "ncit:C66172",
          "comments": []
        },
        "Mobic": {
          "meaning": "rxcui:152699",
          "comments": []
        },
        "Mycophenolate": {
          "meaning": "rxcui:265323",
          "comments": []
        },
        "Nab-Paclitaxel": {
          "meaning": "ncit:C2688",
          "comments": []
        },
        "Naproxen": {
          "meaning": "ncit:C680",
          "comments": []
        },
        "Niraparib": {
          "meaning": "rxcui:1918231",
          "comments": []
        },
        "Olaparib": {
          "meaning": "rxcui:1597582",
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
        "Pazopanib": {
          "meaning": "rxcui:714438",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
          "comments": []
        },
        "Pemigatinib": {
          "meaning": "rxcui:2359268",
          "comments": []
        },
        "Pertuzumab": {
          "meaning": "ncit:C38692",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Ramucirumab": {
          "meaning": "ncit:C70792",
          "comments": []
        },
        "Rapamune": {
          "meaning": "rxcui:258355",
          "comments": []
        },
        "Ribociclib": {
          "meaning": "rxcui:1873986",
          "comments": []
        },
        "Rucaparib": {
          "meaning": "rxcui:1862579",
          "comments": []
        },
        "Sirolimus": {
          "meaning": "rxcui:35302",
          "comments": []
        },
        "Tacrolimus": {
          "meaning": "ncit:C1311",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Talazoparib": {
          "meaning": "rxcui:2099949",
          "comments": []
        },
        "Tamoxifen": {
          "meaning": "rxcui:10324",
          "comments": []
        },
        "Topotecan": {
          "meaning": "rxcui:57308",
          "comments": []
        },
        "Trastuzumab": {
          "meaning": "rxcui:224905",
          "comments": []
        },
        "Trastuzumab Deruxtecan": {
          "meaning": "ncit:C128799",
          "comments": []
        },
        "Vinorelbine": {
          "meaning": "rxcui:39541",
          "comments": []
        },
        "Voltaren": {
          "meaning": "rxcui:202976",
          "comments": []
        },
        "Ziv-Aflibercept": {
          "meaning": "rxcui:1946825",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "LINEAGE": {
          "meaning": "ncit:C192767",
          "comments": []
        }
      }
    },
    "SiteClassificationEnum": {
      "permissible_values": {
        "Benign": {
          "meaning": "ncit:C14172",
          "comments": []
        },
        "Local Extension": {
          "meaning": "",
          "comments": []
        },
        "Metastatic": {
          "meaning": "ncit:C3261",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "",
          "comments": []
        },
        "Premalignant": {
          "meaning": "ncit:C25624",
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
        "ALC": {
          "meaning": "ncit:C113237",
          "comments": []
        },
        "ALP": {
          "meaning": "ncit:C64432",
          "comments": []
        },
        "ALT": {
          "meaning": "ncit:C64433",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "AST": {
          "meaning": "ncit:C64467",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "Albumin": {
          "meaning": "ncit:C64431",
          "comments": []
        },
        "Calcium": {
          "meaning": "ncit:C64488",
          "comments": []
        },
        "Chloride": {
          "meaning": "ncit:C64495",
          "comments": []
        },
        "Creatinine": {
          "meaning": "ncit:C64547",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "Creatinine Clearance": {
          "meaning": "ncit:C25747",
          "comments": []
        },
        "Direct Bilirubin": {
          "meaning": "ncit:C64481",
          "comments": []
        },
        "Estrogen Receptor Test": {
          "meaning": "",
          "comments": []
        },
        "Glucose": {
          "meaning": "ncit:C105585",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "HCT": {
          "meaning": "ncit:C64796",
          "comments": []
        },
        "Hemoglobin": {
          "meaning": "ncit:C64848",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Hemoglobin A1c Measurement": {
          "meaning": "ncit:C64849",
          "comments": []
        },
        "Microsatellite Instability Test": {
          "meaning": "",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Potassium": {
          "meaning": "ncit:C64853",
          "comments": []
        },
        "Progesterone Receptor Test": {
          "meaning": "ncit:C74791",
          "comments": []
        },
        "Protein Total": {
          "meaning": "ncit:C64858",
          "comments": []
        },
        "RBC": {
          "meaning": "ncit:C51946",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Sodium": {
          "meaning": "ncit:C64809",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "Total Bilirubin": {
          "meaning": "ncit:C38037",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "Urine Cytology": {
          "meaning": "ncit:C94473",
          "comments": []
        },
        "WBC": {
          "meaning": "ncit:C51948",
          "comments": []
        }
      }
    },
    "LocoregionalTherapyTechniqueEnum": {
      "permissible_values": {
        "Chemoembolization (TACE)": {
          "meaning": "ncit:C101513",
          "comments": []
        },
        "Radioembolization": {
          "meaning": "ncit:C116649",
          "comments": []
        }
      }
    },
    "RaceSpecifiedEnum": {
      "permissible_values": {
        "Asian Indian": {
          "meaning": "",
          "comments": []
        },
        "Bangladeshi": {
          "meaning": "",
          "comments": []
        },
        "Baram/Burman": {
          "meaning": "",
          "comments": []
        },
        "Bengali": {
          "meaning": "",
          "comments": []
        },
        "Bhutanese": {
          "meaning": "",
          "comments": []
        },
        "Burmese": {
          "meaning": "",
          "comments": []
        },
        "Cambodian": {
          "meaning": "",
          "comments": []
        },
        "Chinese": {
          "meaning": "",
          "comments": []
        },
        "Filipino": {
          "meaning": "",
          "comments": []
        },
        "Hmong": {
          "meaning": "",
          "comments": []
        },
        "Hongkonger": {
          "meaning": "",
          "comments": []
        },
        "Indonesian": {
          "meaning": "",
          "comments": []
        },
        "Japanese": {
          "meaning": "",
          "comments": []
        },
        "Kazakh/Qazaq": {
          "meaning": "",
          "comments": []
        },
        "Kazakhstani": {
          "meaning": "",
          "comments": []
        },
        "Korean": {
          "meaning": "",
          "comments": []
        },
        "Laotian/Lao": {
          "meaning": "",
          "comments": []
        },
        "Malay": {
          "meaning": "",
          "comments": []
        },
        "Malaysian": {
          "meaning": "",
          "comments": []
        },
        "Nepalese/Nepali": {
          "meaning": "",
          "comments": []
        },
        "Okinawan": {
          "meaning": "",
          "comments": []
        },
        "Pakistani": {
          "meaning": "",
          "comments": []
        },
        "Singaporean": {
          "meaning": "",
          "comments": []
        },
        "Sri Lankan": {
          "meaning": "",
          "comments": []
        },
        "Tagalog": {
          "meaning": "",
          "comments": []
        },
        "Taiwanese": {
          "meaning": "",
          "comments": []
        },
        "Thai": {
          "meaning": "",
          "comments": []
        },
        "Vietnamese": {
          "meaning": "",
          "comments": []
        },
        "Agikuyu/Kikuyu": {
          "meaning": "",
          "comments": []
        },
        "Akan": {
          "meaning": "",
          "comments": []
        },
        "Amara/Amhara": {
          "meaning": "",
          "comments": []
        },
        "Australian": {
          "meaning": "",
          "comments": []
        },
        "Bahamian": {
          "meaning": "",
          "comments": []
        },
        "Bantu": {
          "meaning": "",
          "comments": []
        },
        "Barbadian/Bajan": {
          "meaning": "",
          "comments": []
        },
        "Cameroonian": {
          "meaning": "",
          "comments": []
        },
        "Congolese": {
          "meaning": "",
          "comments": []
        },
        "Eritrean": {
          "meaning": "",
          "comments": []
        },
        "Ethiopian": {
          "meaning": "",
          "comments": []
        },
        "Fijian": {
          "meaning": "",
          "comments": []
        },
        "Grenadian": {
          "meaning": "",
          "comments": []
        },
        "Guamanian or Chamorro": {
          "meaning": "",
          "comments": []
        },
        "Haitian": {
          "meaning": "",
          "comments": []
        },
        "Ivoirian/Cote d'Ivoire": {
          "meaning": "",
          "comments": []
        },
        "Jamaican": {
          "meaning": "",
          "comments": []
        },
        "Kenyan": {
          "meaning": "",
          "comments": []
        },
        "Liberian": {
          "meaning": "",
          "comments": []
        },
        "Libyan": {
          "meaning": "",
          "comments": []
        },
        "Mende": {
          "meaning": "",
          "comments": []
        },
        "Native Hawaiian/Hawaiian": {
          "meaning": "",
          "comments": []
        },
        "Nevis Islander/ Kittitian/Nevisian": {
          "meaning": "",
          "comments": []
        },
        "New Zealander": {
          "meaning": "",
          "comments": []
        },
        "Nigerian": {
          "meaning": "",
          "comments": []
        },
        "Oromo": {
          "meaning": "",
          "comments": []
        },
        "Polynesian": {
          "meaning": "",
          "comments": []
        },
        "Samoan": {
          "meaning": "",
          "comments": []
        },
        "Shona": {
          "meaning": "",
          "comments": []
        },
        "St Lucia Islander/ Saint Lucian": {
          "meaning": "",
          "comments": []
        },
        "Tahitian": {
          "meaning": "",
          "comments": []
        },
        "Tanzanian": {
          "meaning": "",
          "comments": []
        },
        "Temne/Temme/Themne": {
          "meaning": "",
          "comments": []
        },
        "Tigrinya/Tigray/Tigraway": {
          "meaning": "",
          "comments": []
        },
        "Togolese": {
          "meaning": "",
          "comments": []
        },
        "Tongan": {
          "meaning": "",
          "comments": []
        },
        "U.S. Virgin Islander": {
          "meaning": "",
          "comments": []
        },
        "Ugandan": {
          "meaning": "",
          "comments": []
        },
        "Part Hawaiian": {
          "meaning": "",
          "comments": []
        },
        "Acadian/Cajun": {
          "meaning": "",
          "comments": []
        },
        "Afghanistani/Afghan/ Afghani": {
          "meaning": "",
          "comments": []
        },
        "Albanian": {
          "meaning": "",
          "comments": []
        },
        "Algerian": {
          "meaning": "",
          "comments": []
        },
        "Alsatian": {
          "meaning": "",
          "comments": []
        },
        "Arab/Arabic": {
          "meaning": "",
          "comments": []
        },
        "Armenian": {
          "meaning": "",
          "comments": []
        },
        "Assyrian": {
          "meaning": "",
          "comments": []
        },
        "Austrian": {
          "meaning": "",
          "comments": []
        },
        "Azerbaijani": {
          "meaning": "",
          "comments": []
        },
        "Azeri": {
          "meaning": "",
          "comments": []
        },
        "Belgian": {
          "meaning": "",
          "comments": []
        },
        "Belorussian/Belarusian": {
          "meaning": "",
          "comments": []
        },
        "Berber/Amazigh/ Imazighen": {
          "meaning": "",
          "comments": []
        },
        "Bosniak": {
          "meaning": "",
          "comments": []
        },
        "British Isles/ British Isles origin": {
          "meaning": "",
          "comments": []
        },
        "British/Briton": {
          "meaning": "",
          "comments": []
        },
        "Bulgarian": {
          "meaning": "",
          "comments": []
        },
        "Canadian": {
          "meaning": "",
          "comments": []
        },
        "Celtic": {
          "meaning": "",
          "comments": []
        },
        "Chaldean": {
          "meaning": "",
          "comments": []
        },
        "Croatian/Croat": {
          "meaning": "",
          "comments": []
        },
        "Cypriot": {
          "meaning": "",
          "comments": []
        },
        "Czech": {
          "meaning": "",
          "comments": []
        },
        "Czechoslovakian": {
          "meaning": "",
          "comments": []
        },
        "Danish/Dane": {
          "meaning": "",
          "comments": []
        },
        "Dutch": {
          "meaning": "",
          "comments": []
        },
        "Dutch West Indian": {
          "meaning": "",
          "comments": []
        },
        "Egyptian": {
          "meaning": "",
          "comments": []
        },
        "English": {
          "meaning": "",
          "comments": []
        },
        "Estonian": {
          "meaning": "",
          "comments": []
        },
        "Finnish/Finn": {
          "meaning": "",
          "comments": []
        },
        "Flemish/Fleming": {
          "meaning": "",
          "comments": []
        },
        "French": {
          "meaning": "",
          "comments": []
        },
        "French Canadian": {
          "meaning": "",
          "comments": []
        },
        "Georgian": {
          "meaning": "",
          "comments": []
        },
        "German": {
          "meaning": "",
          "comments": []
        },
        "Greek": {
          "meaning": "",
          "comments": []
        },
        "Herzegovinian": {
          "meaning": "",
          "comments": []
        },
        "Hungarian": {
          "meaning": "",
          "comments": []
        },
        "Icelander": {
          "meaning": "",
          "comments": []
        },
        "Iranian": {
          "meaning": "",
          "comments": []
        },
        "Iraqi": {
          "meaning": "",
          "comments": []
        },
        "Irish": {
          "meaning": "",
          "comments": []
        },
        "Israeli": {
          "meaning": "",
          "comments": []
        },
        "Italian": {
          "meaning": "",
          "comments": []
        },
        "Jordanian": {
          "meaning": "",
          "comments": []
        },
        "Karelian": {
          "meaning": "",
          "comments": []
        },
        "Kurdish/Kurd": {
          "meaning": "",
          "comments": []
        },
        "Kuwaiti": {
          "meaning": "",
          "comments": []
        },
        "Latvian": {
          "meaning": "",
          "comments": []
        },
        "Lebanese": {
          "meaning": "",
          "comments": []
        },
        "Lithuanian": {
          "meaning": "",
          "comments": []
        },
        "Luxemburger": {
          "meaning": "",
          "comments": []
        },
        "Macedonian": {
          "meaning": "",
          "comments": []
        },
        "Maltese": {
          "meaning": "",
          "comments": []
        },
        "Norwegian": {
          "meaning": "",
          "comments": []
        },
        "Palestinian": {
          "meaning": "",
          "comments": []
        },
        "Pennsylvania German": {
          "meaning": "",
          "comments": []
        },
        "Persian": {
          "meaning": "",
          "comments": []
        },
        "Polish/Pole": {
          "meaning": "",
          "comments": []
        },
        "Portuguese": {
          "meaning": "",
          "comments": []
        },
        "Romanian": {
          "meaning": "",
          "comments": []
        },
        "Russian": {
          "meaning": "",
          "comments": []
        },
        "Saudi/Saudi Arabian": {
          "meaning": "",
          "comments": []
        },
        "Scandinavian": {
          "meaning": "",
          "comments": []
        },
        "Scotch Irish": {
          "meaning": "",
          "comments": []
        },
        "Scottish": {
          "meaning": "",
          "comments": []
        },
        "Serbian": {
          "meaning": "",
          "comments": []
        },
        "Slavic": {
          "meaning": "",
          "comments": []
        },
        "Slovak": {
          "meaning": "",
          "comments": []
        },
        "Slovene": {
          "meaning": "",
          "comments": []
        },
        "Soviet": {
          "meaning": "",
          "comments": []
        },
        "Swedish/Swede": {
          "meaning": "",
          "comments": []
        },
        "Swiss": {
          "meaning": "",
          "comments": []
        },
        "Syriac": {
          "meaning": "",
          "comments": []
        },
        "Syrian": {
          "meaning": "",
          "comments": []
        },
        "Turkish/Turk": {
          "meaning": "",
          "comments": []
        },
        "Ukrainian": {
          "meaning": "",
          "comments": []
        },
        "United Arab Emirates/ Emirati": {
          "meaning": "",
          "comments": []
        },
        "Uzbeg/Uzbek": {
          "meaning": "",
          "comments": []
        },
        "Uzbekistani": {
          "meaning": "",
          "comments": []
        },
        "Welsh": {
          "meaning": "",
          "comments": []
        },
        "Yemeni": {
          "meaning": "",
          "comments": []
        },
        "Yugoslavian": {
          "meaning": "",
          "comments": []
        },
        "Native American": {
          "meaning": "",
          "comments": []
        },
        "Alaska Native": {
          "meaning": "",
          "comments": []
        },
        "First Nation": {
          "meaning": "",
          "comments": []
        },
        "Inuit": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        },
        "Not Specified": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "PerformanceScoreEnum": {
      "permissible_values": {
        "ASA >> 1": {
          "meaning": "ncit:C174992",
          "comments": []
        },
        "ASA >> 2": {
          "meaning": "",
          "comments": []
        },
        "ASA >> 3": {
          "meaning": "",
          "comments": []
        },
        "ASA >> 4": {
          "meaning": "",
          "comments": []
        },
        "ASA >> 5": {
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
        "Curative Intent, No Surgery Planned": {
          "meaning": "",
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
        "Radiation Therapy": {
          "meaning": "ncit:C15313",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
        },
        "Other": {
          "meaning": "ncit:C17649",
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
    "ProbandGenerationEnum": {
      "permissible_values": {
        "Children's Generation (including nieces and nephews)": {
          "meaning": "",
          "comments": []
        },
        "Grandchildren's Generation": {
          "meaning": "",
          "comments": []
        },
        "Grandparents' Generation (including great aunts and uncles)": {
          "meaning": "",
          "comments": []
        },
        "Great Grandparents' Generation": {
          "meaning": "",
          "comments": []
        },
        "Parents' Generation (including aunts and uncles)": {
          "meaning": "",
          "comments": []
        },
        "Same Generation (including siblings and cousins)": {
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
    "AlterationRegionEnum": {
      "permissible_values": {
        "Intronic": {
          "meaning": "ncit:C45387",
          "comments": []
        }
      }
    },
    "RelationLineageEnum": {
      "permissible_values": {
        "Maternal": {
          "meaning": "",
          "comments": []
        },
        "Paternal": {
          "meaning": "",
          "comments": []
        },
        "Unspecified": {
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
        "NX": {
          "meaning": "ncit:C48718",
          "comments": []
        }
      }
    },
    "RemainingColonEnum": {
      "permissible_values": {
        "Ascending Colon": {
          "meaning": "ncit:C12265",
          "comments": []
        },
        "Cecum": {
          "meaning": "ncit:C12381",
          "comments": []
        },
        "Descending Colon": {
          "meaning": "ncit:C12268",
          "comments": []
        },
        "Hepatic Flexure": {
          "meaning": "ncit:C12266",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Sigmoid Colon": {
          "meaning": "ncit:C33550",
          "comments": []
        },
        "Sigmoid Flexure": {
          "meaning": "ncit:C12384",
          "comments": []
        },
        "Splenic Flexure": {
          "meaning": "ncit:C12267",
          "comments": []
        },
        "Transverse Colon": {
          "meaning": "ncit:C12385",
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
    "StageEnum": {
      "permissible_values": {
        "Group 1": {
          "meaning": "ncit:C137992",
          "comments": []
        },
        "Group 2": {
          "meaning": "ncit:C137993",
          "comments": []
        },
        "Group 3": {
          "meaning": "ncit:C137994",
          "comments": []
        },
        "Group 4": {
          "meaning": "ncit:C137995",
          "comments": []
        },
        "Group 5": {
          "meaning": "ncit:C137996",
          "comments": []
        },
        "Stage IIa": {
          "meaning": "",
          "comments": []
        },
        "Stage IIb": {
          "meaning": "",
          "comments": []
        },
        "Stage IIc": {
          "meaning": "",
          "comments": []
        },
        "Stage IIIa": {
          "meaning": "",
          "comments": []
        },
        "Stage IIIb": {
          "meaning": "",
          "comments": []
        },
        "Stage IIIc": {
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
    "RelationEnum": {
      "permissible_values": {
        "Father": {
          "meaning": "ncit:C96572",
          "comments": []
        },
        "Mother": {
          "meaning": "ncit:C96580",
          "comments": []
        },
        "Sibling": {
          "meaning": "ncit:C96586",
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
        "Half-Sibling": {
          "meaning": "",
          "comments": []
        },
        "Child": {
          "meaning": "",
          "comments": []
        },
        "Grandmother": {
          "meaning": "",
          "comments": []
        },
        "Grandfather": {
          "meaning": "",
          "comments": []
        },
        "Niece or Nephew": {
          "meaning": "",
          "comments": []
        },
        "Great Grandfather": {
          "meaning": "",
          "comments": []
        },
        "Great Grandmother": {
          "meaning": "",
          "comments": []
        },
        "Great Uncle": {
          "meaning": "",
          "comments": []
        },
        "Great Aunt": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ExternalRefIdSystemEnum": {
      "permissible_values": {
        "ClinVar": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "BarrettsEsophagusEnum": {
      "permissible_values": {
        "High Grade Dysplasia": {
          "meaning": "ncit:C156083",
          "comments": []
        },
        "Indeterminate for Dysplasia": {
          "meaning": "",
          "comments": []
        },
        "Low Grade Dysplasia": {
          "meaning": "ncit:C156084",
          "comments": []
        },
        "No Dysplasia": {
          "meaning": "",
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
    "ColonPolypMaxSizeEnum": {
      "permissible_values": {
        "1-5 mm": {
          "meaning": "",
          "comments": []
        },
        "20+ mm": {
          "meaning": "",
          "comments": []
        },
        "6-9 mm": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ExposureEnum": {
      "permissible_values": {
        "Alcohol": {
          "meaning": "ncit:C168296",
          "comments": []
        },
        "Drug Use": {
          "meaning": "",
          "comments": []
        },
        "E-Cigarettes": {
          "meaning": "",
          "comments": []
        },
        "Second-Hand Smoke": {
          "meaning": "",
          "comments": []
        },
        "Tobacco": {
          "meaning": "ncit:C18059",
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
        "Predisposed Disease Surveillance": {
          "meaning": "",
          "comments": []
        },
        "Refractory/Progression": {
          "meaning": "ncit:C174991",
          "comments": []
        },
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        },
        "Relapse/Refractory": {
          "meaning": "ncit:C203382",
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
    "ProcedureEnum": {
      "permissible_values": {
        "Abdominoperineal Resection": {
          "meaning": "ncit:C91826",
          "comments": []
        },
        "Appendectomy": {
          "meaning": "ncit:C51687",
          "comments": []
        },
        "Bilateral Salpingo-Oophorectomy": {
          "meaning": "ncit:C51765",
          "comments": []
        },
        "Bile Duct": {
          "meaning": "ncit:C12376",
          "comments": []
        },
        "Biopsy, NOS": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Cecectomy": {
          "meaning": "",
          "comments": []
        },
        "Cholangiocarcinoma": {
          "meaning": "ncit:C4436",
          "comments": []
        },
        "Cold Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Cold Snare": {
          "meaning": "",
          "comments": []
        },
        "Colectomy": {
          "meaning": "ncit:C15209",
          "comments": []
        },
        "Cystectomy": {
          "meaning": "ncit:C15217",
          "comments": []
        },
        "Cystoprostatectomy": {
          "meaning": "ncit:C94464",
          "comments": []
        },
        "Distal Pancreatoduodenectomy (Distal Pancreatectomy)": {
          "meaning": "",
          "comments": []
        },
        "Endoscopic Mucosal Resection": {
          "meaning": "ncit:C103242",
          "comments": []
        },
        "Endoscopic Submucosal Dissection": {
          "meaning": "ncit:C157837",
          "comments": []
        },
        "Esophagectomy": {
          "meaning": "ncit:C15357",
          "comments": []
        },
        "Gallbladder Surgery": {
          "meaning": "ncit:C157797",
          "comments": []
        },
        "Gastrectomy": {
          "meaning": "ncit:C15236",
          "comments": []
        },
        "Hemicolectomy": {
          "meaning": "ncit:C86074",
          "comments": []
        },
        "Hot Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Hot Snare": {
          "meaning": "",
          "comments": []
        },
        "Hysterectomy": {
          "meaning": "ncit:C15256",
          "comments": []
        },
        "Ileocolonic Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Ileorectal Anastamosis": {
          "meaning": "",
          "comments": []
        },
        "Ileosigmoid Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Low Anterior Resection": {
          "meaning": "ncit:C113716",
          "comments": []
        },
        "Lumpectomy": {
          "meaning": "ncit:C15755",
          "comments": []
        },
        "Mastectomy": {
          "meaning": "ncit:C15277",
          "comments": []
        },
        "Nephrectomy": {
          "meaning": "ncit:C15284",
          "comments": []
        },
        "Nephroureterectomy/Ureterectomy": {
          "meaning": "ncit:C51646",
          "comments": []
        },
        "Oophorectomy, NOS": {
          "meaning": "ncit:C15291",
          "comments": []
        },
        "Partial Gastrectomy": {
          "meaning": "",
          "comments": []
        },
        "Prostatectomy": {
          "meaning": "ncit:C15307",
          "comments": []
        },
        "Random Gastric Biopsy": {
          "meaning": "",
          "comments": []
        },
        "Roux-En-Y": {
          "meaning": "ncit:C51758",
          "comments": []
        },
        "Salpingectomy": {
          "meaning": "ncit:C51605",
          "comments": []
        },
        "Sigmoid Colectomy": {
          "meaning": "ncit:C91838",
          "comments": []
        },
        "Sleeve Gastrectomy": {
          "meaning": "ncit:C167213",
          "comments": []
        },
        "Small Bowel Resection": {
          "meaning": "ncit:C51510",
          "comments": []
        },
        "Total Abdominal Hysterectomy": {
          "meaning": "ncit:C51695",
          "comments": []
        },
        "Total Abdominal Hysterectomy With A Bilateral Salpingo-Oophorectomy": {
          "meaning": "ncit:C51761",
          "comments": []
        },
        "Total Colectomy with End Ileostomy": {
          "meaning": "",
          "comments": []
        },
        "Total Colectomy with Ileorectal Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Total Colectomy with Ileosigmoid Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Total Gastrectomy": {
          "meaning": "ncit:C185240",
          "comments": []
        },
        "Total Pancreatectomy": {
          "meaning": "ncit:C51933",
          "comments": []
        },
        "Total Proctocolectomy with End Ileostomy": {
          "meaning": "",
          "comments": []
        },
        "Total Proctocolectomy with Ileal Pouch": {
          "meaning": "",
          "comments": []
        },
        "Transverse Hemicolectomy": {
          "meaning": "",
          "comments": []
        },
        "Whipple Pancreaticoduodenectomy": {
          "meaning": "ncit:C15356",
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
        "IU/mL": {
          "meaning": "ncit:C67378",
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
        "cp/mL": {
          "meaning": "",
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
        "mg/dL": {
          "meaning": "ncit:C67015",
          "comments": []
        },
        "mm/h": {
          "meaning": "ncit:C67419",
          "comments": []
        },
        "mmHg": {
          "meaning": "ncit:C49670",
          "comments": []
        },
        "mmol/L": {
          "meaning": "ncit:C64387",
          "comments": []
        },
        "ng/mL": {
          "meaning": "ncit:C67306",
          "comments": []
        },
        "uIU/mL": {
          "meaning": "ncit:C67405",
          "comments": []
        }
      }
    },
    "BowelPreparationEnum": {
      "permissible_values": {
        "Adequate": {
          "meaning": "",
          "comments": []
        },
        "Excellent": {
          "meaning": "ncit:C82488",
          "comments": []
        },
        "Fair": {
          "meaning": "ncit:C82489",
          "comments": []
        },
        "Good": {
          "meaning": "ncit:C64975",
          "comments": []
        },
        "Inadequate": {
          "meaning": "",
          "comments": []
        },
        "Not Documented": {
          "meaning": "",
          "comments": []
        },
        "Poor": {
          "meaning": "ncit:C77959",
          "comments": []
        }
      }
    }
  }
}
```

</div>