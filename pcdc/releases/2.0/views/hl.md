---
layout: default
title: Hodgkin Lymphoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*HL View*

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
- **Hodgkin Lymphoma**
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

The HL view of the PCDC data model represents consensus data modeling by an international group of pediatric Hodgkin lymphoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Hodgkin Lymphoma Data Collaboration (NODAL). It is based on the collective requirements of its contributors.


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

## FamilyMedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `family_medical_history_condition` | `string` |  |
| `relation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-relationenum')">RelationEnum</button> |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |
| `assisted_conception` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-assistedconceptionenum')">AssistedConceptionEnum</button> |  |

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
| `age_at_enrollment` | `integer` |  |
| `study_phase` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyphaseenum')">StudyPhaseEnum</button> |  |
| `study_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studytypeenum')">StudyTypeEnum</button> |  |
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

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `imaging_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-imagingresultenum')">ImagingResultEnum</button> |  |
| `deauville_score` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-deauvillescoreenum')">DeauvilleScoreEnum</button> |  |
| `qpet_score` | `decimal` |  |
| `performance_score` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-performancescoreenum')">PerformanceScoreEnum</button> |  |
| `presentation_symptoms` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentationsymptomsenum')">PresentationSymptomsEnum</button> |  |
| `presentation_symptoms_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `review_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reviewsourceenum')">ReviewSourceEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement1_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement2` | `decimal` |  |
| `measurement2_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement3` | `decimal` |  |
| `measurement3_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `bulky_disease` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `pleural_effusion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `pericardial_effusion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `bulk_nodal_aggregate` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `med_ratio` | `decimal` |  |
| `nodular_splenic` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |
| `ann_arbor_mod_ab` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-annarbormodabenum')">AnnArborModAbEnum</button> |  |
| `ann_arbor_mod_e` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ann_arbor_mod_s` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

<div class="domain-heading">Intervention</div>

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `protocol_medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `medication_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationcategoryenum')">MedicationCategoryEnum</button> |  |
| `supportive_care_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-supportivecaredetailenum')">SupportiveCareDetailEnum</button> |  |
| `route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `number_doses` | `decimal` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_intended` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |

## ProtocolTreatmentModifications

| Slot | Range | Description |
|---|---|---|
| `age_at_modification` | `integer` |  |
| `modification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-modificationenum')">ModificationEnum</button> |  |
| `modification_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-modificationbasisenum')">ModificationBasisEnum</button> |  |
| `reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonenum')">ReasonEnum</button> |  |
| `toxicity_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-toxicitydetailenum')">ToxicityDetailEnum</button> |  |
| `toxicity_immune` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `toxicity_infusion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `original_agent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-originalagentenum')">OriginalAgentEnum</button> |  |
| `sub_agent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subagentenum')">SubAgentEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `protocol_radiation_therapy` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
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
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `protocol_sct` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `sct_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-scttypeenum')">SctTypeEnum</button> |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `donor_relationship` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-donorrelationshipenum')">DonorRelationshipEnum</button> |  |
| `conditioning_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conditioningtypeenum')">ConditioningTypeEnum</button> |  |
| `cd34_collected` | `decimal` |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `protocol_procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `non_protocol_timing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nonprotocoltimingenum')">NonProtocolTimingEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `extent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-extentenum')">ExtentEnum</button> |  |
| `number_nodes` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-numbernodesenum')">NumberNodesEnum</button> |  |
| `number_nodes_numeric` | `decimal` |  |
| `purpose` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-purposeenum')">PurposeEnum</button> |  |

## TransfusionMedicineProcedure

| Slot | Range | Description |
|---|---|---|
| `age_at_tmp_start` | `integer` |  |
| `tmp_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmptypeenum')">TmpTypeEnum</button> |  |
| `tmp_product` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tmpproductenum')">TmpProductEnum</button> |  |
| `product_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-producttypeenum')">ProductTypeEnum</button> |  |
| `number_units` | `decimal` |  |

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
| `ae_pathogen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aepathogenenum')">AePathogenEnum</button> |  |
| `ae_immune` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_infusion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_reported` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_attribution` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeattributionenum')">AeAttributionEnum</button> |  |
| `ae_expected` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeexpectedenum')">AeExpectedEnum</button> |  |
| `ae_tx_mod` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_hospitalization` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_intervention_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `ae_pathogen_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aepathogenstatusenum')">AePathogenStatusEnum</button> |  |
| `ae_outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aeoutcomeenum')">AeOutcomeEnum</button> |  |

## LateEffects

| Slot | Range | Description |
|---|---|---|
| `age_at_le_eval` | `integer` |  |
| `le` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-leenum')">LeEnum</button> |  |
| `le_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ledetailenum')">LeDetailEnum</button> |  |
| `le_sub_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesubdetailenum')">LeSubDetailEnum</button> |  |
| `le_severity_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-leseveritygradeenum')">LeSeverityGradeEnum</button> |  |
| `le_ctcae_version` | `string` |  |

## PatientReportedOutcomesMetadata

| Slot | Range | Description |
|---|---|---|
| `pro_study_id` | `string` |  |
| `time_point` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-timepointenum')">TimePointEnum</button> |  |
| `pro_measures` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-promeasuresenum')">ProMeasuresEnum</button> |  |
| `pro_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-promeasurementtypeenum')">ProMeasurementTypeEnum</button> |  |
| `raters` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ratersenum')">RatersEnum</button> |  |
| `eligible_age_lower` | `integer` |  |
| `eligible_age_upper` | `integer` |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsemethodenum')">ResponseMethodEnum</button> |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `interim_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-interimresponseenum')">InterimResponseEnum</button> |  |
| `pct_change` | `decimal` |  |
| `symptoms_at_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `palpable_nodes` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `nodular_splenic` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `morph_code` | `string` |  |
| `morph_code_text` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | `TopCodeSystemEnum` |  |
| `smn_field` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smnfieldenum')">SmnFieldEnum</button> |  |

<div class="domain-heading">Testing</div>

## Biospecimen

| Slot | Range | Description |
|---|---|---|
| `biospecimen_container_type` | `string` |  |
| `biospecimen_media` | `string` |  |
| `biospecimen_type` | `string` |  |
| `current_qty_unit` | `string` |  |
| `current_qty_value` | `string` |  |

## FunctionTest

| Slot | Range | Description |
|---|---|---|
| `age_at_function_test` | `integer` |  |
| `function_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functiontestenum')">FunctionTestEnum</button> |  |
| `functional_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functionalmeasurementtypeenum')">FunctionalMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `functional_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-functionalmeasurementresultunitenum')">FunctionalMeasurementResultUnitEnum</button> |  |

## Immunohistochemistry

| Slot | Range | Description |
|---|---|---|
| `age_at_ihc` | `integer` |  |
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

<div id="enum-modal-adverseeventenum" class="enum-modal" onclick="closeEnumModal('enum-modal-adverseeventenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-adverseeventenum')">×</button>
<h3><code>AdverseEventEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Allergic Reaction</code></td><td><code>ncit:C114476</code></td><td></td></tr>
<tr><td><code>Cardiac Toxicity</code></td><td><code>ncit:C27994</code></td><td></td></tr>
<tr><td><code>Endocrine Toxicity</code></td><td><code>ncit:C138163</code></td><td></td></tr>
<tr><td><code>Fatigue</code></td><td><code>ncit:C3036</code></td><td></td></tr>
<tr><td><code>GI Toxicity</code></td><td><code>ncit:C185646</code></td><td></td></tr>
<tr><td><code>Hepatic Toxicity</code></td><td><code>ncit:C185645</code></td><td></td></tr>
<tr><td><code>Infection</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Mucositis</code></td><td><code>ncit:C115965</code></td><td></td></tr>
<tr><td><code>Musculoskeletal Toxicity</code></td><td><code>ncit:C185647</code></td><td></td></tr>
<tr><td><code>Neuropathy</code></td><td><code>ncit:C4731</code></td><td></td></tr>
<tr><td><code>Neutropenia</code></td><td><code>ncit:C80520</code></td><td></td></tr>
<tr><td><code>Psychiatric Toxicity</code></td><td><code>ncit:C185648</code></td><td></td></tr>
<tr><td><code>Pulmonary Toxicity</code></td><td><code>ncit:C177374</code></td><td></td></tr>
<tr><td><code>Rashes</code></td><td><code>ncit:C39594</code></td><td></td></tr>
<tr><td><code>Renal Toxicity</code></td><td><code>ncit:C115459</code></td><td></td></tr>
<tr><td><code>Thrombocytopenia</code></td><td><code>ncit:C3408</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Balis Neuropathy Scale</code></td><td><code>ncit:C178081</code></td><td></td></tr>
<tr><td><code>CTCAE</code></td><td><code>ncit:C49704</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aeexpectedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aeexpectedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aeexpectedenum')">×</button>
<h3><code>AeExpectedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Expected</code></td><td><code>ncit:C41333</code></td><td></td></tr>
<tr><td><code>Unexpected</code></td><td><code>ncit:C41334</code></td><td></td></tr>
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
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aeoutcomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aeoutcomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aeoutcomeenum')">×</button>
<h3><code>AeOutcomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Death, Contributory</code></td><td><code>ncit:C168948</code></td><td></td></tr>
<tr><td><code>Death, Noncontributory</code></td><td><code>ncit:C173315</code></td><td></td></tr>
<tr><td><code>Not Recovered</code></td><td><code>ncit:C49494</code></td><td></td></tr>
<tr><td><code>Recovered</code></td><td><code>ncit:C85257</code></td><td></td></tr>
<tr><td><code>Recovered With Sequelae</code></td><td><code>ncit:C49495</code></td><td></td></tr>
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
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aepathogenstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aepathogenstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aepathogenstatusenum')">×</button>
<h3><code>AePathogenStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Confirmed</code></td><td><code>ncit:C25458</code></td><td></td></tr>
<tr><td><code>Suspected</code></td><td><code>ncit:C71458</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-annarbormodabenum" class="enum-modal" onclick="closeEnumModal('enum-modal-annarbormodabenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-annarbormodabenum')">×</button>
<h3><code>AnnArborModAbEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ann Arbor A Symptoms Indicator</code></td><td><code>ncit:C185483</code></td><td></td></tr>
<tr><td><code>Ann Arbor B Symptoms Indicator</code></td><td><code>ncit:C177585</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>BSA</code></td><td><code>ncit:C25157</code></td><td></td></tr>
<tr><td><code>Height</code></td><td><code>ncit:C164634</code></td><td></td></tr>
<tr><td><code>Weight</code></td><td><code>ncit:C81328</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-assistedconceptionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-assistedconceptionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-assistedconceptionenum')">×</button>
<h3><code>AssistedConceptionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>In Vitro Fertilization</code></td><td><code>ncit:C16580</code></td><td></td></tr>
<tr><td><code>Intracytoplasmic Sperm Injection</code></td><td><code>ncit:C185482</code></td><td></td></tr>
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
<tr><td><code>Bacterial Infection</code></td><td><code>ncit:C2890</code></td><td></td></tr>
<tr><td><code>Cardiac Disease</code></td><td><code>ncit:C3079</code></td><td></td></tr>
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Infection, NOS</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Organ Failure, NOS</code></td><td><code>ncit:C185320</code></td><td></td></tr>
<tr><td><code>Pulmonary Disease</code></td><td><code>ncit:C3198</code></td><td></td></tr>
<tr><td><code>Surgical Complication</code></td><td><code>ncit:C164157</code></td><td></td></tr>
<tr><td><code>Unacceptable Toxicity</code></td><td><code>ncit:C199267</code></td><td></td></tr>
<tr><td><code>Viral Infection</code></td><td><code>ncit:C3439</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Pre-Treatment Disease Complications</code></td><td><code>ncit:C168876</code></td><td></td></tr>
<tr><td><code>Secondary Malignancy</code></td><td><code>ncit:C4968</code></td><td>D4CGNote: Use the Subsequent Malignant Neoplasm table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
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
<tr><td><code>NODAL</code></td><td><code>ncit:C192759</code></td><td></td></tr>
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
<tr><td><code>Chemoimmunotherapy</code></td><td><code>ncit:C94251</code></td><td></td></tr>
<tr><td><code>Chemotherapy, NOS</code></td><td><code>ncit:C15632</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
<tr><td><code>Immunotherapy</code></td><td><code>ncit:C15262</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code>ncit:C15313</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-deauvillescoreenum" class="enum-modal" onclick="closeEnumModal('enum-modal-deauvillescoreenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-deauvillescoreenum')">×</button>
<h3><code>DeauvilleScoreEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Score 1</code></td><td><code>ncit:C99728</code></td><td></td></tr>
<tr><td><code>Score 2</code></td><td><code>ncit:C99747</code></td><td></td></tr>
<tr><td><code>Score 3</code></td><td><code>ncit:C99748</code></td><td></td></tr>
<tr><td><code>Score 4</code></td><td><code>ncit:C99749</code></td><td></td></tr>
<tr><td><code>Score 5</code></td><td><code>ncit:C99750</code></td><td></td></tr>
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
<tr><td><code>Biopsy</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Bone Scan</code></td><td><code>ncit:C17646</code></td><td></td></tr>
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Gallium Scan</code></td><td><code>ncit:C38087</code></td><td></td></tr>
<tr><td><code>Lymphangiogram</code></td><td><code>ncit:C16805</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>PET-MRI</code></td><td><code>ncit:C103514</code></td><td></td></tr>
<tr><td><code>Physical Examination</code></td><td><code>ncit:C20989</code></td><td></td></tr>
<tr><td><code>Staging Laparotomy</code></td><td><code>ncit:C185327</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>X-Ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Hodgkin Lymphoma, Classical, NOS</code></td><td><code>ncit:C9357</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocyte Depletion, NOS</code></td><td><code>ncit:C9283</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nodular Lymphocyte Predominance</code></td><td><code>ncit:C7258</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, Mixed Cellularity, NOS</code></td><td><code>ncit:C3517</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, NOS</code></td><td><code>icdo:9650/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nodular Sclerosis, NOS</code></td><td><code>icdo:9663/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocyte-Rich</code></td><td><code>icdo:9651/3</code></td><td></td></tr>
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
<tr><td><code>HL</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Axilla or Pectoral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Axillary Nodes</code></td><td><code>ncit:C12904</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Celiac Nodes</code></td><td><code>ncit:C65166</code></td><td></td></tr>
<tr><td><code>Cervical Nodes</code></td><td><code>ncit:C32298</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Epitrochlear Nodes</code></td><td><code>ncit:C98182</code></td><td></td></tr>
<tr><td><code>Hilar Nodes</code></td><td><code>ncit:C134731</code></td><td></td></tr>
<tr><td><code>Iliac</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iliac Crest</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Infraclavicular Nodes</code></td><td><code>ncit:C63705</code></td><td></td></tr>
<tr><td><code>Inguinal Nodes</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Inguinal or Femoral Nodes</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C6634</code></td><td></td></tr>
<tr><td><code>Mesenteric Nodes</code></td><td><code>ncit:C77641</code></td><td></td></tr>
<tr><td><code>Muscle</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paraaortic Lymph Node</code></td><td><code>ncit:C77643</code></td><td></td></tr>
<tr><td><code>Pectoral Nodes</code></td><td><code>ncit:C120322</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Popliteal Nodes</code></td><td><code>ncit:C53146</code></td><td></td></tr>
<tr><td><code>Preauricular Lymph Node</code></td><td><code>ncit:C103429</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
<tr><td><code>Spleen</code></td><td><code>ncit:C12432</code></td><td></td></tr>
<tr><td><code>Splenic Hilar Nodes</code></td><td><code>ncit:C33600</code></td><td></td></tr>
<tr><td><code>Supraclavicular Nodes</code></td><td><code>ncit:C12903</code></td><td></td></tr>
<tr><td><code>Thyroid</code></td><td><code>ncit:C12400</code></td><td></td></tr>
<tr><td><code>Waldeyer's Ring</code></td><td><code>ncit:C73468</code></td><td></td></tr>
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
<tr><td><code>Equivocal</code></td><td><code>ncit:C178921</code></td><td></td></tr>
<tr><td><code>Partial Resection</code></td><td><code>ncit:C131680</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>EKG</code></td><td><code>ncit:C168186</code></td><td></td></tr>
<tr><td><code>Echocardiogram</code></td><td><code>ncit:C16525</code></td><td></td></tr>
<tr><td><code>Pulmonary Function Test</code></td><td><code>ncit:C38081</code></td><td></td></tr>
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
<tr><td><code>mL</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-functionalmeasurementtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-functionalmeasurementtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-functionalmeasurementtypeenum')">×</button>
<h3><code>FunctionalMeasurementTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ejection Fraction</code></td><td><code>ncit:C99524</code></td><td></td></tr>
<tr><td><code>FEF at 25-75%</code></td><td><code>ncit:C119546</code></td><td></td></tr>
<tr><td><code>FEV1</code></td><td><code>ncit:C38084</code></td><td></td></tr>
<tr><td><code>FVC</code></td><td><code>ncit:C111361</code></td><td></td></tr>
<tr><td><code>Landolt C</code></td><td><code></code></td><td></td></tr>
<tr><td><code>QTc</code></td><td><code>ncit:C100391</code></td><td></td></tr>
<tr><td><code>Shortening Fraction</code></td><td><code>ncit:C38020</code></td><td></td></tr>
<tr><td><code>Total Lung Capacity</code></td><td><code>ncit:C111325</code></td><td></td></tr>
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

