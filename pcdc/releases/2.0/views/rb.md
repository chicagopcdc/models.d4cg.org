---
layout: default
title: Retinoblastoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*RB View*

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
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- **Retinoblastoma**
- [Rhabdomyosarcoma](rms)

</details>

The RB view of the PCDC data model represents consensus data modeling by an international group of pediatric retinoblastoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Global Retinoblastoma Alliance for Children (Global REACH). It is based on the collective requirements of its contributors.


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
| `exam_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-examtypeenum')">ExamTypeEnum</button> |  |
| `age_at_start` | `integer` |  |
| `year_at_start` | `integer` |  |

## FamilyMedicalHistory

| Slot | Range | Description |
|---|---|---|
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `family_medical_history_condition` | `string` |  |
| `relation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-relationenum')">RelationEnum</button> |  |
| `lkss_of_relative` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssofrelativeenum')">LkssOfRelativeEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `family_medical_history_procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-familymedicalhistoryprocedureenum')">FamilyMedicalHistoryProcedureEnum</button> |  |

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `age_at_condition` | `integer` |  |
| `condition_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-activeresolvedenum')">ActiveResolvedEnum</button> |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |
| `condition_other` | `string` |  |

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
| `data_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-datasourceenum')">DataSourceEnum</button> |  |
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
| `disease_group` | `DiseaseGroupEnum` |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |
| `race` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button> |  |
| `race_identification_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceidentificationsourceenum')">RaceIdentificationSourceEnum</button> |  |
| `ethnicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button> |  |
| `country` | `string` |  |

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `age_lost_to_follow_up` | `integer` |  |
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
| `evaluator` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-evaluatorenum')">EvaluatorEnum</button> |  |
| `diagnosis_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosissiteenum')">DiagnosisSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `suspected_referring_diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-suspectedreferringdiagnosisenum')">SuspectedReferringDiagnosisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histologic_features` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologicfeaturesenum')">HistologicFeaturesEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_characteristic` | `integer` |  |
| `disease_characteristics_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasecharacteristicssiteenum')">DiseaseCharacteristicsSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `trilateral_retinoblastoma` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `presentation_symptoms` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentationsymptomsenum')">PresentationSymptomsEnum</button> |  |
| `presentation_symptoms_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `anterior_segment_exam` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anteriorsegmentexamenum')">AnteriorSegmentExamEnum</button> |  |
| `retinal_detachment` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-retinaldetachmentenum')">RetinalDetachmentEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement1_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement2` | `decimal` |  |
| `measurement2_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement3` | `decimal` |  |
| `measurement3_axis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementaxisenum')">LesionMeasurementAxisEnum</button> |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `tumor_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorsizeenum')">TumorSizeEnum</button> |  |
| `extension_tumor_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-extensiontumortypeenum')">ExtensionTumorTypeEnum</button> |  |
| `visual_discrete_tumors` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `number_of_tumors_numeric` | `decimal` |  |
| `tumor_from_fovea` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorfromfoveaenum')">TumorFromFoveaEnum</button> |  |
| `optic_nerve_obscuration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `optic_nerve_obscuration_degree` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-opticnerveobscurationdegreeenum')">OpticNerveObscurationDegreeEnum</button> |  |
| `tumor_from_optic_nerve` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorfromopticnerveenum')">TumorFromOpticNerveEnum</button> |  |
| `fluid_from_tumor` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fluidfromtumorenum')">FluidFromTumorEnum</button> |  |
| `seeds_present` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `seeds_pattern` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-seedspatternenum')">SeedsPatternEnum</button> |  |
| `seeds_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-seedstypeenum')">SeedsTypeEnum</button> |  |
| `seeds_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-seedsclassificationenum')">SeedsClassificationEnum</button> |  |
| `finding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-findingenum')">FindingEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `staging_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagingsiteenum')">StagingSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `stage_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagecategoryenum')">StageCategoryEnum</button> |  |
| `tnm_tumor_t` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmtumortenum')">TnmTumorTEnum</button> |  |
| `tnm_node_n` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmnodenenum')">TnmNodeNEnum</button> |  |
| `tnm_metastasis_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmmetastasismenum')">TnmMetastasisMEnum</button> |  |
| `h_stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hstageenum')">HStageEnum</button> |  |
| `group_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-groupsystemenum')">GroupSystemEnum</button> |  |
| `group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-groupenum')">GroupEnum</button> |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
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
| `session_number` | `integer` |  |
| `route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `administration_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-administrationsiteenum')">AdministrationSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `number_doses` | `decimal` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_intended` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |
| `total_dose_given` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `delivery_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `indication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-indicationenum')">IndicationEnum</button> |  |
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
| `apex_dose` | `decimal` |  |
| `dose_rate_at_apex` | `decimal` |  |
| `rt_completed` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `plaque_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-plaquesizeenum')">PlaqueSizeEnum</button> |  |
| `rad_seeds_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-radseedstypeenum')">RadSeedsTypeEnum</button> |  |
| `rad_seeds_num` | `decimal` |  |
| `plaque_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-plaquesourceenum')">PlaqueSourceEnum</button> |  |
| `plaque_model` | `string` |  |
| `brach_calc_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-brachcalctypeenum')">BrachCalcTypeEnum</button> |  |
| `implant_duration` | `decimal` |  |
| `suture_coordinates` | `string` |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `age_at_sct_harvest` | `integer` |  |
| `stem_cell_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stemcellsourceenum')">StemCellSourceEnum</button> |  |
| `conditioning_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conditioningtypeenum')">ConditioningTypeEnum</button> |  |
| `prior_tbi` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `sct_success` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure_performed` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `laser_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lasertypeenum')">LaserTypeEnum</button> |  |
| `laser_power` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laserpowerenum')">LaserPowerEnum</button> |  |
| `laser_duration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laserdurationenum')">LaserDurationEnum</button> |  |
| `laser_duration_numeric` | `decimal` |  |
| `cryotherapy_freezes` | `integer` |  |
| `freeze_thaw_cycle_number` | `integer` |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aesiteenum')">AeSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `grade_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gradesystemenum')">GradeSystemEnum</button> |  |
| `grade_system_version` | `string` |  |
| `hospitalization` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `hospitalization_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-hospitalizationreasonenum')">HospitalizationReasonEnum</button> |  |
| `hospitalization_reason_other` | `string` |  |

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `response_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsesiteenum')">ResponseSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `response_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsemethodenum')">ResponseMethodEnum</button> |  |
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
| `smn_field` | `SmnFieldEnum` |  |

<div class="domain-heading">Testing</div>

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `source_lab` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sourcelabenum')">SourceLabEnum</button> |  |
| `test_name` | `string` |  |
| `test_version` | `string` |  |
| `cascade_testing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `biological_analyte` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-biologicalanalyteenum')">BiologicalAnalyteEnum</button> |  |
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
| `reported_significance` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reportedsignificanceenum')">ReportedSignificanceEnum</button> |  |
| `copy_number` | `decimal` |  |
| `maf_numeric` | `decimal` |  |
| `vaf_numeric` | `decimal` |  |
| `allelic_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button> |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestmethodenum')">LaboratoryTestMethodEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `result_text` | `string` |  |

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

<div id="enum-modal-administrationsiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-administrationsiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-administrationsiteenum')">×</button>
<h3><code>AdministrationSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>C12401</code></td><td></td></tr>
<tr><td><code>Femoral Artery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-adverseeventenum" class="enum-modal" onclick="closeEnumModal('enum-modal-adverseeventenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-adverseeventenum')">×</button>
<h3><code>AdverseEventEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Anemia</code></td><td><code>ncit:C2869</code></td><td></td></tr>
<tr><td><code>Bone Marrow Hypocellular</code></td><td><code>ncit:C3516</code></td><td></td></tr>
<tr><td><code>Chorioretinal Toxicity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Disseminated Intravascular Coagulation</code></td><td><code>ncit:C2992</code></td><td></td></tr>
<tr><td><code>Embolic CVA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Febrile Neutropenia</code></td><td><code>ncit:C35665</code></td><td></td></tr>
<tr><td><code>Hemolysis</code></td><td><code>ncit:C37965</code></td><td></td></tr>
<tr><td><code>Hemolytic Uremic Syndrome</code></td><td><code>ncit:C75545</code></td><td></td></tr>
<tr><td><code>Leukocytosis</code></td><td><code>ncit:C35524</code></td><td></td></tr>
<tr><td><code>Lymph Node Pain</code></td><td><code>ncit:C78440</code></td><td></td></tr>
<tr><td><code>Spleen Disorder</code></td><td><code>ncit:C35823</code></td><td></td></tr>
<tr><td><code>Thrombosis of Femoral Artery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thrombosis of Ophthalmic Artery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thrombotic Thrombocytopenic Purpura</code></td><td><code>ncit:C78797</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aesiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aesiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aesiteenum')">×</button>
<h3><code>AeSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
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
<tr><td><code>BCOR Deletion</code></td><td><code>ncit:C101091</code></td><td></td></tr>
<tr><td><code>Chromosome 13q Loss</code></td><td><code>ncit:C36497</code></td><td></td></tr>
<tr><td><code>Chromosome 16q Loss</code></td><td><code>ncit:C36515</code></td><td></td></tr>
<tr><td><code>Chromosome 1q Gain</code></td><td><code>ncit:C36482</code></td><td></td></tr>
<tr><td><code>Chromosome 2p Gain</code></td><td><code>ncit:C36439</code></td><td></td></tr>
<tr><td><code>Chromosome 6p Gain</code></td><td><code>ncit:C36633</code></td><td></td></tr>
<tr><td><code>MYCN Amplification</code></td><td><code>ncit:C36673</code></td><td></td></tr>
<tr><td><code>RB1 Allele</code></td><td><code>ncit:C52102</code></td><td></td></tr>
<tr><td><code>Somatic Gene Mutation</code></td><td><code>ncit:C18060</code></td><td></td></tr>
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

