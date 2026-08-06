---
layout: default
title: Fanconi Anemia
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*FA View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- [Central Nervous System Tumors](cns)
- [Ewing Sarcoma](ews)
- **Fanconi Anemia**
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

The FA view of the PCDC data model represents consensus data modeling by an international group of Fanconi Anemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Fanconi Research Initiative for Education, Networking, and Data Sharing Consortium (FRIENDS). It is based on the collective requirements of its contributors.


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
| `age_at_end` | `integer` |  |

## FamilyMedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `family_medical_history_condition` | `string` |  |
| `relation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-relationenum')">RelationEnum</button> |  |
| `lkss_of_relative` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssofrelativeenum')">LkssOfRelativeEnum</button> |  |
| `age_at_lkss_of_relative` | `integer` |  |
| `relative_sct_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `number_of_pregnancies` | `integer` |  |
| `number_of_live_births` | `integer` |  |
| `number_of_abortions` | `integer` |  |

## SocialAndBehavioralDeterminantsOfHealth

| Slot | Range | Description |
|---|---|---|
| `age_at_status` | `integer` |  |
| `gender_identity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genderidentityenum')">GenderIdentityEnum</button> |  |
| `exposure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposureenum')">ExposureEnum</button> |  |
| `exposure_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposurestatusenum')">ExposureStatusEnum</button> |  |
| `sunscreen_use` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `occupation` | `string` |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |
| `urls` | `string` |  |

## Subject

| Slot | Range | Description |
|---|---|---|
| `consortium` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-consortiumenum')">ConsortiumEnum</button> |  |
| `disease_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasegroupenum')">DiseaseGroupEnum</button> |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |
| `race` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button> |  |
| `ethnicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button> |  |
| `country` | `string` |  |

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `age_at_last_follow_up` | `integer` |  |
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
| `lkss_with_disease` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |
| `cause_of_death_other` | `string` |  |
| `trm_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-trmtypeenum')">TrmTypeEnum</button> |  |
| `trm_type_other` | `string` |  |
| `cause_of_death_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathdetailenum')">CauseOfDeathDetailEnum</button> |  |
| `cause_of_death_detail_other` | `string` |  |
| `cause_of_death_ranking` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathrankingenum')">CauseOfDeathRankingEnum</button> |  |

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
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `vacterlh` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-vacterlhenum')">VacterlhEnum</button> |  |
| `phenos` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-phenosenum')">PhenosEnum</button> |  |
| `vacterlh_phenos_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `clinical_finding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-clinicalfindingenum')">ClinicalFindingEnum</button> |  |
| `clinical_finding_other` | `string` |  |
| `modified_rankin_scale` | `integer` |  |
| `fans_symptom_acuity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fanssymptomacuityenum')">FansSymptomAcuityEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `assessment_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-assessmentreasonenum')">AssessmentReasonEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `nodes_assessed_number` | `integer` |  |
| `tumor_number` | `decimal` |  |
| `dysplasia` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-dysplasiaenum')">DysplasiaEnum</button> |  |
| `hpv_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hpvstatusenum')">HpvStatusEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `stage_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagecategoryenum')">StageCategoryEnum</button> |  |
| `tnm_tumor_t` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmtumortenum')">TnmTumorTEnum</button> |  |
| `tnm_node_n` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmnodenenum')">TnmNodeNEnum</button> |  |
| `tnm_metastasis_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmmetastasismenum')">TnmMetastasisMEnum</button> |  |
| `stage_system_version` | `string` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `year_at_medication_start` | `integer` |  |
| `route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `medication_other` | `string` |  |
| `number_doses` | `decimal` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |
| `frequency` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-frequencyenum')">FrequencyEnum</button> |  |
| `frequency_other` | `string` |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `year_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `year_at_sct` | `integer` |  |
| `sct_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-scttypeenum')">SctTypeEnum</button> |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `donor_relationship` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-donorrelationshipenum')">DonorRelationshipEnum</button> |  |
| `hla_match` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hlamatchenum')">HlaMatchEnum</button> |  |
| `conditioning_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conditioningtypeenum')">ConditioningTypeEnum</button> |  |
| `cd34_collected` | `decimal` |  |
| `cd34_transplant` | `decimal` |  |
| `chimerism` | `decimal` |  |
| `chimerism_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chimerismunitenum')">ChimerismUnitEnum</button> |  |
| `stem_cell_processing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellprocessingenum')">StemCellProcessingEnum</button> |  |
| `stem_cell_processing_other` | `string` |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_other` | `string` |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |
| `outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-outcomeenum')">OutcomeEnum</button> |  |

## TransfusionMedicineProcedure

| Slot | Range | Description |
|---|---|---|
| `age_at_tmp_start` | `integer` |  |
| `tmp_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmptypeenum')">TmpTypeEnum</button> |  |
| `tmp_product` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmpproductenum')">TmpProductEnum</button> |  |
| `number_units` | `decimal` |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `ae_treatment` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aetreatmentenum')">AeTreatmentEnum</button> |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_code` | `string` |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `gvhd_acuity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gvhdacuityenum')">GvhdAcuityEnum</button> |  |
| `gvhd_organ` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gvhdorganenum')">GvhdOrganEnum</button> |  |
| `grade_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gradesystemenum')">GradeSystemEnum</button> |  |
| `grade_system_version` | `string` |  |
| `ae_attribution` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeattributionenum')">AeAttributionEnum</button> |  |

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

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `year_at_genetic_analysis` | `integer` |  |
| `determination_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-determinationsourceenum')">DeterminationSourceEnum</button> |  |
| `source_lab` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sourcelabenum')">SourceLabEnum</button> |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `genomic_source_class` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genomicsourceclassenum')">GenomicSourceClassEnum</button> |  |
| `mosaicism` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `gene` | `string` |  |
| `hgvs_genomic` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein` | `string` |  |
| `reference_genome` | `string` |  |
| `reference_genome_accession` | `string` |  |
| `parental_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-parentalstatusenum')">ParentalStatusEnum</button> |  |
| `reported_significance` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reportedsignificanceenum')">ReportedSignificanceEnum</button> |  |
| `external_ref_id_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-externalrefidsystemenum')">ExternalRefIdSystemEnum</button> |  |
| `external_ref_id` | `string` |  |
| `copy_number` | `decimal` |  |
| `allelic_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button> |  |
| `founder_population` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-founderpopulationenum')">FounderPopulationEnum</button> |  |
| `acmg_based_significance` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestmethodenum')">LaboratoryTestMethodEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `laboratory_test_specimen_other` | `string` |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |
| `breakage_source_lab` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-breakagesourcelabenum')">BreakageSourceLabEnum</button> |  |

## VitalsAndAnthropometrics

| Slot | Range | Description |
|---|---|---|
| `age_at_measurement` | `integer` |  |
| `anthropometric_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementtypeenum')">AnthropometricMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `anthropometric_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">AnthropometricMeasurementResultUnitEnum</button> |  |
| `gestational_age_at_birth` | `integer` |  |

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
<tr><td><code>Allergic Reaction</code></td><td><code>ncit:C114476</code></td><td></td></tr>
<tr><td><code>Anemia</code></td><td><code>ncit:C2869</code></td><td></td></tr>
<tr><td><code>Aortic Valve Disease</code></td><td><code>ncit:C143290</code></td><td></td></tr>
<tr><td><code>Asystole</code></td><td><code>ncit:C146731</code></td><td></td></tr>
<tr><td><code>Atrial Fibrillation</code></td><td><code>ncit:C54767</code></td><td></td></tr>
<tr><td><code>Atrial Flutter</code></td><td><code>ncit:C54768</code></td><td></td></tr>
<tr><td><code>Atrioventricular Block Complete</code></td><td><code>ncit:C143308</code></td><td></td></tr>
<tr><td><code>Atrioventricular Block First Degree</code></td><td><code>ncit:C143309</code></td><td></td></tr>
<tr><td><code>Blood and Lymphatic System Disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow Hypocellular</code></td><td><code>ncit:C3516</code></td><td></td></tr>
<tr><td><code>Cardiac Arrest</code></td><td><code>ncit:c143351</code></td><td></td></tr>
<tr><td><code>Cardiac Disorders - Other, Specify</code></td><td><code>ncit:c143352</code></td><td></td></tr>
<tr><td><code>Chest Pain - Cardiac</code></td><td><code>ncit:c143364</code></td><td></td></tr>
<tr><td><code>Conduction Disorder</code></td><td><code>ncit:c143380</code></td><td></td></tr>
<tr><td><code>Cataract</code></td><td><code>ncit:C26713</code></td><td></td></tr>
<tr><td><code>Heart Failure</code></td><td><code>ncit:c143529</code></td><td></td></tr>
<tr><td><code>Mitral Valve Disease</code></td><td><code>ncit:c143674</code></td><td></td></tr>
<tr><td><code>Mobitz (Type) Ii Atrioventricular Block</code></td><td><code>ncit:c54772</code></td><td></td></tr>
<tr><td><code>Mobitz Type I</code></td><td><code>ncit:c54771</code></td><td></td></tr>
<tr><td><code>Myocardial Infarction</code></td><td><code>ncit:c143691</code></td><td></td></tr>
<tr><td><code>Myocarditis</code></td><td><code>ncit:c146695</code></td><td></td></tr>
<tr><td><code>Palpitations</code></td><td><code>ncit:c54935</code></td><td></td></tr>
<tr><td><code>Paroxysmal Atrial Tachycardia</code></td><td><code>ncit:c143738</code></td><td></td></tr>
<tr><td><code>Pericardial Effusion</code></td><td><code>ncit:c143743</code></td><td></td></tr>
<tr><td><code>Pericardial Tamponade</code></td><td><code>ncit:c143744</code></td><td></td></tr>
<tr><td><code>Pericarditis</code></td><td><code>ncit:c55067</code></td><td></td></tr>
<tr><td><code>Pulmonary Valve Disease</code></td><td><code>ncit:c143793</code></td><td></td></tr>
<tr><td><code>Restrictive Cardiomyopathy</code></td><td><code>ncit:c55069</code></td><td></td></tr>
<tr><td><code>Right Ventricular Dysfunction</code></td><td><code>ncit:c55070</code></td><td></td></tr>
<tr><td><code>Sick Sinus Syndrome</code></td><td><code>ncit:c54938</code></td><td></td></tr>
<tr><td><code>Sinus Bradycardia</code></td><td><code>ncit:c54940</code></td><td></td></tr>
<tr><td><code>Sinus Tachycardia</code></td><td><code>ncit:c26889</code></td><td></td></tr>
<tr><td><code>Supraventricular Tachycardia</code></td><td><code>ncit:c54945</code></td><td></td></tr>
<tr><td><code>Tricuspid Valve Disease</code></td><td><code>ncit:c143889</code></td><td></td></tr>
<tr><td><code>Ventricular Arrhythmia</code></td><td><code>ncit:c146629</code></td><td></td></tr>
<tr><td><code>Ventricular Fibrillation</code></td><td><code>ncit:c146732</code></td><td></td></tr>
<tr><td><code>Ventricular Tachycardia</code></td><td><code>ncit:c146733</code></td><td></td></tr>
<tr><td><code>Congenital, Familial And Genetic Disorders - Other, Specify</code></td><td><code>ncit:c143382</code></td><td></td></tr>
<tr><td><code>Ear And Labyrinth Disorders - Other, Specify</code></td><td><code>ncit:c143429</code></td><td></td></tr>
<tr><td><code>Ear Pain</code></td><td><code>ncit:c143430</code></td><td></td></tr>
<tr><td><code>External Ear Pain</code></td><td><code>ncit:c146745</code></td><td></td></tr>
<tr><td><code>Precocious Puberty</code></td><td><code>ncit:c146645</code></td><td></td></tr>
<tr><td><code>Testosterone Deficiency</code></td><td><code>ncit:c143195</code></td><td></td></tr>
<tr><td><code>Virilization</code></td><td><code>ncit:c143937</code></td><td></td></tr>
<tr><td><code>Blurred Vision</code></td><td><code>ncit:c55906</code></td><td></td></tr>
<tr><td><code>Corneal Ulcer</code></td><td><code>ncit:c143387</code></td><td></td></tr>
<tr><td><code>Dry Eye</code></td><td><code>ncit:c143410</code></td><td></td></tr>
<tr><td><code>Extraocular Muscle Paresis</code></td><td><code>ncit:c143466</code></td><td></td></tr>
<tr><td><code>Eye Disorders - Other, Specify</code></td><td><code>ncit:c143468</code></td><td></td></tr>
<tr><td><code>Eye Pain</code></td><td><code>ncit:c146751</code></td><td></td></tr>
<tr><td><code>Eyelid Function Disorder</code></td><td><code>ncit:c143471</code></td><td></td></tr>
<tr><td><code>Flashing Lights</code></td><td><code>ncit:c143489</code></td><td></td></tr>
<tr><td><code>Floaters</code></td><td><code>ncit:c143491</code></td><td></td></tr>
<tr><td><code>Glaucoma</code></td><td><code>ncit:c55842</code></td><td></td></tr>
<tr><td><code>Keratitis</code></td><td><code>ncit:c55847</code></td><td></td></tr>
<tr><td><code>Night Blindness</code></td><td><code>ncit:c143705</code></td><td></td></tr>
<tr><td><code>Papilledema</code></td><td><code>ncit:c143734</code></td><td></td></tr>
<tr><td><code>Periorbital Edema</code></td><td><code>ncit:c143747</code></td><td></td></tr>
<tr><td><code>Photophobia</code></td><td><code>ncit:c146770</code></td><td></td></tr>
<tr><td><code>Retinal Detachment</code></td><td><code>ncit:c146729</code></td><td></td></tr>
<tr><td><code>Retinal Tear</code></td><td><code>ncit:c143814</code></td><td></td></tr>
<tr><td><code>Retinal Vascular Disorder</code></td><td><code>ncit:c143815</code></td><td></td></tr>
<tr><td><code>Scleral Disorder</code></td><td><code>ncit:c143823</code></td><td></td></tr>
<tr><td><code>Uveitis</code></td><td><code>ncit:c55901</code></td><td></td></tr>
<tr><td><code>Vitreous Hemorrhage</code></td><td><code>ncit:c146677</code></td><td></td></tr>
<tr><td><code>Watering Eyes</code></td><td><code>ncit:c143944</code></td><td></td></tr>
<tr><td><code>Abdominal Distension</code></td><td><code>ncit:c143253</code></td><td></td></tr>
<tr><td><code>Abdominal Pain</code></td><td><code>ncit:c143255</code></td><td></td></tr>
<tr><td><code>Anal Fissure</code></td><td><code>ncit:c143197</code></td><td></td></tr>
<tr><td><code>Anal Fistula</code></td><td><code>ncit:c143275</code></td><td></td></tr>
<tr><td><code>Anal Hemorrhage</code></td><td><code>ncit:c143276</code></td><td></td></tr>
<tr><td><code>Anal Mucositis</code></td><td><code>ncit:c143277</code></td><td></td></tr>
<tr><td><code>Anal Necrosis</code></td><td><code>ncit:c143278</code></td><td></td></tr>
<tr><td><code>Anal Pain</code></td><td><code>ncit:c143279</code></td><td></td></tr>
<tr><td><code>Anal Stenosis</code></td><td><code>ncit:c143280</code></td><td></td></tr>
<tr><td><code>Anal Ulcer</code></td><td><code>ncit:c143281</code></td><td></td></tr>
<tr><td><code>Ascites</code></td><td><code>ncit:c143300</code></td><td></td></tr>
<tr><td><code>Belching</code></td><td><code>ncit:c143198</code></td><td></td></tr>
<tr><td><code>Bloating</code></td><td><code>ncit:c143322</code></td><td></td></tr>
<tr><td><code>Cecal Hemorrhage</code></td><td><code>ncit:c143358</code></td><td></td></tr>
<tr><td><code>Cheilitis</code></td><td><code>ncit:c57901</code></td><td></td></tr>
<tr><td><code>Chylous Ascites</code></td><td><code>ncit:c143199</code></td><td></td></tr>
<tr><td><code>Colitis</code></td><td><code>ncit:c57134</code></td><td></td></tr>
<tr><td><code>Colonic Fistula</code></td><td><code>ncit:c143373</code></td><td></td></tr>
<tr><td><code>Colonic Hemorrhage</code></td><td><code>ncit:c143374</code></td><td></td></tr>
<tr><td><code>Colonic Obstruction</code></td><td><code>ncit:c143375</code></td><td></td></tr>
<tr><td><code>Colonic Perforation</code></td><td><code>ncit:c143376</code></td><td></td></tr>
<tr><td><code>Colonic Stenosis</code></td><td><code>ncit:c143377</code></td><td></td></tr>
<tr><td><code>Colonic Ulcer</code></td><td><code>ncit:c143378</code></td><td></td></tr>
<tr><td><code>Constipation</code></td><td><code>ncit:c57141</code></td><td></td></tr>
<tr><td><code>Dental Caries</code></td><td><code>ncit:c143402</code></td><td></td></tr>
<tr><td><code>Diarrhea</code></td><td><code>ncit:c57788</code></td><td></td></tr>
<tr><td><code>Dry Mouth</code></td><td><code>ncit:c143411</code></td><td></td></tr>
<tr><td><code>Duodenal Fistula</code></td><td><code>ncit:c57789</code></td><td></td></tr>
<tr><td><code>Duodenal Hemorrhage</code></td><td><code>ncit:c143414</code></td><td></td></tr>
<tr><td><code>Duodenal Obstruction</code></td><td><code>ncit:c143416</code></td><td></td></tr>
<tr><td><code>Duodenal Perforation</code></td><td><code>ncit:c143417</code></td><td></td></tr>
<tr><td><code>Duodenal Stenosis</code></td><td><code>ncit:c143418</code></td><td></td></tr>
<tr><td><code>Duodenal Ulcer</code></td><td><code>ncit:c143419</code></td><td></td></tr>
<tr><td><code>Dyspepsia</code></td><td><code>ncit:c143425</code></td><td></td></tr>
<tr><td><code>Enterocolitis</code></td><td><code>ncit:c143445</code></td><td></td></tr>
<tr><td><code>Enterovesical Fistula</code></td><td><code>ncit:c143446</code></td><td></td></tr>
<tr><td><code>Esophageal Fistula</code></td><td><code>ncit:c57798</code></td><td></td></tr>
<tr><td><code>Esophageal Hemorrhage</code></td><td><code>ncit:c143453</code></td><td></td></tr>
<tr><td><code>Esophageal Necrosis</code></td><td><code>ncit:c143455</code></td><td></td></tr>
<tr><td><code>Esophageal Obstruction</code></td><td><code>ncit:c143456</code></td><td></td></tr>
<tr><td><code>Esophageal Pain</code></td><td><code>ncit:c143457</code></td><td></td></tr>
<tr><td><code>Esophageal Perforation</code></td><td><code>ncit:c143458</code></td><td></td></tr>
<tr><td><code>Esophageal Stenosis</code></td><td><code>ncit:c143459</code></td><td></td></tr>
<tr><td><code>Esophageal Ulcer</code></td><td><code>ncit:c143460</code></td><td></td></tr>
<tr><td><code>Esophageal Varices Hemorrhage</code></td><td><code>ncit:c146710</code></td><td></td></tr>
<tr><td><code>Esophagitis</code></td><td><code>ncit:c57797</code></td><td></td></tr>
<tr><td><code>Fecal Incontinence</code></td><td><code>ncit:c143482</code></td><td></td></tr>
<tr><td><code>Flatulence</code></td><td><code>ncit:c57807</code></td><td></td></tr>
<tr><td><code>Gastric Fistula</code></td><td><code>ncit:c143499</code></td><td></td></tr>
<tr><td><code>Gastric Hemorrhage</code></td><td><code>ncit:c143500</code></td><td></td></tr>
<tr><td><code>Gastric Necrosis</code></td><td><code>ncit:c143501</code></td><td></td></tr>
<tr><td><code>Gastric Perforation</code></td><td><code>ncit:c143502</code></td><td></td></tr>
<tr><td><code>Gastric Stenosis</code></td><td><code>ncit:c143503</code></td><td></td></tr>
<tr><td><code>Gastric Ulcer</code></td><td><code>ncit:c143504</code></td><td></td></tr>
<tr><td><code>Gastritis</code></td><td><code>ncit:c57812</code></td><td></td></tr>
<tr><td><code>Gastroesophageal Reflux Disease</code></td><td><code>ncit:c143506</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Disorders - Other, Specify</code></td><td><code>ncit:c143508</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Fistula</code></td><td><code>ncit:c146637</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Pain</code></td><td><code>ncit:c143510</code></td><td></td></tr>
<tr><td><code>Gastroparesis</code></td><td><code>ncit:c143512</code></td><td></td></tr>
<tr><td><code>Gingival Pain</code></td><td><code>ncit:c146626</code></td><td></td></tr>
<tr><td><code>Hemorrhoidal Hemorrhage</code></td><td><code>ncit:c143537</code></td><td></td></tr>
<tr><td><code>Hemorrhoids</code></td><td><code>ncit:c146738</code></td><td></td></tr>
<tr><td><code>Ileal Fistula</code></td><td><code>ncit:c57821</code></td><td></td></tr>
<tr><td><code>Ileal Hemorrhage</code></td><td><code>ncit:c56542</code></td><td></td></tr>
<tr><td><code>Ileal Obstruction</code></td><td><code>ncit:c57823</code></td><td></td></tr>
<tr><td><code>Ileal Perforation</code></td><td><code>ncit:c146633</code></td><td></td></tr>
<tr><td><code>Ileal Stenosis</code></td><td><code>ncit:c143578</code></td><td></td></tr>
<tr><td><code>Ileal Ulcer</code></td><td><code>ncit:c57826</code></td><td></td></tr>
<tr><td><code>Ileus</code></td><td><code>ncit:c57814</code></td><td></td></tr>
<tr><td><code>Intra-Abdominal Hemorrhage</code></td><td><code>ncit:c143595</code></td><td></td></tr>
<tr><td><code>Jejunal Fistula</code></td><td><code>ncit:c57827</code></td><td></td></tr>
<tr><td><code>Jejunal Hemorrhage</code></td><td><code>ncit:c56543</code></td><td></td></tr>
<tr><td><code>Jejunal Obstruction</code></td><td><code>ncit:c57829</code></td><td></td></tr>
<tr><td><code>Jejunal Perforation</code></td><td><code>ncit:c143622</code></td><td></td></tr>
<tr><td><code>Jejunal Stenosis</code></td><td><code>ncit:c143623</code></td><td></td></tr>
<tr><td><code>Jejunal Ulcer</code></td><td><code>ncit:c57832</code></td><td></td></tr>
<tr><td><code>Lip Pain</code></td><td><code>ncit:c146761</code></td><td></td></tr>
<tr><td><code>Lower Gastrointestinal Hemorrhage</code></td><td><code>ncit:c143656</code></td><td></td></tr>
<tr><td><code>Malabsorption</code></td><td><code>ncit:c57838</code></td><td></td></tr>
<tr><td><code>Mucositis Oral</code></td><td><code>ncit:c143679</code></td><td></td></tr>
<tr><td><code>Nausea</code></td><td><code>ncit:c146764</code></td><td></td></tr>
<tr><td><code>Obstruction Gastric</code></td><td><code>ncit:c143710</code></td><td></td></tr>
<tr><td><code>Oral Cavity Fistula</code></td><td><code>ncit:c143715</code></td><td></td></tr>
<tr><td><code>Oral Dysesthesia</code></td><td><code>ncit:c143716</code></td><td></td></tr>
<tr><td><code>Oral Hemorrhage</code></td><td><code>ncit:c56551</code></td><td></td></tr>
<tr><td><code>Oral Pain</code></td><td><code>ncit:c146627</code></td><td></td></tr>
<tr><td><code>Pancreatic Duct Stenosis</code></td><td><code>ncit:c143730</code></td><td></td></tr>
<tr><td><code>Pancreatic Fistula</code></td><td><code>ncit:c57845</code></td><td></td></tr>
<tr><td><code>Pancreatic Hemorrhage</code></td><td><code>ncit:c56554</code></td><td></td></tr>
<tr><td><code>Pancreatic Necrosis</code></td><td><code>ncit:c143732</code></td><td></td></tr>
<tr><td><code>Pancreatitis</code></td><td><code>ncit:c146789</code></td><td></td></tr>
<tr><td><code>Periodontal Disease</code></td><td><code>ncit:c57849</code></td><td></td></tr>
<tr><td><code>Peritoneal Necrosis</code></td><td><code>ncit:c57850</code></td><td></td></tr>
<tr><td><code>Proctitis</code></td><td><code>ncit:c57857</code></td><td></td></tr>
<tr><td><code>Rectal Fissure</code></td><td><code>ncit:c143200</code></td><td></td></tr>
<tr><td><code>Rectal Fistula</code></td><td><code>ncit:c57859</code></td><td></td></tr>
<tr><td><code>Rectal Hemorrhage</code></td><td><code>ncit:c56560</code></td><td></td></tr>
<tr><td><code>Rectal Mucositis</code></td><td><code>ncit:c143802</code></td><td></td></tr>
<tr><td><code>Rectal Necrosis</code></td><td><code>ncit:c57863</code></td><td></td></tr>
<tr><td><code>Rectal Obstruction</code></td><td><code>ncit:c57864</code></td><td></td></tr>
<tr><td><code>Rectal Pain</code></td><td><code>ncit:c146631</code></td><td></td></tr>
<tr><td><code>Rectal Perforation</code></td><td><code>ncit:c146634</code></td><td></td></tr>
<tr><td><code>Rectal Stenosis</code></td><td><code>ncit:c143803</code></td><td></td></tr>
<tr><td><code>Rectal Ulcer</code></td><td><code>ncit:c57867</code></td><td></td></tr>
<tr><td><code>Retroperitoneal Hemorrhage</code></td><td><code>ncit:c146632</code></td><td></td></tr>
<tr><td><code>Salivary Duct Inflammation</code></td><td><code>ncit:c143821</code></td><td></td></tr>
<tr><td><code>Salivary Gland Fistula</code></td><td><code>ncit:c57868</code></td><td></td></tr>
<tr><td><code>Small Intestinal Mucositis</code></td><td><code>ncit:c143842</code></td><td></td></tr>
<tr><td><code>Small Intestinal Obstruction</code></td><td><code>ncit:c143843</code></td><td></td></tr>
<tr><td><code>Small Intestinal Perforation</code></td><td><code>ncit:c146635</code></td><td></td></tr>
<tr><td><code>Small Intestinal Stenosis</code></td><td><code>ncit:c143844</code></td><td></td></tr>
<tr><td><code>Small Intestine Ulcer</code></td><td><code>ncit:c143846</code></td><td></td></tr>
<tr><td><code>Stomach Pain</code></td><td><code>ncit:c146774</code></td><td></td></tr>
<tr><td><code>Middle Ear Inflammation</code></td><td><code>ncit:c143673</code></td><td></td></tr>
<tr><td><code>Vestibular Disorder</code></td><td><code>ncit:c143936</code></td><td></td></tr>
<tr><td><code>Adrenal Insufficiency</code></td><td><code>ncit:c55748</code></td><td></td></tr>
<tr><td><code>Cushingoid</code></td><td><code>ncit:c143392</code></td><td></td></tr>
<tr><td><code>Delayed Puberty</code></td><td><code>ncit:c55742</code></td><td></td></tr>
<tr><td><code>Endocrine Disorders - Other, Specify</code></td><td><code>ncit:c143442</code></td><td></td></tr>
<tr><td><code>Growth Accelerated</code></td><td><code>ncit:c143520</code></td><td></td></tr>
<tr><td><code>Hyperparathyroidism</code></td><td><code>ncit:c143557</code></td><td></td></tr>
<tr><td><code>Hyperthyroidism</code></td><td><code>ncit:c143560</code></td><td></td></tr>
<tr><td><code>Hypoparathyroidism</code></td><td><code>ncit:c143572</code></td><td></td></tr>
<tr><td><code>Tooth development disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tooth discoloration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Toothache</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvic floor muscle weakness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvic pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Penile pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Perineal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Premature menopause</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostatic hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostatic obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostatic pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Reproductive system and breast disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scrotal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spermatic cord hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spermatic cord obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal discharge</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal dryness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal inflammation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal stricture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Adult respiratory distress syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Allergic rhinitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Apnea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aspiration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Atelectasis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchial fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchial obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchial stricture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchopleural fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchopulmonary hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchospasm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chylothorax</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cough</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dyspnea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Epistaxis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hiccups</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoxia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal inflammation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal mucositis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngeal stenosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngopharyngeal dysesthesia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngospasm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mediastinal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal congestion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oropharyngeal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal mucositis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal stenosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngolaryngeal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleural effusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleural hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleuritic pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pneumonitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pneumothorax</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Postnasal drip</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Productive cough</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pulmonary edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pulmonary fibrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pulmonary fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pulmonary hypertension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Respiratory failure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Respiratory, thoracic and mediastinal disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retinoic acid syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhinorrhea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sinus disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sinus pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sleep apnea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sneezing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sore throat</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stridor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheal fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheal mucositis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheal stenosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Voice alteration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wheezing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alopecia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Body odor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bullous dermatitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dry skin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eczema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Erythema multiforme</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Erythroderma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fat atrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hair color changes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hair texture abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hirsutism</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperhidrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperkeratosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypertrichosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypohidrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lipohypertrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nail changes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nail discoloration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nail loss</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nail ridging</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pain of skin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Palmar-plantar erythrodysesthesia syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Photosensitivity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pruritus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Purpura</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rash acneiform</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rash maculo-papular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scalp pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin and subcutaneous tissue disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin atrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin hyperpigmentation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin hypopigmentation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin induration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin ulceration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stevens-Johnson syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subcutaneous emphysema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Telangiectasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Toxic epidermal necrolysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urticaria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Social circumstances - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Surgical and medical procedures - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arterial thromboembolism</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Capillary leak syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flushing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hematoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hot flashes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypertension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypotension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymph leakage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphedema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphocele</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peripheral ischemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Phlebitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Superficial thrombophlebitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Superior vena cava syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thromboembolic event</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vascular disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vasculitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Superficial soft tissue fibrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unequal limb length</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leukemia secondary to oncology chemotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myelodysplastic syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neoplasms benign, malignant and unspecified (incl cysts and polyps) - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin papilloma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Treatment related secondary malignancy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tumor hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tumor pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abducens nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Accessory nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acoustic nerve disorder NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Akathisia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Amnesia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anosmia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aphonia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arachnoiditis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ataxia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brachial plexopathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Central nervous system necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cerebrospinal fluid leakage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cognitive disturbance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Concentration impairment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Depressed level of consciousness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dizziness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysarthria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysesthesia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysgeusia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysphasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Edema cerebral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Encephalopathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Extrapyramidal disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Facial muscle weakness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Facial nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glossopharyngeal nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Guillain-Barre syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Headache</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hydrocephalus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypersomnia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoglossal nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intracranial hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ischemia cerebrovascular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lethargy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leukoencephalopathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Memory impairment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Meningismus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Movements involuntary</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle weakness left-sided</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle weakness right-sided</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myasthenia gravis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nervous system disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neuralgia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nystagmus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oculomotor nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Olfactory nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paresthesia</code></td><td><code>ncit:C143736</code></td><td></td></tr>
<tr><td><code>Peripheral motor neuropathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peripheral sensory neuropathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Phantom pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Presyncope</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pyramidal tract syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radiculitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Recurrent laryngeal nerve palsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Reversible posterior leukoencephalopathy syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Seizure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Somnolence</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spasticity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spinal cord compression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Syncope</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tendon reflex decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transient ischemic attacks</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tremor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trigeminal nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trochlear nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vagus nerve disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vasovagal reaction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fetal growth retardation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pregnancy loss</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pregnancy, puerperium and perinatal conditions - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Premature delivery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Agitation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anorgasmia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anxiety</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Confusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Delayed orgasm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Delirium</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Delusions</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Depression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Euphoria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hallucinations</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Insomnia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Irritability</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Libido decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Libido increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mania</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Personality change</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Psychiatric disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Psychosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Restlessness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Suicidal ideation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Suicide attempt</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acute kidney injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder spasm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chronic kidney disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cystitis noninfective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysuria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glucosuria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hemoglobinuria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nephrotic syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal and urinary disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal calculi</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal colic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary frequency</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary incontinence</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary retention</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary tract obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary tract pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary urgency</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urine discoloration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Amenorrhea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Azoospermia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Breast atrophy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Breast pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysmenorrhea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dyspareunia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ejaculation disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Erectile dysfunction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fallopian tube obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Feminization acquired</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gynecomastia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hematosalpinx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Irregular menstruation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lactation disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Menorrhagia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nipple deformity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oligospermia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovarian hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovarian rupture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovulation pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative respiratory injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative splenic injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative urinary injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative venous injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Large intestinal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pancreatic anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngeal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Postoperative hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Postoperative thoracic procedure complication</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prolapse of intestinal stoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prolapse of urostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radiation recall reaction (dermatologic)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rectal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Seroma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small intestinal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spermatic cord anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spinal fracture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stenosis of gastrointestinal stoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stomal ulcer</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheal obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheostomy site bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ureteric anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urethral anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urostomy leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urostomy obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urostomy site bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urostomy stenosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaccination complication</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vas deferens anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vascular access complication</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Venous injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wound complication</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wound dehiscence</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wrist fracture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Activated partial thromboplastin time prolonged</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alanine aminotransferase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alkaline phosphatase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aspartate aminotransferase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood antidiuretic hormone abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood bicarbonate decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood bilirubin increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood corticotrophin decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood gonadotrophin abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood lactate dehydrogenase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blood prolactin abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Carbon monoxide diffusing capacity decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cardiac troponin I increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cardiac troponin T increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CD4 lymphocytes decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cholesterol high</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CPK increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Creatinine increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ejection fraction decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Electrocardiogram QT corrected interval prolonged</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Electrocardiogram T wave abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fibrinogen decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Forced expiratory volume decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GGT increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Growth hormone abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Haptoglobin decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hemoglobin increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INR increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Investigations - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lipase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphocyte count decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymphocyte count increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neutrophil count decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pancreatic enzymes decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Platelet count decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Serum amylase increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thyroid stimulating hormone increased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urine output decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vital capacity abnormal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Weight gain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Weight loss</code></td><td><code></code></td><td></td></tr>
<tr><td><code>White blood cell decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acidosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alcohol intolerance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alkalosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anorexia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dehydration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glucose intolerance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypercalcemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperglycemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperkalemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperlipidemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypermagnesemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypernatremia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperphosphatemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypertriglyceridemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperuricemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoalbuminemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypocalcemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoglycemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypokalemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypomagnesemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyponatremia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypophosphatemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iron overload</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metabolism and nutrition disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Obesity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tumor lysis syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abdominal soft tissue necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arthralgia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arthritis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Avascular necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Back pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Buttock pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chest wall necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chest wall pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Exostosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fibrosis deep connective tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flank pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Generalized muscle weakness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Growth suppression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head soft tissue necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Joint effusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Joint range of motion decreased</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Joint range of motion decreased cervical spine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Joint range of motion decreased lumbar spine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kyphosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lordosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle cramp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle weakness lower limb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle weakness trunk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Muscle weakness upper limb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Musculoskeletal and connective tissue disorder - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Musculoskeletal deformity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myalgia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myositis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck soft tissue necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Osteonecrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Osteonecrosis of jaw</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Osteoporosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pain in extremity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvic soft tissue necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhabdomyolysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rotator cuff injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scoliosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soft tissue necrosis lower limb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soft tissue necrosis upper limb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic failure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatobiliary disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Perforation bile duct</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Portal hypertension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Portal vein thrombosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anaphylaxis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autoimmune disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cytokine release syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Immune system disorders - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Serum sickness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abdominal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anorectal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Appendicitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Appendicitis perforated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arteritis infective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bacteremia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Biliary tract infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Breast infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bronchial infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Catheter related infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cecal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cervicitis infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Conjunctivitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Conjunctivitis infective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Corneal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cranial nerve infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cytomegalovirus infection reactivation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Device related infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Duodenal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Encephalitis infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Encephalomyelitis infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endocarditis infective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endophthalmitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enterocolitis infectious</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Epstein-Barr virus infection reactivation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Esophageal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Folliculitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fungemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallbladder infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gum infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatic infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatitis B reactivation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hepatitis viral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Herpes simplex reactivation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infections and infestations - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infective myositis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Joint infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lip infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymph gland infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mediastinal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Meningitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mucosal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myelitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nail infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Otitis externa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Otitis media</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovarian infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pancreas infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Papulopustular rash</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paronychia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvic infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Penile infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Periorbital infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peripheral nerve infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peritoneal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Phlebitis infective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleural infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostate infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rash pustular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhinitis infective</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Salivary gland infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scrotal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sepsis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Shingles</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sinusitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small intestine infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soft tissue infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Splenic infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stoma site infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thrush</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tooth infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper respiratory infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urethral infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urinary tract infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterine infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginal infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Viremia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulval infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wound infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ankle fracture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aortic injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arterial injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Biliary anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bruising</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Burn</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dermatitis radiation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Esophageal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fall</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fallopian tube anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fallopian tube perforation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fracture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastric anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastrointestinal anastomotic leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gastrointestinal stoma necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hip fracture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infusion related reaction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injury to carotid artery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injury to inferior vena cava</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injury to jugular vein</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injury to superior vena cava</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injury, poisoning and procedural complications - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intestinal stoma leak</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intestinal stoma obstruction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intestinal stoma site bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative arterial injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative breast injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative cardiac injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative ear injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative endocrine injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative gastrointestinal injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative head and neck injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative hepatobiliary injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative musculoskeletal injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative neurological injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative ocular injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative renal injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraoperative reproductive tract injury</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper gastrointestinal hemorrhage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Visceral arterial ischemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vomiting</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chills</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Death neonatal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Death NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Disease progression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Edema face</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Edema limbs</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Edema trunk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Facial pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fever</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flu like symptoms</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gait disturbance</code></td><td><code></code></td><td></td></tr>
<tr><td><code>General disorders and administration site conditions - Other, specify</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Generalized edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypothermia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infusion site extravasation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Injection site reaction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Localized edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Malaise</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Multi-organ failure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck edema</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-cardiac chest pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sudden death NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaccination site lymphadenopathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bile duct stenosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Biliary fistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Budd-Chiari syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cholecystitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Disseminated Intravascular Coagulation</code></td><td><code>ncit:C2992</code></td><td></td></tr>
<tr><td><code>Dysphagia</code></td><td><code>ncit:C57795</code></td><td></td></tr>
<tr><td><code>Eosinophilia</code></td><td><code>ncit:C143190</code></td><td></td></tr>
<tr><td><code>Fatigue</code></td><td><code>ncit:C3036</code></td><td></td></tr>
<tr><td><code>Febrile Neutropenia</code></td><td><code>ncit:C35665</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hearing Impaired</code></td><td><code>ncit:C143528</code></td><td></td></tr>
<tr><td><code>Hematuria</code></td><td><code>ncit:C3090</code></td><td></td></tr>
<tr><td><code>Hemolysis</code></td><td><code>ncit:C37965</code></td><td></td></tr>
<tr><td><code>Hemolytic Uremic Syndrome</code></td><td><code>ncit:C75545</code></td><td></td></tr>
<tr><td><code>Hoarseness</code></td><td><code>ncit:C47813</code></td><td></td></tr>
<tr><td><code>Hypothyroidism</code></td><td><code>ncit:C143576</code></td><td></td></tr>
<tr><td><code>Left Ventricular Systolic Dysfunction</code></td><td><code>ncit:C64251</code></td><td></td></tr>
<tr><td><code>Leukocytosis</code></td><td><code>ncit:C35524</code></td><td></td></tr>
<tr><td><code>Lymph Node Pain</code></td><td><code>ncit:C78440</code></td><td></td></tr>
<tr><td><code>Methemoglobinemia</code></td><td><code>ncit:C143191</code></td><td></td></tr>
<tr><td><code>Optic Nerve Disorder</code></td><td><code>ncit:C143714</code></td><td></td></tr>
<tr><td><code>Proteinuria</code></td><td><code>ncit:C38012</code></td><td></td></tr>
<tr><td><code>Retinopathy</code></td><td><code>ncit:C55891</code></td><td></td></tr>
<tr><td><code>Sinusoidal Obstruction Syndrome</code></td><td><code>ncit:C26793</code></td><td></td></tr>
<tr><td><code>Stroke</code></td><td><code>ncit:C143862</code></td><td></td></tr>
<tr><td><code>Thrombotic Thrombocytopenic Purpura</code></td><td><code>ncit:C78797</code></td><td></td></tr>
<tr><td><code>Tinnitus</code></td><td><code>ncit:C146690</code></td><td></td></tr>
<tr><td><code>Trismus</code></td><td><code>ncit:C58404</code></td><td></td></tr>
<tr><td><code>Typhlitis</code></td><td><code>ncit:C38043</code></td><td></td></tr>
<tr><td><code>Vertigo</code></td><td><code>ncit:C143935</code></td><td></td></tr>
<tr><td><code>Vision Decreased</code></td><td><code>ncit:C143196</code></td><td></td></tr>
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

<div id="enum-modal-aetreatmentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aetreatmentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aetreatmentenum')">×</button>
<h3><code>AeTreatmentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alternative Medications</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chemotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Immunotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stem Cell Transplant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>lb</code></td><td><code></code></td><td></td></tr>
<tr><td><code>inch</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-assessmentreasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-assessmentreasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-assessmentreasonenum')">×</button>
<h3><code>AssessmentReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Surveillance Assessment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Symptomatic Assessment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-breakagesourcelabenum" class="enum-modal" onclick="closeEnumModal('enum-modal-breakagesourcelabenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-breakagesourcelabenum')">×</button>
<h3><code>BreakageSourceLabEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ARUP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cincinnati Children's Hospital Medical Center</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dana-Farber Cancer Institute</code></td><td><code>ncit:C177330</code></td><td></td></tr>
<tr><td><code>Julius-Maximilians-Universität of Würzburg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laboratorio de Citogenética, Instituto Nacional de Pediatría, México</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OHSU</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Quest Diagnostics</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stanford University</code></td><td><code></code></td><td></td></tr>
<tr><td><code>The Rockefeller University</code></td><td><code></code></td><td></td></tr>
<tr><td><code>University of Chicago</code></td><td><code></code></td><td></td></tr>
<tr><td><code>University of Minnesota</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bone Marrow Failure Complications</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cancer Progression, NOS</code></td><td><code>ncit:C19987</code></td><td></td></tr>
<tr><td><code>Cardiac Disease</code></td><td><code>ncit:C3079</code></td><td></td></tr>
<tr><td><code>Cardiac Failure</code></td><td><code>ncit:C50577</code></td><td></td></tr>
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Immunotherapy-Related</code></td><td><code>ncit:C168874</code></td><td></td></tr>
<tr><td><code>Infection, NOS</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Infection, Not Otherwise Specified</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Kidney Failure</code></td><td><code>ncit:C4376</code></td><td></td></tr>
<tr><td><code>Liver Failure</code></td><td><code>ncit:C26922</code></td><td></td></tr>
<tr><td><code>Multi-Organ Failure</code></td><td><code>ncit:C75568</code></td><td></td></tr>
<tr><td><code>Organ Failure, NOS</code></td><td><code>ncit:C185320</code></td><td></td></tr>
<tr><td><code>Pulmonary Disease</code></td><td><code>ncit:C3198</code></td><td></td></tr>
<tr><td><code>Sinusoidal Obstruction Syndrome</code></td><td><code>ncit:C26793</code></td><td></td></tr>
<tr><td><code>Surgical Complication</code></td><td><code>ncit:C164157</code></td><td></td></tr>
<tr><td><code>Unacceptable Toxicity</code></td><td><code>ncit:C199267</code></td><td></td></tr>
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

<div id="enum-modal-chimerismunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-chimerismunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-chimerismunitenum')">×</button>
<h3><code>ChimerismUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>% of CD34 Cells</code></td><td><code></code></td><td></td></tr>
<tr><td><code>% of T Cells</code></td><td><code></code></td><td></td></tr>
<tr><td><code>% of Granulocytes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>% of White Blood Cells</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-clinicalfindingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-clinicalfindingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-clinicalfindingenum')">×</button>
<h3><code>ClinicalFindingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abdominal pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal Anus Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Anal Anomaly</td></tr>
<tr><td><code>Abnormal Duodenal Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Abnormal Esophagus Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Abnormal Heart Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Abnormal Heart Valve Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Abnormal Morphology of the Thumb</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Abnormal Renal Morphology NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Abnormal Speech</code></td><td><code>ncit:C5041</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Abnormal Thumb Morphology</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Abnormal Uterine Bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal corpus callosum morphology</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal fallopian tube morphology NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal female external genitalia morphology</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal malleus morphology</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal nervous system morphology NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal oral mucosa morphology NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal pinna morhology (Microtia, poliotia, abnormal helix, etc)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal size of the palpebral fissures</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormal tympanic membrane morphology (no hay HP para &quot;small&quot;)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of skin pigmentation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of the Upper Limb NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Abnormality of the Ureter NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Abnormality of the Vertebral Column NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Vertebral Anomaly</td></tr>
<tr><td><code>Abnormality of the dentition NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of the ear NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of the eye NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of the female genitalia NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Abnormality of the male genitalia NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Absent Radius</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Absent Thumb</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Absent testes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia Susceptibility - PAX5</code></td><td><code>ncit:C176907</code></td><td></td></tr>
<tr><td><code>Anal Atresia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Anal Anomaly</td></tr>
<tr><td><code>Anal Fistula</code></td><td><code></code></td><td>(fa) ConsortiumNote: Anal Anomaly</td></tr>
<tr><td><code>Anal Stenosis</code></td><td><code></code></td><td>(fa) ConsortiumNote: Anal Anomaly</td></tr>
<tr><td><code>Aplasia of the ovary</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aplasia uterus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aspiration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ataxia</code></td><td><code>ncit:C26702</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Atresia of the external auditory canal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Atrial Septal Defect</code></td><td><code>ncit:C84473</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Attentions Deficit Hyperactivity Disorder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Back Pain</code></td><td><code></code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Behavioral/Cognitive Changes</code></td><td><code></code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Birth length less than 3rd percentile</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bleeding, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blurry Vision/Loss of Vision</code></td><td><code>ncit:C50602</code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Bruising</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cataracts</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Central nervous system cysts</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cerebellar hypoplasia (vermis, olivo-ponto and hemisphere cerebellar hypoplasia)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cerebral hypoplasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chest pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Choking</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cleft Palate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Coarctation of Aorta</code></td><td><code>ncit:C84567</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Complex Migraine</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Cortical Signs</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Coughing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cranial Mono-neuropathy</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Craniosynostosis</code></td><td><code>ncit:C84655</code></td><td>(fa) ConsortiumNote: PHENOS Feature</td></tr>
<tr><td><code>Crossed Fused Renal Ectopia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Cryptorchidism</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Decreased testicular size</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Difficulty Breathing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Difficulty Swallowing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Double Vision</code></td><td><code>ncit:C37941</code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Duodenal Atresia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Duodenal Stenosis</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Duodenal Web</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Dysdiadochokinesia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Dysphagia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dysplastic Kidney</code></td><td><code>ncit:C123031</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Earache</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ectopic Anus</code></td><td><code></code></td><td>(fa) ConsortiumNote: Anal Anomaly</td></tr>
<tr><td><code>Ectopic Kidney</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Encephalopathy</code></td><td><code>ncit:C26920</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Encephalopathy, Focal Numbness</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Encephalopathy, Focal Weakness</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Epicanthal folds (epicanthus)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Erectile Dysfunction</code></td><td><code>ncit:C3133</code></td><td></td></tr>
<tr><td><code>Erythroplakia</code></td><td><code>ncit:C3025</code></td><td></td></tr>
<tr><td><code>Esophageal Atresia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Esophageal Stenosis</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Esophageal Web</code></td><td><code></code></td><td>(fa) ConsortiumNote: Esophageal Duodenal Atresia</td></tr>
<tr><td><code>Eye Movement Abnormalities</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Fatigue</code></td><td><code>ncit:C3036</code></td><td></td></tr>
<tr><td><code>Feeling of lump in throat</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fevers</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Focal Weakness, NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Gagging</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Generalized hyperpigmentation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glaucoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Halitosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Headache</code></td><td><code>ncit:C34661</code></td><td>(fa) ConsortiumNote: FANS Diagnosis<br>(fa)  ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Hearing impairment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hematemesis</code></td><td><code>ncit:C37964</code></td><td></td></tr>
<tr><td><code>Hepatomegaly</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hoarseness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Horseshoe Kidney</code></td><td><code>ncit:C98947</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Human Papillomavirus Infection</code></td><td><code>ncit:C27851</code></td><td></td></tr>
<tr><td><code>Human immunodeficiency virus [HIV] disease</code></td><td><code>icd10:B20</code></td><td></td></tr>
<tr><td><code>Hydrocephalus</code></td><td><code>ncit:C3111</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Hydronephrosis</code></td><td><code>ncit:C26796</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Hydroureter</code></td><td><code>ncit:C26927</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Hyperpigmented freckle like macules/acanthomas in flexural areas</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperpigmented macules (hypermelanotic macule)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperreflexia</code></td><td><code>ncit:C43248</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Hypertension</code></td><td><code></code></td><td>(fa) ConsortiumNote: Medical HIstory</td></tr>
<tr><td><code>Hypopigmented macules</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoplasia of penis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoplasia of the Radius</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Hypoplasia of the ovary</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoplasia of the uterus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypoplastic Thenar Eminence</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Hypospadias</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hypotelorism</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Imbalance</code></td><td><code>ncit:C200084</code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Impaired Consciousness</code></td><td><code>ncit:C121627</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Incontinence</code></td><td><code>ncit:C3429</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Increased Intracranial Pressure</code></td><td><code>ncit:C187268</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Intellectual disability</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrauterine Growth Restriction</code></td><td><code>ncit:C87088</code></td><td>(fa) ConsortiumNote: Birth History</td></tr>
<tr><td><code>Itching</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Jaw pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leukopenia</code></td><td><code>ncit:C26816</code></td><td></td></tr>
<tr><td><code>Leukoplakia</code></td><td><code>ncit:C3186</code></td><td></td></tr>
<tr><td><code>Lichen Planus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Limb Pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Limbal neovascularization</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver abnormalities</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver adenomas</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Loss of smell</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Loss of taste</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low set ears</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Melena/Black Stool</code></td><td><code>ncit:C86571</code></td><td></td></tr>
<tr><td><code>Meningismus</code></td><td><code>ncit:C79694</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Microcornea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Microdontia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Microphtalmia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Migraine</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Multiple Cranial Neuropathies</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Myelopathy, Focal Numbness</code></td><td><code>ncit:C34857</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Myelopathy, Focal Weakness</code></td><td><code>ncit:C182336</code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Narrow internal auditory canal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nausea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck Pain</code></td><td><code></code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Neural Tube Defects</code></td><td><code></code></td><td>(fa) ConsortiumNote: Vertebral Anomaly</td></tr>
<tr><td><code>Neurogenic Bladder/Bowel</code></td><td><code>ncit:C79696</code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Neuropathy</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Night sweats</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Numbness, NOS</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Optic nerve hypoplasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Bacterial Infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Fungal Infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Viral Infection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pain, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paresthesia</code></td><td><code>ncit:C28177</code></td><td>(fa) ConsortiumNote: FANS Diagnosis<br>(fa)  ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Partial Duplication of Thumb Phalanx</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Patent Ductus Arteriosus</code></td><td><code>ncit:C84492</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Patent Foramen Ovale</code></td><td><code></code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Pelvic Pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Petechiae</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Positive Visual Phenomenon</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Symptoms History</td></tr>
<tr><td><code>Postcoital Bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Postmenopausal Bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Preaxial Hand Polydactyly</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Premalignant lesion / dysplasia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ptosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Recurrent Mouth Sores</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Reflux</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Renal Agenesis</code></td><td><code>ncit:C101220</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Renal Cysts</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Renal Duplication</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Renal Hypoplasia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Renal Malrotation</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Retinopathy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scoliosis</code></td><td><code></code></td><td>(fa) ConsortiumNote: Vertebral Anomaly</td></tr>
<tr><td><code>Seizure</code></td><td><code>ncit:C2962</code></td><td>(fa) ConsortiumNote: FANS Diagnosis<br>(fa)  ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Sensorineural Hearing Loss</code></td><td><code></code></td><td>(fa) ConsortiumNote: Medical HIstory</td></tr>
<tr><td><code>Severe aplastic anemia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Severe isolated lineage cytopenia: platelet</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Severe isolated lineage cytopenia: red cell</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Severe isolated lineage cytopenia: white cell</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Short Thumb</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Short stature NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Situs Inversus</code></td><td><code>ncit:C87121</code></td><td></td></tr>
<tr><td><code>Slurred Speech</code></td><td><code></code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Small for Gestational Age</code></td><td><code>ncit:C114934</code></td><td>(fa) ConsortiumNote: Birth History</td></tr>
<tr><td><code>Small pituitary gland</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sore throat</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spinal Level Myelopathy</code></td><td><code></code></td><td>(fa) ConsortiumNote: Neurological Exam/Phenotype</td></tr>
<tr><td><code>Stenosis of the external auditory canal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Strabismus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subluxed Thumb</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Supernumerary tooth</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Swelling</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Systemic Lupus Erythematosus</code></td><td><code></code></td><td>(fa) ConsortiumNote: Medical HIstory</td></tr>
<tr><td><code>Tetralogy of Fallot</code></td><td><code>ncit:C84505</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Thrombocytopenia</code></td><td><code>ncit:C3408</code></td><td></td></tr>
<tr><td><code>Tightness in chest</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tooth agenesis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transient cytopenia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Triphalangeal Thumb</code></td><td><code></code></td><td>(fa) ConsortiumNote: Upper Limb Anomaly</td></tr>
<tr><td><code>Truncus Arteriosus</code></td><td><code>ncit:C98880</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Ureteral Agenesis</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Ureteral Duplication</code></td><td><code>ncit:C98917</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Ureteral Hypoplasia</code></td><td><code></code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Vaginal Discharge</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ventricular Septal Defect</code></td><td><code>ncit:C84506</code></td><td>(fa) ConsortiumNote: Cardiac Anomaly</td></tr>
<tr><td><code>Ventriculomegaly</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vertebral Fusion</code></td><td><code></code></td><td>(fa) ConsortiumNote: Vertebral Anomaly</td></tr>
<tr><td><code>Vertigo</code></td><td><code>ncit:C38057</code></td><td>(fa) ConsortiumNote: FANS Diagnosis</td></tr>
<tr><td><code>Vesicoureteral Reflux</code></td><td><code>ncit:C84467</code></td><td>(fa) ConsortiumNote: Renal Anomaly</td></tr>
<tr><td><code>Voice Alteration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vomiting</code></td><td><code>ncit:C3442</code></td><td></td></tr>
<tr><td><code>Vulvar Pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Weight Loss</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Wheezing</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Antibody Conditioning</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>FRIENDS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Angiogram</code></td><td><code>ncit:C16290</code></td><td></td></tr>
<tr><td><code>Biopsy</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>CTA</code></td><td><code>ncit:C202408</code></td><td></td></tr>
<tr><td><code>Colonoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colposcopy</code></td><td><code>ncit:C16451</code></td><td></td></tr>
<tr><td><code>Fine-Needle Aspiration</code></td><td><code>ncit:C15361</code></td><td></td></tr>
<tr><td><code>Imaging, NOS</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>Incisional Biopsy</code></td><td><code>ncit:C15386</code></td><td></td></tr>
<tr><td><code>MRA</code></td><td><code>ncit:C114867</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Mammogram</code></td><td><code>ncit:C20178</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Oral Brush Biopsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>PET-MRI</code></td><td><code>ncit:C103514</code></td><td></td></tr>
<tr><td><code>Palpation</code></td><td><code>ncit:C16950</code></td><td></td></tr>
<tr><td><code>Physical Examination</code></td><td><code>ncit:C20989</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>Upper endoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X-Ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Research/Retrospective</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>ACTH-producing tumor</code></td><td><code>icdo:8158/3</code></td><td></td></tr>
<tr><td><code>ALK positive large B-cell lymphoma</code></td><td><code>icdo:9737/3</code></td><td></td></tr>
<tr><td><code>Ac. myelomonocytic leuk. w abn. mar. eosinophils</code></td><td><code>icdo:9871/3</code></td><td></td></tr>
<tr><td><code>Acidophil adenoma</code></td><td><code>icdo:8280/0</code></td><td></td></tr>
<tr><td><code>Acidophil carcinoma</code></td><td><code>icdo:8280/3</code></td><td></td></tr>
<tr><td><code>Acinar cell carcinoma</code></td><td><code>icdo:8550/3</code></td><td></td></tr>
<tr><td><code>Acinar cell cystadenocarcinoma</code></td><td><code>icdo:8551/3</code></td><td></td></tr>
<tr><td><code>Acral lentiginous melanoma, malig.</code></td><td><code>icdo:8744/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Acute basophilic leukemia</code></td><td><code>icdo:9870/3</code></td><td></td></tr>
<tr><td><code>Acute biphenotypic leukemia</code></td><td><code>icdo:9805/3</code></td><td></td></tr>
<tr><td><code>Acute leukemia, NOS</code></td><td><code>icdo:9801/3</code></td><td></td></tr>
<tr><td><code>Acute lymphoblastic leukemia, L2 type, NOS</code></td><td><code>icdo:9828/3</code></td><td></td></tr>
<tr><td><code>Acute megakaryoblastic leukemia</code></td><td><code>icdo:9910/3</code></td><td></td></tr>
<tr><td><code>Acute monocytic leukemia</code></td><td><code>icdo:9891/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leuk. with multilineage dysplasia</code></td><td><code>icdo:9895/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia (megakaryoblastic) with</code></td><td><code>icdo:9911/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with BCR-ABL1</code></td><td><code>icdo:9912/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with biallelic mutations of CEBPA</code></td><td><code>icdo:9878/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with inv(3)(q21q26.2) or</code></td><td><code>icdo:9869/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with maturation</code></td><td><code>icdo:9874/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with mutated NPM1</code></td><td><code>icdo:9877/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with mutated RUNX1</code></td><td><code>icdo:9879/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia with t(6;9)(p23;q34) DEK-NUP214</code></td><td><code>icdo:9865/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia without maturation</code></td><td><code>icdo:9873/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia, 11q23 abnormalities</code></td><td><code>icdo:9897/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia, M6 type</code></td><td><code>icdo:9840/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia, minimal differentiation</code></td><td><code>icdo:9872/3</code></td><td></td></tr>
<tr><td><code>Acute myeloid leukemia, t(8;21)(q22;q22)</code></td><td><code>icdo:9896/3</code></td><td></td></tr>
<tr><td><code>Acute myelomonocytic leukemia</code></td><td><code>icdo:9867/3</code></td><td></td></tr>
<tr><td><code>Acute panmyelosis with myelofibrosis</code></td><td><code>icdo:9931/3</code></td><td></td></tr>
<tr><td><code>Acute promyelocytic leuk.,t(15;17)(q22;q11-12)</code></td><td><code>icdo:9866/3</code></td><td></td></tr>
<tr><td><code>Adamantinoma of long bones</code></td><td><code>icdo:9261/3</code></td><td></td></tr>
<tr><td><code>Adamantinomatous Craniopharyngioma</code></td><td><code>ncit:C4726</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'</td></tr>
<tr><td><code>Adenocarc. in situ in mult. adenomatous polyps</code></td><td><code>icdo:8221/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoid tumor</code></td><td><code>icdo:8245/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in adenoma. polyposis coli</code></td><td><code>icdo:8220/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in adenomatous polyp</code></td><td><code>icdo:8210/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in mult. adenomatous polyps</code></td><td><code>icdo:8221/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ</code></td><td><code>icdo:8140/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ in adenomatous polyp</code></td><td><code>icdo:8210/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ in familial polyp. coli</code></td><td><code>icdo:8220/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ in tubulovillous adenoma</code></td><td><code>icdo:8263/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ in villous adenoma</code></td><td><code>icdo:8261/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ, mucinous</code></td><td><code>icdo:8253/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in situ, non-mucinous</code></td><td><code>icdo:8250/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in tubulovillous adenoma</code></td><td><code>icdo:8263/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma in villous adenoma</code></td><td><code>icdo:8261/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma of anal glands</code></td><td><code>icdo:8215/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma w cartilag. &amp; oss. metaplas.</code></td><td><code>icdo:8571/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma with apocrine metaplasia</code></td><td><code>icdo:8573/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma with mixed subtypes</code></td><td><code>icdo:8255/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma with neuroendocrine differen.</code></td><td><code>icdo:8574/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma with spindle cell mataplasia</code></td><td><code>icdo:8572/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma with squamous metaplasia</code></td><td><code>icdo:8570/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, HPV-associated</code></td><td><code>icdo:8483/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, HPV-independent, NOS</code></td><td><code>icdo:8484/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, NOS</code></td><td><code>icdo:8140/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, endocervical type</code></td><td><code>icdo:8384/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, intestinal type</code></td><td><code>icdo:8144/3</code></td><td></td></tr>
<tr><td><code>Adenoid basal cell carcinoma</code></td><td><code>icdo:8098/3</code></td><td></td></tr>
<tr><td><code>Adenoid cystic carcinoma</code></td><td><code>icdo:8200/3</code></td><td></td></tr>
<tr><td><code>Adenoma, NOS</code></td><td><code>icdo:8140/0</code></td><td></td></tr>
<tr><td><code>Adenomyoepithelioma with carcinoma</code></td><td><code>icdo:8983/3</code></td><td></td></tr>
<tr><td><code>Adenosarcoma</code></td><td><code>icdo:8933/3</code></td><td></td></tr>
<tr><td><code>Adenosquamous carcinoma</code></td><td><code>icdo:8560/3</code></td><td></td></tr>
<tr><td><code>Adult T-cell leukemia/lymphoma (HTLV-1 pos.)</code></td><td><code>icdo:9827/3</code></td><td></td></tr>
<tr><td><code>Aggressive NK-cell leukemia</code></td><td><code>icdo:9948/3</code></td><td></td></tr>
<tr><td><code>Alveolar adenocarcinoma</code></td><td><code>icdo:8251/3</code></td><td></td></tr>
<tr><td><code>Alveolar rhabdomyosarcoma</code></td><td><code>icdo:8920/3</code></td><td></td></tr>
<tr><td><code>Alveolar soft part sarcoma</code></td><td><code>icdo:9581/3</code></td><td></td></tr>
<tr><td><code>Amelanotic melanoma</code></td><td><code>icdo:8730/3</code></td><td></td></tr>
<tr><td><code>Ameloblastic fibrosarcoma</code></td><td><code>icdo:9330/3</code></td><td></td></tr>
<tr><td><code>Ameloblastic odontosarcoma</code></td><td><code>icdo:9290/3</code></td><td></td></tr>
<tr><td><code>Ameloblastoma, malignant</code></td><td><code>icdo:9310/3</code></td><td></td></tr>
<tr><td><code>Anaplastic large cell lymphoma, ALK negative</code></td><td><code>icdo:9715/3</code></td><td></td></tr>
<tr><td><code>Anaplastic large cell lymphoma, T-cell and Null cell type</code></td><td><code>icdo:9714/3</code></td><td></td></tr>
<tr><td><code>Androblastoma, malignant</code></td><td><code>icdo:8630/3</code></td><td></td></tr>
<tr><td><code>Angioimmunoblastic T-cell lymphoma</code></td><td><code>icdo:9705/3</code></td><td></td></tr>
<tr><td><code>Angiolipoma, NOS</code></td><td><code>icdo:8861/0</code></td><td></td></tr>
<tr><td><code>Angiomatous meningioma</code></td><td><code>icdo:9534/0</code></td><td></td></tr>
<tr><td><code>Angiomyosarcoma</code></td><td><code>icdo:8894/3</code></td><td></td></tr>
<tr><td><code>Aortic body tumor, malignant</code></td><td><code>icdo:8691/3</code></td><td></td></tr>
<tr><td><code>Apocrine adenocarcinoma</code></td><td><code>icdo:8401/3</code></td><td></td></tr>
<tr><td><code>Askin tumor</code></td><td><code>icdo:9365/3</code></td><td></td></tr>
<tr><td><code>Astroblastoma</code></td><td><code>icdo:9430/3</code></td><td></td></tr>
<tr><td><code>Astrocytoma, NOS</code></td><td><code>icdo:9400/3</code></td><td></td></tr>
<tr><td><code>Astrocytoma, anaplastic</code></td><td><code>icdo:9401/3</code></td><td></td></tr>
<tr><td><code>Atypical Choroid Plexus Papilloma</code></td><td><code>ncit:C53686</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'</td></tr>
<tr><td><code>Atypical chronic myeloid leuk., BCR/ABL negative</code></td><td><code>icdo:9876/3</code></td><td></td></tr>
<tr><td><code>Atypical lipoma</code></td><td><code>icdo:8850/1</code></td><td></td></tr>
<tr><td><code>Atypical medullary carcinoma</code></td><td><code>icdo:8513/3</code></td><td></td></tr>
<tr><td><code>Atypical meningioma</code></td><td><code>icdo:9539/1</code></td><td></td></tr>
<tr><td><code>Atypical teratoid/rhabdoid tumor</code></td><td><code>icdo:9508/3</code></td><td></td></tr>
<tr><td><code>B lymphblastic leukemia/lymphoma with t(5;14)(q31;q32);IL3-IGH</code></td><td><code>icdo:9817/3</code></td><td></td></tr>
<tr><td><code>B lymphoblastic leukemia/lymphoma with hyperdiploidy</code></td><td><code>icdo:9815/3</code></td><td></td></tr>
<tr><td><code>B lymphoblastic leukemia/lymphoma, NOS</code></td><td><code>icdo:9811/3</code></td><td></td></tr>
<tr><td><code>B-lymphocytic leukemia/lymphoma, BCR-ABL1-like</code></td><td><code>icdo:9819/3</code></td><td></td></tr>
<tr><td><code>Balloon cell melanoma</code></td><td><code>icdo:8722/3</code></td><td></td></tr>
<tr><td><code>Basal cell adenocarcinoma</code></td><td><code>icdo:8147/3</code></td><td></td></tr>
<tr><td><code>Basal cell carcinoma, NOS</code></td><td><code>icdo:8090/3</code></td><td></td></tr>
<tr><td><code>Basal cell carcinoma, fibroepithelial</code></td><td><code>icdo:8093/3</code></td><td></td></tr>
<tr><td><code>Basal cell carcinoma, nodular</code></td><td><code>icdo:8097/3</code></td><td></td></tr>
<tr><td><code>Basaloid carcinoma</code></td><td><code>icdo:8123/3</code></td><td></td></tr>
<tr><td><code>Basaloid squamous cell carcinoma</code></td><td><code>icdo:8083/3</code></td><td></td></tr>
<tr><td><code>Basophil adenoma</code></td><td><code>icdo:8300/0</code></td><td></td></tr>
<tr><td><code>Basophil carcinoma</code></td><td><code>icdo:8300/3</code></td><td></td></tr>
<tr><td><code>Basosquamous carcinoma</code></td><td><code>icdo:8094/3</code></td><td></td></tr>
<tr><td><code>Bile duct cystadenocarcinoma</code></td><td><code>icdo:8161/3</code></td><td></td></tr>
<tr><td><code>Biphenotypic sinonasal sarcoma</code></td><td><code>icdo:9045/3</code></td><td></td></tr>
<tr><td><code>Blue nevus, malignant</code></td><td><code>icdo:8780/3</code></td><td></td></tr>
<tr><td><code>Bowen disease</code></td><td><code>icdo:8081/2</code></td><td></td></tr>
<tr><td><code>Brenner tumor, malignant</code></td><td><code>icdo:9000/3</code></td><td></td></tr>
<tr><td><code>Bronchiolo-alveolar carcinoma, non-mucinous</code></td><td><code>icdo:8252/3</code></td><td></td></tr>
<tr><td><code>Burkitt cell leukemia</code></td><td><code>icdo:9826/3</code></td><td></td></tr>
<tr><td><code>Burkitt lymphoma, NOS</code></td><td><code>icdo:9687/3</code></td><td></td></tr>
<tr><td><code>CIC-rearranged sarcoma</code></td><td><code>icdo:9367/3</code></td><td></td></tr>
<tr><td><code>Capillary hemangioma</code></td><td><code>icdo:9131/0</code></td><td></td></tr>
<tr><td><code>Carcinoid tumor, malignant</code></td><td><code>icdo:8240/3</code></td><td></td></tr>
<tr><td><code>Carcinoma in pleomorphic adenoma</code></td><td><code>icdo:8941/3</code></td><td></td></tr>
<tr><td><code>Carcinoma showing thymus-like element</code></td><td><code>icdo:8589/3</code></td><td></td></tr>
<tr><td><code>Carcinoma simplex</code></td><td><code>icdo:8231/3</code></td><td></td></tr>
<tr><td><code>Carcinoma with osteoclast-like giant cells</code></td><td><code>icdo:8035/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, NOS</code></td><td><code>icdo:8010/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, anaplastic type, NOS</code></td><td><code>icdo:8021/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, diffuse type</code></td><td><code>icdo:8145/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, undifferentiated type, NOS</code></td><td><code>icdo:8020/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma, NOS</code></td><td><code>icdo:8980/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma, embryonal type</code></td><td><code>icdo:8981/3</code></td><td></td></tr>
<tr><td><code>Carotid body tumor, malignant</code></td><td><code>icdo:8692/3</code></td><td></td></tr>
<tr><td><code>Cavernous hemangioma</code></td><td><code>icdo:9121/0</code></td><td></td></tr>
<tr><td><code>Central osteosarcoma</code></td><td><code>icdo:9186/3</code></td><td></td></tr>
<tr><td><code>Centrol neurocytoma</code></td><td><code>icdo:9506/1</code></td><td></td></tr>
<tr><td><code>Cerebellar sarcoma, NOS</code></td><td><code>icdo:9480/3</code></td><td></td></tr>
<tr><td><code>Ceruminous adenocarcinoma</code></td><td><code>icdo:8420/3</code></td><td></td></tr>
<tr><td><code>Cholangiocarcinoma</code></td><td><code>icdo:8160/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Chondroblastic osteosarcoma</code></td><td><code>icdo:9181/3</code></td><td></td></tr>
<tr><td><code>Chondroblastoma, malignant</code></td><td><code>icdo:9230/3</code></td><td></td></tr>
<tr><td><code>Chondroid chordoma</code></td><td><code>icdo:9371/3</code></td><td></td></tr>
<tr><td><code>Chondrosarcoma, NOS</code></td><td><code>icdo:9220/3</code></td><td></td></tr>
<tr><td><code>Chordoid glioma</code></td><td><code>icdo:9444/1</code></td><td></td></tr>
<tr><td><code>Chordoma, NOS</code></td><td><code>icdo:9370/3</code></td><td></td></tr>
<tr><td><code>Choriocarcinoma</code></td><td><code>ncit:C2948</code></td><td></td></tr>
<tr><td><code>Choriocarcinoma combined w/ other germ cell elements</code></td><td><code>icdo:9101/3</code></td><td></td></tr>
<tr><td><code>Choroid plexus papilloma, NOS</code></td><td><code>icdo:9390/0</code></td><td></td></tr>
<tr><td><code>Choroid plexus papilloma, malignant</code></td><td><code>icdo:9390/3</code></td><td></td></tr>
<tr><td><code>Chromophobe adenoma</code></td><td><code>icdo:8270/0</code></td><td></td></tr>
<tr><td><code>Chromophobe carcinoma</code></td><td><code>icdo:8270/3</code></td><td></td></tr>
<tr><td><code>Chronic lymphocytic leukemia/small lymphocytic lymphoma</code></td><td><code>icdo:9823/3</code></td><td></td></tr>
<tr><td><code>Chronic myelogenous leukemia, BCR/ABL positive</code></td><td><code>icdo:9875/3</code></td><td></td></tr>
<tr><td><code>Chronic myeloid leukemia, NOS</code></td><td><code>icdo:9863/3</code></td><td></td></tr>
<tr><td><code>Chronic myelomonocytic leukemia, NOS</code></td><td><code>icdo:9945/3</code></td><td></td></tr>
<tr><td><code>Chronic myeloproliferative disease, NOS</code></td><td><code>icdo:9960/3</code></td><td></td></tr>
<tr><td><code>Chronic neutrophilic leukemia</code></td><td><code>icdo:9963/3</code></td><td></td></tr>
<tr><td><code>Clear cell adenocarcinofibroma</code></td><td><code>icdo:8313/3</code></td><td></td></tr>
<tr><td><code>Clear cell adenocarcinoma, NOS</code></td><td><code>icdo:8310/3</code></td><td></td></tr>
<tr><td><code>Clear cell adenoma</code></td><td><code>icdo:8310/0</code></td><td></td></tr>
<tr><td><code>Clear cell chondrosarcoma</code></td><td><code>icdo:9242/3</code></td><td></td></tr>
<tr><td><code>Clear cell meningioma</code></td><td><code>icdo:9538/1</code></td><td></td></tr>
<tr><td><code>Clear cell odontogenic carcinoma</code></td><td><code>icdo:9341/3</code></td><td></td></tr>
<tr><td><code>Clear cell sarcoma of kidney</code></td><td><code>icdo:8964/3</code></td><td></td></tr>
<tr><td><code>Clear cell sarcoma, NOS</code></td><td><code>icdo:9044/3</code></td><td></td></tr>
<tr><td><code>Clear cell tumor, NOS</code></td><td><code>icdo:8005/0</code></td><td></td></tr>
<tr><td><code>Cloacogenic carcinoma</code></td><td><code>icdo:8124/3</code></td><td></td></tr>
<tr><td><code>Comb. hepatocel. carcinoma &amp; cholangiocarcinoma</code></td><td><code>icdo:8180/3</code></td><td></td></tr>
<tr><td><code>Combined small cell carcinoma</code></td><td><code>icdo:8045/3</code></td><td></td></tr>
<tr><td><code>Comedocarcinoma, NOS</code></td><td><code>icdo:8501/3</code></td><td></td></tr>
<tr><td><code>Comedocarcinoma, non-infiltrating</code></td><td><code>icdo:8501/2</code></td><td></td></tr>
<tr><td><code>Composite Hodgkin and non-Hodgkin lymphoma</code></td><td><code>icdo:9596/3</code></td><td></td></tr>
<tr><td><code>Composite carcinoid</code></td><td><code>icdo:8244/3</code></td><td></td></tr>
<tr><td><code>Craniopharyngioma</code></td><td><code>icdo:9350/1</code></td><td></td></tr>
<tr><td><code>Cribriform carcinoma</code></td><td><code>icdo:8201/3</code></td><td></td></tr>
<tr><td><code>Cribriform carcinoma in situ</code></td><td><code>icdo:8201/2</code></td><td></td></tr>
<tr><td><code>Cutaneous T-cell lymphoma, NOS</code></td><td><code>icdo:9709/3</code></td><td></td></tr>
<tr><td><code>Cyst-associated renal cell carcinoma</code></td><td><code>icdo:8316/3</code></td><td></td></tr>
<tr><td><code>Cystadenocarcinoma, NOS</code></td><td><code>icdo:8440/3</code></td><td></td></tr>
<tr><td><code>Cystic hypersecretory carcinoma</code></td><td><code>icdo:8508/3</code></td><td></td></tr>
<tr><td><code>Dedifferentiated Liposarcoma</code></td><td><code>ncit:C3704</code></td><td></td></tr>
<tr><td><code>Dedifferentiated chondrosarcoma</code></td><td><code>icdo:9243/3</code></td><td></td></tr>
<tr><td><code>Dedifferentiated chordoma</code></td><td><code>icdo:9372/3</code></td><td></td></tr>
<tr><td><code>Dermatofibrosarcoma, NOS</code></td><td><code>icdo:8832/3</code></td><td></td></tr>
<tr><td><code>Dermoid cyst, NOS</code></td><td><code>icdo:9084/0</code></td><td></td></tr>
<tr><td><code>Desmoplastic infantile astrocytoma</code></td><td><code>icdo:9412/1</code></td><td></td></tr>
<tr><td><code>Desmoplastic medulloblastoma</code></td><td><code>icdo:9471/3</code></td><td></td></tr>
<tr><td><code>Desmoplastic melanoma, malignant</code></td><td><code>icdo:8745/3</code></td><td></td></tr>
<tr><td><code>Desmoplastic Small Round Cell Tumor</code></td><td><code>icdo:8806/3</code></td><td></td></tr>
<tr><td><code>Diffuse Leptomeningeal Glioneuronal Tumor</code></td><td><code>icdo:9509/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Diffuse melanocytosis</code></td><td><code>icdo:8728/0</code></td><td></td></tr>
<tr><td><code>Diffuse midline glioma, H3 K27M-mutant</code></td><td><code>icdo:9385/3</code></td><td></td></tr>
<tr><td><code>Duct carcinoma in situ, solid type</code></td><td><code>icdo:8230/2</code></td><td></td></tr>
<tr><td><code>Duct carcinoma, desmoplastic type</code></td><td><code>icdo:8514/3</code></td><td></td></tr>
<tr><td><code>Dysembryoplastic Neuroepithelial Tumor</code></td><td><code>icdo:9413/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Dysgerminoma</code></td><td><code>icdo:9060/3</code></td><td></td></tr>
<tr><td><code>Dysplastic gangliocytoma of cerebellum (Lhermitte-Duclos)</code></td><td><code>icdo:9493/0</code></td><td></td></tr>
<tr><td><code>Eccrine adenocarcinoma</code></td><td><code>icdo:8413/3</code></td><td></td></tr>
<tr><td><code>Eccrine papillary adenocarcinoma</code></td><td><code>icdo:8408/3</code></td><td></td></tr>
<tr><td><code>Eccrine poroma, malignant</code></td><td><code>icdo:8409/3</code></td><td></td></tr>
<tr><td><code>Embryonal carcinoma, NOS</code></td><td><code>icdo:9070/3</code></td><td></td></tr>
<tr><td><code>Embryonal rhabdomyosarcoma</code></td><td><code>icdo:8910/3</code></td><td></td></tr>
<tr><td><code>Embryonal sarcoma</code></td><td><code>icdo:8991/3</code></td><td></td></tr>
<tr><td><code>Embryonal tumor with multilayered rosettes, NOS</code></td><td><code>icdo:9478/3</code></td><td></td></tr>
<tr><td><code>Endometrial stromal sarcoma</code></td><td><code>icdo:8930/3</code></td><td></td></tr>
<tr><td><code>Endometrial stromal sarcoma, low grade</code></td><td><code>icdo:8931/3</code></td><td></td></tr>
<tr><td><code>Endometrioid adenocarcinoma, ciliated cell variant</code></td><td><code>icdo:8383/3</code></td><td></td></tr>
<tr><td><code>Endometrioid adenocarcinoma, secretory variant</code></td><td><code>icdo:8382/3</code></td><td></td></tr>
<tr><td><code>Endometrioid adenofibroma, malignant</code></td><td><code>icdo:8381/3</code></td><td></td></tr>
<tr><td><code>Endometrioid carcinoma</code></td><td><code>icdo:8380/3</code></td><td></td></tr>
<tr><td><code>Endometrioid intraepithelial neoplasia</code></td><td><code>icdo:8380/2</code></td><td></td></tr>
<tr><td><code>Enterochromaffin cell carcinoid</code></td><td><code>icdo:8241/3</code></td><td></td></tr>
<tr><td><code>Enterochromaffin-like cell tumor, malignant</code></td><td><code>icdo:8242/3</code></td><td></td></tr>
<tr><td><code>Enteroglucagonoma, malignant</code></td><td><code>icdo:8157/3</code></td><td></td></tr>
<tr><td><code>Ependymoma, RELA fusion-positive</code></td><td><code>icdo:9396/3</code></td><td></td></tr>
<tr><td><code>Ependymoma, anaplastic</code></td><td><code>icdo:9392/3</code></td><td></td></tr>
<tr><td><code>Epithel. mesothelioma, mal.</code></td><td><code>icdo:9052/3</code></td><td></td></tr>
<tr><td><code>Epithelial tumor, benign</code></td><td><code>icdo:8010/0</code></td><td></td></tr>
<tr><td><code>Epithelial-myoepithelial carcinoma</code></td><td><code>icdo:8562/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>ncit:C6561</code></td><td></td></tr>
<tr><td><code>Epithelioid cell melanoma</code></td><td><code>icdo:8771/3</code></td><td></td></tr>
<tr><td><code>Epithelioid hemangioendothelioma, malignant</code></td><td><code>icdo:9133/3</code></td><td></td></tr>
<tr><td><code>Epithelioid leiomyosarcoma</code></td><td><code>icdo:8891/3</code></td><td></td></tr>
<tr><td><code>Epithelioma, malignant</code></td><td><code>icdo:8011/3</code></td><td></td></tr>
<tr><td><code>Erdheim-Chester Disease</code></td><td><code>icdo:9749/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Essential thrombocythemia</code></td><td><code>icdo:9962/3</code></td><td></td></tr>
<tr><td><code>Ewing Sarcoma</code></td><td><code>icdo:9260/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Extra-adrenal paraganglioma, malignant</code></td><td><code>icdo:8693/3</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia</code></td><td><code>ncit:C62505</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia Neurological Syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fascial fibrosarcoma</code></td><td><code>icdo:8813/3</code></td><td></td></tr>
<tr><td><code>Fetal adenocarcinoma</code></td><td><code>icdo:8333/3</code></td><td></td></tr>
<tr><td><code>Fibrillary astrocytoma</code></td><td><code>icdo:9420/3</code></td><td></td></tr>
<tr><td><code>Fibroblastic Osteosarcoma</code></td><td><code>ncit:C4020</code></td><td></td></tr>
<tr><td><code>Fibroblastic liposarcoma</code></td><td><code>icdo:8857/3</code></td><td></td></tr>
<tr><td><code>Fibroblastic reticular cell tumor</code></td><td><code>icdo:9759/3</code></td><td></td></tr>
<tr><td><code>Fibrolipoma</code></td><td><code>icdo:8851/0</code></td><td></td></tr>
<tr><td><code>Fibroma, NOS</code></td><td><code>icdo:8810/0</code></td><td></td></tr>
<tr><td><code>Fibromyxosarcoma</code></td><td><code>icdo:8811/3</code></td><td></td></tr>
<tr><td><code>Fibrosarcoma, NOS</code></td><td><code>icdo:8810/3</code></td><td></td></tr>
<tr><td><code>Fibrous histiocytoma, malignant</code></td><td><code>icdo:8830/3</code></td><td></td></tr>
<tr><td><code>Fibrous meningioma</code></td><td><code>icdo:9532/0</code></td><td></td></tr>
<tr><td><code>Fibrous mesothelioma, malignant</code></td><td><code>icdo:9051/3</code></td><td></td></tr>
<tr><td><code>Follicular adenocarcinoma trabecular</code></td><td><code>icdo:8332/3</code></td><td></td></tr>
<tr><td><code>Follicular adenocarcinoma well diff.</code></td><td><code>icdo:8331/3</code></td><td></td></tr>
<tr><td><code>Follicular adenocarcinoma, NOS</code></td><td><code>icdo:8330/3</code></td><td></td></tr>
<tr><td><code>Follicular carcinoma, minimally invasive</code></td><td><code>icdo:8335/3</code></td><td></td></tr>
<tr><td><code>Follicular dendritic cell sarcoma</code></td><td><code>icdo:9758/3</code></td><td></td></tr>
<tr><td><code>Follicular lymphoma, NOS</code></td><td><code>icdo:9690/3</code></td><td></td></tr>
<tr><td><code>Follicular lymphoma, grade 1</code></td><td><code>icdo:9695/3</code></td><td></td></tr>
<tr><td><code>Follicular lymphoma, grade 2</code></td><td><code>icdo:9691/3</code></td><td></td></tr>
<tr><td><code>Follicular lymphoma, grade 3</code></td><td><code>icdo:9698/3</code></td><td></td></tr>
<tr><td><code>Follicular thyroid carcinoma (FTC), encapsulated angioinvasive</code></td><td><code>icdo:8339/3</code></td><td></td></tr>
<tr><td><code>Gangliocytoma</code></td><td><code>icdo:9492/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Ganglioglioma, NOS</code></td><td><code>icdo:9505/1</code></td><td></td></tr>
<tr><td><code>Ganglioglioma, anaplastic</code></td><td><code>icdo:9505/3</code></td><td></td></tr>
<tr><td><code>Ganglioneuroblastoma</code></td><td><code>icdo:9490/3</code></td><td></td></tr>
<tr><td><code>Ganglioneuroma</code></td><td><code>icdo:9490/0</code></td><td></td></tr>
<tr><td><code>Gastrinoma, malignant</code></td><td><code>icdo:8153/3</code></td><td></td></tr>
<tr><td><code>Gastroblastoma</code></td><td><code>icdo:8976/3</code></td><td></td></tr>
<tr><td><code>Gastrointestinal stromal sarcoma</code></td><td><code>icdo:8936/3</code></td><td></td></tr>
<tr><td><code>Gemistocytic astrocytoma</code></td><td><code>icdo:9411/3</code></td><td></td></tr>
<tr><td><code>Germ cell tumor, nonseminomatous</code></td><td><code>icdo:9065/3</code></td><td></td></tr>
<tr><td><code>Germ cell tumors with associated hematological malignancy</code></td><td><code>icdo:9086/3</code></td><td></td></tr>
<tr><td><code>Germinoma</code></td><td><code>ncit:C3753</code></td><td></td></tr>
<tr><td><code>Ghost cell odontogenic carcinoma</code></td><td><code>icdo:9302/3</code></td><td></td></tr>
<tr><td><code>Giant cell and spindle cell carcinoma</code></td><td><code>icdo:8030/3</code></td><td></td></tr>
<tr><td><code>Giant cell carcinoma</code></td><td><code>icdo:8031/3</code></td><td></td></tr>
<tr><td><code>Giant cell glioblastoma</code></td><td><code>icdo:9441/3</code></td><td></td></tr>
<tr><td><code>Giant cell sarcoma</code></td><td><code>icdo:8802/3</code></td><td></td></tr>
<tr><td><code>Giant cell tumor of bone, malignant</code></td><td><code>icdo:9250/3</code></td><td></td></tr>
<tr><td><code>Glandular intraepithelial neoplasia, grade III</code></td><td><code>icdo:8148/2</code></td><td></td></tr>
<tr><td><code>Glassy cell carcinoma</code></td><td><code>icdo:8015/3</code></td><td></td></tr>
<tr><td><code>Glioblastoma, IDH-mutant</code></td><td><code>icdo:9445/3</code></td><td></td></tr>
<tr><td><code>Glioblastoma, NOS</code></td><td><code>icdo:9440/3</code></td><td></td></tr>
<tr><td><code>Gliofibroma</code></td><td><code>icdo:9442/1</code></td><td></td></tr>
<tr><td><code>Glioma, malignant</code></td><td><code>icdo:9380/3</code></td><td></td></tr>
<tr><td><code>Gliomatosis cerebri</code></td><td><code>icdo:9381/3</code></td><td></td></tr>
<tr><td><code>Gliosarcoma</code></td><td><code>icdo:9442/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Glomangiosarcoma</code></td><td><code>icdo:8710/3</code></td><td></td></tr>
<tr><td><code>Glucagonoma, malignant</code></td><td><code>icdo:8152/3</code></td><td></td></tr>
<tr><td><code>Glycogen-rich carcinoma</code></td><td><code>icdo:8315/3</code></td><td></td></tr>
<tr><td><code>Goblet cell carcinoid</code></td><td><code>icdo:8243/3</code></td><td></td></tr>
<tr><td><code>Granular cell carcinoma</code></td><td><code>icdo:8320/3</code></td><td></td></tr>
<tr><td><code>Granular cell tumor of the sellar region</code></td><td><code>icdo:9582/0</code></td><td></td></tr>
<tr><td><code>Granular cell tumor, NOS</code></td><td><code>icdo:9580/0</code></td><td></td></tr>
<tr><td><code>Granular cell tumor, malignant</code></td><td><code>icdo:9580/3</code></td><td></td></tr>
<tr><td><code>Granulosa cell tumor, malignant</code></td><td><code>icdo:8620/3</code></td><td></td></tr>
<tr><td><code>Granulosa cell-theca cell tumor, mal.</code></td><td><code>icdo:8621/3</code></td><td></td></tr>
<tr><td><code>Gynandroblastoma, malignant</code></td><td><code>icdo:8632/3</code></td><td></td></tr>
<tr><td><code>Hairy cell leukemia</code></td><td><code>icdo:9940/3</code></td><td></td></tr>
<tr><td><code>Heavy chain disease, NOS</code></td><td><code>icdo:9762/3</code></td><td></td></tr>
<tr><td><code>Hemangioblastoma</code></td><td><code>icdo:9161/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hemangioendothelioma, NOS</code></td><td><code>icdo:9130/1</code></td><td></td></tr>
<tr><td><code>Hemangioendothelioma, benign</code></td><td><code>icdo:9130/0</code></td><td></td></tr>
<tr><td><code>Hemangioendothelioma, malignant</code></td><td><code>icdo:9130/3</code></td><td></td></tr>
<tr><td><code>Hemangioma, NOS</code></td><td><code>icdo:9120/0</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, NOS</code></td><td><code>icdo:9150/1</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, benign</code></td><td><code>icdo:9150/0</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, malignant</code></td><td><code>icdo:9150/3</code></td><td></td></tr>
<tr><td><code>Hemangiosarcoma</code></td><td><code>icdo:9120/3</code></td><td></td></tr>
<tr><td><code>Hepatoblastoma</code></td><td><code>icdo:8970/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, NOS</code></td><td><code>icdo:8170/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, clear cell type</code></td><td><code>icdo:8174/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, fibrolamellar</code></td><td><code>icdo:8171/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, pleomorphic type</code></td><td><code>icdo:8175/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, scirrhous</code></td><td><code>icdo:8172/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular carcinoma, spindle cell variant</code></td><td><code>icdo:8173/3</code></td><td></td></tr>
<tr><td><code>Hepatoid adenocarcinoma</code></td><td><code>icdo:8576/3</code></td><td></td></tr>
<tr><td><code>Hepatosplenic gamma-delta cell lymphoma</code></td><td><code>icdo:9716/3</code></td><td></td></tr>
<tr><td><code>Hereditary leiomyomatosis and RCC-associated renal cell carcinoma</code></td><td><code>icdo:8311/3</code></td><td></td></tr>
<tr><td><code>High grade appendiceal mucinous neoplasm</code></td><td><code>icdo:8480/2</code></td><td></td></tr>
<tr><td><code>High grade surface osteosarcoma</code></td><td><code>icdo:9194/3</code></td><td></td></tr>
<tr><td><code>High-grade serous carcinoma</code></td><td><code>icdo:8461/3</code></td><td></td></tr>
<tr><td><code>Histiocytic Sarcoma</code></td><td><code>ncit:C27349</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hodgkin granuloma [obs]</code></td><td><code>icdo:9661/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymph., lymphocyt. deplet., diffuse fibrosis</code></td><td><code>icdo:9654/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymph., nodular lymphocyte predom.</code></td><td><code>icdo:9659/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, NOS</code></td><td><code>icdo:9650/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, lymphocyt. deplet., reticular</code></td><td><code>icdo:9655/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, lymphocytic deplet., NOS</code></td><td><code>icdo:9653/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, mixed cellularity, NOS</code></td><td><code>icdo:9652/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, nod. scler., cellular phase</code></td><td><code>icdo:9664/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, nod. scler., grade 1</code></td><td><code>icdo:9665/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, nod. scler., grade 2</code></td><td><code>icdo:9667/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nodular Sclerosis, NOS</code></td><td><code>icdo:9663/3</code></td><td></td></tr>
<tr><td><code>Hodgkin sarcoma [obs]</code></td><td><code>icdo:9662/3</code></td><td></td></tr>
<tr><td><code>Hydroa vacciniforme-like lymphoma</code></td><td><code>icdo:9725/3</code></td><td></td></tr>
<tr><td><code>Hypereosinophilic syndrome</code></td><td><code>icdo:9964/3</code></td><td></td></tr>
<tr><td><code>Immunoproliferative disease, NOS</code></td><td><code>icdo:9760/3</code></td><td></td></tr>
<tr><td><code>Immunoproliferative small intestinal disease</code></td><td><code>icdo:9764/3</code></td><td></td></tr>
<tr><td><code>Infantile Fibrosarcoma</code></td><td><code>icdo:8814/3</code></td><td></td></tr>
<tr><td><code>Infiltr. duct mixed with other types of carcinoma</code></td><td><code>icdo:8523/3</code></td><td></td></tr>
<tr><td><code>Infiltr. duct mixed with other types of carcinoma, in situ</code></td><td><code>icdo:8523/2</code></td><td></td></tr>
<tr><td><code>Infiltrating basal cell carcinoma, NOS</code></td><td><code>icdo:8092/3</code></td><td></td></tr>
<tr><td><code>Infiltrating duct and lobular carcinoma</code></td><td><code>icdo:8522/3</code></td><td></td></tr>
<tr><td><code>Infiltrating ductular carcinoma</code></td><td><code>icdo:8521/3</code></td><td></td></tr>
<tr><td><code>Infiltrating lobular mixed with other types of carc.</code></td><td><code>icdo:8524/3</code></td><td></td></tr>
<tr><td><code>Inflammatory carcinoma</code></td><td><code>icdo:8530/3</code></td><td></td></tr>
<tr><td><code>Instrosseous well differentiated osteosarcoma</code></td><td><code>icdo:9187/3</code></td><td></td></tr>
<tr><td><code>Insular carcinoma</code></td><td><code>icdo:8337/3</code></td><td></td></tr>
<tr><td><code>Insulinoma, malignant</code></td><td><code>icdo:8151/3</code></td><td></td></tr>
<tr><td><code>Interdigitating dendritic cell sarcoma</code></td><td><code>icdo:9757/3</code></td><td></td></tr>
<tr><td><code>Intestinal T-cell lymphoma</code></td><td><code>icdo:9717/3</code></td><td></td></tr>
<tr><td><code>Intestinal-type adenoma, high grade</code></td><td><code>icdo:8144/2</code></td><td></td></tr>
<tr><td><code>Intimal Sarcoma</code></td><td><code>icdo:9137/3</code></td><td></td></tr>
<tr><td><code>Intracortical osteosarcoma</code></td><td><code>icdo:9195/3</code></td><td></td></tr>
<tr><td><code>Intracystic carcinoma, NOS</code></td><td><code>icdo:8504/3</code></td><td></td></tr>
<tr><td><code>Intraductal and lobular in situ carcinoma</code></td><td><code>icdo:8522/2</code></td><td></td></tr>
<tr><td><code>Intraductal carcinoma, noninfiltrating, NOS</code></td><td><code>icdo:8500/2</code></td><td></td></tr>
<tr><td><code>Intraductal micropapillary carcinoma</code></td><td><code>icdo:8507/2</code></td><td></td></tr>
<tr><td><code>Intraductal oncocytic papillary neoplasm, NOS</code></td><td><code>icdo:8455/2</code></td><td></td></tr>
<tr><td><code>Intraductal oncocytic papillary neoplasms with associated invasive</code></td><td><code>icdo:8455/3</code></td><td></td></tr>
<tr><td><code>Intraductal papillary adenocarcinoma with invasion</code></td><td><code>icdo:8503/3</code></td><td></td></tr>
<tr><td><code>Intraductal papillary-mucinous carcinoma, invasive</code></td><td><code>icdo:8453/3</code></td><td></td></tr>
<tr><td><code>Intraductal papillary-mucinous carcinoma, non-inv.</code></td><td><code>icdo:8453/2</code></td><td></td></tr>
<tr><td><code>Intratubular malignant germ cells</code></td><td><code>icdo:9064/2</code></td><td></td></tr>
<tr><td><code>Intravascular Large B-Cell Lymphoma</code></td><td><code>icdo:9712/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Invasive micropapillary carcinoma</code></td><td><code>icdo:8507/3</code></td><td></td></tr>
<tr><td><code>Invasive mucinous adenocarcinoma</code></td><td><code>icdo:8253/3</code></td><td></td></tr>
<tr><td><code>Islet cell carcinoma</code></td><td><code>icdo:8150/3</code></td><td></td></tr>
<tr><td><code>Juvenile Xanthogranuloma</code></td><td><code>icdo:9749/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Juvenile myelomonocytic leukemia</code></td><td><code>icdo:9946/3</code></td><td></td></tr>
<tr><td><code>Juxtacortical chondrosarcoma</code></td><td><code>icdo:9221/3</code></td><td></td></tr>
<tr><td><code>Kaposi Sarcoma</code></td><td><code>icdo:9140/3</code></td><td></td></tr>
<tr><td><code>Klatskin tumor</code></td><td><code>icdo:8162/3</code></td><td></td></tr>
<tr><td><code>Kupffer cell sarcoma</code></td><td><code>icdo:9124/3</code></td><td></td></tr>
<tr><td><code>Langerhans cell histiocytosis, NOS</code></td><td><code>icdo:9751/3</code></td><td></td></tr>
<tr><td><code>Langerhans cell histiocytosis, disseminated</code></td><td><code>icdo:9754/3</code></td><td></td></tr>
<tr><td><code>Langerhans cell sarcoma</code></td><td><code>icdo:9756/3</code></td><td></td></tr>
<tr><td><code>Large cell carcinoma with rhabdoid phenotype</code></td><td><code>icdo:8014/3</code></td><td></td></tr>
<tr><td><code>Large cell carcinoma, NOS</code></td><td><code>icdo:8012/3</code></td><td></td></tr>
<tr><td><code>Large cell medulloblastoma</code></td><td><code>icdo:9474/3</code></td><td></td></tr>
<tr><td><code>Large cell neuroendocrine carcinoma</code></td><td><code>icdo:8013/3</code></td><td></td></tr>
<tr><td><code>Leiomyoma, NOS</code></td><td><code>icdo:8890/0</code></td><td></td></tr>
<tr><td><code>Leiomyomatosis, nOS</code></td><td><code>icdo:8890/1</code></td><td></td></tr>
<tr><td><code>Leiomyosarcoma, NOS</code></td><td><code>icdo:8890/3</code></td><td></td></tr>
<tr><td><code>Lentigo maligna</code></td><td><code>icdo:8742/2</code></td><td></td></tr>
<tr><td><code>Lentigo maligna melanoma</code></td><td><code>icdo:8742/3</code></td><td></td></tr>
<tr><td><code>Lepidic adenocarcinoma</code></td><td><code>icdo:8250/3</code></td><td></td></tr>
<tr><td><code>Leukemia, NOS</code></td><td><code>icdo:9800/3</code></td><td></td></tr>
<tr><td><code>Leukemia/lymphoma with hypodiploidy (hypodiploid ALL)</code></td><td><code>icdo:9816/3</code></td><td></td></tr>
<tr><td><code>Leukemia/lymphoma with t(12;21)(p13;q22);TEL-AML1(ETV6-RUNX1)</code></td><td><code>icdo:9814/3</code></td><td></td></tr>
<tr><td><code>Leukemia/lymphoma with t(1;19)(q23;p13.3); E2A PBX1 (TCF3 PBX1)</code></td><td><code>icdo:9818/3</code></td><td></td></tr>
<tr><td><code>Leukemia/lymphoma with t(9;22)(q34;q11.2);BCR-ABL1</code></td><td><code>icdo:9812/3</code></td><td></td></tr>
<tr><td><code>Leukemia/lymphoma with t(v;11q23);MLL rearranged</code></td><td><code>icdo:9813/3</code></td><td></td></tr>
<tr><td><code>Leydig cell tumor, malignant</code></td><td><code>icdo:8650/3</code></td><td></td></tr>
<tr><td><code>Linitis plastica</code></td><td><code>icdo:8142/3</code></td><td></td></tr>
<tr><td><code>Lipid-rich carcinoma</code></td><td><code>icdo:8314/3</code></td><td></td></tr>
<tr><td><code>Lipoma, NOS</code></td><td><code>icdo:8850/0</code></td><td></td></tr>
<tr><td><code>Liposarcoma, NOS</code></td><td><code>ncit:C3194</code></td><td></td></tr>
<tr><td><code>Liposarcoma, well differentiated</code></td><td><code>icdo:8851/3</code></td><td></td></tr>
<tr><td><code>Lobular carcinoma in situ</code></td><td><code>icdo:8520/2</code></td><td></td></tr>
<tr><td><code>Lobular carcinoma, NOS</code></td><td><code>icdo:8520/3</code></td><td></td></tr>
<tr><td><code>Low-grade serous carcinoma</code></td><td><code>icdo:8460/3</code></td><td></td></tr>
<tr><td><code>Lrg B-cell lymphoma in HHV8-assoc. multicentric Castleman DZ</code></td><td><code>icdo:9738/3</code></td><td></td></tr>
<tr><td><code>Lymphangioleiomyomatosis</code></td><td><code>icdo:9174/3</code></td><td></td></tr>
<tr><td><code>Lymphangiosarcoma</code></td><td><code>icdo:9170/3</code></td><td></td></tr>
<tr><td><code>Lymphoepithelial carcinoma</code></td><td><code>icdo:8082/3</code></td><td></td></tr>
<tr><td><code>Lymphoid leukemia, NOS</code></td><td><code>icdo:9820/3</code></td><td></td></tr>
<tr><td><code>Lymphoma, NOS</code></td><td><code>icdo:9590/3</code></td><td></td></tr>
<tr><td><code>Lymphomatoid granulomatosis, grade 3</code></td><td><code>icdo:9766/3</code></td><td></td></tr>
<tr><td><code>ML, large B-cell, diffuse</code></td><td><code>icdo:9680/3</code></td><td></td></tr>
<tr><td><code>ML, large B-cell, diffuse, immunoblastic, NOS</code></td><td><code>icdo:9684/3</code></td><td></td></tr>
<tr><td><code>ML, lymphoplasmacytic</code></td><td><code>icdo:9671/3</code></td><td></td></tr>
<tr><td><code>ML, mixed sm. and lg. cell, diffuse</code></td><td><code>icdo:9675/3</code></td><td></td></tr>
<tr><td><code>ML, small B lymphocytic, NOS</code></td><td><code>icdo:9670/3</code></td><td></td></tr>
<tr><td><code>MPNST with rhabdomyoblastic differentiation</code></td><td><code>icdo:9561/3</code></td><td></td></tr>
<tr><td><code>Mal. melanoma in giant pigmented nevus</code></td><td><code>icdo:8761/3</code></td><td></td></tr>
<tr><td><code>Mal. melanoma in junctional nevus</code></td><td><code>icdo:8740/3</code></td><td></td></tr>
<tr><td><code>Mal. melanoma in precan. melanosis</code></td><td><code>icdo:8741/3</code></td><td></td></tr>
<tr><td><code>Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>icdo:9540/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Malignant cystic nephroma</code></td><td><code>icdo:8959/3</code></td><td></td></tr>
<tr><td><code>Malignant eccrine spiradenoma</code></td><td><code>icdo:8403/3</code></td><td></td></tr>
<tr><td><code>Malignant giant cell tumor of soft parts</code></td><td><code>icdo:9251/3</code></td><td></td></tr>
<tr><td><code>Malignant histiocytosis</code></td><td><code>icdo:9750/3</code></td><td></td></tr>
<tr><td><code>Malignant lymphoma, NOS</code></td><td><code>icdo:9590/3</code></td><td></td></tr>
<tr><td><code>Malignant lymphoma, non-Hodgkin</code></td><td><code>icdo:9591/3</code></td><td></td></tr>
<tr><td><code>Malignant mastocytosis</code></td><td><code>icdo:9741/3</code></td><td></td></tr>
<tr><td><code>Malignant melanoma, NOS</code></td><td><code>icdo:8720/3</code></td><td></td></tr>
<tr><td><code>Malignant melanoma, regressing</code></td><td><code>icdo:8723/3</code></td><td></td></tr>
<tr><td><code>Malignant myoepithelioma</code></td><td><code>icdo:8982/3</code></td><td></td></tr>
<tr><td><code>Malignant placental site trophoblastic tumor</code></td><td><code>icdo:9104/3</code></td><td></td></tr>
<tr><td><code>Malignant rhabdoid tumor</code></td><td><code>icdo:8963/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Malignant tenosynovial giant cell tumor</code></td><td><code>icdo:9252/3</code></td><td></td></tr>
<tr><td><code>Malignant teratoma, intermediate</code></td><td><code>icdo:9083/3</code></td><td></td></tr>
<tr><td><code>Malignant teratoma, trophoblastic</code></td><td><code>icdo:9102/3</code></td><td></td></tr>
<tr><td><code>Malignant teratoma, undiff.</code></td><td><code>icdo:9082/3</code></td><td></td></tr>
<tr><td><code>Malignant tumor, clear cell type</code></td><td><code>icdo:8005/3</code></td><td></td></tr>
<tr><td><code>Malignant tumor, giant cell type</code></td><td><code>icdo:8003/3</code></td><td></td></tr>
<tr><td><code>Malignant tumor, small cell type</code></td><td><code>icdo:8002/3</code></td><td></td></tr>
<tr><td><code>Malignant tumor, spindle cell type</code></td><td><code>icdo:8004/3</code></td><td></td></tr>
<tr><td><code>Mantle cell lymphoma</code></td><td><code>icdo:9673/3</code></td><td></td></tr>
<tr><td><code>Marginal zone B-cell lymphoma, NOS</code></td><td><code>icdo:9699/3</code></td><td></td></tr>
<tr><td><code>Mast cell leukemia</code></td><td><code>icdo:9742/3</code></td><td></td></tr>
<tr><td><code>Mast cell sarcoma</code></td><td><code>icdo:9740/3</code></td><td></td></tr>
<tr><td><code>Mature T-cell lymphoma, NOS</code></td><td><code>icdo:9702/3</code></td><td></td></tr>
<tr><td><code>Mediastinal large B-cell lymphoma</code></td><td><code>icdo:9679/3</code></td><td></td></tr>
<tr><td><code>Medullary carcinoma with amyloid stroma</code></td><td><code>icdo:8345/3</code></td><td></td></tr>
<tr><td><code>Medullary carcinoma with lymphoid stroma</code></td><td><code>icdo:8512/3</code></td><td></td></tr>
<tr><td><code>Medullary carcinoma, NOS</code></td><td><code>icdo:8510/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, NOS</code></td><td><code>icdo:9470/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, SHH-activated and TP53-mutant</code></td><td><code>icdo:9476/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, WNT-activated</code></td><td><code>icdo:9475/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, non-WNT/non-SHH</code></td><td><code>icdo:9477/3</code></td><td></td></tr>
<tr><td><code>Medulloepithelioma, NOS</code></td><td><code>icdo:9501/3</code></td><td></td></tr>
<tr><td><code>Medullomyoblastoma</code></td><td><code>icdo:9472/3</code></td><td></td></tr>
<tr><td><code>Melanoma in situ</code></td><td><code>icdo:8720/2</code></td><td></td></tr>
<tr><td><code>Melanotic neurofibroma</code></td><td><code>icdo:9541/0</code></td><td></td></tr>
<tr><td><code>Melanotic schwannoma</code></td><td><code>icdo:9560/1</code></td><td></td></tr>
<tr><td><code>Meningeal melanocytoma</code></td><td><code>icdo:8728/1</code></td><td></td></tr>
<tr><td><code>Meningeal melanomatosis</code></td><td><code>icdo:8728/3</code></td><td></td></tr>
<tr><td><code>Meningeal sarcomatosis</code></td><td><code>icdo:9539/3</code></td><td></td></tr>
<tr><td><code>Meningioma, NOS</code></td><td><code>icdo:9530/0</code></td><td></td></tr>
<tr><td><code>Meningioma, malignant</code></td><td><code>icdo:9530/3</code></td><td></td></tr>
<tr><td><code>Meningothelial meningioma</code></td><td><code>icdo:9531/0</code></td><td></td></tr>
<tr><td><code>Merkel cell carcinoma</code></td><td><code>icdo:8247/3</code></td><td></td></tr>
<tr><td><code>Mesenchymal Chondrosarcoma</code></td><td><code>icdo:9240/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Mesenchymoma, malignant</code></td><td><code>icdo:8990/3</code></td><td></td></tr>
<tr><td><code>Mesodermal mixed tumor</code></td><td><code>icdo:8951/3</code></td><td></td></tr>
<tr><td><code>Mesonephric-like adenocarcinoma</code></td><td><code>icdo:9111/3</code></td><td></td></tr>
<tr><td><code>Mesonephroma, malignant</code></td><td><code>icdo:9110/3</code></td><td></td></tr>
<tr><td><code>Mesothelioma, biphasic, malignant</code></td><td><code>icdo:9053/3</code></td><td></td></tr>
<tr><td><code>Mesothelioma, in situ</code></td><td><code>icdo:9050/2</code></td><td></td></tr>
<tr><td><code>Mesothelioma, malignant</code></td><td><code>icdo:9050/3</code></td><td></td></tr>
<tr><td><code>Metaplastic carcinoma, NOS</code></td><td><code>icdo:8575/3</code></td><td></td></tr>
<tr><td><code>Metatypical carcinoma</code></td><td><code>icdo:8095/3</code></td><td></td></tr>
<tr><td><code>Micropapillary carcinoma, NOS</code></td><td><code>icdo:8265/3</code></td><td></td></tr>
<tr><td><code>Middle ear paraganglioma</code></td><td><code>icdo:8690/3</code></td><td></td></tr>
<tr><td><code>Minimally invasive adenocarcinoma, mucinous</code></td><td><code>icdo:8257/3</code></td><td></td></tr>
<tr><td><code>Minimally invasive adenocarcinoma, non-mucinous</code></td><td><code>icdo:8256/3</code></td><td></td></tr>
<tr><td><code>Mixed Germ Cell Tumor</code></td><td><code>ncit:C4290</code></td><td></td></tr>
<tr><td><code>Mixed acidophil-basophil adenoma</code></td><td><code>icdo:8281/0</code></td><td></td></tr>
<tr><td><code>Mixed acidophil-basophil carcinoma</code></td><td><code>icdo:8281/3</code></td><td></td></tr>
<tr><td><code>Mixed acinar ductal carcinoma</code></td><td><code>icdo:8552/3</code></td><td></td></tr>
<tr><td><code>Mixed cell adenocarcinoma</code></td><td><code>icdo:8323/3</code></td><td></td></tr>
<tr><td><code>Mixed cell adenoma</code></td><td><code>icdo:8323/0</code></td><td></td></tr>
<tr><td><code>Mixed epithel. &amp; spindle cell melanoma</code></td><td><code>icdo:8770/3</code></td><td></td></tr>
<tr><td><code>Mixed glioma</code></td><td><code>icdo:9382/3</code></td><td></td></tr>
<tr><td><code>Mixed invasive mucinous and non-mucinous adenocarcinoma</code></td><td><code>icdo:8254/3</code></td><td></td></tr>
<tr><td><code>Mixed medullary-follicular carcinoma</code></td><td><code>icdo:8346/3</code></td><td></td></tr>
<tr><td><code>Mixed medullary-papillary carcinoma</code></td><td><code>icdo:8347/3</code></td><td></td></tr>
<tr><td><code>Mixed neuroendocrine non-neuroendocrine neoplasm</code></td><td><code>icdo:8154/3</code></td><td></td></tr>
<tr><td><code>Mixed phenotype acute leukemia with t(9;22)(q34;q11.2);BCR-ABL1</code></td><td><code>icdo:9806/3</code></td><td></td></tr>
<tr><td><code>Mixed phenotype acute leukemia with t(v;11q23);MLL rearranged</code></td><td><code>icdo:9807/3</code></td><td></td></tr>
<tr><td><code>Mixed phenotype acute leukemia, B/myeloid, NOS</code></td><td><code>icdo:9808/3</code></td><td></td></tr>
<tr><td><code>Mixed phenotype acute leukemia, T/myeloid, NOS</code></td><td><code>icdo:9809/3</code></td><td></td></tr>
<tr><td><code>Mixed tumor, malignant, NOS</code></td><td><code>icdo:8940/3</code></td><td></td></tr>
<tr><td><code>Mixed type liposarcoma</code></td><td><code>icdo:8855/3</code></td><td></td></tr>
<tr><td><code>Mixed type rhabdomyosarcoma</code></td><td><code>icdo:8902/3</code></td><td></td></tr>
<tr><td><code>Monomorphic adenoma</code></td><td><code>icdo:8146/0</code></td><td></td></tr>
<tr><td><code>Mucin-producing adenocarcinoma</code></td><td><code>icdo:8481/3</code></td><td></td></tr>
<tr><td><code>Mucinous adenocarcinofibroma</code></td><td><code>icdo:9015/3</code></td><td></td></tr>
<tr><td><code>Mucinous adenocarcinoma</code></td><td><code>icdo:8480/3</code></td><td></td></tr>
<tr><td><code>Mucinous adenocarcinoma, endocervical type</code></td><td><code>icdo:8482/3</code></td><td></td></tr>
<tr><td><code>Mucinous cystadenocarcinoma, NOS</code></td><td><code>icdo:8470/3</code></td><td></td></tr>
<tr><td><code>Mucinous cystadenocarcinoma, non-invasive</code></td><td><code>icdo:8470/2</code></td><td></td></tr>
<tr><td><code>Mucinous cystic tumor of borderline malignancy (C56.9)</code></td><td><code>icdo:8472/1</code></td><td></td></tr>
<tr><td><code>Mucoepidermoid carcinoma</code></td><td><code>icdo:8430/3</code></td><td></td></tr>
<tr><td><code>Mucosal lentiginous melanoma</code></td><td><code>icdo:8746/3</code></td><td></td></tr>
<tr><td><code>Mullerian mixed tumor</code></td><td><code>icdo:8950/3</code></td><td></td></tr>
<tr><td><code>Multifocal superficial basal cell carcinoma</code></td><td><code>icdo:8091/3</code></td><td></td></tr>
<tr><td><code>Multinodular and vacuolating neuronal tumor</code></td><td><code>icdo:9509/0</code></td><td></td></tr>
<tr><td><code>Multinodular and vascolating neuronal tumor</code></td><td><code>icdo:9505/0</code></td><td></td></tr>
<tr><td><code>Multiple myeloma</code></td><td><code>icdo:9732/3</code></td><td></td></tr>
<tr><td><code>Mycosis fungoides</code></td><td><code>icdo:9700/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic syndr. with 5q deletion syndrome</code></td><td><code>icdo:9986/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic syndrome with ring sideroblasts and multilineage</code></td><td><code>icdo:9993/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic syndrome, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Myelodysplastic/Myeloproliferative neoplasm, unclassifiable</code></td><td><code>icdo:9975/3</code></td><td></td></tr>
<tr><td><code>Myeloid and lymphoid neoplasm with FGFR1 abnormalities</code></td><td><code>icdo:9967/3</code></td><td></td></tr>
<tr><td><code>Myeloid and lymphoid neoplasms with PDGFRB re arrangement</code></td><td><code>icdo:9966/3</code></td><td></td></tr>
<tr><td><code>Myeloid and lymphoid neoplasms with PDGFRB rearrangement</code></td><td><code>icdo:9965/3</code></td><td></td></tr>
<tr><td><code>Myeloid leukemia associated with Down Syndrome</code></td><td><code>icdo:9898/3</code></td><td></td></tr>
<tr><td><code>Myeloid leukemia, NOS</code></td><td><code>icdo:9860/3</code></td><td></td></tr>
<tr><td><code>Myeloid sarcoma</code></td><td><code>icdo:9930/3</code></td><td></td></tr>
<tr><td><code>Myeloid/lymphoid neoplasm with PCM1-JAK2</code></td><td><code>icdo:9968/3</code></td><td></td></tr>
<tr><td><code>Myelosclerosis with myeloid metaplasia</code></td><td><code>icdo:9961/3</code></td><td></td></tr>
<tr><td><code>Myofibroblastic sarcoma</code></td><td><code>icdo:8825/3</code></td><td></td></tr>
<tr><td><code>Myosarcoma</code></td><td><code>icdo:8895/3</code></td><td></td></tr>
<tr><td><code>Myxoid Liposarcoma</code></td><td><code>ncit:C27781</code></td><td></td></tr>
<tr><td><code>Myxoid chondrosarcoma</code></td><td><code>icdo:9231/3</code></td><td></td></tr>
<tr><td><code>Myxoid Leiomyosarcoma</code></td><td><code>icdo:8896/3</code></td><td></td></tr>
<tr><td><code>Myxopapillary Ependymoma</code></td><td><code>ncit:C3697</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Myxosarcoma</code></td><td><code>icdo:8840/3</code></td><td></td></tr>
<tr><td><code>NK/T-cell lymphoma, nasal and nasal-type</code></td><td><code>icdo:9719/3</code></td><td></td></tr>
<tr><td><code>NUT carcinoma</code></td><td><code>icdo:8023/3</code></td><td></td></tr>
<tr><td><code>Neoplasm, benign</code></td><td><code>icdo:8000/0</code></td><td></td></tr>
<tr><td><code>Neoplasm, malignant</code></td><td><code>icdo:8000/3</code></td><td></td></tr>
<tr><td><code>Neoplasm, uncertain whether benign or malignant</code></td><td><code>icdo:8000/1</code></td><td></td></tr>
<tr><td><code>Nephroblastoma, NOS</code></td><td><code>icdo:8960/3</code></td><td></td></tr>
<tr><td><code>Neurilemmoma, malignant</code></td><td><code>icdo:9560/3</code></td><td></td></tr>
<tr><td><code>Neurilemoma, NOS</code></td><td><code>icdo:9560/0</code></td><td></td></tr>
<tr><td><code>Neuroblastoma, NOS</code></td><td><code>icdo:9500/3</code></td><td></td></tr>
<tr><td><code>Neuroendocrine carcinoma</code></td><td><code>icdo:8246/3</code></td><td></td></tr>
<tr><td><code>Neuroendocrine tumor</code></td><td><code>icdo:8249/3</code></td><td></td></tr>
<tr><td><code>Neuroepithelioma, NOS</code></td><td><code>icdo:9503/3</code></td><td></td></tr>
<tr><td><code>Neurofibroma, NOS</code></td><td><code>icdo:9540/0</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis, NOS</code></td><td><code>icdo:9540/1</code></td><td></td></tr>
<tr><td><code>Neuroma, NOS</code></td><td><code>icdo:9570/0</code></td><td></td></tr>
<tr><td><code>Neurothekeoma</code></td><td><code>icdo:9562/0</code></td><td></td></tr>
<tr><td><code>Nodular hidradenoma, malignant</code></td><td><code>icdo:8402/3</code></td><td></td></tr>
<tr><td><code>Nodular melanoma</code></td><td><code>icdo:8721/3</code></td><td></td></tr>
<tr><td><code>Non-invasive EFVPTC</code></td><td><code>icdo:8343/2</code></td><td></td></tr>
<tr><td><code>Non-invasive low grade serous carcinoma</code></td><td><code>icdo:8460/2</code></td><td></td></tr>
<tr><td><code>Non-small cell carcinoma</code></td><td><code>icdo:8046/3</code></td><td></td></tr>
<tr><td><code>Nonencapsulated sclerosing carcinoma</code></td><td><code>icdo:8350/3</code></td><td></td></tr>
<tr><td><code>Noninfiltrating intracystic carcinoma</code></td><td><code>icdo:8504/2</code></td><td></td></tr>
<tr><td><code>Noninfiltrating intraductal papillary adenocarcinoma</code></td><td><code>icdo:8503/2</code></td><td></td></tr>
<tr><td><code>Oat cell carcinoma</code></td><td><code>icdo:8042/3</code></td><td></td></tr>
<tr><td><code>Odontogenic carcinosarcoma</code></td><td><code>icdo:9342/3</code></td><td></td></tr>
<tr><td><code>Odontogenic tumor, malignant</code></td><td><code>icdo:9270/3</code></td><td></td></tr>
<tr><td><code>Olfactory neurcytoma</code></td><td><code>icdo:9521/3</code></td><td></td></tr>
<tr><td><code>Olfactory neuroblastoma</code></td><td><code>icdo:9522/3</code></td><td></td></tr>
<tr><td><code>Olfactory neuroepithelioma</code></td><td><code>icdo:9523/3</code></td><td></td></tr>
<tr><td><code>Olfactory neurogenic tumor</code></td><td><code>icdo:9520/3</code></td><td></td></tr>
<tr><td><code>Oligodendroblastoma</code></td><td><code>icdo:9460/3</code></td><td></td></tr>
<tr><td><code>Oligodendroglioma, anaplastic</code></td><td><code>icdo:9451/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma in Paget disease</code></td><td><code>icdo:9184/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma, NOS</code></td><td><code>icdo:9180/3</code></td><td></td></tr>
<tr><td><code>Ovarian stromal tumor, mal.</code></td><td><code>icdo:8590/3</code></td><td></td></tr>
<tr><td><code>Oxyphilic adenocarcinoma</code></td><td><code>icdo:8290/3</code></td><td></td></tr>
<tr><td><code>Oxyphilic adenoma</code></td><td><code>icdo:8290/0</code></td><td></td></tr>
<tr><td><code>PEComa, malignant</code></td><td><code>icdo:8714/3</code></td><td></td></tr>
<tr><td><code>Paget dis. &amp; infil. duct carcinoma</code></td><td><code>icdo:8541/3</code></td><td></td></tr>
<tr><td><code>Paget disease and intraductal ca.</code></td><td><code>icdo:8543/3</code></td><td></td></tr>
<tr><td><code>Paget disease, extramammary</code></td><td><code>icdo:8542/3</code></td><td></td></tr>
<tr><td><code>Paget disease, mammary</code></td><td><code>icdo:8540/3</code></td><td></td></tr>
<tr><td><code>Pancreatobiliary-type carcinoma</code></td><td><code>icdo:8163/3</code></td><td></td></tr>
<tr><td><code>Pancreatoblastoma</code></td><td><code>icdo:8971/3</code></td><td></td></tr>
<tr><td><code>Papillary Craniopharyngioma</code></td><td><code>icdo:9352/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'</td></tr>
<tr><td><code>Papillary Glioneuronal Tumor</code></td><td><code>icdo:9509/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Papillary adenocarcinoma, NOS</code></td><td><code>icdo:8260/3</code></td><td></td></tr>
<tr><td><code>Papillary adenoma, NOS</code></td><td><code>icdo:8260/0</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma in situ</code></td><td><code>icdo:8050/2</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma, NOS</code></td><td><code>icdo:8050/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma, columnar cell</code></td><td><code>icdo:8344/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma, encapsulated</code></td><td><code>icdo:8343/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma, follicular variant</code></td><td><code>icdo:8340/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma, oxyphilic cell</code></td><td><code>icdo:8342/3</code></td><td></td></tr>
<tr><td><code>Papillary cystadenocarcinoma, NOS</code></td><td><code>icdo:8450/3</code></td><td></td></tr>
<tr><td><code>Papillary cystadenoma, borderline malignancy (C56.9)</code></td><td><code>icdo:8451/1</code></td><td></td></tr>
<tr><td><code>Papillary ependymoma</code></td><td><code>icdo:9393/3</code></td><td></td></tr>
<tr><td><code>Papillary meningioma</code></td><td><code>icdo:9538/3</code></td><td></td></tr>
<tr><td><code>Papillary microcarcinoma</code></td><td><code>icdo:8341/3</code></td><td></td></tr>
<tr><td><code>Papillary mucinous cystadenocarcinoma</code></td><td><code>icdo:8471/3</code></td><td></td></tr>
<tr><td><code>Papillary mucinous cystadenoma, borderline malignancy (C56.9)</code></td><td><code>icdo:8473/1</code></td><td></td></tr>
<tr><td><code>Papillary squamous cell carcinoma</code></td><td><code>icdo:8052/3</code></td><td></td></tr>
<tr><td><code>Papillary squamous cell carcinoma, non-invasive</code></td><td><code>icdo:8052/2</code></td><td></td></tr>
<tr><td><code>Papillary trans. cell carcinoma</code></td><td><code>icdo:8130/3</code></td><td></td></tr>
<tr><td><code>Papillary trans. cell carcinoma, non-invasive</code></td><td><code>icdo:8130/2</code></td><td></td></tr>
<tr><td><code>Papillary tumor of pineal region</code></td><td><code>icdo:9395/3</code></td><td></td></tr>
<tr><td><code>Paraganglioma, NOS</code></td><td><code>icdo:8680/1</code></td><td></td></tr>
<tr><td><code>Paraganglioma, malignant</code></td><td><code>icdo:8680/3</code></td><td></td></tr>
<tr><td><code>Parietal cell carcinoma</code></td><td><code>icdo:8214/3</code></td><td></td></tr>
<tr><td><code>Parosteal Osteosarcoma</code></td><td><code>icdo:9192/3</code></td><td></td></tr>
<tr><td><code>Perineurioma, NOS</code></td><td><code>icdo:9571/0</code></td><td></td></tr>
<tr><td><code>Perineurioma, malignant</code></td><td><code>icdo:9571/3</code></td><td></td></tr>
<tr><td><code>Periosteal fibrosarcoma</code></td><td><code>icdo:8812/3</code></td><td></td></tr>
<tr><td><code>Periosteal Osteosarcoma</code></td><td><code>icdo:9193/3</code></td><td></td></tr>
<tr><td><code>Peripheral neuroectodermal tumor</code></td><td><code>icdo:9364/3</code></td><td></td></tr>
<tr><td><code>Pheochromocytoma</code></td><td><code>icdo:8700/3</code></td><td></td></tr>
<tr><td><code>Phyllodes tumor, malignant</code></td><td><code>icdo:9020/3</code></td><td></td></tr>
<tr><td><code>Pilocytic Astrocytoma</code></td><td><code>icdo:9421/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pilomatrix carcinoma</code></td><td><code>icdo:8110/3</code></td><td></td></tr>
<tr><td><code>Pilomyxoid Astrocytoma</code></td><td><code>icdo:9425/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pineocytoma</code></td><td><code>icdo:9361/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pituicytoma</code></td><td><code>icdo:9432/1</code></td><td></td></tr>
<tr><td><code>Pituitary adenoma, NOS</code></td><td><code>icdo:8272/0</code></td><td></td></tr>
<tr><td><code>Pituitary blastoma</code></td><td><code>icdo:8273/3</code></td><td></td></tr>
<tr><td><code>Pituitary carcinoma, NOS</code></td><td><code>icdo:8272/3</code></td><td></td></tr>
<tr><td><code>Plasma cell leukemia</code></td><td><code>icdo:9733/3</code></td><td></td></tr>
<tr><td><code>Plasmablastic lymphoma</code></td><td><code>icdo:9735/3</code></td><td></td></tr>
<tr><td><code>Plasmacytoma, NOS</code></td><td><code>icdo:9731/3</code></td><td></td></tr>
<tr><td><code>Plasmacytoma, extramedullary</code></td><td><code>icdo:9734/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Xanthoastrocytoma</code></td><td><code>icdo:9424/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Pleomorphic carcinoma</code></td><td><code>icdo:8022/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Liposarcoma</code></td><td><code>icdo:8854/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic lobular carcinoma in situ</code></td><td><code>icdo:8519/2</code></td><td></td></tr>
<tr><td><code>Pleomorphic rhabdomyosarcoma, adult type</code></td><td><code>icdo:8901/3</code></td><td></td></tr>
<tr><td><code>Pleuropulmonary blastoma</code></td><td><code>icdo:8973/3</code></td><td></td></tr>
<tr><td><code>Plexiform neurofibroma</code></td><td><code>icdo:9550/0</code></td><td></td></tr>
<tr><td><code>Polar spongioblastoma</code></td><td><code>icdo:9423/3</code></td><td></td></tr>
<tr><td><code>Polycythemia vera</code></td><td><code>icdo:9950/3</code></td><td></td></tr>
<tr><td><code>Polygonal cell carcinoma</code></td><td><code>icdo:8034/3</code></td><td></td></tr>
<tr><td><code>Polymorphic PTLD</code></td><td><code>icdo:9971/3</code></td><td></td></tr>
<tr><td><code>Polymorphous low grade adenocarcinoma</code></td><td><code>icdo:8525/3</code></td><td></td></tr>
<tr><td><code>Precancerous melanosis, NOS</code></td><td><code>icdo:8741/2</code></td><td></td></tr>
<tr><td><code>Precursor B-cell lymphoblastic leukemia</code></td><td><code>icdo:9836/3</code></td><td></td></tr>
<tr><td><code>Precursor B-cell lymphoblastic lymphoma</code></td><td><code>icdo:9728/3</code></td><td></td></tr>
<tr><td><code>Precursor T-cell lymphoblastic lymphoma</code></td><td><code>icdo:9729/3</code></td><td></td></tr>
<tr><td><code>Precursor cell lymphoblastic leukemia, NOS</code></td><td><code>icdo:9835/3</code></td><td></td></tr>
<tr><td><code>Precursor cell lymphoblastic lymphoma, NOS</code></td><td><code>icdo:9727/3</code></td><td></td></tr>
<tr><td><code>Primary Cutaneous follicle centre lymphoma</code></td><td><code>icdo:9597/3</code></td><td></td></tr>
<tr><td><code>Primary Cutaneous gamma-delta T-cell lymphoma</code></td><td><code>icdo:9726/3</code></td><td></td></tr>
<tr><td><code>Primary cutan. CD30+ T-cell lymphoprolif. disorder</code></td><td><code>icdo:9718/3</code></td><td></td></tr>
<tr><td><code>Primary effusion lymphoma</code></td><td><code>icdo:9678/3</code></td><td></td></tr>
<tr><td><code>Primitive Neuroectodermal Tumor</code></td><td><code>icdo:9473/3</code></td><td></td></tr>
<tr><td><code>Prolactinoma</code></td><td><code>icdo:8271/0</code></td><td></td></tr>
<tr><td><code>Prolymphocytic leukemia, B-cell type</code></td><td><code>icdo:9833/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic leukemia, NOS</code></td><td><code>icdo:9832/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic leukemia, T-cell type</code></td><td><code>icdo:9834/3</code></td><td></td></tr>
<tr><td><code>Protoplasmic astrocytoma</code></td><td><code>icdo:9410/3</code></td><td></td></tr>
<tr><td><code>Psammomatous meningioma</code></td><td><code>icdo:9533/0</code></td><td></td></tr>
<tr><td><code>Pseudosarcomatous carcinoma</code></td><td><code>icdo:8033/3</code></td><td></td></tr>
<tr><td><code>Pulmonary blastoma</code></td><td><code>icdo:8972/3</code></td><td></td></tr>
<tr><td><code>Pulmonary myxoid sarcoma with EWSR1-CREB1 translocation</code></td><td><code>icdo:8842/3</code></td><td></td></tr>
<tr><td><code>Queyrat erythroplasia</code></td><td><code>icdo:8080/2</code></td><td></td></tr>
<tr><td><code>Refract. anemia with excess blasts in transformation</code></td><td><code>icdo:9984/3</code></td><td></td></tr>
<tr><td><code>Refractory anemia</code></td><td><code>icdo:9980/3</code></td><td></td></tr>
<tr><td><code>Refractory anemia with excess blasts</code></td><td><code>icdo:9983/3</code></td><td></td></tr>
<tr><td><code>Refractory anemia with sideroblasts</code></td><td><code>icdo:9982/3</code></td><td></td></tr>
<tr><td><code>Refractory cytopenia with multilineage dysplasia</code></td><td><code>icdo:9985/3</code></td><td></td></tr>
<tr><td><code>Refractory neutropenia</code></td><td><code>icdo:9991/3</code></td><td></td></tr>
<tr><td><code>Refractory thrombocytopenia</code></td><td><code>icdo:9992/3</code></td><td></td></tr>
<tr><td><code>Renal cell carcinoma</code></td><td><code>icdo:8312/3</code></td><td></td></tr>
<tr><td><code>Renal cell carcinoma, chromophobe type</code></td><td><code>icdo:8317/3</code></td><td></td></tr>
<tr><td><code>Renal cell carcinoma, sarcomatoid</code></td><td><code>icdo:8318/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, NOS</code></td><td><code>icdo:9510/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, differentiated</code></td><td><code>icdo:9511/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, diffuse</code></td><td><code>icdo:9513/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, undifferentiated</code></td><td><code>icdo:9512/3</code></td><td></td></tr>
<tr><td><code>Rhabdomyoma, NOS</code></td><td><code>icdo:8900/0</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma with ganglionic differentiation</code></td><td><code>icdo:8921/3</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma, NOS</code></td><td><code>icdo:8900/3</code></td><td></td></tr>
<tr><td><code>Round cell liposarcoma</code></td><td><code>icdo:8853/3</code></td><td></td></tr>
<tr><td><code>Round cell sarcoma with EWSR1-non-ETS fusions</code></td><td><code>icdo:9366/3</code></td><td></td></tr>
<tr><td><code>Sarcoma with BCOR genetic alterations</code></td><td><code>icdo:9368/3</code></td><td></td></tr>
<tr><td><code>Sarcoma, NOS</code></td><td><code>icdo:8800/3</code></td><td></td></tr>
<tr><td><code>Schneiderian carcinoma</code></td><td><code>icdo:8121/3</code></td><td></td></tr>
<tr><td><code>Scirrhous adenocarcinoma</code></td><td><code>icdo:8141/3</code></td><td></td></tr>
<tr><td><code>Sclerosing sweat duct carcinoma</code></td><td><code>icdo:8407/3</code></td><td></td></tr>
<tr><td><code>Sebaceous adenocarcinoma</code></td><td><code>icdo:8410/3</code></td><td></td></tr>
<tr><td><code>Secretory carcinoma of no special type</code></td><td><code>icdo:8502/3</code></td><td></td></tr>
<tr><td><code>Sellar ependymoma</code></td><td><code>icdo:9391/1</code></td><td></td></tr>
<tr><td><code>Seminoma, NOS</code></td><td><code>icdo:9061/3</code></td><td></td></tr>
<tr><td><code>Seminoma, anaplastic</code></td><td><code>icdo:9062/3</code></td><td></td></tr>
<tr><td><code>Seromucinous carcinoma</code></td><td><code>icdo:8474/3</code></td><td></td></tr>
<tr><td><code>Serous adenocarcinofibroma</code></td><td><code>icdo:9014/3</code></td><td></td></tr>
<tr><td><code>Serous cystadenocarcinoma</code></td><td><code>icdo:8441/3</code></td><td></td></tr>
<tr><td><code>Serous cystadenoma, borderline malignancy (C56.9)</code></td><td><code>icdo:8442/1</code></td><td></td></tr>
<tr><td><code>Serous papillary cystic tumor of borderline malignancy (C56.9)</code></td><td><code>icdo:8462/1</code></td><td></td></tr>
<tr><td><code>Serous tubal intraepithelial carcinoma</code></td><td><code>icdo:8441/2</code></td><td></td></tr>
<tr><td><code>Serrated adenocarcinoma</code></td><td><code>icdo:8213/3</code></td><td></td></tr>
<tr><td><code>Serrated dysplasia, high grade</code></td><td><code>icdo:8213/2</code></td><td></td></tr>
<tr><td><code>Sertoli cell carcinoma</code></td><td><code>icdo:8640/3</code></td><td></td></tr>
<tr><td><code>Sertoli-Leydig cell tumor, poorly differentiated</code></td><td><code>icdo:8631/3</code></td><td></td></tr>
<tr><td><code>Sertoli-Leydig cl tum., p.d. w heterologous elements</code></td><td><code>icdo:8634/3</code></td><td></td></tr>
<tr><td><code>Sezary syndrome</code></td><td><code>icdo:9701/3</code></td><td></td></tr>
<tr><td><code>Signet ring cell carcinoma</code></td><td><code>icdo:8490/3</code></td><td></td></tr>
<tr><td><code>Skin appendage carcinoma</code></td><td><code>icdo:8390/3</code></td><td></td></tr>
<tr><td><code>Small cell carcinoma, NOS</code></td><td><code>icdo:8041/3</code></td><td></td></tr>
<tr><td><code>Small cell carcinoma, fusiform cell</code></td><td><code>icdo:8043/3</code></td><td></td></tr>
<tr><td><code>Small cell carcinoma, intermediate cell</code></td><td><code>icdo:8044/3</code></td><td></td></tr>
<tr><td><code>Small cell sarcoma</code></td><td><code>icdo:8803/3</code></td><td></td></tr>
<tr><td><code>Smooth muscle tumor, NOS</code></td><td><code>icdo:8897/1</code></td><td></td></tr>
<tr><td><code>Soft tissue tumor, benign</code></td><td><code>icdo:8800/0</code></td><td></td></tr>
<tr><td><code>Solid carcinoma, NOS</code></td><td><code>icdo:8230/3</code></td><td></td></tr>
<tr><td><code>Solid papillary carcinoma in situ</code></td><td><code>icdo:8509/2</code></td><td></td></tr>
<tr><td><code>Solid papillary carcinoma with invasion</code></td><td><code>icdo:8509/3</code></td><td></td></tr>
<tr><td><code>Solid pseudopapillary carcinoma</code></td><td><code>icdo:8452/3</code></td><td></td></tr>
<tr><td><code>Solitary Fibrous Tumor</code></td><td><code>ncit:C7634</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Solitary Fibrous Tumor, Malignant</code></td><td><code>icdo:8815/3</code></td><td></td></tr>
<tr><td><code>Solitary fibrous tumor/hemangiopericytoma Grade 2</code></td><td><code>icdo:8815/1</code></td><td></td></tr>
<tr><td><code>Somatostatinoma, malignant</code></td><td><code>icdo:8156/3</code></td><td></td></tr>
<tr><td><code>Spermatocytic seminoma</code></td><td><code>icdo:9063/3</code></td><td></td></tr>
<tr><td><code>Spindle cell carcinoma</code></td><td><code>icdo:8032/3</code></td><td></td></tr>
<tr><td><code>Spindle cell melanoma, NOS</code></td><td><code>icdo:8772/3</code></td><td></td></tr>
<tr><td><code>Spindle cell melanoma, type A</code></td><td><code>icdo:8773/3</code></td><td></td></tr>
<tr><td><code>Spindle cell melanoma, type B</code></td><td><code>icdo:8774/3</code></td><td></td></tr>
<tr><td><code>Spindle cell rhabdomyosarcoma</code></td><td><code>icdo:8912/3</code></td><td></td></tr>
<tr><td><code>Spindle cell sarcoma</code></td><td><code>icdo:8801/3</code></td><td></td></tr>
<tr><td><code>Spindle epithelial tumor with thymus-like element</code></td><td><code>icdo:8588/3</code></td><td></td></tr>
<tr><td><code>Splenic marginal zone B-cell lymphoma</code></td><td><code>icdo:9689/3</code></td><td></td></tr>
<tr><td><code>Spongioneuroblastoma</code></td><td><code>icdo:9504/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carc. in situ with question. stromal invas.</code></td><td><code>icdo:8076/2</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, keratinizing, NOS</code></td><td><code>icdo:8071/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, keratinizing, NOS, in situ</code></td><td><code>icdo:8071/2</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, lg. cell, non-ker.</code></td><td><code>icdo:8072/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, lg. cell, non-ker., in situ</code></td><td><code>icdo:8072/2</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, micro-invasive</code></td><td><code>icdo:8076/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, sm. cell, non-ker.</code></td><td><code>icdo:8073/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, spindle cell</code></td><td><code>icdo:8074/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, NOS</code></td><td><code>icdo:8070/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma in situ, NOS</code></td><td><code>icdo:8070/2</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma with horn formation</code></td><td><code>icdo:8078/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma, HPV-negative</code></td><td><code>icdo:8086/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma, HPV-positive</code></td><td><code>icdo:8085/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma, adenoid</code></td><td><code>icdo:8075/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma, clear cell type</code></td><td><code>icdo:8084/3</code></td><td></td></tr>
<tr><td><code>Squamous intraepithelial neoplasia, grade III</code></td><td><code>icdo:8077/2</code></td><td></td></tr>
<tr><td><code>Steroid cell tumor, malignant</code></td><td><code>icdo:8670/3</code></td><td></td></tr>
<tr><td><code>Stromal sarcoma, NOS</code></td><td><code>icdo:8935/3</code></td><td></td></tr>
<tr><td><code>Struma ovarii, malignant</code></td><td><code>icdo:9090/3</code></td><td></td></tr>
<tr><td><code>Subcutaneous panniculitis-like T-cell lymphoma</code></td><td><code>icdo:9708/3</code></td><td></td></tr>
<tr><td><code>Subependymoma</code></td><td><code>icdo:9383/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Supependymal giant cell astrocytoma</code></td><td><code>icdo:9384/1</code></td><td></td></tr>
<tr><td><code>Superficial spreading adenocarcinoma</code></td><td><code>icdo:8143/3</code></td><td></td></tr>
<tr><td><code>Superficial spreading melanoma</code></td><td><code>icdo:8743/3</code></td><td></td></tr>
<tr><td><code>Superficial spreading melanoma, in situ</code></td><td><code>icdo:8743/2</code></td><td></td></tr>
<tr><td><code>Sweat gland adenocarcinoma</code></td><td><code>icdo:8400/3</code></td><td></td></tr>
<tr><td><code>Sympathetic Paraganglioma</code></td><td><code>icdo:8681/3</code></td><td></td></tr>
<tr><td><code>Synovial sarcoma, NOS</code></td><td><code>icdo:9040/3</code></td><td></td></tr>
<tr><td><code>Synovial sarcoma, epithelioid cell</code></td><td><code>icdo:9042/3</code></td><td></td></tr>
<tr><td><code>SystemicEBV pos. T-cell lymphoproliferative disease of childhood</code></td><td><code>icdo:9724/3</code></td><td></td></tr>
<tr><td><code>T lymphoblastic leukemia/lymphoma</code></td><td><code>icdo:9837/3</code></td><td></td></tr>
<tr><td><code>T-cell histiocyte rich large B-cell lymphoma</code></td><td><code>icdo:9688/3</code></td><td></td></tr>
<tr><td><code>T-cell large granular lymphocytic leukemia</code></td><td><code>icdo:9831/3</code></td><td></td></tr>
<tr><td><code>Teratocarcinoma</code></td><td><code>icdo:9081/3</code></td><td></td></tr>
<tr><td><code>Teratoid medulloepithelioma</code></td><td><code>icdo:9502/3</code></td><td></td></tr>
<tr><td><code>Teratoma with malig. transformation</code></td><td><code>icdo:9084/3</code></td><td></td></tr>
<tr><td><code>Teratoma, benign</code></td><td><code>icdo:9080/0</code></td><td></td></tr>
<tr><td><code>Teratoma, malignant, NOS</code></td><td><code>icdo:9080/3</code></td><td></td></tr>
<tr><td><code>Thecoma, malignant</code></td><td><code>icdo:8600/3</code></td><td></td></tr>
<tr><td><code>Therapy-related acute myeloid leukemia, NOS</code></td><td><code>icdo:9920/3</code></td><td></td></tr>
<tr><td><code>Therapy-related myelodysplastic syndrome, NOS</code></td><td><code>icdo:9987/3</code></td><td></td></tr>
<tr><td><code>Thymic carcinoma, NOS</code></td><td><code>icdo:8586/3</code></td><td></td></tr>
<tr><td><code>Thymoma, malignant, NOS</code></td><td><code>icdo:8580/3</code></td><td></td></tr>
<tr><td><code>Thymoma, type A, malignant</code></td><td><code>icdo:8581/3</code></td><td></td></tr>
<tr><td><code>Thymoma, type AB, malignant</code></td><td><code>icdo:8582/3</code></td><td></td></tr>
<tr><td><code>Thymoma, type B1, malignant</code></td><td><code>icdo:8583/3</code></td><td></td></tr>
<tr><td><code>Thymoma, type B2, malignant</code></td><td><code>icdo:8584/3</code></td><td></td></tr>
<tr><td><code>Thymoma, type B3, malignant</code></td><td><code>icdo:8585/3</code></td><td></td></tr>
<tr><td><code>Trabecular adenocarcinoma</code></td><td><code>icdo:8190/3</code></td><td></td></tr>
<tr><td><code>Trans. cell carcinoma, spindle cell</code></td><td><code>icdo:8122/3</code></td><td></td></tr>
<tr><td><code>Transitional cell carcinoma in situ</code></td><td><code>icdo:8120/2</code></td><td></td></tr>
<tr><td><code>Transitional cell carcinoma, NOS</code></td><td><code>icdo:8120/3</code></td><td></td></tr>
<tr><td><code>Transitional cell carcinoma, micropapillary</code></td><td><code>icdo:8131/3</code></td><td></td></tr>
<tr><td><code>Transitional meningioma</code></td><td><code>icdo:9537/0</code></td><td></td></tr>
<tr><td><code>Trophoblastic tumor, epithelioid</code></td><td><code>icdo:9105/3</code></td><td></td></tr>
<tr><td><code>Tubular adenocarcinoma</code></td><td><code>icdo:8211/3</code></td><td></td></tr>
<tr><td><code>Tumor cells, benign</code></td><td><code>icdo:8001/0</code></td><td></td></tr>
<tr><td><code>Tumor cells, malignant</code></td><td><code>icdo:8001/3</code></td><td></td></tr>
<tr><td><code>Tumor cells, uncertain whether benign or malignant</code></td><td><code>icdo:8001/1</code></td><td></td></tr>
<tr><td><code>Undifferentiated sarcoma</code></td><td><code>icdo:8805/3</code></td><td></td></tr>
<tr><td><code>Venous hemangioma</code></td><td><code>icdo:9122/0</code></td><td></td></tr>
<tr><td><code>Verrucous carcinoma, NOS</code></td><td><code>icdo:8051/3</code></td><td></td></tr>
<tr><td><code>Villous adenocarcinoma</code></td><td><code>icdo:8262/3</code></td><td></td></tr>
<tr><td><code>Waldenstrom macroglobulinemia</code></td><td><code>icdo:9761/3</code></td><td></td></tr>
<tr><td><code>Warthin tumor, malignant</code></td><td><code>icdo:8561/3</code></td><td></td></tr>
<tr><td><code>Warty carcinoma</code></td><td><code>icdo:8054/3</code></td><td></td></tr>
<tr><td><code>Water-clear cell adenocarcinoma</code></td><td><code>icdo:8322/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocyte-Rich</code></td><td><code>icdo:9651/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Sarcoma</code></td><td><code>icdo:8804/3</code></td><td></td></tr>
<tr><td><code>Yolk Sac Tumor</code></td><td><code>icdo:9071/3</code></td><td></td></tr>
<tr><td><code>Polyembryoma</code></td><td><code>icdo:9072/3</code></td><td></td></tr>
<tr><td><code>Carcinofibroma</code></td><td><code>icdo:8934/3</code></td><td></td></tr>
<tr><td><code>Vipoma</code></td><td><code>icdo:8155/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Spindle Cell</code></td><td><code>icdo:9041/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Biphasic</code></td><td><code>icdo:9043/3</code></td><td></td></tr>
<tr><td><code>Myxoid Pleomorphic Liposarcoma</code></td><td><code>icdo:8859/3</code></td><td></td></tr>
<tr><td><code>Telangiectatic Osteosarcoma</code></td><td><code>icdo:9183/3</code></td><td></td></tr>
<tr><td><code>Small Cell Osteosarcoma</code></td><td><code>icdo:9185/3</code></td><td></td></tr>
<tr><td><code>Trichilemmocarcinoma</code></td><td><code>icdo:8102/3</code></td><td></td></tr>
<tr><td><code>Pigmented Dermatofibrosarcoma Protuberans</code></td><td><code>icdo:8833/3</code></td><td></td></tr>
<tr><td><code>Teratoma, NOS</code></td><td><code>icdo:9080/1</code></td><td></td></tr>
<tr><td><code>Meningiomatosis, NOS</code></td><td><code>icdo:9530/1</code></td><td></td></tr>
<tr><td><code>Ependymoma, NOS</code></td><td><code>icdo:9391/3</code></td><td></td></tr>
<tr><td><code>Pinealoma, NOS</code></td><td><code>icdo:9360/1</code></td><td></td></tr>
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
<tr><td><code>FA</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdominal Peritoneum</code></td><td><code>ncit:C159355</code></td><td></td></tr>
<tr><td><code>Abdominal Skin</code></td><td><code>ncit:C52758</code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Arm Skin</code></td><td><code>ncit:C52754</code></td><td></td></tr>
<tr><td><code>Basal Ganglia-Thalamus</code></td><td><code>ncit:C158080</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Buccal Mucosa</code></td><td><code>ncit:C12505</code></td><td></td></tr>
<tr><td><code>Cerebellum</code></td><td><code>ncit:C12445</code></td><td></td></tr>
<tr><td><code>Cervical Spine</code></td><td><code>ncit:C69313</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Corpus Callosum</code></td><td><code>ncit:C12446</code></td><td></td></tr>
<tr><td><code>Ear Skin</code></td><td><code>ncit:C49481</code></td><td></td></tr>
<tr><td><code>Esophagus</code></td><td><code>ncit:C12389</code></td><td></td></tr>
<tr><td><code>Fallopian Tube</code></td><td><code>ncit:C12403</code></td><td></td></tr>
<tr><td><code>Frontal Lobe</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Gingiva, Lower, Anterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Lower, Posterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, NOS</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Upper, Anterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Upper, Posterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Glottis</code></td><td><code>ncit:C12724</code></td><td></td></tr>
<tr><td><code>Hand Skin</code></td><td><code>ncit:C52753</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Intestine</code></td><td><code>ncit:C12736</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Leg Skin</code></td><td><code>ncit:C52749</code></td><td></td></tr>
<tr><td><code>Lip</code></td><td><code>ncit:C12220</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lumbar Spinal Cord</code></td><td><code>ncit:C12895</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Medulla</code></td><td><code>ncit:C12442</code></td><td></td></tr>
<tr><td><code>Midbrain</code></td><td><code>ncit:C12510</code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasal Cavity and Paranasal Sinuses</code></td><td><code>ncit:C12763</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck Skin</code></td><td><code>ncit:C52756</code></td><td></td></tr>
<tr><td><code>Occipital Lobe</code></td><td><code>ncit:C12355</code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code>ncit:C12421</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Palate</code></td><td><code>ncit:C12229</code></td><td></td></tr>
<tr><td><code>Parietal Lobe</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Penis</code></td><td><code>ncit:C12409</code></td><td></td></tr>
<tr><td><code>Pharynx</code></td><td><code>ncit:C12425</code></td><td></td></tr>
<tr><td><code>Pons</code></td><td><code>ncit:C12511</code></td><td></td></tr>
<tr><td><code>Pyriform Sinus</code></td><td><code>ncit:C33439</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Skin of the Back</code></td><td><code>ncit:C142318</code></td><td></td></tr>
<tr><td><code>Skin of the Chest</code></td><td><code>ncit:C161379</code></td><td></td></tr>
<tr><td><code>Skin of the Face</code></td><td><code>ncit:C33561</code></td><td></td></tr>
<tr><td><code>Skin of the Lip</code></td><td><code>ncit:C12291</code></td><td></td></tr>
<tr><td><code>Skin of the Upper Limb and Shoulder</code></td><td><code>ncit:C12296</code></td><td></td></tr>
<tr><td><code>Skin, NOS</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code>ncit:C12391</code></td><td></td></tr>
<tr><td><code>Submandibular</code></td><td><code>ncit:C129462</code></td><td></td></tr>
<tr><td><code>Temporal Lobe</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Thoracic Spinal Cord</code></td><td><code>ncit:C12894</code></td><td></td></tr>
<tr><td><code>Tongue</code></td><td><code>ncit:C12422</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code>ncit:C12405</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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

<div id="enum-modal-dysplasiaenum" class="enum-modal" onclick="closeEnumModal('enum-modal-dysplasiaenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-dysplasiaenum')">×</button>
<h3><code>DysplasiaEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Mild</code></td><td><code>ncit:C8362</code></td><td></td></tr>
<tr><td><code>Moderate</code></td><td><code>ncit:C8363</code></td><td></td></tr>
<tr><td><code>Severe</code></td><td><code>ncit:C8364</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-exposureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-exposureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-exposureenum')">×</button>
<h3><code>ExposureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alcohol</code></td><td><code>ncit:C168296</code></td><td></td></tr>
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
<tr><td><code>Ever</code></td><td><code>ncit:C159710</code></td><td></td></tr>
<tr><td><code>Never</code></td><td><code>ncit:C70543</code></td><td></td></tr>
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
<tr><td><code>PubMed</code></td><td><code></code></td><td></td></tr>
<tr><td><code>dbsnp</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fanssymptomacuityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fanssymptomacuityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fanssymptomacuityenum')">×</button>
<h3><code>FansSymptomAcuityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Acute</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chronic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyperacute</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subacute</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-founderpopulationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-founderpopulationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-founderpopulationenum')">×</button>
<h3><code>FounderPopulationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ammish/Mennonite/Hutterite</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brazilian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dutch</code></td><td><code></code></td><td></td></tr>
<tr><td><code>French Canadian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gypsy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Indian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Jewish (Ashkenazi)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mixe</code></td><td><code></code></td><td></td></tr>
<tr><td><code>South Asian</code></td><td><code></code></td><td></td></tr>
<tr><td><code>South African</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-frequencyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-frequencyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-frequencyenum')">×</button>
<h3><code>FrequencyEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>As needed</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Before every meal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Before meals and at bedtime</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 2 weeks</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 3 months</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 4 weeks</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 6 months</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 6 weeks</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every 8 weeks</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every night at bedtime</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every other day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Every week</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Four times a day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Once</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Once per day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Three times a day</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Two times a day</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Visual Acuity</code></td><td><code>ncit:C87149</code></td><td></td></tr>
<tr><td><code>Visual Evoked Potentials</code></td><td><code>ncit:C191332</code></td><td></td></tr>
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
<tr><td><code>ms</code></td><td><code>ncit:C41140</code></td><td></td></tr>
<tr><td><code>micrometer</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Asked But Declined</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Female-to-male transsexual</code></td><td><code>SCTID:407377005</code></td><td></td></tr>
<tr><td><code>Identifies As Female Gender</code></td><td><code>SCTID:446141000124107</code></td><td></td></tr>
<tr><td><code>Identifies As Male Gender</code></td><td><code>SCTID:446151000124109</code></td><td></td></tr>
<tr><td><code>Identifies As Nonbinary Gender</code></td><td><code>SCTID:33791000087105</code></td><td></td></tr>
<tr><td><code>Male-To-Female Transsexual</code></td><td><code>SCTID:407377005</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Cytogenetics, Microarray, SNP Array</code></td><td><code>ncit:C116151</code></td><td></td></tr>
<tr><td><code>Cytogenetics, Microarray, aCGH</code></td><td><code>ncit:C18084</code></td><td></td></tr>
<tr><td><code>DNA Methylation, Array</code></td><td><code>ncit:C165222</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, ATAC-seq</code></td><td><code>ncit:C156056</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Long-Read, Nanopore</code></td><td><code>ncit:C146818</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Long-Read, SMRT</code></td><td><code>ncit:C146819</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, NOS</code></td><td><code>ncit:C101293</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, RNA-seq</code></td><td><code>ncit:C124261</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Single Cell RNA-seq</code></td><td><code>ncit:C171152</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Single Gene (DNA)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Targeted DNA Panel</code></td><td><code>ncit:C158253</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Total RNA</code></td><td><code>ncit:C124261</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Exome</code></td><td><code>ncit:C101295</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Genome</code></td><td><code>ncit:C101294</code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Western Blot</code></td><td><code>ncit:C16357</code></td><td></td></tr>
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
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Buccal Swab</code></td><td><code>ncit:C113747</code></td><td></td></tr>
<tr><td><code>Buffy Coat</code></td><td><code>ncit:C84507</code></td><td></td></tr>
<tr><td><code>Chorionic Villus Sampling</code></td><td><code>ncit:C92755</code></td><td></td></tr>
<tr><td><code>Cord Blood</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fetal Amniocytes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Lymphoblastoid Cell Line</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nails</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peripheral Blood Lymphocytes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Potentially Malignant Lesion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fibroblast</code></td><td><code>ncit:C12482</code></td><td></td></tr>
<tr><td><code>Saliva</code></td><td><code>ncit:C174119</code></td><td>(pre) ConsortiumNote: Map to Buccal Swab/Saliva</td></tr>
<tr><td><code>Tissue (Non-Neoplastic)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Primary Tumor</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Metastatic Tumor</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Muscles and Joints</code></td><td><code>ncit:C12463</code></td><td></td></tr>
<tr><td><code>Nails</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Mucosa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Scalp and Body Hair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>System NOS &gt;&gt; Well Differentiated</code></td><td><code>ncit:C28077</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Moderately Differentiated</code></td><td><code>ncit:C28078</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Poorly Differentiated</code></td><td><code>ncit:C28079</code></td><td></td></tr>
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
<tr><td><code>Haploidentical</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Match</code></td><td><code>ncit:C129972</code></td><td></td></tr>
<tr><td><code>Non-Match</code></td><td><code>ncit:C126298</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hpvstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hpvstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hpvstatusenum')">×</button>
<h3><code>HpvStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Negative</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Positive</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>ALT</code></td><td><code>ncit:C64433</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>ANA</code></td><td><code>ncit:C176313</code></td><td></td></tr>
<tr><td><code>AQP4 Ab</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AST</code></td><td><code>ncit:C64467</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Absolute B Lymphocyte Count</code></td><td><code>ncit:C201188</code></td><td>(fa) ConsortiumNote: METHOD = 'Flow Cytometry'</td></tr>
<tr><td><code>Absolute Basophil Count</code></td><td><code>ncit:C64470</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Absolute Blood Lymphocyte Count</code></td><td><code>ncit:C113237</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Absolute Eosinophil Count</code></td><td><code>ncit:C188680</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Absolute Monocyte Count</code></td><td><code>ncit:C181278</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Alkaline Phophatase</code></td><td><code>ncit:C64432</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Angiotension Converting Enzyme</code></td><td><code>ncit:C80169</code></td><td></td></tr>
<tr><td><code>Autoantibodies, NOS</code></td><td><code>ncit:C181397</code></td><td></td></tr>
<tr><td><code>Basophils</code></td><td><code>ncit:C64470</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Blast Count</code></td><td><code>ncit:C74605</code></td><td>(fa) ConsortiumNote: CBC or Bone Marrow</td></tr>
<tr><td><code>Blood Urea Nitrogen</code></td><td><code>ncit:C61019</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>CD19+ B Cells</code></td><td><code>ncit:C201193</code></td><td></td></tr>
<tr><td><code>CD3+ T Cells</code></td><td><code>ncit:C201180</code></td><td></td></tr>
<tr><td><code>CD4+ T Cells</code></td><td><code>ncit:C201182</code></td><td></td></tr>
<tr><td><code>CD8+ T Cells</code></td><td><code>ncit:C201184</code></td><td></td></tr>
<tr><td><code>CRP</code></td><td><code>ncit:C64548</code></td><td></td></tr>
<tr><td><code>CSF Luekocyte Count</code></td><td><code>ncit:C168921</code></td><td>(fa) ConsortiumNote: CSF Studies</td></tr>
<tr><td><code>CSF RBC Count</code></td><td><code>ncit:C168920</code></td><td>(fa) ConsortiumNote: CSF Studies</td></tr>
<tr><td><code>Cellularity</code></td><td><code>ncit:C111153</code></td><td></td></tr>
<tr><td><code>Chromosome Breakage, DEB</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chromosome Breakage, DEB/MMC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chromosome Breakage, MMC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chromosome Breakage, Treated (unknown agent)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chromosome Breakage, Untreated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Creatinine</code></td><td><code>ncit:C64547</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>Dysplasia</code></td><td><code>ncit:C204680</code></td><td></td></tr>
<tr><td><code>ESR</code></td><td><code>ncit:C74611</code></td><td></td></tr>
<tr><td><code>Eosinophils</code></td><td><code>ncit:C64550</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Erythroid Precursors Count</code></td><td><code>ncit:C187802</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Glucose</code></td><td><code>ncit:C105585</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>Granulomas</code></td><td><code>ncit:C176334</code></td><td></td></tr>
<tr><td><code>HIV-1 Ab</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hematocrit Measurement</code></td><td><code>ncit:C64796</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Hemoglobin</code></td><td><code>ncit:C64848</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Hemoglobin A1c Measurement</code></td><td><code>ncit:C64849</code></td><td></td></tr>
<tr><td><code>Histiocytes</code></td><td><code>ncit:C12563</code></td><td></td></tr>
<tr><td><code>IgA</code></td><td><code>ncit:C198278</code></td><td></td></tr>
<tr><td><code>IgD</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IgE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IgG</code></td><td><code>ncit:C198279</code></td><td></td></tr>
<tr><td><code>IgG1</code></td><td><code>ncit:C204624</code></td><td></td></tr>
<tr><td><code>IgG2</code></td><td><code>ncit:C204625</code></td><td></td></tr>
<tr><td><code>IgG3</code></td><td><code>ncit:C204626</code></td><td></td></tr>
<tr><td><code>IgG4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IgM</code></td><td><code>ncit:C198280</code></td><td></td></tr>
<tr><td><code>Immature Granulocytes</code></td><td><code>ncit:C100445</code></td><td>(fa) ConsortiumNote: CBC with Differential</td></tr>
<tr><td><code>Infectious Diseases, NOS</code></td><td><code>ncit:C26726</code></td><td></td></tr>
<tr><td><code>JCV</code></td><td><code>ncit:C199960</code></td><td></td></tr>
<tr><td><code>Kappa to Lambda Ratio</code></td><td><code>ncit:C161351</code></td><td>(fa) ConsortiumNote: METHOD = 'Flow Cytometry'</td></tr>
<tr><td><code>LDL</code></td><td><code>ncit:C189506</code></td><td>(fa) ConsortiumNote: Lipid Testing</td></tr>
<tr><td><code>Lactage Dehydrogenase</code></td><td><code>ncit:C64855</code></td><td></td></tr>
<tr><td><code>Leukocyte Count</code></td><td><code>ncit:C51948</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Lymphoid Aggregates</code></td><td><code>ncit:C187947</code></td><td></td></tr>
<tr><td><code>MCH</code></td><td><code>ncit:C64797</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>MCHC</code></td><td><code>ncit:C64798</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>MCV</code></td><td><code>ncit:C64799</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Mast Cell Count</code></td><td><code>ncit:C111246</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Megakaryocytes Count</code></td><td><code>ncit:C96688</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Monocyte Count</code></td><td><code>ncit:C64823</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Myeloblast Count</code></td><td><code>ncit:C74632</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Myelocyte Count</code></td><td><code>ncit:C74662</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Myeloid Cell Count</code></td><td><code>ncit:C184425</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Myeloid to Erythroid Ratio Measurement</code></td><td><code>ncit:C92242</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Natural Killer Cells to Lymphocytes Ratio Measurement</code></td><td><code>ncit:C181258</code></td><td>(fa) ConsortiumNote: METHOD = 'Flow Cytometry'</td></tr>
<tr><td><code>Neutrophil Band Form Count</code></td><td><code>ncit:C64830</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Neutrophil Count</code></td><td><code>ncit:C51950</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Oligoclonal Bands</code></td><td><code>ncit:C122139</code></td><td>(fa) ConsortiumNote: CSF Studies</td></tr>
<tr><td><code>Opening Pressure</code></td><td><code>ncit:C180559</code></td><td>(fa) ConsortiumNote: CSF Studies</td></tr>
<tr><td><code>Plasma Cells</code></td><td><code>ncit:C128974</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Promyelocyte Count</code></td><td><code>ncit:C74622</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Protein Total</code></td><td><code>ncit:C64858</code></td><td></td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C51946</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Reticulocyte Count</code></td><td><code>ncit:C51947</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Reticulocyte Mean Corpuscular Volume</code></td><td><code>ncitC114215</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Retinal Nerve Fiber Layer Thickness</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ringed Sideroblasts</code></td><td><code>ncit:C100419</code></td><td>(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'</td></tr>
<tr><td><code>Segmented Neutrophils</code></td><td><code>ncit:C81997</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Sodium</code></td><td><code>ncit:C64809</code></td><td>(fa) ConsortiumNote: Basic Metabolic Panel</td></tr>
<tr><td><code>Total Bilirubin</code></td><td><code>ncit:C38037</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>Total Cholesterol</code></td><td><code>ncit:C61032</code></td><td>(fa) ConsortiumNote: Lipid Testing</td></tr>
<tr><td><code>Triglyceride Measurement</code></td><td><code>ncit:C64812</code></td><td>(fa) ConsortiumNote: Lipid Testing</td></tr>
<tr><td><code>Vitamin D 25</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Flow Cytometry</code></td><td><code>ncit:C16585</code></td><td></td></tr>
<tr><td><code>Morphology/Histology</code></td><td><code>ncit:C17943</code></td><td></td></tr>
<tr><td><code>Ploidy</code></td><td><code>ncit:C18303</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>g/dL</code></td><td><code>ncit:C64783</code></td><td></td></tr>
<tr><td><code>mg/L</code></td><td><code>ncit:C64572</code></td><td></td></tr>
<tr><td><code>mg/dL</code></td><td><code>ncit:C67015</code></td><td></td></tr>
<tr><td><code>mm/h</code></td><td><code>ncit:C67419</code></td><td></td></tr>
<tr><td><code>mmol/L</code></td><td><code>ncit:C64387</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone Marrow Aspirate</code></td><td><code>ncit:C133261</code></td><td></td></tr>
<tr><td><code>Bone Marrow Core/Trephine Biopsy</code></td><td><code>ncit:C159488</code></td><td></td></tr>
<tr><td><code>Buccal Mucosa</code></td><td><code>ncit:C12505</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Cervical Specimen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chorionic Villus Sampling</code></td><td><code>ncit:C92755</code></td><td></td></tr>
<tr><td><code>Cord Blood</code></td><td><code>ncit:C13300</code></td><td></td></tr>
<tr><td><code>Fetal Amniocytes</code></td><td><code>ncit:C12497</code></td><td></td></tr>
<tr><td><code>Oral Brush Lesion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Brush Normal Appearing Mucosa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peritoneal Fluid</code></td><td><code>ncit:C185197</code></td><td></td></tr>
<tr><td><code>Plasma</code></td><td><code>ncit:C185204</code></td><td></td></tr>
<tr><td><code>Primary Fibroblast</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Saliva</code></td><td><code>ncit:C174119</code></td><td></td></tr>
<tr><td><code>Serum</code></td><td><code>ncit:C178987</code></td><td></td></tr>
<tr><td><code>Stool Sample</code></td><td><code>ncit:C189125</code></td><td></td></tr>
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

<div id="enum-modal-marginsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-marginsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-marginsenum')">×</button>
<h3><code>MarginsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Biopsy Only</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Incomplete Resection</code></td><td><code>ncit:C182305</code></td><td></td></tr>
<tr><td><code>No Surgical Resection</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-medicationdoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationdoseunitenum')">×</button>
<h3><code>MedicationDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>AUC</code></td><td><code>ncit:C64774</code></td><td></td></tr>
<tr><td><code>g</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IU</code></td><td><code>ncit:C48579</code></td><td></td></tr>
<tr><td><code>IU/m2</code></td><td><code>ncit:C67378</code></td><td></td></tr>
<tr><td><code>mcg</code></td><td><code>ncit:C48152</code></td><td></td></tr>
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
<tr><td><code>Abemaciclib</code></td><td><code>ncit:C97660</code></td><td></td></tr>
<tr><td><code>Acetylcysteine</code></td><td><code>ncit:C200</code></td><td></td></tr>
<tr><td><code>Adalimumab</code></td><td><code>ncit:C65216</code></td><td></td></tr>
<tr><td><code>Alemtuzumab (Campath)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Alpelisib</code></td><td><code>ncit:C94214</code></td><td></td></tr>
<tr><td><code>Amsacrine</code></td><td><code>ncit:C240</code></td><td></td></tr>
<tr><td><code>Anakinra</code></td><td><code>ncit:C38717</code></td><td></td></tr>
<tr><td><code>Anastrozole</code></td><td><code>ncit;C1607</code></td><td></td></tr>
<tr><td><code>Anti-thymocyte Globulin</code></td><td><code>ncit:C278</code></td><td></td></tr>
<tr><td><code>Aspirin</code></td><td><code>ncit:C287</code></td><td></td></tr>
<tr><td><code>Bilnatumomab</code></td><td><code>ncit:</code></td><td></td></tr>
<tr><td><code>Brentuximab Vedotin</code></td><td><code>ncit:C66944</code></td><td></td></tr>
<tr><td><code>Briquilimab</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Capivasertib</code></td><td><code>ncit:C102564</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cetuximab</code></td><td><code>rxcui:318341</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cladribine</code></td><td><code>ncit:C1336</code></td><td></td></tr>
<tr><td><code>Clofarabine</code></td><td><code>ncit:C26638</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cytarabine</code></td><td><code>rxcui:3041</code></td><td></td></tr>
<tr><td><code>DTaP (Diphtheria and tetanus)</code></td><td><code>ncit:C91718</code></td><td></td></tr>
<tr><td><code>Danazol</code></td><td><code>ncit:C414</code></td><td></td></tr>
<tr><td><code>Daunorubicin</code></td><td><code>rxcui:3109</code></td><td></td></tr>
<tr><td><code>Daunorubicin (Liposomal)</code></td><td><code>ncit:C2213</code></td><td></td></tr>
<tr><td><code>Daunorubicin and Cytarabine (Liposomal)</code></td><td><code>ncit:C67504</code></td><td></td></tr>
<tr><td><code>Dexamethasone</code></td><td><code>ncit:C422</code></td><td></td></tr>
<tr><td><code>Dexrazoxane</code></td><td><code>ncit:C1333</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Elacestrant</code></td><td><code>rxcui:2628483</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Exemestane</code></td><td><code>ncit:C1097</code></td><td></td></tr>
<tr><td><code>Fludarabine</code></td><td><code>ncit:C1094</code></td><td></td></tr>
<tr><td><code>Fulvestrant</code></td><td><code>ncit:C1379</code></td><td></td></tr>
<tr><td><code>GCSF</code></td><td><code>ncit:C26078</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Gemtuzumab Ozogamicin</code></td><td><code>ncit:C1806</code></td><td></td></tr>
<tr><td><code>Gilteritinib</code></td><td><code>ncit:C116722</code></td><td></td></tr>
<tr><td><code>Golimumab</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HER2 Inhibitor</code></td><td><code>ncit:C159156</code></td><td></td></tr>
<tr><td><code>HepA (Hepatitis A)</code></td><td><code>ncit:C29090</code></td><td></td></tr>
<tr><td><code>HepB (Hepatitis B)</code></td><td><code>ncit:C29091</code></td><td></td></tr>
<tr><td><code>HiB (Haemophilus influenza type B)</code></td><td><code>ncit:C1126</code></td><td></td></tr>
<tr><td><code>Human Papilloma Virus Vaccine</code></td><td><code>ncit:C1951</code></td><td></td></tr>
<tr><td><code>Hydrocortisone Sodium Succinate</code></td><td><code>ncit:C1819</code></td><td></td></tr>
<tr><td><code>IPV (Poliovirus)</code></td><td><code>ncit:C91715</code></td><td></td></tr>
<tr><td><code>Idarubicin</code></td><td><code>rxcui:5650</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Influenza</code></td><td><code>ncit:C178427</code></td><td></td></tr>
<tr><td><code>Inotuzumab Ozogamicin</code></td><td><code>ncit:C71542</code></td><td></td></tr>
<tr><td><code>Intravenous Immunoglobulin Therapy</code></td><td><code>ncit:C121331</code></td><td></td></tr>
<tr><td><code>Lapatinib</code></td><td><code>ncit:C26653</code></td><td></td></tr>
<tr><td><code>Letrozole</code></td><td><code>rxcui:72965</code></td><td></td></tr>
<tr><td><code>MCV4 (Meningococcal)</code></td><td><code>ncit:C96397</code></td><td></td></tr>
<tr><td><code>MMR (Measles, Mumps, &amp; Rubella)</code></td><td><code>ncit:C96403</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Methylprednisolone</code></td><td><code>ncit:C166880</code></td><td>(fa) ConsortiumNote: Also known as IVMP</td></tr>
<tr><td><code>Midostaurin</code></td><td><code>ncit:C1872</code></td><td></td></tr>
<tr><td><code>Monoclonal Antibody</code></td><td><code>ncit:C20401</code></td><td></td></tr>
<tr><td><code>Mycophenolate Mofetil</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neratinib</code></td><td><code>ncit:C49094</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Olaparib</code></td><td><code>rxcui:1597582</code></td><td></td></tr>
<tr><td><code>PCV (Pneumococcal)</code></td><td><code>ncit:C97123</code></td><td></td></tr>
<tr><td><code>Paclitaxel</code></td><td><code>ncit:C1411</code></td><td></td></tr>
<tr><td><code>Palbociclib</code></td><td><code>ncit:C49176</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Pertuzumab</code></td><td><code>ncit:C38692</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Progestogen</code></td><td><code>ncit:C2296</code></td><td></td></tr>
<tr><td><code>RV (Rotavirus)</code></td><td><code>ncit:C96394</code></td><td></td></tr>
<tr><td><code>Ribociclib</code></td><td><code>rxcui:1873986</code></td><td></td></tr>
<tr><td><code>Rituximab</code></td><td><code>rxcui:121191</code></td><td></td></tr>
<tr><td><code>Sacituzumab Govitecan</code></td><td><code>rxcui:2360537</code></td><td></td></tr>
<tr><td><code>Sirolimus</code></td><td><code>rxcui:35302</code></td><td></td></tr>
<tr><td><code>Sorafenib</code></td><td><code>ncit:C61948</code></td><td></td></tr>
<tr><td><code>Tacrolimus</code></td><td><code>ncit:C1311</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Talazoparib</code></td><td><code>rxcui:2099949</code></td><td></td></tr>
<tr><td><code>Tamoxifen</code></td><td><code>rxcui:10324</code></td><td></td></tr>
<tr><td><code>Tdap (Tetanus, diphtheria, &amp; acellular pertussis)</code></td><td><code>ncit:C91717</code></td><td></td></tr>
<tr><td><code>Therapuetic Growth Hormone</code></td><td><code>ncit:C164163</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>rxcui:10473</code></td><td></td></tr>
<tr><td><code>Thyroxine</code></td><td><code>ncit:C2302</code></td><td></td></tr>
<tr><td><code>Tisotumab Vedotin</code></td><td><code>ncit:C113164</code></td><td></td></tr>
<tr><td><code>Tocilizumab</code></td><td><code>ncit:C84217</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Trastuzumab</code></td><td><code>rxcui:224905</code></td><td></td></tr>
<tr><td><code>Trastuzumab Deruxtecan</code></td><td><code>ncit:C128799</code></td><td></td></tr>
<tr><td><code>Trastuzumab Emtansine</code></td><td><code>ncit:C82492</code></td><td></td></tr>
<tr><td><code>Tretinoin</code></td><td><code>ncit:C900</code></td><td></td></tr>
<tr><td><code>Triiodothyronine</code></td><td><code>ncit:C2303</code></td><td></td></tr>
<tr><td><code>Tucatinib</code></td><td><code>ncit:C77896</code></td><td></td></tr>
<tr><td><code>VAR (Varicella)</code></td><td><code>ncit:C77799</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>ZOS (Zoster/Shingles)</code></td><td><code>ncit:C71079</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Adequate for Analysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hemodiluated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inadequate for Analysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Indeterminate</code></td><td><code>ncit:C48658</code></td><td></td></tr>
<tr><td><code>Non-Viable Tumor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small Amount</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Viable Tumor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-parentalstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-parentalstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-parentalstatusenum')">×</button>
<h3><code>ParentalStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>De Novo</code></td><td><code>ncit:C93106</code></td><td></td></tr>
<tr><td><code>Maternally Inherited</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paternally Inherited</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-phenosenum" class="enum-modal" onclick="closeEnumModal('enum-modal-phenosenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-phenosenum')">×</button>
<h3><code>PhenosEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye Abnormality</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]</td></tr>
<tr><td><code>Genitalia Abnormality</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]</td></tr>
<tr><td><code>Microcephaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[6=microcephaly]</td></tr>
<tr><td><code>Nervous System Abnormality</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Neurological abnormalities]</td></tr>
<tr><td><code>Otological Abnormality</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Israel].[Ear Anomaly]<br>(fa) ConsortiumNote:  [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Ears/Hearing]</td></tr>
<tr><td><code>Short Stature</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Growth]</td></tr>
<tr><td><code>Skin Pigmentation</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Skin]</td></tr>
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
<tr><td><code>Anal Repair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Appendectomy</code></td><td><code>ncit:C51687</code></td><td></td></tr>
<tr><td><code>Cardiac Repair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cervical Decompression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Coloproctostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Colposcopy/Leep</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Conization</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Continent Ileostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Creation of Ileal Reservoir (S or J)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Creation of Mucofistula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Debulking (radical dissection)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Destruction of Lesion(s), extensive</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Destruction of Lesion(s), simple</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Diagnostic Laparoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enterolysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enterostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Esophageal Repair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Esophagogastrectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Exploratory Laparotomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Extracorporeal Photopheresis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hartmann Type Procedure</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hemiglossectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hemivulvectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ileocolostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ileostomy or Ileoproctostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inguinofemoral Lymphadenectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Appendectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Assisted Vaginal Hysterectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Enterectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Enterolysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopy with Aspiration of Cavity or Cyst</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Partial Colectomy Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopic Partial Colectomy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laryngopharyngectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leep conization</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Level II-V Dissection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Limited Para-aortic Lymphadenectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lobectomy</code></td><td><code></code></td><td>(ews) ConsortiumNote: Resection procedure (for metastatic disease).<br>(os) ConsortiumNote: Resection procedure (for metastatic disease).</td></tr>
<tr><td><code>Lumbar Decompression</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Maxillectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck Dissection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Omentectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oophorectomy, NOS</code></td><td><code>ncit:C15291</code></td><td></td></tr>
<tr><td><code>Paratrachial Node Dissection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Colectomy with Anastomosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Colectomy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Glossectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Mandibulectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partial Pharyngectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Para-aortic Lymph Node Sampling</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvic Lymphadenectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharingolaryngocervicalesophagectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pharyngotomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Proctectomy</code></td><td><code>ncit:C15300</code></td><td></td></tr>
<tr><td><code>Radical Cystoprostatectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radical Hysterectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radical Neck Dissection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radical Trachelectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Removal of Paravaginal Tissue (radical)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Removal of Terminal Ileum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Resection, with Colostomy or Ileostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneal Sampling</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Salpingectomy</code></td><td><code>ncit:C51605</code></td><td></td></tr>
<tr><td><code>Skin Level Cecostomy or Colostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subtotal Glossectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thoracotomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Abdominal Hysterectomy</code></td><td><code>ncit:C51695</code></td><td></td></tr>
<tr><td><code>Total Colectomy, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Esophagectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Laparoscopic Hysterectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Laryngectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheostomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tracheo-esophageal Repair</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ureterolysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginectomy, Complete</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vaginectomy, Partial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ventriculoperitoneal Shunt Placement</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulvectomy, Radical, Partial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulvectomy, Radical, Complete</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulvectomy, Simple, Complete</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulvectomy, Simple, Partial</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdominal Skin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Arm Skin</code></td><td><code>ncit:C52754</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Buccal Mucosa</code></td><td><code>ncit:C12505</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Ear Skin</code></td><td><code>ncit:C49481</code></td><td></td></tr>
<tr><td><code>Esophagus</code></td><td><code>ncit:C12389</code></td><td></td></tr>
<tr><td><code>Fallopian Tube</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gingiva, Lower, Anterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Lower, Posterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, NOS</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Upper, Anterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Gingiva, Upper, Posterior</code></td><td><code>ncit:C32677</code></td><td></td></tr>
<tr><td><code>Glottis</code></td><td><code>ncit:C12724</code></td><td></td></tr>
<tr><td><code>Hand Skin</code></td><td><code>ncit:C52753</code></td><td></td></tr>
<tr><td><code>Hilar Nodes</code></td><td><code>ncit:C102330</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Intestine</code></td><td><code>ncit:C12736</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Leg Skin</code></td><td><code>ncit:C52749</code></td><td></td></tr>
<tr><td><code>Lip</code></td><td><code>ncit:C12220</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Mediastinal Node</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck Skin</code></td><td><code>ncit:C52756</code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code>ncit:C12421</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Palate</code></td><td><code>ncit:C12229</code></td><td></td></tr>
<tr><td><code>Paratracheal Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Penis</code></td><td><code>ncit:C12409</code></td><td></td></tr>
<tr><td><code>Pharynx</code></td><td><code>ncit:C12425</code></td><td></td></tr>
<tr><td><code>Primary Peritoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pyriform Sinus</code></td><td><code>ncit:C33439</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Skin of the Back</code></td><td><code>ncit:C142318</code></td><td></td></tr>
<tr><td><code>Skin of the Chest</code></td><td><code>ncit:C161379</code></td><td></td></tr>
<tr><td><code>Skin of the Face</code></td><td><code>ncit:C33561</code></td><td></td></tr>
<tr><td><code>Skin of the Lip</code></td><td><code>ncit:C12291</code></td><td></td></tr>
<tr><td><code>Skin of the Upper Limb and Shoulder</code></td><td><code>ncit:C12296</code></td><td></td></tr>
<tr><td><code>Skin, NOS</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Small Bowel</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Small Intestine</code></td><td><code>ncit:C12386</code></td><td></td></tr>
<tr><td><code>Spinal Cord</code></td><td><code>ncit:C12464</code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code>ncit:C12391</code></td><td></td></tr>
<tr><td><code>Submandibular</code></td><td><code>ncit:C129462</code></td><td></td></tr>
<tr><td><code>Tongue</code></td><td><code>ncit:C12422</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code>ncit:C12405</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vaginal Mucosa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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

<div id="enum-modal-relationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-relationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-relationenum')">×</button>
<h3><code>RelationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Aunt</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brother</code></td><td><code>ncit:C96570</code></td><td></td></tr>
<tr><td><code>Cousin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Daughter</code></td><td><code>ncit:C150887</code></td><td></td></tr>
<tr><td><code>Father</code></td><td><code>ncit:C96572</code></td><td></td></tr>
<tr><td><code>Mother</code></td><td><code>ncit:C96580</code></td><td></td></tr>
<tr><td><code>Second degree relative, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sister</code></td><td><code>ncit:C96586</code></td><td></td></tr>
<tr><td><code>Son</code></td><td><code>ncit:C150888</code></td><td></td></tr>
<tr><td><code>Uncle</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Intramuscular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrathecal</code></td><td><code>ncit:C173292</code></td><td></td></tr>
<tr><td><code>Intravenously</code></td><td><code>ncit:C38276</code></td><td></td></tr>
<tr><td><code>Oral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subcutaneous</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Systemic</code></td><td><code>ncit:C173291</code></td><td></td></tr>
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
<tr><td><code>Gross Tumor Volume</code></td><td><code>ncit:C192975</code></td><td></td></tr>
<tr><td><code>Thoracoabdominal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Body</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Total Lymphoid</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-siteclassificationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-siteclassificationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-siteclassificationenum')">×</button>
<h3><code>SiteClassificationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Benign</code></td><td><code>ncit:C14172</code></td><td></td></tr>
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

<div id="enum-modal-sourcelabenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sourcelabenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sourcelabenum')">×</button>
<h3><code>SourceLabEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cincinnati Children's Hospital Medical Center</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dana-Farber Cancer Institute</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GeneDX</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Invitae</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Julius-Maximilians-Universität of Würzburg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laboratorio de Citogenética, Instituto Nacional de Pediatría, México</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prevention Genetics</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Quest Diagnostics</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stanford University</code></td><td><code></code></td><td></td></tr>
<tr><td><code>The Rockefeller University</code></td><td><code></code></td><td></td></tr>
<tr><td><code>University of Chicago</code></td><td><code></code></td><td></td></tr>
<tr><td><code>University of Minnesota</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stagecategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stagecategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stagecategoryenum')">×</button>
<h3><code>StageCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clinical</code></td><td><code>ncit:C200641</code></td><td></td></tr>
<tr><td><code>Pathologic</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Ann Arbor &gt;&gt; Stage 1</code></td><td><code>ncit:C8071</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 2</code></td><td><code>ncit:C8116</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 3</code></td><td><code>ncit:C8129</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 4</code></td><td><code>ncit:C8142</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 1</code></td><td><code>ncit:C27966</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 2</code></td><td><code>ncit:C28054</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 3</code></td><td><code>ncit:C27970</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 4</code></td><td><code>ncit:C27971</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 4S</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 1</code></td><td><code>ncit:C96244</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 2</code></td><td><code>ncit:C96252</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 3</code></td><td><code>ncit:C96255</code></td><td></td></tr>
<tr><td><code>FIGO &gt;&gt; Stage 4</code></td><td><code>ncit:C96261</code></td><td></td></tr>
<tr><td><code>INRGSS &gt;&gt; Stage L1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRGSS &gt;&gt; Stage L2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRGSS &gt;&gt; Stage M</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRGSS &gt;&gt; Stage Ms</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 2a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 2b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INSS &gt;&gt; Stage 4s</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 3a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 3b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 4a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Stage 4b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System &gt;&gt; Group 1</code></td><td><code>C148012</code></td><td></td></tr>
<tr><td><code>Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System &gt;&gt; Group 2</code></td><td><code>C148015</code></td><td></td></tr>
<tr><td><code>Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System &gt;&gt; Stage 3</code></td><td><code>C148019</code></td><td></td></tr>
<tr><td><code>Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System &gt;&gt; Stage 4</code></td><td><code>C148022</code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M+</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M0</code></td><td><code>ncit:C48699</code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M0 / M1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M1</code></td><td><code>ncit:C48700</code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified Chang Staging &gt;&gt; M4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Localized</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Metastatic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Regionally Advanced</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stemcellprocessingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stemcellprocessingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stemcellprocessingenum')">×</button>
<h3><code>StemCellProcessingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>None</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T Cell Depleted, CD34 Enriched</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T Cell Depleted, TCRab Depleted</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Mobilized Peripheral Blood Stem Cells</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Anogenital Cancer Database</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == The Rockefeller University</td></tr>
<tr><td><code>BC Oral Cancer Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == BC Cancer</td></tr>
<tr><td><code>Clinical features and outcome of patients with Fanconi's anemia, CMCL</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Christian Medical College and Hospital</td></tr>
<tr><td><code>CMC Vellore FA Registry</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fanconi Anemia Patient Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Fanconi Cancer Foundation</td></tr>
<tr><td><code>GenRare</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == CIBER</td></tr>
<tr><td><code>Indraprastha Apollo Hospital Fanconi Anemia Patient Database</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Indraprastha Apollo Hospital; Manipal Hospital Dwarka New Delhi</td></tr>
<tr><td><code>International Fanconi Anemia Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == The Rockefeller University</td></tr>
<tr><td><code>Mazumdar Shaw Medical Centrem Bangalore Fanconi Anemia Patient Database</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Mazumdar Shaw Medical Centrem Bengalore</td></tr>
<tr><td><code>Medanta Gurugram Fanconi Anemia Patient Database</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Medanta Gurugram</td></tr>
<tr><td><code>NCI 001109</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == National Cancer Institute</td></tr>
<tr><td><code>NCI 02-C-0052</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == National Cancer Institute</td></tr>
<tr><td><code>RAFMex</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Instituto Nacional de Pediatria</td></tr>
<tr><td><code>Registry of the Deutsche Fanconi-Anämie-Hilfe e.V.</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Deutsche Fanconi Anämie-Hilfe e.V.</td></tr>
<tr><td><code>Schneider Children's Medical Center Fanconi Anemia Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Schneider Children's Medical Center</td></tr>
<tr><td><code>Shalby Sanar International Hospital Fanconi Anemia Patient Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Shalby Sanar International Hospital</td></tr>
<tr><td><code>Stanford University Fanconi Anemia Patient Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Stanford University</td></tr>
<tr><td><code>UK Fanconi Anaemia Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == University of Manchester</td></tr>
<tr><td><code>Un Corazón por Fanconi Anemia Patient Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Un Corazón por Fanconi</td></tr>
<tr><td><code>University of Düsseldorf Fanconi Anemia Patient Registry</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == University of Düsseldorf</td></tr>
<tr><td><code>Wayne Crismani Australia Fanconi Anemia Research Study</code></td><td><code></code></td><td>(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == St. Vincent's Institute for Medical Research</td></tr>
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
<tr><td><code>EBRT, Intensity-Modulated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Passive Scattering</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Pencil Beam Scanning</code></td><td><code>ncit:C165502</code></td><td>(npc) ConsortiumNote: ENERGY_TYPE = Proton</td></tr>
<tr><td><code>EBRT, Stereotactic Body</code></td><td><code>ncit:C118286</code></td><td>(npc) ConsortiumNote: Stereotactic ablative body radiotherapy</td></tr>
<tr><td><code>EBRT, Stereotactic Radiosurgery</code></td><td><code>ncit:C15358</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Plasma</code></td><td><code>ncit:C13356</code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C133278</code></td><td></td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C133280</code></td><td></td></tr>
<tr><td><code>Whole Blood</code></td><td><code>ncit:C41067</code></td><td></td></tr>
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
<tr><td><code>Plasmapheresis</code></td><td><code>ncit:C15304</code></td><td></td></tr>
<tr><td><code>Simple Transfusion</code></td><td><code>ncit:C173285</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>MX</code></td><td><code>ncit:C48704</code></td><td></td></tr>
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
<tr><td><code>T1a</code></td><td><code>ncit:C48721</code></td><td></td></tr>
<tr><td><code>T1b</code></td><td><code>ncit:C48722</code></td><td></td></tr>
<tr><td><code>T1c</code></td><td><code>ncit:C48723</code></td><td></td></tr>
<tr><td><code>T2</code></td><td><code>ncit:C48724</code></td><td></td></tr>
<tr><td><code>T2a</code></td><td><code>ncit:C48725</code></td><td></td></tr>
<tr><td><code>T2b</code></td><td><code>ncit:C48726</code></td><td></td></tr>
<tr><td><code>T3a</code></td><td><code>ncit:C48729</code></td><td></td></tr>
<tr><td><code>T3b</code></td><td><code>ncit:C48730</code></td><td></td></tr>
<tr><td><code>T3c</code></td><td><code>ncit:C48731</code></td><td></td></tr>
<tr><td><code>T3d</code></td><td><code>ncit:C148412</code></td><td></td></tr>
<tr><td><code>T3e</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T4</code></td><td><code>ncit:C48732</code></td><td></td></tr>
<tr><td><code>T4a</code></td><td><code>ncit:C48733</code></td><td></td></tr>
<tr><td><code>T4b</code></td><td><code>ncit:C48734</code></td><td></td></tr>
<tr><td><code>T4c</code></td><td><code>ncit:C48735</code></td><td></td></tr>
<tr><td><code>T4d</code></td><td><code>ncit:C48736</code></td><td></td></tr>
<tr><td><code>TX</code></td><td><code>ncit:C48737</code></td><td></td></tr>
<tr><td><code>Tis</code></td><td><code>ncit:C48738</code></td><td></td></tr>
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

<div id="enum-modal-vacterlhenum" class="enum-modal" onclick="closeEnumModal('enum-modal-vacterlhenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-vacterlhenum')">×</button>
<h3><code>VacterlhEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Anal Anomaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[1=anal]</td></tr>
<tr><td><code>Cardiac Structure Anomaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Heart]<br>(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[2=cardiac]</td></tr>
<tr><td><code>Esophageal Duodenal Atresia</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]</td></tr>
<tr><td><code>Hydrocephalus</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [Mexico].[Congenital_anomalies_detected_at_birth].[5=hydrocephalus]</td></tr>
<tr><td><code>Renal Anomaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Israel].[Renal Anomaly]<br>(fa) ConsortiumNote:  [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Kidneys]</td></tr>
<tr><td><code>Tracheo-esophageal Fistula</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[3= tracheoesophageal]</td></tr>
<tr><td><code>Upper Limb Anomaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]<br>(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Thumb/Radius]<br>(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[4= radial ray]</td></tr>
<tr><td><code>Vertebral Anomaly</code></td><td><code></code></td><td>(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]</td></tr>
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
    "fa": {
      "name": "fa",
      "title": "Fanconi Anemia",
      "description": "The FA view of the PCDC data model represents consensus data modeling by an international group of Fanconi Anemia experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Fanconi Research Initiative for Education, Networking, and Data Sharing Consortium (FRIENDS). It is based on the collective requirements of its contributors."
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
        "country"
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
    "ClinicalEpisode": {
      "slots": [
        "disease_phase",
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
    "SurvivalCharacteristics": {
      "slots": [
        "age_at_lkss",
        "age_at_last_follow_up",
        "lkss",
        "lkss_with_disease",
        "cause_of_death",
        "cause_of_death_other",
        "trm_type",
        "trm_type_other",
        "cause_of_death_detail",
        "cause_of_death_detail_other",
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
    "FamilyMedicalHistory": {
      "slots": [
        "condition_state",
        "family_medical_history_condition",
        "relation",
        "lkss_of_relative",
        "age_at_lkss_of_relative",
        "relative_sct_status",
        "number_of_pregnancies",
        "number_of_live_births",
        "number_of_abortions"
      ],
      "comments": [
        "D4CGNote: One observation/row per CONDITION when instantiated",
        "(fa) ConsortiumNote: This table is tiered as Priority."
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
        "exposure_status",
        "sunscreen_use",
        "occupation"
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
        "anthropometric_measurement_result_unit",
        "gestational_age_at_birth"
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
        "laboratory_test_status",
        "laboratory_test",
        "laboratory_test_method",
        "laboratory_test_specimen",
        "laboratory_test_specimen_other",
        "result_text",
        "result_numeric",
        "laboratory_test_result_unit",
        "breakage_source_lab"
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
        "year_at_genetic_analysis",
        "determination_source",
        "source_lab",
        "genetic_analysis_method",
        "genetic_analysis_specimen",
        "genomic_source_class",
        "mosaicism",
        "alteration_type",
        "alteration_effect",
        "gene",
        "hgvs_genomic",
        "hgvs_coding",
        "hgvs_protein",
        "reference_genome",
        "reference_genome_accession",
        "parental_status",
        "reported_significance",
        "external_ref_id_system",
        "external_ref_id",
        "copy_number",
        "allelic_state",
        "founder_population",
        "acmg_based_significance"
      ],
      "comments": [
        "D4CGNote: One observation/row per genetic alteration",
        "(fa) ConsortiumNote: This table is tiered as Priority."
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
        "function_test_laterality"
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
        "stage_category",
        "tnm_tumor_t",
        "tnm_node_n",
        "tnm_metastasis_m",
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
        "assessment_reason",
        "disease_site",
        "site_other",
        "laterality",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "nodes_assessed_number",
        "tumor_number",
        "dysplasia",
        "hpv_status"
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
        "laterality",
        "vacterlh",
        "phenos",
        "vacterlh_phenos_status",
        "clinical_finding",
        "clinical_finding_other",
        "modified_rankin_scale",
        "fans_symptom_acuity"
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
        "procedure_other",
        "procedure_site",
        "site_other",
        "laterality",
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
        "year_at_medication_start",
        "route",
        "medication",
        "medication_other",
        "number_doses",
        "medication_dose_administered",
        "medication_dose_unit",
        "frequency",
        "frequency_other"
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
        "year_at_rt_start",
        "age_at_rt_end",
        "site_classification",
        "rt_site",
        "energy_type",
        "technique",
        "rt_dose",
        "rt_dose_unit",
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
        "year_at_sct",
        "sct_type",
        "stem_cell_source",
        "donor_relationship",
        "hla_match",
        "conditioning_type",
        "cd34_collected",
        "cd34_transplant",
        "chimerism",
        "chimerism_unit",
        "stem_cell_processing",
        "stem_cell_processing_other"
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
        "tmp_product",
        "number_units"
      ],
      "comments": [
        "D4CGNote: One observation/row per transfusion when instantiated.",
        "(fa) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "intervention"
      }
    },
    "AdverseEvents": {
      "slots": [
        "age_at_ae",
        "age_at_ae_resolved",
        "ae_treatment",
        "adverse_event",
        "ae_code",
        "ae_grade",
        "gvhd_acuity",
        "gvhd_organ",
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
    "number_of_pregnancies": {
      "slot_uri": "ncit:C106551",
      "range": "integer",
      "comments": [
        "(fa) ConsortiumNote: ConditionalityStatement: if RELATION = 'Mother'"
      ],
      "annotations": {
        "tier_optional": "fa"
      }
    },
    "chimerism_unit": {
      "slot_uri": "",
      "range": "ChimerismUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "route": {
      "slot_uri": "ncit:C186559",
      "range": "RouteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "sunscreen_use": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fa"
      }
    },
    "procedure_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "age_at_last_follow_up": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_optional": "fa"
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
    "nodes_assessed_number": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "stem_cell_processing": {
      "slot_uri": "",
      "range": "StemCellProcessingEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "year_at_rt_start": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "fraction_dose": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,npc,rb"
      }
    },
    "ae_treatment": {
      "slot_uri": "",
      "range": "AeTreatmentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "gestational_age_at_birth": {
      "slot_uri": "ncit:C124435",
      "range": "integer",
      "comments": [
        "(fa) ConsortiumNote: Gestational age in days."
      ],
      "annotations": {
        "tier_priority": "fa"
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
    "gender_identity": {
      "slot_uri": "",
      "range": "GenderIdentityEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,ls"
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
    "clinical_finding_other": {
      "slot_uri": "",
      "range": "string",
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
    "relative_sct_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fa"
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
    "year_at_genetic_analysis": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
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
    "stage_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt,npc"
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
    "phenos": {
      "slot_uri": "",
      "range": "PhenosEnum",
      "comments": [
        "(fa) ConsortiumNote: Must provide a row for each association.",
        "(fa)  ConsortiumNote: No VACTERLH and PHENOS in the same row"
      ],
      "annotations": {
        "tier_priority": "fa"
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
    "alteration_effect": {
      "slot_uri": "ncit:C204195",
      "range": "AlterationEffectEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "modified_rankin_scale": {
      "slot_uri": "ncit:C111383",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "stage_category": {
      "slot_uri": "ncit:C15608",
      "range": "StageCategoryEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "exposure": {
      "slot_uri": "ncit:C17941",
      "range": "ExposureEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
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
    "reference_genome_accession": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "ls"
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
    "frequency_other": {
      "slot_uri": "",
      "range": "string",
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
    "number_units": {
      "slot_uri": "ncit:C185656",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "parental_status": {
      "slot_uri": "",
      "range": "ParentalStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "founder_population": {
      "slot_uri": "",
      "range": "FounderPopulationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "number_of_live_births": {
      "slot_uri": "ncit:C178141",
      "range": "integer",
      "comments": [
        "(fa) ConsortiumNote: ConditionalityStatement: if RELATION = 'Mother'"
      ],
      "annotations": {
        "tier_optional": "fa"
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
    "laboratory_test_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "frequency": {
      "slot_uri": "",
      "range": "FrequencyEnum",
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
    "age_at_lkss_of_relative": {
      "slot_uri": "ncit:C168844",
      "range": "integer",
      "comments": [],
      "annotations": {
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
    "assessment_reason": {
      "slot_uri": "ncit:C171003",
      "range": "AssessmentReasonEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "age_at_measurement": {
      "slot_uri": "ncit:C154628",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "vacterlh_phenos_status": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "tumor_number": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "dysplasia": {
      "slot_uri": "ncit:C4086",
      "range": "DysplasiaEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "tmp_product": {
      "slot_uri": "ncit:C173287",
      "range": "TmpProductEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "hl"
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
    "chimerism": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "year_at_medication_start": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "acmg_based_significance": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "functional_measurement_result_unit": {
      "slot_uri": "",
      "range": "FunctionalMeasurementResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "year_at_sct": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "laboratory_test_specimen_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "number_of_abortions": {
      "slot_uri": "ncit:C106550",
      "range": "integer",
      "comments": [
        "(fa) ConsortiumNote: ConditionalityStatement: if RELATION = 'Mother'"
      ],
      "annotations": {
        "tier_optional": "fa"
      }
    },
    "occupation": {
      "slot_uri": "ncit:C25193",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "fa"
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
    "tmp_type": {
      "slot_uri": "ncit:C173057",
      "range": "TmpTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "hl"
      }
    },
    "source_lab": {
      "slot_uri": "",
      "range": "SourceLabEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "site_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "lt"
      }
    },
    "vacterlh": {
      "slot_uri": "",
      "range": "VacterlhEnum",
      "comments": [
        "(fa) ConsortiumNote: Must provide a row for each association.",
        "(fa)  ConsortiumNote: No VACTERLH and PHENOS in the same row"
      ],
      "annotations": {
        "tier_priority": "fa"
      }
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
    "breakage_source_lab": {
      "slot_uri": "",
      "range": "BreakageSourceLabEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "reported_significance": {
      "slot_uri": "",
      "range": "ReportedSignificanceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
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
    "function_test_laterality": {
      "slot_uri": "",
      "range": "FunctionTestLateralityEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,fa"
      }
    },
    "clinical_finding": {
      "slot_uri": "",
      "range": "ClinicalFindingEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "donor_relationship": {
      "slot_uri": "ncit:C168869",
      "range": "DonorRelationshipEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_priority": "aml"
      }
    },
    "stem_cell_processing_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "fans_symptom_acuity": {
      "slot_uri": "",
      "range": "FansSymptomAcuityEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "cause_of_death_detail_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "hpv_status": {
      "slot_uri": "",
      "range": "HpvStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "trm_type_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
        "T1a": {
          "meaning": "ncit:C48721",
          "comments": []
        },
        "T1b": {
          "meaning": "ncit:C48722",
          "comments": []
        },
        "T1c": {
          "meaning": "ncit:C48723",
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
        "T3a": {
          "meaning": "ncit:C48729",
          "comments": []
        },
        "T3b": {
          "meaning": "ncit:C48730",
          "comments": []
        },
        "T3c": {
          "meaning": "ncit:C48731",
          "comments": []
        },
        "T3d": {
          "meaning": "ncit:C148412",
          "comments": []
        },
        "T3e": {
          "meaning": "",
          "comments": []
        },
        "T4": {
          "meaning": "ncit:C48732",
          "comments": []
        },
        "T4a": {
          "meaning": "ncit:C48733",
          "comments": []
        },
        "T4b": {
          "meaning": "ncit:C48734",
          "comments": []
        },
        "T4c": {
          "meaning": "ncit:C48735",
          "comments": []
        },
        "T4d": {
          "meaning": "ncit:C48736",
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
    "DeterminationSourceEnum": {
      "permissible_values": {
        "Clinical Testing": {
          "meaning": "ncit:C15791",
          "comments": []
        },
        "Research/Retrospective": {
          "meaning": "",
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
    "RtSiteEnum": {
      "permissible_values": {
        "Gross Tumor Volume": {
          "meaning": "ncit:C192975",
          "comments": []
        },
        "Thoracoabdominal": {
          "meaning": "",
          "comments": []
        },
        "Total Body": {
          "meaning": "",
          "comments": []
        },
        "Total Lymphoid": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "FrequencyEnum": {
      "permissible_values": {
        "As needed": {
          "meaning": "",
          "comments": []
        },
        "Before every meal": {
          "meaning": "",
          "comments": []
        },
        "Before meals and at bedtime": {
          "meaning": "",
          "comments": []
        },
        "Every 2 weeks": {
          "meaning": "",
          "comments": []
        },
        "Every 3 months": {
          "meaning": "",
          "comments": []
        },
        "Every 4 weeks": {
          "meaning": "",
          "comments": []
        },
        "Every 6 months": {
          "meaning": "",
          "comments": []
        },
        "Every 6 weeks": {
          "meaning": "",
          "comments": []
        },
        "Every 8 weeks": {
          "meaning": "",
          "comments": []
        },
        "Every night at bedtime": {
          "meaning": "",
          "comments": []
        },
        "Every other day": {
          "meaning": "",
          "comments": []
        },
        "Every week": {
          "meaning": "",
          "comments": []
        },
        "Four times a day": {
          "meaning": "",
          "comments": []
        },
        "Once": {
          "meaning": "",
          "comments": []
        },
        "Once per day": {
          "meaning": "",
          "comments": []
        },
        "Three times a day": {
          "meaning": "",
          "comments": []
        },
        "Two times a day": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationDoseUnitEnum": {
      "permissible_values": {
        "AUC": {
          "meaning": "ncit:C64774",
          "comments": []
        },
        "g": {
          "meaning": "",
          "comments": []
        },
        "IU": {
          "meaning": "ncit:C48579",
          "comments": []
        },
        "IU/m2": {
          "meaning": "ncit:C67378",
          "comments": []
        },
        "mcg": {
          "meaning": "ncit:C48152",
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
    "VacterlhEnum": {
      "permissible_values": {
        "Anal Anomaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[1=anal]"
          ]
        },
        "Cardiac Structure Anomaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Heart]",
            "(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[2=cardiac]"
          ]
        },
        "Esophageal Duodenal Atresia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]"
          ]
        },
        "Hydrocephalus": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [Mexico].[Congenital_anomalies_detected_at_birth].[5=hydrocephalus]"
          ]
        },
        "Renal Anomaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Israel].[Renal Anomaly]",
            "(fa) ConsortiumNote:  [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Kidneys]"
          ]
        },
        "Tracheo-esophageal Fistula": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[3= tracheoesophageal]"
          ]
        },
        "Upper Limb Anomaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Thumb/Radius]",
            "(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[4= radial ray]"
          ]
        },
        "Vertebral Anomaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]"
          ]
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
        "Flow Cytometry": {
          "meaning": "ncit:C16585",
          "comments": []
        },
        "Morphology/Histology": {
          "meaning": "ncit:C17943",
          "comments": []
        },
        "Ploidy": {
          "meaning": "ncit:C18303",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "ChimerismUnitEnum": {
      "permissible_values": {
        "% of CD34 Cells": {
          "meaning": "",
          "comments": []
        },
        "% of T Cells": {
          "meaning": "",
          "comments": []
        },
        "% of Granulocytes": {
          "meaning": "",
          "comments": []
        },
        "% of White Blood Cells": {
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
        "EBRT, Intensity-Modulated": {
          "meaning": "",
          "comments": []
        },
        "EBRT, NOS": {
          "meaning": "",
          "comments": []
        },
        "EBRT, Passive Scattering": {
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
        "Other": {
          "meaning": "ncit:C17649",
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
    "StageCategoryEnum": {
      "permissible_values": {
        "Clinical": {
          "meaning": "ncit:C200641",
          "comments": []
        },
        "Pathologic": {
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
    "FunctionTestEnum": {
      "permissible_values": {
        "Visual Acuity": {
          "meaning": "ncit:C87149",
          "comments": []
        },
        "Visual Evoked Potentials": {
          "meaning": "ncit:C191332",
          "comments": []
        }
      }
    },
    "ExposureStatusEnum": {
      "permissible_values": {
        "Ever": {
          "meaning": "ncit:C159710",
          "comments": []
        },
        "Never": {
          "meaning": "ncit:C70543",
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
    "HistologyGradeEnum": {
      "permissible_values": {
        "System NOS >> Well Differentiated": {
          "meaning": "ncit:C28077",
          "comments": []
        },
        "System NOS >> Moderately Differentiated": {
          "meaning": "ncit:C28078",
          "comments": []
        },
        "System NOS >> Poorly Differentiated": {
          "meaning": "ncit:C28079",
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
        "Bone Marrow Aspirate": {
          "meaning": "ncit:C133261",
          "comments": []
        },
        "Bone Marrow Core/Trephine Biopsy": {
          "meaning": "ncit:C159488",
          "comments": []
        },
        "Buccal Mucosa": {
          "meaning": "ncit:C12505",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Cervical Specimen": {
          "meaning": "",
          "comments": []
        },
        "Chorionic Villus Sampling": {
          "meaning": "ncit:C92755",
          "comments": []
        },
        "Cord Blood": {
          "meaning": "ncit:C13300",
          "comments": []
        },
        "Fetal Amniocytes": {
          "meaning": "ncit:C12497",
          "comments": []
        },
        "Oral Brush Lesion": {
          "meaning": "",
          "comments": []
        },
        "Oral Brush Normal Appearing Mucosa": {
          "meaning": "",
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
        "Primary Fibroblast": {
          "meaning": "",
          "comments": []
        },
        "Saliva": {
          "meaning": "ncit:C174119",
          "comments": []
        },
        "Serum": {
          "meaning": "ncit:C178987",
          "comments": []
        },
        "Stool Sample": {
          "meaning": "ncit:C189125",
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
        "Muscles and Joints": {
          "meaning": "ncit:C12463",
          "comments": []
        },
        "Nails": {
          "meaning": "",
          "comments": []
        },
        "Oral Mucosa": {
          "meaning": "",
          "comments": []
        },
        "Scalp and Body Hair": {
          "meaning": "",
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
    "StudyIdEnum": {
      "permissible_values": {
        "Anogenital Cancer Database": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == The Rockefeller University"
          ]
        },
        "BC Oral Cancer Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == BC Cancer"
          ]
        },
        "Clinical features and outcome of patients with Fanconi's anemia, CMCL": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Christian Medical College and Hospital"
          ]
        },
        "CMC Vellore FA Registry": {
          "meaning": "",
          "comments": []
        },
        "Fanconi Anemia Patient Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Fanconi Cancer Foundation"
          ]
        },
        "GenRare": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == CIBER"
          ]
        },
        "Indraprastha Apollo Hospital Fanconi Anemia Patient Database": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Indraprastha Apollo Hospital; Manipal Hospital Dwarka New Delhi"
          ]
        },
        "International Fanconi Anemia Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == The Rockefeller University"
          ]
        },
        "Mazumdar Shaw Medical Centrem Bangalore Fanconi Anemia Patient Database": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Mazumdar Shaw Medical Centrem Bengalore"
          ]
        },
        "Medanta Gurugram Fanconi Anemia Patient Database": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Medanta Gurugram"
          ]
        },
        "NCI 001109": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == National Cancer Institute"
          ]
        },
        "NCI 02-C-0052": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == National Cancer Institute"
          ]
        },
        "RAFMex": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Instituto Nacional de Pediatria"
          ]
        },
        "Registry of the Deutsche Fanconi-An\u00e4mie-Hilfe e.V.": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Deutsche Fanconi An\u00e4mie-Hilfe e.V."
          ]
        },
        "Schneider Children's Medical Center Fanconi Anemia Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Schneider Children's Medical Center"
          ]
        },
        "Shalby Sanar International Hospital Fanconi Anemia Patient Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Shalby Sanar International Hospital"
          ]
        },
        "Stanford University Fanconi Anemia Patient Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Stanford University"
          ]
        },
        "UK Fanconi Anaemia Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == University of Manchester"
          ]
        },
        "Un Coraz\u00f3n por Fanconi Anemia Patient Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == Un Coraz\u00f3n por Fanconi"
          ]
        },
        "University of D\u00fcsseldorf Fanconi Anemia Patient Registry": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == University of D\u00fcsseldorf"
          ]
        },
        "Wayne Crismani Australia Fanconi Anemia Research Study": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: DATA_CONTRIBUTOR_ID == St. Vincent's Institute for Medical Research"
          ]
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "ACTH-producing tumor": {
          "meaning": "icdo:8158/3",
          "comments": []
        },
        "ALK positive large B-cell lymphoma": {
          "meaning": "icdo:9737/3",
          "comments": []
        },
        "Ac. myelomonocytic leuk. w abn. mar. eosinophils": {
          "meaning": "icdo:9871/3",
          "comments": []
        },
        "Acidophil adenoma": {
          "meaning": "icdo:8280/0",
          "comments": []
        },
        "Acidophil carcinoma": {
          "meaning": "icdo:8280/3",
          "comments": []
        },
        "Acinar cell carcinoma": {
          "meaning": "icdo:8550/3",
          "comments": []
        },
        "Acinar cell cystadenocarcinoma": {
          "meaning": "icdo:8551/3",
          "comments": []
        },
        "Acral lentiginous melanoma, malig.": {
          "meaning": "icdo:8744/3",
          "comments": []
        },
        "Acute Myeloid Leukemia, NOS": {
          "meaning": "",
          "comments": []
        },
        "Acute basophilic leukemia": {
          "meaning": "icdo:9870/3",
          "comments": []
        },
        "Acute biphenotypic leukemia": {
          "meaning": "icdo:9805/3",
          "comments": []
        },
        "Acute leukemia, NOS": {
          "meaning": "icdo:9801/3",
          "comments": []
        },
        "Acute lymphoblastic leukemia, L2 type, NOS": {
          "meaning": "icdo:9828/3",
          "comments": []
        },
        "Acute megakaryoblastic leukemia": {
          "meaning": "icdo:9910/3",
          "comments": []
        },
        "Acute monocytic leukemia": {
          "meaning": "icdo:9891/3",
          "comments": []
        },
        "Acute myeloid leuk. with multilineage dysplasia": {
          "meaning": "icdo:9895/3",
          "comments": []
        },
        "Acute myeloid leukemia (megakaryoblastic) with": {
          "meaning": "icdo:9911/3",
          "comments": []
        },
        "Acute myeloid leukemia with BCR-ABL1": {
          "meaning": "icdo:9912/3",
          "comments": []
        },
        "Acute myeloid leukemia with biallelic mutations of CEBPA": {
          "meaning": "icdo:9878/3",
          "comments": []
        },
        "Acute myeloid leukemia with inv(3)(q21q26.2) or": {
          "meaning": "icdo:9869/3",
          "comments": []
        },
        "Acute myeloid leukemia with maturation": {
          "meaning": "icdo:9874/3",
          "comments": []
        },
        "Acute myeloid leukemia with mutated NPM1": {
          "meaning": "icdo:9877/3",
          "comments": []
        },
        "Acute myeloid leukemia with mutated RUNX1": {
          "meaning": "icdo:9879/3",
          "comments": []
        },
        "Acute myeloid leukemia with t(6;9)(p23;q34) DEK-NUP214": {
          "meaning": "icdo:9865/3",
          "comments": []
        },
        "Acute myeloid leukemia without maturation": {
          "meaning": "icdo:9873/3",
          "comments": []
        },
        "Acute myeloid leukemia, 11q23 abnormalities": {
          "meaning": "icdo:9897/3",
          "comments": []
        },
        "Acute myeloid leukemia, M6 type": {
          "meaning": "icdo:9840/3",
          "comments": []
        },
        "Acute myeloid leukemia, minimal differentiation": {
          "meaning": "icdo:9872/3",
          "comments": []
        },
        "Acute myeloid leukemia, t(8;21)(q22;q22)": {
          "meaning": "icdo:9896/3",
          "comments": []
        },
        "Acute myelomonocytic leukemia": {
          "meaning": "icdo:9867/3",
          "comments": []
        },
        "Acute panmyelosis with myelofibrosis": {
          "meaning": "icdo:9931/3",
          "comments": []
        },
        "Acute promyelocytic leuk.,t(15;17)(q22;q11-12)": {
          "meaning": "icdo:9866/3",
          "comments": []
        },
        "Adamantinoma of long bones": {
          "meaning": "icdo:9261/3",
          "comments": []
        },
        "Adamantinomatous Craniopharyngioma": {
          "meaning": "ncit:C4726",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'"
          ]
        },
        "Adenocarc. in situ in mult. adenomatous polyps": {
          "meaning": "icdo:8221/2",
          "comments": []
        },
        "Adenocarcinoid tumor": {
          "meaning": "icdo:8245/3",
          "comments": []
        },
        "Adenocarcinoma in adenoma. polyposis coli": {
          "meaning": "icdo:8220/3",
          "comments": []
        },
        "Adenocarcinoma in adenomatous polyp": {
          "meaning": "icdo:8210/3",
          "comments": []
        },
        "Adenocarcinoma in mult. adenomatous polyps": {
          "meaning": "icdo:8221/3",
          "comments": []
        },
        "Adenocarcinoma in situ": {
          "meaning": "icdo:8140/2",
          "comments": []
        },
        "Adenocarcinoma in situ in adenomatous polyp": {
          "meaning": "icdo:8210/2",
          "comments": []
        },
        "Adenocarcinoma in situ in familial polyp. coli": {
          "meaning": "icdo:8220/2",
          "comments": []
        },
        "Adenocarcinoma in situ in tubulovillous adenoma": {
          "meaning": "icdo:8263/2",
          "comments": []
        },
        "Adenocarcinoma in situ in villous adenoma": {
          "meaning": "icdo:8261/2",
          "comments": []
        },
        "Adenocarcinoma in situ, mucinous": {
          "meaning": "icdo:8253/2",
          "comments": []
        },
        "Adenocarcinoma in situ, non-mucinous": {
          "meaning": "icdo:8250/2",
          "comments": []
        },
        "Adenocarcinoma in tubulovillous adenoma": {
          "meaning": "icdo:8263/3",
          "comments": []
        },
        "Adenocarcinoma in villous adenoma": {
          "meaning": "icdo:8261/3",
          "comments": []
        },
        "Adenocarcinoma of anal glands": {
          "meaning": "icdo:8215/3",
          "comments": []
        },
        "Adenocarcinoma w cartilag. & oss. metaplas.": {
          "meaning": "icdo:8571/3",
          "comments": []
        },
        "Adenocarcinoma with apocrine metaplasia": {
          "meaning": "icdo:8573/3",
          "comments": []
        },
        "Adenocarcinoma with mixed subtypes": {
          "meaning": "icdo:8255/3",
          "comments": []
        },
        "Adenocarcinoma with neuroendocrine differen.": {
          "meaning": "icdo:8574/3",
          "comments": []
        },
        "Adenocarcinoma with spindle cell mataplasia": {
          "meaning": "icdo:8572/3",
          "comments": []
        },
        "Adenocarcinoma with squamous metaplasia": {
          "meaning": "icdo:8570/3",
          "comments": []
        },
        "Adenocarcinoma, HPV-associated": {
          "meaning": "icdo:8483/3",
          "comments": []
        },
        "Adenocarcinoma, HPV-independent, NOS": {
          "meaning": "icdo:8484/3",
          "comments": []
        },
        "Adenocarcinoma, NOS": {
          "meaning": "icdo:8140/3",
          "comments": []
        },
        "Adenocarcinoma, endocervical type": {
          "meaning": "icdo:8384/3",
          "comments": []
        },
        "Adenocarcinoma, intestinal type": {
          "meaning": "icdo:8144/3",
          "comments": []
        },
        "Adenoid basal cell carcinoma": {
          "meaning": "icdo:8098/3",
          "comments": []
        },
        "Adenoid cystic carcinoma": {
          "meaning": "icdo:8200/3",
          "comments": []
        },
        "Adenoma, NOS": {
          "meaning": "icdo:8140/0",
          "comments": []
        },
        "Adenomyoepithelioma with carcinoma": {
          "meaning": "icdo:8983/3",
          "comments": []
        },
        "Adenosarcoma": {
          "meaning": "icdo:8933/3",
          "comments": []
        },
        "Adenosquamous carcinoma": {
          "meaning": "icdo:8560/3",
          "comments": []
        },
        "Adult T-cell leukemia/lymphoma (HTLV-1 pos.)": {
          "meaning": "icdo:9827/3",
          "comments": []
        },
        "Aggressive NK-cell leukemia": {
          "meaning": "icdo:9948/3",
          "comments": []
        },
        "Alveolar adenocarcinoma": {
          "meaning": "icdo:8251/3",
          "comments": []
        },
        "Alveolar rhabdomyosarcoma": {
          "meaning": "icdo:8920/3",
          "comments": []
        },
        "Alveolar soft part sarcoma": {
          "meaning": "icdo:9581/3",
          "comments": []
        },
        "Amelanotic melanoma": {
          "meaning": "icdo:8730/3",
          "comments": []
        },
        "Ameloblastic fibrosarcoma": {
          "meaning": "icdo:9330/3",
          "comments": []
        },
        "Ameloblastic odontosarcoma": {
          "meaning": "icdo:9290/3",
          "comments": []
        },
        "Ameloblastoma, malignant": {
          "meaning": "icdo:9310/3",
          "comments": []
        },
        "Anaplastic large cell lymphoma, ALK negative": {
          "meaning": "icdo:9715/3",
          "comments": []
        },
        "Anaplastic large cell lymphoma, T-cell and Null cell type": {
          "meaning": "icdo:9714/3",
          "comments": []
        },
        "Androblastoma, malignant": {
          "meaning": "icdo:8630/3",
          "comments": []
        },
        "Angioimmunoblastic T-cell lymphoma": {
          "meaning": "icdo:9705/3",
          "comments": []
        },
        "Angiolipoma, NOS": {
          "meaning": "icdo:8861/0",
          "comments": []
        },
        "Angiomatous meningioma": {
          "meaning": "icdo:9534/0",
          "comments": []
        },
        "Angiomyosarcoma": {
          "meaning": "icdo:8894/3",
          "comments": []
        },
        "Aortic body tumor, malignant": {
          "meaning": "icdo:8691/3",
          "comments": []
        },
        "Apocrine adenocarcinoma": {
          "meaning": "icdo:8401/3",
          "comments": []
        },
        "Askin tumor": {
          "meaning": "icdo:9365/3",
          "comments": []
        },
        "Astroblastoma": {
          "meaning": "icdo:9430/3",
          "comments": []
        },
        "Astrocytoma, NOS": {
          "meaning": "icdo:9400/3",
          "comments": []
        },
        "Astrocytoma, anaplastic": {
          "meaning": "icdo:9401/3",
          "comments": []
        },
        "Atypical Choroid Plexus Papilloma": {
          "meaning": "ncit:C53686",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'"
          ]
        },
        "Atypical chronic myeloid leuk., BCR/ABL negative": {
          "meaning": "icdo:9876/3",
          "comments": []
        },
        "Atypical lipoma": {
          "meaning": "icdo:8850/1",
          "comments": []
        },
        "Atypical medullary carcinoma": {
          "meaning": "icdo:8513/3",
          "comments": []
        },
        "Atypical meningioma": {
          "meaning": "icdo:9539/1",
          "comments": []
        },
        "Atypical teratoid/rhabdoid tumor": {
          "meaning": "icdo:9508/3",
          "comments": []
        },
        "B lymphblastic leukemia/lymphoma with t(5;14)(q31;q32);IL3-IGH": {
          "meaning": "icdo:9817/3",
          "comments": []
        },
        "B lymphoblastic leukemia/lymphoma with hyperdiploidy": {
          "meaning": "icdo:9815/3",
          "comments": []
        },
        "B lymphoblastic leukemia/lymphoma, NOS": {
          "meaning": "icdo:9811/3",
          "comments": []
        },
        "B-lymphocytic leukemia/lymphoma, BCR-ABL1-like": {
          "meaning": "icdo:9819/3",
          "comments": []
        },
        "Balloon cell melanoma": {
          "meaning": "icdo:8722/3",
          "comments": []
        },
        "Basal cell adenocarcinoma": {
          "meaning": "icdo:8147/3",
          "comments": []
        },
        "Basal cell carcinoma, NOS": {
          "meaning": "icdo:8090/3",
          "comments": []
        },
        "Basal cell carcinoma, fibroepithelial": {
          "meaning": "icdo:8093/3",
          "comments": []
        },
        "Basal cell carcinoma, nodular": {
          "meaning": "icdo:8097/3",
          "comments": []
        },
        "Basaloid carcinoma": {
          "meaning": "icdo:8123/3",
          "comments": []
        },
        "Basaloid squamous cell carcinoma": {
          "meaning": "icdo:8083/3",
          "comments": []
        },
        "Basophil adenoma": {
          "meaning": "icdo:8300/0",
          "comments": []
        },
        "Basophil carcinoma": {
          "meaning": "icdo:8300/3",
          "comments": []
        },
        "Basosquamous carcinoma": {
          "meaning": "icdo:8094/3",
          "comments": []
        },
        "Bile duct cystadenocarcinoma": {
          "meaning": "icdo:8161/3",
          "comments": []
        },
        "Biphenotypic sinonasal sarcoma": {
          "meaning": "icdo:9045/3",
          "comments": []
        },
        "Blue nevus, malignant": {
          "meaning": "icdo:8780/3",
          "comments": []
        },
        "Bowen disease": {
          "meaning": "icdo:8081/2",
          "comments": []
        },
        "Brenner tumor, malignant": {
          "meaning": "icdo:9000/3",
          "comments": []
        },
        "Bronchiolo-alveolar carcinoma, non-mucinous": {
          "meaning": "icdo:8252/3",
          "comments": []
        },
        "Burkitt cell leukemia": {
          "meaning": "icdo:9826/3",
          "comments": []
        },
        "Burkitt lymphoma, NOS": {
          "meaning": "icdo:9687/3",
          "comments": []
        },
        "CIC-rearranged sarcoma": {
          "meaning": "icdo:9367/3",
          "comments": []
        },
        "Capillary hemangioma": {
          "meaning": "icdo:9131/0",
          "comments": []
        },
        "Carcinoid tumor, malignant": {
          "meaning": "icdo:8240/3",
          "comments": []
        },
        "Carcinoma in pleomorphic adenoma": {
          "meaning": "icdo:8941/3",
          "comments": []
        },
        "Carcinoma showing thymus-like element": {
          "meaning": "icdo:8589/3",
          "comments": []
        },
        "Carcinoma simplex": {
          "meaning": "icdo:8231/3",
          "comments": []
        },
        "Carcinoma with osteoclast-like giant cells": {
          "meaning": "icdo:8035/3",
          "comments": []
        },
        "Carcinoma, NOS": {
          "meaning": "icdo:8010/3",
          "comments": []
        },
        "Carcinoma, anaplastic type, NOS": {
          "meaning": "icdo:8021/3",
          "comments": []
        },
        "Carcinoma, diffuse type": {
          "meaning": "icdo:8145/3",
          "comments": []
        },
        "Carcinoma, undifferentiated type, NOS": {
          "meaning": "icdo:8020/3",
          "comments": []
        },
        "Carcinosarcoma, NOS": {
          "meaning": "icdo:8980/3",
          "comments": []
        },
        "Carcinosarcoma, embryonal type": {
          "meaning": "icdo:8981/3",
          "comments": []
        },
        "Carotid body tumor, malignant": {
          "meaning": "icdo:8692/3",
          "comments": []
        },
        "Cavernous hemangioma": {
          "meaning": "icdo:9121/0",
          "comments": []
        },
        "Central osteosarcoma": {
          "meaning": "icdo:9186/3",
          "comments": []
        },
        "Centrol neurocytoma": {
          "meaning": "icdo:9506/1",
          "comments": []
        },
        "Cerebellar sarcoma, NOS": {
          "meaning": "icdo:9480/3",
          "comments": []
        },
        "Ceruminous adenocarcinoma": {
          "meaning": "icdo:8420/3",
          "comments": []
        },
        "Cholangiocarcinoma": {
          "meaning": "icdo:8160/3",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Chondroblastic osteosarcoma": {
          "meaning": "icdo:9181/3",
          "comments": []
        },
        "Chondroblastoma, malignant": {
          "meaning": "icdo:9230/3",
          "comments": []
        },
        "Chondroid chordoma": {
          "meaning": "icdo:9371/3",
          "comments": []
        },
        "Chondrosarcoma, NOS": {
          "meaning": "icdo:9220/3",
          "comments": []
        },
        "Chordoid glioma": {
          "meaning": "icdo:9444/1",
          "comments": []
        },
        "Chordoma, NOS": {
          "meaning": "icdo:9370/3",
          "comments": []
        },
        "Choriocarcinoma": {
          "meaning": "ncit:C2948",
          "comments": []
        },
        "Choriocarcinoma combined w/ other germ cell elements": {
          "meaning": "icdo:9101/3",
          "comments": []
        },
        "Choroid plexus papilloma, NOS": {
          "meaning": "icdo:9390/0",
          "comments": []
        },
        "Choroid plexus papilloma, malignant": {
          "meaning": "icdo:9390/3",
          "comments": []
        },
        "Chromophobe adenoma": {
          "meaning": "icdo:8270/0",
          "comments": []
        },
        "Chromophobe carcinoma": {
          "meaning": "icdo:8270/3",
          "comments": []
        },
        "Chronic lymphocytic leukemia/small lymphocytic lymphoma": {
          "meaning": "icdo:9823/3",
          "comments": []
        },
        "Chronic myelogenous leukemia, BCR/ABL positive": {
          "meaning": "icdo:9875/3",
          "comments": []
        },
        "Chronic myeloid leukemia, NOS": {
          "meaning": "icdo:9863/3",
          "comments": []
        },
        "Chronic myelomonocytic leukemia, NOS": {
          "meaning": "icdo:9945/3",
          "comments": []
        },
        "Chronic myeloproliferative disease, NOS": {
          "meaning": "icdo:9960/3",
          "comments": []
        },
        "Chronic neutrophilic leukemia": {
          "meaning": "icdo:9963/3",
          "comments": []
        },
        "Clear cell adenocarcinofibroma": {
          "meaning": "icdo:8313/3",
          "comments": []
        },
        "Clear cell adenocarcinoma, NOS": {
          "meaning": "icdo:8310/3",
          "comments": []
        },
        "Clear cell adenoma": {
          "meaning": "icdo:8310/0",
          "comments": []
        },
        "Clear cell chondrosarcoma": {
          "meaning": "icdo:9242/3",
          "comments": []
        },
        "Clear cell meningioma": {
          "meaning": "icdo:9538/1",
          "comments": []
        },
        "Clear cell odontogenic carcinoma": {
          "meaning": "icdo:9341/3",
          "comments": []
        },
        "Clear cell sarcoma of kidney": {
          "meaning": "icdo:8964/3",
          "comments": []
        },
        "Clear cell sarcoma, NOS": {
          "meaning": "icdo:9044/3",
          "comments": []
        },
        "Clear cell tumor, NOS": {
          "meaning": "icdo:8005/0",
          "comments": []
        },
        "Cloacogenic carcinoma": {
          "meaning": "icdo:8124/3",
          "comments": []
        },
        "Comb. hepatocel. carcinoma & cholangiocarcinoma": {
          "meaning": "icdo:8180/3",
          "comments": []
        },
        "Combined small cell carcinoma": {
          "meaning": "icdo:8045/3",
          "comments": []
        },
        "Comedocarcinoma, NOS": {
          "meaning": "icdo:8501/3",
          "comments": []
        },
        "Comedocarcinoma, non-infiltrating": {
          "meaning": "icdo:8501/2",
          "comments": []
        },
        "Composite Hodgkin and non-Hodgkin lymphoma": {
          "meaning": "icdo:9596/3",
          "comments": []
        },
        "Composite carcinoid": {
          "meaning": "icdo:8244/3",
          "comments": []
        },
        "Craniopharyngioma": {
          "meaning": "icdo:9350/1",
          "comments": []
        },
        "Cribriform carcinoma": {
          "meaning": "icdo:8201/3",
          "comments": []
        },
        "Cribriform carcinoma in situ": {
          "meaning": "icdo:8201/2",
          "comments": []
        },
        "Cutaneous T-cell lymphoma, NOS": {
          "meaning": "icdo:9709/3",
          "comments": []
        },
        "Cyst-associated renal cell carcinoma": {
          "meaning": "icdo:8316/3",
          "comments": []
        },
        "Cystadenocarcinoma, NOS": {
          "meaning": "icdo:8440/3",
          "comments": []
        },
        "Cystic hypersecretory carcinoma": {
          "meaning": "icdo:8508/3",
          "comments": []
        },
        "Dedifferentiated Liposarcoma": {
          "meaning": "ncit:C3704",
          "comments": []
        },
        "Dedifferentiated chondrosarcoma": {
          "meaning": "icdo:9243/3",
          "comments": []
        },
        "Dedifferentiated chordoma": {
          "meaning": "icdo:9372/3",
          "comments": []
        },
        "Dermatofibrosarcoma, NOS": {
          "meaning": "icdo:8832/3",
          "comments": []
        },
        "Dermoid cyst, NOS": {
          "meaning": "icdo:9084/0",
          "comments": []
        },
        "Desmoplastic infantile astrocytoma": {
          "meaning": "icdo:9412/1",
          "comments": []
        },
        "Desmoplastic medulloblastoma": {
          "meaning": "icdo:9471/3",
          "comments": []
        },
        "Desmoplastic melanoma, malignant": {
          "meaning": "icdo:8745/3",
          "comments": []
        },
        "Desmoplastic Small Round Cell Tumor": {
          "meaning": "icdo:8806/3",
          "comments": []
        },
        "Diffuse Leptomeningeal Glioneuronal Tumor": {
          "meaning": "icdo:9509/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Diffuse melanocytosis": {
          "meaning": "icdo:8728/0",
          "comments": []
        },
        "Diffuse midline glioma, H3 K27M-mutant": {
          "meaning": "icdo:9385/3",
          "comments": []
        },
        "Duct carcinoma in situ, solid type": {
          "meaning": "icdo:8230/2",
          "comments": []
        },
        "Duct carcinoma, desmoplastic type": {
          "meaning": "icdo:8514/3",
          "comments": []
        },
        "Dysembryoplastic Neuroepithelial Tumor": {
          "meaning": "icdo:9413/0",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Dysgerminoma": {
          "meaning": "icdo:9060/3",
          "comments": []
        },
        "Dysplastic gangliocytoma of cerebellum (Lhermitte-Duclos)": {
          "meaning": "icdo:9493/0",
          "comments": []
        },
        "Eccrine adenocarcinoma": {
          "meaning": "icdo:8413/3",
          "comments": []
        },
        "Eccrine papillary adenocarcinoma": {
          "meaning": "icdo:8408/3",
          "comments": []
        },
        "Eccrine poroma, malignant": {
          "meaning": "icdo:8409/3",
          "comments": []
        },
        "Embryonal carcinoma, NOS": {
          "meaning": "icdo:9070/3",
          "comments": []
        },
        "Embryonal rhabdomyosarcoma": {
          "meaning": "icdo:8910/3",
          "comments": []
        },
        "Embryonal sarcoma": {
          "meaning": "icdo:8991/3",
          "comments": []
        },
        "Embryonal tumor with multilayered rosettes, NOS": {
          "meaning": "icdo:9478/3",
          "comments": []
        },
        "Endometrial stromal sarcoma": {
          "meaning": "icdo:8930/3",
          "comments": []
        },
        "Endometrial stromal sarcoma, low grade": {
          "meaning": "icdo:8931/3",
          "comments": []
        },
        "Endometrioid adenocarcinoma, ciliated cell variant": {
          "meaning": "icdo:8383/3",
          "comments": []
        },
        "Endometrioid adenocarcinoma, secretory variant": {
          "meaning": "icdo:8382/3",
          "comments": []
        },
        "Endometrioid adenofibroma, malignant": {
          "meaning": "icdo:8381/3",
          "comments": []
        },
        "Endometrioid carcinoma": {
          "meaning": "icdo:8380/3",
          "comments": []
        },
        "Endometrioid intraepithelial neoplasia": {
          "meaning": "icdo:8380/2",
          "comments": []
        },
        "Enterochromaffin cell carcinoid": {
          "meaning": "icdo:8241/3",
          "comments": []
        },
        "Enterochromaffin-like cell tumor, malignant": {
          "meaning": "icdo:8242/3",
          "comments": []
        },
        "Enteroglucagonoma, malignant": {
          "meaning": "icdo:8157/3",
          "comments": []
        },
        "Ependymoma, RELA fusion-positive": {
          "meaning": "icdo:9396/3",
          "comments": []
        },
        "Ependymoma, anaplastic": {
          "meaning": "icdo:9392/3",
          "comments": []
        },
        "Epithel. mesothelioma, mal.": {
          "meaning": "icdo:9052/3",
          "comments": []
        },
        "Epithelial tumor, benign": {
          "meaning": "icdo:8010/0",
          "comments": []
        },
        "Epithelial-myoepithelial carcinoma": {
          "meaning": "icdo:8562/3",
          "comments": []
        },
        "Epithelioid Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "ncit:C6561",
          "comments": []
        },
        "Epithelioid cell melanoma": {
          "meaning": "icdo:8771/3",
          "comments": []
        },
        "Epithelioid hemangioendothelioma, malignant": {
          "meaning": "icdo:9133/3",
          "comments": []
        },
        "Epithelioid leiomyosarcoma": {
          "meaning": "icdo:8891/3",
          "comments": []
        },
        "Epithelioma, malignant": {
          "meaning": "icdo:8011/3",
          "comments": []
        },
        "Erdheim-Chester Disease": {
          "meaning": "icdo:9749/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Essential thrombocythemia": {
          "meaning": "icdo:9962/3",
          "comments": []
        },
        "Ewing Sarcoma": {
          "meaning": "icdo:9260/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Extra-adrenal paraganglioma, malignant": {
          "meaning": "icdo:8693/3",
          "comments": []
        },
        "Fanconi Anemia": {
          "meaning": "ncit:C62505",
          "comments": []
        },
        "Fanconi Anemia Neurological Syndrome": {
          "meaning": "",
          "comments": []
        },
        "Fascial fibrosarcoma": {
          "meaning": "icdo:8813/3",
          "comments": []
        },
        "Fetal adenocarcinoma": {
          "meaning": "icdo:8333/3",
          "comments": []
        },
        "Fibrillary astrocytoma": {
          "meaning": "icdo:9420/3",
          "comments": []
        },
        "Fibroblastic Osteosarcoma": {
          "meaning": "ncit:C4020",
          "comments": []
        },
        "Fibroblastic liposarcoma": {
          "meaning": "icdo:8857/3",
          "comments": []
        },
        "Fibroblastic reticular cell tumor": {
          "meaning": "icdo:9759/3",
          "comments": []
        },
        "Fibrolipoma": {
          "meaning": "icdo:8851/0",
          "comments": []
        },
        "Fibroma, NOS": {
          "meaning": "icdo:8810/0",
          "comments": []
        },
        "Fibromyxosarcoma": {
          "meaning": "icdo:8811/3",
          "comments": []
        },
        "Fibrosarcoma, NOS": {
          "meaning": "icdo:8810/3",
          "comments": []
        },
        "Fibrous histiocytoma, malignant": {
          "meaning": "icdo:8830/3",
          "comments": []
        },
        "Fibrous meningioma": {
          "meaning": "icdo:9532/0",
          "comments": []
        },
        "Fibrous mesothelioma, malignant": {
          "meaning": "icdo:9051/3",
          "comments": []
        },
        "Follicular adenocarcinoma trabecular": {
          "meaning": "icdo:8332/3",
          "comments": []
        },
        "Follicular adenocarcinoma well diff.": {
          "meaning": "icdo:8331/3",
          "comments": []
        },
        "Follicular adenocarcinoma, NOS": {
          "meaning": "icdo:8330/3",
          "comments": []
        },
        "Follicular carcinoma, minimally invasive": {
          "meaning": "icdo:8335/3",
          "comments": []
        },
        "Follicular dendritic cell sarcoma": {
          "meaning": "icdo:9758/3",
          "comments": []
        },
        "Follicular lymphoma, NOS": {
          "meaning": "icdo:9690/3",
          "comments": []
        },
        "Follicular lymphoma, grade 1": {
          "meaning": "icdo:9695/3",
          "comments": []
        },
        "Follicular lymphoma, grade 2": {
          "meaning": "icdo:9691/3",
          "comments": []
        },
        "Follicular lymphoma, grade 3": {
          "meaning": "icdo:9698/3",
          "comments": []
        },
        "Follicular thyroid carcinoma (FTC), encapsulated angioinvasive": {
          "meaning": "icdo:8339/3",
          "comments": []
        },
        "Gangliocytoma": {
          "meaning": "icdo:9492/0",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Ganglioglioma, NOS": {
          "meaning": "icdo:9505/1",
          "comments": []
        },
        "Ganglioglioma, anaplastic": {
          "meaning": "icdo:9505/3",
          "comments": []
        },
        "Ganglioneuroblastoma": {
          "meaning": "icdo:9490/3",
          "comments": []
        },
        "Ganglioneuroma": {
          "meaning": "icdo:9490/0",
          "comments": []
        },
        "Gastrinoma, malignant": {
          "meaning": "icdo:8153/3",
          "comments": []
        },
        "Gastroblastoma": {
          "meaning": "icdo:8976/3",
          "comments": []
        },
        "Gastrointestinal stromal sarcoma": {
          "meaning": "icdo:8936/3",
          "comments": []
        },
        "Gemistocytic astrocytoma": {
          "meaning": "icdo:9411/3",
          "comments": []
        },
        "Germ cell tumor, nonseminomatous": {
          "meaning": "icdo:9065/3",
          "comments": []
        },
        "Germ cell tumors with associated hematological malignancy": {
          "meaning": "icdo:9086/3",
          "comments": []
        },
        "Germinoma": {
          "meaning": "ncit:C3753",
          "comments": []
        },
        "Ghost cell odontogenic carcinoma": {
          "meaning": "icdo:9302/3",
          "comments": []
        },
        "Giant cell and spindle cell carcinoma": {
          "meaning": "icdo:8030/3",
          "comments": []
        },
        "Giant cell carcinoma": {
          "meaning": "icdo:8031/3",
          "comments": []
        },
        "Giant cell glioblastoma": {
          "meaning": "icdo:9441/3",
          "comments": []
        },
        "Giant cell sarcoma": {
          "meaning": "icdo:8802/3",
          "comments": []
        },
        "Giant cell tumor of bone, malignant": {
          "meaning": "icdo:9250/3",
          "comments": []
        },
        "Glandular intraepithelial neoplasia, grade III": {
          "meaning": "icdo:8148/2",
          "comments": []
        },
        "Glassy cell carcinoma": {
          "meaning": "icdo:8015/3",
          "comments": []
        },
        "Glioblastoma, IDH-mutant": {
          "meaning": "icdo:9445/3",
          "comments": []
        },
        "Glioblastoma, NOS": {
          "meaning": "icdo:9440/3",
          "comments": []
        },
        "Gliofibroma": {
          "meaning": "icdo:9442/1",
          "comments": []
        },
        "Glioma, malignant": {
          "meaning": "icdo:9380/3",
          "comments": []
        },
        "Gliomatosis cerebri": {
          "meaning": "icdo:9381/3",
          "comments": []
        },
        "Gliosarcoma": {
          "meaning": "icdo:9442/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Glomangiosarcoma": {
          "meaning": "icdo:8710/3",
          "comments": []
        },
        "Glucagonoma, malignant": {
          "meaning": "icdo:8152/3",
          "comments": []
        },
        "Glycogen-rich carcinoma": {
          "meaning": "icdo:8315/3",
          "comments": []
        },
        "Goblet cell carcinoid": {
          "meaning": "icdo:8243/3",
          "comments": []
        },
        "Granular cell carcinoma": {
          "meaning": "icdo:8320/3",
          "comments": []
        },
        "Granular cell tumor of the sellar region": {
          "meaning": "icdo:9582/0",
          "comments": []
        },
        "Granular cell tumor, NOS": {
          "meaning": "icdo:9580/0",
          "comments": []
        },
        "Granular cell tumor, malignant": {
          "meaning": "icdo:9580/3",
          "comments": []
        },
        "Granulosa cell tumor, malignant": {
          "meaning": "icdo:8620/3",
          "comments": []
        },
        "Granulosa cell-theca cell tumor, mal.": {
          "meaning": "icdo:8621/3",
          "comments": []
        },
        "Gynandroblastoma, malignant": {
          "meaning": "icdo:8632/3",
          "comments": []
        },
        "Hairy cell leukemia": {
          "meaning": "icdo:9940/3",
          "comments": []
        },
        "Heavy chain disease, NOS": {
          "meaning": "icdo:9762/3",
          "comments": []
        },
        "Hemangioblastoma": {
          "meaning": "icdo:9161/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Hemangioendothelioma, NOS": {
          "meaning": "icdo:9130/1",
          "comments": []
        },
        "Hemangioendothelioma, benign": {
          "meaning": "icdo:9130/0",
          "comments": []
        },
        "Hemangioendothelioma, malignant": {
          "meaning": "icdo:9130/3",
          "comments": []
        },
        "Hemangioma, NOS": {
          "meaning": "icdo:9120/0",
          "comments": []
        },
        "Hemangiopericytoma, NOS": {
          "meaning": "icdo:9150/1",
          "comments": []
        },
        "Hemangiopericytoma, benign": {
          "meaning": "icdo:9150/0",
          "comments": []
        },
        "Hemangiopericytoma, malignant": {
          "meaning": "icdo:9150/3",
          "comments": []
        },
        "Hemangiosarcoma": {
          "meaning": "icdo:9120/3",
          "comments": []
        },
        "Hepatoblastoma": {
          "meaning": "icdo:8970/3",
          "comments": []
        },
        "Hepatocellular carcinoma, NOS": {
          "meaning": "icdo:8170/3",
          "comments": []
        },
        "Hepatocellular carcinoma, clear cell type": {
          "meaning": "icdo:8174/3",
          "comments": []
        },
        "Hepatocellular carcinoma, fibrolamellar": {
          "meaning": "icdo:8171/3",
          "comments": []
        },
        "Hepatocellular carcinoma, pleomorphic type": {
          "meaning": "icdo:8175/3",
          "comments": []
        },
        "Hepatocellular carcinoma, scirrhous": {
          "meaning": "icdo:8172/3",
          "comments": []
        },
        "Hepatocellular carcinoma, spindle cell variant": {
          "meaning": "icdo:8173/3",
          "comments": []
        },
        "Hepatoid adenocarcinoma": {
          "meaning": "icdo:8576/3",
          "comments": []
        },
        "Hepatosplenic gamma-delta cell lymphoma": {
          "meaning": "icdo:9716/3",
          "comments": []
        },
        "Hereditary leiomyomatosis and RCC-associated renal cell carcinoma": {
          "meaning": "icdo:8311/3",
          "comments": []
        },
        "High grade appendiceal mucinous neoplasm": {
          "meaning": "icdo:8480/2",
          "comments": []
        },
        "High grade surface osteosarcoma": {
          "meaning": "icdo:9194/3",
          "comments": []
        },
        "High-grade serous carcinoma": {
          "meaning": "icdo:8461/3",
          "comments": []
        },
        "Histiocytic Sarcoma": {
          "meaning": "ncit:C27349",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Hodgkin granuloma [obs]": {
          "meaning": "icdo:9661/3",
          "comments": []
        },
        "Hodgkin lymph., lymphocyt. deplet., diffuse fibrosis": {
          "meaning": "icdo:9654/3",
          "comments": []
        },
        "Hodgkin lymph., nodular lymphocyte predom.": {
          "meaning": "icdo:9659/3",
          "comments": []
        },
        "Hodgkin Lymphoma, NOS": {
          "meaning": "icdo:9650/3",
          "comments": []
        },
        "Hodgkin lymphoma, lymphocyt. deplet., reticular": {
          "meaning": "icdo:9655/3",
          "comments": []
        },
        "Hodgkin lymphoma, lymphocytic deplet., NOS": {
          "meaning": "icdo:9653/3",
          "comments": []
        },
        "Hodgkin lymphoma, mixed cellularity, NOS": {
          "meaning": "icdo:9652/3",
          "comments": []
        },
        "Hodgkin lymphoma, nod. scler., cellular phase": {
          "meaning": "icdo:9664/3",
          "comments": []
        },
        "Hodgkin lymphoma, nod. scler., grade 1": {
          "meaning": "icdo:9665/3",
          "comments": []
        },
        "Hodgkin lymphoma, nod. scler., grade 2": {
          "meaning": "icdo:9667/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nodular Sclerosis, NOS": {
          "meaning": "icdo:9663/3",
          "comments": []
        },
        "Hodgkin sarcoma [obs]": {
          "meaning": "icdo:9662/3",
          "comments": []
        },
        "Hydroa vacciniforme-like lymphoma": {
          "meaning": "icdo:9725/3",
          "comments": []
        },
        "Hypereosinophilic syndrome": {
          "meaning": "icdo:9964/3",
          "comments": []
        },
        "Immunoproliferative disease, NOS": {
          "meaning": "icdo:9760/3",
          "comments": []
        },
        "Immunoproliferative small intestinal disease": {
          "meaning": "icdo:9764/3",
          "comments": []
        },
        "Infantile Fibrosarcoma": {
          "meaning": "icdo:8814/3",
          "comments": []
        },
        "Infiltr. duct mixed with other types of carcinoma": {
          "meaning": "icdo:8523/3",
          "comments": []
        },
        "Infiltr. duct mixed with other types of carcinoma, in situ": {
          "meaning": "icdo:8523/2",
          "comments": []
        },
        "Infiltrating basal cell carcinoma, NOS": {
          "meaning": "icdo:8092/3",
          "comments": []
        },
        "Infiltrating duct and lobular carcinoma": {
          "meaning": "icdo:8522/3",
          "comments": []
        },
        "Infiltrating ductular carcinoma": {
          "meaning": "icdo:8521/3",
          "comments": []
        },
        "Infiltrating lobular mixed with other types of carc.": {
          "meaning": "icdo:8524/3",
          "comments": []
        },
        "Inflammatory carcinoma": {
          "meaning": "icdo:8530/3",
          "comments": []
        },
        "Instrosseous well differentiated osteosarcoma": {
          "meaning": "icdo:9187/3",
          "comments": []
        },
        "Insular carcinoma": {
          "meaning": "icdo:8337/3",
          "comments": []
        },
        "Insulinoma, malignant": {
          "meaning": "icdo:8151/3",
          "comments": []
        },
        "Interdigitating dendritic cell sarcoma": {
          "meaning": "icdo:9757/3",
          "comments": []
        },
        "Intestinal T-cell lymphoma": {
          "meaning": "icdo:9717/3",
          "comments": []
        },
        "Intestinal-type adenoma, high grade": {
          "meaning": "icdo:8144/2",
          "comments": []
        },
        "Intimal Sarcoma": {
          "meaning": "icdo:9137/3",
          "comments": []
        },
        "Intracortical osteosarcoma": {
          "meaning": "icdo:9195/3",
          "comments": []
        },
        "Intracystic carcinoma, NOS": {
          "meaning": "icdo:8504/3",
          "comments": []
        },
        "Intraductal and lobular in situ carcinoma": {
          "meaning": "icdo:8522/2",
          "comments": []
        },
        "Intraductal carcinoma, noninfiltrating, NOS": {
          "meaning": "icdo:8500/2",
          "comments": []
        },
        "Intraductal micropapillary carcinoma": {
          "meaning": "icdo:8507/2",
          "comments": []
        },
        "Intraductal oncocytic papillary neoplasm, NOS": {
          "meaning": "icdo:8455/2",
          "comments": []
        },
        "Intraductal oncocytic papillary neoplasms with associated invasive": {
          "meaning": "icdo:8455/3",
          "comments": []
        },
        "Intraductal papillary adenocarcinoma with invasion": {
          "meaning": "icdo:8503/3",
          "comments": []
        },
        "Intraductal papillary-mucinous carcinoma, invasive": {
          "meaning": "icdo:8453/3",
          "comments": []
        },
        "Intraductal papillary-mucinous carcinoma, non-inv.": {
          "meaning": "icdo:8453/2",
          "comments": []
        },
        "Intratubular malignant germ cells": {
          "meaning": "icdo:9064/2",
          "comments": []
        },
        "Intravascular Large B-Cell Lymphoma": {
          "meaning": "icdo:9712/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Invasive micropapillary carcinoma": {
          "meaning": "icdo:8507/3",
          "comments": []
        },
        "Invasive mucinous adenocarcinoma": {
          "meaning": "icdo:8253/3",
          "comments": []
        },
        "Islet cell carcinoma": {
          "meaning": "icdo:8150/3",
          "comments": []
        },
        "Juvenile Xanthogranuloma": {
          "meaning": "icdo:9749/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Juvenile myelomonocytic leukemia": {
          "meaning": "icdo:9946/3",
          "comments": []
        },
        "Juxtacortical chondrosarcoma": {
          "meaning": "icdo:9221/3",
          "comments": []
        },
        "Kaposi Sarcoma": {
          "meaning": "icdo:9140/3",
          "comments": []
        },
        "Klatskin tumor": {
          "meaning": "icdo:8162/3",
          "comments": []
        },
        "Kupffer cell sarcoma": {
          "meaning": "icdo:9124/3",
          "comments": []
        },
        "Langerhans cell histiocytosis, NOS": {
          "meaning": "icdo:9751/3",
          "comments": []
        },
        "Langerhans cell histiocytosis, disseminated": {
          "meaning": "icdo:9754/3",
          "comments": []
        },
        "Langerhans cell sarcoma": {
          "meaning": "icdo:9756/3",
          "comments": []
        },
        "Large cell carcinoma with rhabdoid phenotype": {
          "meaning": "icdo:8014/3",
          "comments": []
        },
        "Large cell carcinoma, NOS": {
          "meaning": "icdo:8012/3",
          "comments": []
        },
        "Large cell medulloblastoma": {
          "meaning": "icdo:9474/3",
          "comments": []
        },
        "Large cell neuroendocrine carcinoma": {
          "meaning": "icdo:8013/3",
          "comments": []
        },
        "Leiomyoma, NOS": {
          "meaning": "icdo:8890/0",
          "comments": []
        },
        "Leiomyomatosis, nOS": {
          "meaning": "icdo:8890/1",
          "comments": []
        },
        "Leiomyosarcoma, NOS": {
          "meaning": "icdo:8890/3",
          "comments": []
        },
        "Lentigo maligna": {
          "meaning": "icdo:8742/2",
          "comments": []
        },
        "Lentigo maligna melanoma": {
          "meaning": "icdo:8742/3",
          "comments": []
        },
        "Lepidic adenocarcinoma": {
          "meaning": "icdo:8250/3",
          "comments": []
        },
        "Leukemia, NOS": {
          "meaning": "icdo:9800/3",
          "comments": []
        },
        "Leukemia/lymphoma with hypodiploidy (hypodiploid ALL)": {
          "meaning": "icdo:9816/3",
          "comments": []
        },
        "Leukemia/lymphoma with t(12;21)(p13;q22);TEL-AML1(ETV6-RUNX1)": {
          "meaning": "icdo:9814/3",
          "comments": []
        },
        "Leukemia/lymphoma with t(1;19)(q23;p13.3); E2A PBX1 (TCF3 PBX1)": {
          "meaning": "icdo:9818/3",
          "comments": []
        },
        "Leukemia/lymphoma with t(9;22)(q34;q11.2);BCR-ABL1": {
          "meaning": "icdo:9812/3",
          "comments": []
        },
        "Leukemia/lymphoma with t(v;11q23);MLL rearranged": {
          "meaning": "icdo:9813/3",
          "comments": []
        },
        "Leydig cell tumor, malignant": {
          "meaning": "icdo:8650/3",
          "comments": []
        },
        "Linitis plastica": {
          "meaning": "icdo:8142/3",
          "comments": []
        },
        "Lipid-rich carcinoma": {
          "meaning": "icdo:8314/3",
          "comments": []
        },
        "Lipoma, NOS": {
          "meaning": "icdo:8850/0",
          "comments": []
        },
        "Liposarcoma, NOS": {
          "meaning": "ncit:C3194",
          "comments": []
        },
        "Liposarcoma, well differentiated": {
          "meaning": "icdo:8851/3",
          "comments": []
        },
        "Lobular carcinoma in situ": {
          "meaning": "icdo:8520/2",
          "comments": []
        },
        "Lobular carcinoma, NOS": {
          "meaning": "icdo:8520/3",
          "comments": []
        },
        "Low-grade serous carcinoma": {
          "meaning": "icdo:8460/3",
          "comments": []
        },
        "Lrg B-cell lymphoma in HHV8-assoc. multicentric Castleman DZ": {
          "meaning": "icdo:9738/3",
          "comments": []
        },
        "Lymphangioleiomyomatosis": {
          "meaning": "icdo:9174/3",
          "comments": []
        },
        "Lymphangiosarcoma": {
          "meaning": "icdo:9170/3",
          "comments": []
        },
        "Lymphoepithelial carcinoma": {
          "meaning": "icdo:8082/3",
          "comments": []
        },
        "Lymphoid leukemia, NOS": {
          "meaning": "icdo:9820/3",
          "comments": []
        },
        "Lymphoma, NOS": {
          "meaning": "icdo:9590/3",
          "comments": []
        },
        "Lymphomatoid granulomatosis, grade 3": {
          "meaning": "icdo:9766/3",
          "comments": []
        },
        "ML, large B-cell, diffuse": {
          "meaning": "icdo:9680/3",
          "comments": []
        },
        "ML, large B-cell, diffuse, immunoblastic, NOS": {
          "meaning": "icdo:9684/3",
          "comments": []
        },
        "ML, lymphoplasmacytic": {
          "meaning": "icdo:9671/3",
          "comments": []
        },
        "ML, mixed sm. and lg. cell, diffuse": {
          "meaning": "icdo:9675/3",
          "comments": []
        },
        "ML, small B lymphocytic, NOS": {
          "meaning": "icdo:9670/3",
          "comments": []
        },
        "MPNST with rhabdomyoblastic differentiation": {
          "meaning": "icdo:9561/3",
          "comments": []
        },
        "Mal. melanoma in giant pigmented nevus": {
          "meaning": "icdo:8761/3",
          "comments": []
        },
        "Mal. melanoma in junctional nevus": {
          "meaning": "icdo:8740/3",
          "comments": []
        },
        "Mal. melanoma in precan. melanosis": {
          "meaning": "icdo:8741/3",
          "comments": []
        },
        "Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "icdo:9540/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Malignant cystic nephroma": {
          "meaning": "icdo:8959/3",
          "comments": []
        },
        "Malignant eccrine spiradenoma": {
          "meaning": "icdo:8403/3",
          "comments": []
        },
        "Malignant giant cell tumor of soft parts": {
          "meaning": "icdo:9251/3",
          "comments": []
        },
        "Malignant histiocytosis": {
          "meaning": "icdo:9750/3",
          "comments": []
        },
        "Malignant lymphoma, NOS": {
          "meaning": "icdo:9590/3",
          "comments": []
        },
        "Malignant lymphoma, non-Hodgkin": {
          "meaning": "icdo:9591/3",
          "comments": []
        },
        "Malignant mastocytosis": {
          "meaning": "icdo:9741/3",
          "comments": []
        },
        "Malignant melanoma, NOS": {
          "meaning": "icdo:8720/3",
          "comments": []
        },
        "Malignant melanoma, regressing": {
          "meaning": "icdo:8723/3",
          "comments": []
        },
        "Malignant myoepithelioma": {
          "meaning": "icdo:8982/3",
          "comments": []
        },
        "Malignant placental site trophoblastic tumor": {
          "meaning": "icdo:9104/3",
          "comments": []
        },
        "Malignant rhabdoid tumor": {
          "meaning": "icdo:8963/3",
          "comments": [
            "(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'"
          ]
        },
        "Malignant tenosynovial giant cell tumor": {
          "meaning": "icdo:9252/3",
          "comments": []
        },
        "Malignant teratoma, intermediate": {
          "meaning": "icdo:9083/3",
          "comments": []
        },
        "Malignant teratoma, trophoblastic": {
          "meaning": "icdo:9102/3",
          "comments": []
        },
        "Malignant teratoma, undiff.": {
          "meaning": "icdo:9082/3",
          "comments": []
        },
        "Malignant tumor, clear cell type": {
          "meaning": "icdo:8005/3",
          "comments": []
        },
        "Malignant tumor, giant cell type": {
          "meaning": "icdo:8003/3",
          "comments": []
        },
        "Malignant tumor, small cell type": {
          "meaning": "icdo:8002/3",
          "comments": []
        },
        "Malignant tumor, spindle cell type": {
          "meaning": "icdo:8004/3",
          "comments": []
        },
        "Mantle cell lymphoma": {
          "meaning": "icdo:9673/3",
          "comments": []
        },
        "Marginal zone B-cell lymphoma, NOS": {
          "meaning": "icdo:9699/3",
          "comments": []
        },
        "Mast cell leukemia": {
          "meaning": "icdo:9742/3",
          "comments": []
        },
        "Mast cell sarcoma": {
          "meaning": "icdo:9740/3",
          "comments": []
        },
        "Mature T-cell lymphoma, NOS": {
          "meaning": "icdo:9702/3",
          "comments": []
        },
        "Mediastinal large B-cell lymphoma": {
          "meaning": "icdo:9679/3",
          "comments": []
        },
        "Medullary carcinoma with amyloid stroma": {
          "meaning": "icdo:8345/3",
          "comments": []
        },
        "Medullary carcinoma with lymphoid stroma": {
          "meaning": "icdo:8512/3",
          "comments": []
        },
        "Medullary carcinoma, NOS": {
          "meaning": "icdo:8510/3",
          "comments": []
        },
        "Medulloblastoma, NOS": {
          "meaning": "icdo:9470/3",
          "comments": []
        },
        "Medulloblastoma, SHH-activated and TP53-mutant": {
          "meaning": "icdo:9476/3",
          "comments": []
        },
        "Medulloblastoma, WNT-activated": {
          "meaning": "icdo:9475/3",
          "comments": []
        },
        "Medulloblastoma, non-WNT/non-SHH": {
          "meaning": "icdo:9477/3",
          "comments": []
        },
        "Medulloepithelioma, NOS": {
          "meaning": "icdo:9501/3",
          "comments": []
        },
        "Medullomyoblastoma": {
          "meaning": "icdo:9472/3",
          "comments": []
        },
        "Melanoma in situ": {
          "meaning": "icdo:8720/2",
          "comments": []
        },
        "Melanotic neurofibroma": {
          "meaning": "icdo:9541/0",
          "comments": []
        },
        "Melanotic schwannoma": {
          "meaning": "icdo:9560/1",
          "comments": []
        },
        "Meningeal melanocytoma": {
          "meaning": "icdo:8728/1",
          "comments": []
        },
        "Meningeal melanomatosis": {
          "meaning": "icdo:8728/3",
          "comments": []
        },
        "Meningeal sarcomatosis": {
          "meaning": "icdo:9539/3",
          "comments": []
        },
        "Meningioma, NOS": {
          "meaning": "icdo:9530/0",
          "comments": []
        },
        "Meningioma, malignant": {
          "meaning": "icdo:9530/3",
          "comments": []
        },
        "Meningothelial meningioma": {
          "meaning": "icdo:9531/0",
          "comments": []
        },
        "Merkel cell carcinoma": {
          "meaning": "icdo:8247/3",
          "comments": []
        },
        "Mesenchymal Chondrosarcoma": {
          "meaning": "icdo:9240/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Mesenchymoma, malignant": {
          "meaning": "icdo:8990/3",
          "comments": []
        },
        "Mesodermal mixed tumor": {
          "meaning": "icdo:8951/3",
          "comments": []
        },
        "Mesonephric-like adenocarcinoma": {
          "meaning": "icdo:9111/3",
          "comments": []
        },
        "Mesonephroma, malignant": {
          "meaning": "icdo:9110/3",
          "comments": []
        },
        "Mesothelioma, biphasic, malignant": {
          "meaning": "icdo:9053/3",
          "comments": []
        },
        "Mesothelioma, in situ": {
          "meaning": "icdo:9050/2",
          "comments": []
        },
        "Mesothelioma, malignant": {
          "meaning": "icdo:9050/3",
          "comments": []
        },
        "Metaplastic carcinoma, NOS": {
          "meaning": "icdo:8575/3",
          "comments": []
        },
        "Metatypical carcinoma": {
          "meaning": "icdo:8095/3",
          "comments": []
        },
        "Micropapillary carcinoma, NOS": {
          "meaning": "icdo:8265/3",
          "comments": []
        },
        "Middle ear paraganglioma": {
          "meaning": "icdo:8690/3",
          "comments": []
        },
        "Minimally invasive adenocarcinoma, mucinous": {
          "meaning": "icdo:8257/3",
          "comments": []
        },
        "Minimally invasive adenocarcinoma, non-mucinous": {
          "meaning": "icdo:8256/3",
          "comments": []
        },
        "Mixed Germ Cell Tumor": {
          "meaning": "ncit:C4290",
          "comments": []
        },
        "Mixed acidophil-basophil adenoma": {
          "meaning": "icdo:8281/0",
          "comments": []
        },
        "Mixed acidophil-basophil carcinoma": {
          "meaning": "icdo:8281/3",
          "comments": []
        },
        "Mixed acinar ductal carcinoma": {
          "meaning": "icdo:8552/3",
          "comments": []
        },
        "Mixed cell adenocarcinoma": {
          "meaning": "icdo:8323/3",
          "comments": []
        },
        "Mixed cell adenoma": {
          "meaning": "icdo:8323/0",
          "comments": []
        },
        "Mixed epithel. & spindle cell melanoma": {
          "meaning": "icdo:8770/3",
          "comments": []
        },
        "Mixed glioma": {
          "meaning": "icdo:9382/3",
          "comments": []
        },
        "Mixed invasive mucinous and non-mucinous adenocarcinoma": {
          "meaning": "icdo:8254/3",
          "comments": []
        },
        "Mixed medullary-follicular carcinoma": {
          "meaning": "icdo:8346/3",
          "comments": []
        },
        "Mixed medullary-papillary carcinoma": {
          "meaning": "icdo:8347/3",
          "comments": []
        },
        "Mixed neuroendocrine non-neuroendocrine neoplasm": {
          "meaning": "icdo:8154/3",
          "comments": []
        },
        "Mixed phenotype acute leukemia with t(9;22)(q34;q11.2);BCR-ABL1": {
          "meaning": "icdo:9806/3",
          "comments": []
        },
        "Mixed phenotype acute leukemia with t(v;11q23);MLL rearranged": {
          "meaning": "icdo:9807/3",
          "comments": []
        },
        "Mixed phenotype acute leukemia, B/myeloid, NOS": {
          "meaning": "icdo:9808/3",
          "comments": []
        },
        "Mixed phenotype acute leukemia, T/myeloid, NOS": {
          "meaning": "icdo:9809/3",
          "comments": []
        },
        "Mixed tumor, malignant, NOS": {
          "meaning": "icdo:8940/3",
          "comments": []
        },
        "Mixed type liposarcoma": {
          "meaning": "icdo:8855/3",
          "comments": []
        },
        "Mixed type rhabdomyosarcoma": {
          "meaning": "icdo:8902/3",
          "comments": []
        },
        "Monomorphic adenoma": {
          "meaning": "icdo:8146/0",
          "comments": []
        },
        "Mucin-producing adenocarcinoma": {
          "meaning": "icdo:8481/3",
          "comments": []
        },
        "Mucinous adenocarcinofibroma": {
          "meaning": "icdo:9015/3",
          "comments": []
        },
        "Mucinous adenocarcinoma": {
          "meaning": "icdo:8480/3",
          "comments": []
        },
        "Mucinous adenocarcinoma, endocervical type": {
          "meaning": "icdo:8482/3",
          "comments": []
        },
        "Mucinous cystadenocarcinoma, NOS": {
          "meaning": "icdo:8470/3",
          "comments": []
        },
        "Mucinous cystadenocarcinoma, non-invasive": {
          "meaning": "icdo:8470/2",
          "comments": []
        },
        "Mucinous cystic tumor of borderline malignancy (C56.9)": {
          "meaning": "icdo:8472/1",
          "comments": []
        },
        "Mucoepidermoid carcinoma": {
          "meaning": "icdo:8430/3",
          "comments": []
        },
        "Mucosal lentiginous melanoma": {
          "meaning": "icdo:8746/3",
          "comments": []
        },
        "Mullerian mixed tumor": {
          "meaning": "icdo:8950/3",
          "comments": []
        },
        "Multifocal superficial basal cell carcinoma": {
          "meaning": "icdo:8091/3",
          "comments": []
        },
        "Multinodular and vacuolating neuronal tumor": {
          "meaning": "icdo:9509/0",
          "comments": []
        },
        "Multinodular and vascolating neuronal tumor": {
          "meaning": "icdo:9505/0",
          "comments": []
        },
        "Multiple myeloma": {
          "meaning": "icdo:9732/3",
          "comments": []
        },
        "Mycosis fungoides": {
          "meaning": "icdo:9700/3",
          "comments": []
        },
        "Myelodysplastic syndr. with 5q deletion syndrome": {
          "meaning": "icdo:9986/3",
          "comments": []
        },
        "Myelodysplastic syndrome with ring sideroblasts and multilineage": {
          "meaning": "icdo:9993/3",
          "comments": []
        },
        "Myelodysplastic syndrome, NOS": {
          "meaning": "",
          "comments": []
        },
        "Myelodysplastic/Myeloproliferative neoplasm, unclassifiable": {
          "meaning": "icdo:9975/3",
          "comments": []
        },
        "Myeloid and lymphoid neoplasm with FGFR1 abnormalities": {
          "meaning": "icdo:9967/3",
          "comments": []
        },
        "Myeloid and lymphoid neoplasms with PDGFRB re arrangement": {
          "meaning": "icdo:9966/3",
          "comments": []
        },
        "Myeloid and lymphoid neoplasms with PDGFRB rearrangement": {
          "meaning": "icdo:9965/3",
          "comments": []
        },
        "Myeloid leukemia associated with Down Syndrome": {
          "meaning": "icdo:9898/3",
          "comments": []
        },
        "Myeloid leukemia, NOS": {
          "meaning": "icdo:9860/3",
          "comments": []
        },
        "Myeloid sarcoma": {
          "meaning": "icdo:9930/3",
          "comments": []
        },
        "Myeloid/lymphoid neoplasm with PCM1-JAK2": {
          "meaning": "icdo:9968/3",
          "comments": []
        },
        "Myelosclerosis with myeloid metaplasia": {
          "meaning": "icdo:9961/3",
          "comments": []
        },
        "Myofibroblastic sarcoma": {
          "meaning": "icdo:8825/3",
          "comments": []
        },
        "Myosarcoma": {
          "meaning": "icdo:8895/3",
          "comments": []
        },
        "Myxoid Liposarcoma": {
          "meaning": "ncit:C27781",
          "comments": []
        },
        "Myxoid chondrosarcoma": {
          "meaning": "icdo:9231/3",
          "comments": []
        },
        "Myxoid Leiomyosarcoma": {
          "meaning": "icdo:8896/3",
          "comments": []
        },
        "Myxopapillary Ependymoma": {
          "meaning": "ncit:C3697",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Myxosarcoma": {
          "meaning": "icdo:8840/3",
          "comments": []
        },
        "NK/T-cell lymphoma, nasal and nasal-type": {
          "meaning": "icdo:9719/3",
          "comments": []
        },
        "NUT carcinoma": {
          "meaning": "icdo:8023/3",
          "comments": []
        },
        "Neoplasm, benign": {
          "meaning": "icdo:8000/0",
          "comments": []
        },
        "Neoplasm, malignant": {
          "meaning": "icdo:8000/3",
          "comments": []
        },
        "Neoplasm, uncertain whether benign or malignant": {
          "meaning": "icdo:8000/1",
          "comments": []
        },
        "Nephroblastoma, NOS": {
          "meaning": "icdo:8960/3",
          "comments": []
        },
        "Neurilemmoma, malignant": {
          "meaning": "icdo:9560/3",
          "comments": []
        },
        "Neurilemoma, NOS": {
          "meaning": "icdo:9560/0",
          "comments": []
        },
        "Neuroblastoma, NOS": {
          "meaning": "icdo:9500/3",
          "comments": []
        },
        "Neuroendocrine carcinoma": {
          "meaning": "icdo:8246/3",
          "comments": []
        },
        "Neuroendocrine tumor": {
          "meaning": "icdo:8249/3",
          "comments": []
        },
        "Neuroepithelioma, NOS": {
          "meaning": "icdo:9503/3",
          "comments": []
        },
        "Neurofibroma, NOS": {
          "meaning": "icdo:9540/0",
          "comments": []
        },
        "Neurofibromatosis, NOS": {
          "meaning": "icdo:9540/1",
          "comments": []
        },
        "Neuroma, NOS": {
          "meaning": "icdo:9570/0",
          "comments": []
        },
        "Neurothekeoma": {
          "meaning": "icdo:9562/0",
          "comments": []
        },
        "Nodular hidradenoma, malignant": {
          "meaning": "icdo:8402/3",
          "comments": []
        },
        "Nodular melanoma": {
          "meaning": "icdo:8721/3",
          "comments": []
        },
        "Non-invasive EFVPTC": {
          "meaning": "icdo:8343/2",
          "comments": []
        },
        "Non-invasive low grade serous carcinoma": {
          "meaning": "icdo:8460/2",
          "comments": []
        },
        "Non-small cell carcinoma": {
          "meaning": "icdo:8046/3",
          "comments": []
        },
        "Nonencapsulated sclerosing carcinoma": {
          "meaning": "icdo:8350/3",
          "comments": []
        },
        "Noninfiltrating intracystic carcinoma": {
          "meaning": "icdo:8504/2",
          "comments": []
        },
        "Noninfiltrating intraductal papillary adenocarcinoma": {
          "meaning": "icdo:8503/2",
          "comments": []
        },
        "Oat cell carcinoma": {
          "meaning": "icdo:8042/3",
          "comments": []
        },
        "Odontogenic carcinosarcoma": {
          "meaning": "icdo:9342/3",
          "comments": []
        },
        "Odontogenic tumor, malignant": {
          "meaning": "icdo:9270/3",
          "comments": []
        },
        "Olfactory neurcytoma": {
          "meaning": "icdo:9521/3",
          "comments": []
        },
        "Olfactory neuroblastoma": {
          "meaning": "icdo:9522/3",
          "comments": []
        },
        "Olfactory neuroepithelioma": {
          "meaning": "icdo:9523/3",
          "comments": []
        },
        "Olfactory neurogenic tumor": {
          "meaning": "icdo:9520/3",
          "comments": []
        },
        "Oligodendroblastoma": {
          "meaning": "icdo:9460/3",
          "comments": []
        },
        "Oligodendroglioma, anaplastic": {
          "meaning": "icdo:9451/3",
          "comments": []
        },
        "Osteosarcoma in Paget disease": {
          "meaning": "icdo:9184/3",
          "comments": []
        },
        "Osteosarcoma, NOS": {
          "meaning": "icdo:9180/3",
          "comments": []
        },
        "Ovarian stromal tumor, mal.": {
          "meaning": "icdo:8590/3",
          "comments": []
        },
        "Oxyphilic adenocarcinoma": {
          "meaning": "icdo:8290/3",
          "comments": []
        },
        "Oxyphilic adenoma": {
          "meaning": "icdo:8290/0",
          "comments": []
        },
        "PEComa, malignant": {
          "meaning": "icdo:8714/3",
          "comments": []
        },
        "Paget dis. & infil. duct carcinoma": {
          "meaning": "icdo:8541/3",
          "comments": []
        },
        "Paget disease and intraductal ca.": {
          "meaning": "icdo:8543/3",
          "comments": []
        },
        "Paget disease, extramammary": {
          "meaning": "icdo:8542/3",
          "comments": []
        },
        "Paget disease, mammary": {
          "meaning": "icdo:8540/3",
          "comments": []
        },
        "Pancreatobiliary-type carcinoma": {
          "meaning": "icdo:8163/3",
          "comments": []
        },
        "Pancreatoblastoma": {
          "meaning": "icdo:8971/3",
          "comments": []
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
        "Papillary adenocarcinoma, NOS": {
          "meaning": "icdo:8260/3",
          "comments": []
        },
        "Papillary adenoma, NOS": {
          "meaning": "icdo:8260/0",
          "comments": []
        },
        "Papillary carcinoma in situ": {
          "meaning": "icdo:8050/2",
          "comments": []
        },
        "Papillary carcinoma, NOS": {
          "meaning": "icdo:8050/3",
          "comments": []
        },
        "Papillary carcinoma, columnar cell": {
          "meaning": "icdo:8344/3",
          "comments": []
        },
        "Papillary carcinoma, encapsulated": {
          "meaning": "icdo:8343/3",
          "comments": []
        },
        "Papillary carcinoma, follicular variant": {
          "meaning": "icdo:8340/3",
          "comments": []
        },
        "Papillary carcinoma, oxyphilic cell": {
          "meaning": "icdo:8342/3",
          "comments": []
        },
        "Papillary cystadenocarcinoma, NOS": {
          "meaning": "icdo:8450/3",
          "comments": []
        },
        "Papillary cystadenoma, borderline malignancy (C56.9)": {
          "meaning": "icdo:8451/1",
          "comments": []
        },
        "Papillary ependymoma": {
          "meaning": "icdo:9393/3",
          "comments": []
        },
        "Papillary meningioma": {
          "meaning": "icdo:9538/3",
          "comments": []
        },
        "Papillary microcarcinoma": {
          "meaning": "icdo:8341/3",
          "comments": []
        },
        "Papillary mucinous cystadenocarcinoma": {
          "meaning": "icdo:8471/3",
          "comments": []
        },
        "Papillary mucinous cystadenoma, borderline malignancy (C56.9)": {
          "meaning": "icdo:8473/1",
          "comments": []
        },
        "Papillary squamous cell carcinoma": {
          "meaning": "icdo:8052/3",
          "comments": []
        },
        "Papillary squamous cell carcinoma, non-invasive": {
          "meaning": "icdo:8052/2",
          "comments": []
        },
        "Papillary trans. cell carcinoma": {
          "meaning": "icdo:8130/3",
          "comments": []
        },
        "Papillary trans. cell carcinoma, non-invasive": {
          "meaning": "icdo:8130/2",
          "comments": []
        },
        "Papillary tumor of pineal region": {
          "meaning": "icdo:9395/3",
          "comments": []
        },
        "Paraganglioma, NOS": {
          "meaning": "icdo:8680/1",
          "comments": []
        },
        "Paraganglioma, malignant": {
          "meaning": "icdo:8680/3",
          "comments": []
        },
        "Parietal cell carcinoma": {
          "meaning": "icdo:8214/3",
          "comments": []
        },
        "Parosteal Osteosarcoma": {
          "meaning": "icdo:9192/3",
          "comments": []
        },
        "Perineurioma, NOS": {
          "meaning": "icdo:9571/0",
          "comments": []
        },
        "Perineurioma, malignant": {
          "meaning": "icdo:9571/3",
          "comments": []
        },
        "Periosteal fibrosarcoma": {
          "meaning": "icdo:8812/3",
          "comments": []
        },
        "Periosteal Osteosarcoma": {
          "meaning": "icdo:9193/3",
          "comments": []
        },
        "Peripheral neuroectodermal tumor": {
          "meaning": "icdo:9364/3",
          "comments": []
        },
        "Pheochromocytoma": {
          "meaning": "icdo:8700/3",
          "comments": []
        },
        "Phyllodes tumor, malignant": {
          "meaning": "icdo:9020/3",
          "comments": []
        },
        "Pilocytic Astrocytoma": {
          "meaning": "icdo:9421/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Pilomatrix carcinoma": {
          "meaning": "icdo:8110/3",
          "comments": []
        },
        "Pilomyxoid Astrocytoma": {
          "meaning": "icdo:9425/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Pineocytoma": {
          "meaning": "icdo:9361/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Pituicytoma": {
          "meaning": "icdo:9432/1",
          "comments": []
        },
        "Pituitary adenoma, NOS": {
          "meaning": "icdo:8272/0",
          "comments": []
        },
        "Pituitary blastoma": {
          "meaning": "icdo:8273/3",
          "comments": []
        },
        "Pituitary carcinoma, NOS": {
          "meaning": "icdo:8272/3",
          "comments": []
        },
        "Plasma cell leukemia": {
          "meaning": "icdo:9733/3",
          "comments": []
        },
        "Plasmablastic lymphoma": {
          "meaning": "icdo:9735/3",
          "comments": []
        },
        "Plasmacytoma, NOS": {
          "meaning": "icdo:9731/3",
          "comments": []
        },
        "Plasmacytoma, extramedullary": {
          "meaning": "icdo:9734/3",
          "comments": []
        },
        "Pleomorphic Xanthoastrocytoma": {
          "meaning": "icdo:9424/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Pleomorphic carcinoma": {
          "meaning": "icdo:8022/3",
          "comments": []
        },
        "Pleomorphic Liposarcoma": {
          "meaning": "icdo:8854/3",
          "comments": []
        },
        "Pleomorphic lobular carcinoma in situ": {
          "meaning": "icdo:8519/2",
          "comments": []
        },
        "Pleomorphic rhabdomyosarcoma, adult type": {
          "meaning": "icdo:8901/3",
          "comments": []
        },
        "Pleuropulmonary blastoma": {
          "meaning": "icdo:8973/3",
          "comments": []
        },
        "Plexiform neurofibroma": {
          "meaning": "icdo:9550/0",
          "comments": []
        },
        "Polar spongioblastoma": {
          "meaning": "icdo:9423/3",
          "comments": []
        },
        "Polycythemia vera": {
          "meaning": "icdo:9950/3",
          "comments": []
        },
        "Polygonal cell carcinoma": {
          "meaning": "icdo:8034/3",
          "comments": []
        },
        "Polymorphic PTLD": {
          "meaning": "icdo:9971/3",
          "comments": []
        },
        "Polymorphous low grade adenocarcinoma": {
          "meaning": "icdo:8525/3",
          "comments": []
        },
        "Precancerous melanosis, NOS": {
          "meaning": "icdo:8741/2",
          "comments": []
        },
        "Precursor B-cell lymphoblastic leukemia": {
          "meaning": "icdo:9836/3",
          "comments": []
        },
        "Precursor B-cell lymphoblastic lymphoma": {
          "meaning": "icdo:9728/3",
          "comments": []
        },
        "Precursor T-cell lymphoblastic lymphoma": {
          "meaning": "icdo:9729/3",
          "comments": []
        },
        "Precursor cell lymphoblastic leukemia, NOS": {
          "meaning": "icdo:9835/3",
          "comments": []
        },
        "Precursor cell lymphoblastic lymphoma, NOS": {
          "meaning": "icdo:9727/3",
          "comments": []
        },
        "Primary Cutaneous follicle centre lymphoma": {
          "meaning": "icdo:9597/3",
          "comments": []
        },
        "Primary Cutaneous gamma-delta T-cell lymphoma": {
          "meaning": "icdo:9726/3",
          "comments": []
        },
        "Primary cutan. CD30+ T-cell lymphoprolif. disorder": {
          "meaning": "icdo:9718/3",
          "comments": []
        },
        "Primary effusion lymphoma": {
          "meaning": "icdo:9678/3",
          "comments": []
        },
        "Primitive Neuroectodermal Tumor": {
          "meaning": "icdo:9473/3",
          "comments": []
        },
        "Prolactinoma": {
          "meaning": "icdo:8271/0",
          "comments": []
        },
        "Prolymphocytic leukemia, B-cell type": {
          "meaning": "icdo:9833/3",
          "comments": []
        },
        "Prolymphocytic leukemia, NOS": {
          "meaning": "icdo:9832/3",
          "comments": []
        },
        "Prolymphocytic leukemia, T-cell type": {
          "meaning": "icdo:9834/3",
          "comments": []
        },
        "Protoplasmic astrocytoma": {
          "meaning": "icdo:9410/3",
          "comments": []
        },
        "Psammomatous meningioma": {
          "meaning": "icdo:9533/0",
          "comments": []
        },
        "Pseudosarcomatous carcinoma": {
          "meaning": "icdo:8033/3",
          "comments": []
        },
        "Pulmonary blastoma": {
          "meaning": "icdo:8972/3",
          "comments": []
        },
        "Pulmonary myxoid sarcoma with EWSR1-CREB1 translocation": {
          "meaning": "icdo:8842/3",
          "comments": []
        },
        "Queyrat erythroplasia": {
          "meaning": "icdo:8080/2",
          "comments": []
        },
        "Refract. anemia with excess blasts in transformation": {
          "meaning": "icdo:9984/3",
          "comments": []
        },
        "Refractory anemia": {
          "meaning": "icdo:9980/3",
          "comments": []
        },
        "Refractory anemia with excess blasts": {
          "meaning": "icdo:9983/3",
          "comments": []
        },
        "Refractory anemia with sideroblasts": {
          "meaning": "icdo:9982/3",
          "comments": []
        },
        "Refractory cytopenia with multilineage dysplasia": {
          "meaning": "icdo:9985/3",
          "comments": []
        },
        "Refractory neutropenia": {
          "meaning": "icdo:9991/3",
          "comments": []
        },
        "Refractory thrombocytopenia": {
          "meaning": "icdo:9992/3",
          "comments": []
        },
        "Renal cell carcinoma": {
          "meaning": "icdo:8312/3",
          "comments": []
        },
        "Renal cell carcinoma, chromophobe type": {
          "meaning": "icdo:8317/3",
          "comments": []
        },
        "Renal cell carcinoma, sarcomatoid": {
          "meaning": "icdo:8318/3",
          "comments": []
        },
        "Retinoblastoma, NOS": {
          "meaning": "icdo:9510/3",
          "comments": []
        },
        "Retinoblastoma, differentiated": {
          "meaning": "icdo:9511/3",
          "comments": []
        },
        "Retinoblastoma, diffuse": {
          "meaning": "icdo:9513/3",
          "comments": []
        },
        "Retinoblastoma, undifferentiated": {
          "meaning": "icdo:9512/3",
          "comments": []
        },
        "Rhabdomyoma, NOS": {
          "meaning": "icdo:8900/0",
          "comments": []
        },
        "Rhabdomyosarcoma with ganglionic differentiation": {
          "meaning": "icdo:8921/3",
          "comments": []
        },
        "Rhabdomyosarcoma, NOS": {
          "meaning": "icdo:8900/3",
          "comments": []
        },
        "Round cell liposarcoma": {
          "meaning": "icdo:8853/3",
          "comments": []
        },
        "Round cell sarcoma with EWSR1-non-ETS fusions": {
          "meaning": "icdo:9366/3",
          "comments": []
        },
        "Sarcoma with BCOR genetic alterations": {
          "meaning": "icdo:9368/3",
          "comments": []
        },
        "Sarcoma, NOS": {
          "meaning": "icdo:8800/3",
          "comments": []
        },
        "Schneiderian carcinoma": {
          "meaning": "icdo:8121/3",
          "comments": []
        },
        "Scirrhous adenocarcinoma": {
          "meaning": "icdo:8141/3",
          "comments": []
        },
        "Sclerosing sweat duct carcinoma": {
          "meaning": "icdo:8407/3",
          "comments": []
        },
        "Sebaceous adenocarcinoma": {
          "meaning": "icdo:8410/3",
          "comments": []
        },
        "Secretory carcinoma of no special type": {
          "meaning": "icdo:8502/3",
          "comments": []
        },
        "Sellar ependymoma": {
          "meaning": "icdo:9391/1",
          "comments": []
        },
        "Seminoma, NOS": {
          "meaning": "icdo:9061/3",
          "comments": []
        },
        "Seminoma, anaplastic": {
          "meaning": "icdo:9062/3",
          "comments": []
        },
        "Seromucinous carcinoma": {
          "meaning": "icdo:8474/3",
          "comments": []
        },
        "Serous adenocarcinofibroma": {
          "meaning": "icdo:9014/3",
          "comments": []
        },
        "Serous cystadenocarcinoma": {
          "meaning": "icdo:8441/3",
          "comments": []
        },
        "Serous cystadenoma, borderline malignancy (C56.9)": {
          "meaning": "icdo:8442/1",
          "comments": []
        },
        "Serous papillary cystic tumor of borderline malignancy (C56.9)": {
          "meaning": "icdo:8462/1",
          "comments": []
        },
        "Serous tubal intraepithelial carcinoma": {
          "meaning": "icdo:8441/2",
          "comments": []
        },
        "Serrated adenocarcinoma": {
          "meaning": "icdo:8213/3",
          "comments": []
        },
        "Serrated dysplasia, high grade": {
          "meaning": "icdo:8213/2",
          "comments": []
        },
        "Sertoli cell carcinoma": {
          "meaning": "icdo:8640/3",
          "comments": []
        },
        "Sertoli-Leydig cell tumor, poorly differentiated": {
          "meaning": "icdo:8631/3",
          "comments": []
        },
        "Sertoli-Leydig cl tum., p.d. w heterologous elements": {
          "meaning": "icdo:8634/3",
          "comments": []
        },
        "Sezary syndrome": {
          "meaning": "icdo:9701/3",
          "comments": []
        },
        "Signet ring cell carcinoma": {
          "meaning": "icdo:8490/3",
          "comments": []
        },
        "Skin appendage carcinoma": {
          "meaning": "icdo:8390/3",
          "comments": []
        },
        "Small cell carcinoma, NOS": {
          "meaning": "icdo:8041/3",
          "comments": []
        },
        "Small cell carcinoma, fusiform cell": {
          "meaning": "icdo:8043/3",
          "comments": []
        },
        "Small cell carcinoma, intermediate cell": {
          "meaning": "icdo:8044/3",
          "comments": []
        },
        "Small cell sarcoma": {
          "meaning": "icdo:8803/3",
          "comments": []
        },
        "Smooth muscle tumor, NOS": {
          "meaning": "icdo:8897/1",
          "comments": []
        },
        "Soft tissue tumor, benign": {
          "meaning": "icdo:8800/0",
          "comments": []
        },
        "Solid carcinoma, NOS": {
          "meaning": "icdo:8230/3",
          "comments": []
        },
        "Solid papillary carcinoma in situ": {
          "meaning": "icdo:8509/2",
          "comments": []
        },
        "Solid papillary carcinoma with invasion": {
          "meaning": "icdo:8509/3",
          "comments": []
        },
        "Solid pseudopapillary carcinoma": {
          "meaning": "icdo:8452/3",
          "comments": []
        },
        "Solitary Fibrous Tumor": {
          "meaning": "ncit:C7634",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Solitary Fibrous Tumor, Malignant": {
          "meaning": "icdo:8815/3",
          "comments": []
        },
        "Solitary fibrous tumor/hemangiopericytoma Grade 2": {
          "meaning": "icdo:8815/1",
          "comments": []
        },
        "Somatostatinoma, malignant": {
          "meaning": "icdo:8156/3",
          "comments": []
        },
        "Spermatocytic seminoma": {
          "meaning": "icdo:9063/3",
          "comments": []
        },
        "Spindle cell carcinoma": {
          "meaning": "icdo:8032/3",
          "comments": []
        },
        "Spindle cell melanoma, NOS": {
          "meaning": "icdo:8772/3",
          "comments": []
        },
        "Spindle cell melanoma, type A": {
          "meaning": "icdo:8773/3",
          "comments": []
        },
        "Spindle cell melanoma, type B": {
          "meaning": "icdo:8774/3",
          "comments": []
        },
        "Spindle cell rhabdomyosarcoma": {
          "meaning": "icdo:8912/3",
          "comments": []
        },
        "Spindle cell sarcoma": {
          "meaning": "icdo:8801/3",
          "comments": []
        },
        "Spindle epithelial tumor with thymus-like element": {
          "meaning": "icdo:8588/3",
          "comments": []
        },
        "Splenic marginal zone B-cell lymphoma": {
          "meaning": "icdo:9689/3",
          "comments": []
        },
        "Spongioneuroblastoma": {
          "meaning": "icdo:9504/3",
          "comments": []
        },
        "Sq. cell carc. in situ with question. stromal invas.": {
          "meaning": "icdo:8076/2",
          "comments": []
        },
        "Sq. cell carcinoma, keratinizing, NOS": {
          "meaning": "icdo:8071/3",
          "comments": []
        },
        "Sq. cell carcinoma, keratinizing, NOS, in situ": {
          "meaning": "icdo:8071/2",
          "comments": []
        },
        "Sq. cell carcinoma, lg. cell, non-ker.": {
          "meaning": "icdo:8072/3",
          "comments": []
        },
        "Sq. cell carcinoma, lg. cell, non-ker., in situ": {
          "meaning": "icdo:8072/2",
          "comments": []
        },
        "Sq. cell carcinoma, micro-invasive": {
          "meaning": "icdo:8076/3",
          "comments": []
        },
        "Sq. cell carcinoma, sm. cell, non-ker.": {
          "meaning": "icdo:8073/3",
          "comments": []
        },
        "Sq. cell carcinoma, spindle cell": {
          "meaning": "icdo:8074/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, NOS": {
          "meaning": "icdo:8070/3",
          "comments": []
        },
        "Squamous cell carcinoma in situ, NOS": {
          "meaning": "icdo:8070/2",
          "comments": []
        },
        "Squamous cell carcinoma with horn formation": {
          "meaning": "icdo:8078/3",
          "comments": []
        },
        "Squamous cell carcinoma, HPV-negative": {
          "meaning": "icdo:8086/3",
          "comments": []
        },
        "Squamous cell carcinoma, HPV-positive": {
          "meaning": "icdo:8085/3",
          "comments": []
        },
        "Squamous cell carcinoma, adenoid": {
          "meaning": "icdo:8075/3",
          "comments": []
        },
        "Squamous cell carcinoma, clear cell type": {
          "meaning": "icdo:8084/3",
          "comments": []
        },
        "Squamous intraepithelial neoplasia, grade III": {
          "meaning": "icdo:8077/2",
          "comments": []
        },
        "Steroid cell tumor, malignant": {
          "meaning": "icdo:8670/3",
          "comments": []
        },
        "Stromal sarcoma, NOS": {
          "meaning": "icdo:8935/3",
          "comments": []
        },
        "Struma ovarii, malignant": {
          "meaning": "icdo:9090/3",
          "comments": []
        },
        "Subcutaneous panniculitis-like T-cell lymphoma": {
          "meaning": "icdo:9708/3",
          "comments": []
        },
        "Subependymoma": {
          "meaning": "icdo:9383/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Supependymal giant cell astrocytoma": {
          "meaning": "icdo:9384/1",
          "comments": []
        },
        "Superficial spreading adenocarcinoma": {
          "meaning": "icdo:8143/3",
          "comments": []
        },
        "Superficial spreading melanoma": {
          "meaning": "icdo:8743/3",
          "comments": []
        },
        "Superficial spreading melanoma, in situ": {
          "meaning": "icdo:8743/2",
          "comments": []
        },
        "Sweat gland adenocarcinoma": {
          "meaning": "icdo:8400/3",
          "comments": []
        },
        "Sympathetic Paraganglioma": {
          "meaning": "icdo:8681/3",
          "comments": []
        },
        "Synovial sarcoma, NOS": {
          "meaning": "icdo:9040/3",
          "comments": []
        },
        "Synovial sarcoma, epithelioid cell": {
          "meaning": "icdo:9042/3",
          "comments": []
        },
        "SystemicEBV pos. T-cell lymphoproliferative disease of childhood": {
          "meaning": "icdo:9724/3",
          "comments": []
        },
        "T lymphoblastic leukemia/lymphoma": {
          "meaning": "icdo:9837/3",
          "comments": []
        },
        "T-cell histiocyte rich large B-cell lymphoma": {
          "meaning": "icdo:9688/3",
          "comments": []
        },
        "T-cell large granular lymphocytic leukemia": {
          "meaning": "icdo:9831/3",
          "comments": []
        },
        "Teratocarcinoma": {
          "meaning": "icdo:9081/3",
          "comments": []
        },
        "Teratoid medulloepithelioma": {
          "meaning": "icdo:9502/3",
          "comments": []
        },
        "Teratoma with malig. transformation": {
          "meaning": "icdo:9084/3",
          "comments": []
        },
        "Teratoma, benign": {
          "meaning": "icdo:9080/0",
          "comments": []
        },
        "Teratoma, malignant, NOS": {
          "meaning": "icdo:9080/3",
          "comments": []
        },
        "Thecoma, malignant": {
          "meaning": "icdo:8600/3",
          "comments": []
        },
        "Therapy-related acute myeloid leukemia, NOS": {
          "meaning": "icdo:9920/3",
          "comments": []
        },
        "Therapy-related myelodysplastic syndrome, NOS": {
          "meaning": "icdo:9987/3",
          "comments": []
        },
        "Thymic carcinoma, NOS": {
          "meaning": "icdo:8586/3",
          "comments": []
        },
        "Thymoma, malignant, NOS": {
          "meaning": "icdo:8580/3",
          "comments": []
        },
        "Thymoma, type A, malignant": {
          "meaning": "icdo:8581/3",
          "comments": []
        },
        "Thymoma, type AB, malignant": {
          "meaning": "icdo:8582/3",
          "comments": []
        },
        "Thymoma, type B1, malignant": {
          "meaning": "icdo:8583/3",
          "comments": []
        },
        "Thymoma, type B2, malignant": {
          "meaning": "icdo:8584/3",
          "comments": []
        },
        "Thymoma, type B3, malignant": {
          "meaning": "icdo:8585/3",
          "comments": []
        },
        "Trabecular adenocarcinoma": {
          "meaning": "icdo:8190/3",
          "comments": []
        },
        "Trans. cell carcinoma, spindle cell": {
          "meaning": "icdo:8122/3",
          "comments": []
        },
        "Transitional cell carcinoma in situ": {
          "meaning": "icdo:8120/2",
          "comments": []
        },
        "Transitional cell carcinoma, NOS": {
          "meaning": "icdo:8120/3",
          "comments": []
        },
        "Transitional cell carcinoma, micropapillary": {
          "meaning": "icdo:8131/3",
          "comments": []
        },
        "Transitional meningioma": {
          "meaning": "icdo:9537/0",
          "comments": []
        },
        "Trophoblastic tumor, epithelioid": {
          "meaning": "icdo:9105/3",
          "comments": []
        },
        "Tubular adenocarcinoma": {
          "meaning": "icdo:8211/3",
          "comments": []
        },
        "Tumor cells, benign": {
          "meaning": "icdo:8001/0",
          "comments": []
        },
        "Tumor cells, malignant": {
          "meaning": "icdo:8001/3",
          "comments": []
        },
        "Tumor cells, uncertain whether benign or malignant": {
          "meaning": "icdo:8001/1",
          "comments": []
        },
        "Undifferentiated sarcoma": {
          "meaning": "icdo:8805/3",
          "comments": []
        },
        "Venous hemangioma": {
          "meaning": "icdo:9122/0",
          "comments": []
        },
        "Verrucous carcinoma, NOS": {
          "meaning": "icdo:8051/3",
          "comments": []
        },
        "Villous adenocarcinoma": {
          "meaning": "icdo:8262/3",
          "comments": []
        },
        "Waldenstrom macroglobulinemia": {
          "meaning": "icdo:9761/3",
          "comments": []
        },
        "Warthin tumor, malignant": {
          "meaning": "icdo:8561/3",
          "comments": []
        },
        "Warty carcinoma": {
          "meaning": "icdo:8054/3",
          "comments": []
        },
        "Water-clear cell adenocarcinoma": {
          "meaning": "icdo:8322/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocyte-Rich": {
          "meaning": "icdo:9651/3",
          "comments": []
        },
        "Epithelioid Sarcoma": {
          "meaning": "icdo:8804/3",
          "comments": []
        },
        "Yolk Sac Tumor": {
          "meaning": "icdo:9071/3",
          "comments": []
        },
        "Polyembryoma": {
          "meaning": "icdo:9072/3",
          "comments": []
        },
        "Carcinofibroma": {
          "meaning": "icdo:8934/3",
          "comments": []
        },
        "Vipoma": {
          "meaning": "icdo:8155/3",
          "comments": []
        },
        "Synovial Sarcoma, Spindle Cell": {
          "meaning": "icdo:9041/3",
          "comments": []
        },
        "Synovial Sarcoma, Biphasic": {
          "meaning": "icdo:9043/3",
          "comments": []
        },
        "Myxoid Pleomorphic Liposarcoma": {
          "meaning": "icdo:8859/3",
          "comments": []
        },
        "Telangiectatic Osteosarcoma": {
          "meaning": "icdo:9183/3",
          "comments": []
        },
        "Small Cell Osteosarcoma": {
          "meaning": "icdo:9185/3",
          "comments": []
        },
        "Trichilemmocarcinoma": {
          "meaning": "icdo:8102/3",
          "comments": []
        },
        "Pigmented Dermatofibrosarcoma Protuberans": {
          "meaning": "icdo:8833/3",
          "comments": []
        },
        "Teratoma, NOS": {
          "meaning": "icdo:9080/1",
          "comments": []
        },
        "Meningiomatosis, NOS": {
          "meaning": "icdo:9530/1",
          "comments": []
        },
        "Ependymoma, NOS": {
          "meaning": "icdo:9391/3",
          "comments": []
        },
        "Pinealoma, NOS": {
          "meaning": "icdo:9360/1",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Angiogram": {
          "meaning": "ncit:C16290",
          "comments": []
        },
        "Biopsy": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "CT Scan": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "CTA": {
          "meaning": "ncit:C202408",
          "comments": []
        },
        "Colonoscopy": {
          "meaning": "",
          "comments": []
        },
        "Colposcopy": {
          "meaning": "ncit:C16451",
          "comments": []
        },
        "Fine-Needle Aspiration": {
          "meaning": "ncit:C15361",
          "comments": []
        },
        "Imaging, NOS": {
          "meaning": "ncit:C17369",
          "comments": []
        },
        "Incisional Biopsy": {
          "meaning": "ncit:C15386",
          "comments": []
        },
        "MRA": {
          "meaning": "ncit:C114867",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "Mammogram": {
          "meaning": "ncit:C20178",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "Oral Brush Biopsy": {
          "meaning": "",
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
        "PET-MRI": {
          "meaning": "ncit:C103514",
          "comments": []
        },
        "Palpation": {
          "meaning": "ncit:C16950",
          "comments": []
        },
        "Physical Examination": {
          "meaning": "ncit:C20989",
          "comments": []
        },
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        },
        "Upper endoscopy": {
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
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Abdominal Skin": {
          "meaning": "",
          "comments": []
        },
        "Anal/Perianal": {
          "meaning": "ncit:C99148",
          "comments": []
        },
        "Arm Skin": {
          "meaning": "ncit:C52754",
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
        "Buccal Mucosa": {
          "meaning": "ncit:C12505",
          "comments": []
        },
        "Cervix": {
          "meaning": "ncit:C12311",
          "comments": []
        },
        "Ear Skin": {
          "meaning": "ncit:C49481",
          "comments": []
        },
        "Esophagus": {
          "meaning": "ncit:C12389",
          "comments": []
        },
        "Fallopian Tube": {
          "meaning": "",
          "comments": []
        },
        "Gingiva, Lower, Anterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Lower, Posterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, NOS": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Upper, Anterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Upper, Posterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Glottis": {
          "meaning": "ncit:C12724",
          "comments": []
        },
        "Hand Skin": {
          "meaning": "ncit:C52753",
          "comments": []
        },
        "Hilar Nodes": {
          "meaning": "ncit:C102330",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "ncit:C12246",
          "comments": []
        },
        "Intestine": {
          "meaning": "ncit:C12736",
          "comments": []
        },
        "Larynx": {
          "meaning": "ncit:C12420",
          "comments": []
        },
        "Leg Skin": {
          "meaning": "ncit:C52749",
          "comments": []
        },
        "Lip": {
          "meaning": "ncit:C12220",
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
        "Mandible": {
          "meaning": "ncit:C12290",
          "comments": []
        },
        "Mediastinal Node": {
          "meaning": "",
          "comments": []
        },
        "Nasal Cavity": {
          "meaning": "ncit:C12424",
          "comments": []
        },
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        },
        "Neck Skin": {
          "meaning": "ncit:C52756",
          "comments": []
        },
        "Oral Cavity": {
          "meaning": "ncit:C12421",
          "comments": []
        },
        "Oropharynx": {
          "meaning": "ncit:C12762",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Palate": {
          "meaning": "ncit:C12229",
          "comments": []
        },
        "Paratracheal Nodes": {
          "meaning": "",
          "comments": []
        },
        "Penis": {
          "meaning": "ncit:C12409",
          "comments": []
        },
        "Pharynx": {
          "meaning": "ncit:C12425",
          "comments": []
        },
        "Primary Peritoneal": {
          "meaning": "",
          "comments": []
        },
        "Pyriform Sinus": {
          "meaning": "ncit:C33439",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Scalp": {
          "meaning": "ncit:C89807",
          "comments": []
        },
        "Skin of the Back": {
          "meaning": "ncit:C142318",
          "comments": []
        },
        "Skin of the Chest": {
          "meaning": "ncit:C161379",
          "comments": []
        },
        "Skin of the Face": {
          "meaning": "ncit:C33561",
          "comments": []
        },
        "Skin of the Lip": {
          "meaning": "ncit:C12291",
          "comments": []
        },
        "Skin of the Upper Limb and Shoulder": {
          "meaning": "ncit:C12296",
          "comments": []
        },
        "Skin, NOS": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Small Bowel": {
          "meaning": "",
          "comments": []
        },
        "Small Intestine": {
          "meaning": "ncit:C12386",
          "comments": []
        },
        "Spinal Cord": {
          "meaning": "ncit:C12464",
          "comments": []
        },
        "Stomach": {
          "meaning": "ncit:C12391",
          "comments": []
        },
        "Submandibular": {
          "meaning": "ncit:C129462",
          "comments": []
        },
        "Tongue": {
          "meaning": "ncit:C12422",
          "comments": []
        },
        "Uterus": {
          "meaning": "ncit:C12405",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
          "comments": []
        },
        "Vaginal Mucosa": {
          "meaning": "",
          "comments": []
        },
        "Vulva": {
          "meaning": "ncit:C12408",
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
        "Sequencing, NGS, ATAC-seq": {
          "meaning": "ncit:C156056",
          "comments": []
        },
        "Sequencing, NGS, Long-Read, Nanopore": {
          "meaning": "ncit:C146818",
          "comments": []
        },
        "Sequencing, NGS, Long-Read, SMRT": {
          "meaning": "ncit:C146819",
          "comments": []
        },
        "Sequencing, NGS, NOS": {
          "meaning": "ncit:C101293",
          "comments": []
        },
        "Sequencing, NGS, RNA-seq": {
          "meaning": "ncit:C124261",
          "comments": []
        },
        "Sequencing, NGS, Single Cell RNA-seq": {
          "meaning": "ncit:C171152",
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
        },
        "Sequencing, Sanger, NOS": {
          "meaning": "",
          "comments": []
        },
        "Western Blot": {
          "meaning": "ncit:C16357",
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
    "GenderIdentityEnum": {
      "permissible_values": {
        "Asked But Declined": {
          "meaning": "",
          "comments": []
        },
        "Female-to-male transsexual": {
          "meaning": "SCTID:407377005",
          "comments": []
        },
        "Identifies As Female Gender": {
          "meaning": "SCTID:446141000124107",
          "comments": []
        },
        "Identifies As Male Gender": {
          "meaning": "SCTID:446151000124109",
          "comments": []
        },
        "Identifies As Nonbinary Gender": {
          "meaning": "SCTID:33791000087105",
          "comments": []
        },
        "Male-To-Female Transsexual": {
          "meaning": "SCTID:407377005",
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
    "PhenosEnum": {
      "permissible_values": {
        "Eye Abnormality": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]"
          ]
        },
        "Genitalia Abnormality": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]"
          ]
        },
        "Microcephaly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [Mexico Registry].[Congenital_anomalies_detected_at_birth].[6=microcephaly]"
          ]
        },
        "Nervous System Abnormality": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Neurological abnormalities]"
          ]
        },
        "Otological Abnormality": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Israel].[Ear Anomaly]",
            "(fa) ConsortiumNote:  [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Ears/Hearing]"
          ]
        },
        "Short Stature": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Growth]"
          ]
        },
        "Skin Pigmentation": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: [Fiesco-Roa et al. - 2019]",
            "(fa) ConsortiumNote:  [German FA Support Group Questionnaire].[Questions about Fanconi Anemia].[Which or where do you have physical abnormalities?].[Skin]"
          ]
        }
      }
    },
    "AeTreatmentEnum": {
      "permissible_values": {
        "Alternative Medications": {
          "meaning": "",
          "comments": []
        },
        "Chemotherapy": {
          "meaning": "",
          "comments": []
        },
        "Immunotherapy": {
          "meaning": "",
          "comments": []
        },
        "Radiation Therapy": {
          "meaning": "",
          "comments": []
        },
        "Stem Cell Transplant": {
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
    "DiseaseGroupEnum": {
      "permissible_values": {
        "FA": {
          "meaning": "",
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
        "Biopsy Only": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Incomplete Resection": {
          "meaning": "ncit:C182305",
          "comments": []
        },
        "No Surgical Resection": {
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
    "AdverseEventEnum": {
      "permissible_values": {
        "Allergic Reaction": {
          "meaning": "ncit:C114476",
          "comments": []
        },
        "Anemia": {
          "meaning": "ncit:C2869",
          "comments": []
        },
        "Aortic Valve Disease": {
          "meaning": "ncit:C143290",
          "comments": []
        },
        "Asystole": {
          "meaning": "ncit:C146731",
          "comments": []
        },
        "Atrial Fibrillation": {
          "meaning": "ncit:C54767",
          "comments": []
        },
        "Atrial Flutter": {
          "meaning": "ncit:C54768",
          "comments": []
        },
        "Atrioventricular Block Complete": {
          "meaning": "ncit:C143308",
          "comments": []
        },
        "Atrioventricular Block First Degree": {
          "meaning": "ncit:C143309",
          "comments": []
        },
        "Blood and Lymphatic System Disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Bone Marrow Hypocellular": {
          "meaning": "ncit:C3516",
          "comments": []
        },
        "Cardiac Arrest": {
          "meaning": "ncit:c143351",
          "comments": []
        },
        "Cardiac Disorders - Other, Specify": {
          "meaning": "ncit:c143352",
          "comments": []
        },
        "Chest Pain - Cardiac": {
          "meaning": "ncit:c143364",
          "comments": []
        },
        "Conduction Disorder": {
          "meaning": "ncit:c143380",
          "comments": []
        },
        "Cataract": {
          "meaning": "ncit:C26713",
          "comments": []
        },
        "Heart Failure": {
          "meaning": "ncit:c143529",
          "comments": []
        },
        "Mitral Valve Disease": {
          "meaning": "ncit:c143674",
          "comments": []
        },
        "Mobitz (Type) Ii Atrioventricular Block": {
          "meaning": "ncit:c54772",
          "comments": []
        },
        "Mobitz Type I": {
          "meaning": "ncit:c54771",
          "comments": []
        },
        "Myocardial Infarction": {
          "meaning": "ncit:c143691",
          "comments": []
        },
        "Myocarditis": {
          "meaning": "ncit:c146695",
          "comments": []
        },
        "Palpitations": {
          "meaning": "ncit:c54935",
          "comments": []
        },
        "Paroxysmal Atrial Tachycardia": {
          "meaning": "ncit:c143738",
          "comments": []
        },
        "Pericardial Effusion": {
          "meaning": "ncit:c143743",
          "comments": []
        },
        "Pericardial Tamponade": {
          "meaning": "ncit:c143744",
          "comments": []
        },
        "Pericarditis": {
          "meaning": "ncit:c55067",
          "comments": []
        },
        "Pulmonary Valve Disease": {
          "meaning": "ncit:c143793",
          "comments": []
        },
        "Restrictive Cardiomyopathy": {
          "meaning": "ncit:c55069",
          "comments": []
        },
        "Right Ventricular Dysfunction": {
          "meaning": "ncit:c55070",
          "comments": []
        },
        "Sick Sinus Syndrome": {
          "meaning": "ncit:c54938",
          "comments": []
        },
        "Sinus Bradycardia": {
          "meaning": "ncit:c54940",
          "comments": []
        },
        "Sinus Tachycardia": {
          "meaning": "ncit:c26889",
          "comments": []
        },
        "Supraventricular Tachycardia": {
          "meaning": "ncit:c54945",
          "comments": []
        },
        "Tricuspid Valve Disease": {
          "meaning": "ncit:c143889",
          "comments": []
        },
        "Ventricular Arrhythmia": {
          "meaning": "ncit:c146629",
          "comments": []
        },
        "Ventricular Fibrillation": {
          "meaning": "ncit:c146732",
          "comments": []
        },
        "Ventricular Tachycardia": {
          "meaning": "ncit:c146733",
          "comments": []
        },
        "Congenital, Familial And Genetic Disorders - Other, Specify": {
          "meaning": "ncit:c143382",
          "comments": []
        },
        "Ear And Labyrinth Disorders - Other, Specify": {
          "meaning": "ncit:c143429",
          "comments": []
        },
        "Ear Pain": {
          "meaning": "ncit:c143430",
          "comments": []
        },
        "External Ear Pain": {
          "meaning": "ncit:c146745",
          "comments": []
        },
        "Precocious Puberty": {
          "meaning": "ncit:c146645",
          "comments": []
        },
        "Testosterone Deficiency": {
          "meaning": "ncit:c143195",
          "comments": []
        },
        "Virilization": {
          "meaning": "ncit:c143937",
          "comments": []
        },
        "Blurred Vision": {
          "meaning": "ncit:c55906",
          "comments": []
        },
        "Corneal Ulcer": {
          "meaning": "ncit:c143387",
          "comments": []
        },
        "Dry Eye": {
          "meaning": "ncit:c143410",
          "comments": []
        },
        "Extraocular Muscle Paresis": {
          "meaning": "ncit:c143466",
          "comments": []
        },
        "Eye Disorders - Other, Specify": {
          "meaning": "ncit:c143468",
          "comments": []
        },
        "Eye Pain": {
          "meaning": "ncit:c146751",
          "comments": []
        },
        "Eyelid Function Disorder": {
          "meaning": "ncit:c143471",
          "comments": []
        },
        "Flashing Lights": {
          "meaning": "ncit:c143489",
          "comments": []
        },
        "Floaters": {
          "meaning": "ncit:c143491",
          "comments": []
        },
        "Glaucoma": {
          "meaning": "ncit:c55842",
          "comments": []
        },
        "Keratitis": {
          "meaning": "ncit:c55847",
          "comments": []
        },
        "Night Blindness": {
          "meaning": "ncit:c143705",
          "comments": []
        },
        "Papilledema": {
          "meaning": "ncit:c143734",
          "comments": []
        },
        "Periorbital Edema": {
          "meaning": "ncit:c143747",
          "comments": []
        },
        "Photophobia": {
          "meaning": "ncit:c146770",
          "comments": []
        },
        "Retinal Detachment": {
          "meaning": "ncit:c146729",
          "comments": []
        },
        "Retinal Tear": {
          "meaning": "ncit:c143814",
          "comments": []
        },
        "Retinal Vascular Disorder": {
          "meaning": "ncit:c143815",
          "comments": []
        },
        "Scleral Disorder": {
          "meaning": "ncit:c143823",
          "comments": []
        },
        "Uveitis": {
          "meaning": "ncit:c55901",
          "comments": []
        },
        "Vitreous Hemorrhage": {
          "meaning": "ncit:c146677",
          "comments": []
        },
        "Watering Eyes": {
          "meaning": "ncit:c143944",
          "comments": []
        },
        "Abdominal Distension": {
          "meaning": "ncit:c143253",
          "comments": []
        },
        "Abdominal Pain": {
          "meaning": "ncit:c143255",
          "comments": []
        },
        "Anal Fissure": {
          "meaning": "ncit:c143197",
          "comments": []
        },
        "Anal Fistula": {
          "meaning": "ncit:c143275",
          "comments": []
        },
        "Anal Hemorrhage": {
          "meaning": "ncit:c143276",
          "comments": []
        },
        "Anal Mucositis": {
          "meaning": "ncit:c143277",
          "comments": []
        },
        "Anal Necrosis": {
          "meaning": "ncit:c143278",
          "comments": []
        },
        "Anal Pain": {
          "meaning": "ncit:c143279",
          "comments": []
        },
        "Anal Stenosis": {
          "meaning": "ncit:c143280",
          "comments": []
        },
        "Anal Ulcer": {
          "meaning": "ncit:c143281",
          "comments": []
        },
        "Ascites": {
          "meaning": "ncit:c143300",
          "comments": []
        },
        "Belching": {
          "meaning": "ncit:c143198",
          "comments": []
        },
        "Bloating": {
          "meaning": "ncit:c143322",
          "comments": []
        },
        "Cecal Hemorrhage": {
          "meaning": "ncit:c143358",
          "comments": []
        },
        "Cheilitis": {
          "meaning": "ncit:c57901",
          "comments": []
        },
        "Chylous Ascites": {
          "meaning": "ncit:c143199",
          "comments": []
        },
        "Colitis": {
          "meaning": "ncit:c57134",
          "comments": []
        },
        "Colonic Fistula": {
          "meaning": "ncit:c143373",
          "comments": []
        },
        "Colonic Hemorrhage": {
          "meaning": "ncit:c143374",
          "comments": []
        },
        "Colonic Obstruction": {
          "meaning": "ncit:c143375",
          "comments": []
        },
        "Colonic Perforation": {
          "meaning": "ncit:c143376",
          "comments": []
        },
        "Colonic Stenosis": {
          "meaning": "ncit:c143377",
          "comments": []
        },
        "Colonic Ulcer": {
          "meaning": "ncit:c143378",
          "comments": []
        },
        "Constipation": {
          "meaning": "ncit:c57141",
          "comments": []
        },
        "Dental Caries": {
          "meaning": "ncit:c143402",
          "comments": []
        },
        "Diarrhea": {
          "meaning": "ncit:c57788",
          "comments": []
        },
        "Dry Mouth": {
          "meaning": "ncit:c143411",
          "comments": []
        },
        "Duodenal Fistula": {
          "meaning": "ncit:c57789",
          "comments": []
        },
        "Duodenal Hemorrhage": {
          "meaning": "ncit:c143414",
          "comments": []
        },
        "Duodenal Obstruction": {
          "meaning": "ncit:c143416",
          "comments": []
        },
        "Duodenal Perforation": {
          "meaning": "ncit:c143417",
          "comments": []
        },
        "Duodenal Stenosis": {
          "meaning": "ncit:c143418",
          "comments": []
        },
        "Duodenal Ulcer": {
          "meaning": "ncit:c143419",
          "comments": []
        },
        "Dyspepsia": {
          "meaning": "ncit:c143425",
          "comments": []
        },
        "Enterocolitis": {
          "meaning": "ncit:c143445",
          "comments": []
        },
        "Enterovesical Fistula": {
          "meaning": "ncit:c143446",
          "comments": []
        },
        "Esophageal Fistula": {
          "meaning": "ncit:c57798",
          "comments": []
        },
        "Esophageal Hemorrhage": {
          "meaning": "ncit:c143453",
          "comments": []
        },
        "Esophageal Necrosis": {
          "meaning": "ncit:c143455",
          "comments": []
        },
        "Esophageal Obstruction": {
          "meaning": "ncit:c143456",
          "comments": []
        },
        "Esophageal Pain": {
          "meaning": "ncit:c143457",
          "comments": []
        },
        "Esophageal Perforation": {
          "meaning": "ncit:c143458",
          "comments": []
        },
        "Esophageal Stenosis": {
          "meaning": "ncit:c143459",
          "comments": []
        },
        "Esophageal Ulcer": {
          "meaning": "ncit:c143460",
          "comments": []
        },
        "Esophageal Varices Hemorrhage": {
          "meaning": "ncit:c146710",
          "comments": []
        },
        "Esophagitis": {
          "meaning": "ncit:c57797",
          "comments": []
        },
        "Fecal Incontinence": {
          "meaning": "ncit:c143482",
          "comments": []
        },
        "Flatulence": {
          "meaning": "ncit:c57807",
          "comments": []
        },
        "Gastric Fistula": {
          "meaning": "ncit:c143499",
          "comments": []
        },
        "Gastric Hemorrhage": {
          "meaning": "ncit:c143500",
          "comments": []
        },
        "Gastric Necrosis": {
          "meaning": "ncit:c143501",
          "comments": []
        },
        "Gastric Perforation": {
          "meaning": "ncit:c143502",
          "comments": []
        },
        "Gastric Stenosis": {
          "meaning": "ncit:c143503",
          "comments": []
        },
        "Gastric Ulcer": {
          "meaning": "ncit:c143504",
          "comments": []
        },
        "Gastritis": {
          "meaning": "ncit:c57812",
          "comments": []
        },
        "Gastroesophageal Reflux Disease": {
          "meaning": "ncit:c143506",
          "comments": []
        },
        "Gastrointestinal Disorders - Other, Specify": {
          "meaning": "ncit:c143508",
          "comments": []
        },
        "Gastrointestinal Fistula": {
          "meaning": "ncit:c146637",
          "comments": []
        },
        "Gastrointestinal Pain": {
          "meaning": "ncit:c143510",
          "comments": []
        },
        "Gastroparesis": {
          "meaning": "ncit:c143512",
          "comments": []
        },
        "Gingival Pain": {
          "meaning": "ncit:c146626",
          "comments": []
        },
        "Hemorrhoidal Hemorrhage": {
          "meaning": "ncit:c143537",
          "comments": []
        },
        "Hemorrhoids": {
          "meaning": "ncit:c146738",
          "comments": []
        },
        "Ileal Fistula": {
          "meaning": "ncit:c57821",
          "comments": []
        },
        "Ileal Hemorrhage": {
          "meaning": "ncit:c56542",
          "comments": []
        },
        "Ileal Obstruction": {
          "meaning": "ncit:c57823",
          "comments": []
        },
        "Ileal Perforation": {
          "meaning": "ncit:c146633",
          "comments": []
        },
        "Ileal Stenosis": {
          "meaning": "ncit:c143578",
          "comments": []
        },
        "Ileal Ulcer": {
          "meaning": "ncit:c57826",
          "comments": []
        },
        "Ileus": {
          "meaning": "ncit:c57814",
          "comments": []
        },
        "Intra-Abdominal Hemorrhage": {
          "meaning": "ncit:c143595",
          "comments": []
        },
        "Jejunal Fistula": {
          "meaning": "ncit:c57827",
          "comments": []
        },
        "Jejunal Hemorrhage": {
          "meaning": "ncit:c56543",
          "comments": []
        },
        "Jejunal Obstruction": {
          "meaning": "ncit:c57829",
          "comments": []
        },
        "Jejunal Perforation": {
          "meaning": "ncit:c143622",
          "comments": []
        },
        "Jejunal Stenosis": {
          "meaning": "ncit:c143623",
          "comments": []
        },
        "Jejunal Ulcer": {
          "meaning": "ncit:c57832",
          "comments": []
        },
        "Lip Pain": {
          "meaning": "ncit:c146761",
          "comments": []
        },
        "Lower Gastrointestinal Hemorrhage": {
          "meaning": "ncit:c143656",
          "comments": []
        },
        "Malabsorption": {
          "meaning": "ncit:c57838",
          "comments": []
        },
        "Mucositis Oral": {
          "meaning": "ncit:c143679",
          "comments": []
        },
        "Nausea": {
          "meaning": "ncit:c146764",
          "comments": []
        },
        "Obstruction Gastric": {
          "meaning": "ncit:c143710",
          "comments": []
        },
        "Oral Cavity Fistula": {
          "meaning": "ncit:c143715",
          "comments": []
        },
        "Oral Dysesthesia": {
          "meaning": "ncit:c143716",
          "comments": []
        },
        "Oral Hemorrhage": {
          "meaning": "ncit:c56551",
          "comments": []
        },
        "Oral Pain": {
          "meaning": "ncit:c146627",
          "comments": []
        },
        "Pancreatic Duct Stenosis": {
          "meaning": "ncit:c143730",
          "comments": []
        },
        "Pancreatic Fistula": {
          "meaning": "ncit:c57845",
          "comments": []
        },
        "Pancreatic Hemorrhage": {
          "meaning": "ncit:c56554",
          "comments": []
        },
        "Pancreatic Necrosis": {
          "meaning": "ncit:c143732",
          "comments": []
        },
        "Pancreatitis": {
          "meaning": "ncit:c146789",
          "comments": []
        },
        "Periodontal Disease": {
          "meaning": "ncit:c57849",
          "comments": []
        },
        "Peritoneal Necrosis": {
          "meaning": "ncit:c57850",
          "comments": []
        },
        "Proctitis": {
          "meaning": "ncit:c57857",
          "comments": []
        },
        "Rectal Fissure": {
          "meaning": "ncit:c143200",
          "comments": []
        },
        "Rectal Fistula": {
          "meaning": "ncit:c57859",
          "comments": []
        },
        "Rectal Hemorrhage": {
          "meaning": "ncit:c56560",
          "comments": []
        },
        "Rectal Mucositis": {
          "meaning": "ncit:c143802",
          "comments": []
        },
        "Rectal Necrosis": {
          "meaning": "ncit:c57863",
          "comments": []
        },
        "Rectal Obstruction": {
          "meaning": "ncit:c57864",
          "comments": []
        },
        "Rectal Pain": {
          "meaning": "ncit:c146631",
          "comments": []
        },
        "Rectal Perforation": {
          "meaning": "ncit:c146634",
          "comments": []
        },
        "Rectal Stenosis": {
          "meaning": "ncit:c143803",
          "comments": []
        },
        "Rectal Ulcer": {
          "meaning": "ncit:c57867",
          "comments": []
        },
        "Retroperitoneal Hemorrhage": {
          "meaning": "ncit:c146632",
          "comments": []
        },
        "Salivary Duct Inflammation": {
          "meaning": "ncit:c143821",
          "comments": []
        },
        "Salivary Gland Fistula": {
          "meaning": "ncit:c57868",
          "comments": []
        },
        "Small Intestinal Mucositis": {
          "meaning": "ncit:c143842",
          "comments": []
        },
        "Small Intestinal Obstruction": {
          "meaning": "ncit:c143843",
          "comments": []
        },
        "Small Intestinal Perforation": {
          "meaning": "ncit:c146635",
          "comments": []
        },
        "Small Intestinal Stenosis": {
          "meaning": "ncit:c143844",
          "comments": []
        },
        "Small Intestine Ulcer": {
          "meaning": "ncit:c143846",
          "comments": []
        },
        "Stomach Pain": {
          "meaning": "ncit:c146774",
          "comments": []
        },
        "Middle Ear Inflammation": {
          "meaning": "ncit:c143673",
          "comments": []
        },
        "Vestibular Disorder": {
          "meaning": "ncit:c143936",
          "comments": []
        },
        "Adrenal Insufficiency": {
          "meaning": "ncit:c55748",
          "comments": []
        },
        "Cushingoid": {
          "meaning": "ncit:c143392",
          "comments": []
        },
        "Delayed Puberty": {
          "meaning": "ncit:c55742",
          "comments": []
        },
        "Endocrine Disorders - Other, Specify": {
          "meaning": "ncit:c143442",
          "comments": []
        },
        "Growth Accelerated": {
          "meaning": "ncit:c143520",
          "comments": []
        },
        "Hyperparathyroidism": {
          "meaning": "ncit:c143557",
          "comments": []
        },
        "Hyperthyroidism": {
          "meaning": "ncit:c143560",
          "comments": []
        },
        "Hypoparathyroidism": {
          "meaning": "ncit:c143572",
          "comments": []
        },
        "Tooth development disorder": {
          "meaning": "",
          "comments": []
        },
        "Tooth discoloration": {
          "meaning": "",
          "comments": []
        },
        "Toothache": {
          "meaning": "",
          "comments": []
        },
        "Pelvic floor muscle weakness": {
          "meaning": "",
          "comments": []
        },
        "Pelvic pain": {
          "meaning": "",
          "comments": []
        },
        "Penile pain": {
          "meaning": "",
          "comments": []
        },
        "Perineal pain": {
          "meaning": "",
          "comments": []
        },
        "Premature menopause": {
          "meaning": "",
          "comments": []
        },
        "Prostatic hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Prostatic obstruction": {
          "meaning": "",
          "comments": []
        },
        "Prostatic pain": {
          "meaning": "",
          "comments": []
        },
        "Reproductive system and breast disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Scrotal pain": {
          "meaning": "",
          "comments": []
        },
        "Spermatic cord hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Spermatic cord obstruction": {
          "meaning": "",
          "comments": []
        },
        "Testicular disorder": {
          "meaning": "",
          "comments": []
        },
        "Testicular hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Testicular pain": {
          "meaning": "",
          "comments": []
        },
        "Uterine fistula": {
          "meaning": "",
          "comments": []
        },
        "Uterine hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Uterine obstruction": {
          "meaning": "",
          "comments": []
        },
        "Uterine pain": {
          "meaning": "",
          "comments": []
        },
        "Vaginal discharge": {
          "meaning": "",
          "comments": []
        },
        "Vaginal dryness": {
          "meaning": "",
          "comments": []
        },
        "Vaginal fistula": {
          "meaning": "",
          "comments": []
        },
        "Vaginal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Vaginal inflammation": {
          "meaning": "",
          "comments": []
        },
        "Vaginal obstruction": {
          "meaning": "",
          "comments": []
        },
        "Vaginal pain": {
          "meaning": "",
          "comments": []
        },
        "Vaginal perforation": {
          "meaning": "",
          "comments": []
        },
        "Vaginal stricture": {
          "meaning": "",
          "comments": []
        },
        "Adult respiratory distress syndrome": {
          "meaning": "",
          "comments": []
        },
        "Allergic rhinitis": {
          "meaning": "",
          "comments": []
        },
        "Apnea": {
          "meaning": "",
          "comments": []
        },
        "Aspiration": {
          "meaning": "",
          "comments": []
        },
        "Atelectasis": {
          "meaning": "",
          "comments": []
        },
        "Bronchial fistula": {
          "meaning": "",
          "comments": []
        },
        "Bronchial obstruction": {
          "meaning": "",
          "comments": []
        },
        "Bronchial stricture": {
          "meaning": "",
          "comments": []
        },
        "Bronchopleural fistula": {
          "meaning": "",
          "comments": []
        },
        "Bronchopulmonary hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Bronchospasm": {
          "meaning": "",
          "comments": []
        },
        "Chylothorax": {
          "meaning": "",
          "comments": []
        },
        "Cough": {
          "meaning": "",
          "comments": []
        },
        "Dyspnea": {
          "meaning": "",
          "comments": []
        },
        "Epistaxis": {
          "meaning": "",
          "comments": []
        },
        "Hiccups": {
          "meaning": "",
          "comments": []
        },
        "Hypoxia": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal edema": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal fistula": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal inflammation": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal mucositis": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal obstruction": {
          "meaning": "",
          "comments": []
        },
        "Laryngeal stenosis": {
          "meaning": "",
          "comments": []
        },
        "Laryngopharyngeal dysesthesia": {
          "meaning": "",
          "comments": []
        },
        "Laryngospasm": {
          "meaning": "",
          "comments": []
        },
        "Mediastinal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Nasal congestion": {
          "meaning": "",
          "comments": []
        },
        "Oropharyngeal pain": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal fistula": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal mucositis": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal necrosis": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal stenosis": {
          "meaning": "",
          "comments": []
        },
        "Pharyngolaryngeal pain": {
          "meaning": "",
          "comments": []
        },
        "Pleural effusion": {
          "meaning": "",
          "comments": []
        },
        "Pleural hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Pleuritic pain": {
          "meaning": "",
          "comments": []
        },
        "Pneumonitis": {
          "meaning": "",
          "comments": []
        },
        "Pneumothorax": {
          "meaning": "",
          "comments": []
        },
        "Postnasal drip": {
          "meaning": "",
          "comments": []
        },
        "Productive cough": {
          "meaning": "",
          "comments": []
        },
        "Pulmonary edema": {
          "meaning": "",
          "comments": []
        },
        "Pulmonary fibrosis": {
          "meaning": "",
          "comments": []
        },
        "Pulmonary fistula": {
          "meaning": "",
          "comments": []
        },
        "Pulmonary hypertension": {
          "meaning": "",
          "comments": []
        },
        "Respiratory failure": {
          "meaning": "",
          "comments": []
        },
        "Respiratory, thoracic and mediastinal disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Retinoic acid syndrome": {
          "meaning": "",
          "comments": []
        },
        "Rhinorrhea": {
          "meaning": "",
          "comments": []
        },
        "Sinus disorder": {
          "meaning": "",
          "comments": []
        },
        "Sinus pain": {
          "meaning": "",
          "comments": []
        },
        "Sleep apnea": {
          "meaning": "",
          "comments": []
        },
        "Sneezing": {
          "meaning": "",
          "comments": []
        },
        "Sore throat": {
          "meaning": "",
          "comments": []
        },
        "Stridor": {
          "meaning": "",
          "comments": []
        },
        "Tracheal fistula": {
          "meaning": "",
          "comments": []
        },
        "Tracheal mucositis": {
          "meaning": "",
          "comments": []
        },
        "Tracheal stenosis": {
          "meaning": "",
          "comments": []
        },
        "Voice alteration": {
          "meaning": "",
          "comments": []
        },
        "Wheezing": {
          "meaning": "",
          "comments": []
        },
        "Alopecia": {
          "meaning": "",
          "comments": []
        },
        "Body odor": {
          "meaning": "",
          "comments": []
        },
        "Bullous dermatitis": {
          "meaning": "",
          "comments": []
        },
        "Dry skin": {
          "meaning": "",
          "comments": []
        },
        "Eczema": {
          "meaning": "",
          "comments": []
        },
        "Erythema multiforme": {
          "meaning": "",
          "comments": []
        },
        "Erythroderma": {
          "meaning": "",
          "comments": []
        },
        "Fat atrophy": {
          "meaning": "",
          "comments": []
        },
        "Hair color changes": {
          "meaning": "",
          "comments": []
        },
        "Hair texture abnormal": {
          "meaning": "",
          "comments": []
        },
        "Hirsutism": {
          "meaning": "",
          "comments": []
        },
        "Hyperhidrosis": {
          "meaning": "",
          "comments": []
        },
        "Hyperkeratosis": {
          "meaning": "",
          "comments": []
        },
        "Hypertrichosis": {
          "meaning": "",
          "comments": []
        },
        "Hypohidrosis": {
          "meaning": "",
          "comments": []
        },
        "Lipohypertrophy": {
          "meaning": "",
          "comments": []
        },
        "Nail changes": {
          "meaning": "",
          "comments": []
        },
        "Nail discoloration": {
          "meaning": "",
          "comments": []
        },
        "Nail loss": {
          "meaning": "",
          "comments": []
        },
        "Nail ridging": {
          "meaning": "",
          "comments": []
        },
        "Pain of skin": {
          "meaning": "",
          "comments": []
        },
        "Palmar-plantar erythrodysesthesia syndrome": {
          "meaning": "",
          "comments": []
        },
        "Photosensitivity": {
          "meaning": "",
          "comments": []
        },
        "Pruritus": {
          "meaning": "",
          "comments": []
        },
        "Purpura": {
          "meaning": "",
          "comments": []
        },
        "Rash acneiform": {
          "meaning": "",
          "comments": []
        },
        "Rash maculo-papular": {
          "meaning": "",
          "comments": []
        },
        "Scalp pain": {
          "meaning": "",
          "comments": []
        },
        "Skin and subcutaneous tissue disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Skin atrophy": {
          "meaning": "",
          "comments": []
        },
        "Skin hyperpigmentation": {
          "meaning": "",
          "comments": []
        },
        "Skin hypopigmentation": {
          "meaning": "",
          "comments": []
        },
        "Skin induration": {
          "meaning": "",
          "comments": []
        },
        "Skin ulceration": {
          "meaning": "",
          "comments": []
        },
        "Stevens-Johnson syndrome": {
          "meaning": "",
          "comments": []
        },
        "Subcutaneous emphysema": {
          "meaning": "",
          "comments": []
        },
        "Telangiectasia": {
          "meaning": "",
          "comments": []
        },
        "Toxic epidermal necrolysis": {
          "meaning": "",
          "comments": []
        },
        "Urticaria": {
          "meaning": "",
          "comments": []
        },
        "Social circumstances - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Surgical and medical procedures - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Arterial thromboembolism": {
          "meaning": "",
          "comments": []
        },
        "Capillary leak syndrome": {
          "meaning": "",
          "comments": []
        },
        "Flushing": {
          "meaning": "",
          "comments": []
        },
        "Hematoma": {
          "meaning": "",
          "comments": []
        },
        "Hot flashes": {
          "meaning": "",
          "comments": []
        },
        "Hypertension": {
          "meaning": "",
          "comments": []
        },
        "Hypotension": {
          "meaning": "",
          "comments": []
        },
        "Lymph leakage": {
          "meaning": "",
          "comments": []
        },
        "Lymphedema": {
          "meaning": "",
          "comments": []
        },
        "Lymphocele": {
          "meaning": "",
          "comments": []
        },
        "Peripheral ischemia": {
          "meaning": "",
          "comments": []
        },
        "Phlebitis": {
          "meaning": "",
          "comments": []
        },
        "Superficial thrombophlebitis": {
          "meaning": "",
          "comments": []
        },
        "Superior vena cava syndrome": {
          "meaning": "",
          "comments": []
        },
        "Thromboembolic event": {
          "meaning": "",
          "comments": []
        },
        "Vascular disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Vasculitis": {
          "meaning": "",
          "comments": []
        },
        "Superficial soft tissue fibrosis": {
          "meaning": "",
          "comments": []
        },
        "Unequal limb length": {
          "meaning": "",
          "comments": []
        },
        "Leukemia secondary to oncology chemotherapy": {
          "meaning": "",
          "comments": []
        },
        "Myelodysplastic syndrome": {
          "meaning": "",
          "comments": []
        },
        "Neoplasms benign, malignant and unspecified (incl cysts and polyps) - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Skin papilloma": {
          "meaning": "",
          "comments": []
        },
        "Treatment related secondary malignancy": {
          "meaning": "",
          "comments": []
        },
        "Tumor hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Tumor pain": {
          "meaning": "",
          "comments": []
        },
        "Abducens nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Accessory nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Acoustic nerve disorder NOS": {
          "meaning": "",
          "comments": []
        },
        "Akathisia": {
          "meaning": "",
          "comments": []
        },
        "Amnesia": {
          "meaning": "",
          "comments": []
        },
        "Anosmia": {
          "meaning": "",
          "comments": []
        },
        "Aphonia": {
          "meaning": "",
          "comments": []
        },
        "Arachnoiditis": {
          "meaning": "",
          "comments": []
        },
        "Ataxia": {
          "meaning": "",
          "comments": []
        },
        "Brachial plexopathy": {
          "meaning": "",
          "comments": []
        },
        "Central nervous system necrosis": {
          "meaning": "",
          "comments": []
        },
        "Cerebrospinal fluid leakage": {
          "meaning": "",
          "comments": []
        },
        "Cognitive disturbance": {
          "meaning": "",
          "comments": []
        },
        "Concentration impairment": {
          "meaning": "",
          "comments": []
        },
        "Depressed level of consciousness": {
          "meaning": "",
          "comments": []
        },
        "Dizziness": {
          "meaning": "",
          "comments": []
        },
        "Dysarthria": {
          "meaning": "",
          "comments": []
        },
        "Dysesthesia": {
          "meaning": "",
          "comments": []
        },
        "Dysgeusia": {
          "meaning": "",
          "comments": []
        },
        "Dysphasia": {
          "meaning": "",
          "comments": []
        },
        "Edema cerebral": {
          "meaning": "",
          "comments": []
        },
        "Encephalopathy": {
          "meaning": "",
          "comments": []
        },
        "Extrapyramidal disorder": {
          "meaning": "",
          "comments": []
        },
        "Facial muscle weakness": {
          "meaning": "",
          "comments": []
        },
        "Facial nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Glossopharyngeal nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Guillain-Barre syndrome": {
          "meaning": "",
          "comments": []
        },
        "Headache": {
          "meaning": "",
          "comments": []
        },
        "Hydrocephalus": {
          "meaning": "",
          "comments": []
        },
        "Hypersomnia": {
          "meaning": "",
          "comments": []
        },
        "Hypoglossal nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Intracranial hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Ischemia cerebrovascular": {
          "meaning": "",
          "comments": []
        },
        "Lethargy": {
          "meaning": "",
          "comments": []
        },
        "Leukoencephalopathy": {
          "meaning": "",
          "comments": []
        },
        "Memory impairment": {
          "meaning": "",
          "comments": []
        },
        "Meningismus": {
          "meaning": "",
          "comments": []
        },
        "Movements involuntary": {
          "meaning": "",
          "comments": []
        },
        "Muscle weakness left-sided": {
          "meaning": "",
          "comments": []
        },
        "Muscle weakness right-sided": {
          "meaning": "",
          "comments": []
        },
        "Myasthenia gravis": {
          "meaning": "",
          "comments": []
        },
        "Nervous system disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Neuralgia": {
          "meaning": "",
          "comments": []
        },
        "Nystagmus": {
          "meaning": "",
          "comments": []
        },
        "Oculomotor nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Olfactory nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Paresthesia": {
          "meaning": "ncit:C143736",
          "comments": []
        },
        "Peripheral motor neuropathy": {
          "meaning": "",
          "comments": []
        },
        "Peripheral sensory neuropathy": {
          "meaning": "",
          "comments": []
        },
        "Phantom pain": {
          "meaning": "",
          "comments": []
        },
        "Presyncope": {
          "meaning": "",
          "comments": []
        },
        "Pyramidal tract syndrome": {
          "meaning": "",
          "comments": []
        },
        "Radiculitis": {
          "meaning": "",
          "comments": []
        },
        "Recurrent laryngeal nerve palsy": {
          "meaning": "",
          "comments": []
        },
        "Reversible posterior leukoencephalopathy syndrome": {
          "meaning": "",
          "comments": []
        },
        "Seizure": {
          "meaning": "",
          "comments": []
        },
        "Somnolence": {
          "meaning": "",
          "comments": []
        },
        "Spasticity": {
          "meaning": "",
          "comments": []
        },
        "Spinal cord compression": {
          "meaning": "",
          "comments": []
        },
        "Syncope": {
          "meaning": "",
          "comments": []
        },
        "Tendon reflex decreased": {
          "meaning": "",
          "comments": []
        },
        "Transient ischemic attacks": {
          "meaning": "",
          "comments": []
        },
        "Tremor": {
          "meaning": "",
          "comments": []
        },
        "Trigeminal nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Trochlear nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Vagus nerve disorder": {
          "meaning": "",
          "comments": []
        },
        "Vasovagal reaction": {
          "meaning": "",
          "comments": []
        },
        "Fetal growth retardation": {
          "meaning": "",
          "comments": []
        },
        "Pregnancy loss": {
          "meaning": "",
          "comments": []
        },
        "Pregnancy, puerperium and perinatal conditions - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Premature delivery": {
          "meaning": "",
          "comments": []
        },
        "Agitation": {
          "meaning": "",
          "comments": []
        },
        "Anorgasmia": {
          "meaning": "",
          "comments": []
        },
        "Anxiety": {
          "meaning": "",
          "comments": []
        },
        "Confusion": {
          "meaning": "",
          "comments": []
        },
        "Delayed orgasm": {
          "meaning": "",
          "comments": []
        },
        "Delirium": {
          "meaning": "",
          "comments": []
        },
        "Delusions": {
          "meaning": "",
          "comments": []
        },
        "Depression": {
          "meaning": "",
          "comments": []
        },
        "Euphoria": {
          "meaning": "",
          "comments": []
        },
        "Hallucinations": {
          "meaning": "",
          "comments": []
        },
        "Insomnia": {
          "meaning": "",
          "comments": []
        },
        "Irritability": {
          "meaning": "",
          "comments": []
        },
        "Libido decreased": {
          "meaning": "",
          "comments": []
        },
        "Libido increased": {
          "meaning": "",
          "comments": []
        },
        "Mania": {
          "meaning": "",
          "comments": []
        },
        "Personality change": {
          "meaning": "",
          "comments": []
        },
        "Psychiatric disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Psychosis": {
          "meaning": "",
          "comments": []
        },
        "Restlessness": {
          "meaning": "",
          "comments": []
        },
        "Suicidal ideation": {
          "meaning": "",
          "comments": []
        },
        "Suicide attempt": {
          "meaning": "",
          "comments": []
        },
        "Acute kidney injury": {
          "meaning": "",
          "comments": []
        },
        "Bladder perforation": {
          "meaning": "",
          "comments": []
        },
        "Bladder spasm": {
          "meaning": "",
          "comments": []
        },
        "Chronic kidney disease": {
          "meaning": "",
          "comments": []
        },
        "Cystitis noninfective": {
          "meaning": "",
          "comments": []
        },
        "Dysuria": {
          "meaning": "",
          "comments": []
        },
        "Glucosuria": {
          "meaning": "",
          "comments": []
        },
        "Hemoglobinuria": {
          "meaning": "",
          "comments": []
        },
        "Nephrotic syndrome": {
          "meaning": "",
          "comments": []
        },
        "Renal and urinary disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Renal calculi": {
          "meaning": "",
          "comments": []
        },
        "Renal colic": {
          "meaning": "",
          "comments": []
        },
        "Renal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Urinary fistula": {
          "meaning": "",
          "comments": []
        },
        "Urinary frequency": {
          "meaning": "",
          "comments": []
        },
        "Urinary incontinence": {
          "meaning": "",
          "comments": []
        },
        "Urinary retention": {
          "meaning": "",
          "comments": []
        },
        "Urinary tract obstruction": {
          "meaning": "",
          "comments": []
        },
        "Urinary tract pain": {
          "meaning": "",
          "comments": []
        },
        "Urinary urgency": {
          "meaning": "",
          "comments": []
        },
        "Urine discoloration": {
          "meaning": "",
          "comments": []
        },
        "Amenorrhea": {
          "meaning": "",
          "comments": []
        },
        "Azoospermia": {
          "meaning": "",
          "comments": []
        },
        "Breast atrophy": {
          "meaning": "",
          "comments": []
        },
        "Breast pain": {
          "meaning": "",
          "comments": []
        },
        "Dysmenorrhea": {
          "meaning": "",
          "comments": []
        },
        "Dyspareunia": {
          "meaning": "",
          "comments": []
        },
        "Ejaculation disorder": {
          "meaning": "",
          "comments": []
        },
        "Erectile dysfunction": {
          "meaning": "",
          "comments": []
        },
        "Fallopian tube obstruction": {
          "meaning": "",
          "comments": []
        },
        "Feminization acquired": {
          "meaning": "",
          "comments": []
        },
        "Genital edema": {
          "meaning": "",
          "comments": []
        },
        "Gynecomastia": {
          "meaning": "",
          "comments": []
        },
        "Hematosalpinx": {
          "meaning": "",
          "comments": []
        },
        "Irregular menstruation": {
          "meaning": "",
          "comments": []
        },
        "Lactation disorder": {
          "meaning": "",
          "comments": []
        },
        "Menorrhagia": {
          "meaning": "",
          "comments": []
        },
        "Nipple deformity": {
          "meaning": "",
          "comments": []
        },
        "Oligospermia": {
          "meaning": "",
          "comments": []
        },
        "Ovarian hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Ovarian rupture": {
          "meaning": "",
          "comments": []
        },
        "Ovulation pain": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative respiratory injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative splenic injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative urinary injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative venous injury": {
          "meaning": "",
          "comments": []
        },
        "Kidney anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Large intestinal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Pancreatic anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Pharyngeal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Postoperative hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Postoperative thoracic procedure complication": {
          "meaning": "",
          "comments": []
        },
        "Prolapse of intestinal stoma": {
          "meaning": "",
          "comments": []
        },
        "Prolapse of urostomy": {
          "meaning": "",
          "comments": []
        },
        "Radiation recall reaction (dermatologic)": {
          "meaning": "",
          "comments": []
        },
        "Rectal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Seroma": {
          "meaning": "",
          "comments": []
        },
        "Small intestinal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Spermatic cord anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Spinal fracture": {
          "meaning": "",
          "comments": []
        },
        "Stenosis of gastrointestinal stoma": {
          "meaning": "",
          "comments": []
        },
        "Stomal ulcer": {
          "meaning": "",
          "comments": []
        },
        "Tracheal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Tracheal obstruction": {
          "meaning": "",
          "comments": []
        },
        "Tracheostomy site bleeding": {
          "meaning": "",
          "comments": []
        },
        "Ureteric anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Urethral anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Urostomy leak": {
          "meaning": "",
          "comments": []
        },
        "Urostomy obstruction": {
          "meaning": "",
          "comments": []
        },
        "Urostomy site bleeding": {
          "meaning": "",
          "comments": []
        },
        "Urostomy stenosis": {
          "meaning": "",
          "comments": []
        },
        "Uterine anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Uterine perforation": {
          "meaning": "",
          "comments": []
        },
        "Vaccination complication": {
          "meaning": "",
          "comments": []
        },
        "Vaginal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Vas deferens anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Vascular access complication": {
          "meaning": "",
          "comments": []
        },
        "Venous injury": {
          "meaning": "",
          "comments": []
        },
        "Wound complication": {
          "meaning": "",
          "comments": []
        },
        "Wound dehiscence": {
          "meaning": "",
          "comments": []
        },
        "Wrist fracture": {
          "meaning": "",
          "comments": []
        },
        "Activated partial thromboplastin time prolonged": {
          "meaning": "",
          "comments": []
        },
        "Alanine aminotransferase increased": {
          "meaning": "",
          "comments": []
        },
        "Alkaline phosphatase increased": {
          "meaning": "",
          "comments": []
        },
        "Aspartate aminotransferase increased": {
          "meaning": "",
          "comments": []
        },
        "Blood antidiuretic hormone abnormal": {
          "meaning": "",
          "comments": []
        },
        "Blood bicarbonate decreased": {
          "meaning": "",
          "comments": []
        },
        "Blood bilirubin increased": {
          "meaning": "",
          "comments": []
        },
        "Blood corticotrophin decreased": {
          "meaning": "",
          "comments": []
        },
        "Blood gonadotrophin abnormal": {
          "meaning": "",
          "comments": []
        },
        "Blood lactate dehydrogenase increased": {
          "meaning": "",
          "comments": []
        },
        "Blood prolactin abnormal": {
          "meaning": "",
          "comments": []
        },
        "Carbon monoxide diffusing capacity decreased": {
          "meaning": "",
          "comments": []
        },
        "Cardiac troponin I increased": {
          "meaning": "",
          "comments": []
        },
        "Cardiac troponin T increased": {
          "meaning": "",
          "comments": []
        },
        "CD4 lymphocytes decreased": {
          "meaning": "",
          "comments": []
        },
        "Cholesterol high": {
          "meaning": "",
          "comments": []
        },
        "CPK increased": {
          "meaning": "",
          "comments": []
        },
        "Creatinine increased": {
          "meaning": "",
          "comments": []
        },
        "Ejection fraction decreased": {
          "meaning": "",
          "comments": []
        },
        "Electrocardiogram QT corrected interval prolonged": {
          "meaning": "",
          "comments": []
        },
        "Electrocardiogram T wave abnormal": {
          "meaning": "",
          "comments": []
        },
        "Fibrinogen decreased": {
          "meaning": "",
          "comments": []
        },
        "Forced expiratory volume decreased": {
          "meaning": "",
          "comments": []
        },
        "GGT increased": {
          "meaning": "",
          "comments": []
        },
        "Growth hormone abnormal": {
          "meaning": "",
          "comments": []
        },
        "Haptoglobin decreased": {
          "meaning": "",
          "comments": []
        },
        "Hemoglobin increased": {
          "meaning": "",
          "comments": []
        },
        "INR increased": {
          "meaning": "",
          "comments": []
        },
        "Investigations - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Lipase increased": {
          "meaning": "",
          "comments": []
        },
        "Lymphocyte count decreased": {
          "meaning": "",
          "comments": []
        },
        "Lymphocyte count increased": {
          "meaning": "",
          "comments": []
        },
        "Neutrophil count decreased": {
          "meaning": "",
          "comments": []
        },
        "Pancreatic enzymes decreased": {
          "meaning": "",
          "comments": []
        },
        "Platelet count decreased": {
          "meaning": "",
          "comments": []
        },
        "Serum amylase increased": {
          "meaning": "",
          "comments": []
        },
        "Thyroid stimulating hormone increased": {
          "meaning": "",
          "comments": []
        },
        "Urine output decreased": {
          "meaning": "",
          "comments": []
        },
        "Vital capacity abnormal": {
          "meaning": "",
          "comments": []
        },
        "Weight gain": {
          "meaning": "",
          "comments": []
        },
        "Weight loss": {
          "meaning": "",
          "comments": []
        },
        "White blood cell decreased": {
          "meaning": "",
          "comments": []
        },
        "Acidosis": {
          "meaning": "",
          "comments": []
        },
        "Alcohol intolerance": {
          "meaning": "",
          "comments": []
        },
        "Alkalosis": {
          "meaning": "",
          "comments": []
        },
        "Anorexia": {
          "meaning": "",
          "comments": []
        },
        "Dehydration": {
          "meaning": "",
          "comments": []
        },
        "Glucose intolerance": {
          "meaning": "",
          "comments": []
        },
        "Hypercalcemia": {
          "meaning": "",
          "comments": []
        },
        "Hyperglycemia": {
          "meaning": "",
          "comments": []
        },
        "Hyperkalemia": {
          "meaning": "",
          "comments": []
        },
        "Hyperlipidemia": {
          "meaning": "",
          "comments": []
        },
        "Hypermagnesemia": {
          "meaning": "",
          "comments": []
        },
        "Hypernatremia": {
          "meaning": "",
          "comments": []
        },
        "Hyperphosphatemia": {
          "meaning": "",
          "comments": []
        },
        "Hypertriglyceridemia": {
          "meaning": "",
          "comments": []
        },
        "Hyperuricemia": {
          "meaning": "",
          "comments": []
        },
        "Hypoalbuminemia": {
          "meaning": "",
          "comments": []
        },
        "Hypocalcemia": {
          "meaning": "",
          "comments": []
        },
        "Hypoglycemia": {
          "meaning": "",
          "comments": []
        },
        "Hypokalemia": {
          "meaning": "",
          "comments": []
        },
        "Hypomagnesemia": {
          "meaning": "",
          "comments": []
        },
        "Hyponatremia": {
          "meaning": "",
          "comments": []
        },
        "Hypophosphatemia": {
          "meaning": "",
          "comments": []
        },
        "Iron overload": {
          "meaning": "",
          "comments": []
        },
        "Metabolism and nutrition disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Obesity": {
          "meaning": "",
          "comments": []
        },
        "Tumor lysis syndrome": {
          "meaning": "",
          "comments": []
        },
        "Abdominal soft tissue necrosis": {
          "meaning": "",
          "comments": []
        },
        "Arthralgia": {
          "meaning": "",
          "comments": []
        },
        "Arthritis": {
          "meaning": "",
          "comments": []
        },
        "Avascular necrosis": {
          "meaning": "",
          "comments": []
        },
        "Back pain": {
          "meaning": "",
          "comments": []
        },
        "Bone pain": {
          "meaning": "",
          "comments": []
        },
        "Buttock pain": {
          "meaning": "",
          "comments": []
        },
        "Chest wall necrosis": {
          "meaning": "",
          "comments": []
        },
        "Chest wall pain": {
          "meaning": "",
          "comments": []
        },
        "Exostosis": {
          "meaning": "",
          "comments": []
        },
        "Fibrosis deep connective tissue": {
          "meaning": "",
          "comments": []
        },
        "Flank pain": {
          "meaning": "",
          "comments": []
        },
        "Generalized muscle weakness": {
          "meaning": "",
          "comments": []
        },
        "Growth suppression": {
          "meaning": "",
          "comments": []
        },
        "Head soft tissue necrosis": {
          "meaning": "",
          "comments": []
        },
        "Joint effusion": {
          "meaning": "",
          "comments": []
        },
        "Joint range of motion decreased": {
          "meaning": "",
          "comments": []
        },
        "Joint range of motion decreased cervical spine": {
          "meaning": "",
          "comments": []
        },
        "Joint range of motion decreased lumbar spine": {
          "meaning": "",
          "comments": []
        },
        "Kyphosis": {
          "meaning": "",
          "comments": []
        },
        "Lordosis": {
          "meaning": "",
          "comments": []
        },
        "Muscle cramp": {
          "meaning": "",
          "comments": []
        },
        "Muscle weakness lower limb": {
          "meaning": "",
          "comments": []
        },
        "Muscle weakness trunk": {
          "meaning": "",
          "comments": []
        },
        "Muscle weakness upper limb": {
          "meaning": "",
          "comments": []
        },
        "Musculoskeletal and connective tissue disorder - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Musculoskeletal deformity": {
          "meaning": "",
          "comments": []
        },
        "Myalgia": {
          "meaning": "",
          "comments": []
        },
        "Myositis": {
          "meaning": "",
          "comments": []
        },
        "Neck pain": {
          "meaning": "",
          "comments": []
        },
        "Neck soft tissue necrosis": {
          "meaning": "",
          "comments": []
        },
        "Osteonecrosis": {
          "meaning": "",
          "comments": []
        },
        "Osteonecrosis of jaw": {
          "meaning": "",
          "comments": []
        },
        "Osteoporosis": {
          "meaning": "",
          "comments": []
        },
        "Pain in extremity": {
          "meaning": "",
          "comments": []
        },
        "Pelvic soft tissue necrosis": {
          "meaning": "",
          "comments": []
        },
        "Rhabdomyolysis": {
          "meaning": "",
          "comments": []
        },
        "Rotator cuff injury": {
          "meaning": "",
          "comments": []
        },
        "Scoliosis": {
          "meaning": "",
          "comments": []
        },
        "Soft tissue necrosis lower limb": {
          "meaning": "",
          "comments": []
        },
        "Soft tissue necrosis upper limb": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder fistula": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder necrosis": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder obstruction": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder pain": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder perforation": {
          "meaning": "",
          "comments": []
        },
        "Hepatic failure": {
          "meaning": "",
          "comments": []
        },
        "Hepatic hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Hepatic necrosis": {
          "meaning": "",
          "comments": []
        },
        "Hepatic pain": {
          "meaning": "",
          "comments": []
        },
        "Hepatobiliary disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Perforation bile duct": {
          "meaning": "",
          "comments": []
        },
        "Portal hypertension": {
          "meaning": "",
          "comments": []
        },
        "Portal vein thrombosis": {
          "meaning": "",
          "comments": []
        },
        "Anaphylaxis": {
          "meaning": "",
          "comments": []
        },
        "Autoimmune disorder": {
          "meaning": "",
          "comments": []
        },
        "Cytokine release syndrome": {
          "meaning": "",
          "comments": []
        },
        "Immune system disorders - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Serum sickness": {
          "meaning": "",
          "comments": []
        },
        "Abdominal infection": {
          "meaning": "",
          "comments": []
        },
        "Anorectal infection": {
          "meaning": "",
          "comments": []
        },
        "Appendicitis": {
          "meaning": "",
          "comments": []
        },
        "Appendicitis perforated": {
          "meaning": "",
          "comments": []
        },
        "Arteritis infective": {
          "meaning": "",
          "comments": []
        },
        "Bacteremia": {
          "meaning": "",
          "comments": []
        },
        "Biliary tract infection": {
          "meaning": "",
          "comments": []
        },
        "Bladder infection": {
          "meaning": "",
          "comments": []
        },
        "Bone infection": {
          "meaning": "",
          "comments": []
        },
        "Breast infection": {
          "meaning": "",
          "comments": []
        },
        "Bronchial infection": {
          "meaning": "",
          "comments": []
        },
        "Catheter related infection": {
          "meaning": "",
          "comments": []
        },
        "Cecal infection": {
          "meaning": "",
          "comments": []
        },
        "Cervicitis infection": {
          "meaning": "",
          "comments": []
        },
        "Conjunctivitis": {
          "meaning": "",
          "comments": []
        },
        "Conjunctivitis infective": {
          "meaning": "",
          "comments": []
        },
        "Corneal infection": {
          "meaning": "",
          "comments": []
        },
        "Cranial nerve infection": {
          "meaning": "",
          "comments": []
        },
        "Cytomegalovirus infection reactivation": {
          "meaning": "",
          "comments": []
        },
        "Device related infection": {
          "meaning": "",
          "comments": []
        },
        "Duodenal infection": {
          "meaning": "",
          "comments": []
        },
        "Encephalitis infection": {
          "meaning": "",
          "comments": []
        },
        "Encephalomyelitis infection": {
          "meaning": "",
          "comments": []
        },
        "Endocarditis infective": {
          "meaning": "",
          "comments": []
        },
        "Endophthalmitis": {
          "meaning": "",
          "comments": []
        },
        "Enterocolitis infectious": {
          "meaning": "",
          "comments": []
        },
        "Epstein-Barr virus infection reactivation": {
          "meaning": "",
          "comments": []
        },
        "Esophageal infection": {
          "meaning": "",
          "comments": []
        },
        "Eye infection": {
          "meaning": "",
          "comments": []
        },
        "Folliculitis": {
          "meaning": "",
          "comments": []
        },
        "Fungemia": {
          "meaning": "",
          "comments": []
        },
        "Gallbladder infection": {
          "meaning": "",
          "comments": []
        },
        "Gum infection": {
          "meaning": "",
          "comments": []
        },
        "Hepatic infection": {
          "meaning": "",
          "comments": []
        },
        "Hepatitis B reactivation": {
          "meaning": "",
          "comments": []
        },
        "Hepatitis viral": {
          "meaning": "",
          "comments": []
        },
        "Herpes simplex reactivation": {
          "meaning": "",
          "comments": []
        },
        "Infections and infestations - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Infective myositis": {
          "meaning": "",
          "comments": []
        },
        "Joint infection": {
          "meaning": "",
          "comments": []
        },
        "Kidney infection": {
          "meaning": "",
          "comments": []
        },
        "Laryngitis": {
          "meaning": "",
          "comments": []
        },
        "Lip infection": {
          "meaning": "",
          "comments": []
        },
        "Lung infection": {
          "meaning": "",
          "comments": []
        },
        "Lymph gland infection": {
          "meaning": "",
          "comments": []
        },
        "Mediastinal infection": {
          "meaning": "",
          "comments": []
        },
        "Meningitis": {
          "meaning": "",
          "comments": []
        },
        "Mucosal infection": {
          "meaning": "",
          "comments": []
        },
        "Myelitis": {
          "meaning": "",
          "comments": []
        },
        "Nail infection": {
          "meaning": "",
          "comments": []
        },
        "Otitis externa": {
          "meaning": "",
          "comments": []
        },
        "Otitis media": {
          "meaning": "",
          "comments": []
        },
        "Ovarian infection": {
          "meaning": "",
          "comments": []
        },
        "Pancreas infection": {
          "meaning": "",
          "comments": []
        },
        "Papulopustular rash": {
          "meaning": "",
          "comments": []
        },
        "Paronychia": {
          "meaning": "",
          "comments": []
        },
        "Pelvic infection": {
          "meaning": "",
          "comments": []
        },
        "Penile infection": {
          "meaning": "",
          "comments": []
        },
        "Periorbital infection": {
          "meaning": "",
          "comments": []
        },
        "Peripheral nerve infection": {
          "meaning": "",
          "comments": []
        },
        "Peritoneal infection": {
          "meaning": "",
          "comments": []
        },
        "Pharyngitis": {
          "meaning": "",
          "comments": []
        },
        "Phlebitis infective": {
          "meaning": "",
          "comments": []
        },
        "Pleural infection": {
          "meaning": "",
          "comments": []
        },
        "Prostate infection": {
          "meaning": "",
          "comments": []
        },
        "Rash pustular": {
          "meaning": "",
          "comments": []
        },
        "Rhinitis infective": {
          "meaning": "",
          "comments": []
        },
        "Salivary gland infection": {
          "meaning": "",
          "comments": []
        },
        "Scrotal infection": {
          "meaning": "",
          "comments": []
        },
        "Sepsis": {
          "meaning": "",
          "comments": []
        },
        "Shingles": {
          "meaning": "",
          "comments": []
        },
        "Sinusitis": {
          "meaning": "",
          "comments": []
        },
        "Skin infection": {
          "meaning": "",
          "comments": []
        },
        "Small intestine infection": {
          "meaning": "",
          "comments": []
        },
        "Soft tissue infection": {
          "meaning": "",
          "comments": []
        },
        "Splenic infection": {
          "meaning": "",
          "comments": []
        },
        "Stoma site infection": {
          "meaning": "",
          "comments": []
        },
        "Thrush": {
          "meaning": "",
          "comments": []
        },
        "Tooth infection": {
          "meaning": "",
          "comments": []
        },
        "Tracheitis": {
          "meaning": "",
          "comments": []
        },
        "Upper respiratory infection": {
          "meaning": "",
          "comments": []
        },
        "Urethral infection": {
          "meaning": "",
          "comments": []
        },
        "Urinary tract infection": {
          "meaning": "",
          "comments": []
        },
        "Uterine infection": {
          "meaning": "",
          "comments": []
        },
        "Vaginal infection": {
          "meaning": "",
          "comments": []
        },
        "Viremia": {
          "meaning": "",
          "comments": []
        },
        "Vulval infection": {
          "meaning": "",
          "comments": []
        },
        "Wound infection": {
          "meaning": "",
          "comments": []
        },
        "Ankle fracture": {
          "meaning": "",
          "comments": []
        },
        "Aortic injury": {
          "meaning": "",
          "comments": []
        },
        "Arterial injury": {
          "meaning": "",
          "comments": []
        },
        "Biliary anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Bladder anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Bruising": {
          "meaning": "",
          "comments": []
        },
        "Burn": {
          "meaning": "",
          "comments": []
        },
        "Dermatitis radiation": {
          "meaning": "",
          "comments": []
        },
        "Esophageal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Fall": {
          "meaning": "",
          "comments": []
        },
        "Fallopian tube anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Fallopian tube perforation": {
          "meaning": "",
          "comments": []
        },
        "Fracture": {
          "meaning": "",
          "comments": []
        },
        "Gastric anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Gastrointestinal anastomotic leak": {
          "meaning": "",
          "comments": []
        },
        "Gastrointestinal stoma necrosis": {
          "meaning": "",
          "comments": []
        },
        "Hip fracture": {
          "meaning": "",
          "comments": []
        },
        "Infusion related reaction": {
          "meaning": "",
          "comments": []
        },
        "Injury to carotid artery": {
          "meaning": "",
          "comments": []
        },
        "Injury to inferior vena cava": {
          "meaning": "",
          "comments": []
        },
        "Injury to jugular vein": {
          "meaning": "",
          "comments": []
        },
        "Injury to superior vena cava": {
          "meaning": "",
          "comments": []
        },
        "Injury, poisoning and procedural complications - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Intestinal stoma leak": {
          "meaning": "",
          "comments": []
        },
        "Intestinal stoma obstruction": {
          "meaning": "",
          "comments": []
        },
        "Intestinal stoma site bleeding": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative arterial injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative breast injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative cardiac injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative ear injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative endocrine injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative gastrointestinal injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative head and neck injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative hepatobiliary injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative musculoskeletal injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative neurological injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative ocular injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative renal injury": {
          "meaning": "",
          "comments": []
        },
        "Intraoperative reproductive tract injury": {
          "meaning": "",
          "comments": []
        },
        "Upper gastrointestinal hemorrhage": {
          "meaning": "",
          "comments": []
        },
        "Visceral arterial ischemia": {
          "meaning": "",
          "comments": []
        },
        "Vomiting": {
          "meaning": "",
          "comments": []
        },
        "Chills": {
          "meaning": "",
          "comments": []
        },
        "Death neonatal": {
          "meaning": "",
          "comments": []
        },
        "Death NOS": {
          "meaning": "",
          "comments": []
        },
        "Disease progression": {
          "meaning": "",
          "comments": []
        },
        "Edema face": {
          "meaning": "",
          "comments": []
        },
        "Edema limbs": {
          "meaning": "",
          "comments": []
        },
        "Edema trunk": {
          "meaning": "",
          "comments": []
        },
        "Facial pain": {
          "meaning": "",
          "comments": []
        },
        "Fever": {
          "meaning": "",
          "comments": []
        },
        "Flu like symptoms": {
          "meaning": "",
          "comments": []
        },
        "Gait disturbance": {
          "meaning": "",
          "comments": []
        },
        "General disorders and administration site conditions - Other, specify": {
          "meaning": "",
          "comments": []
        },
        "Generalized edema": {
          "meaning": "",
          "comments": []
        },
        "Hypothermia": {
          "meaning": "",
          "comments": []
        },
        "Infusion site extravasation": {
          "meaning": "",
          "comments": []
        },
        "Injection site reaction": {
          "meaning": "",
          "comments": []
        },
        "Localized edema": {
          "meaning": "",
          "comments": []
        },
        "Malaise": {
          "meaning": "",
          "comments": []
        },
        "Multi-organ failure": {
          "meaning": "",
          "comments": []
        },
        "Neck edema": {
          "meaning": "",
          "comments": []
        },
        "Non-cardiac chest pain": {
          "meaning": "",
          "comments": []
        },
        "Pain": {
          "meaning": "",
          "comments": []
        },
        "Sudden death NOS": {
          "meaning": "",
          "comments": []
        },
        "Vaccination site lymphadenopathy": {
          "meaning": "",
          "comments": []
        },
        "Bile duct stenosis": {
          "meaning": "",
          "comments": []
        },
        "Biliary fistula": {
          "meaning": "",
          "comments": []
        },
        "Budd-Chiari syndrome": {
          "meaning": "",
          "comments": []
        },
        "Cholecystitis": {
          "meaning": "",
          "comments": []
        },
        "Disseminated Intravascular Coagulation": {
          "meaning": "ncit:C2992",
          "comments": []
        },
        "Dysphagia": {
          "meaning": "ncit:C57795",
          "comments": []
        },
        "Eosinophilia": {
          "meaning": "ncit:C143190",
          "comments": []
        },
        "Fatigue": {
          "meaning": "ncit:C3036",
          "comments": []
        },
        "Febrile Neutropenia": {
          "meaning": "ncit:C35665",
          "comments": []
        },
        "Graft Versus Host Disease": {
          "meaning": "ncit:C3063",
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
        "Hemolysis": {
          "meaning": "ncit:C37965",
          "comments": []
        },
        "Hemolytic Uremic Syndrome": {
          "meaning": "ncit:C75545",
          "comments": []
        },
        "Hoarseness": {
          "meaning": "ncit:C47813",
          "comments": []
        },
        "Hypothyroidism": {
          "meaning": "ncit:C143576",
          "comments": []
        },
        "Left Ventricular Systolic Dysfunction": {
          "meaning": "ncit:C64251",
          "comments": []
        },
        "Leukocytosis": {
          "meaning": "ncit:C35524",
          "comments": []
        },
        "Lymph Node Pain": {
          "meaning": "ncit:C78440",
          "comments": []
        },
        "Methemoglobinemia": {
          "meaning": "ncit:C143191",
          "comments": []
        },
        "Optic Nerve Disorder": {
          "meaning": "ncit:C143714",
          "comments": []
        },
        "Proteinuria": {
          "meaning": "ncit:C38012",
          "comments": []
        },
        "Retinopathy": {
          "meaning": "ncit:C55891",
          "comments": []
        },
        "Sinusoidal Obstruction Syndrome": {
          "meaning": "ncit:C26793",
          "comments": []
        },
        "Stroke": {
          "meaning": "ncit:C143862",
          "comments": []
        },
        "Thrombotic Thrombocytopenic Purpura": {
          "meaning": "ncit:C78797",
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
        "Typhlitis": {
          "meaning": "ncit:C38043",
          "comments": []
        },
        "Vertigo": {
          "meaning": "ncit:C143935",
          "comments": []
        },
        "Vision Decreased": {
          "meaning": "ncit:C143196",
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
        },
        "Buccal Swab": {
          "meaning": "ncit:C113747",
          "comments": []
        },
        "Buffy Coat": {
          "meaning": "ncit:C84507",
          "comments": []
        },
        "Chorionic Villus Sampling": {
          "meaning": "ncit:C92755",
          "comments": []
        },
        "Cord Blood": {
          "meaning": "",
          "comments": []
        },
        "Fetal Amniocytes": {
          "meaning": "",
          "comments": []
        },
        "Hair": {
          "meaning": "",
          "comments": []
        },
        "Lymph Node": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Lymphoblastoid Cell Line": {
          "meaning": "",
          "comments": []
        },
        "Nails": {
          "meaning": "",
          "comments": []
        },
        "Peripheral Blood Lymphocytes": {
          "meaning": "",
          "comments": []
        },
        "Potentially Malignant Lesion": {
          "meaning": "",
          "comments": []
        },
        "Fibroblast": {
          "meaning": "ncit:C12482",
          "comments": []
        },
        "Saliva": {
          "meaning": "ncit:C174119",
          "comments": [
            "(pre) ConsortiumNote: Map to Buccal Swab/Saliva"
          ]
        },
        "Tissue (Non-Neoplastic)": {
          "meaning": "",
          "comments": []
        },
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
    "StemCellProcessingEnum": {
      "permissible_values": {
        "None": {
          "meaning": "",
          "comments": []
        },
        "T Cell Depleted, CD34 Enriched": {
          "meaning": "",
          "comments": []
        },
        "T Cell Depleted, TCRab Depleted": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "HpvStatusEnum": {
      "permissible_values": {
        "Negative": {
          "meaning": "",
          "comments": []
        },
        "Positive": {
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
        "Mobilized Peripheral Blood Stem Cells": {
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
        "Abdominal Peritoneum": {
          "meaning": "ncit:C159355",
          "comments": []
        },
        "Abdominal Skin": {
          "meaning": "ncit:C52758",
          "comments": []
        },
        "Anal/Perianal": {
          "meaning": "ncit:C99148",
          "comments": []
        },
        "Arm Skin": {
          "meaning": "ncit:C52754",
          "comments": []
        },
        "Basal Ganglia-Thalamus": {
          "meaning": "ncit:C158080",
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
        "Buccal Mucosa": {
          "meaning": "ncit:C12505",
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
        "Cervix": {
          "meaning": "ncit:C12311",
          "comments": []
        },
        "Corpus Callosum": {
          "meaning": "ncit:C12446",
          "comments": []
        },
        "Ear Skin": {
          "meaning": "ncit:C49481",
          "comments": []
        },
        "Esophagus": {
          "meaning": "ncit:C12389",
          "comments": []
        },
        "Fallopian Tube": {
          "meaning": "ncit:C12403",
          "comments": []
        },
        "Frontal Lobe": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Gingiva, Lower, Anterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Lower, Posterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, NOS": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Upper, Anterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Gingiva, Upper, Posterior": {
          "meaning": "ncit:C32677",
          "comments": []
        },
        "Glottis": {
          "meaning": "ncit:C12724",
          "comments": []
        },
        "Hand Skin": {
          "meaning": "ncit:C52753",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "ncit:C12246",
          "comments": []
        },
        "Intestine": {
          "meaning": "ncit:C12736",
          "comments": []
        },
        "Larynx": {
          "meaning": "ncit:C12420",
          "comments": []
        },
        "Leg Skin": {
          "meaning": "ncit:C52749",
          "comments": []
        },
        "Lip": {
          "meaning": "ncit:C12220",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Lumbar Spinal Cord": {
          "meaning": "ncit:C12895",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
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
        "Nasal Cavity": {
          "meaning": "ncit:C12424",
          "comments": []
        },
        "Nasal Cavity and Paranasal Sinuses": {
          "meaning": "ncit:C12763",
          "comments": []
        },
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        },
        "Neck Skin": {
          "meaning": "ncit:C52756",
          "comments": []
        },
        "Occipital Lobe": {
          "meaning": "ncit:C12355",
          "comments": []
        },
        "Oral Cavity": {
          "meaning": "ncit:C12421",
          "comments": []
        },
        "Oropharynx": {
          "meaning": "ncit:C12762",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Palate": {
          "meaning": "ncit:C12229",
          "comments": []
        },
        "Parietal Lobe": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Penis": {
          "meaning": "ncit:C12409",
          "comments": []
        },
        "Pharynx": {
          "meaning": "ncit:C12425",
          "comments": []
        },
        "Pons": {
          "meaning": "ncit:C12511",
          "comments": []
        },
        "Pyriform Sinus": {
          "meaning": "ncit:C33439",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Scalp": {
          "meaning": "ncit:C89807",
          "comments": []
        },
        "Skin of the Back": {
          "meaning": "ncit:C142318",
          "comments": []
        },
        "Skin of the Chest": {
          "meaning": "ncit:C161379",
          "comments": []
        },
        "Skin of the Face": {
          "meaning": "ncit:C33561",
          "comments": []
        },
        "Skin of the Lip": {
          "meaning": "ncit:C12291",
          "comments": []
        },
        "Skin of the Upper Limb and Shoulder": {
          "meaning": "ncit:C12296",
          "comments": []
        },
        "Skin, NOS": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Stomach": {
          "meaning": "ncit:C12391",
          "comments": []
        },
        "Submandibular": {
          "meaning": "ncit:C129462",
          "comments": []
        },
        "Temporal Lobe": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Thoracic Spinal Cord": {
          "meaning": "ncit:C12894",
          "comments": []
        },
        "Tongue": {
          "meaning": "ncit:C12422",
          "comments": []
        },
        "Uterus": {
          "meaning": "ncit:C12405",
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
        "MX": {
          "meaning": "ncit:C48704",
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
        },
        "lb": {
          "meaning": "",
          "comments": []
        },
        "inch": {
          "meaning": "",
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
        "Bone Marrow Failure Complications": {
          "meaning": "",
          "comments": []
        },
        "Cancer Progression, NOS": {
          "meaning": "ncit:C19987",
          "comments": []
        },
        "Cardiac Disease": {
          "meaning": "ncit:C3079",
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
        "Immunotherapy-Related": {
          "meaning": "ncit:C168874",
          "comments": []
        },
        "Infection, NOS": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Infection, Not Otherwise Specified": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Kidney Failure": {
          "meaning": "ncit:C4376",
          "comments": []
        },
        "Liver Failure": {
          "meaning": "ncit:C26922",
          "comments": []
        },
        "Multi-Organ Failure": {
          "meaning": "ncit:C75568",
          "comments": []
        },
        "Organ Failure, NOS": {
          "meaning": "ncit:C185320",
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
        "Surgical Complication": {
          "meaning": "ncit:C164157",
          "comments": []
        },
        "Unacceptable Toxicity": {
          "meaning": "ncit:C199267",
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
    "SourceLabEnum": {
      "permissible_values": {
        "Cincinnati Children's Hospital Medical Center": {
          "meaning": "",
          "comments": []
        },
        "Dana-Farber Cancer Institute": {
          "meaning": "",
          "comments": []
        },
        "GeneDX": {
          "meaning": "",
          "comments": []
        },
        "Invitae": {
          "meaning": "",
          "comments": []
        },
        "Julius-Maximilians-Universit\u00e4t of W\u00fcrzburg": {
          "meaning": "",
          "comments": []
        },
        "Laboratorio de Citogen\u00e9tica, Instituto Nacional de Pediatr\u00eda, M\u00e9xico": {
          "meaning": "",
          "comments": []
        },
        "Prevention Genetics": {
          "meaning": "",
          "comments": []
        },
        "Quest Diagnostics": {
          "meaning": "",
          "comments": []
        },
        "Stanford University": {
          "meaning": "",
          "comments": []
        },
        "The Rockefeller University": {
          "meaning": "",
          "comments": []
        },
        "University of Chicago": {
          "meaning": "",
          "comments": []
        },
        "University of Minnesota": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
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
        "Unknown": {
          "meaning": "ncit:C17998",
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
        "Acetylcysteine": {
          "meaning": "ncit:C200",
          "comments": []
        },
        "Adalimumab": {
          "meaning": "ncit:C65216",
          "comments": []
        },
        "Alemtuzumab (Campath)": {
          "meaning": "",
          "comments": []
        },
        "Alpelisib": {
          "meaning": "ncit:C94214",
          "comments": []
        },
        "Amsacrine": {
          "meaning": "ncit:C240",
          "comments": []
        },
        "Anakinra": {
          "meaning": "ncit:C38717",
          "comments": []
        },
        "Anastrozole": {
          "meaning": "ncit;C1607",
          "comments": []
        },
        "Anti-thymocyte Globulin": {
          "meaning": "ncit:C278",
          "comments": []
        },
        "Aspirin": {
          "meaning": "ncit:C287",
          "comments": []
        },
        "Bilnatumomab": {
          "meaning": "ncit:",
          "comments": []
        },
        "Brentuximab Vedotin": {
          "meaning": "ncit:C66944",
          "comments": []
        },
        "Briquilimab": {
          "meaning": "",
          "comments": []
        },
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Capivasertib": {
          "meaning": "ncit:C102564",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Cetuximab": {
          "meaning": "rxcui:318341",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Cladribine": {
          "meaning": "ncit:C1336",
          "comments": []
        },
        "Clofarabine": {
          "meaning": "ncit:C26638",
          "comments": []
        },
        "Cyclophosphamide": {
          "meaning": "rxcui:3002",
          "comments": []
        },
        "Cytarabine": {
          "meaning": "rxcui:3041",
          "comments": []
        },
        "DTaP (Diphtheria and tetanus)": {
          "meaning": "ncit:C91718",
          "comments": []
        },
        "Danazol": {
          "meaning": "ncit:C414",
          "comments": []
        },
        "Daunorubicin": {
          "meaning": "rxcui:3109",
          "comments": []
        },
        "Daunorubicin (Liposomal)": {
          "meaning": "ncit:C2213",
          "comments": []
        },
        "Daunorubicin and Cytarabine (Liposomal)": {
          "meaning": "ncit:C67504",
          "comments": []
        },
        "Dexamethasone": {
          "meaning": "ncit:C422",
          "comments": []
        },
        "Dexrazoxane": {
          "meaning": "ncit:C1333",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention"
          ]
        },
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
          "comments": []
        },
        "Elacestrant": {
          "meaning": "rxcui:2628483",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Exemestane": {
          "meaning": "ncit:C1097",
          "comments": []
        },
        "Fludarabine": {
          "meaning": "ncit:C1094",
          "comments": []
        },
        "Fulvestrant": {
          "meaning": "ncit:C1379",
          "comments": []
        },
        "GCSF": {
          "meaning": "ncit:C26078",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Gemtuzumab Ozogamicin": {
          "meaning": "ncit:C1806",
          "comments": []
        },
        "Gilteritinib": {
          "meaning": "ncit:C116722",
          "comments": []
        },
        "Golimumab": {
          "meaning": "",
          "comments": []
        },
        "HER2 Inhibitor": {
          "meaning": "ncit:C159156",
          "comments": []
        },
        "HepA (Hepatitis A)": {
          "meaning": "ncit:C29090",
          "comments": []
        },
        "HepB (Hepatitis B)": {
          "meaning": "ncit:C29091",
          "comments": []
        },
        "HiB (Haemophilus influenza type B)": {
          "meaning": "ncit:C1126",
          "comments": []
        },
        "Human Papilloma Virus Vaccine": {
          "meaning": "ncit:C1951",
          "comments": []
        },
        "Hydrocortisone Sodium Succinate": {
          "meaning": "ncit:C1819",
          "comments": []
        },
        "IPV (Poliovirus)": {
          "meaning": "ncit:C91715",
          "comments": []
        },
        "Idarubicin": {
          "meaning": "rxcui:5650",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "rxcui:5657",
          "comments": []
        },
        "Influenza": {
          "meaning": "ncit:C178427",
          "comments": []
        },
        "Inotuzumab Ozogamicin": {
          "meaning": "ncit:C71542",
          "comments": []
        },
        "Intravenous Immunoglobulin Therapy": {
          "meaning": "ncit:C121331",
          "comments": []
        },
        "Lapatinib": {
          "meaning": "ncit:C26653",
          "comments": []
        },
        "Letrozole": {
          "meaning": "rxcui:72965",
          "comments": []
        },
        "MCV4 (Meningococcal)": {
          "meaning": "ncit:C96397",
          "comments": []
        },
        "MMR (Measles, Mumps, & Rubella)": {
          "meaning": "ncit:C96403",
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
        "Methylprednisolone": {
          "meaning": "ncit:C166880",
          "comments": [
            "(fa) ConsortiumNote: Also known as IVMP"
          ]
        },
        "Midostaurin": {
          "meaning": "ncit:C1872",
          "comments": []
        },
        "Monoclonal Antibody": {
          "meaning": "ncit:C20401",
          "comments": []
        },
        "Mycophenolate Mofetil": {
          "meaning": "",
          "comments": []
        },
        "Neratinib": {
          "meaning": "ncit:C49094",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Olaparib": {
          "meaning": "rxcui:1597582",
          "comments": []
        },
        "PCV (Pneumococcal)": {
          "meaning": "ncit:C97123",
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
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
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
        "Progestogen": {
          "meaning": "ncit:C2296",
          "comments": []
        },
        "RV (Rotavirus)": {
          "meaning": "ncit:C96394",
          "comments": []
        },
        "Ribociclib": {
          "meaning": "rxcui:1873986",
          "comments": []
        },
        "Rituximab": {
          "meaning": "rxcui:121191",
          "comments": []
        },
        "Sacituzumab Govitecan": {
          "meaning": "rxcui:2360537",
          "comments": []
        },
        "Sirolimus": {
          "meaning": "rxcui:35302",
          "comments": []
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
        "Talazoparib": {
          "meaning": "rxcui:2099949",
          "comments": []
        },
        "Tamoxifen": {
          "meaning": "rxcui:10324",
          "comments": []
        },
        "Tdap (Tetanus, diphtheria, & acellular pertussis)": {
          "meaning": "ncit:C91717",
          "comments": []
        },
        "Therapuetic Growth Hormone": {
          "meaning": "ncit:C164163",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "rxcui:10473",
          "comments": []
        },
        "Thyroxine": {
          "meaning": "ncit:C2302",
          "comments": []
        },
        "Tisotumab Vedotin": {
          "meaning": "ncit:C113164",
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
        "Trastuzumab": {
          "meaning": "rxcui:224905",
          "comments": []
        },
        "Trastuzumab Deruxtecan": {
          "meaning": "ncit:C128799",
          "comments": []
        },
        "Trastuzumab Emtansine": {
          "meaning": "ncit:C82492",
          "comments": []
        },
        "Tretinoin": {
          "meaning": "ncit:C900",
          "comments": []
        },
        "Triiodothyronine": {
          "meaning": "ncit:C2303",
          "comments": []
        },
        "Tucatinib": {
          "meaning": "ncit:C77896",
          "comments": []
        },
        "VAR (Varicella)": {
          "meaning": "ncit:C77799",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
          "comments": []
        },
        "ZOS (Zoster/Shingles)": {
          "meaning": "ncit:C71079",
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
        "FRIENDS": {
          "meaning": "",
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
        "Benign": {
          "meaning": "ncit:C14172",
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
        "ALT": {
          "meaning": "ncit:C64433",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "ANA": {
          "meaning": "ncit:C176313",
          "comments": []
        },
        "AQP4 Ab": {
          "meaning": "",
          "comments": []
        },
        "AST": {
          "meaning": "ncit:C64467",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "Absolute B Lymphocyte Count": {
          "meaning": "ncit:C201188",
          "comments": [
            "(fa) ConsortiumNote: METHOD = 'Flow Cytometry'"
          ]
        },
        "Absolute Basophil Count": {
          "meaning": "ncit:C64470",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Absolute Blood Lymphocyte Count": {
          "meaning": "ncit:C113237",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Absolute Eosinophil Count": {
          "meaning": "ncit:C188680",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Absolute Monocyte Count": {
          "meaning": "ncit:C181278",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Alkaline Phophatase": {
          "meaning": "ncit:C64432",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "Angiotension Converting Enzyme": {
          "meaning": "ncit:C80169",
          "comments": []
        },
        "Autoantibodies, NOS": {
          "meaning": "ncit:C181397",
          "comments": []
        },
        "Basophils": {
          "meaning": "ncit:C64470",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Blast Count": {
          "meaning": "ncit:C74605",
          "comments": [
            "(fa) ConsortiumNote: CBC or Bone Marrow"
          ]
        },
        "Blood Urea Nitrogen": {
          "meaning": "ncit:C61019",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "CD19+ B Cells": {
          "meaning": "ncit:C201193",
          "comments": []
        },
        "CD3+ T Cells": {
          "meaning": "ncit:C201180",
          "comments": []
        },
        "CD4+ T Cells": {
          "meaning": "ncit:C201182",
          "comments": []
        },
        "CD8+ T Cells": {
          "meaning": "ncit:C201184",
          "comments": []
        },
        "CRP": {
          "meaning": "ncit:C64548",
          "comments": []
        },
        "CSF Luekocyte Count": {
          "meaning": "ncit:C168921",
          "comments": [
            "(fa) ConsortiumNote: CSF Studies"
          ]
        },
        "CSF RBC Count": {
          "meaning": "ncit:C168920",
          "comments": [
            "(fa) ConsortiumNote: CSF Studies"
          ]
        },
        "Cellularity": {
          "meaning": "ncit:C111153",
          "comments": []
        },
        "Chromosome Breakage, DEB": {
          "meaning": "",
          "comments": []
        },
        "Chromosome Breakage, DEB/MMC": {
          "meaning": "",
          "comments": []
        },
        "Chromosome Breakage, MMC": {
          "meaning": "",
          "comments": []
        },
        "Chromosome Breakage, Treated (unknown agent)": {
          "meaning": "",
          "comments": []
        },
        "Chromosome Breakage, Untreated": {
          "meaning": "",
          "comments": []
        },
        "Creatinine": {
          "meaning": "ncit:C64547",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "Dysplasia": {
          "meaning": "ncit:C204680",
          "comments": []
        },
        "ESR": {
          "meaning": "ncit:C74611",
          "comments": []
        },
        "Eosinophils": {
          "meaning": "ncit:C64550",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Erythroid Precursors Count": {
          "meaning": "ncit:C187802",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Glucose": {
          "meaning": "ncit:C105585",
          "comments": [
            "(fa) ConsortiumNote: Basic Metabolic Panel"
          ]
        },
        "Granulomas": {
          "meaning": "ncit:C176334",
          "comments": []
        },
        "HIV-1 Ab": {
          "meaning": "",
          "comments": []
        },
        "Hematocrit Measurement": {
          "meaning": "ncit:C64796",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
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
        "Histiocytes": {
          "meaning": "ncit:C12563",
          "comments": []
        },
        "IgA": {
          "meaning": "ncit:C198278",
          "comments": []
        },
        "IgD": {
          "meaning": "",
          "comments": []
        },
        "IgE": {
          "meaning": "",
          "comments": []
        },
        "IgG": {
          "meaning": "ncit:C198279",
          "comments": []
        },
        "IgG1": {
          "meaning": "ncit:C204624",
          "comments": []
        },
        "IgG2": {
          "meaning": "ncit:C204625",
          "comments": []
        },
        "IgG3": {
          "meaning": "ncit:C204626",
          "comments": []
        },
        "IgG4": {
          "meaning": "",
          "comments": []
        },
        "IgM": {
          "meaning": "ncit:C198280",
          "comments": []
        },
        "Immature Granulocytes": {
          "meaning": "ncit:C100445",
          "comments": [
            "(fa) ConsortiumNote: CBC with Differential"
          ]
        },
        "Infectious Diseases, NOS": {
          "meaning": "ncit:C26726",
          "comments": []
        },
        "JCV": {
          "meaning": "ncit:C199960",
          "comments": []
        },
        "Kappa to Lambda Ratio": {
          "meaning": "ncit:C161351",
          "comments": [
            "(fa) ConsortiumNote: METHOD = 'Flow Cytometry'"
          ]
        },
        "LDL": {
          "meaning": "ncit:C189506",
          "comments": [
            "(fa) ConsortiumNote: Lipid Testing"
          ]
        },
        "Lactage Dehydrogenase": {
          "meaning": "ncit:C64855",
          "comments": []
        },
        "Leukocyte Count": {
          "meaning": "ncit:C51948",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Lymphoid Aggregates": {
          "meaning": "ncit:C187947",
          "comments": []
        },
        "MCH": {
          "meaning": "ncit:C64797",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "MCHC": {
          "meaning": "ncit:C64798",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "MCV": {
          "meaning": "ncit:C64799",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Mast Cell Count": {
          "meaning": "ncit:C111246",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Megakaryocytes Count": {
          "meaning": "ncit:C96688",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Monocyte Count": {
          "meaning": "ncit:C64823",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Myeloblast Count": {
          "meaning": "ncit:C74632",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Myelocyte Count": {
          "meaning": "ncit:C74662",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Myeloid Cell Count": {
          "meaning": "ncit:C184425",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Myeloid to Erythroid Ratio Measurement": {
          "meaning": "ncit:C92242",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Natural Killer Cells to Lymphocytes Ratio Measurement": {
          "meaning": "ncit:C181258",
          "comments": [
            "(fa) ConsortiumNote: METHOD = 'Flow Cytometry'"
          ]
        },
        "Neutrophil Band Form Count": {
          "meaning": "ncit:C64830",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Neutrophil Count": {
          "meaning": "ncit:C51950",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Oligoclonal Bands": {
          "meaning": "ncit:C122139",
          "comments": [
            "(fa) ConsortiumNote: CSF Studies"
          ]
        },
        "Opening Pressure": {
          "meaning": "ncit:C180559",
          "comments": [
            "(fa) ConsortiumNote: CSF Studies"
          ]
        },
        "Plasma Cells": {
          "meaning": "ncit:C128974",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Promyelocyte Count": {
          "meaning": "ncit:C74622",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
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
        "Reticulocyte Count": {
          "meaning": "ncit:C51947",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Reticulocyte Mean Corpuscular Volume": {
          "meaning": "ncitC114215",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Retinal Nerve Fiber Layer Thickness": {
          "meaning": "",
          "comments": []
        },
        "Ringed Sideroblasts": {
          "meaning": "ncit:C100419",
          "comments": [
            "(fa) ConsortiumNote: SPECIMEN = 'Bone Marrow'"
          ]
        },
        "Segmented Neutrophils": {
          "meaning": "ncit:C81997",
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
        "Total Cholesterol": {
          "meaning": "ncit:C61032",
          "comments": [
            "(fa) ConsortiumNote: Lipid Testing"
          ]
        },
        "Triglyceride Measurement": {
          "meaning": "ncit:C64812",
          "comments": [
            "(fa) ConsortiumNote: Lipid Testing"
          ]
        },
        "Vitamin D 25": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TmpProductEnum": {
      "permissible_values": {
        "Plasma": {
          "meaning": "ncit:C13356",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C133278",
          "comments": []
        },
        "RBC": {
          "meaning": "ncit:C133280",
          "comments": []
        },
        "Whole Blood": {
          "meaning": "ncit:C41067",
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
    "FansSymptomAcuityEnum": {
      "permissible_values": {
        "Acute": {
          "meaning": "",
          "comments": []
        },
        "Chronic": {
          "meaning": "",
          "comments": []
        },
        "Hyperacute": {
          "meaning": "",
          "comments": []
        },
        "Subacute": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ClinicalFindingEnum": {
      "permissible_values": {
        "Abdominal pain": {
          "meaning": "",
          "comments": []
        },
        "Abnormal Anus Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Anal Anomaly"
          ]
        },
        "Abnormal Duodenal Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Abnormal Esophagus Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Abnormal Heart Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Abnormal Heart Valve Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Abnormal Morphology of the Thumb": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Abnormal Renal Morphology NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Abnormal Speech": {
          "meaning": "ncit:C5041",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Abnormal Thumb Morphology": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Abnormal Uterine Bleeding": {
          "meaning": "",
          "comments": []
        },
        "Abnormal corpus callosum morphology": {
          "meaning": "",
          "comments": []
        },
        "Abnormal fallopian tube morphology NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormal female external genitalia morphology": {
          "meaning": "",
          "comments": []
        },
        "Abnormal malleus morphology": {
          "meaning": "",
          "comments": []
        },
        "Abnormal nervous system morphology NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormal oral mucosa morphology NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormal pinna morhology (Microtia, poliotia, abnormal helix, etc)": {
          "meaning": "",
          "comments": []
        },
        "Abnormal size of the palpebral fissures": {
          "meaning": "",
          "comments": []
        },
        "Abnormal tympanic membrane morphology (no hay HP para \"small\")": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of skin pigmentation": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of the Upper Limb NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Abnormality of the Ureter NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Abnormality of the Vertebral Column NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Vertebral Anomaly"
          ]
        },
        "Abnormality of the dentition NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of the ear NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of the eye NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of the female genitalia NOS": {
          "meaning": "",
          "comments": []
        },
        "Abnormality of the male genitalia NOS": {
          "meaning": "",
          "comments": []
        },
        "Absent Radius": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Absent Thumb": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Absent testes": {
          "meaning": "",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia Susceptibility - PAX5": {
          "meaning": "ncit:C176907",
          "comments": []
        },
        "Anal Atresia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Anal Anomaly"
          ]
        },
        "Anal Fistula": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Anal Anomaly"
          ]
        },
        "Anal Stenosis": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Anal Anomaly"
          ]
        },
        "Aplasia of the ovary": {
          "meaning": "",
          "comments": []
        },
        "Aplasia uterus": {
          "meaning": "",
          "comments": []
        },
        "Aspiration": {
          "meaning": "",
          "comments": []
        },
        "Ataxia": {
          "meaning": "ncit:C26702",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Atresia of the external auditory canal": {
          "meaning": "",
          "comments": []
        },
        "Atrial Septal Defect": {
          "meaning": "ncit:C84473",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Attentions Deficit Hyperactivity Disorder": {
          "meaning": "",
          "comments": []
        },
        "Back Pain": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Behavioral/Cognitive Changes": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Birth length less than 3rd percentile": {
          "meaning": "",
          "comments": []
        },
        "Bleeding, NOS": {
          "meaning": "",
          "comments": []
        },
        "Blurry Vision/Loss of Vision": {
          "meaning": "ncit:C50602",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Bruising": {
          "meaning": "",
          "comments": []
        },
        "Cataracts": {
          "meaning": "",
          "comments": []
        },
        "Central nervous system cysts": {
          "meaning": "",
          "comments": []
        },
        "Cerebellar hypoplasia (vermis, olivo-ponto and hemisphere cerebellar hypoplasia)": {
          "meaning": "",
          "comments": []
        },
        "Cerebral hypoplasia": {
          "meaning": "",
          "comments": []
        },
        "Chest pain": {
          "meaning": "",
          "comments": []
        },
        "Choking": {
          "meaning": "",
          "comments": []
        },
        "Cleft Palate": {
          "meaning": "",
          "comments": []
        },
        "Coarctation of Aorta": {
          "meaning": "ncit:C84567",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Complex Migraine": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Cortical Signs": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Coughing": {
          "meaning": "",
          "comments": []
        },
        "Cranial Mono-neuropathy": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Craniosynostosis": {
          "meaning": "ncit:C84655",
          "comments": [
            "(fa) ConsortiumNote: PHENOS Feature"
          ]
        },
        "Crossed Fused Renal Ectopia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Cryptorchidism": {
          "meaning": "",
          "comments": []
        },
        "Decreased testicular size": {
          "meaning": "",
          "comments": []
        },
        "Difficulty Breathing": {
          "meaning": "",
          "comments": []
        },
        "Difficulty Swallowing": {
          "meaning": "",
          "comments": []
        },
        "Double Vision": {
          "meaning": "ncit:C37941",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Duodenal Atresia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Duodenal Stenosis": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Duodenal Web": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Dysdiadochokinesia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Dysphagia": {
          "meaning": "",
          "comments": []
        },
        "Dysplastic Kidney": {
          "meaning": "ncit:C123031",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Earache": {
          "meaning": "",
          "comments": []
        },
        "Ectopic Anus": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Anal Anomaly"
          ]
        },
        "Ectopic Kidney": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Encephalopathy": {
          "meaning": "ncit:C26920",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Encephalopathy, Focal Numbness": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Encephalopathy, Focal Weakness": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Epicanthal folds (epicanthus)": {
          "meaning": "",
          "comments": []
        },
        "Erectile Dysfunction": {
          "meaning": "ncit:C3133",
          "comments": []
        },
        "Erythroplakia": {
          "meaning": "ncit:C3025",
          "comments": []
        },
        "Esophageal Atresia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Esophageal Stenosis": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Esophageal Web": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Esophageal Duodenal Atresia"
          ]
        },
        "Eye Movement Abnormalities": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Fatigue": {
          "meaning": "ncit:C3036",
          "comments": []
        },
        "Feeling of lump in throat": {
          "meaning": "",
          "comments": []
        },
        "Fevers": {
          "meaning": "",
          "comments": []
        },
        "Focal Weakness, NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Gagging": {
          "meaning": "",
          "comments": []
        },
        "Generalized hyperpigmentation": {
          "meaning": "",
          "comments": []
        },
        "Glaucoma": {
          "meaning": "",
          "comments": []
        },
        "Halitosis": {
          "meaning": "",
          "comments": []
        },
        "Headache": {
          "meaning": "ncit:C34661",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis",
            "(fa)  ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Hearing impairment": {
          "meaning": "",
          "comments": []
        },
        "Hematemesis": {
          "meaning": "ncit:C37964",
          "comments": []
        },
        "Hepatomegaly": {
          "meaning": "",
          "comments": []
        },
        "Hoarseness": {
          "meaning": "",
          "comments": []
        },
        "Horseshoe Kidney": {
          "meaning": "ncit:C98947",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Human Papillomavirus Infection": {
          "meaning": "ncit:C27851",
          "comments": []
        },
        "Human immunodeficiency virus [HIV] disease": {
          "meaning": "icd10:B20",
          "comments": []
        },
        "Hydrocephalus": {
          "meaning": "ncit:C3111",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Hydronephrosis": {
          "meaning": "ncit:C26796",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Hydroureter": {
          "meaning": "ncit:C26927",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Hyperpigmented freckle like macules/acanthomas in flexural areas": {
          "meaning": "",
          "comments": []
        },
        "Hyperpigmented macules (hypermelanotic macule)": {
          "meaning": "",
          "comments": []
        },
        "Hyperreflexia": {
          "meaning": "ncit:C43248",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Hypertension": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Medical HIstory"
          ]
        },
        "Hypopigmented macules": {
          "meaning": "",
          "comments": []
        },
        "Hypoplasia of penis": {
          "meaning": "",
          "comments": []
        },
        "Hypoplasia of the Radius": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Hypoplasia of the ovary": {
          "meaning": "",
          "comments": []
        },
        "Hypoplasia of the uterus": {
          "meaning": "",
          "comments": []
        },
        "Hypoplastic Thenar Eminence": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Hypospadias": {
          "meaning": "",
          "comments": []
        },
        "Hypotelorism": {
          "meaning": "",
          "comments": []
        },
        "Imbalance": {
          "meaning": "ncit:C200084",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Impaired Consciousness": {
          "meaning": "ncit:C121627",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Incontinence": {
          "meaning": "ncit:C3429",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Increased Intracranial Pressure": {
          "meaning": "ncit:C187268",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Intellectual disability": {
          "meaning": "",
          "comments": []
        },
        "Intrauterine Growth Restriction": {
          "meaning": "ncit:C87088",
          "comments": [
            "(fa) ConsortiumNote: Birth History"
          ]
        },
        "Itching": {
          "meaning": "",
          "comments": []
        },
        "Jaw pain": {
          "meaning": "",
          "comments": []
        },
        "Leukopenia": {
          "meaning": "ncit:C26816",
          "comments": []
        },
        "Leukoplakia": {
          "meaning": "ncit:C3186",
          "comments": []
        },
        "Lichen Planus": {
          "meaning": "",
          "comments": []
        },
        "Limb Pain": {
          "meaning": "",
          "comments": []
        },
        "Limbal neovascularization": {
          "meaning": "",
          "comments": []
        },
        "Liver abnormalities": {
          "meaning": "",
          "comments": []
        },
        "Liver adenomas": {
          "meaning": "",
          "comments": []
        },
        "Loss of smell": {
          "meaning": "",
          "comments": []
        },
        "Loss of taste": {
          "meaning": "",
          "comments": []
        },
        "Low set ears": {
          "meaning": "",
          "comments": []
        },
        "Melena/Black Stool": {
          "meaning": "ncit:C86571",
          "comments": []
        },
        "Meningismus": {
          "meaning": "ncit:C79694",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Microcornea": {
          "meaning": "",
          "comments": []
        },
        "Microdontia": {
          "meaning": "",
          "comments": []
        },
        "Microphtalmia": {
          "meaning": "",
          "comments": []
        },
        "Migraine": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Multiple Cranial Neuropathies": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Myelopathy, Focal Numbness": {
          "meaning": "ncit:C34857",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Myelopathy, Focal Weakness": {
          "meaning": "ncit:C182336",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Narrow internal auditory canal": {
          "meaning": "",
          "comments": []
        },
        "Nausea": {
          "meaning": "",
          "comments": []
        },
        "Neck Pain": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Neural Tube Defects": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Vertebral Anomaly"
          ]
        },
        "Neurogenic Bladder/Bowel": {
          "meaning": "ncit:C79696",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Neuropathy": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Night sweats": {
          "meaning": "",
          "comments": []
        },
        "Numbness, NOS": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Optic nerve hypoplasia": {
          "meaning": "",
          "comments": []
        },
        "Oral Bacterial Infection": {
          "meaning": "",
          "comments": []
        },
        "Oral Fungal Infection": {
          "meaning": "",
          "comments": []
        },
        "Oral Viral Infection": {
          "meaning": "",
          "comments": []
        },
        "Pain, NOS": {
          "meaning": "",
          "comments": []
        },
        "Paresthesia": {
          "meaning": "ncit:C28177",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis",
            "(fa)  ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Partial Duplication of Thumb Phalanx": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Patent Ductus Arteriosus": {
          "meaning": "ncit:C84492",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Patent Foramen Ovale": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Pelvic Pain": {
          "meaning": "",
          "comments": []
        },
        "Petechiae": {
          "meaning": "",
          "comments": []
        },
        "Positive Visual Phenomenon": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Symptoms History"
          ]
        },
        "Postcoital Bleeding": {
          "meaning": "",
          "comments": []
        },
        "Postmenopausal Bleeding": {
          "meaning": "",
          "comments": []
        },
        "Preaxial Hand Polydactyly": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Premalignant lesion / dysplasia": {
          "meaning": "",
          "comments": []
        },
        "Ptosis": {
          "meaning": "",
          "comments": []
        },
        "Recurrent Mouth Sores": {
          "meaning": "",
          "comments": []
        },
        "Reflux": {
          "meaning": "",
          "comments": []
        },
        "Renal Agenesis": {
          "meaning": "ncit:C101220",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Renal Cysts": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Renal Duplication": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Renal Hypoplasia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Renal Malrotation": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Retinopathy": {
          "meaning": "",
          "comments": []
        },
        "Scoliosis": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Vertebral Anomaly"
          ]
        },
        "Seizure": {
          "meaning": "ncit:C2962",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis",
            "(fa)  ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Sensorineural Hearing Loss": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Medical HIstory"
          ]
        },
        "Severe aplastic anemia": {
          "meaning": "",
          "comments": []
        },
        "Severe isolated lineage cytopenia: platelet": {
          "meaning": "",
          "comments": []
        },
        "Severe isolated lineage cytopenia: red cell": {
          "meaning": "",
          "comments": []
        },
        "Severe isolated lineage cytopenia: white cell": {
          "meaning": "",
          "comments": []
        },
        "Short Thumb": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Short stature NOS": {
          "meaning": "",
          "comments": []
        },
        "Situs Inversus": {
          "meaning": "ncit:C87121",
          "comments": []
        },
        "Slurred Speech": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Small for Gestational Age": {
          "meaning": "ncit:C114934",
          "comments": [
            "(fa) ConsortiumNote: Birth History"
          ]
        },
        "Small pituitary gland": {
          "meaning": "",
          "comments": []
        },
        "Sore throat": {
          "meaning": "",
          "comments": []
        },
        "Spinal Level Myelopathy": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Neurological Exam/Phenotype"
          ]
        },
        "Stenosis of the external auditory canal": {
          "meaning": "",
          "comments": []
        },
        "Strabismus": {
          "meaning": "",
          "comments": []
        },
        "Subluxed Thumb": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Supernumerary tooth": {
          "meaning": "",
          "comments": []
        },
        "Swelling": {
          "meaning": "",
          "comments": []
        },
        "Systemic Lupus Erythematosus": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Medical HIstory"
          ]
        },
        "Tetralogy of Fallot": {
          "meaning": "ncit:C84505",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Thrombocytopenia": {
          "meaning": "ncit:C3408",
          "comments": []
        },
        "Tightness in chest": {
          "meaning": "",
          "comments": []
        },
        "Tooth agenesis": {
          "meaning": "",
          "comments": []
        },
        "Transient cytopenia": {
          "meaning": "",
          "comments": []
        },
        "Triphalangeal Thumb": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Upper Limb Anomaly"
          ]
        },
        "Truncus Arteriosus": {
          "meaning": "ncit:C98880",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Ureteral Agenesis": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Ureteral Duplication": {
          "meaning": "ncit:C98917",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Ureteral Hypoplasia": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Vaginal Discharge": {
          "meaning": "",
          "comments": []
        },
        "Ventricular Septal Defect": {
          "meaning": "ncit:C84506",
          "comments": [
            "(fa) ConsortiumNote: Cardiac Anomaly"
          ]
        },
        "Ventriculomegaly": {
          "meaning": "",
          "comments": []
        },
        "Vertebral Fusion": {
          "meaning": "",
          "comments": [
            "(fa) ConsortiumNote: Vertebral Anomaly"
          ]
        },
        "Vertigo": {
          "meaning": "ncit:C38057",
          "comments": [
            "(fa) ConsortiumNote: FANS Diagnosis"
          ]
        },
        "Vesicoureteral Reflux": {
          "meaning": "ncit:C84467",
          "comments": [
            "(fa) ConsortiumNote: Renal Anomaly"
          ]
        },
        "Voice Alteration": {
          "meaning": "",
          "comments": []
        },
        "Vomiting": {
          "meaning": "ncit:C3442",
          "comments": []
        },
        "Vulvar Pain": {
          "meaning": "",
          "comments": []
        },
        "Weight Loss": {
          "meaning": "",
          "comments": []
        },
        "Wheezing": {
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
    "TmpTypeEnum": {
      "permissible_values": {
        "Plasmapheresis": {
          "meaning": "ncit:C15304",
          "comments": []
        },
        "Simple Transfusion": {
          "meaning": "ncit:C173285",
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
    "ParentalStatusEnum": {
      "permissible_values": {
        "De Novo": {
          "meaning": "ncit:C93106",
          "comments": []
        },
        "Maternally Inherited": {
          "meaning": "",
          "comments": []
        },
        "Paternally Inherited": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
    "RouteEnum": {
      "permissible_values": {
        "Intraarterial": {
          "meaning": "ncit:C38222",
          "comments": []
        },
        "Intramuscular": {
          "meaning": "",
          "comments": []
        },
        "Intrathecal": {
          "meaning": "ncit:C173292",
          "comments": []
        },
        "Intravenously": {
          "meaning": "ncit:C38276",
          "comments": []
        },
        "Oral": {
          "meaning": "",
          "comments": []
        },
        "Subcutaneous": {
          "meaning": "",
          "comments": []
        },
        "Systemic": {
          "meaning": "ncit:C173291",
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
        "Ann Arbor >> Stage 1": {
          "meaning": "ncit:C8071",
          "comments": []
        },
        "Ann Arbor >> Stage 2": {
          "meaning": "ncit:C8116",
          "comments": []
        },
        "Ann Arbor >> Stage 3": {
          "meaning": "ncit:C8129",
          "comments": []
        },
        "Ann Arbor >> Stage 4": {
          "meaning": "ncit:C8142",
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
        "COG >> Stage 4S": {
          "meaning": "",
          "comments": []
        },
        "Evans >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "Evans >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "Evans >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "Evans >> Stage 4": {
          "meaning": "",
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
        "INRGSS >> Stage L1": {
          "meaning": "",
          "comments": []
        },
        "INRGSS >> Stage L2": {
          "meaning": "",
          "comments": []
        },
        "INRGSS >> Stage M": {
          "meaning": "",
          "comments": []
        },
        "INRGSS >> Stage Ms": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 2a": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 2b": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 4": {
          "meaning": "",
          "comments": []
        },
        "INSS >> Stage 4s": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 0": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 3a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 3b": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 4a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Stage 4b": {
          "meaning": "",
          "comments": []
        },
        "Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System >> Group 1": {
          "meaning": "C148012",
          "comments": []
        },
        "Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System >> Group 2": {
          "meaning": "C148015",
          "comments": []
        },
        "Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System >> Stage 3": {
          "meaning": "C148019",
          "comments": []
        },
        "Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System >> Stage 4": {
          "meaning": "C148022",
          "comments": []
        },
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
        },
        "System NOS >> Localized": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Metastatic": {
          "meaning": "",
          "comments": []
        },
        "System NOS >> Regionally Advanced": {
          "meaning": "",
          "comments": []
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
    "FounderPopulationEnum": {
      "permissible_values": {
        "Ammish/Mennonite/Hutterite": {
          "meaning": "",
          "comments": []
        },
        "Brazilian": {
          "meaning": "",
          "comments": []
        },
        "Dutch": {
          "meaning": "",
          "comments": []
        },
        "French Canadian": {
          "meaning": "",
          "comments": []
        },
        "Gypsy": {
          "meaning": "",
          "comments": []
        },
        "Indian": {
          "meaning": "",
          "comments": []
        },
        "Jewish (Ashkenazi)": {
          "meaning": "",
          "comments": []
        },
        "Mixe": {
          "meaning": "",
          "comments": []
        },
        "South Asian": {
          "meaning": "",
          "comments": []
        },
        "South African": {
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
    "RelationEnum": {
      "permissible_values": {
        "Aunt": {
          "meaning": "",
          "comments": []
        },
        "Brother": {
          "meaning": "ncit:C96570",
          "comments": []
        },
        "Cousin": {
          "meaning": "",
          "comments": []
        },
        "Daughter": {
          "meaning": "ncit:C150887",
          "comments": []
        },
        "Father": {
          "meaning": "ncit:C96572",
          "comments": []
        },
        "Mother": {
          "meaning": "ncit:C96580",
          "comments": []
        },
        "Second degree relative, NOS": {
          "meaning": "",
          "comments": []
        },
        "Sister": {
          "meaning": "ncit:C96586",
          "comments": []
        },
        "Son": {
          "meaning": "ncit:C150888",
          "comments": []
        },
        "Uncle": {
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
        },
        "PubMed": {
          "meaning": "",
          "comments": []
        },
        "dbsnp": {
          "meaning": "",
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
        }
      }
    },
    "ConditioningTypeEnum": {
      "permissible_values": {
        "Antibody Conditioning": {
          "meaning": "",
          "comments": []
        },
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
        "Haploidentical": {
          "meaning": "",
          "comments": []
        },
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
    "DysplasiaEnum": {
      "permissible_values": {
        "Mild": {
          "meaning": "ncit:C8362",
          "comments": []
        },
        "Moderate": {
          "meaning": "ncit:C8363",
          "comments": []
        },
        "Severe": {
          "meaning": "ncit:C8364",
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
    "BreakageSourceLabEnum": {
      "permissible_values": {
        "ARUP": {
          "meaning": "",
          "comments": []
        },
        "Cincinnati Children's Hospital Medical Center": {
          "meaning": "",
          "comments": []
        },
        "Dana-Farber Cancer Institute": {
          "meaning": "ncit:C177330",
          "comments": []
        },
        "Julius-Maximilians-Universit\u00e4t of W\u00fcrzburg": {
          "meaning": "",
          "comments": []
        },
        "Laboratorio de Citogen\u00e9tica, Instituto Nacional de Pediatr\u00eda, M\u00e9xico": {
          "meaning": "",
          "comments": []
        },
        "OHSU": {
          "meaning": "",
          "comments": []
        },
        "Quest Diagnostics": {
          "meaning": "",
          "comments": []
        },
        "Stanford University": {
          "meaning": "",
          "comments": []
        },
        "The Rockefeller University": {
          "meaning": "",
          "comments": []
        },
        "University of Chicago": {
          "meaning": "",
          "comments": []
        },
        "University of Minnesota": {
          "meaning": "",
          "comments": []
        },
        "Other": {
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
    "FunctionalMeasurementResultUnitEnum": {
      "permissible_values": {
        "ms": {
          "meaning": "ncit:C41140",
          "comments": []
        },
        "micrometer": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OutcomeEnum": {
      "permissible_values": {
        "Adequate for Analysis": {
          "meaning": "",
          "comments": []
        },
        "Hemodiluated": {
          "meaning": "",
          "comments": []
        },
        "Inadequate for Analysis": {
          "meaning": "",
          "comments": []
        },
        "Indeterminate": {
          "meaning": "ncit:C48658",
          "comments": []
        },
        "Non-Viable Tumor": {
          "meaning": "",
          "comments": []
        },
        "Small Amount": {
          "meaning": "",
          "comments": []
        },
        "Viable Tumor": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
    "AssessmentReasonEnum": {
      "permissible_values": {
        "Surveillance Assessment": {
          "meaning": "",
          "comments": []
        },
        "Symptomatic Assessment": {
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
    "ProcedureEnum": {
      "permissible_values": {
        "Anal Repair": {
          "meaning": "",
          "comments": []
        },
        "Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Appendectomy": {
          "meaning": "ncit:C51687",
          "comments": []
        },
        "Cardiac Repair": {
          "meaning": "",
          "comments": []
        },
        "Cervical Decompression": {
          "meaning": "",
          "comments": []
        },
        "Coloproctostomy": {
          "meaning": "",
          "comments": []
        },
        "Colostomy": {
          "meaning": "",
          "comments": []
        },
        "Colposcopy/Leep": {
          "meaning": "",
          "comments": []
        },
        "Conization": {
          "meaning": "",
          "comments": []
        },
        "Continent Ileostomy": {
          "meaning": "",
          "comments": []
        },
        "Creation of Ileal Reservoir (S or J)": {
          "meaning": "",
          "comments": []
        },
        "Creation of Mucofistula": {
          "meaning": "",
          "comments": []
        },
        "Debulking (radical dissection)": {
          "meaning": "",
          "comments": []
        },
        "Destruction of Lesion(s), extensive": {
          "meaning": "",
          "comments": []
        },
        "Destruction of Lesion(s), simple": {
          "meaning": "",
          "comments": []
        },
        "Diagnostic Laparoscopy": {
          "meaning": "",
          "comments": []
        },
        "Enterolysis": {
          "meaning": "",
          "comments": []
        },
        "Enterostomy": {
          "meaning": "",
          "comments": []
        },
        "Esophageal Repair": {
          "meaning": "",
          "comments": []
        },
        "Esophagogastrectomy": {
          "meaning": "",
          "comments": []
        },
        "Exploratory Laparotomy": {
          "meaning": "",
          "comments": []
        },
        "Extracorporeal Photopheresis": {
          "meaning": "",
          "comments": []
        },
        "Hartmann Type Procedure": {
          "meaning": "",
          "comments": []
        },
        "Hemiglossectomy": {
          "meaning": "",
          "comments": []
        },
        "Hemivulvectomy": {
          "meaning": "",
          "comments": []
        },
        "Ileocolostomy": {
          "meaning": "",
          "comments": []
        },
        "Ileostomy or Ileoproctostomy": {
          "meaning": "",
          "comments": []
        },
        "Inguinofemoral Lymphadenectomy": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Appendectomy": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Assisted Vaginal Hysterectomy": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Enterectomy": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Enterolysis": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopy with Aspiration of Cavity or Cyst": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Partial Colectomy Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopic Partial Colectomy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Laryngopharyngectomy": {
          "meaning": "",
          "comments": []
        },
        "Leep conization": {
          "meaning": "",
          "comments": []
        },
        "Level II-V Dissection": {
          "meaning": "",
          "comments": []
        },
        "Limited Para-aortic Lymphadenectomy": {
          "meaning": "",
          "comments": []
        },
        "Lobectomy": {
          "meaning": "",
          "comments": [
            "(ews) ConsortiumNote: Resection procedure (for metastatic disease).",
            "(os) ConsortiumNote: Resection procedure (for metastatic disease)."
          ]
        },
        "Lumbar Decompression": {
          "meaning": "",
          "comments": []
        },
        "Maxillectomy": {
          "meaning": "",
          "comments": []
        },
        "Neck Dissection": {
          "meaning": "",
          "comments": []
        },
        "Omentectomy": {
          "meaning": "",
          "comments": []
        },
        "Oophorectomy, NOS": {
          "meaning": "ncit:C15291",
          "comments": []
        },
        "Paratrachial Node Dissection": {
          "meaning": "",
          "comments": []
        },
        "Partial Colectomy with Anastomosis": {
          "meaning": "",
          "comments": []
        },
        "Partial Colectomy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Partial Glossectomy": {
          "meaning": "",
          "comments": []
        },
        "Partial Mandibulectomy": {
          "meaning": "",
          "comments": []
        },
        "Partial Pharyngectomy": {
          "meaning": "",
          "comments": []
        },
        "Para-aortic Lymph Node Sampling": {
          "meaning": "",
          "comments": []
        },
        "Pelvic Lymphadenectomy": {
          "meaning": "",
          "comments": []
        },
        "Pharingolaryngocervicalesophagectomy": {
          "meaning": "",
          "comments": []
        },
        "Pharyngectomy": {
          "meaning": "",
          "comments": []
        },
        "Pharyngotomy": {
          "meaning": "",
          "comments": []
        },
        "Proctectomy": {
          "meaning": "ncit:C15300",
          "comments": []
        },
        "Radical Cystoprostatectomy": {
          "meaning": "",
          "comments": []
        },
        "Radical Hysterectomy": {
          "meaning": "",
          "comments": []
        },
        "Radical Neck Dissection": {
          "meaning": "",
          "comments": []
        },
        "Radical Trachelectomy": {
          "meaning": "",
          "comments": []
        },
        "Removal of Paravaginal Tissue (radical)": {
          "meaning": "",
          "comments": []
        },
        "Removal of Terminal Ileum": {
          "meaning": "",
          "comments": []
        },
        "Resection, with Colostomy or Ileostomy": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneal Sampling": {
          "meaning": "",
          "comments": []
        },
        "Salpingectomy": {
          "meaning": "ncit:C51605",
          "comments": []
        },
        "Skin Level Cecostomy or Colostomy": {
          "meaning": "",
          "comments": []
        },
        "Subtotal Glossectomy": {
          "meaning": "",
          "comments": []
        },
        "Thoracotomy": {
          "meaning": "",
          "comments": []
        },
        "Total Abdominal Hysterectomy": {
          "meaning": "ncit:C51695",
          "comments": []
        },
        "Total Colectomy, NOS": {
          "meaning": "",
          "comments": []
        },
        "Total Esophagectomy": {
          "meaning": "",
          "comments": []
        },
        "Total Laparoscopic Hysterectomy": {
          "meaning": "",
          "comments": []
        },
        "Total Laryngectomy": {
          "meaning": "",
          "comments": []
        },
        "Tracheostomy": {
          "meaning": "",
          "comments": []
        },
        "Tracheo-esophageal Repair": {
          "meaning": "",
          "comments": []
        },
        "Ureterolysis": {
          "meaning": "",
          "comments": []
        },
        "Vaginectomy, Complete": {
          "meaning": "",
          "comments": []
        },
        "Vaginectomy, Partial": {
          "meaning": "",
          "comments": []
        },
        "Ventriculoperitoneal Shunt Placement": {
          "meaning": "",
          "comments": []
        },
        "Vulvectomy, Radical, Partial": {
          "meaning": "",
          "comments": []
        },
        "Vulvectomy, Radical, Complete": {
          "meaning": "",
          "comments": []
        },
        "Vulvectomy, Simple, Complete": {
          "meaning": "",
          "comments": []
        },
        "Vulvectomy, Simple, Partial": {
          "meaning": "",
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
        "mmol/L": {
          "meaning": "ncit:C64387",
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