<div id="enum-modal-imagingresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-imagingresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-imagingresultenum')">×</button>
<h3><code>ImagingResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Equivocal</code></td><td><code>ncit:C178921</code></td><td></td></tr>
<tr><td><code>Negative</code></td><td><code>ncit:C38757</code></td><td></td></tr>
<tr><td><code>Positive</code></td><td><code>ncit:C38758</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-interimresponseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-interimresponseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-interimresponseenum')">×</button>
<h3><code>InterimResponseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>Rapid Early Response (Adequate)</code></td><td><code>ncit:C185658</code></td><td></td></tr>
<tr><td><code>Slow Early Response (Inadequate)</code></td><td><code>ncit:C185659</code></td><td></td></tr>
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
<tr><td><code>Albumin</code></td><td><code>ncit:C64431</code></td><td></td></tr>
<tr><td><code>Alkaline Phophatase</code></td><td><code>ncit:C64432</code></td><td>(fa) ConsortiumNote: Liver Function Test</td></tr>
<tr><td><code>CD34</code></td><td><code>ncit:C102260</code></td><td></td></tr>
<tr><td><code>CRP</code></td><td><code>ncit:C64548</code></td><td></td></tr>
<tr><td><code>EBV DNA</code></td><td><code>ncit:C166035</code></td><td></td></tr>
<tr><td><code>EBV IgG</code></td><td><code>ncit:C184675</code></td><td></td></tr>
<tr><td><code>ESR</code></td><td><code>ncit:C74611</code></td><td></td></tr>
<tr><td><code>Eosinophils</code></td><td><code>ncit:C64550</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Free T4</code></td><td><code>ncit:C74786</code></td><td></td></tr>
<tr><td><code>Hemoglobin</code></td><td><code>ncit:C64848</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>LDH</code></td><td><code>ncit:C64855</code></td><td></td></tr>
<tr><td><code>Lymphocytes</code></td><td><code>ncit:C12535</code></td><td></td></tr>
<tr><td><code>Monocytes</code></td><td><code>ncit:C64823</code></td><td></td></tr>
<tr><td><code>Myelocyte</code></td><td><code>ncit:C13115</code></td><td></td></tr>
<tr><td><code>Neutrophil Count</code></td><td><code>ncit:C51950</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Phosphorus</code></td><td><code>ncit:C47934</code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Protein Total</code></td><td><code>ncit:C64858</code></td><td></td></tr>
<tr><td><code>RBC</code></td><td><code>ncit:C51946</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Segmented Neutrophils</code></td><td><code>ncit:C81997</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>TSH</code></td><td><code>ncit:C64813</code></td><td></td></tr>
<tr><td><code>Total T4</code></td><td><code>ncit:C74794</code></td><td></td></tr>
<tr><td><code>Uric Acid</code></td><td><code>ncit:C62652</code></td><td></td></tr>
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
<tr><td><code>PCR</code></td><td><code>ncit:C17003</code></td><td></td></tr>
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

<div id="enum-modal-ledetailenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ledetailenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ledetailenum')">×</button>
<h3><code>LeDetailEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Acquired Immunodeficiency</code></td><td><code>ncit:C2851</code></td><td></td></tr>
<tr><td><code>Arrhythmia</code></td><td><code>ncit:C2881</code></td><td></td></tr>
<tr><td><code>Arthritis</code></td><td><code>ncit:C2883</code></td><td></td></tr>
<tr><td><code>Atrophy</code></td><td><code>ncit:C79748</code></td><td></td></tr>
<tr><td><code>Autoimmune Reaction</code></td><td><code>ncit:C16313</code></td><td></td></tr>
<tr><td><code>Avascular-Necrosis</code></td><td><code>ncit:C118385</code></td><td></td></tr>
<tr><td><code>Bladder Disorder</code></td><td><code>ncit:C2900</code></td><td></td></tr>
<tr><td><code>Conduction Abnormality</code></td><td><code>ncit:C78245</code></td><td></td></tr>
<tr><td><code>Contraction</code></td><td><code>ncit:C30085</code></td><td></td></tr>
<tr><td><code>Dryness</code></td><td><code>ncit:C25489</code></td><td></td></tr>
<tr><td><code>Esophagitis</code></td><td><code>ncit:C9224</code></td><td></td></tr>
<tr><td><code>GI Adhesions</code></td><td><code>ncit:C185688</code></td><td></td></tr>
<tr><td><code>Gastritis</code></td><td><code>ncit:C26780</code></td><td></td></tr>
<tr><td><code>Gonadal Dysfunction</code></td><td><code>ncit:C26786</code></td><td></td></tr>
<tr><td><code>Hepatic Dysfunction</code></td><td><code>ncit:C50634</code></td><td></td></tr>
<tr><td><code>Hypertension</code></td><td><code>ncit:C3117</code></td><td></td></tr>
<tr><td><code>Musculoskeletal Hypoplasia</code></td><td><code>ncit:C185696</code></td><td></td></tr>
<tr><td><code>Neurocognitive Functions</code></td><td><code>ncit:C94321</code></td><td></td></tr>
<tr><td><code>Neuropathy</code></td><td><code>ncit:C4731</code></td><td></td></tr>
<tr><td><code>Obstructive Lung Disease</code></td><td><code>ncit:C3199</code></td><td></td></tr>
<tr><td><code>Osteopenia</code></td><td><code>ncit:C50910</code></td><td></td></tr>
<tr><td><code>Osteoporosis</code></td><td><code>ncit:C3298</code></td><td></td></tr>
<tr><td><code>Pancreatitis</code></td><td><code>ncit:C3306</code></td><td></td></tr>
<tr><td><code>Pericarditis</code></td><td><code>ncit:C34915</code></td><td></td></tr>
<tr><td><code>Pigment Changes</code></td><td><code>ncit:C124224</code></td><td></td></tr>
<tr><td><code>Reactive Airway Disease</code></td><td><code>ncit:C113673</code></td><td></td></tr>
<tr><td><code>Renal Disorder</code></td><td><code>ncit:C3149</code></td><td></td></tr>
<tr><td><code>Restrictive Lung Disease</code></td><td><code>ncit:C91762</code></td><td></td></tr>
<tr><td><code>Scarring</code></td><td><code>ncit:C34483</code></td><td></td></tr>
<tr><td><code>Scoliosis</code></td><td><code>ncit:C78603</code></td><td></td></tr>
<tr><td><code>Stroke</code></td><td><code>ncit:C3390</code></td><td></td></tr>
<tr><td><code>Telangiectasia</code></td><td><code>ncit:C28194</code></td><td></td></tr>
<tr><td><code>Thyroid Disorder</code></td><td><code>ncit:C26893</code></td><td></td></tr>
<tr><td><code>Valvular Disease</code></td><td><code>ncit:C45525</code></td><td></td></tr>
<tr><td><code>Vascular Disorder</code></td><td><code>ncit:C35117</code></td><td></td></tr>
<tr><td><code>Ventricular Dysfunction</code></td><td><code>ncit:C111655</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-leenum" class="enum-modal" onclick="closeEnumModal('enum-modal-leenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-leenum')">×</button>
<h3><code>LeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Breast Hypoplasia</code></td><td><code>ncit:C78222</code></td><td></td></tr>
<tr><td><code>Cardiovascular Disorder</code></td><td><code>ncit:C2931</code></td><td></td></tr>
<tr><td><code>Dermatologic Disorder</code></td><td><code>ncit:C3371</code></td><td></td></tr>
<tr><td><code>Endocrine Disorder</code></td><td><code>ncit:C3009</code></td><td></td></tr>
<tr><td><code>Fatigue</code></td><td><code>ncit:C3036</code></td><td></td></tr>
<tr><td><code>GI Disorder</code></td><td><code>ncit:C2990</code></td><td></td></tr>
<tr><td><code>Genitourinary Disorder</code></td><td><code>ncit:C156660</code></td><td></td></tr>
<tr><td><code>Immunologic Disorder</code></td><td><code>ncit:C3507</code></td><td></td></tr>
<tr><td><code>Musculoskeletal Disorder</code></td><td><code>ncit:C107377</code></td><td></td></tr>
<tr><td><code>Neurological Disorder</code></td><td><code>ncit:C26835</code></td><td></td></tr>
<tr><td><code>Psychiatric Disorder</code></td><td><code>ncit:C2893</code></td><td></td></tr>
<tr><td><code>Pulmonary Disorder</code></td><td><code>ncit:C3198</code></td><td></td></tr>
<tr><td><code>Xerostomia</code></td><td><code>ncit:C26917</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-leseveritygradeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-leseveritygradeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-leseveritygradeenum')">×</button>
<h3><code>LeSeverityGradeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CTCAE &gt;&gt; Grade 1</code></td><td><code>ncit:C41338</code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 2</code></td><td><code>ncit:C41339</code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 3</code></td><td><code>ncit:C41340</code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 4</code></td><td><code>ncit:C84266</code></td><td></td></tr>
<tr><td><code>CTCAE &gt;&gt; Grade 5</code></td><td><code>ncit:C48275</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lesubdetailenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lesubdetailenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lesubdetailenum')">×</button>
<h3><code>LeSubDetailEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>AIN</code></td><td><code>ncit:C176730</code></td><td></td></tr>
<tr><td><code>AKI</code></td><td><code>ncit:C26808</code></td><td></td></tr>
<tr><td><code>Amenorrhea</code></td><td><code>ncit:C61443</code></td><td></td></tr>
<tr><td><code>Asthma</code></td><td><code>ncit:C28397</code></td><td></td></tr>
<tr><td><code>Cardiomyopathy, NOS</code></td><td><code>ncit:C34830</code></td><td></td></tr>
<tr><td><code>Decreased Creatinine Clearance</code></td><td><code>ncit:C185671</code></td><td></td></tr>
<tr><td><code>Decreased GFR</code></td><td><code>ncit:C78326</code></td><td></td></tr>
<tr><td><code>Dilated Cardiomyopathy</code></td><td><code>ncit:C84673</code></td><td></td></tr>
<tr><td><code>Fertility Disorder</code></td><td><code>ncit:C3836</code></td><td></td></tr>
<tr><td><code>Germ Cell Failure, Confirmed</code></td><td><code>ncit:C185685</code></td><td></td></tr>
<tr><td><code>Germ Cell Failure, Suspected</code></td><td><code>ncit:C185684</code></td><td></td></tr>
<tr><td><code>Heart Block</code></td><td><code>ncit:C50501</code></td><td></td></tr>
<tr><td><code>Hyperthyroid</code></td><td><code>ncit:C3123</code></td><td>(hl) ConsortiumNote: If multiple late effect sub-details, include one observation per late effect sub-detail.</td></tr>
<tr><td><code>Hypothyroid</code></td><td><code>ncit:C26800</code></td><td></td></tr>
<tr><td><code>Menstrual Cycle Dysfunction</code></td><td><code>ncit:C34815</code></td><td></td></tr>
<tr><td><code>Motor Neuropathy</code></td><td><code>ncit:C3500</code></td><td></td></tr>
<tr><td><code>Prolonged QT</code></td><td><code>ncit:C71034</code></td><td></td></tr>
<tr><td><code>Pulmonary Fibrosis</code></td><td><code>ncit:C26869</code></td><td></td></tr>
<tr><td><code>Restrictive Cardiomyopathy</code></td><td><code>ncit:C62798</code></td><td></td></tr>
<tr><td><code>Sensory Neuropathy</code></td><td><code>ncit:C3501</code></td><td></td></tr>
<tr><td><code>Supraventricular Tachycardia</code></td><td><code>ncit:C35061</code></td><td></td></tr>
<tr><td><code>Testosterone Deficiency</code></td><td><code>ncit:C143195</code></td><td></td></tr>
<tr><td><code>Thyroid Nodule</code></td><td><code>ncit:C3415</code></td><td></td></tr>
<tr><td><code>Tubular Damage</code></td><td><code>ncit:C185689</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lesionmeasurementaxisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lesionmeasurementaxisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lesionmeasurementaxisenum')">×</button>
<h3><code>LesionMeasurementAxisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Anteroposterior</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cranial-Caudal</code></td><td><code>ncit:C182395</code></td><td>D4CGNote: This value is synonymous with 'Height'.</td></tr>
<tr><td><code>Transverse</code></td><td><code>ncit:C182199</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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