<div id="enum-modal-anteriorsegmentexamenum" class="enum-modal" onclick="closeEnumModal('enum-modal-anteriorsegmentexamenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-anteriorsegmentexamenum')">×</button>
<h3><code>AnteriorSegmentExamEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abnormal</code></td><td><code>ncit:C168875</code></td><td></td></tr>
<tr><td><code>Normal</code></td><td><code>ncit:C162623</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-biologicalanalyteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-biologicalanalyteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-biologicalanalyteenum')">×</button>
<h3><code>BiologicalAnalyteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>DNA</code></td><td><code>ncit:C449</code></td><td></td></tr>
<tr><td><code>RNA</code></td><td><code>ncit:C812</code></td><td></td></tr>
<tr><td><code>cfDNA</code></td><td><code>ncit:C128274</code></td><td></td></tr>
<tr><td><code>ctDNA</code></td><td><code>ncit:C113243</code></td><td></td></tr>
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

<div id="enum-modal-brachcalctypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-brachcalctypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-brachcalctypeenum')">×</button>
<h3><code>BrachCalcTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>2D</code></td><td><code></code></td><td></td></tr>
<tr><td><code>3D</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Cardiac Disease</code></td><td><code>ncit:C3079</code></td><td></td></tr>
<tr><td><code>Cardiac Failure</code></td><td><code>ncit:C50577</code></td><td></td></tr>
<tr><td><code>Fungal Infection</code></td><td><code>ncit:C3245</code></td><td></td></tr>
<tr><td><code>Graft Versus Host Disease</code></td><td><code>ncit:C3063</code></td><td></td></tr>
<tr><td><code>Hemorrhage</code></td><td><code>ncit:C26791</code></td><td>(hl) ConsortiumNote: If multiple cause of death details, include one observation per cause of death detail.</td></tr>
<tr><td><code>Immunotherapy-Related</code></td><td><code>ncit:C168874</code></td><td></td></tr>
<tr><td><code>Infection, NOS</code></td><td><code>ncit:C128320</code></td><td></td></tr>
<tr><td><code>Infection, Not Otherwise Specified</code></td><td><code>ncit:C128320</code></td><td></td></tr>
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
<tr><td><code>Global REACH</code></td><td><code>ncit:C192766</code></td><td></td></tr>
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
<tr><td><code>Institutional Study</code></td><td><code>ncit:C41206</code></td><td></td></tr>
<tr><td><code>Registry</code></td><td><code>ncit:C129000</code></td><td>(npc) ConsortiumNotes: For TROD, use Registry only.</td></tr>
<tr><td><code>Therapeutic Trial</code></td><td><code>ncit:C39536</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>B-Scan Ultrasonography</code></td><td><code>ncit:C198675</code></td><td></td></tr>
<tr><td><code>Bone Scan</code></td><td><code>ncit:C17646</code></td><td></td></tr>
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Fluorescein Angiography</code></td><td><code>ncit:C190541</code></td><td></td></tr>
<tr><td><code>Histological Assessment</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Optical Coherence Tomography (OCT)</code></td><td><code>ncit:C20828</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>Ultrasound Biomicroscopy (UBM)</code></td><td><code>ncit:C94186</code></td><td></td></tr>
<tr><td><code>Wide Field Retinal Photography</code></td><td><code></code></td><td></td></tr>
<tr><td><code>cfDNA Analysis</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Clinical Exam</code></td><td><code>ncit:C38060</code></td><td></td></tr>
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
<tr><td><code>Retinoblastoma, NOS</code></td><td><code>icdo:9510/3</code></td><td></td></tr>
<tr><td><code>Retinoma</code></td><td><code>ncit:C66812</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diagnosissiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosissiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosissiteenum')">×</button>
<h3><code>DiagnosisSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diseasecharacteristicssiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diseasecharacteristicssiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diseasecharacteristicssiteenum')">×</button>
<h3><code>DiseaseCharacteristicsSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
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
<tr><td><code>Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Anterior Chamber</code></td><td><code>ncit:C12667</code></td><td></td></tr>
<tr><td><code>Eye, Choroid</code></td><td><code>ncit:C12344</code></td><td></td></tr>
<tr><td><code>Eye, Intra-Retinal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Schlemm's Canal</code></td><td><code>ncit:C32256</code></td><td></td></tr>
<tr><td><code>Eye, Stroma of Iris</code></td><td><code>ncit:C199652</code></td><td></td></tr>
<tr><td><code>Eye, Trabecular Meshwork</code></td><td><code>ncit:C12803</code></td><td></td></tr>
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

<div id="enum-modal-evaluatorenum" class="enum-modal" onclick="closeEnumModal('enum-modal-evaluatorenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-evaluatorenum')">×</button>
<h3><code>EvaluatorEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clinical Non-Pediatrician (General Practitioner, Optometrist)</code></td><td><code>ncit:C132424</code></td><td></td></tr>
<tr><td><code>Ophthalmologist</code></td><td><code>ncit:C17822</code></td><td></td></tr>
<tr><td><code>Pediatrician</code></td><td><code>ncit:C83190</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-examtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-examtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-examtypeenum')">×</button>
<h3><code>ExamTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diagnostic Evaluation, Clinic and/or EUA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subsequent, Clinic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Subsequent, EUA</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-extensiontumortypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-extensiontumortypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-extensiontumortypeenum')">×</button>
<h3><code>ExtensionTumorTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Tumor, Focal</code></td><td><code>ncit:C157425</code></td><td></td></tr>
<tr><td><code>Tumor, NOS</code></td><td><code>ncit:C3262</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-familymedicalhistoryprocedureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-familymedicalhistoryprocedureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-familymedicalhistoryprocedureenum')">×</button>
<h3><code>FamilyMedicalHistoryProcedureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Enucleation of Eye</code></td><td><code>ncit:C198837</code></td><td></td></tr>
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
<tr><td><code>Anterior Segment Tumor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Aseptic Orbital Cellulitis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Buphthalmia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cataract</code></td><td><code>ncit:C26713</code></td><td></td></tr>
<tr><td><code>Decreased Vision</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Glaucoma</code></td><td><code>ncit:C26782</code></td><td></td></tr>
<tr><td><code>Heterochromia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hyphema</code></td><td><code>ncit:C50592</code></td><td></td></tr>
<tr><td><code>Hypopyon</code></td><td><code>ncit:C50593</code></td><td></td></tr>
<tr><td><code>Invasion of Ciliary Body</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leukocoria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>None</code></td><td><code>ncit:C41132</code></td><td></td></tr>
<tr><td><code>Opaque Media</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Orbital Cellulitis</code></td><td><code>ncit:C99000</code></td><td></td></tr>
<tr><td><code>Photoleukocoria</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Proptosis</code></td><td><code>ncit:C87114</code></td><td></td></tr>
<tr><td><code>Rubeosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Strabismus</code></td><td><code>ncit:C35040</code></td><td></td></tr>
<tr><td><code>Tumor in Anterior Chamber</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uveitis</code></td><td><code>ncit:C26909</code></td><td></td></tr>
<tr><td><code>Vitreous Hemorrhage</code></td><td><code>ncit:C50469</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fluidfromtumorenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fluidfromtumorenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fluidfromtumorenum')">×</button>
<h3><code>FluidFromTumorEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;=5mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;5mm</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>cGy</code></td><td><code>ncit:C64693</code></td><td></td></tr>
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
<tr><td><code>Aqueous</code></td><td><code>ncit:C28273</code></td><td></td></tr>
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Buccal Swab</code></td><td><code>ncit:C113747</code></td><td></td></tr>
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