<div id="enum-modal-markersenum" class="enum-modal" onclick="closeEnumModal('enum-modal-markersenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-markersenum')">×</button>
<h3><code>MarkersEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>CD20</code></td><td><code>ncit:C38896</code></td><td></td></tr>
<tr><td><code>CD30</code></td><td><code>ncit:C38906</code></td><td></td></tr>
<tr><td><code>EBER</code></td><td><code>ncit:C111618</code></td><td></td></tr>
<tr><td><code>LMP1</code></td><td><code>ncit:C18863</code></td><td></td></tr>
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
<tr><td><code>Beckwith-Wiedemann Syndrome</code></td><td><code>ncit:C34415</code></td><td></td></tr>
<tr><td><code>Celiac Disease</code></td><td><code>ncit:C26714</code></td><td></td></tr>
<tr><td><code>Central Hypoventilation Syndrome</code></td><td><code>ncit:C98889</code></td><td></td></tr>
<tr><td><code>Cleft Lip</code></td><td><code>ncit:C87175</code></td><td></td></tr>
<tr><td><code>Cleft Palate</code></td><td><code>ncit:C87069</code></td><td></td></tr>
<tr><td><code>Clubfoot</code></td><td><code>ncit:C84641</code></td><td></td></tr>
<tr><td><code>Costello Syndrome</code></td><td><code>ncit:C84652</code></td><td></td></tr>
<tr><td><code>Cushing Syndrome</code></td><td><code>ncit:C2969</code></td><td></td></tr>
<tr><td><code>Denys-Drash Syndrome</code></td><td><code>ncit:C84668</code></td><td></td></tr>
<tr><td><code>Diabetes Mellitus (Type I)</code></td><td><code>ncit:C2986</code></td><td></td></tr>
<tr><td><code>Down Syndrome</code></td><td><code>ncit:C2993</code></td><td></td></tr>
<tr><td><code>Gastroschisis</code></td><td><code>ncit:C84725</code></td><td></td></tr>
<tr><td><code>Goodpasture's Syndrome</code></td><td><code>ncit:C34649</code></td><td></td></tr>
<tr><td><code>Gorlin Syndrome</code></td><td><code>ncit:C2892</code></td><td></td></tr>
<tr><td><code>Graves' Disease</code></td><td><code>ncit:C3071</code></td><td></td></tr>
<tr><td><code>Hashimoto's Thyroiditis</code></td><td><code>ncit:C27191</code></td><td></td></tr>
<tr><td><code>Heart Defect</code></td><td><code>ncit:C168217</code></td><td></td></tr>
<tr><td><code>Hemihypertrophy</code></td><td><code>ncit:C88541</code></td><td></td></tr>
<tr><td><code>Hereditary Retinoblastoma</code></td><td><code>ncit:C8495</code></td><td></td></tr>
<tr><td><code>Hirschprung Disease</code></td><td><code>ncit:C34700</code></td><td></td></tr>
<tr><td><code>Inflammatory Bowel Disease</code></td><td><code>ncit:C3138</code></td><td></td></tr>
<tr><td><code>Juvenile Idiopathic Arthritis</code></td><td><code>ncit:C114357</code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Lynch Syndrome</code></td><td><code>ncit:C8494</code></td><td></td></tr>
<tr><td><code>Mixed Connective Tissue Disease</code></td><td><code>ncit:C84892</code></td><td></td></tr>
<tr><td><code>Multiple Sclerosis</code></td><td><code>ncit:C3243</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis Type I</code></td><td><code>ncit:C143014</code></td><td></td></tr>
<tr><td><code>Noonan Syndrome</code></td><td><code>ncit:C34854</code></td><td></td></tr>
<tr><td><code>Psoriasis</code></td><td><code>ncit:C3346</code></td><td></td></tr>
<tr><td><code>Scleroderma</code></td><td><code>ncit:C26746</code></td><td></td></tr>
<tr><td><code>Systemic Lupus Erythematosus</code></td><td><code>ncit:C3201</code></td><td></td></tr>
<tr><td><code>Vitiligo</code></td><td><code>ncit:C26915</code></td><td></td></tr>
<tr><td><code>WAGR Syndrome</code></td><td><code>ncit:C3718</code></td><td></td></tr>
<tr><td><code>Weaver Syndrome</code></td><td><code>ncit:C125599</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>IU/m2</code></td><td><code>ncit:C67378</code></td><td></td></tr>
<tr><td><code>MBq</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bendamustine</code></td><td><code>ncit:C73261</code></td><td></td></tr>
<tr><td><code>Bleomycin</code></td><td><code>rxcui:1622</code></td><td></td></tr>
<tr><td><code>Brentuximab Vedotin</code></td><td><code>ncit:C66944</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Carmustine</code></td><td><code>ncit:C349</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cytarabine</code></td><td><code>rxcui:3041</code></td><td></td></tr>
<tr><td><code>Dacarbazine</code></td><td><code>rxcui:3098</code></td><td></td></tr>
<tr><td><code>Dexamethasone</code></td><td><code>ncit:C422</code></td><td></td></tr>
<tr><td><code>Dexrazoxane</code></td><td><code>ncit:C1333</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Toxicity Prevention</td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Erythropoeitin</code></td><td><code>ncit:C20429</code></td><td></td></tr>
<tr><td><code>Etopophos</code></td><td><code>ncit:C1093</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Filgrastim</code></td><td><code>ncit:C1474</code></td><td></td></tr>
<tr><td><code>Fludarabine</code></td><td><code>ncit:C1094</code></td><td></td></tr>
<tr><td><code>Gabapentin</code></td><td><code>ncit:C1108</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Morphine</code></td><td><code>ncit:C62051</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Non-Corticosteroid Immunosuppressive Agent</code></td><td><code>ncit:C185652</code></td><td></td></tr>
<tr><td><code>PEG-filgrastim</code></td><td><code>ncit:C1854</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Plerixafor</code></td><td><code>ncit:C1777</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td>(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant</td></tr>
<tr><td><code>Procarbazine</code></td><td><code>rxcui:8702</code></td><td></td></tr>
<tr><td><code>Systemic Corticosteroid</code></td><td><code>ncit:C122080</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>rxcui:10473</code></td><td></td></tr>
<tr><td><code>Thyroid Hormone Replacement</code></td><td><code>ncit:C888</code></td><td></td></tr>
<tr><td><code>Topical Corticosteroid</code></td><td><code>ncit:C29505</code></td><td></td></tr>
<tr><td><code>Vinblastine</code></td><td><code>rxcui:11198</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>rxcui:39541</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-modificationbasisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-modificationbasisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-modificationbasisenum')">×</button>
<h3><code>ModificationBasisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clinical Indication</code></td><td><code>ncit:C185637</code></td><td>(hl) ConsortiumNote: Only fill in Disease Phase, Disease Phase Number, Course, and Course Number if 'AGE_' not known Note: Course Number is grouped within subcategory. I.e. number Induction 1, 2, 3, 4, etc..., Prephase 1, 2, 3, 4, etc..., Maintenance 1,2,3,4,5,6 etc...</td></tr>
<tr><td><code>Per Protocol</code></td><td><code>ncit:C181023</code></td><td>(pre) ConsortiumNote: If multiple modifications made, include one observation per modification.</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(hl) ConsortiumNote: If multiple modifications made, include one observation per modification.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-modificationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-modificationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-modificationenum')">×</button>
<h3><code>ModificationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Delayed</code></td><td><code>ncit:C25476</code></td><td></td></tr>
<tr><td><code>Discontinued</code></td><td><code>ncit:C25484</code></td><td></td></tr>
<tr><td><code>Dose Reduction</code></td><td><code>ncit:C49505</code></td><td></td></tr>
<tr><td><code>New Agent Addition</code></td><td><code>ncit:C185633</code></td><td></td></tr>
<tr><td><code>Not Given</code></td><td><code>ncit:C106487</code></td><td></td></tr>
<tr><td><code>Substitution</code></td><td><code>ncit:C54071</code></td><td></td></tr>
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

<div id="enum-modal-numbernodesenum" class="enum-modal" onclick="closeEnumModal('enum-modal-numbernodesenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-numbernodesenum')">×</button>
<h3><code>NumberNodesEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Multiple Lymph Nodes</code></td><td><code>ncit:C185519</code></td><td></td></tr>
<tr><td><code>Single Lymph Node</code></td><td><code>ncit:C185518</code></td><td></td></tr>
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

<div id="enum-modal-originalagentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-originalagentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-originalagentenum')">×</button>
<h3><code>OriginalAgentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bendamustine</code></td><td><code>ncit:C73261</code></td><td></td></tr>
<tr><td><code>Bleomycin</code></td><td><code>ncit:C313</code></td><td></td></tr>
<tr><td><code>Brentuximab Vedotin</code></td><td><code>ncit:C66944</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>ncit:C1282</code></td><td></td></tr>
<tr><td><code>Carmustine</code></td><td><code>ncit:C349</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>ncit:C405</code></td><td></td></tr>
<tr><td><code>Cytarabine</code></td><td><code>ncit:C408</code></td><td></td></tr>
<tr><td><code>Dacarbazine</code></td><td><code>ncit:C411</code></td><td></td></tr>
<tr><td><code>Dexamethasone</code></td><td><code>ncit:C422</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>ncit:C456</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>ncit:C491</code></td><td></td></tr>
<tr><td><code>Etoposide Phosphate</code></td><td><code>ncit:C1093</code></td><td></td></tr>
<tr><td><code>Fludarabine</code></td><td><code>ncit:C1094</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>ncit:C66876</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>ncit:C564</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>ncit:C633</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>ncit:C642</code></td><td></td></tr>
<tr><td><code>Nitrogen Mustard</code></td><td><code>ncit:C62056</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>ncit:C68814</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>ncit:C106432</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td></td></tr>
<tr><td><code>Procarbazine</code></td><td><code>ncit:C62072</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>ncit:C875</code></td><td></td></tr>
<tr><td><code>Vinblastine</code></td><td><code>ncit:C930</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>ncit:C933</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>ncit:C1275</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-presentationsymptomsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-presentationsymptomsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-presentationsymptomsenum')">×</button>
<h3><code>PresentationSymptomsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fever</code></td><td><code>ncit:C3038</code></td><td></td></tr>
<tr><td><code>Night Sweats</code></td><td><code>ncit:C3279</code></td><td></td></tr>
<tr><td><code>Weight Loss</code></td><td><code>ncit:C55339</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-promeasurementtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-promeasurementtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-promeasurementtypeenum')">×</button>
<h3><code>ProMeasurementTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Health Profile</code></td><td><code>ncit:C62359</code></td><td></td></tr>
<tr><td><code>Health Utility</code></td><td><code>ncit:C185674</code></td><td></td></tr>
<tr><td><code>Symptom Scale</code></td><td><code>ncit:C124147</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C432234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-promeasuresenum" class="enum-modal" onclick="closeEnumModal('enum-modal-promeasuresenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-promeasuresenum')">×</button>
<h3><code>ProMeasuresEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fact NTX</code></td><td><code>ncit:C177378</code></td><td></td></tr>
<tr><td><code>PEDPRO-CTCAE</code></td><td><code>ncit:C186439</code></td><td></td></tr>
<tr><td><code>PRO-CTCAE</code></td><td><code>ncit:C103843</code></td><td></td></tr>
<tr><td><code>PROMIS Fatigue Short Form</code></td><td><code>ncit:C129493</code></td><td></td></tr>
<tr><td><code>PROMIS Global</code></td><td><code>ncit:C103253</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Axillary Nodes</code></td><td><code>ncit:C12904</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Celiac Nodes</code></td><td><code>ncit:C65166</code></td><td></td></tr>
<tr><td><code>Cervical Nodes</code></td><td><code>ncit:C32298</code></td><td></td></tr>
<tr><td><code>Epitrochlear</code></td><td><code>ncit:C98182</code></td><td></td></tr>
<tr><td><code>Hilar Nodes</code></td><td><code>ncit:C102330</code></td><td></td></tr>
<tr><td><code>Iliac Crest</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Infraclavicular Nodes</code></td><td><code>ncit:C63705</code></td><td></td></tr>
<tr><td><code>Inguinal</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Mesenteric Nodes</code></td><td><code>ncit:C77641</code></td><td></td></tr>
<tr><td><code>Para-Aortic Nodes</code></td><td><code>ncit:C77643</code></td><td></td></tr>
<tr><td><code>Pectoral Nodes</code></td><td><code>ncit:C120322</code></td><td></td></tr>
<tr><td><code>Popliteal Nodes</code></td><td><code>ncit:C53146</code></td><td></td></tr>
<tr><td><code>Preauricular Nodes</code></td><td><code>ncit:C103429</code></td><td></td></tr>
<tr><td><code>Spleen</code></td><td><code>ncit:C7295</code></td><td></td></tr>
<tr><td><code>Splenic Hilar Nodes</code></td><td><code>ncit:C33600</code></td><td></td></tr>
<tr><td><code>Supraclavicular Nodes</code></td><td><code>ncit:C12903</code></td><td></td></tr>
<tr><td><code>Waldeyer's Ring</code></td><td><code>ncit:C73468</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-producttypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-producttypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-producttypeenum')">×</button>
<h3><code>ProductTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Apheresis</code></td><td><code>ncit:C15191</code></td><td></td></tr>
<tr><td><code>Random</code></td><td><code>ncit:C60702</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-purposeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-purposeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-purposeenum')">×</button>
<h3><code>PurposeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Biopsy of Distant Site for Staging</code></td><td><code>ncit:C185530</code></td><td></td></tr>
<tr><td><code>Diagnostic Biopsy for Possible Recurrence</code></td><td><code>ncit:C185534</code></td><td></td></tr>
<tr><td><code>Initial Diagnostic Procedure</code></td><td><code>ncit:C185527</code></td><td></td></tr>
<tr><td><code>Second Look Surgery to Attempt Total Resection</code></td><td><code>ncit:C185528</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-ratersenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ratersenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ratersenum')">×</button>
<h3><code>RatersEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Subject</code></td><td><code>ncit:C41189</code></td><td></td></tr>
<tr><td><code>Parent/Guardian</code></td><td><code>ncit:C185701</code></td><td></td></tr>
<tr><td><code>Subject + Parent/GuardianParent/Guardian</code></td><td><code>ncit:C185702</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C432234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-reasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasonenum')">×</button>
<h3><code>ReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Drug Not Available</code></td><td><code>ncit:C185643</code></td><td></td></tr>
<tr><td><code>Hematologic Toxicity</code></td><td><code>ncit:C15474</code></td><td></td></tr>
<tr><td><code>Non-Hematologic Toxicity</code></td><td><code>ncit:C185641</code></td><td></td></tr>
<tr><td><code>Pre-Existing Organ Dysfunction</code></td><td><code>ncit:C185644</code></td><td></td></tr>
<tr><td><code>Scheduling Issues</code></td><td><code>ncit:C1685642</code></td><td></td></tr>
<tr><td><code>Subject Non-Compliance</code></td><td><code>ncit:C91752</code></td><td></td></tr>
<tr><td><code>Surgical Complications</code></td><td><code>ncit:C164157</code></td><td></td></tr>
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

<div id="enum-modal-relationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-relationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-relationenum')">×</button>
<h3><code>RelationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Brother</code></td><td><code>ncit:C96570</code></td><td></td></tr>
<tr><td><code>Daughter</code></td><td><code>ncit:C150887</code></td><td></td></tr>
<tr><td><code>Father</code></td><td><code>ncit:C96572</code></td><td></td></tr>
<tr><td><code>Mother</code></td><td><code>ncit:C96580</code></td><td></td></tr>
<tr><td><code>Sister</code></td><td><code>ncit:C96586</code></td><td></td></tr>
<tr><td><code>Son</code></td><td><code>ncit:C150888</code></td><td></td></tr>
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
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Partial Response</code></td><td><code>ncit:C18058</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stable Disease</code></td><td><code>ncit:C18213</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Very Good Partial Response</code></td><td><code>ncit:C123618</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow Biopsy</code></td><td><code>ncit:C15193</code></td><td></td></tr>
<tr><td><code>Bone Scan</code></td><td><code>ncit:C17646</code></td><td></td></tr>
<tr><td><code>CT</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Gallium</code></td><td><code>ncit:C66798</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>PET</code></td><td><code>ncit:C17007</code></td><td>(hl) ConsortiumNote: If RESPONSE_CATEGORY is 'overall' and not based on a single response method, RESPONSE_METHOD should be 'Not applicable'</td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>PET-MRI</code></td><td><code>ncit:C103514</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>X-ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Intrathecal</code></td><td><code>ncit:C173292</code></td><td></td></tr>
<tr><td><code>Oral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parenteral</code></td><td><code>ncit:C38291</code></td><td></td></tr>
<tr><td><code>Systemic</code></td><td><code>ncit:C173291</code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Axilla</code></td><td><code>ncit:C12674</code></td><td></td></tr>
<tr><td><code>Axilla or Pectoral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chest</code></td><td><code>ncit:C25389</code></td><td></td></tr>
<tr><td><code>Heart, Pericardium</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iliac</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C12748</code></td><td></td></tr>
<tr><td><code>Mesenteric or Hepatis Porta</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Paraaortic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paratracheal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Splenic Hilar or Spleen</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-stageenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stageenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stageenum')">×</button>
<h3><code>StageEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ann Arbor &gt;&gt; Stage 1</code></td><td><code>ncit:C8071</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 2</code></td><td><code>ncit:C8116</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 3</code></td><td><code>ncit:C8129</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 4</code></td><td><code>ncit:C8142</code></td><td></td></tr>
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
<tr><td><code>Mixture of Stem Cells</code></td><td><code>ncit:C168886</code></td><td></td></tr>
<tr><td><code>Peripheral Blood</code></td><td><code>ncit:C15430</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>AHOD0031</code></td><td><code>ncit:C185311</code></td><td></td></tr>
<tr><td><code>AHOD03P1</code></td><td><code>ncit:C185314</code></td><td></td></tr>
<tr><td><code>AHOD0431</code></td><td><code>ncit:C185310</code></td><td></td></tr>
<tr><td><code>AHOD0831</code></td><td><code>ncit:C185308</code></td><td></td></tr>
<tr><td><code>AHOD1221</code></td><td><code>ncit:C185313</code></td><td></td></tr>
<tr><td><code>AHOD1331</code></td><td><code>ncit:C185312</code></td><td></td></tr>
<tr><td><code>HLHR13</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HOD05</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HOD08</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HOD99</code></td><td><code></code></td><td></td></tr>
<tr><td><code>cHOD17</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-studyphaseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-studyphaseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-studyphaseenum')">×</button>
<h3><code>StudyPhaseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Phase 1</code></td><td><code>ncit:C15600</code></td><td></td></tr>
<tr><td><code>Phase 2</code></td><td><code>ncit:C15601</code></td><td></td></tr>
<tr><td><code>Phase 3</code></td><td><code>ncit:C15602</code></td><td></td></tr>
<tr><td><code>Pilot</code></td><td><code>ncit:C15303</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-studytypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-studytypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-studytypeenum')">×</button>
<h3><code>StudyTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Frontline Study</code></td><td><code>ncit:C185306</code></td><td></td></tr>
<tr><td><code>Retrieval</code></td><td><code>ncit:C185307</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-subagentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-subagentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-subagentenum')">×</button>
<h3><code>SubAgentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bendamustine</code></td><td><code>ncit:C73261</code></td><td></td></tr>
<tr><td><code>Bleomycin</code></td><td><code>ncit:C313</code></td><td></td></tr>
<tr><td><code>Brentuximab Vedotin</code></td><td><code>ncit:C66944</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>ncit:C1282</code></td><td></td></tr>
<tr><td><code>Carmustine</code></td><td><code>ncit:C349</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>ncit:C376</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>ncit:C405</code></td><td></td></tr>
<tr><td><code>Cytarabine</code></td><td><code>ncit:C408</code></td><td></td></tr>
<tr><td><code>Dacarbazine</code></td><td><code>ncit:C411</code></td><td></td></tr>
<tr><td><code>Dexamethasone</code></td><td><code>ncit:C422</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>ncit:C456</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>ncit:C491</code></td><td></td></tr>
<tr><td><code>Etoposide Phosphate</code></td><td><code>ncit:C1093</code></td><td></td></tr>
<tr><td><code>Fludarabine</code></td><td><code>ncit:C1094</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>ncit:C66876</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>ncit:C564</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>ncit:C633</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>ncit:C642</code></td><td></td></tr>
<tr><td><code>Nitrogen Mustard</code></td><td><code>ncit:C62056</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>ncit:C68814</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>ncit:C106432</code></td><td></td></tr>
<tr><td><code>Prednisone</code></td><td><code>ncit:C770</code></td><td></td></tr>
<tr><td><code>Procarbazine</code></td><td><code>ncit:C62072</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>ncit:C875</code></td><td></td></tr>
<tr><td><code>Vinblastine</code></td><td><code>ncit:C930</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>ncit:C933</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>ncit:C1275</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>HOD05: Experimental</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-supportivecaredetailenum" class="enum-modal" onclick="closeEnumModal('enum-modal-supportivecaredetailenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-supportivecaredetailenum')">×</button>
<h3><code>SupportiveCareDetailEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Prevention of Adverse Event</code></td><td><code>ncit:C185654</code></td><td></td></tr>
<tr><td><code>Stem Cell Mobilization</code></td><td><code>ncit:C62604</code></td><td></td></tr>
<tr><td><code>Treatment for Adverse Event</code></td><td><code>ncit:C88082</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-timepointenum" class="enum-modal" onclick="closeEnumModal('enum-modal-timepointenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-timepointenum')">×</button>
<h3><code>TimePointEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Baseline</code></td><td><code>ncit:C25213</code></td><td></td></tr>
<tr><td><code>On Treatment</code></td><td><code>ncit:C142170</code></td><td></td></tr>
<tr><td><code>End of Treatment</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Follow-Up Assessment</code></td><td><code>ncit:C168935</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C432234</code></td><td></td></tr>
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
<tr><td><code>Simple Transfusion</code></td><td><code>ncit:C173285</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-toxicitydetailenum" class="enum-modal" onclick="closeEnumModal('enum-modal-toxicitydetailenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-toxicitydetailenum')">×</button>
<h3><code>ToxicityDetailEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Allergic Reaction</code></td><td><code>ncit:C114476</code></td><td></td></tr>
<tr><td><code>Cardiac Toxicity</code></td><td><code>ncit:C27994</code></td><td></td></tr>
<tr><td><code>Endocrine Toxicity</code></td><td><code>ncit:C138163</code></td><td></td></tr>
<tr><td><code>GI Toxicity</code></td><td><code>ncit:C185646</code></td><td></td></tr>
<tr><td><code>Hepatic Toxicity</code></td><td><code>ncit:C185645</code></td><td></td></tr>
<tr><td><code>Infection</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Mucositis</code></td><td><code>ncit:C115965</code></td><td></td></tr>
<tr><td><code>Musculoskeletal Toxicity</code></td><td><code>ncit:C185647</code></td><td></td></tr>
<tr><td><code>Neuropathy</code></td><td><code>ncit:C4731</code></td><td></td></tr>
<tr><td><code>Neutropenia</code></td><td><code>ncit:C80520</code></td><td></td></tr>
<tr><td><code>Psychiatric Toxicity</code></td><td><code>ncit:C185648</code></td><td></td></tr>
<tr><td><code>Pulmonary Toxicity</code></td><td><code>ncit:C177374</code></td><td></td></tr>
<tr><td><code>Rashes</code></td><td><code>ncit:C39594</code></td><td></td></tr>
<tr><td><code>Renal Toxicity</code></td><td><code>ncit:C115459</code></td><td></td></tr>
<tr><td><code>Thrombocytopenia</code></td><td><code>ncit:C3408</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
    "hl": {
      "name": "hl",
      "title": "Hodgkin Lymphoma",
      "description": "The HL view of the PCDC data model represents consensus data modeling by an international group of pediatric Hodgkin lymphoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Hodgkin Lymphoma Data Collaboration (NODAL). It is based on the collective requirements of its contributors."
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
        "age_at_enrollment",
        "study_phase",
        "study_type",
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
    "FamilyMedicalHistory": {
      "slots": [
        "condition_state",
        "family_medical_history_condition",
        "relation"
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
        "condition_state",
        "medical_history_condition",
        "assisted_conception"
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
    "FunctionTest": {
      "slots": [
        "age_at_function_test",
        "function_test",
        "functional_measurement_type",
        "result_text",
        "result_numeric",
        "functional_measurement_result_unit"
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
    "Immunohistochemistry": {
      "slots": [
        "age_at_ihc",
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
        "stage",
        "ann_arbor_mod_ab",
        "ann_arbor_mod_e",
        "ann_arbor_mod_s"
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
        "disease_site",
        "laterality",
        "measurement1",
        "measurement1_axis",
        "measurement2",
        "measurement2_axis",
        "measurement3",
        "measurement3_axis",
        "measurement_unit",
        "bulky_disease",
        "pleural_effusion",
        "pericardial_effusion",
        "bulk_nodal_aggregate",
        "med_ratio",
        "nodular_splenic"
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
        "detection_method",
        "imaging_result",
        "deauville_score",
        "qpet_score",
        "performance_score",
        "presentation_symptoms",
        "presentation_symptoms_status"
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
        "protocol_procedure",
        "non_protocol_timing",
        "procedure_site",
        "extent",
        "number_nodes",
        "number_nodes_numeric",
        "purpose"
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
        "medication_category",
        "supportive_care_detail",
        "route",
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
    "ProtocolTreatmentModifications": {
      "slots": [
        "age_at_modification",
        "modification",
        "modification_basis",
        "reason",
        "toxicity_detail",
        "toxicity_immune",
        "toxicity_infusion",
        "original_agent",
        "sub_agent"
      ],
      "comments": [
        "D4CGNote: One observation/row per MODIFICATION when instantiated."
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
        "non_protocol_timing",
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
        "non_protocol_timing",
        "protocol_sct",
        "sct_type",
        "stem_cell_source",
        "donor_relationship",
        "conditioning_type",
        "cd34_collected"
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
        "product_type",
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
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "response_method",
        "response_category",
        "response",
        "interim_response",
        "pct_change",
        "symptoms_at_response",
        "palpable_nodes",
        "nodular_splenic"
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
        "ae_pathogen",
        "ae_immune",
        "ae_infusion",
        "ae_reported",
        "ae_attribution",
        "ae_expected",
        "ae_tx_mod",
        "ae_hospitalization",
        "ae_medication",
        "ae_intervention_status",
        "ae_pathogen_status",
        "ae_outcome"
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
        "top_code_system",
        "smn_field"
      ],
      "comments": [
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "monitoring"
      }
    },
    "LateEffects": {
      "slots": [
        "age_at_le_eval",
        "le",
        "le_detail",
        "le_sub_detail",
        "le_severity_grade",
        "le_ctcae_version"
      ],
      "comments": [],
      "annotations": {
        "domain": "monitoring"
      }
    },
    "PatientReportedOutcomesMetadata": {
      "slots": [
        "pro_study_id",
        "time_point",
        "pro_measures",
        "pro_measurement_type",
        "raters",
        "eligible_age_lower",
        "eligible_age_upper"
      ],
      "comments": [],
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
    "relation": {
      "slot_uri": "ncit:C21480",
      "range": "RelationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,rb",
        "tier_optional": "fa,hl,ls"
      }
    },
    "ae_expected": {
      "slot_uri": "ncit:C93710",
      "range": "AeExpectedEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "pro_measures": {
      "slot_uri": "ncit:C177377",
      "range": "ProMeasuresEnum",
      "comments": [],
      "annotations": {}
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
    "review_source": {
      "slot_uri": "ncit:C185324",
      "range": "ReviewSourceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
        "tier_optional": "npc,ls"
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
    "measurement3_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "ann_arbor_mod_s": {
      "slot_uri": "ncit:C185484",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "assisted_conception": {
      "slot_uri": "",
      "range": "AssistedConceptionEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "pericardial_effusion": {
      "slot_uri": "ncit:C3319",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "diagnosis_basis": {
      "slot_uri": "",
      "range": "DiagnosisBasisEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "npc"
      }
    },
    "raters": {
      "slot_uri": "ncit:C185700",
      "range": "RatersEnum",
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
    "interim_response": {
      "slot_uri": "ncit:C185657",
      "range": "InterimResponseEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "symptoms_at_response": {
      "slot_uri": "ncit:C25269",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "hl"
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
    "number_nodes": {
      "slot_uri": "ncit:C185516",
      "range": "NumberNodesEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "ae_pathogen_status": {
      "slot_uri": "ncit:C168955",
      "range": "AePathogenStatusEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "measurement2_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
      }
    },
    "imaging_result": {
      "slot_uri": "ncit:C176708",
      "range": "ImagingResultEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "ann_arbor_mod_ab": {
      "slot_uri": "ncit:C181839",
      "range": "AnnArborModAbEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "modification": {
      "slot_uri": "ncit:C185632",
      "range": "ModificationEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "npc"
      }
    },
    "toxicity_infusion": {
      "slot_uri": "ncit:C185649",
      "range": "YesNoEnum",
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
    "ae_medication": {
      "slot_uri": "ncit:C173317",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "time_point": {
      "slot_uri": "ncit:C82576",
      "range": "TimePointEnum",
      "comments": [],
      "annotations": {}
    },
    "ae_tx_mod": {
      "slot_uri": "ncit:C53606",
      "range": "YesNoEnum",
      "comments": [],
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
    "bulky_disease": {
      "slot_uri": "ncit:C38655",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "le_sub_detail": {
      "slot_uri": "ncit:C186352",
      "range": "LeSubDetailEnum",
      "comments": [
        "(hl) ConsortiumNote: If multiple late effect sub-details, include one observation per late effect sub-detail."
      ],
      "annotations": {
        "tier_optional": "hl"
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
    "original_agent": {
      "slot_uri": "ncit:C185650",
      "range": "OriginalAgentEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
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
    "ae_infusion": {
      "slot_uri": "ncit:C185663",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "age_at_ae": {
      "slot_uri": "ncit:C172677",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "sub_agent": {
      "slot_uri": "ncit:C185634",
      "range": "SubAgentEnum",
      "comments": [],
      "annotations": {}
    },
    "smn_field": {
      "slot_uri": "ncit:C175044",
      "range": "SmnFieldEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "pro_study_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "age_at_le_eval": {
      "slot_uri": "ncit:C185670",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "study_phase": {
      "slot_uri": "ncit:C48281",
      "range": "StudyPhaseEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_optional": "npc"
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
    "qpet_score": {
      "slot_uri": "ncit:C185623",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "pleural_effusion": {
      "slot_uri": "ncit:C3331",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "presentation_symptoms_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "hl",
        "tier_optional": "rb"
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
    "ihc_result_unit": {
      "slot_uri": "",
      "range": "IhcResultUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "med_ratio": {
      "slot_uri": "ncit:C185323",
      "range": "decimal",
      "comments": [],
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
    "measurement1_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "le_severity_grade": {
      "slot_uri": "ncit:C186476",
      "range": "LeSeverityGradeEnum",
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
    "top_code_system": {
      "slot_uri": "",
      "range": "TopCodeSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt",
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
    "modification_basis": {
      "slot_uri": "ncit:C93529",
      "range": "ModificationBasisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
      }
    },
    "ae_reported": {
      "slot_uri": "ncit:C185669",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "presentation_symptoms": {
      "slot_uri": "",
      "range": "PresentationSymptomsEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_optional": "rb"
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
    "supportive_care_detail": {
      "slot_uri": "",
      "range": "SupportiveCareDetailEnum",
      "comments": [],
      "annotations": {}
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
    "protocol_sct": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "ae_hospitalization": {
      "slot_uri": "ncit:C83052",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
      }
    },
    "study_type": {
      "slot_uri": "ncit:C142175",
      "range": "StudyTypeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_optional": "npc"
      }
    },
    "toxicity_immune": {
      "slot_uri": "ncit:C63814",
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
    "palpable_nodes": {
      "slot_uri": "ncit:C185660",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "ae_outcome": {
      "slot_uri": "ncit:C49489",
      "range": "AeOutcomeEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "nodular_splenic": {
      "slot_uri": "ncit:C185322",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "biospecimen_container_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "non_protocol_timing": {
      "slot_uri": "ncit:C175038",
      "range": "NonProtocolTimingEnum",
      "comments": [],
      "annotations": {}
    },
    "le_ctcae_version": {
      "slot_uri": "ncit:C185691",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "eligible_age_lower": {
      "slot_uri": "ncit:C185672",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "functional_measurement_result_unit": {
      "slot_uri": "",
      "range": "FunctionalMeasurementResultUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
      }
    },
    "reason": {
      "slot_uri": "ncit:C185636",
      "range": "ReasonEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc"
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
    "age_at_modification": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "le_detail": {
      "slot_uri": "ncit:C185686",
      "range": "LeDetailEnum",
      "comments": [
        "(hl) ConsortiumNote: If multiple late effect details, include one observation per late effect detail."
      ],
      "annotations": {
        "tier_optional": "hl"
      }
    },
    "product_type": {
      "slot_uri": "ncit:C185655",
      "range": "ProductTypeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
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
    "tmp_type": {
      "slot_uri": "ncit:C173057",
      "range": "TmpTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
        "tier_optional": "hl"
      }
    },
    "bulk_nodal_aggregate": {
      "slot_uri": "ncit:C185476",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "le": {
      "slot_uri": "ncit:C4808",
      "range": "LeEnum",
      "comments": [
        "(hl) ConsortiumNote: If multiple late effects, include one observation per late effect."
      ],
      "annotations": {
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
    "measurement2": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
      }
    },
    "deauville_score": {
      "slot_uri": "ncit:C99723",
      "range": "DeauvilleScoreEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "toxicity_detail": {
      "slot_uri": "ncit:C185693",
      "range": "ToxicityDetailEnum",
      "comments": [],
      "annotations": {}
    },
    "ann_arbor_mod_e": {
      "slot_uri": "ncit:C177586",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "protocol_medication": {
      "slot_uri": "ncit:C175038",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
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
    "functional_measurement_type": {
      "slot_uri": "ncit:C185625",
      "range": "FunctionalMeasurementTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "protocol_procedure": {
      "slot_uri": "ncit:C175038",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt"
      }
    },
    "ae_immune": {
      "slot_uri": "ncit:C185661",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl"
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
    "pct_change": {
      "slot_uri": "ncit:C185497",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "age_at_staging": {
      "slot_uri": "ncit:C177359",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "pro_measurement_type": {
      "slot_uri": "ncit:C186353",
      "range": "ProMeasurementTypeEnum",
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
    },
    "number_nodes_numeric": {
      "slot_uri": "ncit:C124446",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
      }
    },
    "eligible_age_upper": {
      "slot_uri": "ncit:C185673",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "purpose": {
      "slot_uri": "ncit:C185526",
      "range": "PurposeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "hl"
      }
    }
  },
  "enums": {
    "StudyPhaseEnum": {
      "permissible_values": {
        "Phase 1": {
          "meaning": "ncit:C15600",
          "comments": []
        },
        "Phase 2": {
          "meaning": "ncit:C15601",
          "comments": []
        },
        "Phase 3": {
          "meaning": "ncit:C15602",
          "comments": []
        },
        "Pilot": {
          "meaning": "ncit:C15303",
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
    "ResponseMethodEnum": {
      "permissible_values": {
        "Bone Marrow Biopsy": {
          "meaning": "ncit:C15193",
          "comments": []
        },
        "Bone Scan": {
          "meaning": "ncit:C17646",
          "comments": []
        },
        "CT": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "Gallium": {
          "meaning": "ncit:C66798",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "PET": {
          "meaning": "ncit:C17007",
          "comments": [
            "(hl) ConsortiumNote: If RESPONSE_CATEGORY is 'overall' and not based on a single response method, RESPONSE_METHOD should be 'Not applicable'"
          ]
        },
        "PET-CT": {
          "meaning": "ncit:C103512",
          "comments": []
        },
        "PET-MRI": {
          "meaning": "ncit:C103514",
          "comments": []
        },
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        },
        "X-ray": {
          "meaning": "ncit:C38101",
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
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Axilla": {
          "meaning": "ncit:C12674",
          "comments": []
        },
        "Axilla or Pectoral": {
          "meaning": "",
          "comments": []
        },
        "Bone, NOS": {
          "meaning": "",
          "comments": []
        },
        "Chest": {
          "meaning": "ncit:C25389",
          "comments": []
        },
        "Heart, Pericardium": {
          "meaning": "",
          "comments": []
        },
        "Iliac": {
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
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Mesenteric or Hepatis Porta": {
          "meaning": "",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Paraaortic": {
          "meaning": "",
          "comments": []
        },
        "Paratracheal": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Splenic Hilar or Spleen": {
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
    "AssistedConceptionEnum": {
      "permissible_values": {
        "In Vitro Fertilization": {
          "meaning": "ncit:C16580",
          "comments": []
        },
        "Intracytoplasmic Sperm Injection": {
          "meaning": "ncit:C185482",
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
    "ImagingResultEnum": {
      "permissible_values": {
        "Equivocal": {
          "meaning": "ncit:C178921",
          "comments": []
        },
        "Negative": {
          "meaning": "ncit:C38757",
          "comments": []
        },
        "Positive": {
          "meaning": "ncit:C38758",
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
        }
      }
    },
    "LaboratoryTestMethodEnum": {
      "permissible_values": {
        "PCR": {
          "meaning": "ncit:C17003",
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
    "TechniqueEnum": {
      "permissible_values": {
        "EBRT, 3D Conformal": {
          "meaning": "ncit:C16035",
          "comments": []
        },
        "EBRT, Intensity-Modulated": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "Beckwith-Wiedemann Syndrome": {
          "meaning": "ncit:C34415",
          "comments": []
        },
        "Celiac Disease": {
          "meaning": "ncit:C26714",
          "comments": []
        },
        "Central Hypoventilation Syndrome": {
          "meaning": "ncit:C98889",
          "comments": []
        },
        "Cleft Lip": {
          "meaning": "ncit:C87175",
          "comments": []
        },
        "Cleft Palate": {
          "meaning": "ncit:C87069",
          "comments": []
        },
        "Clubfoot": {
          "meaning": "ncit:C84641",
          "comments": []
        },
        "Costello Syndrome": {
          "meaning": "ncit:C84652",
          "comments": []
        },
        "Cushing Syndrome": {
          "meaning": "ncit:C2969",
          "comments": []
        },
        "Denys-Drash Syndrome": {
          "meaning": "ncit:C84668",
          "comments": []
        },
        "Diabetes Mellitus (Type I)": {
          "meaning": "ncit:C2986",
          "comments": []
        },
        "Down Syndrome": {
          "meaning": "ncit:C2993",
          "comments": []
        },
        "Gastroschisis": {
          "meaning": "ncit:C84725",
          "comments": []
        },
        "Goodpasture's Syndrome": {
          "meaning": "ncit:C34649",
          "comments": []
        },
        "Gorlin Syndrome": {
          "meaning": "ncit:C2892",
          "comments": []
        },
        "Graves' Disease": {
          "meaning": "ncit:C3071",
          "comments": []
        },
        "Hashimoto's Thyroiditis": {
          "meaning": "ncit:C27191",
          "comments": []
        },
        "Heart Defect": {
          "meaning": "ncit:C168217",
          "comments": []
        },
        "Hemihypertrophy": {
          "meaning": "ncit:C88541",
          "comments": []
        },
        "Hereditary Retinoblastoma": {
          "meaning": "ncit:C8495",
          "comments": []
        },
        "Hirschprung Disease": {
          "meaning": "ncit:C34700",
          "comments": []
        },
        "Inflammatory Bowel Disease": {
          "meaning": "ncit:C3138",
          "comments": []
        },
        "Juvenile Idiopathic Arthritis": {
          "meaning": "ncit:C114357",
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
        "Mixed Connective Tissue Disease": {
          "meaning": "ncit:C84892",
          "comments": []
        },
        "Multiple Sclerosis": {
          "meaning": "ncit:C3243",
          "comments": []
        },
        "Neurofibromatosis Type I": {
          "meaning": "ncit:C143014",
          "comments": []
        },
        "Noonan Syndrome": {
          "meaning": "ncit:C34854",
          "comments": []
        },
        "Psoriasis": {
          "meaning": "ncit:C3346",
          "comments": []
        },
        "Scleroderma": {
          "meaning": "ncit:C26746",
          "comments": []
        },
        "Systemic Lupus Erythematosus": {
          "meaning": "ncit:C3201",
          "comments": []
        },
        "Vitiligo": {
          "meaning": "ncit:C26915",
          "comments": []
        },
        "WAGR Syndrome": {
          "meaning": "ncit:C3718",
          "comments": []
        },
        "Weaver Syndrome": {
          "meaning": "ncit:C125599",
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
    "RatersEnum": {
      "permissible_values": {
        "Subject": {
          "meaning": "ncit:C41189",
          "comments": []
        },
        "Parent/Guardian": {
          "meaning": "ncit:C185701",
          "comments": []
        },
        "Subject + Parent/GuardianParent/Guardian": {
          "meaning": "ncit:C185702",
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
          "meaning": "ncit:C432234",
          "comments": []
        }
      }
    },
    "FunctionTestEnum": {
      "permissible_values": {
        "EKG": {
          "meaning": "ncit:C168186",
          "comments": []
        },
        "Echocardiogram": {
          "meaning": "ncit:C16525",
          "comments": []
        },
        "Pulmonary Function Test": {
          "meaning": "ncit:C38081",
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
        }
      }
    },
    "ModificationEnum": {
      "permissible_values": {
        "Delayed": {
          "meaning": "ncit:C25476",
          "comments": []
        },
        "Discontinued": {
          "meaning": "ncit:C25484",
          "comments": []
        },
        "Dose Reduction": {
          "meaning": "ncit:C49505",
          "comments": []
        },
        "New Agent Addition": {
          "meaning": "ncit:C185633",
          "comments": []
        },
        "Not Given": {
          "meaning": "ncit:C106487",
          "comments": []
        },
        "Substitution": {
          "meaning": "ncit:C54071",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
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
    "LeSubDetailEnum": {
      "permissible_values": {
        "AIN": {
          "meaning": "ncit:C176730",
          "comments": []
        },
        "AKI": {
          "meaning": "ncit:C26808",
          "comments": []
        },
        "Amenorrhea": {
          "meaning": "ncit:C61443",
          "comments": []
        },
        "Asthma": {
          "meaning": "ncit:C28397",
          "comments": []
        },
        "Cardiomyopathy, NOS": {
          "meaning": "ncit:C34830",
          "comments": []
        },
        "Decreased Creatinine Clearance": {
          "meaning": "ncit:C185671",
          "comments": []
        },
        "Decreased GFR": {
          "meaning": "ncit:C78326",
          "comments": []
        },
        "Dilated Cardiomyopathy": {
          "meaning": "ncit:C84673",
          "comments": []
        },
        "Fertility Disorder": {
          "meaning": "ncit:C3836",
          "comments": []
        },
        "Germ Cell Failure, Confirmed": {
          "meaning": "ncit:C185685",
          "comments": []
        },
        "Germ Cell Failure, Suspected": {
          "meaning": "ncit:C185684",
          "comments": []
        },
        "Heart Block": {
          "meaning": "ncit:C50501",
          "comments": []
        },
        "Hyperthyroid": {
          "meaning": "ncit:C3123",
          "comments": [
            "(hl) ConsortiumNote: If multiple late effect sub-details, include one observation per late effect sub-detail."
          ]
        },
        "Hypothyroid": {
          "meaning": "ncit:C26800",
          "comments": []
        },
        "Menstrual Cycle Dysfunction": {
          "meaning": "ncit:C34815",
          "comments": []
        },
        "Motor Neuropathy": {
          "meaning": "ncit:C3500",
          "comments": []
        },
        "Prolonged QT": {
          "meaning": "ncit:C71034",
          "comments": []
        },
        "Pulmonary Fibrosis": {
          "meaning": "ncit:C26869",
          "comments": []
        },
        "Restrictive Cardiomyopathy": {
          "meaning": "ncit:C62798",
          "comments": []
        },
        "Sensory Neuropathy": {
          "meaning": "ncit:C3501",
          "comments": []
        },
        "Supraventricular Tachycardia": {
          "meaning": "ncit:C35061",
          "comments": []
        },
        "Testosterone Deficiency": {
          "meaning": "ncit:C143195",
          "comments": []
        },
        "Thyroid Nodule": {
          "meaning": "ncit:C3415",
          "comments": []
        },
        "Tubular Damage": {
          "meaning": "ncit:C185689",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
    "ReasonEnum": {
      "permissible_values": {
        "Drug Not Available": {
          "meaning": "ncit:C185643",
          "comments": []
        },
        "Hematologic Toxicity": {
          "meaning": "ncit:C15474",
          "comments": []
        },
        "Non-Hematologic Toxicity": {
          "meaning": "ncit:C185641",
          "comments": []
        },
        "Pre-Existing Organ Dysfunction": {
          "meaning": "ncit:C185644",
          "comments": []
        },
        "Scheduling Issues": {
          "meaning": "ncit:C1685642",
          "comments": []
        },
        "Subject Non-Compliance": {
          "meaning": "ncit:C91752",
          "comments": []
        },
        "Surgical Complications": {
          "meaning": "ncit:C164157",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        }
      }
    },
    "LaboratoryTestSpecimenEnum": {
      "permissible_values": {
        "Blood": {
          "meaning": "ncit:C17610",
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
    "TimePointEnum": {
      "permissible_values": {
        "Baseline": {
          "meaning": "ncit:C25213",
          "comments": []
        },
        "On Treatment": {
          "meaning": "ncit:C142170",
          "comments": []
        },
        "End of Treatment": {
          "meaning": "ncit:C168935",
          "comments": []
        },
        "Follow-Up Assessment": {
          "meaning": "ncit:C168935",
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
          "meaning": "ncit:C432234",
          "comments": []
        }
      }
    },
    "AeExpectedEnum": {
      "permissible_values": {
        "Expected": {
          "meaning": "ncit:C41333",
          "comments": []
        },
        "Unexpected": {
          "meaning": "ncit:C41334",
          "comments": []
        }
      }
    },
    "ProductTypeEnum": {
      "permissible_values": {
        "Apheresis": {
          "meaning": "ncit:C15191",
          "comments": []
        },
        "Random": {
          "meaning": "ncit:C60702",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "StudyIdEnum": {
      "permissible_values": {
        "AHOD0031": {
          "meaning": "ncit:C185311",
          "comments": []
        },
        "AHOD03P1": {
          "meaning": "ncit:C185314",
          "comments": []
        },
        "AHOD0431": {
          "meaning": "ncit:C185310",
          "comments": []
        },
        "AHOD0831": {
          "meaning": "ncit:C185308",
          "comments": []
        },
        "AHOD1221": {
          "meaning": "ncit:C185313",
          "comments": []
        },
        "AHOD1331": {
          "meaning": "ncit:C185312",
          "comments": []
        },
        "HLHR13": {
          "meaning": "",
          "comments": []
        },
        "HOD05": {
          "meaning": "",
          "comments": []
        },
        "HOD08": {
          "meaning": "",
          "comments": []
        },
        "HOD99": {
          "meaning": "",
          "comments": []
        },
        "cHOD17": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ToxicityDetailEnum": {
      "permissible_values": {
        "Allergic Reaction": {
          "meaning": "ncit:C114476",
          "comments": []
        },
        "Cardiac Toxicity": {
          "meaning": "ncit:C27994",
          "comments": []
        },
        "Endocrine Toxicity": {
          "meaning": "ncit:C138163",
          "comments": []
        },
        "GI Toxicity": {
          "meaning": "ncit:C185646",
          "comments": []
        },
        "Hepatic Toxicity": {
          "meaning": "ncit:C185645",
          "comments": []
        },
        "Infection": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Mucositis": {
          "meaning": "ncit:C115965",
          "comments": []
        },
        "Musculoskeletal Toxicity": {
          "meaning": "ncit:C185647",
          "comments": []
        },
        "Neuropathy": {
          "meaning": "ncit:C4731",
          "comments": []
        },
        "Neutropenia": {
          "meaning": "ncit:C80520",
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
        "Rashes": {
          "meaning": "ncit:C39594",
          "comments": []
        },
        "Renal Toxicity": {
          "meaning": "ncit:C115459",
          "comments": []
        },
        "Thrombocytopenia": {
          "meaning": "ncit:C3408",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
    "DiagnosisEnum": {
      "permissible_values": {
        "Hodgkin Lymphoma, Classical, NOS": {
          "meaning": "ncit:C9357",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocyte Depletion, NOS": {
          "meaning": "ncit:C9283",
          "comments": []
        },
        "Hodgkin Lymphoma, Nodular Lymphocyte Predominance": {
          "meaning": "ncit:C7258",
          "comments": []
        },
        "Hodgkin lymphoma, Mixed Cellularity, NOS": {
          "meaning": "ncit:C3517",
          "comments": []
        },
        "Hodgkin Lymphoma, NOS": {
          "meaning": "icdo:9650/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nodular Sclerosis, NOS": {
          "meaning": "icdo:9663/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocyte-Rich": {
          "meaning": "icdo:9651/3",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Biopsy": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Bone Scan": {
          "meaning": "ncit:C17646",
          "comments": []
        },
        "CT Scan": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "Gallium Scan": {
          "meaning": "ncit:C38087",
          "comments": []
        },
        "Lymphangiogram": {
          "meaning": "ncit:C16805",
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
        "PET-MRI": {
          "meaning": "ncit:C103514",
          "comments": []
        },
        "Physical Examination": {
          "meaning": "ncit:C20989",
          "comments": []
        },
        "Staging Laparotomy": {
          "meaning": "ncit:C185327",
          "comments": []
        },
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        },
        "X-Ray": {
          "meaning": "ncit:C38101",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "LeEnum": {
      "permissible_values": {
        "Breast Hypoplasia": {
          "meaning": "ncit:C78222",
          "comments": []
        },
        "Cardiovascular Disorder": {
          "meaning": "ncit:C2931",
          "comments": []
        },
        "Dermatologic Disorder": {
          "meaning": "ncit:C3371",
          "comments": []
        },
        "Endocrine Disorder": {
          "meaning": "ncit:C3009",
          "comments": []
        },
        "Fatigue": {
          "meaning": "ncit:C3036",
          "comments": []
        },
        "GI Disorder": {
          "meaning": "ncit:C2990",
          "comments": []
        },
        "Genitourinary Disorder": {
          "meaning": "ncit:C156660",
          "comments": []
        },
        "Immunologic Disorder": {
          "meaning": "ncit:C3507",
          "comments": []
        },
        "Musculoskeletal Disorder": {
          "meaning": "ncit:C107377",
          "comments": []
        },
        "Neurological Disorder": {
          "meaning": "ncit:C26835",
          "comments": []
        },
        "Psychiatric Disorder": {
          "meaning": "ncit:C2893",
          "comments": []
        },
        "Pulmonary Disorder": {
          "meaning": "ncit:C3198",
          "comments": []
        },
        "Xerostomia": {
          "meaning": "ncit:C26917",
          "comments": []
        }
      }
    },
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Axillary Nodes": {
          "meaning": "ncit:C12904",
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
        "Celiac Nodes": {
          "meaning": "ncit:C65166",
          "comments": []
        },
        "Cervical Nodes": {
          "meaning": "ncit:C32298",
          "comments": []
        },
        "Epitrochlear": {
          "meaning": "ncit:C98182",
          "comments": []
        },
        "Hilar Nodes": {
          "meaning": "ncit:C102330",
          "comments": []
        },
        "Iliac Crest": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Infraclavicular Nodes": {
          "meaning": "ncit:C63705",
          "comments": []
        },
        "Inguinal": {
          "meaning": "ncit:C32801",
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
        "Mediastinum": {
          "meaning": "ncit:C12748",
          "comments": []
        },
        "Mesenteric Nodes": {
          "meaning": "ncit:C77641",
          "comments": []
        },
        "Para-Aortic Nodes": {
          "meaning": "ncit:C77643",
          "comments": []
        },
        "Pectoral Nodes": {
          "meaning": "ncit:C120322",
          "comments": []
        },
        "Popliteal Nodes": {
          "meaning": "ncit:C53146",
          "comments": []
        },
        "Preauricular Nodes": {
          "meaning": "ncit:C103429",
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
        "Supraclavicular Nodes": {
          "meaning": "ncit:C12903",
          "comments": []
        },
        "Waldeyer's Ring": {
          "meaning": "ncit:C73468",
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
        "HL": {
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
        }
      }
    },
    "MarkersEnum": {
      "permissible_values": {
        "CD20": {
          "meaning": "ncit:C38896",
          "comments": []
        },
        "CD30": {
          "meaning": "ncit:C38906",
          "comments": []
        },
        "EBER": {
          "meaning": "ncit:C111618",
          "comments": []
        },
        "LMP1": {
          "meaning": "ncit:C18863",
          "comments": []
        }
      }
    },
    "SubgroupNameEnum": {
      "permissible_values": {
        "HOD05: Experimental": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AnnArborModAbEnum": {
      "permissible_values": {
        "Ann Arbor A Symptoms Indicator": {
          "meaning": "ncit:C185483",
          "comments": []
        },
        "Ann Arbor B Symptoms Indicator": {
          "meaning": "ncit:C177585",
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
        "Cardiac Toxicity": {
          "meaning": "ncit:C27994",
          "comments": []
        },
        "Endocrine Toxicity": {
          "meaning": "ncit:C138163",
          "comments": []
        },
        "Fatigue": {
          "meaning": "ncit:C3036",
          "comments": []
        },
        "GI Toxicity": {
          "meaning": "ncit:C185646",
          "comments": []
        },
        "Hepatic Toxicity": {
          "meaning": "ncit:C185645",
          "comments": []
        },
        "Infection": {
          "meaning": "ncit:C128320",
          "comments": []
        },
        "Mucositis": {
          "meaning": "ncit:C115965",
          "comments": []
        },
        "Musculoskeletal Toxicity": {
          "meaning": "ncit:C185647",
          "comments": []
        },
        "Neuropathy": {
          "meaning": "ncit:C4731",
          "comments": []
        },
        "Neutropenia": {
          "meaning": "ncit:C80520",
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
        "Rashes": {
          "meaning": "ncit:C39594",
          "comments": []
        },
        "Renal Toxicity": {
          "meaning": "ncit:C115459",
          "comments": []
        },
        "Thrombocytopenia": {
          "meaning": "ncit:C3408",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "NumberNodesEnum": {
      "permissible_values": {
        "Multiple Lymph Nodes": {
          "meaning": "ncit:C185519",
          "comments": []
        },
        "Single Lymph Node": {
          "meaning": "ncit:C185518",
          "comments": []
        }
      }
    },
    "DeauvilleScoreEnum": {
      "permissible_values": {
        "Score 1": {
          "meaning": "ncit:C99728",
          "comments": []
        },
        "Score 2": {
          "meaning": "ncit:C99747",
          "comments": []
        },
        "Score 3": {
          "meaning": "ncit:C99748",
          "comments": []
        },
        "Score 4": {
          "meaning": "ncit:C99749",
          "comments": []
        },
        "Score 5": {
          "meaning": "ncit:C99750",
          "comments": []
        }
      }
    },
    "LeDetailEnum": {
      "permissible_values": {
        "Acquired Immunodeficiency": {
          "meaning": "ncit:C2851",
          "comments": []
        },
        "Arrhythmia": {
          "meaning": "ncit:C2881",
          "comments": []
        },
        "Arthritis": {
          "meaning": "ncit:C2883",
          "comments": []
        },
        "Atrophy": {
          "meaning": "ncit:C79748",
          "comments": []
        },
        "Autoimmune Reaction": {
          "meaning": "ncit:C16313",
          "comments": []
        },
        "Avascular-Necrosis": {
          "meaning": "ncit:C118385",
          "comments": []
        },
        "Bladder Disorder": {
          "meaning": "ncit:C2900",
          "comments": []
        },
        "Conduction Abnormality": {
          "meaning": "ncit:C78245",
          "comments": []
        },
        "Contraction": {
          "meaning": "ncit:C30085",
          "comments": []
        },
        "Dryness": {
          "meaning": "ncit:C25489",
          "comments": []
        },
        "Esophagitis": {
          "meaning": "ncit:C9224",
          "comments": []
        },
        "GI Adhesions": {
          "meaning": "ncit:C185688",
          "comments": []
        },
        "Gastritis": {
          "meaning": "ncit:C26780",
          "comments": []
        },
        "Gonadal Dysfunction": {
          "meaning": "ncit:C26786",
          "comments": []
        },
        "Hepatic Dysfunction": {
          "meaning": "ncit:C50634",
          "comments": []
        },
        "Hypertension": {
          "meaning": "ncit:C3117",
          "comments": []
        },
        "Musculoskeletal Hypoplasia": {
          "meaning": "ncit:C185696",
          "comments": []
        },
        "Neurocognitive Functions": {
          "meaning": "ncit:C94321",
          "comments": []
        },
        "Neuropathy": {
          "meaning": "ncit:C4731",
          "comments": []
        },
        "Obstructive Lung Disease": {
          "meaning": "ncit:C3199",
          "comments": []
        },
        "Osteopenia": {
          "meaning": "ncit:C50910",
          "comments": []
        },
        "Osteoporosis": {
          "meaning": "ncit:C3298",
          "comments": []
        },
        "Pancreatitis": {
          "meaning": "ncit:C3306",
          "comments": []
        },
        "Pericarditis": {
          "meaning": "ncit:C34915",
          "comments": []
        },
        "Pigment Changes": {
          "meaning": "ncit:C124224",
          "comments": []
        },
        "Reactive Airway Disease": {
          "meaning": "ncit:C113673",
          "comments": []
        },
        "Renal Disorder": {
          "meaning": "ncit:C3149",
          "comments": []
        },
        "Restrictive Lung Disease": {
          "meaning": "ncit:C91762",
          "comments": []
        },
        "Scarring": {
          "meaning": "ncit:C34483",
          "comments": []
        },
        "Scoliosis": {
          "meaning": "ncit:C78603",
          "comments": []
        },
        "Stroke": {
          "meaning": "ncit:C3390",
          "comments": []
        },
        "Telangiectasia": {
          "meaning": "ncit:C28194",
          "comments": []
        },
        "Thyroid Disorder": {
          "meaning": "ncit:C26893",
          "comments": []
        },
        "Valvular Disease": {
          "meaning": "ncit:C45525",
          "comments": []
        },
        "Vascular Disorder": {
          "meaning": "ncit:C35117",
          "comments": []
        },
        "Ventricular Dysfunction": {
          "meaning": "ncit:C111655",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        "Mixture of Stem Cells": {
          "meaning": "ncit:C168886",
          "comments": []
        },
        "Peripheral Blood": {
          "meaning": "ncit:C15430",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "ProMeasuresEnum": {
      "permissible_values": {
        "Fact NTX": {
          "meaning": "ncit:C177378",
          "comments": []
        },
        "PEDPRO-CTCAE": {
          "meaning": "ncit:C186439",
          "comments": []
        },
        "PRO-CTCAE": {
          "meaning": "ncit:C103843",
          "comments": []
        },
        "PROMIS Fatigue Short Form": {
          "meaning": "ncit:C129493",
          "comments": []
        },
        "PROMIS Global": {
          "meaning": "ncit:C103253",
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
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Axilla or Pectoral": {
          "meaning": "",
          "comments": []
        },
        "Axillary Nodes": {
          "meaning": "ncit:C12904",
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
        "Celiac Nodes": {
          "meaning": "ncit:C65166",
          "comments": []
        },
        "Cervical Nodes": {
          "meaning": "ncit:C32298",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Epitrochlear Nodes": {
          "meaning": "ncit:C98182",
          "comments": []
        },
        "Hilar Nodes": {
          "meaning": "ncit:C134731",
          "comments": []
        },
        "Iliac": {
          "meaning": "",
          "comments": []
        },
        "Iliac Crest": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Infraclavicular Nodes": {
          "meaning": "ncit:C63705",
          "comments": []
        },
        "Inguinal Nodes": {
          "meaning": "ncit:C32801",
          "comments": []
        },
        "Inguinal or Femoral Nodes": {
          "meaning": "ncit:C32801",
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
        "Mediastinum": {
          "meaning": "ncit:C6634",
          "comments": []
        },
        "Mesenteric Nodes": {
          "meaning": "ncit:C77641",
          "comments": []
        },
        "Muscle": {
          "meaning": "",
          "comments": []
        },
        "Paraaortic Lymph Node": {
          "meaning": "ncit:C77643",
          "comments": []
        },
        "Pectoral Nodes": {
          "meaning": "ncit:C120322",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": [
            "(ews) ConsortiumNote: Included so that pleural effusions can be reported.",
            "(os) ConsortiumNote: Included so that pleural effusions can be reported."
          ]
        },
        "Popliteal Nodes": {
          "meaning": "ncit:C53146",
          "comments": []
        },
        "Preauricular Lymph Node": {
          "meaning": "ncit:C103429",
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
        "Spleen": {
          "meaning": "ncit:C12432",
          "comments": []
        },
        "Splenic Hilar Nodes": {
          "meaning": "ncit:C33600",
          "comments": []
        },
        "Supraclavicular Nodes": {
          "meaning": "ncit:C12903",
          "comments": []
        },
        "Thyroid": {
          "meaning": "ncit:C12400",
          "comments": []
        },
        "Waldeyer's Ring": {
          "meaning": "ncit:C73468",
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
    "ProMeasurementTypeEnum": {
      "permissible_values": {
        "Health Profile": {
          "meaning": "ncit:C62359",
          "comments": []
        },
        "Health Utility": {
          "meaning": "ncit:C185674",
          "comments": []
        },
        "Symptom Scale": {
          "meaning": "ncit:C124147",
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
          "meaning": "ncit:C432234",
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
    "AeOutcomeEnum": {
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
          "meaning": "ncit:C85257",
          "comments": []
        },
        "Recovered With Sequelae": {
          "meaning": "ncit:C49495",
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
        "Infection, NOS": {
          "meaning": "ncit:C128320",
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
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Bendamustine": {
          "meaning": "ncit:C73261",
          "comments": []
        },
        "Bleomycin": {
          "meaning": "rxcui:1622",
          "comments": []
        },
        "Brentuximab Vedotin": {
          "meaning": "ncit:C66944",
          "comments": []
        },
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "rxcui:40048",
          "comments": []
        },
        "Carmustine": {
          "meaning": "ncit:C349",
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
        "Cytarabine": {
          "meaning": "rxcui:3041",
          "comments": []
        },
        "Dacarbazine": {
          "meaning": "rxcui:3098",
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
        "Erythropoeitin": {
          "meaning": "ncit:C20429",
          "comments": []
        },
        "Etopophos": {
          "meaning": "ncit:C1093",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Filgrastim": {
          "meaning": "ncit:C1474",
          "comments": []
        },
        "Fludarabine": {
          "meaning": "ncit:C1094",
          "comments": []
        },
        "Gabapentin": {
          "meaning": "ncit:C1108",
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
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Morphine": {
          "meaning": "ncit:C62051",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Non-Corticosteroid Immunosuppressive Agent": {
          "meaning": "ncit:C185652",
          "comments": []
        },
        "PEG-filgrastim": {
          "meaning": "ncit:C1854",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
          "comments": []
        },
        "Plerixafor": {
          "meaning": "ncit:C1777",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": [
            "(lt) ConsortiumNote: Supportive Care Agent, Liver Transplant"
          ]
        },
        "Procarbazine": {
          "meaning": "rxcui:8702",
          "comments": []
        },
        "Systemic Corticosteroid": {
          "meaning": "ncit:C122080",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "rxcui:10473",
          "comments": []
        },
        "Thyroid Hormone Replacement": {
          "meaning": "ncit:C888",
          "comments": []
        },
        "Topical Corticosteroid": {
          "meaning": "ncit:C29505",
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
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "NODAL": {
          "meaning": "ncit:C192759",
          "comments": []
        }
      }
    },
    "StudyTypeEnum": {
      "permissible_values": {
        "Frontline Study": {
          "meaning": "ncit:C185306",
          "comments": []
        },
        "Retrieval": {
          "meaning": "ncit:C185307",
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
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "Albumin": {
          "meaning": "ncit:C64431",
          "comments": []
        },
        "Alkaline Phophatase": {
          "meaning": "ncit:C64432",
          "comments": [
            "(fa) ConsortiumNote: Liver Function Test"
          ]
        },
        "CD34": {
          "meaning": "ncit:C102260",
          "comments": []
        },
        "CRP": {
          "meaning": "ncit:C64548",
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
        "Free T4": {
          "meaning": "ncit:C74786",
          "comments": []
        },
        "Hemoglobin": {
          "meaning": "ncit:C64848",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "LDH": {
          "meaning": "ncit:C64855",
          "comments": []
        },
        "Lymphocytes": {
          "meaning": "ncit:C12535",
          "comments": []
        },
        "Monocytes": {
          "meaning": "ncit:C64823",
          "comments": []
        },
        "Myelocyte": {
          "meaning": "ncit:C13115",
          "comments": []
        },
        "Neutrophil Count": {
          "meaning": "ncit:C51950",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Phosphorus": {
          "meaning": "ncit:C47934",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
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
        "Segmented Neutrophils": {
          "meaning": "ncit:C81997",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "TSH": {
          "meaning": "ncit:C64813",
          "comments": []
        },
        "Total T4": {
          "meaning": "ncit:C74794",
          "comments": []
        },
        "Uric Acid": {
          "meaning": "ncit:C62652",
          "comments": []
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
        }
      }
    },
    "PerformanceScoreEnum": {
      "permissible_values": {
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
        }
      }
    },
    "LesionMeasurementAxisEnum": {
      "permissible_values": {
        "Anteroposterior": {
          "meaning": "",
          "comments": []
        },
        "Cranial-Caudal": {
          "meaning": "ncit:C182395",
          "comments": [
            "D4CGNote: This value is synonymous with 'Height'."
          ]
        },
        "Transverse": {
          "meaning": "ncit:C182199",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "AePathogenStatusEnum": {
      "permissible_values": {
        "Confirmed": {
          "meaning": "ncit:C25458",
          "comments": []
        },
        "Suspected": {
          "meaning": "ncit:C71458",
          "comments": []
        }
      }
    },
    "PresentationSymptomsEnum": {
      "permissible_values": {
        "Fever": {
          "meaning": "ncit:C3038",
          "comments": []
        },
        "Night Sweats": {
          "meaning": "ncit:C3279",
          "comments": []
        },
        "Weight Loss": {
          "meaning": "ncit:C55339",
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
        "System NOS >> Very Good Partial Response": {
          "meaning": "ncit:C123618",
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
        "Chemoimmunotherapy": {
          "meaning": "ncit:C94251",
          "comments": []
        },
        "Chemotherapy, NOS": {
          "meaning": "ncit:C15632",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
        },
        "Immunotherapy": {
          "meaning": "ncit:C15262",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
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
        }
      }
    },
    "FunctionalMeasurementTypeEnum": {
      "permissible_values": {
        "Ejection Fraction": {
          "meaning": "ncit:C99524",
          "comments": []
        },
        "FEF at 25-75%": {
          "meaning": "ncit:C119546",
          "comments": []
        },
        "FEV1": {
          "meaning": "ncit:C38084",
          "comments": []
        },
        "FVC": {
          "meaning": "ncit:C111361",
          "comments": []
        },
        "Landolt C": {
          "meaning": "",
          "comments": []
        },
        "QTc": {
          "meaning": "ncit:C100391",
          "comments": []
        },
        "Shortening Fraction": {
          "meaning": "ncit:C38020",
          "comments": []
        },
        "Total Lung Capacity": {
          "meaning": "ncit:C111325",
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
    "SupportiveCareDetailEnum": {
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
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "TmpTypeEnum": {
      "permissible_values": {
        "Simple Transfusion": {
          "meaning": "ncit:C173285",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "ModificationBasisEnum": {
      "permissible_values": {
        "Clinical Indication": {
          "meaning": "ncit:C185637",
          "comments": [
            "(hl) ConsortiumNote: Only fill in Disease Phase, Disease Phase Number, Course, and Course Number if 'AGE_' not known Note: Course Number is grouped within subcategory. I.e. number Induction 1, 2, 3, 4, etc..., Prephase 1, 2, 3, 4, etc..., Maintenance 1,2,3,4,5,6 etc..."
          ]
        },
        "Per Protocol": {
          "meaning": "ncit:C181023",
          "comments": [
            "(pre) ConsortiumNote: If multiple modifications made, include one observation per modification."
          ]
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": [
            "(hl) ConsortiumNote: If multiple modifications made, include one observation per modification."
          ]
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
        "Intrathecal": {
          "meaning": "ncit:C173292",
          "comments": []
        },
        "Oral": {
          "meaning": "",
          "comments": []
        },
        "Parenteral": {
          "meaning": "ncit:C38291",
          "comments": []
        },
        "Systemic": {
          "meaning": "ncit:C173291",
          "comments": []
        }
      }
    },
    "StageEnum": {
      "permissible_values": {
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
        "Brother": {
          "meaning": "ncit:C96570",
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
        "Sister": {
          "meaning": "ncit:C96586",
          "comments": []
        },
        "Son": {
          "meaning": "ncit:C150888",
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
    "OriginalAgentEnum": {
      "permissible_values": {
        "Bendamustine": {
          "meaning": "ncit:C73261",
          "comments": []
        },
        "Bleomycin": {
          "meaning": "ncit:C313",
          "comments": []
        },
        "Brentuximab Vedotin": {
          "meaning": "ncit:C66944",
          "comments": []
        },
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "ncit:C1282",
          "comments": []
        },
        "Carmustine": {
          "meaning": "ncit:C349",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Cyclophosphamide": {
          "meaning": "ncit:C405",
          "comments": []
        },
        "Cytarabine": {
          "meaning": "ncit:C408",
          "comments": []
        },
        "Dacarbazine": {
          "meaning": "ncit:C411",
          "comments": []
        },
        "Dexamethasone": {
          "meaning": "ncit:C422",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "ncit:C456",
          "comments": []
        },
        "Etoposide": {
          "meaning": "ncit:C491",
          "comments": []
        },
        "Etoposide Phosphate": {
          "meaning": "ncit:C1093",
          "comments": []
        },
        "Fludarabine": {
          "meaning": "ncit:C1094",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "ncit:C66876",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "ncit:C564",
          "comments": []
        },
        "Melphalan": {
          "meaning": "ncit:C633",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "ncit:C642",
          "comments": []
        },
        "Nitrogen Mustard": {
          "meaning": "ncit:C62056",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "ncit:C68814",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "ncit:C106432",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": []
        },
        "Procarbazine": {
          "meaning": "ncit:C62072",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "ncit:C875",
          "comments": []
        },
        "Vinblastine": {
          "meaning": "ncit:C930",
          "comments": []
        },
        "Vincristine": {
          "meaning": "ncit:C933",
          "comments": []
        },
        "Vinorelbine": {
          "meaning": "ncit:C1275",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "SubAgentEnum": {
      "permissible_values": {
        "Bendamustine": {
          "meaning": "ncit:C73261",
          "comments": []
        },
        "Bleomycin": {
          "meaning": "ncit:C313",
          "comments": []
        },
        "Brentuximab Vedotin": {
          "meaning": "ncit:C66944",
          "comments": []
        },
        "Busulfan": {
          "meaning": "ncit:C321",
          "comments": []
        },
        "Carboplatin": {
          "meaning": "ncit:C1282",
          "comments": []
        },
        "Carmustine": {
          "meaning": "ncit:C349",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "ncit:C376",
          "comments": []
        },
        "Cyclophosphamide": {
          "meaning": "ncit:C405",
          "comments": []
        },
        "Cytarabine": {
          "meaning": "ncit:C408",
          "comments": []
        },
        "Dacarbazine": {
          "meaning": "ncit:C411",
          "comments": []
        },
        "Dexamethasone": {
          "meaning": "ncit:C422",
          "comments": []
        },
        "Doxorubicin": {
          "meaning": "ncit:C456",
          "comments": []
        },
        "Etoposide": {
          "meaning": "ncit:C491",
          "comments": []
        },
        "Etoposide Phosphate": {
          "meaning": "ncit:C1093",
          "comments": []
        },
        "Fludarabine": {
          "meaning": "ncit:C1094",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "ncit:C66876",
          "comments": []
        },
        "Ifosfamide": {
          "meaning": "ncit:C564",
          "comments": []
        },
        "Melphalan": {
          "meaning": "ncit:C633",
          "comments": []
        },
        "Methotrexate": {
          "meaning": "ncit:C642",
          "comments": []
        },
        "Nitrogen Mustard": {
          "meaning": "ncit:C62056",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "ncit:C68814",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "ncit:C106432",
          "comments": []
        },
        "Prednisone": {
          "meaning": "ncit:C770",
          "comments": []
        },
        "Procarbazine": {
          "meaning": "ncit:C62072",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "ncit:C875",
          "comments": []
        },
        "Vinblastine": {
          "meaning": "ncit:C930",
          "comments": []
        },
        "Vincristine": {
          "meaning": "ncit:C933",
          "comments": []
        },
        "Vinorelbine": {
          "meaning": "ncit:C1275",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "InterimResponseEnum": {
      "permissible_values": {
        "Progressive Disease": {
          "meaning": "ncit:C35571",
          "comments": []
        },
        "Rapid Early Response (Adequate)": {
          "meaning": "ncit:C185658",
          "comments": []
        },
        "Slow Early Response (Inadequate)": {
          "meaning": "ncit:C185659",
          "comments": []
        }
      }
    },
    "EnergyTypeEnum": {
      "permissible_values": {
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
        }
      }
    },
    "AeCodeSystemEnum": {
      "permissible_values": {
        "Balis Neuropathy Scale": {
          "meaning": "ncit:C178081",
          "comments": []
        },
        "CTCAE": {
          "meaning": "ncit:C49704",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "LeSeverityGradeEnum": {
      "permissible_values": {
        "CTCAE >> Grade 1": {
          "meaning": "ncit:C41338",
          "comments": []
        },
        "CTCAE >> Grade 2": {
          "meaning": "ncit:C41339",
          "comments": []
        },
        "CTCAE >> Grade 3": {
          "meaning": "ncit:C41340",
          "comments": []
        },
        "CTCAE >> Grade 4": {
          "meaning": "ncit:C84266",
          "comments": []
        },
        "CTCAE >> Grade 5": {
          "meaning": "ncit:C48275",
          "comments": []
        }
      }
    },
    "PurposeEnum": {
      "permissible_values": {
        "Biopsy of Distant Site for Staging": {
          "meaning": "ncit:C185530",
          "comments": []
        },
        "Diagnostic Biopsy for Possible Recurrence": {
          "meaning": "ncit:C185534",
          "comments": []
        },
        "Initial Diagnostic Procedure": {
          "meaning": "ncit:C185527",
          "comments": []
        },
        "Second Look Surgery to Attempt Total Resection": {
          "meaning": "ncit:C185528",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        "Equivocal": {
          "meaning": "ncit:C178921",
          "comments": []
        },
        "Partial Resection": {
          "meaning": "ncit:C131680",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
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
        "mL": {
          "meaning": "",
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
        "uIU/mL": {
          "meaning": "ncit:C67405",
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