<div id="enum-modal-groupenum" class="enum-modal" onclick="closeEnumModal('enum-modal-groupenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-groupenum')">×</button>
<h3><code>GroupEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ICRB &gt;&gt; Group A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>ICRB &gt;&gt; Group B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>ICRB &gt;&gt; Group C</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>ICRB &gt;&gt; Group D</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>ICRB &gt;&gt; Group E</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>IIRC &gt;&gt; Group A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>IIRC &gt;&gt; Group B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>IIRC &gt;&gt; Group C</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>IIRC &gt;&gt; Group D</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>IIRC &gt;&gt; Group E</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 1A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 1B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 2A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 2B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 3A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 3B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 4A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 4B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 5A</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Reese-Ellsworth &gt;&gt; Group 5B</code></td><td><code></code></td><td>(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-groupsystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-groupsystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-groupsystemenum')">×</button>
<h3><code>GroupSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ICRB</code></td><td><code>ncit:C189851</code></td><td></td></tr>
<tr><td><code>IIRC</code></td><td><code>ncit:C189851</code></td><td></td></tr>
<tr><td><code>Reese-Ellsworth</code></td><td><code>ncit:C123333</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hstageenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hstageenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hstageenum')">×</button>
<h3><code>HStageEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>H0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>H0*</code></td><td><code></code></td><td></td></tr>
<tr><td><code>H1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HX</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Apoptosis</code></td><td><code>ncit:C17557</code></td><td></td></tr>
<tr><td><code>Fleurette</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flexner-Wintersteiner Rosette</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Full Thickness Sclera, into the outer third</code></td><td><code>ncit:C76132</code></td><td></td></tr>
<tr><td><code>Homer-Wright Rosette</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Increased Cell Mitotic Activity</code></td><td><code>ncit:C163732</code></td><td></td></tr>
<tr><td><code>Involvement of Adipose Tissue</code></td><td><code>ncit:C12472</code></td><td></td></tr>
<tr><td><code>Involvement of Anterior Chamber</code></td><td><code>ncit:C12667</code></td><td></td></tr>
<tr><td><code>Involvement of Bone</code></td><td><code>ncit:C8288</code></td><td></td></tr>
<tr><td><code>Involvement of Ciliary Body</code></td><td><code>ncit:C12345</code></td><td></td></tr>
<tr><td><code>Involvement of Conjunctiva</code></td><td><code>ncit:C12341</code></td><td></td></tr>
<tr><td><code>Involvement of Emissary Channels</code></td><td><code>ncit:C112364</code></td><td></td></tr>
<tr><td><code>Involvement of Episclera</code></td><td><code>ncit:C12989</code></td><td></td></tr>
<tr><td><code>Involvement of Extraocular Muscle</code></td><td><code>ncit:C33199</code></td><td></td></tr>
<tr><td><code>Involvement of Iris</code></td><td><code>ncit:C25548</code></td><td></td></tr>
<tr><td><code>Involvement of Meningeal Spaces around Optic Nerve</code></td><td><code>ncit:C33094</code></td><td></td></tr>
<tr><td><code>Involvement of Optic Nerve Cut End</code></td><td><code>ncit:C6769</code></td><td></td></tr>
<tr><td><code>Involvement of Optic Nerve Head, Intra-Laminar</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Involvement of Optic Nerve Head, Posterior-Laminar</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Involvement of Optic Nerve Head, Pre-Laminar</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Involvement of Orbit</code></td><td><code>ncit:C12347</code></td><td></td></tr>
<tr><td><code>Involvement of Peripapillary Choroid</code></td><td><code>ncit:C4562</code></td><td></td></tr>
<tr><td><code>Involvement of Schlemm's Canal</code></td><td><code>ncit:C32256</code></td><td></td></tr>
<tr><td><code>Involvement of Trabecular Meshwork</code></td><td><code>ncit:C12803</code></td><td></td></tr>
<tr><td><code>Invovement of Eyelids</code></td><td><code>ncit:C32679</code></td><td></td></tr>
<tr><td><code>Massive Choroidal Extension, full thickness into the outer third</code></td><td><code>ncit:C76132</code></td><td></td></tr>
<tr><td><code>Massive Choroidal Extension, multiple foci more than 3mm</code></td><td><code>ncit:C121127</code></td><td></td></tr>
<tr><td><code>Massive Choroidal Extension, one focus more than 3mm</code></td><td><code>ncit:C115811</code></td><td></td></tr>
<tr><td><code>Necrosis</code></td><td><code>ncit:C112114</code></td><td></td></tr>
<tr><td><code>Nuclear Moulding</code></td><td><code>ncit:C13361</code></td><td></td></tr>
<tr><td><code>Partial Thickness Sclera, within the inner two-thirds</code></td><td><code>ncit:C201274</code></td><td></td></tr>
<tr><td><code>Pseudo-Rosettes</code></td><td><code>ncit:C186534</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-hospitalizationreasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hospitalizationreasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hospitalizationreasonenum')">×</button>
<h3><code>HospitalizationReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fever</code></td><td><code>ncit:C3038</code></td><td></td></tr>
<tr><td><code>Neutropenia</code></td><td><code>ncit:C80520</code></td><td></td></tr>
<tr><td><code>Platelets Transfusion</code></td><td><code>ncit:C15366</code></td><td></td></tr>
<tr><td><code>Positive Blood Culture</code></td><td><code>ncit:C122437</code></td><td></td></tr>
<tr><td><code>Red Blood Cells Transfusion</code></td><td><code>ncit:C15409</code></td><td></td></tr>
<tr><td><code>Transfusion</code></td><td><code>ncit:C15192</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-indicationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-indicationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-indicationenum')">×</button>
<h3><code>IndicationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Adjuvant for extrascleral disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Adjuvant for positive margin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Consolidation of completely responding metastases</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Consolidation of inadequately responding metastases</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Definitive</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Incidental Exposure</code></td><td><code></code></td><td>(rb) ConsortiumNote: If the patient has existing Brachytherapy observations</td></tr>
<tr><td><code>Salvage</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Malignant Cells</code></td><td><code>ncit:C74660</code></td><td></td></tr>
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
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Tumor</code></td><td><code>ncit:C18009</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laserdurationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laserdurationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laserdurationenum')">×</button>
<h3><code>LaserDurationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Continuous Wave</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Millisecond</code></td><td><code>ncit:C41140</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laserpowerenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laserpowerenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laserpowerenum')">×</button>
<h3><code>LaserPowerEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>High</code></td><td><code>ncit:C177365</code></td><td></td></tr>
<tr><td><code>Low</code></td><td><code>ncit:C177366</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-lasertypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lasertypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lasertypeenum')">×</button>
<h3><code>LaserTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1064 nm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>532 nm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>810 nm</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-lesionmeasurementaxisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lesionmeasurementaxisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lesionmeasurementaxisenum')">×</button>
<h3><code>LesionMeasurementAxisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Base</code></td><td><code>ncit:C92955</code></td><td>D4CGNote: Disease-specific, not a universal axis.</td></tr>
<tr><td><code>Cranial-Caudal</code></td><td><code>ncit:C182395</code></td><td>D4CGNote: This value is synonymous with 'Height'.</td></tr>
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

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3><code>MedicalHistoryConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>13q Syndrome</code></td><td><code>ncit:C98993</code></td><td></td></tr>
<tr><td><code>Autism Spectrum Disorder</code></td><td><code>ncit:C88412</code></td><td></td></tr>
<tr><td><code>Bladder Cancer</code></td><td><code>ncit:C4912</code></td><td></td></tr>
<tr><td><code>Breast Cancer</code></td><td><code>ncit:C4872</code></td><td></td></tr>
<tr><td><code>Down Syndrome</code></td><td><code>ncit:C2993</code></td><td></td></tr>
<tr><td><code>Hemihypertrophy</code></td><td><code>ncit:C88541</code></td><td></td></tr>
<tr><td><code>Liposarcoma</code></td><td><code>ncit:C3194</code></td><td></td></tr>
<tr><td><code>Lung Cancer</code></td><td><code>ncit:C4878</code></td><td></td></tr>
<tr><td><code>Melanoma</code></td><td><code>ncit:C3224</code></td><td></td></tr>
<tr><td><code>Osteosarcoma</code></td><td><code>ncit:C9145</code></td><td></td></tr>
<tr><td><code>Pineal Gland Tumor</code></td><td><code>ncit:C6965</code></td><td></td></tr>
<tr><td><code>Retinoblastoma</code></td><td><code>ncit:C7541</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>ncit:C3359</code></td><td></td></tr>
<tr><td><code>Soft Tissue Sarcoma</code></td><td><code>ncit:C9306</code></td><td></td></tr>
<tr><td><code>Thyroid Cancer</code></td><td><code>ncit:C4815</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>IU</code></td><td><code>ncit:C48579</code></td><td></td></tr>
<tr><td><code>MBq</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Idarubicin</code></td><td><code>rxcui:5650</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Topotecan</code></td><td><code>rxcui:57308</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
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

<div id="enum-modal-opticnerveobscurationdegreeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-opticnerveobscurationdegreeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-opticnerveobscurationdegreeenum')">×</button>
<h3><code>OpticNerveObscurationDegreeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Partial</code></td><td><code>ncit:C25378</code></td><td></td></tr>
<tr><td><code>Total</code></td><td><code>ncit:C25304</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-plaquesizeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-plaquesizeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-plaquesizeenum')">×</button>
<h3><code>PlaqueSizeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>12 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>14 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>16 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>18 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>20 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>22 mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-plaquesourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-plaquesourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-plaquesourceenum')">×</button>
<h3><code>PlaqueSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>COMS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EyePhysics</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-presentationsymptomsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-presentationsymptomsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-presentationsymptomsenum')">×</button>
<h3><code>PresentationSymptomsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Amblyopia (Lazy Eye)</code></td><td><code>ncit:C118764</code></td><td></td></tr>
<tr><td><code>Conjunctivitis (Pink Eye)</code></td><td><code>ncit:C34504</code></td><td></td></tr>
<tr><td><code>Heterochromia (Different Colored Eyes)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leukocoria (Abnormal Glow)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>None</code></td><td><code>ncit:C41132</code></td><td></td></tr>
<tr><td><code>Periorbital Edema (Swelling Around The Eye)</code></td><td><code>ncit:C78530</code></td><td></td></tr>
<tr><td><code>Strabismus (Crossed Eyes)</code></td><td><code>ncit:C35040</code></td><td></td></tr>
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
<tr><td><code>Cryotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enucleation of Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Experimental Procedure</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
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

<div id="enum-modal-raceidentificationsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-raceidentificationsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-raceidentificationsourceenum')">×</button>
<h3><code>RaceIdentificationSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Institution-Identified</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Self-Identified</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-radseedstypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-radseedstypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-radseedstypeenum')">×</button>
<h3><code>RadSeedsTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Iodine-125</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ruthinium-106</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Major Deviation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Physician Decision</code></td><td><code>ncit:C48250</code></td><td></td></tr>
<tr><td><code>Relapse</code></td><td><code>ncit:C38155</code></td><td></td></tr>
<tr><td><code>Study Discontinuation</code></td><td><code>ncit:C142444</code></td><td></td></tr>
<tr><td><code>Subject Non-Compliance</code></td><td><code>ncit:C91752</code></td><td></td></tr>
<tr><td><code>Subject/Guardian Refused Further Treatment</code></td><td><code>ncit:C168934</code></td><td></td></tr>
<tr><td><code>Toxicity</code></td><td><code>ncit:C27990</code></td><td></td></tr>
<tr><td><code>Withdrawal of Consent</code></td><td><code>ncit:C48271</code></td><td></td></tr>
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
<tr><td><code>Brother</code></td><td><code>ncit:C96570</code></td><td></td></tr>
<tr><td><code>Daughter</code></td><td><code>ncit:C150887</code></td><td></td></tr>
<tr><td><code>Father</code></td><td><code>ncit:C96572</code></td><td></td></tr>
<tr><td><code>Mother</code></td><td><code>ncit:C96580</code></td><td></td></tr>
<tr><td><code>Sister</code></td><td><code>ncit:C96586</code></td><td></td></tr>
<tr><td><code>Son</code></td><td><code>ncit:C150888</code></td><td></td></tr>
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
<tr><td><code>Retinal Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sub-Retinal Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vitreous Response</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>RB-RECIST &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RB-RECIST &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RB-RECIST &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RB-RECIST &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>EUA</code></td><td><code>ncit:C40971</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>PET-MRI</code></td><td><code>ncit:C103514</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>X-Ray</code></td><td><code>ncit:C38101</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-responsesiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsesiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsesiteenum')">×</button>
<h3><code>ResponseSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
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
<tr><td><code>RB-RECIST</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-retinaldetachmentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-retinaldetachmentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-retinaldetachmentenum')">×</button>
<h3><code>RetinalDetachmentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>No</code></td><td><code>ncit:C49487</code></td><td></td></tr>
<tr><td><code>Yes, 1 Quadrant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, 2 Quadrants</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, 3 Quadrants</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, 4 Quadrants</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Yes, NOS</code></td><td><code>ncit:C49488</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Intracameral</code></td><td><code>ncit:C64984</code></td><td></td></tr>
<tr><td><code>Intrathecal</code></td><td><code>ncit:C173292</code></td><td></td></tr>
<tr><td><code>Intravenously</code></td><td><code>ncit:C38276</code></td><td></td></tr>
<tr><td><code>Intravitreal</code></td><td><code>ncit:C38280</code></td><td></td></tr>
<tr><td><code>Systemic</code></td><td><code>ncit:C173291</code></td><td></td></tr>
<tr><td><code>Transscleral</code></td><td><code>ncit:C199207</code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Abdominal Wall</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Craniospinal</code></td><td><code>ncit:C84352</code></td><td></td></tr>
<tr><td><code>Exact Volume Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Fovea</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Lens</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Macula</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Optic Disk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Optic Nerve</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eye, Sclera</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Extremity</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Posterior Fossa</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Tumor Bed Plus Margin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper Extremity</code></td><td><code>ncit:C12671</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-seedsclassificationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-seedsclassificationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-seedsclassificationenum')">×</button>
<h3><code>SeedsClassificationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clouds</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dust</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spheres</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-seedspatternenum" class="enum-modal" onclick="closeEnumModal('enum-modal-seedspatternenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-seedspatternenum')">×</button>
<h3><code>SeedsPatternEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diffuse</code></td><td><code>ncit:C14175</code></td><td></td></tr>
<tr><td><code>Focal</code></td><td><code>ncit:C28224</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-seedstypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-seedstypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-seedstypeenum')">×</button>
<h3><code>SeedsTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Subretinal</code></td><td><code>ncit:C189892</code></td><td></td></tr>
<tr><td><code>Vitreous</code></td><td><code>ncit:C189881</code></td><td></td></tr>
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
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Pelvis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Glioblastoma</code></td><td><code>ncit:C3058</code></td><td></td></tr>
<tr><td><code>Leukemia</code></td><td><code>ncit:C3161</code></td><td></td></tr>
<tr><td><code>Low Grade Glioma</code></td><td><code>ncit:C132067</code></td><td></td></tr>
<tr><td><code>Melanoma</code></td><td><code>ncit:C3224</code></td><td></td></tr>
<tr><td><code>Osteosarcoma</code></td><td><code>ncit:C9145</code></td><td></td></tr>
<tr><td><code>Soft Tissue Sarcoma</code></td><td><code>ncit:C9306</code></td><td></td></tr>
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
<tr><td><code>Boston Children's</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sloan Kettering</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Toronto</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Pathological</code></td><td><code>ncit:C28257</code></td><td></td></tr>
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
<tr><td><code>IRSS</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-stagingsiteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-stagingsiteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-stagingsiteenum')">×</button>
<h3><code>StagingSiteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eye</code></td><td><code>ncit:C12401</code></td><td></td></tr>
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
<tr><td><code>APEC14B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0231</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0321</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET0332</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARET12P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHLA Registry</code></td><td><code>ncit:C192782</code></td><td></td></tr>
<tr><td><code>DEPICT Registry</code></td><td><code>ncit:C192784</code></td><td></td></tr>
<tr><td><code>EuRBG Registry</code></td><td><code>ncit:C192785</code></td><td></td></tr>
<tr><td><code>GALOP Registry</code></td><td><code>ncit:C192786</code></td><td></td></tr>
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

<div id="enum-modal-suspectedreferringdiagnosisenum" class="enum-modal" onclick="closeEnumModal('enum-modal-suspectedreferringdiagnosisenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-suspectedreferringdiagnosisenum')">×</button>
<h3><code>SuspectedReferringDiagnosisEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cataract</code></td><td><code>ncit:C26713</code></td><td></td></tr>
<tr><td><code>Coat's Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endophthalmitis</code></td><td><code>ncit:C34586</code></td><td></td></tr>
<tr><td><code>Enucleated Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Normal</code></td><td><code>ncit:C162623</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Persistent Hyperplastic Primary Viterous (PHPV)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Red Eye</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retinoblastoma</code></td><td><code>ncit:C7541</code></td><td></td></tr>
<tr><td><code>Retinopathy of Prematurity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uveitis</code></td><td><code>ncit:C26909</code></td><td></td></tr>
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
<tr><td><code>EBRT, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Passive Scattering</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EBRT, Pencil Beam Scanning</code></td><td><code>ncit:C165502</code></td><td>(npc) ConsortiumNote: ENERGY_TYPE = Proton</td></tr>
<tr><td><code>EBRT, Stereotactic Radiosurgery</code></td><td><code>ncit:C15358</code></td><td></td></tr>
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
<tr><td><code>M1a</code></td><td><code>ncit:C48701</code></td><td></td></tr>
<tr><td><code>M1b</code></td><td><code>ncit:C48702</code></td><td></td></tr>
<tr><td><code>M1c</code></td><td><code>ncit:C48703</code></td><td></td></tr>
<tr><td><code>M1d</code></td><td><code>ncit:C188301</code></td><td></td></tr>
<tr><td><code>M1e</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-tumorfromfoveaenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorfromfoveaenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorfromfoveaenum')">×</button>
<h3><code>TumorFromFoveaEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;1.5mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;=1.5mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tumorfromopticnerveenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorfromopticnerveenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorfromopticnerveenum')">×</button>
<h3><code>TumorFromOpticNerveEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;1.5mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;=1.5mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Touching Optic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tumorsizeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tumorsizeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tumorsizeenum')">×</button>
<h3><code>TumorSizeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>&lt;=3mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;3mm</code></td><td><code></code></td><td></td></tr>
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
    "rb": {
      "name": "rb",
      "title": "Retinoblastoma",
      "description": "The RB view of the PCDC data model represents consensus data modeling by an international group of pediatric retinoblastoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Global Retinoblastoma Alliance for Children (Global REACH). It is based on the collective requirements of its contributors."
    }
  },
  "classes": {
    "Subject": {
      "slots": [
        "consortium",
        "disease_group",
        "sex",
        "race",
        "race_identification_source",
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
        "exam_type",
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
        "age_lost_to_follow_up",
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
        "laterality",
        "family_medical_history_procedure"
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
        "medical_history_condition",
        "condition_other"
      ],
      "comments": [
        "(os) ConsortiumNote: No AOST0331/EURAMOS1 data"
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "LaboratoryTest": {
      "slots": [
        "age_at_lab",
        "laboratory_test",
        "laboratory_test_method",
        "laboratory_test_specimen",
        "result_text"
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
        "source_lab",
        "test_name",
        "test_version",
        "cascade_testing",
        "genetic_analysis_specimen",
        "biological_analyte",
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
        "reported_significance",
        "copy_number",
        "maf_numeric",
        "vaf_numeric",
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
        "evaluator",
        "diagnosis_site",
        "laterality",
        "diagnosis_basis",
        "suspected_referring_diagnosis",
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
        "staging_site",
        "laterality",
        "stage_category",
        "tnm_tumor_t",
        "tnm_node_n",
        "tnm_metastasis_m",
        "h_stage",
        "group_system",
        "group",
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
        "detection_method",
        "site_classification",
        "disease_presence",
        "disease_site",
        "laterality",
        "measurement1",
        "measurement1_axis",
        "measurement2",
        "measurement2_axis",
        "measurement3",
        "measurement3_axis",
        "measurement_unit",
        "tumor_size",
        "extension_tumor_type",
        "visual_discrete_tumors",
        "number_of_tumors_numeric",
        "tumor_from_fovea",
        "optic_nerve_obscuration",
        "optic_nerve_obscuration_degree",
        "tumor_from_optic_nerve",
        "fluid_from_tumor",
        "seeds_present",
        "seeds_pattern",
        "seeds_type",
        "seeds_classification",
        "finding"
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
        "disease_characteristics_site",
        "laterality",
        "detection_method",
        "trilateral_retinoblastoma",
        "presentation_symptoms",
        "presentation_symptoms_status",
        "anterior_segment_exam",
        "retinal_detachment"
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
        "laser_type",
        "laser_power",
        "laser_duration",
        "laser_duration_numeric",
        "cryotherapy_freezes",
        "freeze_thaw_cycle_number"
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
        "session_number",
        "route",
        "medication",
        "administration_site",
        "laterality",
        "number_doses",
        "medication_dose_administered",
        "medication_dose_intended",
        "medication_dose_unit",
        "total_dose_given",
        "delivery_status"
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
        "indication",
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
        "apex_dose",
        "dose_rate_at_apex",
        "rt_completed",
        "plaque_size",
        "rad_seeds_type",
        "rad_seeds_num",
        "plaque_source",
        "plaque_model",
        "brach_calc_type",
        "implant_duration",
        "suture_coordinates"
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
        "stem_cell_source",
        "conditioning_type",
        "prior_tbi",
        "sct_success"
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
        "response_site",
        "laterality",
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
        "age_at_ae_resolved",
        "adverse_event",
        "ae_site",
        "laterality",
        "ae_grade",
        "grade_system",
        "grade_system_version",
        "hospitalization",
        "hospitalization_reason",
        "hospitalization_reason_other"
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
    "smn_type": {
      "slot_uri": "",
      "range": "SmnTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,npc"
      }
    },
    "suspected_referring_diagnosis": {
      "slot_uri": "",
      "range": "SuspectedReferringDiagnosisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "diagnosis_site": {
      "slot_uri": "ncit:C157120",
      "range": "DiagnosisSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "staging_site": {
      "slot_uri": "ncit:C157120",
      "range": "StagingSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "test_name": {
      "slot_uri": "",
      "range": "string",
      "comments": [
        "(rb) ConsortiumNote: OncoKids should be designated in this field."
      ],
      "annotations": {
        "tier_optional": "rb"
      }
    },
    "rt_site": {
      "slot_uri": "ncit:C173281",
      "range": "RtSiteEnum",
      "comments": [],
      "annotations": {}
    },
    "measurement3_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "hospitalization": {
      "slot_uri": "ncit:C83052",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
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
    "route": {
      "slot_uri": "ncit:C186559",
      "range": "RouteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "rt_completed": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "diagnosis_basis": {
      "slot_uri": "",
      "range": "DiagnosisBasisEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "lt,rb",
        "tier_optional": "npc"
      }
    },
    "laser_power": {
      "slot_uri": "",
      "range": "LaserPowerEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "condition_other": {
      "slot_uri": "ncit:C53263",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "lt,rb"
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
    "fluid_from_tumor": {
      "slot_uri": "",
      "range": "FluidFromTumorEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "dose_rate_at_apex": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
      }
    },
    "suture_coordinates": {
      "slot_uri": "",
      "range": "string",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "indication": {
      "slot_uri": "",
      "range": "IndicationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "anterior_segment_exam": {
      "slot_uri": "",
      "range": "AnteriorSegmentExamEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "delivery_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "group": {
      "slot_uri": "",
      "range": "GroupEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "implant_duration": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "plaque_size": {
      "slot_uri": "",
      "range": "PlaqueSizeEnum",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "family_medical_history_procedure": {
      "slot_uri": "ncit:C161601",
      "range": "FamilyMedicalHistoryProcedureEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "h_stage": {
      "slot_uri": "",
      "range": "HStageEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "session_number": {
      "slot_uri": "",
      "range": "integer",
      "comments": [
        "(rb) ConsortiumNote: For RB, this field should be used to designate the intra-arterial chemotherapy session"
      ],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "laser_duration": {
      "slot_uri": "",
      "range": "LaserDurationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "plaque_model": {
      "slot_uri": "",
      "range": "string",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "test_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "trilateral_retinoblastoma": {
      "slot_uri": "ncit:C7019",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "plaque_source": {
      "slot_uri": "",
      "range": "PlaqueSourceEnum",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "age_at_genetic_analysis": {
      "slot_uri": "ncit:C168848",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "extension_tumor_type": {
      "slot_uri": "",
      "range": "ExtensionTumorTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "optic_nerve_obscuration_degree": {
      "slot_uri": "",
      "range": "OpticNerveObscurationDegreeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "retinal_detachment": {
      "slot_uri": "",
      "range": "RetinalDetachmentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "rad_seeds_type": {
      "slot_uri": "",
      "range": "RadSeedsTypeEnum",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "stage_category": {
      "slot_uri": "ncit:C15608",
      "range": "StageCategoryEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "rad_seeds_num": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "group_system": {
      "slot_uri": "",
      "range": "GroupSystemEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "presentation_symptoms_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "hl",
        "tier_optional": "rb"
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
    "evaluator": {
      "slot_uri": "ncit:C51824",
      "range": "EvaluatorEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "measurement1_axis": {
      "slot_uri": "",
      "range": "LesionMeasurementAxisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "seeds_classification": {
      "slot_uri": "",
      "range": "SeedsClassificationEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "visual_discrete_tumors": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "sct_success": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "tumor_from_fovea": {
      "slot_uri": "",
      "range": "TumorFromFoveaEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "cryotherapy_freezes": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "presentation_symptoms": {
      "slot_uri": "",
      "range": "PresentationSymptomsEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
        "tier_optional": "rb"
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
    "biological_analyte": {
      "slot_uri": "",
      "range": "BiologicalAnalyteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "procedure_performed": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "vaf_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "laser_duration_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "optic_nerve_obscuration": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "hospitalization_reason": {
      "slot_uri": "",
      "range": "HospitalizationReasonEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "number_of_tumors_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "apex_dose": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "tumor_from_optic_nerve": {
      "slot_uri": "",
      "range": "TumorFromOpticNerveEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "response_site": {
      "slot_uri": "ncit:C157120",
      "range": "ResponseSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "freeze_thaw_cycle_number": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "laser_type": {
      "slot_uri": "",
      "range": "LaserTypeEnum",
      "comments": [],
      "annotations": {
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
    "ae_site": {
      "slot_uri": "ncit:C157120",
      "range": "AeSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "exam_type": {
      "slot_uri": "",
      "range": "ExamTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "prior_tbi": {
      "slot_uri": "ncit:C15350",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb"
      }
    },
    "race_identification_source": {
      "slot_uri": "",
      "range": "RaceIdentificationSourceEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "hospitalization_reason_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "cascade_testing": {
      "slot_uri": "ncit:C200724",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb"
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
    "age_at_condition": {
      "slot_uri": "ncit:C18772",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
      }
    },
    "seeds_type": {
      "slot_uri": "",
      "range": "SeedsTypeEnum",
      "comments": [
        "(rb) ConsortiumNote: If SEEDS_PRESENT == Yes"
      ],
      "annotations": {
        "tier_priority": "rb"
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
    "disease_characteristics_site": {
      "slot_uri": "ncit:C157120",
      "range": "DiseaseCharacteristicsSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "seeds_present": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "brach_calc_type": {
      "slot_uri": "",
      "range": "BrachCalcTypeEnum",
      "comments": [
        "(rb) ConsortiumNote: Use if TECHNIQUE == 'Brachytherapy'"
      ],
      "annotations": {
        "tier_optional": "rb"
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
    "administration_site": {
      "slot_uri": "",
      "range": "AdministrationSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "seeds_pattern": {
      "slot_uri": "",
      "range": "SeedsPatternEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "total_dose_given": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
        "Major Deviation": {
          "meaning": "",
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
        "Toxicity": {
          "meaning": "ncit:C27990",
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
        "CT Scan": {
          "meaning": "ncit:C17204",
          "comments": []
        },
        "EUA": {
          "meaning": "ncit:C40971",
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
        }
      }
    },
    "RtSiteEnum": {
      "permissible_values": {
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Abdominal Wall": {
          "meaning": "",
          "comments": []
        },
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "",
          "comments": []
        },
        "Craniospinal": {
          "meaning": "ncit:C84352",
          "comments": []
        },
        "Exact Volume Unknown": {
          "meaning": "",
          "comments": []
        },
        "Eye": {
          "meaning": "",
          "comments": []
        },
        "Eye, Fovea": {
          "meaning": "",
          "comments": []
        },
        "Eye, Lens": {
          "meaning": "",
          "comments": []
        },
        "Eye, Macula": {
          "meaning": "",
          "comments": []
        },
        "Eye, Optic Disk": {
          "meaning": "",
          "comments": []
        },
        "Eye, Optic Nerve": {
          "meaning": "",
          "comments": []
        },
        "Eye, Sclera": {
          "meaning": "",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Intrathoracic": {
          "meaning": "",
          "comments": []
        },
        "Lower Extremity": {
          "meaning": "ncit:C12742",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Lymph Nodes": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Posterior Fossa": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C28256",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
          "comments": []
        },
        "Tumor Bed Plus Margin": {
          "meaning": "",
          "comments": []
        },
        "Upper Extremity": {
          "meaning": "ncit:C12671",
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
        "AUC": {
          "meaning": "ncit:C64774",
          "comments": []
        },
        "IU": {
          "meaning": "ncit:C48579",
          "comments": []
        },
        "MBq": {
          "meaning": "",
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
    "StagingSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
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
    "SmnTypeEnum": {
      "permissible_values": {
        "Carcinoma": {
          "meaning": "ncit:C2916",
          "comments": []
        },
        "Glioblastoma": {
          "meaning": "ncit:C3058",
          "comments": []
        },
        "Leukemia": {
          "meaning": "ncit:C3161",
          "comments": []
        },
        "Low Grade Glioma": {
          "meaning": "ncit:C132067",
          "comments": []
        },
        "Melanoma": {
          "meaning": "ncit:C3224",
          "comments": []
        },
        "Osteosarcoma": {
          "meaning": "ncit:C9145",
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
    "FractionDoseUnitEnum": {
      "permissible_values": {
        "CGE": {
          "meaning": "ncit:C128269",
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
    "RaceIdentificationSourceEnum": {
      "permissible_values": {
        "Institution-Identified": {
          "meaning": "",
          "comments": []
        },
        "Self-Identified": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AeSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
          "comments": []
        }
      }
    },
    "HospitalizationReasonEnum": {
      "permissible_values": {
        "Fever": {
          "meaning": "ncit:C3038",
          "comments": []
        },
        "Neutropenia": {
          "meaning": "ncit:C80520",
          "comments": []
        },
        "Platelets Transfusion": {
          "meaning": "ncit:C15366",
          "comments": []
        },
        "Positive Blood Culture": {
          "meaning": "ncit:C122437",
          "comments": []
        },
        "Red Blood Cells Transfusion": {
          "meaning": "ncit:C15409",
          "comments": []
        },
        "Transfusion": {
          "meaning": "ncit:C15192",
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
        "Cytology": {
          "meaning": "ncit:C16491",
          "comments": []
        },
        "Flow Cytometry": {
          "meaning": "ncit:C16585",
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
        "13q Syndrome": {
          "meaning": "ncit:C98993",
          "comments": []
        },
        "Autism Spectrum Disorder": {
          "meaning": "ncit:C88412",
          "comments": []
        },
        "Bladder Cancer": {
          "meaning": "ncit:C4912",
          "comments": []
        },
        "Breast Cancer": {
          "meaning": "ncit:C4872",
          "comments": []
        },
        "Down Syndrome": {
          "meaning": "ncit:C2993",
          "comments": []
        },
        "Hemihypertrophy": {
          "meaning": "ncit:C88541",
          "comments": []
        },
        "Liposarcoma": {
          "meaning": "ncit:C3194",
          "comments": []
        },
        "Lung Cancer": {
          "meaning": "ncit:C4878",
          "comments": []
        },
        "Melanoma": {
          "meaning": "ncit:C3224",
          "comments": []
        },
        "Osteosarcoma": {
          "meaning": "ncit:C9145",
          "comments": []
        },
        "Pineal Gland Tumor": {
          "meaning": "ncit:C6965",
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
        "Soft Tissue Sarcoma": {
          "meaning": "ncit:C9306",
          "comments": []
        },
        "Thyroid Cancer": {
          "meaning": "ncit:C4815",
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
        "Brachytherapy": {
          "meaning": "ncit:C15195",
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
        "EBRT, Stereotactic Radiosurgery": {
          "meaning": "ncit:C15358",
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
        "Pathological": {
          "meaning": "ncit:C28257",
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
    "TumorFromOpticNerveEnum": {
      "permissible_values": {
        "<1.5mm": {
          "meaning": "",
          "comments": []
        },
        ">=1.5mm": {
          "meaning": "",
          "comments": []
        },
        "Touching Optic": {
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
    "DiagnosisBasisEnum": {
      "permissible_values": {
        "Clinical Exam": {
          "meaning": "ncit:C38060",
          "comments": []
        },
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
    "TumorFromFoveaEnum": {
      "permissible_values": {
        "<1.5mm": {
          "meaning": "",
          "comments": []
        },
        ">=1.5mm": {
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
    "OpticNerveObscurationDegreeEnum": {
      "permissible_values": {
        "Partial": {
          "meaning": "ncit:C25378",
          "comments": []
        },
        "Total": {
          "meaning": "ncit:C25304",
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
    "FindingEnum": {
      "permissible_values": {
        "Anterior Segment Tumor": {
          "meaning": "",
          "comments": []
        },
        "Aseptic Orbital Cellulitis": {
          "meaning": "",
          "comments": []
        },
        "Buphthalmia": {
          "meaning": "",
          "comments": []
        },
        "Cataract": {
          "meaning": "ncit:C26713",
          "comments": []
        },
        "Decreased Vision": {
          "meaning": "",
          "comments": []
        },
        "Glaucoma": {
          "meaning": "ncit:C26782",
          "comments": []
        },
        "Heterochromia": {
          "meaning": "",
          "comments": []
        },
        "Hyphema": {
          "meaning": "ncit:C50592",
          "comments": []
        },
        "Hypopyon": {
          "meaning": "ncit:C50593",
          "comments": []
        },
        "Invasion of Ciliary Body": {
          "meaning": "",
          "comments": []
        },
        "Leukocoria": {
          "meaning": "",
          "comments": []
        },
        "None": {
          "meaning": "ncit:C41132",
          "comments": []
        },
        "Opaque Media": {
          "meaning": "",
          "comments": []
        },
        "Orbital Cellulitis": {
          "meaning": "ncit:C99000",
          "comments": []
        },
        "Photoleukocoria": {
          "meaning": "",
          "comments": []
        },
        "Proptosis": {
          "meaning": "ncit:C87114",
          "comments": []
        },
        "Rubeosis": {
          "meaning": "",
          "comments": []
        },
        "Strabismus": {
          "meaning": "ncit:C35040",
          "comments": []
        },
        "Tumor in Anterior Chamber": {
          "meaning": "",
          "comments": []
        },
        "Uveitis": {
          "meaning": "ncit:C26909",
          "comments": []
        },
        "Vitreous Hemorrhage": {
          "meaning": "ncit:C50469",
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
    "SuspectedReferringDiagnosisEnum": {
      "permissible_values": {
        "Cataract": {
          "meaning": "ncit:C26713",
          "comments": []
        },
        "Coat's Disease": {
          "meaning": "",
          "comments": []
        },
        "Endophthalmitis": {
          "meaning": "ncit:C34586",
          "comments": []
        },
        "Enucleated Eye": {
          "meaning": "",
          "comments": []
        },
        "Normal": {
          "meaning": "ncit:C162623",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "Persistent Hyperplastic Primary Viterous (PHPV)": {
          "meaning": "",
          "comments": []
        },
        "Red Eye": {
          "meaning": "",
          "comments": []
        },
        "Retinoblastoma": {
          "meaning": "ncit:C7541",
          "comments": []
        },
        "Retinopathy of Prematurity": {
          "meaning": "",
          "comments": []
        },
        "Uveitis": {
          "meaning": "ncit:C26909",
          "comments": []
        }
      }
    },
    "DataSourceEnum": {
      "permissible_values": {
        "Institutional Study": {
          "meaning": "ncit:C41206",
          "comments": []
        },
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
    "LaboratoryTestSpecimenEnum": {
      "permissible_values": {
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Tumor": {
          "meaning": "ncit:C18009",
          "comments": []
        }
      }
    },
    "HStageEnum": {
      "permissible_values": {
        "H0": {
          "meaning": "",
          "comments": []
        },
        "H0*": {
          "meaning": "",
          "comments": []
        },
        "H1": {
          "meaning": "",
          "comments": []
        },
        "HX": {
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
    "AlterationEnum": {
      "permissible_values": {
        "BCOR Deletion": {
          "meaning": "ncit:C101091",
          "comments": []
        },
        "Chromosome 13q Loss": {
          "meaning": "ncit:C36497",
          "comments": []
        },
        "Chromosome 16q Loss": {
          "meaning": "ncit:C36515",
          "comments": []
        },
        "Chromosome 1q Gain": {
          "meaning": "ncit:C36482",
          "comments": []
        },
        "Chromosome 2p Gain": {
          "meaning": "ncit:C36439",
          "comments": []
        },
        "Chromosome 6p Gain": {
          "meaning": "ncit:C36633",
          "comments": []
        },
        "MYCN Amplification": {
          "meaning": "ncit:C36673",
          "comments": []
        },
        "RB1 Allele": {
          "meaning": "ncit:C52102",
          "comments": []
        },
        "Somatic Gene Mutation": {
          "meaning": "ncit:C18060",
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
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "Pelvis": {
          "meaning": "",
          "comments": []
        },
        "Thorax": {
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
    "StageSystemEnum": {
      "permissible_values": {
        "IRSS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "StudyIdEnum": {
      "permissible_values": {
        "APEC14B1": {
          "meaning": "",
          "comments": []
        },
        "ARET0231": {
          "meaning": "",
          "comments": []
        },
        "ARET0321": {
          "meaning": "",
          "comments": []
        },
        "ARET0331": {
          "meaning": "",
          "comments": []
        },
        "ARET0332": {
          "meaning": "",
          "comments": []
        },
        "ARET12P1": {
          "meaning": "",
          "comments": []
        },
        "CHLA Registry": {
          "meaning": "ncit:C192782",
          "comments": []
        },
        "DEPICT Registry": {
          "meaning": "ncit:C192784",
          "comments": []
        },
        "EuRBG Registry": {
          "meaning": "ncit:C192785",
          "comments": []
        },
        "GALOP Registry": {
          "meaning": "ncit:C192786",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Retinoblastoma, NOS": {
          "meaning": "icdo:9510/3",
          "comments": []
        },
        "Retinoma": {
          "meaning": "ncit:C66812",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "B-Scan Ultrasonography": {
          "meaning": "ncit:C198675",
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
        "Fluorescein Angiography": {
          "meaning": "ncit:C190541",
          "comments": []
        },
        "Histological Assessment": {
          "meaning": "",
          "comments": []
        },
        "MRI": {
          "meaning": "ncit:C16809",
          "comments": []
        },
        "Optical Coherence Tomography (OCT)": {
          "meaning": "ncit:C20828",
          "comments": []
        },
        "PET Scan": {
          "meaning": "ncit:C17007",
          "comments": []
        },
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        },
        "Ultrasound Biomicroscopy (UBM)": {
          "meaning": "ncit:C94186",
          "comments": []
        },
        "Wide Field Retinal Photography": {
          "meaning": "",
          "comments": []
        },
        "cfDNA Analysis": {
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
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
          "comments": []
        }
      }
    },
    "BrachCalcTypeEnum": {
      "permissible_values": {
        "2D": {
          "meaning": "",
          "comments": []
        },
        "3D": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SeedsClassificationEnum": {
      "permissible_values": {
        "Clouds": {
          "meaning": "",
          "comments": []
        },
        "Dust": {
          "meaning": "",
          "comments": []
        },
        "Spheres": {
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
    "PlaqueSourceEnum": {
      "permissible_values": {
        "COMS": {
          "meaning": "",
          "comments": []
        },
        "EyePhysics": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "PlaqueSizeEnum": {
      "permissible_values": {
        "12 mm": {
          "meaning": "",
          "comments": []
        },
        "14 mm": {
          "meaning": "",
          "comments": []
        },
        "16 mm": {
          "meaning": "",
          "comments": []
        },
        "18 mm": {
          "meaning": "",
          "comments": []
        },
        "20 mm": {
          "meaning": "",
          "comments": []
        },
        "22 mm": {
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
    "GroupEnum": {
      "permissible_values": {
        "ICRB >> Group A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "ICRB >> Group B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "ICRB >> Group C": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "ICRB >> Group D": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "ICRB >> Group E": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "IIRC >> Group A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "IIRC >> Group B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "IIRC >> Group C": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "IIRC >> Group D": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "IIRC >> Group E": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'ICRB' or 'IIRC'"
          ]
        },
        "Reese-Ellsworth >> Group 1A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 1B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 2A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 2B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 3A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 3B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 4A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 4B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 5A": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
          ]
        },
        "Reese-Ellsworth >> Group 5B": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: GROUP_SYSTEM = 'Reese Ellsworth'"
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
    "TumorSizeEnum": {
      "permissible_values": {
        "<=3mm": {
          "meaning": "",
          "comments": []
        },
        ">3mm": {
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
    "AdverseEventEnum": {
      "permissible_values": {
        "Anemia": {
          "meaning": "ncit:C2869",
          "comments": []
        },
        "Bone Marrow Hypocellular": {
          "meaning": "ncit:C3516",
          "comments": []
        },
        "Chorioretinal Toxicity": {
          "meaning": "",
          "comments": []
        },
        "Disseminated Intravascular Coagulation": {
          "meaning": "ncit:C2992",
          "comments": []
        },
        "Embolic CVA": {
          "meaning": "",
          "comments": []
        },
        "Febrile Neutropenia": {
          "meaning": "ncit:C35665",
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
        "Leukocytosis": {
          "meaning": "ncit:C35524",
          "comments": []
        },
        "Lymph Node Pain": {
          "meaning": "ncit:C78440",
          "comments": []
        },
        "Spleen Disorder": {
          "meaning": "ncit:C35823",
          "comments": []
        },
        "Thrombosis of Femoral Artery": {
          "meaning": "",
          "comments": []
        },
        "Thrombosis of Ophthalmic Artery": {
          "meaning": "",
          "comments": []
        },
        "Thrombotic Thrombocytopenic Purpura": {
          "meaning": "ncit:C78797",
          "comments": []
        }
      }
    },
    "GeneticAnalysisSpecimenEnum": {
      "permissible_values": {
        "Aqueous": {
          "meaning": "ncit:C28273",
          "comments": []
        },
        "Blood": {
          "meaning": "ncit:C17610",
          "comments": []
        },
        "Buccal Swab": {
          "meaning": "ncit:C113747",
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
    "ExtensionTumorTypeEnum": {
      "permissible_values": {
        "Tumor, Focal": {
          "meaning": "ncit:C157425",
          "comments": []
        },
        "Tumor, NOS": {
          "meaning": "ncit:C3262",
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
    "LaserPowerEnum": {
      "permissible_values": {
        "High": {
          "meaning": "ncit:C177365",
          "comments": []
        },
        "Low": {
          "meaning": "ncit:C177366",
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
    "DiseaseCharacteristicsSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
          "comments": []
        }
      }
    },
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "",
          "comments": []
        },
        "Eye, Anterior Chamber": {
          "meaning": "ncit:C12667",
          "comments": []
        },
        "Eye, Choroid": {
          "meaning": "ncit:C12344",
          "comments": []
        },
        "Eye, Intra-Retinal": {
          "meaning": "",
          "comments": []
        },
        "Eye, Schlemm's Canal": {
          "meaning": "ncit:C32256",
          "comments": []
        },
        "Eye, Stroma of Iris": {
          "meaning": "ncit:C199652",
          "comments": []
        },
        "Eye, Trabecular Meshwork": {
          "meaning": "ncit:C12803",
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
        "M1a": {
          "meaning": "ncit:C48701",
          "comments": []
        },
        "M1b": {
          "meaning": "ncit:C48702",
          "comments": []
        },
        "M1c": {
          "meaning": "ncit:C48703",
          "comments": []
        },
        "M1d": {
          "meaning": "ncit:C188301",
          "comments": []
        },
        "M1e": {
          "meaning": "",
          "comments": []
        },
        "MX": {
          "meaning": "ncit:C48704",
          "comments": []
        }
      }
    },
    "IndicationEnum": {
      "permissible_values": {
        "Adjuvant for extrascleral disease": {
          "meaning": "",
          "comments": []
        },
        "Adjuvant for positive margin": {
          "meaning": "",
          "comments": []
        },
        "Consolidation of completely responding metastases": {
          "meaning": "",
          "comments": []
        },
        "Consolidation of inadequately responding metastases": {
          "meaning": "",
          "comments": []
        },
        "Definitive": {
          "meaning": "",
          "comments": []
        },
        "Incidental Exposure": {
          "meaning": "",
          "comments": [
            "(rb) ConsortiumNote: If the patient has existing Brachytherapy observations"
          ]
        },
        "Salvage": {
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
        "Apoptosis": {
          "meaning": "ncit:C17557",
          "comments": []
        },
        "Fleurette": {
          "meaning": "",
          "comments": []
        },
        "Flexner-Wintersteiner Rosette": {
          "meaning": "",
          "comments": []
        },
        "Full Thickness Sclera, into the outer third": {
          "meaning": "ncit:C76132",
          "comments": []
        },
        "Homer-Wright Rosette": {
          "meaning": "",
          "comments": []
        },
        "Increased Cell Mitotic Activity": {
          "meaning": "ncit:C163732",
          "comments": []
        },
        "Involvement of Adipose Tissue": {
          "meaning": "ncit:C12472",
          "comments": []
        },
        "Involvement of Anterior Chamber": {
          "meaning": "ncit:C12667",
          "comments": []
        },
        "Involvement of Bone": {
          "meaning": "ncit:C8288",
          "comments": []
        },
        "Involvement of Ciliary Body": {
          "meaning": "ncit:C12345",
          "comments": []
        },
        "Involvement of Conjunctiva": {
          "meaning": "ncit:C12341",
          "comments": []
        },
        "Involvement of Emissary Channels": {
          "meaning": "ncit:C112364",
          "comments": []
        },
        "Involvement of Episclera": {
          "meaning": "ncit:C12989",
          "comments": []
        },
        "Involvement of Extraocular Muscle": {
          "meaning": "ncit:C33199",
          "comments": []
        },
        "Involvement of Iris": {
          "meaning": "ncit:C25548",
          "comments": []
        },
        "Involvement of Meningeal Spaces around Optic Nerve": {
          "meaning": "ncit:C33094",
          "comments": []
        },
        "Involvement of Optic Nerve Cut End": {
          "meaning": "ncit:C6769",
          "comments": []
        },
        "Involvement of Optic Nerve Head, Intra-Laminar": {
          "meaning": "ncit:C12761",
          "comments": []
        },
        "Involvement of Optic Nerve Head, Posterior-Laminar": {
          "meaning": "ncit:C12761",
          "comments": []
        },
        "Involvement of Optic Nerve Head, Pre-Laminar": {
          "meaning": "ncit:C12761",
          "comments": []
        },
        "Involvement of Orbit": {
          "meaning": "ncit:C12347",
          "comments": []
        },
        "Involvement of Peripapillary Choroid": {
          "meaning": "ncit:C4562",
          "comments": []
        },
        "Involvement of Schlemm's Canal": {
          "meaning": "ncit:C32256",
          "comments": []
        },
        "Involvement of Trabecular Meshwork": {
          "meaning": "ncit:C12803",
          "comments": []
        },
        "Invovement of Eyelids": {
          "meaning": "ncit:C32679",
          "comments": []
        },
        "Massive Choroidal Extension, full thickness into the outer third": {
          "meaning": "ncit:C76132",
          "comments": []
        },
        "Massive Choroidal Extension, multiple foci more than 3mm": {
          "meaning": "ncit:C121127",
          "comments": []
        },
        "Massive Choroidal Extension, one focus more than 3mm": {
          "meaning": "ncit:C115811",
          "comments": []
        },
        "Necrosis": {
          "meaning": "ncit:C112114",
          "comments": []
        },
        "Nuclear Moulding": {
          "meaning": "ncit:C13361",
          "comments": []
        },
        "Partial Thickness Sclera, within the inner two-thirds": {
          "meaning": "ncit:C201274",
          "comments": []
        },
        "Pseudo-Rosettes": {
          "meaning": "ncit:C186534",
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
    "RetinalDetachmentEnum": {
      "permissible_values": {
        "No": {
          "meaning": "ncit:C49487",
          "comments": []
        },
        "Yes, 1 Quadrant": {
          "meaning": "",
          "comments": []
        },
        "Yes, 2 Quadrants": {
          "meaning": "",
          "comments": []
        },
        "Yes, 3 Quadrants": {
          "meaning": "",
          "comments": []
        },
        "Yes, 4 Quadrants": {
          "meaning": "",
          "comments": []
        },
        "Yes, NOS": {
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
    "LaserDurationEnum": {
      "permissible_values": {
        "Continuous Wave": {
          "meaning": "",
          "comments": []
        },
        "Millisecond": {
          "meaning": "ncit:C41140",
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
        "Boston Children's": {
          "meaning": "",
          "comments": []
        },
        "Sloan Kettering": {
          "meaning": "",
          "comments": []
        },
        "Toronto": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SeedsTypeEnum": {
      "permissible_values": {
        "Subretinal": {
          "meaning": "ncit:C189892",
          "comments": []
        },
        "Vitreous": {
          "meaning": "ncit:C189881",
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
        }
      }
    },
    "AdministrationSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "C12401",
          "comments": []
        },
        "Femoral Artery": {
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
    "MedicationEnum": {
      "permissible_values": {
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
        "Doxorubicin": {
          "meaning": "rxcui:1799303",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Idarubicin": {
          "meaning": "rxcui:5650",
          "comments": []
        },
        "Melphalan": {
          "meaning": "rxcui:6718",
          "comments": []
        },
        "Topotecan": {
          "meaning": "rxcui:57308",
          "comments": []
        },
        "Vincristine": {
          "meaning": "rxcui:11202",
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
    "LaserTypeEnum": {
      "permissible_values": {
        "1064 nm": {
          "meaning": "",
          "comments": []
        },
        "532 nm": {
          "meaning": "",
          "comments": []
        },
        "810 nm": {
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
    "ConsortiumEnum": {
      "permissible_values": {
        "Global REACH": {
          "meaning": "ncit:C192766",
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
    "RadSeedsTypeEnum": {
      "permissible_values": {
        "Iodine-125": {
          "meaning": "",
          "comments": []
        },
        "Ruthinium-106": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LaboratoryTestEnum": {
      "permissible_values": {
        "Malignant Cells": {
          "meaning": "ncit:C74660",
          "comments": []
        }
      }
    },
    "LesionMeasurementAxisEnum": {
      "permissible_values": {
        "Base": {
          "meaning": "ncit:C92955",
          "comments": [
            "D4CGNote: Disease-specific, not a universal axis."
          ]
        },
        "Cranial-Caudal": {
          "meaning": "ncit:C182395",
          "comments": [
            "D4CGNote: This value is synonymous with 'Height'."
          ]
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "PresentationSymptomsEnum": {
      "permissible_values": {
        "Amblyopia (Lazy Eye)": {
          "meaning": "ncit:C118764",
          "comments": []
        },
        "Conjunctivitis (Pink Eye)": {
          "meaning": "ncit:C34504",
          "comments": []
        },
        "Heterochromia (Different Colored Eyes)": {
          "meaning": "",
          "comments": []
        },
        "Leukocoria (Abnormal Glow)": {
          "meaning": "",
          "comments": []
        },
        "None": {
          "meaning": "ncit:C41132",
          "comments": []
        },
        "Periorbital Edema (Swelling Around The Eye)": {
          "meaning": "ncit:C78530",
          "comments": []
        },
        "Strabismus (Crossed Eyes)": {
          "meaning": "ncit:C35040",
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
        "RB-RECIST >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "RB-RECIST >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "RB-RECIST >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "RB-RECIST >> Stable Disease": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "BiologicalAnalyteEnum": {
      "permissible_values": {
        "DNA": {
          "meaning": "ncit:C449",
          "comments": []
        },
        "RNA": {
          "meaning": "ncit:C812",
          "comments": []
        },
        "cfDNA": {
          "meaning": "ncit:C128274",
          "comments": []
        },
        "ctDNA": {
          "meaning": "ncit:C113243",
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
        "Consolidation": {
          "meaning": "ncit:C15679",
          "comments": []
        },
        "Induction": {
          "meaning": "ncit:C158876",
          "comments": []
        },
        "Radiation Therapy": {
          "meaning": "ncit:C15313",
          "comments": [
            "(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'."
          ]
        }
      }
    },
    "ExamTypeEnum": {
      "permissible_values": {
        "Diagnostic Evaluation, Clinic and/or EUA": {
          "meaning": "",
          "comments": []
        },
        "Subsequent, Clinic": {
          "meaning": "",
          "comments": []
        },
        "Subsequent, EUA": {
          "meaning": "",
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
    "DiagnosisSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
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
    "ResponseSystemEnum": {
      "permissible_values": {
        "RB-RECIST": {
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
    "RouteEnum": {
      "permissible_values": {
        "Intraarterial": {
          "meaning": "ncit:C38222",
          "comments": []
        },
        "Intracameral": {
          "meaning": "ncit:C64984",
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
        "Intravitreal": {
          "meaning": "ncit:C38280",
          "comments": []
        },
        "Systemic": {
          "meaning": "ncit:C173291",
          "comments": []
        },
        "Transscleral": {
          "meaning": "ncit:C199207",
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
        }
      }
    },
    "SeedsPatternEnum": {
      "permissible_values": {
        "Diffuse": {
          "meaning": "ncit:C14175",
          "comments": []
        },
        "Focal": {
          "meaning": "ncit:C28224",
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
    "AnteriorSegmentExamEnum": {
      "permissible_values": {
        "Abnormal": {
          "meaning": "ncit:C168875",
          "comments": []
        },
        "Normal": {
          "meaning": "ncit:C162623",
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
    "GroupSystemEnum": {
      "permissible_values": {
        "ICRB": {
          "meaning": "ncit:C189851",
          "comments": []
        },
        "IIRC": {
          "meaning": "ncit:C189851",
          "comments": []
        },
        "Reese-Ellsworth": {
          "meaning": "ncit:C123333",
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
    "EvaluatorEnum": {
      "permissible_values": {
        "Clinical Non-Pediatrician (General Practitioner, Optometrist)": {
          "meaning": "ncit:C132424",
          "comments": []
        },
        "Ophthalmologist": {
          "meaning": "ncit:C17822",
          "comments": []
        },
        "Pediatrician": {
          "meaning": "ncit:C83190",
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
    "FluidFromTumorEnum": {
      "permissible_values": {
        "<=5mm": {
          "meaning": "",
          "comments": []
        },
        ">5mm": {
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
    "ResponseSiteEnum": {
      "permissible_values": {
        "Eye": {
          "meaning": "ncit:C12401",
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
        "Retinal Response": {
          "meaning": "",
          "comments": []
        },
        "Sub-Retinal Response": {
          "meaning": "",
          "comments": []
        },
        "Vitreous Response": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ProcedureEnum": {
      "permissible_values": {
        "Cryotherapy": {
          "meaning": "",
          "comments": []
        },
        "Enucleation of Eye": {
          "meaning": "",
          "comments": []
        },
        "Experimental Procedure": {
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
    "FamilyMedicalHistoryProcedureEnum": {
      "permissible_values": {
        "Enucleation of Eye": {
          "meaning": "ncit:C198837",
          "comments": []
        }
      }
    }
  }
}
```

</div>