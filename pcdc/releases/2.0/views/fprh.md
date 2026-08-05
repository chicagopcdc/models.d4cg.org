---
layout: default
title: Fertility Preservation and Reproductive Health
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*FPRH View*

<details markdown="1">
<summary class="text-delta">Views</summary>

- [PCDC Base](../)
- [Acute Lymphoblastic Leukemia](all)
- [Acute Myeloid Leukemia](aml)
- [Central Nervous System Tumors](cns)
- [Ewing Sarcoma](ews)
- [Fanconi Anemia](fa)
- **Fertility Preservation and Reproductive Health**
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

The FPRH view of the PCDC data model represents consensus data modeling by an international group of oncology-related fertility preservation and reproductive health experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Reproductive Hope Consortium (R-HOPE). It is based on the collective requirements of its contributors.


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

## Consult

| Slot | Range | Description |
|---|---|---|
| `age_at_fertility_consult` | `integer` |  |
| `fertility_consult_eligibility` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fertilityconsulteligibilityenum')">FertilityConsultEligibilityEnum</button> |  |
| `fertility_consult_ineligible_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fertilityconsultineligiblereasonenum')">FertilityConsultIneligibleReasonEnum</button> |  |
| `reason_declined_fertility_consult` | `string` |  |
| `reason_declined_fertility_preservation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasondeclinedfertilitypreservationenum')">ReasonDeclinedFertilityPreservationEnum</button> |  |
| `fertility_consult_who_present` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fertilityconsultwhopresentenum')">FertilityConsultWhoPresentEnum</button> |  |
| `fertility_consult_outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fertilityconsultoutcomeenum')">FertilityConsultOutcomeEnum</button> |  |
| `interpreter_used` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `insurance_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-insurancetypeenum')">InsuranceTypeEnum</button> |  |

## SocialAndBehavioralDeterminantsOfHealth

| Slot | Range | Description |
|---|---|---|
| `age_at_status` | `integer` |  |
| `gender_identity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genderidentityenum')">GenderIdentityEnum</button> |  |
| `exposure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposureenum')">ExposureEnum</button> |  |
| `exposure_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-exposurestatusenum')">ExposureStatusEnum</button> |  |
| `marital_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-maritalstatusenum')">MaritalStatusEnum</button> |  |
| `religion_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-religiontypeenum')">ReligionTypeEnum</button> |  |
| `religion_type_other` | `string` |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `year_at_enrollment` | `integer` |  |
| `data_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-datasourceenum')">DataSourceEnum</button> |  |

## Subject

| Slot | Range | Description |
|---|---|---|
| `consortium` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-consortiumenum')">ConsortiumEnum</button> |  |
| `disease_group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasegroupenum')">DiseaseGroupEnum</button> |  |
| `sex` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button> |  |
| `race` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button> |  |
| `race_other` | `string` |  |
| `ethnicity` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button> |  |
| `country` | `string` |  |

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
| `diagnosis_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosiscategoryenum')">DiagnosisCategoryEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_characteristic` | `integer` |  |
| `gonadotoxic_risk` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-gonadotoxicriskenum')">GonadotoxicRiskEnum</button> |  |
| `gonadotoxic_risk_system` | `string` |  |
| `gonadotoxic_risk_system_version` | `string` |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `site_finding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sitefindingenum')">SiteFindingEnum</button> |  |
| `volume` | `decimal` |  |
| `volume_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-volumeunitenum')">VolumeUnitEnum</button> |  |
| `endometrial_stripe_thickness` | `decimal` |  |
| `endometrial_stripe_thickness_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-endometrialstripethicknessunitenum')">EndometrialStripeThicknessUnitEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Intervention</div>

## FertilityProcedures

| Slot | Range | Description |
|---|---|---|
| `fertility_procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fertilityprocedureenum')">FertilityProcedureEnum</button> |  |
| `procedure_class` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureclassenum')">ProcedureClassEnum</button> |  |
| `tissue_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tissuetypeenum')">TissueTypeEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `transport_media` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-transportmediaenum')">TransportMediaEnum</button> |  |
| `transport_media_other` | `string` |  |
| `cryopreservation_media` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-cryopreservationmediaenum')">CryopreservationMediaEnum</button> |  |
| `cryopreservation_media_other` | `string` |  |
| `freezing_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-freezingmethodenum')">FreezingMethodEnum</button> |  |
| `freezing_method_other` | `string` |  |
| `monitor_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-monitormethodenum')">MonitorMethodEnum</button> |  |
| `retrieval_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-retrievalmethodenum')">RetrievalMethodEnum</button> |  |
| `collection_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `cryopreservation_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `oocyte_collection_attempts` | `integer` |  |
| `oocyte_retrieved_numeric` | `integer` |  |
| `mature_oocytes_numeric` | `integer` |  |
| `oocytes_fertilized_numeric` | `decimal` |  |
| `fertilization_rate` | `decimal` |  |
| `maturity_rate` | `decimal` |  |
| `cryopreserved_embryo_numeric` | `decimal` |  |
| `cryopreserved_oocyte_numeric` | `decimal` |  |
| `embryo_cryopreserved_day` | `integer` |  |
| `embryo_vitrification_stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-embryovitrificationstageenum')">EmbryoVitrificationStageEnum</button> |  |
| `menstrual_phase` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-menstrualphaseenum')">MenstrualPhaseEnum</button> |  |
| `preimplantation_genetic_testing` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `preimplantation_genetic_testing_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-preimplantationgenetictestingtypeenum')">PreimplantationGeneticTestingTypeEnum</button> |  |
| `semen_volume` | `decimal` |  |
| `semen_concentration` | `decimal` |  |
| `semen_motility` | `decimal` |  |
| `semen_morphology` | `decimal` |  |
| `semen_count` | `decimal` |  |
| `semen_motility_count` | `decimal` |  |
| `semen_abnormality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-semenabnormalityenum')">SemenAbnormalityEnum</button> |  |
| `cryopreserved_semen_vials_numeric` | `decimal` |  |
| `semen_cryopreservation_attempts` | `decimal` |  |
| `testicular_tissue_weight_processed` | `integer` |  |
| `testicular_tissue_weight_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcstripsweightunitenum')">OtcStripsWeightUnitEnum</button> |  |
| `testicular_tissue_pieces_cryopreserved` | `integer` |  |
| `testicular_tissue_vials_cryopreserved` | `integer` |  |
| `sperm_present` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `surgeon_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-surgeontypeenum')">SurgeonTypeEnum</button> |  |
| `otc_resection_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcresectiontypeenum')">OtcResectionTypeEnum</button> |  |
| `otc_surgical_technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcsurgicaltechniqueenum')">OtcSurgicalTechniqueEnum</button> |  |
| `otc_conversion_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcconversionreasonenum')">OtcConversionReasonEnum</button> |  |
| `otc_surgical_energy_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcsurgicalenergysourceenum')">OtcSurgicalEnergySourceEnum</button> |  |
| `germ_cells_present_spermatogonia` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `spermatogonia_density` | `decimal` |  |
| `spermatogonia_density_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-spermatogoniadensityunitenum')">SpermatogoniaDensityUnitEnum</button> |  |
| `germ_cells_present_follicles` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `follicle_density` | `decimal` |  |
| `follicle_density_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-follicledensityunitenum')">FollicleDensityUnitEnum</button> |  |
| `ovary_resect_percent` | `decimal` |  |
| `otc_vials_number` | `integer` |  |
| `otc_strips_number` | `integer` |  |
| `otc_strips_weight` | `decimal` |  |
| `otc_strips_weight_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-otcstripsweightunitenum')">OtcStripsWeightUnitEnum</button> |  |
| `menarchal_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-menarchalstatusenum')">MenarchalStatusEnum</button> |  |
| `sexual_maturity_index` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-sexualmaturityindexenum')">SexualMaturityIndexEnum</button> |  |

## Medication

| Slot | Range | Description |
|---|---|---|
| `age_at_medication_start` | `integer` |  |
| `age_at_medication_end` | `integer` |  |
| `route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button> |  |
| `medication` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationenum')">MedicationEnum</button> |  |
| `medication_other` | `string` |  |
| `medication_dose_administered` | `decimal` |  |
| `medication_dose_intended` | `decimal` |  |
| `medication_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicationdoseunitenum')">MedicationDoseUnitEnum</button> |  |
| `lifetime_cumulative_dose` | `decimal` |  |
| `lifetime_cumulative_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lifetimecumulativedoseunitenum')">LifetimeCumulativeDoseUnitEnum</button> |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `administration_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-administrationstatusenum')">AdministrationStatusEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-fractiondoseunitenum')">FractionDoseUnitEnum</button> |  |
| `transposition_organ` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-transpositionorganenum')">TranspositionOrganEnum</button> |  |
| `reporting_level` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reportinglevelenum')">ReportingLevelEnum</button> |  |
| `shielding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## StemCellTransplant

| Slot | Range | Description |
|---|---|---|
| `age_at_sct` | `integer` |  |
| `year_at_sct` | `integer` |  |
| `sct_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
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
| `procedure` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-procedureenum')">ProcedureEnum</button> |  |
| `laterality` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lateralityenum')">LateralityEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `ae_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradeenum')">AeGradeEnum</button> |  |
| `ae_grade_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-aegradesystemenum')">AeGradeSystemEnum</button> |  |

## ReproductiveOutcomes

| Slot | Range | Description |
|---|---|---|
| `age_at_pregnancy` | `integer` |  |
| `gestational_age_end_of_pregnancy_days` | `integer` |  |
| `age_at_pregnancy_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ageatpregnancymethodenum')">AgeAtPregnancyMethodEnum</button> |  |
| `age_precision` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-ageprecisionenum')">AgePrecisionEnum</button> |  |
| `menstrual_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-menstrualstatusenum')">MenstrualStatusEnum</button> |  |
| `pregnancy_attempted` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `pregnancy_achieved` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `pregnancy_person` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-pregnancypersonenum')">PregnancyPersonEnum</button> |  |
| `fertility_tissue_utilized` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `tissue_type_utilized` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tissuetypeutilizedenum')">TissueTypeUtilizedEnum</button> |  |
| `conception_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-conceptiontypeenum')">ConceptionTypeEnum</button> |  |
| `oocyte_or_embryo_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-oocyteorembryosourceenum')">OocyteOrEmbryoSourceEnum</button> |  |
| `sperm_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-spermsourceenum')">SpermSourceEnum</button> |  |
| `oocyte_or_embryo_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-oocyteorembryostateenum')">OocyteOrEmbryoStateEnum</button> |  |
| `sperm_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-oocyteorembryostateenum')">OocyteOrEmbryoStateEnum</button> |  |
| `ectopic_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `plurality` | `integer` |  |
| `pregnancy_outcome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-pregnancyoutcomeenum')">PregnancyOutcomeEnum</button> |  |
| `delivery_route` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-deliveryrouteenum')">DeliveryRouteEnum</button> |  |
| `birth_order` | `integer` |  |
| `birth_weight` | `decimal` |  |
| `birth_weight_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-birthweightunitenum')">BirthWeightUnitEnum</button> |  |

<div class="domain-heading">Testing</div>

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `laboratory_test_specimen_other` | `string` |  |
| `laboratory_result` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratoryresultenum')">LaboratoryResultEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `laboratory_test_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestresultunitenum')">LaboratoryTestResultUnitEnum</button> |  |
| `result_hormone_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## VitalsAndAnthropometrics

| Slot | Range | Description |
|---|---|---|
| `age_at_measurement` | `integer` |  |
| `anthropometric_measurement_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementtypeenum')">AnthropometricMeasurementTypeEnum</button> |  |
| `result_text` | `string` |  |
| `result_numeric` | `decimal` |  |
| `anthropometric_measurement_result_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anthropometricmeasurementresultunitenum')">AnthropometricMeasurementResultUnitEnum</button> |  |

<div id="enum-modal-administrationstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-administrationstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-administrationstatusenum')">×</button>
<h3><code>AdministrationStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Radiation Administered</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Radiation Not Administered</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Bleeding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fever</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pain</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infection</code></td><td><code>ncit:C128320</code></td><td></td></tr>
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
<tr><td><code>Clavien-Dindo, Grade I</code></td><td><code>ncit:C121447</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade II</code></td><td><code>ncit:C121447</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade III</code></td><td><code>ncit:C121449</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade IIIa</code></td><td><code>ncit:C121450</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade IIIb</code></td><td><code>ncit:C121451</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade IV</code></td><td><code>ncit:C121452</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade IVa</code></td><td><code>ncit:C121453</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade IVb</code></td><td><code>ncit:C121454</code></td><td></td></tr>
<tr><td><code>Clavien-Dindo, Grade V</code></td><td><code>ncit:C121455</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-aegradesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-aegradesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-aegradesystemenum')">×</button>
<h3><code>AeGradeSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Clavien-Dindo Classification</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-ageatpregnancymethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ageatpregnancymethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ageatpregnancymethodenum')">×</button>
<h3><code>AgeAtPregnancyMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Last Menstrual Period</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Day of Implantation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ultrasound Dating</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unspecified Method</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

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
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-birthweightunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-birthweightunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-birthweightunitenum')">×</button>
<h3><code>BirthWeightUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>g</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-conceptiontypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-conceptiontypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-conceptiontypeenum')">×</button>
<h3><code>ConceptionTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Artifical Insemination</code></td><td><code>ncit:C16739</code></td><td></td></tr>
<tr><td><code>In Vitro Fertilization, Conventional</code></td><td><code>ncit:C16580</code></td><td></td></tr>
<tr><td><code>In Vitro Fertilization, Intracytoplasmic Sperm Injection</code></td><td><code>ncit:C185482</code></td><td></td></tr>
<tr><td><code>Egg Donor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovulation Induction</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-assisted</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>RHOPE</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Consolidation</code></td><td><code>ncit:C15679</code></td><td></td></tr>
<tr><td><code>Fertility Preservation Therapy</code></td><td><code>ncit:C71326</code></td><td></td></tr>
<tr><td><code>Fertility Utilization</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Induction</code></td><td><code>ncit:C158876</code></td><td></td></tr>
<tr><td><code>Maintenance</code></td><td><code>ncit:C15688</code></td><td>(ews) ConsortiumNote: In EE99, we did not differenciate maintenance and consolidation courses. They will be all coded as consolidation courses.</td></tr>
<tr><td><code>Radiation Therapy</code></td><td><code>ncit:C15313</code></td><td>(npc) ConsortiumNote: Only when DISEASE_PHASE = 'Relapse'.</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-cryopreservationmediaenum" class="enum-modal" onclick="closeEnumModal('enum-modal-cryopreservationmediaenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-cryopreservationmediaenum')">×</button>
<h3><code>CryopreservationMediaEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cooper Surgical (SAGE OFC Cryomedia)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Modified human tubal fluid 5% DMSO 5% SSS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-deliveryrouteenum" class="enum-modal" onclick="closeEnumModal('enum-modal-deliveryrouteenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-deliveryrouteenum')">×</button>
<h3><code>DeliveryRouteEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Vaginal Delivery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cesarean Section</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
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
<tr><td><code>Carcinoma In Situ</code></td><td><code>icdo:8010/2</code></td><td></td></tr>
<tr><td><code>Ependymoma</code></td><td><code>icdo:9391/3</code></td><td>(cns) ConsortiumNote: Includes ependymal tumors</td></tr>
<tr><td><code>Carcinoma</code></td><td><code>icdo:8010/3</code></td><td></td></tr>
<tr><td><code>Large Cell Carcinoma</code></td><td><code>icdo:8012/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, Undifferentiated Type</code></td><td><code>icdo:8020/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, Anaplastic Type</code></td><td><code>icdo:8021/3</code></td><td></td></tr>
<tr><td><code>Papillary carcinoma</code></td><td><code>icdo:8050/3</code></td><td></td></tr>
<tr><td><code>Verrucous carcinoma</code></td><td><code>icdo:8051/3</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma in situ</code></td><td><code>icdo:8070/2</code></td><td></td></tr>
<tr><td><code>Squamous cell carcinoma</code></td><td><code>icdo:8070/3</code></td><td></td></tr>
<tr><td><code>Sq. cell carcinoma, keratinizing</code></td><td><code>icdo:8071/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma</code></td><td><code>icdo:8140/3</code></td><td></td></tr>
<tr><td><code>Papillary adenocarcinoma</code></td><td><code>icdo:8260/3</code></td><td></td></tr>
<tr><td><code>Malignant melanoma</code></td><td><code>icdo:8720/3</code></td><td></td></tr>
<tr><td><code>Spindle cell melanoma</code></td><td><code>icdo:8772/3</code></td><td></td></tr>
<tr><td><code>Mixed tumor, malignant</code></td><td><code>icdo:8940/3</code></td><td></td></tr>
<tr><td><code>Marginal zone B-cell lymphoma</code></td><td><code>icdo:9699/3</code></td><td></td></tr>
<tr><td><code>Metaplastic carcinoma</code></td><td><code>icdo:8575/3</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma</code></td><td><code>icdo:8900/3</code></td><td></td></tr>
<tr><td><code>Malignant lymphoma</code></td><td><code>icdo:9590/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma</code></td><td><code>icdo:9650/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, mixed cellularity</code></td><td><code>icdo:9652/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, lymphocytic deplet.</code></td><td><code>icdo:9653/3</code></td><td></td></tr>
<tr><td><code>Hodgkin lymphoma, nodular sclerosis</code></td><td><code>icdo:9663/3</code></td><td></td></tr>
<tr><td><code>ML, small B lymphocytic</code></td><td><code>icdo:9670/3</code></td><td></td></tr>
<tr><td><code>ML, large B-cell, diffuse, immunoblastic</code></td><td><code>icdo:9684/3</code></td><td></td></tr>
<tr><td><code>Burkitt lymphoma</code></td><td><code>icdo:9687/3</code></td><td></td></tr>
<tr><td><code>Follicular lymphoma</code></td><td><code>icdo:9690/3</code></td><td></td></tr>
<tr><td><code>Mature T-cell lymphoma</code></td><td><code>icdo:9702/3</code></td><td></td></tr>
<tr><td><code>Precursor cell lymphoblastic lymphoma</code></td><td><code>icdo:9727/3</code></td><td></td></tr>
<tr><td><code>Plasmacytoma</code></td><td><code>icdo:9731/3</code></td><td></td></tr>
<tr><td><code>Langerhans cell histiocytosis</code></td><td><code>icdo:9751/3</code></td><td></td></tr>
<tr><td><code>B lymphoblastic leukemia/lymphoma</code></td><td><code>icdo:9811/3</code></td><td></td></tr>
<tr><td><code>Clear cell adenocarcinoma</code></td><td><code>icdo:8310/3</code></td><td></td></tr>
<tr><td><code>Cystadenocarcinoma</code></td><td><code>icdo:8440/3</code></td><td></td></tr>
<tr><td><code>Fibrosarcoma</code></td><td><code>icdo:8810/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma</code></td><td><code>icdo:8980/3</code></td><td></td></tr>
<tr><td><code>Solid carcinoma</code></td><td><code>icdo:8230/3</code></td><td></td></tr>
<tr><td><code>Sarcoma</code></td><td><code>icdo:8800/3</code></td><td></td></tr>
<tr><td><code>Liposarcoma</code></td><td><code>icdo:8850/3</code></td><td></td></tr>
<tr><td><code>Leiomyosarcoma</code></td><td><code>icdo:8890/3</code></td><td></td></tr>
<tr><td><code>Transitional Cell Carcinoma</code></td><td><code>icdo:8120/3</code></td><td></td></tr>
<tr><td><code>Small Cell Carcinoma</code></td><td><code>icdo:8041/3</code></td><td></td></tr>
<tr><td><code>Embryonal Carcinoma</code></td><td><code>icdo:9070/3</code></td><td></td></tr>
<tr><td><code>Chordoma</code></td><td><code>icdo:9370/3</code></td><td></td></tr>
<tr><td><code>Medullary Carcinoma</code></td><td><code>icdo:8510/3</code></td><td></td></tr>
<tr><td><code>Stromal Sarcoma</code></td><td><code>icdo:8935/3</code></td><td></td></tr>
<tr><td><code>Micropapillary Carcinoma</code></td><td><code>icdo:8265/3</code></td><td></td></tr>
<tr><td><code>Mucinous Cystadenocarcinoma</code></td><td><code>icdo:8470/3</code></td><td></td></tr>
<tr><td><code>Intraductal Carcinoma, Noninfiltrating</code></td><td><code>icdo:8500/2</code></td><td></td></tr>
<tr><td><code>Intracystic Carcinoma</code></td><td><code>icdo:8504/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma</code></td><td><code>icdo:8170/3</code></td><td></td></tr>
<tr><td><code>Comedocarcinoma</code></td><td><code>icdo:8501/3</code></td><td></td></tr>
<tr><td><code>Papillary Cystadenocarcinoma</code></td><td><code>icdo:8450/3</code></td><td></td></tr>
<tr><td><code>Intraductal Oncocytic Papillary Neoplasm</code></td><td><code>icdo:8455/2</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma</code></td><td><code>icdo:9040/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Sarcoma, NOS (Except of Kidney M-)</code></td><td><code>icdo:9044/3</code></td><td></td></tr>
<tr><td><code>Teratoma, Malignant</code></td><td><code>icdo:9080/3</code></td><td></td></tr>
<tr><td><code>Neuroblastoma</code></td><td><code>icdo:9500/3</code></td><td></td></tr>
<tr><td><code>Medulloepithelioma</code></td><td><code>icdo:9501/3</code></td><td></td></tr>
<tr><td><code>Neuroepithelioma</code></td><td><code>icdo:9503/3</code></td><td></td></tr>
<tr><td><code>Chondrosarcoma</code></td><td><code>icdo:9220/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Malignant</code></td><td><code>icdo:8580/3</code></td><td></td></tr>
<tr><td><code>Thymic Carcinoma</code></td><td><code>icdo:8586/3</code></td><td></td></tr>
<tr><td><code>Cutaneous T-cell Lymphoma</code></td><td><code>icdo:9709/3</code></td><td></td></tr>
<tr><td><code>Seminoma</code></td><td><code>icdo:9061/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma</code></td><td><code>icdo:9180/3</code></td><td></td></tr>
<tr><td><code>Immunoproliferative Disease</code></td><td><code>icdo:9760/3</code></td><td></td></tr>
<tr><td><code>Heavy Chain Disease</code></td><td><code>icdo:9762/3</code></td><td></td></tr>
<tr><td><code>Leukemia</code></td><td><code>icdo:9800/3</code></td><td></td></tr>
<tr><td><code>Acute Leukemia</code></td><td><code>icdo:9801/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia, B/Myeloid</code></td><td><code>icdo:9808/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia, T/Myeloid</code></td><td><code>icdo:9809/3</code></td><td></td></tr>
<tr><td><code>Lymphoid Leukemia</code></td><td><code>icdo:9820/3</code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia, L2 Type</code></td><td><code>icdo:9828/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic Leukemia</code></td><td><code>icdo:9832/3</code></td><td></td></tr>
<tr><td><code>Precursor Cell Lymphoblastic Leukemia</code></td><td><code>icdo:9835/3</code></td><td></td></tr>
<tr><td><code>Myeloid Leukemia</code></td><td><code>icdo:9860/3</code></td><td></td></tr>
<tr><td><code>Chronic Myeloid Leukemia</code></td><td><code>icdo:9863/3</code></td><td></td></tr>
<tr><td><code>Therapy-related Acute Myeloid Leukemia</code></td><td><code>icdo:9920/3</code></td><td></td></tr>
<tr><td><code>Chronic Myelomonocytic Leukemia</code></td><td><code>icdo:9945/3</code></td><td></td></tr>
<tr><td><code>Chronic Myeloproliferative Disease</code></td><td><code>icdo:9960/3</code></td><td></td></tr>
<tr><td><code>Therapy-related Myelodysplastic Syndrome</code></td><td><code>icdo:9987/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic Syndrome</code></td><td><code>icdo:9989/3</code></td><td></td></tr>
<tr><td><code>Precancerous Melanosis</code></td><td><code>icdo:8741/2</code></td><td></td></tr>
<tr><td><code>Dermatofibrosarcoma</code></td><td><code>icdo:8832/3</code></td><td></td></tr>
<tr><td><code>Lobular Carcinoma</code></td><td><code>icdo:8520/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Keratinizing, in Situ</code></td><td><code>icdo:8071/2</code></td><td></td></tr>
<tr><td><code>Basal Cell Carcinoma</code></td><td><code>icdo:8090/3</code></td><td></td></tr>
<tr><td><code>Infiltrating Basal Cell Carcinoma</code></td><td><code>icdo:8092/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, HPV-independent</code></td><td><code>icdo:8484/3</code></td><td></td></tr>
<tr><td><code>Nephroblastoma</code></td><td><code>icdo:8960/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma</code></td><td><code>icdo:9510/3</code></td><td></td></tr>
<tr><td><code>Fibroma</code></td><td><code>icdo:8810/0</code></td><td></td></tr>
<tr><td><code>Lipoma</code></td><td><code>icdo:8850/0</code></td><td></td></tr>
<tr><td><code>Angiolipoma</code></td><td><code>icdo:8861/0</code></td><td></td></tr>
<tr><td><code>Teratoma</code></td><td><code>icdo:9080/1</code></td><td></td></tr>
<tr><td><code>Dermoid Cyst</code></td><td><code>icdo:9084/0</code></td><td></td></tr>
<tr><td><code>Hemangioma</code></td><td><code>icdo:9120/0</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma</code></td><td><code>icdo:9150/1</code></td><td></td></tr>
<tr><td><code>Meningioma</code></td><td><code>icdo:9530/0</code></td><td></td></tr>
<tr><td><code>Meningiomatosis</code></td><td><code>icdo:9530/1</code></td><td></td></tr>
<tr><td><code>Paraganglioma</code></td><td><code>icdo:8680/1</code></td><td></td></tr>
<tr><td><code>Astrocytoma</code></td><td><code>icdo:9400/3</code></td><td></td></tr>
<tr><td><code>Glioblastoma</code></td><td><code>icdo:9440/3</code></td><td></td></tr>
<tr><td><code>Oligodendroglioma</code></td><td><code>icdo:9450/3</code></td><td></td></tr>
<tr><td><code>Embryonal Tumor with Multilayered Rosettes</code></td><td><code>icdo:9478/3</code></td><td></td></tr>
<tr><td><code>Ganglioglioma</code></td><td><code>icdo:9505/1</code></td><td></td></tr>
<tr><td><code>Neurofibroma</code></td><td><code>icdo:9540/0</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis</code></td><td><code>icdo:9540/1</code></td><td></td></tr>
<tr><td><code>Neurilemoma</code></td><td><code>icdo:9560/0</code></td><td></td></tr>
<tr><td><code>Neuroma</code></td><td><code>icdo:9570/0</code></td><td></td></tr>
<tr><td><code>Perineurioma</code></td><td><code>icdo:9571/0</code></td><td></td></tr>
<tr><td><code>Choroid Plexus Papilloma</code></td><td><code>icdo:9390/0</code></td><td></td></tr>
<tr><td><code>Medulloblastoma</code></td><td><code>icdo:9470/3</code></td><td></td></tr>
<tr><td><code>Cerebellar Sarcoma</code></td><td><code>icdo:9480/3</code></td><td></td></tr>
<tr><td><code>Leiomyoma</code></td><td><code>icdo:8890/0</code></td><td></td></tr>
<tr><td><code>Smooth Muscle Tumor</code></td><td><code>icdo:8897/1</code></td><td></td></tr>
<tr><td><code>Rhabdomyoma</code></td><td><code>icdo:8900/0</code></td><td></td></tr>
<tr><td><code>Hemangioendothelioma</code></td><td><code>icdo:9130/1</code></td><td></td></tr>
<tr><td><code>Follicular Adenocarcinoma</code></td><td><code>icdo:8330/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Tumor</code></td><td><code>icdo:8005/0</code></td><td></td></tr>
<tr><td><code>Adenoma</code></td><td><code>icdo:8140/0</code></td><td></td></tr>
<tr><td><code>Papillary Adenoma</code></td><td><code>icdo:8260/0</code></td><td></td></tr>
<tr><td><code>Pituitary Adenoma</code></td><td><code>icdo:8272/0</code></td><td></td></tr>
<tr><td><code>Pituitary Carcinoma</code></td><td><code>icdo:8272/3</code></td><td></td></tr>
<tr><td><code>Granular Cell Tumor</code></td><td><code>icdo:9580/0</code></td><td></td></tr>
<tr><td><code>Pinealoma</code></td><td><code>icdo:9360/1</code></td><td></td></tr>
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
<tr><td><code>Adenocarcinoma, NOS</code></td><td><code>icdo:8140/3</code></td><td></td></tr>
<tr><td><code>Adenoma, NOS</code></td><td><code>icdo:8140/0</code></td><td></td></tr>
<tr><td><code>Adenosarcoma</code></td><td><code>icdo:8933/3</code></td><td></td></tr>
<tr><td><code>Angiocentric Glioma</code></td><td><code>icdo:9431/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Angiomyosarcoma</code></td><td><code>icdo:8894/3</code></td><td></td></tr>
<tr><td><code>Astroblastoma</code></td><td><code>icdo:9430/3</code></td><td></td></tr>
<tr><td><code>Astrocytoma, NOS</code></td><td><code>icdo:9400/3</code></td><td></td></tr>
<tr><td><code>Atypical Choroid Plexus Papilloma</code></td><td><code>ncit:C53686</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'</td></tr>
<tr><td><code>Carcinoma, NOS</code></td><td><code>icdo:8010/3</code></td><td></td></tr>
<tr><td><code>Cholangiocarcinoma</code></td><td><code>icdo:8160/3</code></td><td>(lt) ConsortiumNote: DIAGNOSIS_CATEGORY == 'Hepatic Tumor, Other'</td></tr>
<tr><td><code>Chondroblastic osteosarcoma</code></td><td><code>icdo:9181/3</code></td><td></td></tr>
<tr><td><code>Choriocarcinoma</code></td><td><code>ncit:C2948</code></td><td></td></tr>
<tr><td><code>Clear cell sarcoma, NOS</code></td><td><code>icdo:9044/3</code></td><td></td></tr>
<tr><td><code>Craniopharyngioma</code></td><td><code>icdo:9350/1</code></td><td></td></tr>
<tr><td><code>Cystadenocarcinoma, NOS</code></td><td><code>icdo:8440/3</code></td><td></td></tr>
<tr><td><code>Dedifferentiated Liposarcoma</code></td><td><code>ncit:C3704</code></td><td></td></tr>
<tr><td><code>Desmoplastic Small Round Cell Tumor</code></td><td><code>icdo:8806/3</code></td><td></td></tr>
<tr><td><code>Diffuse Leptomeningeal Glioneuronal Tumor</code></td><td><code>icdo:9509/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Dysembryoplastic Neuroepithelial Tumor</code></td><td><code>icdo:9413/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Dysgerminoma</code></td><td><code>icdo:9060/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>ncit:C6561</code></td><td></td></tr>
<tr><td><code>Ewing Sarcoma</code></td><td><code>icdo:9260/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Fibroblastic Osteosarcoma</code></td><td><code>ncit:C4020</code></td><td></td></tr>
<tr><td><code>Fibrolipoma</code></td><td><code>icdo:8851/0</code></td><td></td></tr>
<tr><td><code>Fibromyxosarcoma</code></td><td><code>icdo:8811/3</code></td><td></td></tr>
<tr><td><code>Fibrosarcoma, NOS</code></td><td><code>icdo:8810/3</code></td><td></td></tr>
<tr><td><code>Gangliocytoma</code></td><td><code>icdo:9492/0</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Ganglioneuroblastoma</code></td><td><code>icdo:9490/3</code></td><td></td></tr>
<tr><td><code>Ganglioneuroma</code></td><td><code>icdo:9490/0</code></td><td></td></tr>
<tr><td><code>Gastroblastoma</code></td><td><code>icdo:8976/3</code></td><td></td></tr>
<tr><td><code>Germinoma</code></td><td><code>ncit:C3753</code></td><td></td></tr>
<tr><td><code>Gliofibroma</code></td><td><code>icdo:9442/1</code></td><td></td></tr>
<tr><td><code>Gliosarcoma</code></td><td><code>icdo:9442/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Glomangiosarcoma</code></td><td><code>icdo:8710/3</code></td><td></td></tr>
<tr><td><code>Hemangioblastoma</code></td><td><code>icdo:9161/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hemangioendothelioma, NOS</code></td><td><code>icdo:9130/1</code></td><td></td></tr>
<tr><td><code>Hemangioma, NOS</code></td><td><code>icdo:9120/0</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, NOS</code></td><td><code>icdo:9150/1</code></td><td></td></tr>
<tr><td><code>Hemangiosarcoma</code></td><td><code>icdo:9120/3</code></td><td></td></tr>
<tr><td><code>Hepatoblastoma</code></td><td><code>icdo:8970/3</code></td><td></td></tr>
<tr><td><code>Histiocytic Sarcoma</code></td><td><code>ncit:C27349</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Hodgkin Lymphoma, NOS</code></td><td><code>icdo:9650/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nodular Sclerosis, NOS</code></td><td><code>icdo:9663/3</code></td><td></td></tr>
<tr><td><code>Infantile Fibrosarcoma</code></td><td><code>icdo:8814/3</code></td><td></td></tr>
<tr><td><code>Intimal Sarcoma</code></td><td><code>icdo:9137/3</code></td><td></td></tr>
<tr><td><code>Intravascular Large B-Cell Lymphoma</code></td><td><code>icdo:9712/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Juvenile Xanthogranuloma</code></td><td><code>icdo:9749/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Kaposi Sarcoma</code></td><td><code>icdo:9140/3</code></td><td></td></tr>
<tr><td><code>Leiomyosarcoma, NOS</code></td><td><code>icdo:8890/3</code></td><td></td></tr>
<tr><td><code>Lymphangioleiomyomatosis</code></td><td><code>icdo:9174/3</code></td><td></td></tr>
<tr><td><code>Lymphangiosarcoma</code></td><td><code>icdo:9170/3</code></td><td></td></tr>
<tr><td><code>Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>icdo:9540/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Medullomyoblastoma</code></td><td><code>icdo:9472/3</code></td><td></td></tr>
<tr><td><code>Meningioma, NOS</code></td><td><code>icdo:9530/0</code></td><td></td></tr>
<tr><td><code>Mesenchymal Chondrosarcoma</code></td><td><code>icdo:9240/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Mixed Germ Cell Tumor</code></td><td><code>ncit:C4290</code></td><td></td></tr>
<tr><td><code>Myosarcoma</code></td><td><code>icdo:8895/3</code></td><td></td></tr>
<tr><td><code>Myxoid Liposarcoma</code></td><td><code>ncit:C27781</code></td><td></td></tr>
<tr><td><code>Myxoid Leiomyosarcoma</code></td><td><code>icdo:8896/3</code></td><td></td></tr>
<tr><td><code>Myxopapillary Ependymoma</code></td><td><code>ncit:C3697</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Myxosarcoma</code></td><td><code>icdo:8840/3</code></td><td></td></tr>
<tr><td><code>Neuroma, NOS</code></td><td><code>icdo:9570/0</code></td><td></td></tr>
<tr><td><code>Neurothekeoma</code></td><td><code>icdo:9562/0</code></td><td></td></tr>
<tr><td><code>Oligodendroblastoma</code></td><td><code>icdo:9460/3</code></td><td></td></tr>
<tr><td><code>Pancreatoblastoma</code></td><td><code>icdo:8971/3</code></td><td></td></tr>
<tr><td><code>Papillary Craniopharyngioma</code></td><td><code>icdo:9352/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'</td></tr>
<tr><td><code>Papillary Glioneuronal Tumor</code></td><td><code>icdo:9509/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'</td></tr>
<tr><td><code>Parosteal Osteosarcoma</code></td><td><code>icdo:9192/3</code></td><td></td></tr>
<tr><td><code>Perineurioma, NOS</code></td><td><code>icdo:9571/0</code></td><td></td></tr>
<tr><td><code>Periosteal Osteosarcoma</code></td><td><code>icdo:9193/3</code></td><td></td></tr>
<tr><td><code>Pheochromocytoma</code></td><td><code>icdo:8700/3</code></td><td></td></tr>
<tr><td><code>Pilocytic Astrocytoma</code></td><td><code>icdo:9421/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pilomyxoid Astrocytoma</code></td><td><code>icdo:9425/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'</td></tr>
<tr><td><code>Pineocytoma</code></td><td><code>icdo:9361/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Pituicytoma</code></td><td><code>icdo:9432/1</code></td><td></td></tr>
<tr><td><code>Plasmacytoma, NOS</code></td><td><code>icdo:9731/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Xanthoastrocytoma</code></td><td><code>icdo:9424/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'</td></tr>
<tr><td><code>Pleomorphic Liposarcoma</code></td><td><code>icdo:8854/3</code></td><td></td></tr>
<tr><td><code>Polymorphic PTLD</code></td><td><code>icdo:9971/3</code></td><td></td></tr>
<tr><td><code>Primitive Neuroectodermal Tumor</code></td><td><code>icdo:9473/3</code></td><td></td></tr>
<tr><td><code>Prolactinoma</code></td><td><code>icdo:8271/0</code></td><td></td></tr>
<tr><td><code>Rhabdomyoma, NOS</code></td><td><code>icdo:8900/0</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma, NOS</code></td><td><code>icdo:8900/3</code></td><td></td></tr>
<tr><td><code>Solitary Fibrous Tumor</code></td><td><code>ncit:C7634</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Solitary Fibrous Tumor, Malignant</code></td><td><code>icdo:8815/3</code></td><td></td></tr>
<tr><td><code>Spongioneuroblastoma</code></td><td><code>icdo:9504/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, NOS</code></td><td><code>icdo:8070/3</code></td><td></td></tr>
<tr><td><code>Subependymoma</code></td><td><code>icdo:9383/1</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'</td></tr>
<tr><td><code>Sympathetic Paraganglioma</code></td><td><code>icdo:8681/3</code></td><td></td></tr>
<tr><td><code>Teratocarcinoma</code></td><td><code>icdo:9081/3</code></td><td></td></tr>
<tr><td><code>Neoplasm, Malignant</code></td><td><code>icdo:8000/3</code></td><td></td></tr>
<tr><td><code>Tumor Cells, Malignant</code></td><td><code>icdo:8001/3</code></td><td></td></tr>
<tr><td><code>Malignant Tumor, Small Cell Type</code></td><td><code>icdo:8002/3</code></td><td></td></tr>
<tr><td><code>Malignant Tumor, Giant Cell Type</code></td><td><code>icdo:8003/3</code></td><td></td></tr>
<tr><td><code>Malignant Tumor, Spindle Cell Type</code></td><td><code>icdo:8004/3</code></td><td></td></tr>
<tr><td><code>Malignant Tumor, Clear Cell Type</code></td><td><code>icdo:8005/3</code></td><td></td></tr>
<tr><td><code>Carcinoma In Situ, NOS</code></td><td><code>icdo:8010/2</code></td><td></td></tr>
<tr><td><code>Epithelioma, Malignant</code></td><td><code>icdo:8011/3</code></td><td></td></tr>
<tr><td><code>Large Cell Carcinoma, NOS</code></td><td><code>icdo:8012/3</code></td><td></td></tr>
<tr><td><code>Large Cell Neuroendocrine Carcinoma</code></td><td><code>icdo:8013/3</code></td><td></td></tr>
<tr><td><code>Large Cell Carcinoma With Rhabdoid Phenotype</code></td><td><code>icdo:8014/3</code></td><td></td></tr>
<tr><td><code>Glassy Cell Carcinoma</code></td><td><code>icdo:8015/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, Undifferentiated Type, NOS</code></td><td><code>icdo:8020/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, Anaplastic Type, NOS</code></td><td><code>icdo:8021/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Carcinoma</code></td><td><code>icdo:8022/3</code></td><td></td></tr>
<tr><td><code>Giant Cell And Spindle Cell Carcinoma</code></td><td><code>icdo:8030/3</code></td><td></td></tr>
<tr><td><code>Giant Cell Carcinoma</code></td><td><code>icdo:8031/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Carcinoma</code></td><td><code>icdo:8032/3</code></td><td></td></tr>
<tr><td><code>Pseudosarcomatous Carcinoma</code></td><td><code>icdo:8033/3</code></td><td></td></tr>
<tr><td><code>Polygonal Cell Carcinoma</code></td><td><code>icdo:8034/3</code></td><td></td></tr>
<tr><td><code>Carcinoma With Osteoclast-Like Giant Cells</code></td><td><code>icdo:8035/3</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma In Situ</code></td><td><code>icdo:8050/2</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma, NOS</code></td><td><code>icdo:8050/3</code></td><td></td></tr>
<tr><td><code>Verrucous Carcinoma, NOS</code></td><td><code>icdo:8051/3</code></td><td></td></tr>
<tr><td><code>Papillary Squamous Cell Carcinoma, Non-Invasive</code></td><td><code>icdo:8052/2</code></td><td></td></tr>
<tr><td><code>Papillary Squamous Cell Carcinoma</code></td><td><code>icdo:8052/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma In Situ, NOS</code></td><td><code>icdo:8070/2</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Keratinizing, NOS</code></td><td><code>icdo:8071/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Lg. Cell, Non-Ker.</code></td><td><code>icdo:8072/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Sm. Cell, Non-Ker.</code></td><td><code>icdo:8073/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Spindle Cell</code></td><td><code>icdo:8074/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, Adenoid</code></td><td><code>icdo:8075/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carc. In Situ With Question. Stromal Invas.</code></td><td><code>icdo:8076/2</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Micro-Invasive</code></td><td><code>icdo:8076/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma With Horn Formation</code></td><td><code>icdo:8078/3</code></td><td></td></tr>
<tr><td><code>Bowen Disease</code></td><td><code>icdo:8081/2</code></td><td></td></tr>
<tr><td><code>Lymphoepithelial Carcinoma</code></td><td><code>icdo:8082/3</code></td><td></td></tr>
<tr><td><code>Basaloid Squamous Cell Carcinoma</code></td><td><code>icdo:8083/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, Clear Cell Type</code></td><td><code>icdo:8084/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ</code></td><td><code>icdo:8140/2</code></td><td></td></tr>
<tr><td><code>Scirrhous Adenocarcinoma</code></td><td><code>icdo:8141/3</code></td><td></td></tr>
<tr><td><code>Superficial Spreading Adenocarcinoma</code></td><td><code>icdo:8143/3</code></td><td></td></tr>
<tr><td><code>Basal Cell Adenocarcinoma</code></td><td><code>icdo:8147/3</code></td><td></td></tr>
<tr><td><code>Adenoid Cystic Carcinoma</code></td><td><code>icdo:8200/3</code></td><td></td></tr>
<tr><td><code>Cribriform Carcinoma In Situ</code></td><td><code>icdo:8201/2</code></td><td></td></tr>
<tr><td><code>Cribriform Carcinoma</code></td><td><code>icdo:8201/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Mixed Subtypes</code></td><td><code>icdo:8255/3</code></td><td></td></tr>
<tr><td><code>Papillary Adenocarcinoma, NOS</code></td><td><code>icdo:8260/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ In Villous Adenoma</code></td><td><code>icdo:8261/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Villous Adenoma</code></td><td><code>icdo:8261/3</code></td><td></td></tr>
<tr><td><code>Villous Adenocarcinoma</code></td><td><code>icdo:8262/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ In Tubulovillous Adenoma</code></td><td><code>icdo:8263/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Tubulovillous Adenoma</code></td><td><code>icdo:8263/3</code></td><td></td></tr>
<tr><td><code>Mucoepidermoid Carcinoma</code></td><td><code>icdo:8430/3</code></td><td></td></tr>
<tr><td><code>Mucinous Adenocarcinoma</code></td><td><code>icdo:8480/3</code></td><td></td></tr>
<tr><td><code>Mucin-Producing Adenocarcinoma</code></td><td><code>icdo:8481/3</code></td><td></td></tr>
<tr><td><code>Melanoma In Situ</code></td><td><code>icdo:8720/2</code></td><td></td></tr>
<tr><td><code>Malignant Melanoma, NOS</code></td><td><code>icdo:8720/3</code></td><td></td></tr>
<tr><td><code>Nodular Melanoma</code></td><td><code>icdo:8721/3</code></td><td></td></tr>
<tr><td><code>Balloon Cell Melanoma</code></td><td><code>icdo:8722/3</code></td><td></td></tr>
<tr><td><code>Malignant Melanoma, Regressing</code></td><td><code>icdo:8723/3</code></td><td></td></tr>
<tr><td><code>Amelanotic Melanoma</code></td><td><code>icdo:8730/3</code></td><td></td></tr>
<tr><td><code>Superficial Spreading Melanoma</code></td><td><code>icdo:8743/3</code></td><td></td></tr>
<tr><td><code>Desmoplastic Melanoma, Malignant</code></td><td><code>icdo:8745/3</code></td><td></td></tr>
<tr><td><code>Mucosal Lentiginous Melanoma</code></td><td><code>icdo:8746/3</code></td><td></td></tr>
<tr><td><code>Mixed Epithel. &amp; Spindle Cell Melanoma</code></td><td><code>icdo:8770/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Cell Melanoma</code></td><td><code>icdo:8771/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Melanoma, NOS</code></td><td><code>icdo:8772/3</code></td><td></td></tr>
<tr><td><code>Mixed Tumor, Malignant, NOS</code></td><td><code>icdo:8940/3</code></td><td></td></tr>
<tr><td><code>Carcinoma In Pleomorphic Adenoma</code></td><td><code>icdo:8941/3</code></td><td></td></tr>
<tr><td><code>Marginal Zone B-Cell Lymphoma, NOS</code></td><td><code>icdo:9699/3</code></td><td></td></tr>
<tr><td><code>Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma</code></td><td><code>icdo:9823/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, HPV-Positive</code></td><td><code>icdo:8085/3</code></td><td></td></tr>
<tr><td><code>Squamous Cell Carcinoma, HPV-Negative</code></td><td><code>icdo:8086/3</code></td><td></td></tr>
<tr><td><code>Adenosquamous Carcinoma</code></td><td><code>icdo:8560/3</code></td><td></td></tr>
<tr><td><code>Epithelial-Myoepithelial Carcinoma</code></td><td><code>icdo:8562/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Squamous Metaplasia</code></td><td><code>icdo:8570/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Cartilaginous &amp; Oss. Metaplasia</code></td><td><code>icdo:8571/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Spindle Cell Metaplasia</code></td><td><code>icdo:8572/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Apocrine Metaplasia</code></td><td><code>icdo:8573/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma With Neuroendocrine Differentiation</code></td><td><code>icdo:8574/3</code></td><td></td></tr>
<tr><td><code>Metaplastic Carcinoma, NOS</code></td><td><code>icdo:8575/3</code></td><td></td></tr>
<tr><td><code>Myofibroblastic Sarcoma</code></td><td><code>icdo:8825/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Rhabdomyosarcoma, Adult Type</code></td><td><code>icdo:8901/3</code></td><td></td></tr>
<tr><td><code>Mixed Type Rhabdomyosarcoma</code></td><td><code>icdo:8902/3</code></td><td></td></tr>
<tr><td><code>Embryonal Rhabdomyosarcoma</code></td><td><code>icdo:8910/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Rhabdomyosarcoma</code></td><td><code>icdo:8912/3</code></td><td></td></tr>
<tr><td><code>Malignant Lymphoma, NOS</code></td><td><code>icdo:9590/3</code></td><td></td></tr>
<tr><td><code>Malignant Lymphoma, Non-Hodgkin</code></td><td><code>icdo:9591/3</code></td><td></td></tr>
<tr><td><code>Composite Hodgkin and Non-Hodgkin Lymphoma</code></td><td><code>icdo:9596/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocyte-Rich</code></td><td><code>icdo:9651/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Mixed Cellularity, NOS</code></td><td><code>icdo:9652/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocytic Deplet., NOS</code></td><td><code>icdo:9653/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocytic Deplet., Diffuse Fibrosis</code></td><td><code>icdo:9654/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Lymphocytic Deplet., Reticular</code></td><td><code>icdo:9655/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nodular Lymphocyte Predom.</code></td><td><code>icdo:9659/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Granuloma [Obs]</code></td><td><code>icdo:9661/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Sarcoma [Obs]</code></td><td><code>icdo:9662/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nod. Scler., Cellular Phase</code></td><td><code>icdo:9664/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nod. Scler., Grade 1</code></td><td><code>icdo:9665/3</code></td><td></td></tr>
<tr><td><code>Hodgkin Lymphoma, Nod. Scler., Grade 2</code></td><td><code>icdo:9667/3</code></td><td></td></tr>
<tr><td><code>ML, Small B Lymphocytic, NOS</code></td><td><code>icdo:9670/3</code></td><td></td></tr>
<tr><td><code>ML, Lymphoplasmacytic</code></td><td><code>icdo:9671/3</code></td><td></td></tr>
<tr><td><code>Mantle Cell Lymphoma</code></td><td><code>icdo:9673/3</code></td><td></td></tr>
<tr><td><code>ML, Mixed Sm. and Lg. Cell, Diffuse</code></td><td><code>icdo:9675/3</code></td><td></td></tr>
<tr><td><code>ML, Large B-Cell, Diffuse</code></td><td><code>icdo:9680/3</code></td><td></td></tr>
<tr><td><code>ML, Large B-Cell, Diffuse, Immunoblastic, NOS</code></td><td><code>icdo:9684/3</code></td><td></td></tr>
<tr><td><code>Burkitt Lymphoma, NOS</code></td><td><code>icdo:9687/3</code></td><td></td></tr>
<tr><td><code>T-Cell Histiocyte Rich Large B-Cell Lymphoma</code></td><td><code>icdo:9688/3</code></td><td></td></tr>
<tr><td><code>Follicular Lymphoma, NOS</code></td><td><code>icdo:9690/3</code></td><td></td></tr>
<tr><td><code>Follicular Lymphoma, Grade 2</code></td><td><code>icdo:9691/3</code></td><td></td></tr>
<tr><td><code>Follicular Lymphoma, Grade 1</code></td><td><code>icdo:9695/3</code></td><td></td></tr>
<tr><td><code>Follicular Lymphoma, Grade 3</code></td><td><code>icdo:9698/3</code></td><td></td></tr>
<tr><td><code>Sezary Syndrome</code></td><td><code>icdo:9701/3</code></td><td></td></tr>
<tr><td><code>Mature T-Cell Lymphoma, NOS</code></td><td><code>icdo:9702/3</code></td><td></td></tr>
<tr><td><code>Angioimmunoblastic T-Cell Lymphoma</code></td><td><code>icdo:9705/3</code></td><td></td></tr>
<tr><td><code>Anaplastic Large Cell Lymphoma, T-Cell and Null Cell Type</code></td><td><code>icdo:9714/3</code></td><td></td></tr>
<tr><td><code>Anaplastic Large Cell Lymphoma, ALK Negative</code></td><td><code>icdo:9715/3</code></td><td></td></tr>
<tr><td><code>NK/T-Cell Lymphoma, Nasal and Nasal-Type</code></td><td><code>icdo:9719/3</code></td><td></td></tr>
<tr><td><code>Systemic EBV Pos. T-Cell Lymphoproliferative Disease of Childhood</code></td><td><code>icdo:9724/3</code></td><td></td></tr>
<tr><td><code>Precursor Cell Lymphoblastic Lymphoma, NOS</code></td><td><code>icdo:9727/3</code></td><td></td></tr>
<tr><td><code>Precursor B-Cell Lymphoblastic Lymphoma</code></td><td><code>icdo:9728/3</code></td><td></td></tr>
<tr><td><code>Precursor T-Cell Lymphoblastic Lymphoma</code></td><td><code>icdo:9729/3</code></td><td></td></tr>
<tr><td><code>Plasmacytoma, Extramedullary</code></td><td><code>icdo:9734/3</code></td><td></td></tr>
<tr><td><code>Plasmablastic Lymphoma</code></td><td><code>icdo:9735/3</code></td><td></td></tr>
<tr><td><code>ALK Positive Large B-Cell Lymphoma</code></td><td><code>icdo:9737/3</code></td><td></td></tr>
<tr><td><code>Lrg B-Cell Lymphoma in HHV8-Assoc. Multicentric Castleman DZ</code></td><td><code>icdo:9738/3</code></td><td></td></tr>
<tr><td><code>Mast Cell Sarcoma</code></td><td><code>icdo:9740/3</code></td><td></td></tr>
<tr><td><code>Malignant Mastocytosis</code></td><td><code>icdo:9741/3</code></td><td></td></tr>
<tr><td><code>Erdhiem-Chester Disease</code></td><td><code>icdo:9749/3</code></td><td></td></tr>
<tr><td><code>Malignant Histiocytosis</code></td><td><code>icdo:9750/3</code></td><td></td></tr>
<tr><td><code>Langerhans Cell Histiocytosis, NOS</code></td><td><code>icdo:9751/3</code></td><td></td></tr>
<tr><td><code>Langerhans Cell Histiocytosis, Disseminated</code></td><td><code>icdo:9754/3</code></td><td></td></tr>
<tr><td><code>Langerhans Cell Sarcoma</code></td><td><code>icdo:9756/3</code></td><td></td></tr>
<tr><td><code>Interdigitating Dendritic Cell Sarcoma</code></td><td><code>icdo:9757/3</code></td><td></td></tr>
<tr><td><code>Follicular Dendritic Cell Sarcoma</code></td><td><code>icdo:9758/3</code></td><td></td></tr>
<tr><td><code>Fibroblastic Reticular Cell Tumor</code></td><td><code>icdo:9759/3</code></td><td></td></tr>
<tr><td><code>Lymphomatoid Granulomatosis, Grade 3</code></td><td><code>icdo:9766/3</code></td><td></td></tr>
<tr><td><code>B Lymphoblastic Leukemia/Lymphoma, NOS</code></td><td><code>icdo:9811/3</code></td><td></td></tr>
<tr><td><code>Leukemia/Lymphoma with t(9;22)(q34;q11.2);BCR-ABL1</code></td><td><code>icdo:9812/3</code></td><td></td></tr>
<tr><td><code>Leukemia/Lymphoma with t(v;11q23);MLL Rearranged</code></td><td><code>icdo:9813/3</code></td><td></td></tr>
<tr><td><code>Leukemia/Lymphoma with t(12;21)(p13;q22);TEL-AML1(ETV6-RUNX1)</code></td><td><code>icdo:9814/3</code></td><td></td></tr>
<tr><td><code>B Lymphoblastic Leukemia/Lymphoma with Hyperdiploidy</code></td><td><code>icdo:9815/3</code></td><td></td></tr>
<tr><td><code>Leukemia/Lymphoma with Hypodiploidy (Hypodiploid ALL)</code></td><td><code>icdo:9816/3</code></td><td></td></tr>
<tr><td><code>B Lymphoblastic Leukemia/Lymphoma with t(5;14)(q31;q32);IL3-IGH</code></td><td><code>icdo:9817/3</code></td><td></td></tr>
<tr><td><code>Leukemia/Lymphoma with t(1;19)(q23;p13.3);E2A PBX1 (TCF3 PBX1)</code></td><td><code>icdo:9818/3</code></td><td></td></tr>
<tr><td><code>B-Lymphocytic Leukemia/Lymphoma, BCR-ABL1-Like</code></td><td><code>icdo:9819/3</code></td><td></td></tr>
<tr><td><code>T-Cell Large Granular Lymphocytic Leukemia</code></td><td><code>icdo:9831/3</code></td><td></td></tr>
<tr><td><code>T Lymphoblastic Leukemia/Lymphoma</code></td><td><code>icdo:9837/3</code></td><td></td></tr>
<tr><td><code>Myeloid and Lymphoid Neoplasms with PDGFRB Rearrangement</code></td><td><code>icdo:9965/3</code></td><td></td></tr>
<tr><td><code>Myeloid and Lymphoid Neoplasm with FGFR1 Abnormalities</code></td><td><code>icdo:9967/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic/Myeloproliferative Neoplasm, Unclassifiable</code></td><td><code>icdo:9975/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Adenocarcinoma, NOS</code></td><td><code>icdo:8310/3</code></td><td></td></tr>
<tr><td><code>Acinar Cell Carcinoma</code></td><td><code>icdo:8550/3</code></td><td></td></tr>
<tr><td><code>Acinar Cell Cystadenocarcinoma</code></td><td><code>icdo:8551/3</code></td><td></td></tr>
<tr><td><code>Fascial Fibrosarcoma</code></td><td><code>icdo:8813/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma, Nos</code></td><td><code>icdo:8980/3</code></td><td></td></tr>
<tr><td><code>Carcinosarcoma, Embryonal Type</code></td><td><code>icdo:8981/3</code></td><td></td></tr>
<tr><td><code>Malignant Myoepithelioma</code></td><td><code>icdo:8982/3</code></td><td></td></tr>
<tr><td><code>Trabecular Adenocarcinoma</code></td><td><code>icdo:8190/3</code></td><td></td></tr>
<tr><td><code>Duct Carcinoma In Situ, Solid Type</code></td><td><code>icdo:8230/2</code></td><td></td></tr>
<tr><td><code>Solid Carcinoma, Nos</code></td><td><code>icdo:8230/3</code></td><td></td></tr>
<tr><td><code>Carcinoma Simplex</code></td><td><code>icdo:8231/3</code></td><td></td></tr>
<tr><td><code>Oxyphilic Adenocarcinoma</code></td><td><code>icdo:8290/3</code></td><td></td></tr>
<tr><td><code>Invasive Carcinoma Of No Special Type</code></td><td><code>icdo:8500/3</code></td><td></td></tr>
<tr><td><code>Secretory Carcinoma Of No Special Type</code></td><td><code>icdo:8502/3</code></td><td></td></tr>
<tr><td><code>Polymorphous Low Grade Adenocarcinoma</code></td><td><code>icdo:8525/3</code></td><td></td></tr>
<tr><td><code>Warthin Tumor, Malignant</code></td><td><code>icdo:8561/3</code></td><td></td></tr>
<tr><td><code>Sarcoma, Nos</code></td><td><code>icdo:8800/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Sarcoma</code></td><td><code>icdo:8801/3</code></td><td></td></tr>
<tr><td><code>Giant Cell Sarcoma</code></td><td><code>icdo:8802/3</code></td><td></td></tr>
<tr><td><code>Small Cell Sarcoma</code></td><td><code>icdo:8803/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Sarcoma</code></td><td><code>icdo:8804/3</code></td><td></td></tr>
<tr><td><code>Undifferentiated Sarcoma</code></td><td><code>icdo:8805/3</code></td><td></td></tr>
<tr><td><code>Liposarcoma, Nos</code></td><td><code>icdo:8850/3</code></td><td></td></tr>
<tr><td><code>Liposarcoma, Well Differentiated</code></td><td><code>icdo:8851/3</code></td><td></td></tr>
<tr><td><code>Round Cell Liposarcoma</code></td><td><code>icdo:8853/3</code></td><td></td></tr>
<tr><td><code>Mixed Type Liposarcoma</code></td><td><code>icdo:8855/3</code></td><td></td></tr>
<tr><td><code>Fibroblastic Liposarcoma</code></td><td><code>icdo:8857/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Leiomyosarcoma</code></td><td><code>icdo:8891/3</code></td><td></td></tr>
<tr><td><code>Mesenchymoma, Malignant</code></td><td><code>icdo:8990/3</code></td><td></td></tr>
<tr><td><code>Embryonal Sarcoma</code></td><td><code>icdo:8991/3</code></td><td></td></tr>
<tr><td><code>Transitional Cell Carcinoma In Situ</code></td><td><code>icdo:8120/2</code></td><td></td></tr>
<tr><td><code>Transitional Cell Carcinoma, Nos</code></td><td><code>icdo:8120/3</code></td><td></td></tr>
<tr><td><code>Schneiderian Carcinoma</code></td><td><code>icdo:8121/3</code></td><td></td></tr>
<tr><td><code>Trans. Cell Carcinoma, Spindle Cell</code></td><td><code>icdo:8122/3</code></td><td></td></tr>
<tr><td><code>Basaloid Carcinoma</code></td><td><code>icdo:8123/3</code></td><td></td></tr>
<tr><td><code>Cloacogenic Carcinoma</code></td><td><code>icdo:8124/3</code></td><td></td></tr>
<tr><td><code>Mal. Melanoma In Giant Pigmented Nevus</code></td><td><code>icdo:8761/3</code></td><td></td></tr>
<tr><td><code>Small Cell Carcinoma, Nos</code></td><td><code>icdo:8041/3</code></td><td></td></tr>
<tr><td><code>Small Cell Carcinoma, Fusiform Cell</code></td><td><code>icdo:8043/3</code></td><td></td></tr>
<tr><td><code>Embryonal Carcinoma, Nos</code></td><td><code>icdo:9070/3</code></td><td></td></tr>
<tr><td><code>Yolk Sac Tumor</code></td><td><code>icdo:9071/3</code></td><td></td></tr>
<tr><td><code>Polyembryoma</code></td><td><code>icdo:9072/3</code></td><td></td></tr>
<tr><td><code>Chordoma, Nos</code></td><td><code>icdo:9370/3</code></td><td></td></tr>
<tr><td><code>Chondroid Chordoma</code></td><td><code>icdo:9371/3</code></td><td></td></tr>
<tr><td><code>Dedifferentiated Chordoma</code></td><td><code>icdo:9372/3</code></td><td></td></tr>
<tr><td><code>Combined Small Cell Carcinoma</code></td><td><code>icdo:8045/3</code></td><td></td></tr>
<tr><td><code>Carcinoma, Diffuse Type</code></td><td><code>icdo:8145/3</code></td><td></td></tr>
<tr><td><code>Mixed Neuroendocrine Non-Neuroendocrine Neoplasm</code></td><td><code>icdo:8154/3</code></td><td></td></tr>
<tr><td><code>Carcinoid Tumor, Malignant</code></td><td><code>icdo:8240/3</code></td><td></td></tr>
<tr><td><code>Composite Carcinoid</code></td><td><code>icdo:8244/3</code></td><td></td></tr>
<tr><td><code>Neuroendocrine Carcinoma</code></td><td><code>icdo:8246/3</code></td><td></td></tr>
<tr><td><code>Neuroendocrine Tumor</code></td><td><code>icdo:8249/3</code></td><td></td></tr>
<tr><td><code>Linitis Plastica</code></td><td><code>icdo:8142/3</code></td><td></td></tr>
<tr><td><code>Intestinal-Type Adenoma, High Grade</code></td><td><code>icdo:8144/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, Intestinal Type</code></td><td><code>icdo:8144/3</code></td><td></td></tr>
<tr><td><code>Gastrinoma, Malignant</code></td><td><code>icdo:8153/3</code></td><td></td></tr>
<tr><td><code>Somatostatinoma, Malignant</code></td><td><code>icdo:8156/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ In Adenomatous Polyp</code></td><td><code>icdo:8210/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Adenomatous Polyp</code></td><td><code>icdo:8210/3</code></td><td></td></tr>
<tr><td><code>Tubular Adenocarcinoma</code></td><td><code>icdo:8211/3</code></td><td></td></tr>
<tr><td><code>Serrated Dysplasia, High Grade</code></td><td><code>icdo:8213/2</code></td><td></td></tr>
<tr><td><code>Parietal Cell Carcinoma</code></td><td><code>icdo:8214/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ In Familial Polyp. Coli</code></td><td><code>icdo:8220/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Adenoma. Polyposis Coli</code></td><td><code>icdo:8220/3</code></td><td></td></tr>
<tr><td><code>Adenocarc. In Situ In Mult. Adenomatous Polyps</code></td><td><code>icdo:8221/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Mult. Adenomatous Polyps</code></td><td><code>icdo:8221/3</code></td><td></td></tr>
<tr><td><code>Enterochromaffin Cell Carcinoid</code></td><td><code>icdo:8241/3</code></td><td></td></tr>
<tr><td><code>Enterochromaffin-Like Cell Tumor, Malignant</code></td><td><code>icdo:8242/3</code></td><td></td></tr>
<tr><td><code>Goblet Cell Carcinoid</code></td><td><code>icdo:8243/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoid Tumor</code></td><td><code>icdo:8245/3</code></td><td></td></tr>
<tr><td><code>Signet Ring Cell Carcinoma</code></td><td><code>icdo:8490/3</code></td><td></td></tr>
<tr><td><code>Medullary Carcinoma, Nos</code></td><td><code>icdo:8510/3</code></td><td></td></tr>
<tr><td><code>Medullary Carcinoma With Lymphoid Stroma</code></td><td><code>icdo:8512/3</code></td><td></td></tr>
<tr><td><code>Hepatoid Adenocarcinoma</code></td><td><code>icdo:8576/3</code></td><td></td></tr>
<tr><td><code>Carcinofibroma</code></td><td><code>icdo:8934/3</code></td><td></td></tr>
<tr><td><code>Stromal Sarcoma, Nos</code></td><td><code>icdo:8935/3</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Stromal Sarcoma</code></td><td><code>icdo:8936/3</code></td><td></td></tr>
<tr><td><code>Multiple Myeloma</code></td><td><code>icdo:9732/3</code></td><td></td></tr>
<tr><td><code>Glucagonoma, Malignant</code></td><td><code>icdo:8152/3</code></td><td></td></tr>
<tr><td><code>Enteroglucagonoma, Malignant</code></td><td><code>icdo:8157/3</code></td><td></td></tr>
<tr><td><code>Pancreatobiliary-Type Carcinoma</code></td><td><code>icdo:8163/3</code></td><td></td></tr>
<tr><td><code>Extra-Adrenal Paraganglioma, Malignant</code></td><td><code>icdo:8693/3</code></td><td></td></tr>
<tr><td><code>Intestinal T-Cell Lymphoma</code></td><td><code>icdo:9717/3</code></td><td></td></tr>
<tr><td><code>Immunoproliferative Small Intestinal Disease</code></td><td><code>icdo:9764/3</code></td><td></td></tr>
<tr><td><code>Serrated Adenocarcinoma</code></td><td><code>icdo:8213/3</code></td><td></td></tr>
<tr><td><code>Micropapillary Carcinoma, Nos</code></td><td><code>icdo:8265/3</code></td><td></td></tr>
<tr><td><code>Mucinous Cystadenocarcinoma, Non-Invasive</code></td><td><code>icdo:8470/2</code></td><td></td></tr>
<tr><td><code>Mucinous Cystadenocarcinoma, Nos</code></td><td><code>icdo:8470/3</code></td><td></td></tr>
<tr><td><code>Papillary Mucinous Cystadenocarcinoma</code></td><td><code>icdo:8471/3</code></td><td></td></tr>
<tr><td><code>High Grade Appendiceal Mucinous Neoplasm</code></td><td><code>icdo:8480/2</code></td><td></td></tr>
<tr><td><code>Squamous Intraepithelial Neoplasia, Grade Iii</code></td><td><code>icdo:8077/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma Of Anal Glands</code></td><td><code>icdo:8215/3</code></td><td></td></tr>
<tr><td><code>Intraductal Carcinoma, Noninfiltrating, Nos</code></td><td><code>icdo:8500/2</code></td><td></td></tr>
<tr><td><code>Noninfiltrating Intraductal Papillary Adenocarcinoma</code></td><td><code>icdo:8503/2</code></td><td></td></tr>
<tr><td><code>Intraductal Papillary Adenocarcinoma With Invasion</code></td><td><code>icdo:8503/3</code></td><td></td></tr>
<tr><td><code>Noninfiltrating Intracystic Carcinoma</code></td><td><code>icdo:8504/2</code></td><td></td></tr>
<tr><td><code>Intracystic Carcinoma, Nos</code></td><td><code>icdo:8504/3</code></td><td></td></tr>
<tr><td><code>Paget Disease, Extramammary</code></td><td><code>icdo:8542/3</code></td><td></td></tr>
<tr><td><code>Bile Duct Cystadenocarcinoma</code></td><td><code>icdo:8161/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Nos</code></td><td><code>icdo:8170/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Fibrolamellar</code></td><td><code>icdo:8171/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Scirrhous</code></td><td><code>icdo:8172/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Spindle Cell Variant</code></td><td><code>icdo:8173/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Clear Cell Type</code></td><td><code>icdo:8174/3</code></td><td></td></tr>
<tr><td><code>Hepatocellular Carcinoma, Pleomorphic Type</code></td><td><code>icdo:8175/3</code></td><td></td></tr>
<tr><td><code>Comb. Hepatocel. Carcinoma &amp; Cholangiocarcinoma</code></td><td><code>icdo:8180/3</code></td><td></td></tr>
<tr><td><code>Comedocarcinoma, Non-Infiltrating</code></td><td><code>icdo:8501/2</code></td><td></td></tr>
<tr><td><code>Comedocarcinoma, Nos</code></td><td><code>icdo:8501/3</code></td><td></td></tr>
<tr><td><code>Intraductal Micropapillary Carcinoma</code></td><td><code>icdo:8507/2</code></td><td></td></tr>
<tr><td><code>Cystic Hypersecretory Carcinoma</code></td><td><code>icdo:8508/3</code></td><td></td></tr>
<tr><td><code>Kupffer Cell Sarcoma</code></td><td><code>icdo:9124/3</code></td><td></td></tr>
<tr><td><code>Hemangioendothelioma, Malignant</code></td><td><code>icdo:9130/3</code></td><td></td></tr>
<tr><td><code>Epithelioid Hemangioendothelioma, Malignant</code></td><td><code>icdo:9133/3</code></td><td></td></tr>
<tr><td><code>Hepatosplenic Gamma-Delta Cell Lymphoma</code></td><td><code>icdo:9716/3</code></td><td></td></tr>
<tr><td><code>Klatskin Tumor</code></td><td><code>icdo:8162/3</code></td><td></td></tr>
<tr><td><code>Glandular Intraepithelial Neoplasia, Grade Iii</code></td><td><code>icdo:8148/2</code></td><td></td></tr>
<tr><td><code>Islet Cell Carcinoma</code></td><td><code>icdo:8150/3</code></td><td></td></tr>
<tr><td><code>Insulinoma, Malignant</code></td><td><code>icdo:8151/3</code></td><td></td></tr>
<tr><td><code>Vipoma</code></td><td><code>icdo:8155/3</code></td><td></td></tr>
<tr><td><code>Acth-Producing Tumor</code></td><td><code>icdo:8158/3</code></td><td></td></tr>
<tr><td><code>Mixed Cell Adenocarcinoma</code></td><td><code>icdo:8323/3</code></td><td></td></tr>
<tr><td><code>Serous Cystadenocarcinoma</code></td><td><code>icdo:8441/3</code></td><td></td></tr>
<tr><td><code>Papillary Cystadenocarcinoma, Nos</code></td><td><code>icdo:8450/3</code></td><td></td></tr>
<tr><td><code>Solid Pseudopapillary Carcinoma</code></td><td><code>icdo:8452/3</code></td><td></td></tr>
<tr><td><code>Intraductal Papillary-Mucinous Carcinoma, Non-Inv.</code></td><td><code>icdo:8453/2</code></td><td></td></tr>
<tr><td><code>Intraductal Papillary-Mucinous Carcinoma, Invasive</code></td><td><code>icdo:8453/3</code></td><td></td></tr>
<tr><td><code>Intraductal Oncocytic Papillary Neoplasm, Nos</code></td><td><code>icdo:8455/2</code></td><td></td></tr>
<tr><td><code>Intraductal Oncocytic Papillary Neoplasms With Associated Invasive</code></td><td><code>icdo:8455/3</code></td><td></td></tr>
<tr><td><code>Duct Carcinoma, Desmoplastic Type</code></td><td><code>icdo:8514/3</code></td><td></td></tr>
<tr><td><code>Infiltrating Ductular Carcinoma</code></td><td><code>icdo:8521/3</code></td><td></td></tr>
<tr><td><code>Mixed Acinar Ductal Carcinoma</code></td><td><code>icdo:8552/3</code></td><td></td></tr>
<tr><td><code>Papillary Trans. Cell Carcinoma, Non-Invasive</code></td><td><code>icdo:8130/2</code></td><td></td></tr>
<tr><td><code>Papillary Trans. Cell Carcinoma</code></td><td><code>icdo:8130/3</code></td><td></td></tr>
<tr><td><code>Transitional Cell Carcinoma, Micropapillary</code></td><td><code>icdo:8131/3</code></td><td></td></tr>
<tr><td><code>Alveolar Adenocarcinoma</code></td><td><code>icdo:8251/3</code></td><td></td></tr>
<tr><td><code>Granular Cell Carcinoma</code></td><td><code>icdo:8320/3</code></td><td></td></tr>
<tr><td><code>Endometrioid Carcinoma</code></td><td><code>icdo:8380/3</code></td><td></td></tr>
<tr><td><code>Apocrine Adenocarcinoma</code></td><td><code>icdo:8401/3</code></td><td></td></tr>
<tr><td><code>Fibrous Histiocytoma, Malignant</code></td><td><code>icdo:8830/3</code></td><td></td></tr>
<tr><td><code>Alveolar Rhabdomyosarcoma</code></td><td><code>icdo:8920/3</code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma With Ganglionic Differentiation</code></td><td><code>icdo:8921/3</code></td><td></td></tr>
<tr><td><code>Mullerian Mixed Tumor</code></td><td><code>icdo:8950/3</code></td><td></td></tr>
<tr><td><code>Mesodermal Mixed Tumor</code></td><td><code>icdo:8951/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Nos</code></td><td><code>icdo:9040/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Spindle Cell</code></td><td><code>icdo:9041/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Epithelioid Cell</code></td><td><code>icdo:9042/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Biphasic</code></td><td><code>icdo:9043/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Sarcoma, Nos (Except Of Kidney M-</code></td><td><code>icdo:9044/3</code></td><td></td></tr>
<tr><td><code>Germ Cell Tumor, Nonseminomatous</code></td><td><code>icdo:9065/3</code></td><td></td></tr>
<tr><td><code>Teratoma, Malignant, Nos</code></td><td><code>icdo:9080/3</code></td><td></td></tr>
<tr><td><code>Malignant Teratoma, Undiff.</code></td><td><code>icdo:9082/3</code></td><td></td></tr>
<tr><td><code>Malignant Teratoma, Intermediate</code></td><td><code>icdo:9083/3</code></td><td></td></tr>
<tr><td><code>Teratoma With Malig. Transformation</code></td><td><code>icdo:9084/3</code></td><td></td></tr>
<tr><td><code>Choriocarcinoma Combined W/ Other Germ Cell Elements</code></td><td><code>icdo:9101/3</code></td><td></td></tr>
<tr><td><code>Trophoblastic Tumor, Epithelioid</code></td><td><code>icdo:9105/3</code></td><td></td></tr>
<tr><td><code>Mesonephroma, Malignant</code></td><td><code>icdo:9110/3</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, Malignant</code></td><td><code>icdo:9150/3</code></td><td></td></tr>
<tr><td><code>Malignant Giant Cell Tumor Of Soft Parts</code></td><td><code>icdo:9251/3</code></td><td></td></tr>
<tr><td><code>Malignant Tenosynovial Giant Cell Tumor</code></td><td><code>icdo:9252/3</code></td><td></td></tr>
<tr><td><code>Neuroblastoma, Nos</code></td><td><code>icdo:9500/3</code></td><td></td></tr>
<tr><td><code>Medulloepithelioma, Nos</code></td><td><code>icdo:9501/3</code></td><td></td></tr>
<tr><td><code>Teratoid Medulloepithelioma</code></td><td><code>icdo:9502/3</code></td><td></td></tr>
<tr><td><code>Neuroepithelioma, Nos</code></td><td><code>icdo:9503/3</code></td><td></td></tr>
<tr><td><code>Ganglioglioma, Anaplastic</code></td><td><code>icdo:9505/3</code></td><td></td></tr>
<tr><td><code>Neurilemmoma, Malignant</code></td><td><code>icdo:9560/3</code></td><td></td></tr>
<tr><td><code>MpnsT With Rhabdomyoblastic Differentiation</code></td><td><code>icdo:9561/3</code></td><td></td></tr>
<tr><td><code>Perineurioma, Malignant</code></td><td><code>icdo:9571/3</code></td><td></td></tr>
<tr><td><code>Nut Carcinoma</code></td><td><code>icdo:8023/3</code></td><td></td></tr>
<tr><td><code>Biphenotypic Sinonasal Sarcoma</code></td><td><code>icdo:9045/3</code></td><td></td></tr>
<tr><td><code>Chondrosarcoma, Nos</code></td><td><code>icdo:9220/3</code></td><td></td></tr>
<tr><td><code>Juxtacortical Chondrosarcoma</code></td><td><code>icdo:9221/3</code></td><td></td></tr>
<tr><td><code>Olfactory Neurogenic Tumor</code></td><td><code>icdo:9520/3</code></td><td></td></tr>
<tr><td><code>Olfactory Neurcytoma</code></td><td><code>icdo:9521/3</code></td><td></td></tr>
<tr><td><code>Olfactory Neuroblastoma</code></td><td><code>icdo:9522/3</code></td><td></td></tr>
<tr><td><code>Olfactory Neuroepithelioma</code></td><td><code>icdo:9523/3</code></td><td></td></tr>
<tr><td><code>Non-Small Cell Carcinoma</code></td><td><code>icdo:8046/3</code></td><td></td></tr>
<tr><td><code>Oat Cell Carcinoma</code></td><td><code>icdo:8042/3</code></td><td></td></tr>
<tr><td><code>Small Cell Carcinoma, Intermediate Cell</code></td><td><code>icdo:8044/3</code></td><td></td></tr>
<tr><td><code>Lepidic Adenocarcinoma</code></td><td><code>icdo:8250/3</code></td><td></td></tr>
<tr><td><code>Bronchiolo-Alveolar Carcinoma, Non-Mucinous</code></td><td><code>icdo:8252/3</code></td><td></td></tr>
<tr><td><code>Invasive Mucinous Adenocarcinoma</code></td><td><code>icdo:8253/3</code></td><td></td></tr>
<tr><td><code>Mixed Invasive Mucinous And Non-Mucinous Adenocarcinoma</code></td><td><code>icdo:8254/3</code></td><td></td></tr>
<tr><td><code>Pulmonary Blastoma</code></td><td><code>icdo:8972/3</code></td><td></td></tr>
<tr><td><code>Pleuropulmonary Blastoma</code></td><td><code>icdo:8973/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ, Non-Mucinous</code></td><td><code>icdo:8250/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma In Situ, Mucinous</code></td><td><code>icdo:8253/2</code></td><td></td></tr>
<tr><td><code>Minimally Invasive Adenocarcinoma, Non-Mucinous</code></td><td><code>icdo:8256/3</code></td><td></td></tr>
<tr><td><code>Minimally Invasive Adenocarcinoma, Mucinous</code></td><td><code>icdo:8257/3</code></td><td></td></tr>
<tr><td><code>Fetal Adenocarcinoma</code></td><td><code>icdo:8333/3</code></td><td></td></tr>
<tr><td><code>Pecoma, Malignant</code></td><td><code>icdo:8714/3</code></td><td></td></tr>
<tr><td><code>Pulmonary Myxoid Sarcoma With Ewsr1-Creb1 Translocation</code></td><td><code>icdo:8842/3</code></td><td></td></tr>
<tr><td><code>Mesothelioma, In Situ</code></td><td><code>icdo:9050/2</code></td><td></td></tr>
<tr><td><code>Mesothelioma, Malignant</code></td><td><code>icdo:9050/3</code></td><td></td></tr>
<tr><td><code>Fibrous Mesothelioma, Malignant</code></td><td><code>icdo:9051/3</code></td><td></td></tr>
<tr><td><code>Epithel. Mesothelioma, Mal.</code></td><td><code>icdo:9052/3</code></td><td></td></tr>
<tr><td><code>Mesothelioma, Biphasic, Malignant</code></td><td><code>icdo:9053/3</code></td><td></td></tr>
<tr><td><code>Primary Effusion Lymphoma</code></td><td><code>icdo:9678/3</code></td><td></td></tr>
<tr><td><code>Mediastinal Large B-Cell Lymphoma</code></td><td><code>icdo:9679/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Malignant, Nos</code></td><td><code>icdo:8580/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Type A, Malignant</code></td><td><code>icdo:8581/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Type Ab, Malignant</code></td><td><code>icdo:8582/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Type B1, Malignant</code></td><td><code>icdo:8583/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Type B2, Malignant</code></td><td><code>icdo:8584/3</code></td><td></td></tr>
<tr><td><code>Thymoma, Type B3, Malignant</code></td><td><code>icdo:8585/3</code></td><td></td></tr>
<tr><td><code>Thymic Carcinoma, Nos</code></td><td><code>icdo:8586/3</code></td><td></td></tr>
<tr><td><code>Spindle Epithelial Tumor With Thymus-Like Element</code></td><td><code>icdo:8588/3</code></td><td></td></tr>
<tr><td><code>Carcinoma Showing Thymus-Like Element</code></td><td><code>icdo:8589/3</code></td><td></td></tr>
<tr><td><code>Germ Cell Tumors With Associated Hematological Malignancy</code></td><td><code>icdo:9086/3</code></td><td></td></tr>
<tr><td><code>Splenic Marginal Zone B-Cell Lymphoma</code></td><td><code>icdo:9689/3</code></td><td></td></tr>
<tr><td><code>Mycosis Fungoides</code></td><td><code>icdo:9700/3</code></td><td></td></tr>
<tr><td><code>Subcutaneous Panniculitis-Like T-Cell Lymphoma</code></td><td><code>icdo:9708/3</code></td><td></td></tr>
<tr><td><code>Cutaneous T-Cell Lymphoma, Nos</code></td><td><code>icdo:9709/3</code></td><td></td></tr>
<tr><td><code>Primary Cutan. Cd30+ T-Cell Lymphoprolif. Disorder</code></td><td><code>icdo:9718/3</code></td><td></td></tr>
<tr><td><code>Paraganglioma, Malignant</code></td><td><code>icdo:8680/3</code></td><td></td></tr>
<tr><td><code>Myxoid Pleomorphic Liposarcoma</code></td><td><code>icdo:8859/3</code></td><td></td></tr>
<tr><td><code>Seminoma, Nos</code></td><td><code>icdo:9061/3</code></td><td></td></tr>
<tr><td><code>Seminoma, Anaplastic</code></td><td><code>icdo:9062/3</code></td><td></td></tr>
<tr><td><code>Spermatocytic Seminoma</code></td><td><code>icdo:9063/3</code></td><td></td></tr>
<tr><td><code>Peripheral Neuroectodermal Tumor</code></td><td><code>icdo:9364/3</code></td><td></td></tr>
<tr><td><code>Askin Tumor</code></td><td><code>icdo:9365/3</code></td><td></td></tr>
<tr><td><code>Periosteal Fibrosarcoma</code></td><td><code>icdo:8812/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma, Nos</code></td><td><code>icdo:9180/3</code></td><td></td></tr>
<tr><td><code>Telangiectatic Osteosarcoma</code></td><td><code>icdo:9183/3</code></td><td></td></tr>
<tr><td><code>Osteosarcoma In Paget Disease</code></td><td><code>icdo:9184/3</code></td><td></td></tr>
<tr><td><code>Small Cell Osteosarcoma</code></td><td><code>icdo:9185/3</code></td><td></td></tr>
<tr><td><code>Central Osteosarcoma</code></td><td><code>icdo:9186/3</code></td><td></td></tr>
<tr><td><code>Instrosseous Well Differentiated Osteosarcoma</code></td><td><code>icdo:9187/3</code></td><td></td></tr>
<tr><td><code>High Grade Surface Osteosarcoma</code></td><td><code>icdo:9194/3</code></td><td></td></tr>
<tr><td><code>Intracortical Osteosarcoma</code></td><td><code>icdo:9195/3</code></td><td></td></tr>
<tr><td><code>Chondroblastoma, Malignant</code></td><td><code>icdo:9230/3</code></td><td></td></tr>
<tr><td><code>Myxoid Chondrosarcoma</code></td><td><code>icdo:9231/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Chondrosarcoma</code></td><td><code>icdo:9242/3</code></td><td></td></tr>
<tr><td><code>Dedifferentiated Chondrosarcoma</code></td><td><code>icdo:9243/3</code></td><td></td></tr>
<tr><td><code>Giant Cell Tumor Of Bone, Malignant</code></td><td><code>icdo:9250/3</code></td><td></td></tr>
<tr><td><code>Adamantinoma Of Long Bones</code></td><td><code>icdo:9261/3</code></td><td></td></tr>
<tr><td><code>Odontogenic Tumor, Malignant</code></td><td><code>icdo:9270/3</code></td><td></td></tr>
<tr><td><code>Ameloblastic Odontosarcoma</code></td><td><code>icdo:9290/3</code></td><td></td></tr>
<tr><td><code>Ameloblastoma, Malignant</code></td><td><code>icdo:9310/3</code></td><td></td></tr>
<tr><td><code>Ameloblastic Fibrosarcoma</code></td><td><code>icdo:9330/3</code></td><td></td></tr>
<tr><td><code>Odontogenic Carcinosarcoma</code></td><td><code>icdo:9342/3</code></td><td></td></tr>
<tr><td><code>Ghost Cell Odontogenic Carcinoma</code></td><td><code>icdo:9302/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Odontogenic Carcinoma</code></td><td><code>icdo:9341/3</code></td><td></td></tr>
<tr><td><code>Round Cell Sarcoma With Ewsr1-Non-Ets Fusions</code></td><td><code>icdo:9366/3</code></td><td></td></tr>
<tr><td><code>Cic-Rearranged Sarcoma</code></td><td><code>icdo:9367/3</code></td><td></td></tr>
<tr><td><code>Sarcoma With Bcor Genetic Alterations</code></td><td><code>icdo:9368/3</code></td><td></td></tr>
<tr><td><code>Plasma Cell Leukemia</code></td><td><code>icdo:9733/3</code></td><td></td></tr>
<tr><td><code>Mast Cell Leukemia</code></td><td><code>icdo:9742/3</code></td><td></td></tr>
<tr><td><code>Immunoproliferative Disease, Nos</code></td><td><code>icdo:9760/3</code></td><td></td></tr>
<tr><td><code>Waldenstrom Macroglobulinemia</code></td><td><code>icdo:9761/3</code></td><td></td></tr>
<tr><td><code>Heavy Chain Disease, Nos</code></td><td><code>icdo:9762/3</code></td><td></td></tr>
<tr><td><code>Leukemia, Nos</code></td><td><code>icdo:9800/3</code></td><td></td></tr>
<tr><td><code>Acute Leukemia, Nos</code></td><td><code>icdo:9801/3</code></td><td></td></tr>
<tr><td><code>Acute Biphenotypic Leukemia</code></td><td><code>icdo:9805/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia With T(9;22)(Q34;Q11.2);Bcr-Abl1</code></td><td><code>icdo:9806/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia With T(V;11Q23);Mll Rearranged</code></td><td><code>icdo:9807/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia, B/Myeloid, Nos</code></td><td><code>icdo:9808/3</code></td><td></td></tr>
<tr><td><code>Mixed Phenotype Acute Leukemia, T/Myeloid, Nos</code></td><td><code>icdo:9809/3</code></td><td></td></tr>
<tr><td><code>Lymphoid Leukemia, Nos</code></td><td><code>icdo:9820/3</code></td><td></td></tr>
<tr><td><code>Burkitt Cell Leukemia</code></td><td><code>icdo:9826/3</code></td><td></td></tr>
<tr><td><code>Adult T-Cell Leukemia/Lymphoma (Htlv-1 Pos.)</code></td><td><code>icdo:9827/3</code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia, L2 Type, Nos</code></td><td><code>icdo:9828/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic Leukemia, Nos</code></td><td><code>icdo:9832/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic Leukemia, B-Cell Type</code></td><td><code>icdo:9833/3</code></td><td></td></tr>
<tr><td><code>Prolymphocytic Leukemia, T-Cell Type</code></td><td><code>icdo:9834/3</code></td><td></td></tr>
<tr><td><code>Precursor Cell Lymphoblastic Leukemia, Nos</code></td><td><code>icdo:9835/3</code></td><td></td></tr>
<tr><td><code>Precursor B-Cell Lymphoblastic Leukemia</code></td><td><code>icdo:9836/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia, M6 Type</code></td><td><code>icdo:9840/3</code></td><td></td></tr>
<tr><td><code>Myeloid Leukemia, Nos</code></td><td><code>icdo:9860/3</code></td><td></td></tr>
<tr><td><code>Chronic Myeloid Leukemia, Nos</code></td><td><code>icdo:9863/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With T(6;9)(P23;Q34) Dek-Nup214</code></td><td><code>icdo:9865/3</code></td><td></td></tr>
<tr><td><code>Acute Promyelocytic Leuk.,T(15;17)(Q22;Q11-12)</code></td><td><code>icdo:9866/3</code></td><td></td></tr>
<tr><td><code>Acute Myelomonocytic Leukemia</code></td><td><code>icdo:9867/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Inv(3)(Q21Q26.2) Or</code></td><td><code>icdo:9869/3</code></td><td></td></tr>
<tr><td><code>Acute Basophilic Leukemia</code></td><td><code>icdo:9870/3</code></td><td></td></tr>
<tr><td><code>Ac. Myelomonocytic Leuk. W Abn. Mar. Eosinophils</code></td><td><code>icdo:9871/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia, Minimal Differentiation</code></td><td><code>icdo:9872/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia Without Maturation</code></td><td><code>icdo:9873/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Maturation</code></td><td><code>icdo:9874/3</code></td><td></td></tr>
<tr><td><code>Chronic Myelogenous Leukemia, Bcr/Abl Positive</code></td><td><code>icdo:9875/3</code></td><td></td></tr>
<tr><td><code>Atypical Chronic Myeloid Leuk., Bcr/Abl Negative</code></td><td><code>icdo:9876/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Mutated Npm1</code></td><td><code>icdo:9877/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Biallelic Mutations Of Cebpa</code></td><td><code>icdo:9878/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Mutated Runx1</code></td><td><code>icdo:9879/3</code></td><td></td></tr>
<tr><td><code>Acute Monocytic Leukemia</code></td><td><code>icdo:9891/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Multilineage Dysplasia</code></td><td><code>icdo:9895/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia, T(8;21)(Q22;Q22)</code></td><td><code>icdo:9896/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia, 11Q23 Abnormalities</code></td><td><code>icdo:9897/3</code></td><td></td></tr>
<tr><td><code>Myeloid Leukemia Associated With Down Syndrome</code></td><td><code>icdo:9898/3</code></td><td></td></tr>
<tr><td><code>Acute Megakaryoblastic Leukemia</code></td><td><code>icdo:9910/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia (Megakaryoblastic) With</code></td><td><code>icdo:9911/3</code></td><td></td></tr>
<tr><td><code>Acute Myeloid Leukemia With Bcr-Abl1</code></td><td><code>icdo:9912/3</code></td><td></td></tr>
<tr><td><code>Therapy-Related Acute Myeloid Leukemia, Nos</code></td><td><code>icdo:9920/3</code></td><td></td></tr>
<tr><td><code>Myeloid Sarcoma</code></td><td><code>icdo:9930/3</code></td><td></td></tr>
<tr><td><code>Acute Panmyelosis With Myelofibrosis</code></td><td><code>icdo:9931/3</code></td><td></td></tr>
<tr><td><code>Hairy Cell Leukemia</code></td><td><code>icdo:9940/3</code></td><td></td></tr>
<tr><td><code>Chronic Myelomonocytic Leukemia, Nos</code></td><td><code>icdo:9945/3</code></td><td></td></tr>
<tr><td><code>Juvenile Myelomonocytic Leukemia</code></td><td><code>icdo:9946/3</code></td><td></td></tr>
<tr><td><code>Aggressive Nk-Cell Leukemia</code></td><td><code>icdo:9948/3</code></td><td></td></tr>
<tr><td><code>Polycythemia Vera</code></td><td><code>icdo:9950/3</code></td><td></td></tr>
<tr><td><code>Chronic Myeloproliferative Disease, Nos</code></td><td><code>icdo:9960/3</code></td><td></td></tr>
<tr><td><code>Myelosclerosis With Myeloid Metaplasia</code></td><td><code>icdo:9961/3</code></td><td></td></tr>
<tr><td><code>Essential Thrombocythemia</code></td><td><code>icdo:9962/3</code></td><td></td></tr>
<tr><td><code>Chronic Neutrophilic Leukemia</code></td><td><code>icdo:9963/3</code></td><td></td></tr>
<tr><td><code>Hypereosinophilic Syndrome</code></td><td><code>icdo:9964/3</code></td><td></td></tr>
<tr><td><code>Refractory Anemia</code></td><td><code>icdo:9980/3</code></td><td></td></tr>
<tr><td><code>Refractory Anemia With Sideroblasts</code></td><td><code>icdo:9982/3</code></td><td></td></tr>
<tr><td><code>Refractory Anemia With Excess Blasts</code></td><td><code>icdo:9983/3</code></td><td></td></tr>
<tr><td><code>Refract. Anemia With Excess Blasts In Transformation</code></td><td><code>icdo:9984/3</code></td><td></td></tr>
<tr><td><code>Refractory Cytopenia With Multilineage Dysplasia</code></td><td><code>icdo:9985/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic Syndr. With 5Q Deletion Syndrome</code></td><td><code>icdo:9986/3</code></td><td></td></tr>
<tr><td><code>Therapy-Related Myelodysplastic Syndrome, Nos</code></td><td><code>icdo:9987/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic Syndrome, Nos</code></td><td><code>icdo:9989/3</code></td><td></td></tr>
<tr><td><code>Refractory Neutropenia</code></td><td><code>icdo:9991/3</code></td><td></td></tr>
<tr><td><code>Refractory Thrombocytopenia</code></td><td><code>icdo:9992/3</code></td><td></td></tr>
<tr><td><code>Myelodysplastic Syndrome With Ring Sideroblasts And Multilineage</code></td><td><code>icdo:9993/3</code></td><td></td></tr>
<tr><td><code>Trichilemmocarcinoma</code></td><td><code>icdo:8102/3</code></td><td></td></tr>
<tr><td><code>Pilomatrix Carcinoma</code></td><td><code>icdo:8110/3</code></td><td></td></tr>
<tr><td><code>Merkel Cell Carcinoma</code></td><td><code>icdo:8247/3</code></td><td></td></tr>
<tr><td><code>Skin Appendage Carcinoma</code></td><td><code>icdo:8390/3</code></td><td></td></tr>
<tr><td><code>Sweat Gland Adenocarcinoma</code></td><td><code>icdo:8400/3</code></td><td></td></tr>
<tr><td><code>Nodular Hidradenoma, Malignant</code></td><td><code>icdo:8402/3</code></td><td></td></tr>
<tr><td><code>Malignant Eccrine Spiradenoma</code></td><td><code>icdo:8403/3</code></td><td></td></tr>
<tr><td><code>Sclerosing Sweat Duct Carcinoma</code></td><td><code>icdo:8407/3</code></td><td></td></tr>
<tr><td><code>Eccrine Papillary Adenocarcinoma</code></td><td><code>icdo:8408/3</code></td><td></td></tr>
<tr><td><code>Eccrine Poroma, Malignant</code></td><td><code>icdo:8409/3</code></td><td></td></tr>
<tr><td><code>Sebaceous Adenocarcinoma</code></td><td><code>icdo:8410/3</code></td><td></td></tr>
<tr><td><code>Eccrine Adenocarcinoma</code></td><td><code>icdo:8413/3</code></td><td></td></tr>
<tr><td><code>Ceruminous Adenocarcinoma</code></td><td><code>icdo:8420/3</code></td><td></td></tr>
<tr><td><code>Mal. Melanoma In Junctional Nevus</code></td><td><code>icdo:8740/3</code></td><td></td></tr>
<tr><td><code>Precancerous Melanosis, NOS</code></td><td><code>icdo:8741/2</code></td><td></td></tr>
<tr><td><code>Mal. Melanoma In Precan. Melanosis</code></td><td><code>icdo:8741/3</code></td><td></td></tr>
<tr><td><code>Lentigo Maligna</code></td><td><code>icdo:8742/2</code></td><td></td></tr>
<tr><td><code>Lentigo Maligna Melanoma</code></td><td><code>icdo:8742/3</code></td><td></td></tr>
<tr><td><code>Superficial Spreading Melanoma, In Situ</code></td><td><code>icdo:8743/2</code></td><td></td></tr>
<tr><td><code>Acral Lentiginous Melanoma, Malig.</code></td><td><code>icdo:8744/3</code></td><td></td></tr>
<tr><td><code>Blue Nevus, Malignant</code></td><td><code>icdo:8780/3</code></td><td></td></tr>
<tr><td><code>Dermatofibrosarcoma, Nos</code></td><td><code>icdo:8832/3</code></td><td></td></tr>
<tr><td><code>Pigmented Dermatofibrosarcoma Protuberans</code></td><td><code>icdo:8833/3</code></td><td></td></tr>
<tr><td><code>Primary Cutaneous Follicle Centre Lymphoma</code></td><td><code>icdo:9597/3</code></td><td></td></tr>
<tr><td><code>Hydroa Vacciniforme-Like Lymphoma</code></td><td><code>icdo:9725/3</code></td><td></td></tr>
<tr><td><code>Primary Cutaneous Gamma-Delta T-Cell Lymphoma</code></td><td><code>icdo:9726/3</code></td><td></td></tr>
<tr><td><code>Granular Cell Tumor, Malignant</code></td><td><code>icdo:9580/3</code></td><td></td></tr>
<tr><td><code>Alveolar Soft Part Sarcoma</code></td><td><code>icdo:9581/3</code></td><td></td></tr>
<tr><td><code>Low-Grade Serous Carcinoma</code></td><td><code>icdo:8460/3</code></td><td></td></tr>
<tr><td><code>High-Grade Serous Carcinoma</code></td><td><code>icdo:8461/3</code></td><td></td></tr>
<tr><td><code>Endometrial Stromal Sarcoma</code></td><td><code>icdo:8930/3</code></td><td></td></tr>
<tr><td><code>Endometrial Stromal Sarcoma, Low Grade</code></td><td><code>icdo:8931/3</code></td><td></td></tr>
<tr><td><code>Myeloid And Lymphoid Neoplasms With Pdgfrb Re Arrangement</code></td><td><code>icdo:9966/3</code></td><td></td></tr>
<tr><td><code>Myeloid/Lymphoid Neoplasm With Pcm1-Jak2</code></td><td><code>icdo:9968/3</code></td><td></td></tr>
<tr><td><code>Lipid-Rich Carcinoma</code></td><td><code>icdo:8314/3</code></td><td></td></tr>
<tr><td><code>Glycogen-Rich Carcinoma</code></td><td><code>icdo:8315/3</code></td><td></td></tr>
<tr><td><code>Invasive Micropapillary Carcinoma</code></td><td><code>icdo:8507/3</code></td><td></td></tr>
<tr><td><code>Solid Papillary Carcinoma In Situ</code></td><td><code>icdo:8509/2</code></td><td></td></tr>
<tr><td><code>Solid Papillary Carcinoma With Invasion</code></td><td><code>icdo:8509/3</code></td><td></td></tr>
<tr><td><code>Atypical Medullary Carcinoma</code></td><td><code>icdo:8513/3</code></td><td></td></tr>
<tr><td><code>Pleomorphic Lobular Carcinoma In Situ</code></td><td><code>icdo:8519/2</code></td><td></td></tr>
<tr><td><code>Lobular Carcinoma In Situ</code></td><td><code>icdo:8520/2</code></td><td></td></tr>
<tr><td><code>Lobular Carcinoma, Nos</code></td><td><code>icdo:8520/3</code></td><td></td></tr>
<tr><td><code>Intraductal And Lobular In Situ Carcinoma</code></td><td><code>icdo:8522/2</code></td><td></td></tr>
<tr><td><code>Infiltrating Duct And Lobular Carcinoma</code></td><td><code>icdo:8522/3</code></td><td></td></tr>
<tr><td><code>Infiltr. Duct Mixed With Other Types Of Carcinoma, In Situ</code></td><td><code>icdo:8523/2</code></td><td></td></tr>
<tr><td><code>Infiltr. Duct Mixed With Other Types Of Carcinoma</code></td><td><code>icdo:8523/3</code></td><td></td></tr>
<tr><td><code>Infiltrating Lobular Mixed With Other Types Of Carc.</code></td><td><code>icdo:8524/3</code></td><td></td></tr>
<tr><td><code>Inflammatory Carcinoma</code></td><td><code>icdo:8530/3</code></td><td></td></tr>
<tr><td><code>Paget Disease, Mammary</code></td><td><code>icdo:8540/3</code></td><td></td></tr>
<tr><td><code>Paget Dis. &amp; Infil. Duct Carcinoma</code></td><td><code>icdo:8541/3</code></td><td></td></tr>
<tr><td><code>Paget Disease And Intraductal Ca.</code></td><td><code>icdo:8543/3</code></td><td></td></tr>
<tr><td><code>Adenomyoepithelioma With Carcinoma</code></td><td><code>icdo:8983/3</code></td><td></td></tr>
<tr><td><code>Phyllodes Tumor, Malignant</code></td><td><code>icdo:9020/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Keratinizing, Nos, In Situ</code></td><td><code>icdo:8071/2</code></td><td></td></tr>
<tr><td><code>Basal Cell Carcinoma, Nos</code></td><td><code>icdo:8090/3</code></td><td></td></tr>
<tr><td><code>Multifocal Superficial Basal Cell Carcinoma</code></td><td><code>icdo:8091/3</code></td><td></td></tr>
<tr><td><code>Infiltrating Basal Cell Carcinoma, Nos</code></td><td><code>icdo:8092/3</code></td><td></td></tr>
<tr><td><code>Basal Cell Carcinoma, Fibroepithelial</code></td><td><code>icdo:8093/3</code></td><td></td></tr>
<tr><td><code>Basosquamous Carcinoma</code></td><td><code>icdo:8094/3</code></td><td></td></tr>
<tr><td><code>Metatypical Carcinoma</code></td><td><code>icdo:8095/3</code></td><td></td></tr>
<tr><td><code>Basal Cell Carcinoma, Nodular</code></td><td><code>icdo:8097/3</code></td><td></td></tr>
<tr><td><code>Adenoid Basal Cell Carcinoma</code></td><td><code>icdo:8098/3</code></td><td></td></tr>
<tr><td><code>Mucinous Adenocarcinoma, Endocervical Type</code></td><td><code>icdo:8482/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, Hpv-Associated</code></td><td><code>icdo:8483/3</code></td><td></td></tr>
<tr><td><code>Phyllodes Tumor, Malignant (9092/3)</code></td><td><code>icdo:9092/3</code></td><td></td></tr>
<tr><td><code>Sq. Cell Carcinoma, Lg. Cell, Non-Ker., In Situ</code></td><td><code>icdo:8072/2</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, Endocervical Type</code></td><td><code>icdo:8384/3</code></td><td></td></tr>
<tr><td><code>Adenocarcinoma, Hpv-Independent, Nos</code></td><td><code>icdo:8484/3</code></td><td></td></tr>
<tr><td><code>Endometrioid Intraepithelial Neoplasia</code></td><td><code>icdo:8380/2</code></td><td></td></tr>
<tr><td><code>Endometrioid Adenofibroma, Malignant</code></td><td><code>icdo:8381/3</code></td><td></td></tr>
<tr><td><code>Endometrioid Adenocarcinoma, Secretory Variant</code></td><td><code>icdo:8382/3</code></td><td></td></tr>
<tr><td><code>Endometrioid Adenocarcinoma, Ciliated Cell Variant</code></td><td><code>icdo:8383/3</code></td><td></td></tr>
<tr><td><code>Serous Tubal Intraepithelial Carcinoma</code></td><td><code>icdo:8441/2</code></td><td></td></tr>
<tr><td><code>Mesonephric-Like Adenocarcinoma</code></td><td><code>icdo:9111/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Adenocarcinofibroma</code></td><td><code>icdo:8313/3</code></td><td></td></tr>
<tr><td><code>Serous Cystadenoma, Borderline Malignancy (C56.9)</code></td><td><code>icdo:8442/1</code></td><td></td></tr>
<tr><td><code>Papillary Cystadenoma, Borderline Malignancy (C56.9)</code></td><td><code>icdo:8451/1</code></td><td></td></tr>
<tr><td><code>Non-Invasive Low Grade Serous Carcinoma</code></td><td><code>icdo:8460/2</code></td><td></td></tr>
<tr><td><code>Serous Papillary Cystic Tumor Of Borderline Malignancy (C56.9)</code></td><td><code>icdo:8462/1</code></td><td></td></tr>
<tr><td><code>Mucinous Cystic Tumor Of Borderline Malignancy (C56.9)</code></td><td><code>icdo:8472/1</code></td><td></td></tr>
<tr><td><code>Papillary Mucinous Cystadenoma, Borderline Malignancy (C56.9)</code></td><td><code>icdo:8473/1</code></td><td></td></tr>
<tr><td><code>Seromucinous Carcinoma</code></td><td><code>icdo:8474/3</code></td><td></td></tr>
<tr><td><code>Ovarian Stromal Tumor, Mal.</code></td><td><code>icdo:8590/3</code></td><td></td></tr>
<tr><td><code>Thecoma, Malignant</code></td><td><code>icdo:8600/3</code></td><td></td></tr>
<tr><td><code>Granulosa Cell Tumor, Malignant</code></td><td><code>icdo:8620/3</code></td><td></td></tr>
<tr><td><code>Granulosa Cell-Theca Cell Tumor, Mal.</code></td><td><code>icdo:8621/3</code></td><td></td></tr>
<tr><td><code>Androblastoma, Malignant</code></td><td><code>icdo:8630/3</code></td><td></td></tr>
<tr><td><code>Sertoli-Leydig Cell Tumor, Poorly Differentiated</code></td><td><code>icdo:8631/3</code></td><td></td></tr>
<tr><td><code>Gynandroblastoma, Malignant</code></td><td><code>icdo:8632/3</code></td><td></td></tr>
<tr><td><code>Sertoli-Leydig Cl Tum., P.D. W Heterologous Elements</code></td><td><code>icdo:8634/3</code></td><td></td></tr>
<tr><td><code>Steroid Cell Tumor, Malignant</code></td><td><code>icdo:8670/3</code></td><td></td></tr>
<tr><td><code>Brenner Tumor, Malignant</code></td><td><code>icdo:9000/3</code></td><td></td></tr>
<tr><td><code>Serous Adenocarcinofibroma</code></td><td><code>icdo:9014/3</code></td><td></td></tr>
<tr><td><code>Mucinous Adenocarcinofibroma</code></td><td><code>icdo:9015/3</code></td><td></td></tr>
<tr><td><code>Struma Ovarii, Malignant</code></td><td><code>icdo:9090/3</code></td><td></td></tr>
<tr><td><code>Malignant Placental Site Trophoblastic Tumor</code></td><td><code>icdo:9104/3</code></td><td></td></tr>
<tr><td><code>Warty Carcinoma</code></td><td><code>icdo:8054/3</code></td><td></td></tr>
<tr><td><code>Queyrat Erythroplasia</code></td><td><code>icdo:8080/2</code></td><td></td></tr>
<tr><td><code>Sertoli Cell Carcinoma</code></td><td><code>icdo:8640/3</code></td><td></td></tr>
<tr><td><code>Leydig Cell Tumor, Malignant</code></td><td><code>icdo:8650/3</code></td><td></td></tr>
<tr><td><code>Intratubular Malignant Germ Cells</code></td><td><code>icdo:9064/2</code></td><td></td></tr>
<tr><td><code>Malignant Teratoma, Trophoblastic</code></td><td><code>icdo:9102/3</code></td><td></td></tr>
<tr><td><code>Hereditary Leiomyomatosis And Rcc-Associated Renal Cell Carcinoma</code></td><td><code>icdo:8311/3</code></td><td></td></tr>
<tr><td><code>Renal Cell Carcinoma</code></td><td><code>icdo:8312/3</code></td><td></td></tr>
<tr><td><code>Cyst-Associated Renal Cell Carcinoma</code></td><td><code>icdo:8316/3</code></td><td></td></tr>
<tr><td><code>Renal Cell Carcinoma, Chromophobe Type</code></td><td><code>icdo:8317/3</code></td><td></td></tr>
<tr><td><code>Renal Cell Carcinoma, Sarcomatoid</code></td><td><code>icdo:8318/3</code></td><td></td></tr>
<tr><td><code>Collecting Duct Carcinoma</code></td><td><code>icdo:8319/3</code></td><td></td></tr>
<tr><td><code>Malignant Cystic Nephroma</code></td><td><code>icdo:8959/3</code></td><td></td></tr>
<tr><td><code>Nephroblastoma, Nos</code></td><td><code>icdo:8960/3</code></td><td></td></tr>
<tr><td><code>Malignant Rhabdoid Tumor</code></td><td><code>icdo:8963/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Sarcoma Of Kidney</code></td><td><code>icdo:8964/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Melanoma, Type A</code></td><td><code>icdo:8773/3</code></td><td></td></tr>
<tr><td><code>Spindle Cell Melanoma, Type B</code></td><td><code>icdo:8774/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, Nos</code></td><td><code>icdo:9510/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, Differentiated</code></td><td><code>icdo:9511/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, Undifferentiated</code></td><td><code>icdo:9512/3</code></td><td></td></tr>
<tr><td><code>Retinoblastoma, Diffuse</code></td><td><code>icdo:9513/3</code></td><td></td></tr>
<tr><td><code>Neoplasm, Benign</code></td><td><code>icdo:8000/0</code></td><td></td></tr>
<tr><td><code>Neoplasm, Uncertain Whether Benign Or Malignant</code></td><td><code>icdo:8000/1</code></td><td></td></tr>
<tr><td><code>Tumor Cells, Benign</code></td><td><code>icdo:8001/0</code></td><td></td></tr>
<tr><td><code>Tumor Cells, Uncertain Whether Benign Or Malignant</code></td><td><code>icdo:8001/1</code></td><td></td></tr>
<tr><td><code>Diffuse Melanocytosis</code></td><td><code>icdo:8728/0</code></td><td></td></tr>
<tr><td><code>Meningeal Melanocytoma</code></td><td><code>icdo:8728/1</code></td><td></td></tr>
<tr><td><code>Meningeal Melanomatosis</code></td><td><code>icdo:8728/3</code></td><td></td></tr>
<tr><td><code>Soft Tissue Tumor, Benign</code></td><td><code>icdo:8800/0</code></td><td></td></tr>
<tr><td><code>Fibroma, Nos</code></td><td><code>icdo:8810/0</code></td><td></td></tr>
<tr><td><code>Lipoma, Nos</code></td><td><code>icdo:8850/0</code></td><td></td></tr>
<tr><td><code>Angiolipoma, Nos</code></td><td><code>icdo:8861/0</code></td><td></td></tr>
<tr><td><code>Teratoma, Benign</code></td><td><code>icdo:9080/0</code></td><td></td></tr>
<tr><td><code>Teratoma, NOS</code></td><td><code>icdo:9080/1</code></td><td></td></tr>
<tr><td><code>Dermoid Cyst, NOS</code></td><td><code>icdo:9084/0</code></td><td></td></tr>
<tr><td><code>Cavernous Hemangioma</code></td><td><code>icdo:9121/0</code></td><td></td></tr>
<tr><td><code>Hemangiopericytoma, Benign</code></td><td><code>icdo:9150/0</code></td><td></td></tr>
<tr><td><code>Meningiomatosis, NOS</code></td><td><code>icdo:9530/1</code></td><td></td></tr>
<tr><td><code>Meningioma, Malignant</code></td><td><code>icdo:9530/3</code></td><td></td></tr>
<tr><td><code>Meningothelial Meningioma</code></td><td><code>icdo:9531/0</code></td><td></td></tr>
<tr><td><code>Fibrous Meningioma</code></td><td><code>icdo:9532/0</code></td><td></td></tr>
<tr><td><code>Psammomatous Meningioma</code></td><td><code>icdo:9533/0</code></td><td></td></tr>
<tr><td><code>Angiomatous Meningioma</code></td><td><code>icdo:9534/0</code></td><td></td></tr>
<tr><td><code>Transitional Meningioma</code></td><td><code>icdo:9537/0</code></td><td></td></tr>
<tr><td><code>Clear Cell Meningioma</code></td><td><code>icdo:9538/1</code></td><td></td></tr>
<tr><td><code>Papillary Meningioma</code></td><td><code>icdo:9538/3</code></td><td></td></tr>
<tr><td><code>Atypical Meningioma</code></td><td><code>icdo:9539/1</code></td><td></td></tr>
<tr><td><code>Meningeal Sarcomatosis</code></td><td><code>icdo:9539/3</code></td><td></td></tr>
<tr><td><code>Paraganglioma, Nos</code></td><td><code>icdo:8680/1</code></td><td></td></tr>
<tr><td><code>Solitary Fibrous Tumor/Hemangiopericytoma Grade 2</code></td><td><code>icdo:8815/1</code></td><td></td></tr>
<tr><td><code>Venous Hemangioma</code></td><td><code>icdo:9122/0</code></td><td></td></tr>
<tr><td><code>Capillary Hemangioma</code></td><td><code>icdo:9131/0</code></td><td></td></tr>
<tr><td><code>Glioma, Malignant</code></td><td><code>icdo:9380/3</code></td><td></td></tr>
<tr><td><code>Gliomatosis Cerebri</code></td><td><code>icdo:9381/3</code></td><td></td></tr>
<tr><td><code>Mixed Glioma</code></td><td><code>icdo:9382/3</code></td><td></td></tr>
<tr><td><code>Supependymal Giant Cell Astrocytoma</code></td><td><code>icdo:9384/1</code></td><td></td></tr>
<tr><td><code>Diffuse Midline Glioma, H3 K27M-Mutant</code></td><td><code>icdo:9385/3</code></td><td></td></tr>
<tr><td><code>Sellar Ependymoma</code></td><td><code>icdo:9391/1</code></td><td></td></tr>
<tr><td><code>Ependymoma, NOS</code></td><td><code>icdo:9391/3</code></td><td></td></tr>
<tr><td><code>Ependymoma, Anaplastic</code></td><td><code>icdo:9392/3</code></td><td></td></tr>
<tr><td><code>Papillary Ependymoma</code></td><td><code>icdo:9393/3</code></td><td></td></tr>
<tr><td><code>Ependymoma, Rela Fusion-Positive</code></td><td><code>icdo:9396/3</code></td><td></td></tr>
<tr><td><code>Astrocytoma, Anaplastic</code></td><td><code>icdo:9401/3</code></td><td></td></tr>
<tr><td><code>Protoplasmic Astrocytoma</code></td><td><code>icdo:9410/3</code></td><td></td></tr>
<tr><td><code>Gemistocytic Astrocytoma</code></td><td><code>icdo:9411/3</code></td><td></td></tr>
<tr><td><code>Desmoplastic Infantile Astrocytoma</code></td><td><code>icdo:9412/1</code></td><td></td></tr>
<tr><td><code>Fibrillary Astrocytoma</code></td><td><code>icdo:9420/3</code></td><td></td></tr>
<tr><td><code>Polar Spongioblastoma</code></td><td><code>icdo:9423/3</code></td><td></td></tr>
<tr><td><code>Glioblastoma, Nos</code></td><td><code>icdo:9440/3</code></td><td></td></tr>
<tr><td><code>Giant Cell Glioblastoma</code></td><td><code>icdo:9441/3</code></td><td></td></tr>
<tr><td><code>Chordoid Glioma</code></td><td><code>icdo:9444/1</code></td><td></td></tr>
<tr><td><code>Glioblastoma, Idh-Mutant</code></td><td><code>icdo:9445/3</code></td><td></td></tr>
<tr><td><code>Oligodendroglioma, Nos</code></td><td><code>icdo:9450/3</code></td><td></td></tr>
<tr><td><code>Oligodendroglioma, Anaplastic</code></td><td><code>icdo:9451/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, Wnt-Activated</code></td><td><code>icdo:9475/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, Shh-Activated And Tp53-Mutant</code></td><td><code>icdo:9476/3</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, Non-Wnt/Non-Shh</code></td><td><code>icdo:9477/3</code></td><td></td></tr>
<tr><td><code>Embryonal Tumor With Multilayered Rosettes, Nos</code></td><td><code>icdo:9478/3</code></td><td></td></tr>
<tr><td><code>Multinodular And Vascolating Neuronal Tumor</code></td><td><code>icdo:9505/0</code></td><td></td></tr>
<tr><td><code>Ganglioglioma, Nos</code></td><td><code>icdo:9505/1</code></td><td></td></tr>
<tr><td><code>Atypical Teratoid/Rhabdoid Tumor</code></td><td><code>icdo:9508/3</code></td><td></td></tr>
<tr><td><code>Neurofibroma, Nos</code></td><td><code>icdo:9540/0</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis, Nos</code></td><td><code>icdo:9540/1</code></td><td></td></tr>
<tr><td><code>Melanotic Neurofibroma</code></td><td><code>icdo:9541/0</code></td><td></td></tr>
<tr><td><code>Plexiform Neurofibroma</code></td><td><code>icdo:9550/0</code></td><td></td></tr>
<tr><td><code>Neurilemoma, Nos</code></td><td><code>icdo:9560/0</code></td><td></td></tr>
<tr><td><code>Melanotic Schwannoma</code></td><td><code>icdo:9560/1</code></td><td></td></tr>
<tr><td><code>Choroid Plexus Papilloma, NOS</code></td><td><code>icdo:9390/0</code></td><td></td></tr>
<tr><td><code>Choroid Plexus Papilloma, Malignant</code></td><td><code>icdo:9390/3</code></td><td></td></tr>
<tr><td><code>Centrol Neurocytoma</code></td><td><code>icdo:9506/1</code></td><td></td></tr>
<tr><td><code>Medulloblastoma, Nos</code></td><td><code>icdo:9470/3</code></td><td></td></tr>
<tr><td><code>Desmoplastic Medulloblastoma</code></td><td><code>icdo:9471/3</code></td><td></td></tr>
<tr><td><code>Large Cell Medulloblastoma</code></td><td><code>icdo:9474/3</code></td><td></td></tr>
<tr><td><code>Cerebellar Sarcoma, NOS</code></td><td><code>icdo:9480/3</code></td><td></td></tr>
<tr><td><code>Dysplastic Gangliocytoma Of Cerebellum (Lhermitte-Duclos)</code></td><td><code>icdo:9493/0</code></td><td></td></tr>
<tr><td><code>Multinodular And Vacuolating Neuronal Tumor</code></td><td><code>icdo:9509/0</code></td><td></td></tr>
<tr><td><code>Atypical Lipoma</code></td><td><code>icdo:8850/1</code></td><td></td></tr>
<tr><td><code>Leiomyoma, Nos</code></td><td><code>icdo:8890/0</code></td><td></td></tr>
<tr><td><code>Leiomyomatosis, NOS</code></td><td><code>icdo:8890/1</code></td><td></td></tr>
<tr><td><code>Smooth Muscle Tumor, NOS</code></td><td><code>icdo:8897/1</code></td><td></td></tr>
<tr><td><code>Hemangioendothelioma, Benign</code></td><td><code>icdo:9130/0</code></td><td></td></tr>
<tr><td><code>Follicular Adenocarcinoma, NOS</code></td><td><code>icdo:8330/3</code></td><td></td></tr>
<tr><td><code>Follicular Adenocarcinoma Well Diff.</code></td><td><code>icdo:8331/3</code></td><td></td></tr>
<tr><td><code>Follicular Adenocarcinoma Trabecular</code></td><td><code>icdo:8332/3</code></td><td></td></tr>
<tr><td><code>Follicular Carcinoma, Minimally Invasive</code></td><td><code>icdo:8335/3</code></td><td></td></tr>
<tr><td><code>Insular Carcinoma</code></td><td><code>icdo:8337/3</code></td><td></td></tr>
<tr><td><code>Follicular Thyroid Carcinoma (Ftc), Encapsulated Angioinvasive</code></td><td><code>icdo:8339/3</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma, Follicular Variant</code></td><td><code>icdo:8340/3</code></td><td></td></tr>
<tr><td><code>Papillary Microcarcinoma</code></td><td><code>icdo:8341/3</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma, Oxyphilic Cell</code></td><td><code>icdo:8342/3</code></td><td></td></tr>
<tr><td><code>Non-Invasive Efvptc</code></td><td><code>icdo:8343/2</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma, Encapsulated</code></td><td><code>icdo:8343/3</code></td><td></td></tr>
<tr><td><code>Papillary Carcinoma, Columnar Cell</code></td><td><code>icdo:8344/3</code></td><td></td></tr>
<tr><td><code>Medullary Carcinoma With Amyloid Stroma</code></td><td><code>icdo:8345/3</code></td><td></td></tr>
<tr><td><code>Mixed Medullary-Follicular Carcinoma</code></td><td><code>icdo:8346/3</code></td><td></td></tr>
<tr><td><code>Mixed Medullary-Papillary Carcinoma</code></td><td><code>icdo:8347/3</code></td><td></td></tr>
<tr><td><code>Nonencapsulated Sclerosing Carcinoma</code></td><td><code>icdo:8350/3</code></td><td></td></tr>
<tr><td><code>Adrenal Cortical Carcinoma</code></td><td><code>icdo:8370/3</code></td><td></td></tr>
<tr><td><code>Water-Clear Cell Adenocarcinoma</code></td><td><code>icdo:8322/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Tumor, NOS</code></td><td><code>icdo:8005/0</code></td><td></td></tr>
<tr><td><code>Epithelial Tumor, Benign</code></td><td><code>icdo:8010/0</code></td><td></td></tr>
<tr><td><code>Monomorphic Adenoma</code></td><td><code>icdo:8146/0</code></td><td></td></tr>
<tr><td><code>Papillary Adenoma, NOS</code></td><td><code>icdo:8260/0</code></td><td></td></tr>
<tr><td><code>Chromophobe Adenoma</code></td><td><code>icdo:8270/0</code></td><td></td></tr>
<tr><td><code>Chromophobe Carcinoma</code></td><td><code>icdo:8270/3</code></td><td></td></tr>
<tr><td><code>Pituitary Adenoma, NOS</code></td><td><code>icdo:8272/0</code></td><td></td></tr>
<tr><td><code>Pituitary Carcinoma, NOS</code></td><td><code>icdo:8272/3</code></td><td></td></tr>
<tr><td><code>Pituitary Blastoma</code></td><td><code>icdo:8273/3</code></td><td></td></tr>
<tr><td><code>Acidophil Adenoma</code></td><td><code>icdo:8280/0</code></td><td></td></tr>
<tr><td><code>Acidophil Carcinoma</code></td><td><code>icdo:8280/3</code></td><td></td></tr>
<tr><td><code>Mixed Acidophil-Basophil Adenoma</code></td><td><code>icdo:8281/0</code></td><td></td></tr>
<tr><td><code>Mixed Acidophil-Basophil Carcinoma</code></td><td><code>icdo:8281/3</code></td><td></td></tr>
<tr><td><code>Oxyphilic Adenoma</code></td><td><code>icdo:8290/0</code></td><td></td></tr>
<tr><td><code>Basophil Adenoma</code></td><td><code>icdo:8300/0</code></td><td></td></tr>
<tr><td><code>Basophil Carcinoma</code></td><td><code>icdo:8300/3</code></td><td></td></tr>
<tr><td><code>Clear Cell Adenoma</code></td><td><code>icdo:8310/0</code></td><td></td></tr>
<tr><td><code>Mixed Cell Adenoma</code></td><td><code>icdo:8323/0</code></td><td></td></tr>
<tr><td><code>Granular Cell Tumor, NOS</code></td><td><code>icdo:9580/0</code></td><td></td></tr>
<tr><td><code>Granular Cell Tumor Of The Sellar Region</code></td><td><code>icdo:9582/0</code></td><td></td></tr>
<tr><td><code>Pinealoma, NOS</code></td><td><code>icdo:9360/1</code></td><td></td></tr>
<tr><td><code>Pineoblastoma</code></td><td><code>icdo:9362/3</code></td><td></td></tr>
<tr><td><code>Papillary Tumor Of Pineal Region</code></td><td><code>icdo:9395/3</code></td><td></td></tr>
<tr><td><code>Parasympathetic Paraganglioma</code></td><td><code>icdo:8682/3</code></td><td></td></tr>
<tr><td><code>Middle Ear Paraganglioma</code></td><td><code>icdo:8690/3</code></td><td></td></tr>
<tr><td><code>Aortic Body Tumor, Malignant</code></td><td><code>icdo:8691/3</code></td><td></td></tr>
<tr><td><code>Carotid Body Tumor, Malignant</code></td><td><code>icdo:8692/3</code></td><td></td></tr>
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
<tr><td><code>FPRH</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Off Therapy</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Abdominal Wall</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Acetabulum</code></td><td><code>ncit:C32042</code></td><td></td></tr>
<tr><td><code>Adjacent Organ</code></td><td><code>ncit:C180347</code></td><td></td></tr>
<tr><td><code>Adrenal Gland</code></td><td><code>ncit:C12666</code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Ankle</code></td><td><code>ncit:C32078</code></td><td></td></tr>
<tr><td><code>Ankle Joint</code></td><td><code>ncit:C32078</code></td><td></td></tr>
<tr><td><code>Anterior Skull Base</code></td><td><code>ncit:C180372</code></td><td></td></tr>
<tr><td><code>Anus</code></td><td><code>ncit:C43362</code></td><td></td></tr>
<tr><td><code>Appendix</code></td><td><code>ncit:C12380</code></td><td></td></tr>
<tr><td><code>Ascitic Fluid</code></td><td><code>ncit:C159203</code></td><td></td></tr>
<tr><td><code>Axilla</code></td><td><code>ncit:C12674</code></td><td></td></tr>
<tr><td><code>Axilla or Pectoral</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Axillary Nodes</code></td><td><code>ncit:C12904</code></td><td></td></tr>
<tr><td><code>Basal Ganglia-Thalamus</code></td><td><code>ncit:C158080</code></td><td></td></tr>
<tr><td><code>Basin</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Bladder</code></td><td><code>ncit:C12414</code></td><td></td></tr>
<tr><td><code>Bladder/Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Bone Face</code></td><td><code>ncit:C63706</code></td><td></td></tr>
<tr><td><code>Bone Foot</code></td><td><code>ncit:C13068</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone Shoulder Girdle</code></td><td><code>ncit:C33547</code></td><td></td></tr>
<tr><td><code>Bone or Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Brain/Leptomeninges</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Bronchus</code></td><td><code>ncit:C12683</code></td><td></td></tr>
<tr><td><code>Buttock</code></td><td><code>ncit:C89806</code></td><td></td></tr>
<tr><td><code>Calcaneum</code></td><td><code>ncit:C32250</code></td><td></td></tr>
<tr><td><code>Carpal Bone</code></td><td><code>ncit:C12688</code></td><td></td></tr>
<tr><td><code>Cauda Equina Spinal Cord</code></td><td><code>ncit:C12689</code></td><td></td></tr>
<tr><td><code>Celiac Nodes</code></td><td><code>ncit:C65166</code></td><td></td></tr>
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
<tr><td><code>Cerebellum</code></td><td><code>ncit:C12445</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Cervical Nodes</code></td><td><code>ncit:C32298</code></td><td></td></tr>
<tr><td><code>Cervical Spine</code></td><td><code>ncit:C69313</code></td><td></td></tr>
<tr><td><code>Cervical Vertebra</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Cheek</code></td><td><code>ncit:C13070</code></td><td></td></tr>
<tr><td><code>Chest</code></td><td><code>ncit:C25389</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Choroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Clavicle</code></td><td><code>ncit:C24203</code></td><td></td></tr>
<tr><td><code>Coccyx</code></td><td><code>ncit:C12696</code></td><td></td></tr>
<tr><td><code>Colon</code></td><td><code>ncit:C12382</code></td><td></td></tr>
<tr><td><code>Cranium</code></td><td><code>ncit:C12697</code></td><td></td></tr>
<tr><td><code>Cutaneous</code></td><td><code>ncit:C13316</code></td><td></td></tr>
<tr><td><code>Dermis</code></td><td><code>ncit:C12701</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Dorsal Spine</code></td><td><code>ncit:C32472</code></td><td></td></tr>
<tr><td><code>Dorsal Vertebra</code></td><td><code>ncit:C12693</code></td><td></td></tr>
<tr><td><code>Duodenum</code></td><td><code>ncit:C12263</code></td><td></td></tr>
<tr><td><code>Elbow</code></td><td><code>ncit:C32497</code></td><td></td></tr>
<tr><td><code>Elbow Joint</code></td><td><code>ncit:C32497</code></td><td></td></tr>
<tr><td><code>Epididymis</code></td><td><code>ncit:C12328</code></td><td></td></tr>
<tr><td><code>Epitrochlear Nodes</code></td><td><code>ncit:C98182</code></td><td></td></tr>
<tr><td><code>Esophagus</code></td><td><code>ncit:C12389</code></td><td></td></tr>
<tr><td><code>Ethmoid Bone</code></td><td><code>ncit:C12711</code></td><td></td></tr>
<tr><td><code>Extra CNS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eyelid</code></td><td><code>ncit:C12713</code></td><td></td></tr>
<tr><td><code>Face</code></td><td><code>ncit:C13071</code></td><td></td></tr>
<tr><td><code>Facial Region</code></td><td><code>ncit:C13071</code></td><td></td></tr>
<tr><td><code>Fallopian Tube</code></td><td><code>ncit:C12403</code></td><td></td></tr>
<tr><td><code>Female Reproductive System Part</code></td><td><code>ncit:C13039</code></td><td></td></tr>
<tr><td><code>Femur</code></td><td><code>ncit:C12717</code></td><td></td></tr>
<tr><td><code>Fibula</code></td><td><code>ncit:C12718</code></td><td></td></tr>
<tr><td><code>Fibular Head</code></td><td><code>ncit:C32719</code></td><td></td></tr>
<tr><td><code>Finger</code></td><td><code>ncit:C32608</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Foot Bone</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Foot Joint</code></td><td><code>ncit:C32623</code></td><td></td></tr>
<tr><td><code>Foot Phalanges</code></td><td><code>ncit:C52772</code></td><td></td></tr>
<tr><td><code>Forearm</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Fourth Ventricle</code></td><td><code>ncit:C12828</code></td><td></td></tr>
<tr><td><code>Frontal Bone</code></td><td><code>ncit:C32635</code></td><td></td></tr>
<tr><td><code>Frontal Cortex</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Frontal Lobe</code></td><td><code>ncit:C12352</code></td><td></td></tr>
<tr><td><code>Gallbladder</code></td><td><code>ncit:C12377</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Tract</code></td><td><code>ncit:C34082</code></td><td></td></tr>
<tr><td><code>Groin</code></td><td><code>ncit:C12726</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hand Bone</code></td><td><code>ncit:C52771</code></td><td></td></tr>
<tr><td><code>Hand Joint</code></td><td><code>ncit:C32868</code></td><td></td></tr>
<tr><td><code>Hand Phalanges</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Head</code></td><td><code>ncit:C12419</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Heart</code></td><td><code>ncit:C12727</code></td><td></td></tr>
<tr><td><code>Hilar Nodes</code></td><td><code>ncit:C134731</code></td><td></td></tr>
<tr><td><code>Hip</code></td><td><code>ncit:C64193</code></td><td></td></tr>
<tr><td><code>Hip/Inguinal Region</code></td><td><code>ncit:C12726</code></td><td></td></tr>
<tr><td><code>Humerus</code></td><td><code>ncit:C12731</code></td><td></td></tr>
<tr><td><code>Hypodermis</code></td><td><code>ncit:C92441</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Iliac</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Iliac Crest</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Ilium</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Inferior Limb</code></td><td><code>ncit:C12982</code></td><td></td></tr>
<tr><td><code>Infraclavicular Lymph Node</code></td><td><code>ncit:C63705</code></td><td></td></tr>
<tr><td><code>Infraclavicular Nodes</code></td><td><code>ncit:C63705</code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine and Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inguinal Nodes</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Inguinal or Femoral Nodes</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Intra-Abdominal</code></td><td><code>ncit:C12726</code></td><td></td></tr>
<tr><td><code>Intraperitoneal</code></td><td><code>ncit:C13352</code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code>ncit:C105579</code></td><td></td></tr>
<tr><td><code>Intraspinal</code></td><td><code>ncit:C96908</code></td><td></td></tr>
<tr><td><code>Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Knee</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Knee Joint</code></td><td><code>ncit:C32899</code></td><td></td></tr>
<tr><td><code>Lacrimal Bone</code></td><td><code>ncit:C32906</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Lateral Ventricle</code></td><td><code>ncit:C12834</code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Leptomeningeal</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Liver/Biliary Tract</code></td><td><code>ncit:C12678</code></td><td></td></tr>
<tr><td><code>Lower Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Extremity</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lower Leg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Limb, NOS</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lower Spine</code></td><td><code>ncit:C69314</code></td><td></td></tr>
<tr><td><code>Lumbar Spinal Cord</code></td><td><code>ncit:C12895</code></td><td></td></tr>
<tr><td><code>Lumbar Spine</code></td><td><code>ncit:C69314</code></td><td></td></tr>
<tr><td><code>Lumbar Vertebra</code></td><td><code>ncit:C45874</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lung/Pleura</code></td><td><code>ncit:C12469</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Lymphatic Basin</code></td><td><code>ncit:C94547</code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Maxilla</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C6634</code></td><td></td></tr>
<tr><td><code>Medulla</code></td><td><code>ncit:C12442</code></td><td></td></tr>
<tr><td><code>Meninges</code></td><td><code>ncit:C12348</code></td><td></td></tr>
<tr><td><code>Mesenteric Nodes</code></td><td><code>ncit:C77641</code></td><td></td></tr>
<tr><td><code>Metacarpals</code></td><td><code>ncit:C12751</code></td><td></td></tr>
<tr><td><code>Metacarpus</code></td><td><code>ncit:C12751</code></td><td></td></tr>
<tr><td><code>Metatarsals</code></td><td><code>ncit:C12752</code></td><td></td></tr>
<tr><td><code>Metatarsus</code></td><td><code>ncit:C12752</code></td><td></td></tr>
<tr><td><code>Midbrain</code></td><td><code>ncit:C12510</code></td><td></td></tr>
<tr><td><code>Middle Ear</code></td><td><code>ncit:C12274</code></td><td></td></tr>
<tr><td><code>Muscle</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal Bone</code></td><td><code>ncit:C33157</code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasal Cavity and Paranasal Sinuses</code></td><td><code>ncit:C12763</code></td><td></td></tr>
<tr><td><code>Nasal Septum</code></td><td><code>ncit:C33160</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Occipital Bone</code></td><td><code>ncit:C12757</code></td><td></td></tr>
<tr><td><code>Occipital Lobe</code></td><td><code>ncit:C12355</code></td><td></td></tr>
<tr><td><code>Omentum</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Omentum/Peritoneum</code></td><td><code>ncit:C33209</code></td><td></td></tr>
<tr><td><code>Optic Chiasm</code></td><td><code>ncit:C90609</code></td><td></td></tr>
<tr><td><code>Optic Nerve</code></td><td><code>ncit:C12761</code></td><td></td></tr>
<tr><td><code>Optic Nerve Head, Intra-Laminar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Optic Nerve Head, Pre-Laminar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code>ncit:C12421</code></td><td></td></tr>
<tr><td><code>Orbit</code></td><td><code>ncit:C12347</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Other Extremity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other Face</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other GU Non-Bladder/Prostate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other Head and Neck</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other Orbit</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other Parameningeal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Pancreas</code></td><td><code>ncit:C12393</code></td><td></td></tr>
<tr><td><code>Paraaortic Lymph Node</code></td><td><code>ncit:C77643</code></td><td></td></tr>
<tr><td><code>Paranasal Sinuses</code></td><td><code>ncit:C12763</code></td><td></td></tr>
<tr><td><code>Parapharyngeal Area</code></td><td><code>ncit:C162818</code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code>ncit:C129461</code></td><td></td></tr>
<tr><td><code>Paratesticular</code></td><td><code>ncit:C162491</code></td><td></td></tr>
<tr><td><code>Parathyroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parietal Bone</code></td><td><code>ncit:C12766</code></td><td></td></tr>
<tr><td><code>Parietal Cortex</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Parietal Lobe</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Parotid</code></td><td><code>ncit:C12427</code></td><td></td></tr>
<tr><td><code>Patella</code></td><td><code>ncit:C33282</code></td><td></td></tr>
<tr><td><code>Pectoral Nodes</code></td><td><code>ncit:C120322</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Penis</code></td><td><code>ncit:C12409</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code>ncit:C33301</code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Pleural Effusion</code></td><td><code>ncit:C3331</code></td><td></td></tr>
<tr><td><code>Pons</code></td><td><code>ncit:C12511</code></td><td></td></tr>
<tr><td><code>Popliteal Nodes</code></td><td><code>ncit:C53146</code></td><td></td></tr>
<tr><td><code>Preauricular Lymph Node</code></td><td><code>ncit:C103429</code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Radius Bone</code></td><td><code>ncit:C12777</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Regional Lymph Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Rib</code></td><td><code>ncit:C12782</code></td><td></td></tr>
<tr><td><code>Sacral Region</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Sacrococcygeal</code></td><td><code>ncit:C33506</code></td><td></td></tr>
<tr><td><code>Salivary Gland</code></td><td><code>ncit:C12426</code></td><td></td></tr>
<tr><td><code>Sacrum</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code>ncit:C12783</code></td><td></td></tr>
<tr><td><code>Shoulder Girdle</code></td><td><code>ncit:C33547</code></td><td></td></tr>
<tr><td><code>Shoulder Joint</code></td><td><code>ncit:C33548</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Skull, NOS</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Small Intestine</code></td><td><code>ncit:C12386</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
<tr><td><code>Sphenoid Bone</code></td><td><code>ncit:C12790</code></td><td></td></tr>
<tr><td><code>Spinal Cord</code></td><td><code>ncit:C12464</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Spleen</code></td><td><code>ncit:C12432</code></td><td></td></tr>
<tr><td><code>Splenic Hilar Nodes</code></td><td><code>ncit:C33600</code></td><td></td></tr>
<tr><td><code>Sternum</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Stomach</code></td><td><code>ncit:C12391</code></td><td></td></tr>
<tr><td><code>Stroma of Iris</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Superior Maxilla</code></td><td><code>ncit:C33682</code></td><td></td></tr>
<tr><td><code>Supraclavicular Lymph Node</code></td><td><code>ncit:C12903</code></td><td></td></tr>
<tr><td><code>Supraclavicular Nodes</code></td><td><code>ncit:C12903</code></td><td></td></tr>
<tr><td><code>Suprasellar Pituitary</code></td><td><code>ncit:C95445</code></td><td></td></tr>
<tr><td><code>Suprasellar/Neurohypophyseal</code></td><td><code>ncit:C42602</code></td><td></td></tr>
<tr><td><code>Talus</code></td><td><code>ncit:C52799</code></td><td></td></tr>
<tr><td><code>Tarsal Bone</code></td><td><code>ncit:C12796</code></td><td></td></tr>
<tr><td><code>Tarsals</code></td><td><code>ncit:C12796</code></td><td></td></tr>
<tr><td><code>Temporal Bone</code></td><td><code>ncit:C12797</code></td><td></td></tr>
<tr><td><code>Temporal Cortex</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Temporal Lobe</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thalamus</code></td><td><code>ncit:C12459</code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Third Ventricle</code></td><td><code>ncit:C12827</code></td><td></td></tr>
<tr><td><code>Thoracic Spinal Cord</code></td><td><code>ncit:C12894</code></td><td></td></tr>
<tr><td><code>Thoracic Vertebra</code></td><td><code>ncit:C12798</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Thymus</code></td><td><code>ncit:C12433</code></td><td></td></tr>
<tr><td><code>Thyroid</code></td><td><code>ncit:C12400</code></td><td></td></tr>
<tr><td><code>Tibia</code></td><td><code>ncit:C12800</code></td><td></td></tr>
<tr><td><code>Toe</code></td><td><code>ncit:C33788</code></td><td></td></tr>
<tr><td><code>Tonsil</code></td><td><code>ncit:C12802</code></td><td></td></tr>
<tr><td><code>Trachea</code></td><td><code>ncit:C12428</code></td><td></td></tr>
<tr><td><code>Trabecular Meshwork</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trunk</code></td><td><code>ncit:C33816</code></td><td></td></tr>
<tr><td><code>Ulna</code></td><td><code>ncit:C12809</code></td><td></td></tr>
<tr><td><code>Upper Airway</code></td><td><code>ncit:C33839</code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code>ncit:C32141</code></td><td></td></tr>
<tr><td><code>Upper Extremity</code></td><td><code>ncit:C12671</code></td><td></td></tr>
<tr><td><code>Upper Limb, NOS</code></td><td><code>ncit:C12671</code></td><td></td></tr>
<tr><td><code>Ureter</code></td><td><code>ncit:C12416</code></td><td></td></tr>
<tr><td><code>Urogenital</code></td><td><code>ncit:C25350</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code>ncit:C12405</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vasculo-Nervous</code></td><td><code>ncit:C74603</code></td><td></td></tr>
<tr><td><code>Viscera</code></td><td><code>ncit:C28287</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
<tr><td><code>Waldeyer's Ring</code></td><td><code>ncit:C73468</code></td><td></td></tr>
<tr><td><code>Wrist</code></td><td><code>ncit:C33894</code></td><td></td></tr>
<tr><td><code>Wrist Joint</code></td><td><code>ncit:C33895</code></td><td></td></tr>
<tr><td><code>Zygomatic Bone</code></td><td><code>ncit:C33897</code></td><td></td></tr>
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

<div id="enum-modal-embryovitrificationstageenum" class="enum-modal" onclick="closeEnumModal('enum-modal-embryovitrificationstageenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-embryovitrificationstageenum')">×</button>
<h3><code>EmbryoVitrificationStageEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Zygote</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cleavage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Blastocyst</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Both Cleavage and Blastocyst</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-endometrialstripethicknessunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-endometrialstripethicknessunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-endometrialstripethicknessunitenum')">×</button>
<h3><code>EndometrialStripeThicknessUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>mm</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-exposureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-exposureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-exposureenum')">×</button>
<h3><code>ExposureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Alcohol</code></td><td><code>ncit:C168296</code></td><td></td></tr>
<tr><td><code>Marijuana</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Tobacco</code></td><td><code>ncit:C18059</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Never</code></td><td><code>ncit:C70543</code></td><td></td></tr>
<tr><td><code>Past</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fertilityconsulteligibilityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fertilityconsulteligibilityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fertilityconsulteligibilityenum')">×</button>
<h3><code>FertilityConsultEligibilityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Eligible</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ineligible</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fertilityconsultineligiblereasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fertilityconsultineligiblereasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fertilityconsultineligiblereasonenum')">×</button>
<h3><code>FertilityConsultIneligibleReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Observation Only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Palliative Or &lt;20% Expected Survival</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Severe Cognitive Delay</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fertilityconsultoutcomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fertilityconsultoutcomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fertilityconsultoutcomeenum')">×</button>
<h3><code>FertilityConsultOutcomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Sperm Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oocyte Or Embryo Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Tissue Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovarian Tissue Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Declined Fertility Preservation Consult</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No Fertility Preservation Available</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No Fertility Preservation Indicated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fertilityconsultwhopresentenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fertilityconsultwhopresentenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fertilityconsultwhopresentenum')">×</button>
<h3><code>FertilityConsultWhoPresentEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Patient And Parents(s)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Patient And Partner</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Patient Only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Provider Only</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-fertilityprocedureenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fertilityprocedureenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fertilityprocedureenum')">×</button>
<h3><code>FertilityProcedureEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cryopreserved Ovarian Tissue Reimplantation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Testicular Cell Reimplantation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Testicular Tissue Reimplantation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Embryo Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Epidydimal Sperm Aspiration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oocyte Cryopreservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oocyte Retrieval from Transplanted Ovarian Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oophoropexy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OTC, Cortical Strip</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OTC, Oophorectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OTC, Partial Oophorectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Semen Collection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sperm Retrieval from Transplanted Testicular Cells</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sperm Retrieval from Transplanted Testicular Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Sperm Aspiration</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Sperm Extraction, Micro TESE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Sperm Extraction, TESE</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Tissue Cryopreservation, Orchiectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Tissue Cryopreservation, Partial Orchiectomy/Biopsy</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-follicledensityunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-follicledensityunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-follicledensityunitenum')">×</button>
<h3><code>FollicleDensityUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>count/mm2</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-freezingmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-freezingmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-freezingmethodenum')">×</button>
<h3><code>FreezingMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Vitrification</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Controlled Slow Rate Freezing</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Identifies As Female Gender</code></td><td><code>SCTID:446141000124107</code></td><td></td></tr>
<tr><td><code>Identifies As Male Gender</code></td><td><code>SCTID:446151000124109</code></td><td></td></tr>
<tr><td><code>Identifies As Nonbinary Gender</code></td><td><code>SCTID:33791000087105</code></td><td></td></tr>
<tr><td><code>Male-To-Female Transgender</code></td><td><code>SCTID: 33791000087105</code></td><td></td></tr>
<tr><td><code>Female-To-Male Transgender</code></td><td><code>SCTID: 407377005</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-gonadotoxicriskenum" class="enum-modal" onclick="closeEnumModal('enum-modal-gonadotoxicriskenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-gonadotoxicriskenum')">×</button>
<h3><code>GonadotoxicRiskEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>No Previous Therapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intermediate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>High</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Mismatch</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-insurancetypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-insurancetypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-insurancetypeenum')">×</button>
<h3><code>InsuranceTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Public</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Private</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Military</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No Insurance</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-laboratoryresultenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratoryresultenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratoryresultenum')">×</button>
<h3><code>LaboratoryResultEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Positive</code></td><td><code>ncit:C38758</code></td><td></td></tr>
<tr><td><code>Negative</code></td><td><code>ncit:C38757</code></td><td></td></tr>
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
<tr><td><code>Absolute Neutrophil Count (ANC)</code></td><td><code>ncit:C63321</code></td><td></td></tr>
<tr><td><code>Anti-Mullerian Hormone (AMH)</code></td><td><code>ncit:C120625</code></td><td></td></tr>
<tr><td><code>Antral Follicle Count</code></td><td><code>ncit:C97213</code></td><td></td></tr>
<tr><td><code>Estradiol</code></td><td><code>ncit:C74782</code></td><td></td></tr>
<tr><td><code>Follicle-Stimulating Hormone (FSH)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Free Testosterone</code></td><td><code>ncit:C74785</code></td><td></td></tr>
<tr><td><code>hCG</code></td><td><code>ncit:C75387</code></td><td></td></tr>
<tr><td><code>Hemoglobin</code></td><td><code>ncit:C64848</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Inhibin-B</code></td><td><code>ncit:C2276</code></td><td></td></tr>
<tr><td><code>Luteinizing Hormone Test</code></td><td><code>ncit:C74790</code></td><td></td></tr>
<tr><td><code>Platelets</code></td><td><code>ncit:C51951</code></td><td>(fa) ConsortiumNote: CBC</td></tr>
<tr><td><code>Progesterone</code></td><td><code>ncit:C74791</code></td><td></td></tr>
<tr><td><code>Prolactin</code></td><td><code>ncit:C74870</code></td><td></td></tr>
<tr><td><code>Total Testosterone</code></td><td><code>ncit:C74793</code></td><td></td></tr>
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
<tr><td><code>mIU/mL</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ng/mL</code></td><td><code>ncit:C67306</code></td><td></td></tr>
<tr><td><code>ng/dL</code></td><td><code>ncit:C67326</code></td><td></td></tr>
<tr><td><code>pg/mL</code></td><td><code>ncit:C67327</code></td><td></td></tr>
<tr><td><code>pmol/l</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Plasma</code></td><td><code>ncit:C185204</code></td><td></td></tr>
<tr><td><code>Serum</code></td><td><code>ncit:C178987</code></td><td></td></tr>
<tr><td><code>Urine</code></td><td><code>ncit:C13283</code></td><td></td></tr>
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

<div id="enum-modal-lifetimecumulativedoseunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lifetimecumulativedoseunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lifetimecumulativedoseunitenum')">×</button>
<h3><code>LifetimeCumulativeDoseUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>mg/m2</code></td><td><code>ncit:C67402</code></td><td></td></tr>
<tr><td><code>g/m2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mg/kg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Units</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-maritalstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-maritalstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-maritalstatusenum')">×</button>
<h3><code>MaritalStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Divorced</code></td><td><code>ncit:C51776</code></td><td></td></tr>
<tr><td><code>Domestic Partnership</code></td><td><code>ncit:C53262</code></td><td></td></tr>
<tr><td><code>Married</code></td><td><code>ncit:C51773</code></td><td></td></tr>
<tr><td><code>Never Married</code></td><td><code>ncit:C51774</code></td><td></td></tr>
<tr><td><code>Separated</code></td><td><code>ncit:C156541</code></td><td></td></tr>
<tr><td><code>Widowed</code></td><td><code>ncit:C51775</code></td><td></td></tr>
<tr><td><code>Marital or Civil Status Not Disclosed</code></td><td><code>ncit:C150742</code></td><td></td></tr>
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
<tr><td><code>g/m2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>mg/kg</code></td><td><code>ncit:C105468</code></td><td></td></tr>
<tr><td><code>mg/m2</code></td><td><code>ncit:C67402</code></td><td></td></tr>
<tr><td><code>Units</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Ixabepilone</code></td><td><code>rxcui:10485</code></td><td></td></tr>
<tr><td><code>Iobenguane I-131</code></td><td><code>rxcui:10485</code></td><td></td></tr>
<tr><td><code>6 Thioguanine</code></td><td><code>rxcui:10485</code></td><td></td></tr>
<tr><td><code>6 Mercaptopurine</code></td><td><code>rxcui:103</code></td><td></td></tr>
<tr><td><code>Alemtuzumab</code></td><td><code>rxcui:117055</code></td><td></td></tr>
<tr><td><code>Aspacytarabine</code></td><td><code>ncit:C1614</code></td><td></td></tr>
<tr><td><code>Axitinib</code></td><td><code>rxcui:1242999</code></td><td></td></tr>
<tr><td><code>Bevacizumab</code></td><td><code>rxcui:253337</code></td><td></td></tr>
<tr><td><code>Bleomycin</code></td><td><code>rxcui:1622</code></td><td></td></tr>
<tr><td><code>Brentuximab Vedotin</code></td><td><code>ncit:C66944</code></td><td></td></tr>
<tr><td><code>Busulfan</code></td><td><code>ncit:C321</code></td><td></td></tr>
<tr><td><code>Cabozantinib</code></td><td><code>ncit:C52200</code></td><td></td></tr>
<tr><td><code>Capecitabine</code></td><td><code>rxcui:194000</code></td><td></td></tr>
<tr><td><code>Carboplatin</code></td><td><code>rxcui:40048</code></td><td></td></tr>
<tr><td><code>Carmustine</code></td><td><code>ncit:C349</code></td><td></td></tr>
<tr><td><code>Cetrotide</code></td><td><code>rxcui:284693</code></td><td></td></tr>
<tr><td><code>Cisplatin</code></td><td><code>rxcui:2555</code></td><td></td></tr>
<tr><td><code>Chlorambucil</code></td><td><code>rxcui:2346</code></td><td></td></tr>
<tr><td><code>Combination Estrogen/Progestin Hormonal Contraception</code></td><td><code>ncit:C91717</code></td><td></td></tr>
<tr><td><code>Contraceptive Patch</code></td><td><code>rxcui:220714</code></td><td></td></tr>
<tr><td><code>Crizotinib</code></td><td><code>ncit:C74061</code></td><td></td></tr>
<tr><td><code>Cyclophosphamide</code></td><td><code>rxcui:3002</code></td><td></td></tr>
<tr><td><code>Cytarabine</code></td><td><code>rxcui:3041</code></td><td></td></tr>
<tr><td><code>Dabrafenib</code></td><td><code>rxcui:1424911</code></td><td></td></tr>
<tr><td><code>Actinomycin</code></td><td><code>rxcui:3100</code></td><td></td></tr>
<tr><td><code>Daunorubicin</code></td><td><code>rxcui:3109</code></td><td></td></tr>
<tr><td><code>Depo Provera</code></td><td><code>rxcui:202886</code></td><td></td></tr>
<tr><td><code>Dinutuximab</code></td><td><code>rxcui:1606274</code></td><td></td></tr>
<tr><td><code>Docetaxel</code></td><td><code>rxcui:72962</code></td><td></td></tr>
<tr><td><code>Doxorubicin</code></td><td><code>rxcui:1799303</code></td><td></td></tr>
<tr><td><code>Entrectinib</code></td><td><code>rxcui:2197862</code></td><td></td></tr>
<tr><td><code>Epirubicin</code></td><td><code>rxcui:3995</code></td><td></td></tr>
<tr><td><code>Eribulin</code></td><td><code>rxcui:1045453</code></td><td></td></tr>
<tr><td><code>Estradiol</code></td><td><code>rxcui:4083</code></td><td></td></tr>
<tr><td><code>Etoposide</code></td><td><code>rxcui:4179</code></td><td></td></tr>
<tr><td><code>Ganilreix</code></td><td><code>rxcui:35825</code></td><td></td></tr>
<tr><td><code>Gemcitabine</code></td><td><code>rxcui:12574</code></td><td></td></tr>
<tr><td><code>Goserelin</code></td><td><code>rxcui:50610</code></td><td></td></tr>
<tr><td><code>Human Chorionic Gonadotropin (hCG)</code></td><td><code>ncit:C528</code></td><td></td></tr>
<tr><td><code>Human Menopausal Gonadotropin (hMG)</code></td><td><code>ncit:C2274</code></td><td></td></tr>
<tr><td><code>Hydroxyurea</code></td><td><code>rxcui:5552</code></td><td></td></tr>
<tr><td><code>Idarubicin</code></td><td><code>rxcui:5650</code></td><td></td></tr>
<tr><td><code>Ifosfamide</code></td><td><code>rxcui:5657</code></td><td></td></tr>
<tr><td><code>Ipilimumab</code></td><td><code>ncit:C2654</code></td><td></td></tr>
<tr><td><code>Larotrectinib</code></td><td><code>rxcui:2105628</code></td><td></td></tr>
<tr><td><code>Lenvatinib</code></td><td><code>rxcui:1603296</code></td><td></td></tr>
<tr><td><code>Letrozole</code></td><td><code>rxcui:72965</code></td><td></td></tr>
<tr><td><code>Leuprolide Acetate</code></td><td><code>rxcui:203217</code></td><td></td></tr>
<tr><td><code>Lomustine</code></td><td><code>rxcui:6466</code></td><td></td></tr>
<tr><td><code>Mechlorethamine</code></td><td><code>rxcui:6674</code></td><td></td></tr>
<tr><td><code>Melphalan</code></td><td><code>rxcui:6718</code></td><td></td></tr>
<tr><td><code>Methotrexate</code></td><td><code>rxcui:6851</code></td><td></td></tr>
<tr><td><code>Mitoxantrone</code></td><td><code>rxcui:7005</code></td><td></td></tr>
<tr><td><code>Nab-Paclitaxel</code></td><td><code>ncit:C2688</code></td><td></td></tr>
<tr><td><code>Nelarabine</code></td><td><code>rxcui:274771</code></td><td></td></tr>
<tr><td><code>Nitrogen Mustard</code></td><td><code>rxcui:6674</code></td><td></td></tr>
<tr><td><code>Nivolumab</code></td><td><code>rxcui:1597876</code></td><td></td></tr>
<tr><td><code>Nuva Ring</code></td><td><code>rxcui:1367439</code></td><td></td></tr>
<tr><td><code>Oxaliplatin</code></td><td><code>rxcui:32592</code></td><td></td></tr>
<tr><td><code>Pazopanib</code></td><td><code>rxcui:714438</code></td><td></td></tr>
<tr><td><code>Pegylated Liposomal Doxorubicin Hydrochloride</code></td><td><code>ncit:C1555</code></td><td></td></tr>
<tr><td><code>Pembrolizumab</code></td><td><code>rxcui:1547545</code></td><td></td></tr>
<tr><td><code>Procarbazine</code></td><td><code>rxcui:8702</code></td><td></td></tr>
<tr><td><code>Progestin Implant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Progestin-Only Pills</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Progestogen</code></td><td><code>ncit:C2296</code></td><td></td></tr>
<tr><td><code>Progestational Intrauterine Device</code></td><td><code>ncit:C184790</code></td><td></td></tr>
<tr><td><code>Recombinant FSH</code></td><td><code>ncit:C1822</code></td><td></td></tr>
<tr><td><code>Rituximab</code></td><td><code>rxcui:121191</code></td><td></td></tr>
<tr><td><code>Selpercatinib</code></td><td><code>rxcui:2370147</code></td><td></td></tr>
<tr><td><code>Sunitinib</code></td><td><code>rxcui:357977</code></td><td></td></tr>
<tr><td><code>Tamoxifen</code></td><td><code>rxcui:10324</code></td><td></td></tr>
<tr><td><code>Temozolomide</code></td><td><code>rxcui:37776</code></td><td></td></tr>
<tr><td><code>Testosterone</code></td><td><code>rxcui:10379</code></td><td></td></tr>
<tr><td><code>Thiotepa</code></td><td><code>rxcui:10473</code></td><td></td></tr>
<tr><td><code>Treosulfan</code></td><td><code>rxcui:38508</code></td><td></td></tr>
<tr><td><code>Triptorelin</code></td><td><code>rxcui:38782</code></td><td></td></tr>
<tr><td><code>Vinblastine</code></td><td><code>rxcui:11198</code></td><td></td></tr>
<tr><td><code>Vincristine</code></td><td><code>rxcui:11202</code></td><td></td></tr>
<tr><td><code>Vinorelbine</code></td><td><code>rxcui:39541</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-menarchalstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-menarchalstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-menarchalstatusenum')">×</button>
<h3><code>MenarchalStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Pre-Menarchal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Post-Menarchal</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-menstrualphaseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-menstrualphaseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-menstrualphaseenum')">×</button>
<h3><code>MenstrualPhaseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Early Follicular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Mid/Late Follicular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Follicular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Luteal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Periovulatory</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-menstrualstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-menstrualstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-menstrualstatusenum')">×</button>
<h3><code>MenstrualStatusEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Menstruating, Regular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Menstruating, Irregular</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Menstruating</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-monitormethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-monitormethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-monitormethodenum')">×</button>
<h3><code>MonitorMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abdominal Ultrasound</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transvaginal Ultrasound Scanning (TVUS)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-oocyteorembryosourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-oocyteorembryosourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-oocyteorembryosourceenum')">×</button>
<h3><code>OocyteOrEmbryoSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Autologous Egg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autologous Embryo</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Donated Embryo</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Donated Egg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autologous Ovarian Tissue</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-oocyteorembryostateenum" class="enum-modal" onclick="closeEnumModal('enum-modal-oocyteorembryostateenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-oocyteorembryostateenum')">×</button>
<h3><code>OocyteOrEmbryoStateEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fresh</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thawed</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-otcconversionreasonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-otcconversionreasonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-otcconversionreasonenum')">×</button>
<h3><code>OtcConversionReasonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Purpose of Fertility Presevation Only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Secondary To Surgical Complication</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-otcresectiontypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-otcresectiontypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-otcresectiontypeenum')">×</button>
<h3><code>OtcResectionTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Distal to Proximal Removal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Proximal to Distal Removal</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-otcstripsweightunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-otcstripsweightunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-otcstripsweightunitenum')">×</button>
<h3><code>OtcStripsWeightUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>mg</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-otcsurgicalenergysourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-otcsurgicalenergysourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-otcsurgicalenergysourceenum')">×</button>
<h3><code>OtcSurgicalEnergySourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Ligasure Bipolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Harmonic Bipolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Monopolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>None / Cold Scissor</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cold Scissor Converted to Ligasure Bipolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cold Scissor Converted to Harmonic Bipolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cold Scissor Converted to Monopolar</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-otcsurgicaltechniqueenum" class="enum-modal" onclick="closeEnumModal('enum-modal-otcsurgicaltechniqueenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-otcsurgicaltechniqueenum')">×</button>
<h3><code>OtcSurgicalTechniqueEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Laparotomy Only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparascopy Only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Laparoscopy Converted to Laparotomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-pregnancyoutcomeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-pregnancyoutcomeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-pregnancyoutcomeenum')">×</button>
<h3><code>PregnancyOutcomeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Implantation unsuccessful</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Term birth of newborn</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Premature delivery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Induced termination of pregnancy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Miscarriage</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Stillbirth</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-pregnancypersonenum" class="enum-modal" onclick="closeEnumModal('enum-modal-pregnancypersonenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-pregnancypersonenum')">×</button>
<h3><code>PregnancyPersonEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Subject</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Partner</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gestational Carrier</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-preimplantationgenetictestingtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-preimplantationgenetictestingtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-preimplantationgenetictestingtypeenum')">×</button>
<h3><code>PreimplantationGeneticTestingTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>PGT-A (Aneuploidy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PGT-M (Monogenic/Single Gene Defect)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PGT-SR (Structural Rearrangement)</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-procedureclassenum" class="enum-modal" onclick="closeEnumModal('enum-modal-procedureclassenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-procedureclassenum')">×</button>
<h3><code>ProcedureClassEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Fertility Tissue Preservation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fertility Preserved Tissue Utilization</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdominal Myomectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hysterectomy</code></td><td><code>ncit:C15256</code></td><td></td></tr>
<tr><td><code>Hysteroscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oophorectomy, NOS</code></td><td><code>ncit:C15291</code></td><td></td></tr>
<tr><td><code>Orchiectomy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Dialysis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Endometrial Ablation/Resection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney Surgery, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney Transplant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>None</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oophorectomy, Complete</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oophorectomy, Partial</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneal Lymph Node Dissection</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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

<div id="enum-modal-reasondeclinedfertilitypreservationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasondeclinedfertilitypreservationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasondeclinedfertilitypreservationenum')">×</button>
<h3><code>ReasonDeclinedFertilityPreservationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cost</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No Time</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sexual Orientation</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Interested</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Contraindicated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-religiontypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-religiontypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-religiontypeenum')">×</button>
<h3><code>ReligionTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>None</code></td><td><code>ncit:C41132</code></td><td></td></tr>
<tr><td><code>Christian</code></td><td><code>ncit:C176033</code></td><td></td></tr>
<tr><td><code>Buddhist</code></td><td><code>ncit:C103284</code></td><td></td></tr>
<tr><td><code>Hindu</code></td><td><code>ncit:C103291</code></td><td></td></tr>
<tr><td><code>Jewish</code></td><td><code>ncit:C211623</code></td><td></td></tr>
<tr><td><code>Muslim</code></td><td><code>ncit:C103285</code></td><td></td></tr>
<tr><td><code>Sikh</code></td><td><code>ncit:C176036</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-reportinglevelenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reportinglevelenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reportinglevelenum')">×</button>
<h3><code>ReportingLevelEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cumulative</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Fraction</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-retrievalmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-retrievalmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-retrievalmethodenum')">×</button>
<h3><code>RetrievalMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Abdominal Ultrasound Guided</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Transvaginal Ultrasound Scanning (TVUS) Guided</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Intraperitoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrathecal</code></td><td><code>ncit:C173292</code></td><td></td></tr>
<tr><td><code>Oral</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cranium</code></td><td><code>ncit:C12789</code></td><td></td></tr>
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Occiptial Cortex</code></td><td><code>ncit:C12757</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Schlemm's Canal</code></td><td><code>ncit:C12783</code></td><td></td></tr>
<tr><td><code>Spine</code></td><td><code>ncit:C12998</code></td><td></td></tr>
<tr><td><code>Testes</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-semenabnormalityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-semenabnormalityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-semenabnormalityenum')">×</button>
<h3><code>SemenAbnormalityEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Oligospermia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Severe Oligospermia</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Azoospermia</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Intersex, NOS</code></td><td><code>ncit:C45908</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-sexualmaturityindexenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sexualmaturityindexenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sexualmaturityindexenum')">×</button>
<h3><code>SexualMaturityIndexEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>NOS, Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOS, Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOS, Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOS, Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOS, Stage 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital, Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital, Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital, Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital, Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genital, Stage 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 1, Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 2, Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 3, Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 4, Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 5, Female</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 1, Male</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 2, Male</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 3, Male</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 4, Male</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pubic Hair, Stage 5, Male</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Not Applicable</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-sitefindingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sitefindingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sitefindingenum')">×</button>
<h3><code>SiteFindingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cyst</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-spermsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-spermsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-spermsourceenum')">×</button>
<h3><code>SpermSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Partner Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Donated Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autologous Testicular Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Autologous Testicular Cells</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-spermatogoniadensityunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-spermatogoniadensityunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-spermatogoniadensityunitenum')">×</button>
<h3><code>SpermatogoniaDensityUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>count/tubule</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>IRS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 1a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 1b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 2a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 2b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 3a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 3b</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 4a</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRSS &gt;&gt; Group 4b</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>System NOS, L1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS, L2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS, M</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS, MS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>AIDS-Related Kaposi Sarcoma Stage</code></td><td><code>ncit:C134969</code></td><td></td></tr>
<tr><td><code>AJCC v6 Stage</code></td><td><code>ncit:C90529</code></td><td></td></tr>
<tr><td><code>AJCC v7 Stage</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC v8 Stage</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>Ann Arbor</code></td><td><code>ncit:C54179</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group</code></td><td><code>ncit:C39353</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Liver Tumor Staging System</code></td><td><code>ncit:C177630</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Neuroblastoma Risk Group Staging System</code></td><td><code>ncit:C177631</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Retinoblastoma Risk Group Staging System</code></td><td><code>ncit:C177633</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System</code></td><td><code>ncit:C140271</code></td><td></td></tr>
<tr><td><code>EVANS</code></td><td><code>ncit:C85407</code></td><td></td></tr>
<tr><td><code>Enneking Staging System</code></td><td><code>ncit:C140258</code></td><td></td></tr>
<tr><td><code>FIGO</code></td><td><code>ncit:C125738</code></td><td></td></tr>
<tr><td><code>INRGSS</code></td><td><code>ncit:C133427</code></td><td></td></tr>
<tr><td><code>INSS</code></td><td><code>ncit:C85416</code></td><td></td></tr>
<tr><td><code>Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System</code></td><td><code>ncit:C148010</code></td><td></td></tr>
<tr><td><code>International Retinoblastoma Staging System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>International Society of Pediatric Oncology Staging System</code></td><td><code>ncit:C140270</code></td><td></td></tr>
<tr><td><code>Lugano Stage</code></td><td><code>ncit:C141147</code></td><td></td></tr>
<tr><td><code>PRETEXT Staging System</code></td><td><code>ncit:C141133</code></td><td></td></tr>
<tr><td><code>Pediatric Oncology Group Neuroblastoma Staging System</code></td><td><code>ncit:C85423</code></td><td></td></tr>
<tr><td><code>Reese-Ellsworth Staging System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>St. Jude Stage</code></td><td><code>ncit:C141216</code></td><td></td></tr>
<tr><td><code>TNM Staging System</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Fertility Preservation And Outcomes Of Fertility Treatment Registries</code></td><td><code></code></td><td></td></tr>
<tr><td><code>National Fertility Preservation Database</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NIH 000106</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NIH 000715</code></td><td><code></code></td><td></td></tr>
<tr><td><code>De-Identified Clinical Data Of Patients Seen At Indiana University</code></td><td><code></code></td><td></td></tr>
<tr><td><code>De-Identified Patients Seen For Oncofertility At Cincinnati Children'S Hospital Medical Center</code></td><td><code></code></td><td></td></tr>
<tr><td><code>National Oncofertility Database</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-surgeontypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-surgeontypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-surgeontypeenum')">×</button>
<h3><code>SurgeonTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Adult Urologist</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pediatric Urologist</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Adult General</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pediatric General</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Adult Gynecologist</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pediatric Gynecologist</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>EBRT, Stereotactic Radiosurgery</code></td><td><code>ncit:C15358</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tissuetypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tissuetypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tissuetypeenum')">×</button>
<h3><code>TissueTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Oocyte</code></td><td><code>ncit:C12598</code></td><td></td></tr>
<tr><td><code>Embryo</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovarian Cortical Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Testicular Tissue</code></td><td><code>ncit:C33758</code></td><td></td></tr>
<tr><td><code>Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Epididymal Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tissuetypeutilizedenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tissuetypeutilizedenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tissuetypeutilizedenum')">×</button>
<h3><code>TissueTypeUtilizedEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cryopreserved Ovarian Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Embryo</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Oocyte</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Ovarian Tissue Oocyte</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Ejaculated Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Testicular Tissue Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved TESE/TESA Sperm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cryopreserved Testicular Tissue </code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-transportmediaenum" class="enum-modal" onclick="closeEnumModal('enum-modal-transportmediaenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-transportmediaenum')">×</button>
<h3><code>TransportMediaEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Cooper Surgical (OFC Transport Media)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lactated Ringers</code></td><td><code>ncit:C65149</code></td><td></td></tr>
<tr><td><code>Modified Human Tubal Fluid, NOS</code></td><td><code>ncit:C65149</code></td><td></td></tr>
<tr><td><code>Irvine Modified Human Tubal Fluid</code></td><td><code>ncit:C65149</code></td><td></td></tr>
<tr><td><code>Irvine Modified Human Tubal FluidOrigio Handling Media</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Custodiol</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Uterus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-volumeunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-volumeunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-volumeunitenum')">×</button>
<h3><code>VolumeUnitEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>cm^3</code></td><td><code></code></td><td></td></tr>
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
    "fprh": {
      "name": "fprh",
      "title": "Fertility Preservation and Reproductive Health",
      "description": "The FPRH view of the PCDC data model represents consensus data modeling by an international group of oncology-related fertility preservation and reproductive health experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Reproductive Hope Consortium (R-HOPE). It is based on the collective requirements of its contributors."
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
    "Consult": {
      "slots": [
        "age_at_fertility_consult",
        "fertility_consult_eligibility",
        "fertility_consult_ineligible_reason",
        "reason_declined_fertility_consult",
        "reason_declined_fertility_preservation",
        "fertility_consult_who_present",
        "fertility_consult_outcome",
        "interpreter_used",
        "insurance_type"
      ],
      "comments": [
        "(fprh) ConsortiumNote: This table is tiered as Optional."
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
    "SocialAndBehavioralDeterminantsOfHealth": {
      "slots": [
        "age_at_status",
        "gender_identity",
        "exposure",
        "exposure_status",
        "marital_status",
        "religion_type",
        "religion_type_other"
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
        "laboratory_test_specimen_other",
        "laboratory_result",
        "result_text",
        "result_numeric",
        "laboratory_test_result_unit",
        "result_hormone_status"
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
        "diagnosis_category",
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
        "disease_site",
        "site_other",
        "laterality",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "site_finding",
        "volume",
        "volume_unit",
        "endometrial_stripe_thickness",
        "endometrial_stripe_thickness_unit"
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
        "gonadotoxic_risk",
        "gonadotoxic_risk_system",
        "gonadotoxic_risk_system_version"
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
        "procedure",
        "laterality"
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
        "route",
        "medication",
        "medication_other",
        "medication_dose_administered",
        "medication_dose_intended",
        "medication_dose_unit",
        "lifetime_cumulative_dose",
        "lifetime_cumulative_dose_unit"
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
        "administration_status",
        "site_classification",
        "rt_site",
        "laterality",
        "energy_type",
        "technique",
        "rt_dose",
        "rt_dose_unit",
        "num_fraction",
        "fraction_dose",
        "fraction_dose_unit",
        "transposition_organ",
        "reporting_level",
        "shielding"
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
        "sct_status",
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
    "AdverseEvents": {
      "slots": [
        "age_at_ae",
        "age_at_ae_resolved",
        "adverse_event",
        "ae_grade",
        "ae_grade_system"
      ],
      "comments": [
        "(fa) ConsortiumNote: This table is tiered as Priority.",
        "(npc) ConsortiumNote: This table is tiered as Optional."
      ],
      "annotations": {
        "domain": "monitoring"
      }
    },
    "FertilityProcedures": {
      "slots": [
        "fertility_procedure",
        "procedure_class",
        "tissue_type",
        "laterality",
        "transport_media",
        "transport_media_other",
        "cryopreservation_media",
        "cryopreservation_media_other",
        "freezing_method",
        "freezing_method_other",
        "monitor_method",
        "retrieval_method",
        "collection_status",
        "cryopreservation_status",
        "oocyte_collection_attempts",
        "oocyte_retrieved_numeric",
        "mature_oocytes_numeric",
        "oocytes_fertilized_numeric",
        "fertilization_rate",
        "maturity_rate",
        "cryopreserved_embryo_numeric",
        "cryopreserved_oocyte_numeric",
        "embryo_cryopreserved_day",
        "embryo_vitrification_stage",
        "menstrual_phase",
        "preimplantation_genetic_testing",
        "preimplantation_genetic_testing_type",
        "semen_volume",
        "semen_concentration",
        "semen_motility",
        "semen_morphology",
        "semen_count",
        "semen_motility_count",
        "semen_abnormality",
        "cryopreserved_semen_vials_numeric",
        "semen_cryopreservation_attempts",
        "testicular_tissue_weight_processed",
        "testicular_tissue_weight_unit",
        "testicular_tissue_pieces_cryopreserved",
        "testicular_tissue_vials_cryopreserved",
        "sperm_present",
        "surgeon_type",
        "otc_resection_type",
        "otc_surgical_technique",
        "otc_conversion_reason",
        "otc_surgical_energy_source",
        "germ_cells_present_spermatogonia",
        "spermatogonia_density",
        "spermatogonia_density_unit",
        "germ_cells_present_follicles",
        "follicle_density",
        "follicle_density_unit",
        "ovary_resect_percent",
        "otc_vials_number",
        "otc_strips_number",
        "otc_strips_weight",
        "otc_strips_weight_unit",
        "menarchal_status",
        "sexual_maturity_index"
      ],
      "comments": [],
      "annotations": {
        "domain": "intervention"
      }
    },
    "ReproductiveOutcomes": {
      "slots": [
        "age_at_pregnancy",
        "gestational_age_end_of_pregnancy_days",
        "age_at_pregnancy_method",
        "age_precision",
        "menstrual_status",
        "pregnancy_attempted",
        "pregnancy_achieved",
        "pregnancy_person",
        "fertility_tissue_utilized",
        "tissue_type_utilized",
        "conception_type",
        "oocyte_or_embryo_source",
        "sperm_source",
        "oocyte_or_embryo_state",
        "sperm_state",
        "ectopic_status",
        "plurality",
        "pregnancy_outcome",
        "delivery_route",
        "birth_order",
        "birth_weight",
        "birth_weight_unit"
      ],
      "comments": [],
      "annotations": {
        "domain": "monitoring"
      }
    }
  },
  "slots": {
    "ectopic_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_status": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "transposition_organ": {
      "slot_uri": "ncit:C175035",
      "range": "TranspositionOrganEnum",
      "comments": [],
      "annotations": {}
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
    "freezing_method_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "chimerism_unit": {
      "slot_uri": "",
      "range": "ChimerismUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "semen_abnormality": {
      "slot_uri": "",
      "range": "SemenAbnormalityEnum",
      "comments": [],
      "annotations": {}
    },
    "monitor_method": {
      "slot_uri": "",
      "range": "MonitorMethodEnum",
      "comments": [],
      "annotations": {}
    },
    "lifetime_cumulative_dose_unit": {
      "slot_uri": "",
      "range": "LifetimeCumulativeDoseUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "rt_site": {
      "slot_uri": "ncit:C173281",
      "range": "RtSiteEnum",
      "comments": [],
      "annotations": {}
    },
    "menstrual_phase": {
      "slot_uri": "",
      "range": "MenstrualPhaseEnum",
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
    "religion_type": {
      "slot_uri": "ncit:C17085",
      "range": "ReligionTypeEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fprh"
      }
    },
    "conception_type": {
      "slot_uri": "",
      "range": "ConceptionTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "semen_morphology": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "oocyte_or_embryo_state": {
      "slot_uri": "",
      "range": "OocyteOrEmbryoStateEnum",
      "comments": [],
      "annotations": {}
    },
    "sperm_source": {
      "slot_uri": "",
      "range": "SpermSourceEnum",
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
    "semen_motility_count": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "stem_cell_processing": {
      "slot_uri": "",
      "range": "StemCellProcessingEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "otc_resection_type": {
      "slot_uri": "",
      "range": "OtcResectionTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "pregnancy_person": {
      "slot_uri": "",
      "range": "PregnancyPersonEnum",
      "comments": [],
      "annotations": {}
    },
    "spermatogonia_density_unit": {
      "slot_uri": "",
      "range": "SpermatogoniaDensityUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "oocyte_or_embryo_source": {
      "slot_uri": "",
      "range": "OocyteOrEmbryoSourceEnum",
      "comments": [],
      "annotations": {}
    },
    "fraction_dose": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "fa,npc,rb"
      }
    },
    "embryo_vitrification_stage": {
      "slot_uri": "",
      "range": "EmbryoVitrificationStageEnum",
      "comments": [],
      "annotations": {}
    },
    "sperm_present": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "preimplantation_genetic_testing": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "result_hormone_status": {
      "slot_uri": "ncit:C36292",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fprh"
      }
    },
    "semen_count": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "cryopreserved_embryo_numeric": {
      "slot_uri": "",
      "range": "decimal",
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
    "fertility_procedure": {
      "slot_uri": "",
      "range": "FertilityProcedureEnum",
      "comments": [],
      "annotations": {}
    },
    "age_at_pregnancy_method": {
      "slot_uri": "",
      "range": "AgeAtPregnancyMethodEnum",
      "comments": [],
      "annotations": {}
    },
    "race_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "surgeon_type": {
      "slot_uri": "",
      "range": "SurgeonTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "cryopreserved_semen_vials_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "procedure_class": {
      "slot_uri": "",
      "range": "ProcedureClassEnum",
      "comments": [],
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
    "mature_oocytes_numeric": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "semen_cryopreservation_attempts": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "semen_motility": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "marital_status": {
      "slot_uri": "ncit:C25188",
      "range": "MaritalStatusEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "fprh"
      }
    },
    "ovary_resect_percent": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "fertility_consult_who_present": {
      "slot_uri": "",
      "range": "FertilityConsultWhoPresentEnum",
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
    "maturity_rate": {
      "slot_uri": "",
      "range": "decimal",
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
    "cryopreserved_oocyte_numeric": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "reason_declined_fertility_preservation": {
      "slot_uri": "",
      "range": "ReasonDeclinedFertilityPreservationEnum",
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
    "transport_media_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "menstrual_status": {
      "slot_uri": "",
      "range": "MenstrualStatusEnum",
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
    "age_at_ae": {
      "slot_uri": "ncit:C172677",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
      }
    },
    "gonadotoxic_risk_system": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "retrieval_method": {
      "slot_uri": "",
      "range": "RetrievalMethodEnum",
      "comments": [],
      "annotations": {}
    },
    "gonadotoxic_risk_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "reason_declined_fertility_consult": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "otc_vials_number": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "otc_strips_weight_unit": {
      "slot_uri": "",
      "range": "OtcStripsWeightUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "transport_media": {
      "slot_uri": "",
      "range": "TransportMediaEnum",
      "comments": [],
      "annotations": {}
    },
    "insurance_type": {
      "slot_uri": "",
      "range": "InsuranceTypeEnum",
      "comments": [],
      "annotations": {}
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
    "testicular_tissue_pieces_cryopreserved": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
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
    "testicular_tissue_vials_cryopreserved": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "oocyte_collection_attempts": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
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
    "volume": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "endometrial_stripe_thickness": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "laboratory_result": {
      "slot_uri": "ncit:C36292",
      "range": "LaboratoryResultEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "pregnancy_attempted": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "germ_cells_present_spermatogonia": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "lifetime_cumulative_dose": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "endometrial_stripe_thickness_unit": {
      "slot_uri": "",
      "range": "EndometrialStripeThicknessUnitEnum",
      "comments": [],
      "annotations": {}
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
    "otc_conversion_reason": {
      "slot_uri": "",
      "range": "OtcConversionReasonEnum",
      "comments": [],
      "annotations": {}
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
    "fertilization_rate": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "embryo_cryopreserved_day": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "pregnancy_outcome": {
      "slot_uri": "",
      "range": "PregnancyOutcomeEnum",
      "comments": [],
      "annotations": {}
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
    "sperm_state": {
      "slot_uri": "",
      "range": "OocyteOrEmbryoStateEnum",
      "comments": [],
      "annotations": {}
    },
    "spermatogonia_density": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "oocytes_fertilized_numeric": {
      "slot_uri": "",
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
    "ae_grade_system": {
      "slot_uri": "",
      "range": "AeGradeSystemEnum",
      "comments": [],
      "annotations": []
    },
    "cryopreservation_media_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "religion_type_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "fprh"
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
    "age_at_pregnancy": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "site_finding": {
      "slot_uri": "",
      "range": "SiteFindingEnum",
      "comments": [],
      "annotations": {}
    },
    "testicular_tissue_weight_processed": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
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
    "age_precision": {
      "slot_uri": "ncit:C48045",
      "range": "AgePrecisionEnum",
      "comments": [
        "(cns) ConsortiumNote: PNOC uses more general dates to avoid PHI"
      ],
      "annotations": {}
    },
    "plurality": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "fertility_consult_eligibility": {
      "slot_uri": "",
      "range": "FertilityConsultEligibilityEnum",
      "comments": [],
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
    "volume_unit": {
      "slot_uri": "",
      "range": "VolumeUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "gestational_age_end_of_pregnancy_days": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "germ_cells_present_follicles": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "testicular_tissue_weight_unit": {
      "slot_uri": "",
      "range": "OtcStripsWeightUnitEnum",
      "comments": [],
      "annotations": {}
    },
    "birth_weight": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "chimerism": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "freezing_method": {
      "slot_uri": "",
      "range": "FreezingMethodEnum",
      "comments": [],
      "annotations": {}
    },
    "birth_weight_unit": {
      "slot_uri": "",
      "range": "BirthWeightUnitEnum",
      "comments": [],
      "annotations": {}
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
    "oocyte_retrieved_numeric": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "delivery_route": {
      "slot_uri": "",
      "range": "DeliveryRouteEnum",
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
    "fertility_tissue_utilized": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "sexual_maturity_index": {
      "slot_uri": "",
      "range": "SexualMaturityIndexEnum",
      "comments": [],
      "annotations": {}
    },
    "cryopreservation_media": {
      "slot_uri": "",
      "range": "CryopreservationMediaEnum",
      "comments": [],
      "annotations": {}
    },
    "follicle_density": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "pregnancy_achieved": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "sct_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "medication_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "age_at_fertility_consult": {
      "slot_uri": "",
      "range": "integer",
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
    "semen_concentration": {
      "slot_uri": "",
      "range": "decimal",
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
    "laboratory_test_specimen_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "shielding": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "otc_surgical_energy_source": {
      "slot_uri": "",
      "range": "OtcSurgicalEnergySourceEnum",
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
    "preimplantation_genetic_testing_type": {
      "slot_uri": "",
      "range": "PreimplantationGeneticTestingTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "menarchal_status": {
      "slot_uri": "",
      "range": "MenarchalStatusEnum",
      "comments": [],
      "annotations": {}
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
    "interpreter_used": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "cryopreservation_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "semen_volume": {
      "slot_uri": "",
      "range": "decimal",
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
    "birth_order": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "otc_strips_number": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "otc_surgical_technique": {
      "slot_uri": "",
      "range": "OtcSurgicalTechniqueEnum",
      "comments": [],
      "annotations": {}
    },
    "gonadotoxic_risk": {
      "slot_uri": "",
      "range": "GonadotoxicRiskEnum",
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
    "reporting_level": {
      "slot_uri": "",
      "range": "ReportingLevelEnum",
      "comments": [],
      "annotations": {}
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
    "fertility_consult_ineligible_reason": {
      "slot_uri": "",
      "range": "FertilityConsultIneligibleReasonEnum",
      "comments": [],
      "annotations": {}
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
    "tissue_type": {
      "slot_uri": "ncit:C119940",
      "range": "TissueTypeEnum",
      "comments": [],
      "annotations": {}
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
    "otc_strips_weight": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "collection_status": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "follicle_density_unit": {
      "slot_uri": "",
      "range": "FollicleDensityUnitEnum",
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
    "tissue_type_utilized": {
      "slot_uri": "",
      "range": "TissueTypeUtilizedEnum",
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
    "fertility_consult_outcome": {
      "slot_uri": "",
      "range": "FertilityConsultOutcomeEnum",
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
    "FertilityConsultWhoPresentEnum": {
      "permissible_values": {
        "Patient And Parents(s)": {
          "meaning": "",
          "comments": []
        },
        "Patient And Partner": {
          "meaning": "",
          "comments": []
        },
        "Patient Only": {
          "meaning": "",
          "comments": []
        },
        "Provider Only": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SexualMaturityIndexEnum": {
      "permissible_values": {
        "NOS, Stage 1": {
          "meaning": "",
          "comments": []
        },
        "NOS, Stage 2": {
          "meaning": "",
          "comments": []
        },
        "NOS, Stage 3": {
          "meaning": "",
          "comments": []
        },
        "NOS, Stage 4": {
          "meaning": "",
          "comments": []
        },
        "NOS, Stage 5": {
          "meaning": "",
          "comments": []
        },
        "Genital, Stage 1": {
          "meaning": "",
          "comments": []
        },
        "Genital, Stage 2": {
          "meaning": "",
          "comments": []
        },
        "Genital, Stage 3": {
          "meaning": "",
          "comments": []
        },
        "Genital, Stage 4": {
          "meaning": "",
          "comments": []
        },
        "Genital, Stage 5": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 1, Female": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 2, Female": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 3, Female": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 4, Female": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 5, Female": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 1, Male": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 2, Male": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 3, Male": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 4, Male": {
          "meaning": "",
          "comments": []
        },
        "Pubic Hair, Stage 5, Male": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "PreimplantationGeneticTestingTypeEnum": {
      "permissible_values": {
        "PGT-A (Aneuploidy)": {
          "meaning": "",
          "comments": []
        },
        "PGT-M (Monogenic/Single Gene Defect)": {
          "meaning": "",
          "comments": []
        },
        "PGT-SR (Structural Rearrangement)": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "GonadotoxicRiskEnum": {
      "permissible_values": {
        "No Previous Therapy": {
          "meaning": "",
          "comments": []
        },
        "Low": {
          "meaning": "",
          "comments": []
        },
        "Intermediate": {
          "meaning": "",
          "comments": []
        },
        "High": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Cranium": {
          "meaning": "ncit:C12789",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "ncit:C12418",
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
        "Occiptial Cortex": {
          "meaning": "ncit:C12757",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Schlemm's Canal": {
          "meaning": "ncit:C12783",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
          "comments": []
        },
        "Testes": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
          "comments": []
        },
        "Uterus": {
          "meaning": "",
          "comments": []
        },
        "Vagina": {
          "meaning": "ncit:C12407",
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
    "OtcResectionTypeEnum": {
      "permissible_values": {
        "Distal to Proximal Removal": {
          "meaning": "",
          "comments": []
        },
        "Proximal to Distal Removal": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationDoseUnitEnum": {
      "permissible_values": {
        "g/m2": {
          "meaning": "",
          "comments": []
        },
        "mg/kg": {
          "meaning": "ncit:C105468",
          "comments": []
        },
        "mg/m2": {
          "meaning": "ncit:C67402",
          "comments": []
        },
        "Units": {
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
        "Intersex, NOS": {
          "meaning": "ncit:C45908",
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
    "AgeAtPregnancyMethodEnum": {
      "permissible_values": {
        "Last Menstrual Period": {
          "meaning": "",
          "comments": []
        },
        "Day of Implantation": {
          "meaning": "",
          "comments": []
        },
        "Ultrasound Dating": {
          "meaning": "",
          "comments": []
        },
        "Unspecified Method": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "PregnancyOutcomeEnum": {
      "permissible_values": {
        "Implantation unsuccessful": {
          "meaning": "",
          "comments": []
        },
        "Term birth of newborn": {
          "meaning": "",
          "comments": []
        },
        "Premature delivery": {
          "meaning": "",
          "comments": []
        },
        "Induced termination of pregnancy": {
          "meaning": "",
          "comments": []
        },
        "Miscarriage": {
          "meaning": "",
          "comments": []
        },
        "Stillbirth": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ReportingLevelEnum": {
      "permissible_values": {
        "Cumulative": {
          "meaning": "",
          "comments": []
        },
        "Fraction": {
          "meaning": "",
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
    "MenarchalStatusEnum": {
      "permissible_values": {
        "Pre-Menarchal": {
          "meaning": "",
          "comments": []
        },
        "Post-Menarchal": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LifetimeCumulativeDoseUnitEnum": {
      "permissible_values": {
        "mg/m2": {
          "meaning": "ncit:C67402",
          "comments": []
        },
        "g/m2": {
          "meaning": "",
          "comments": []
        },
        "mg/kg": {
          "meaning": "",
          "comments": []
        },
        "Units": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DeliveryRouteEnum": {
      "permissible_values": {
        "Vaginal Delivery": {
          "meaning": "",
          "comments": []
        },
        "Cesarean Section": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SpermSourceEnum": {
      "permissible_values": {
        "Partner Sperm": {
          "meaning": "",
          "comments": []
        },
        "Donated Sperm": {
          "meaning": "",
          "comments": []
        },
        "Autologous Testicular Tissue": {
          "meaning": "",
          "comments": []
        },
        "Autologous Testicular Cells": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "CryopreservationMediaEnum": {
      "permissible_values": {
        "Cooper Surgical (SAGE OFC Cryomedia)": {
          "meaning": "",
          "comments": []
        },
        "Modified human tubal fluid 5% DMSO 5% SSS": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "EmbryoVitrificationStageEnum": {
      "permissible_values": {
        "Zygote": {
          "meaning": "",
          "comments": []
        },
        "Cleavage": {
          "meaning": "",
          "comments": []
        },
        "Blastocyst": {
          "meaning": "",
          "comments": []
        },
        "Both Cleavage and Blastocyst": {
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
    "ConceptionTypeEnum": {
      "permissible_values": {
        "Artifical Insemination": {
          "meaning": "ncit:C16739",
          "comments": []
        },
        "In Vitro Fertilization, Conventional": {
          "meaning": "ncit:C16580",
          "comments": []
        },
        "In Vitro Fertilization, Intracytoplasmic Sperm Injection": {
          "meaning": "ncit:C185482",
          "comments": []
        },
        "Egg Donor": {
          "meaning": "",
          "comments": []
        },
        "Ovulation Induction": {
          "meaning": "",
          "comments": []
        },
        "Non-assisted": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "PregnancyPersonEnum": {
      "permissible_values": {
        "Subject": {
          "meaning": "",
          "comments": []
        },
        "Partner": {
          "meaning": "",
          "comments": []
        },
        "Gestational Carrier": {
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
        "EBRT, Stereotactic Radiosurgery": {
          "meaning": "ncit:C15358",
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
        "Radiation Administered": {
          "meaning": "",
          "comments": []
        },
        "Radiation Not Administered": {
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
    "ExposureStatusEnum": {
      "permissible_values": {
        "Current": {
          "meaning": "",
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
    "DiagnosisCategoryEnum": {
      "permissible_values": {
        "Carcinoma In Situ": {
          "meaning": "icdo:8010/2",
          "comments": []
        },
        "Ependymoma": {
          "meaning": "icdo:9391/3",
          "comments": [
            "(cns) ConsortiumNote: Includes ependymal tumors"
          ]
        },
        "Carcinoma": {
          "meaning": "icdo:8010/3",
          "comments": []
        },
        "Large Cell Carcinoma": {
          "meaning": "icdo:8012/3",
          "comments": []
        },
        "Carcinoma, Undifferentiated Type": {
          "meaning": "icdo:8020/3",
          "comments": []
        },
        "Carcinoma, Anaplastic Type": {
          "meaning": "icdo:8021/3",
          "comments": []
        },
        "Papillary carcinoma": {
          "meaning": "icdo:8050/3",
          "comments": []
        },
        "Verrucous carcinoma": {
          "meaning": "icdo:8051/3",
          "comments": []
        },
        "Squamous cell carcinoma in situ": {
          "meaning": "icdo:8070/2",
          "comments": []
        },
        "Squamous cell carcinoma": {
          "meaning": "icdo:8070/3",
          "comments": []
        },
        "Sq. cell carcinoma, keratinizing": {
          "meaning": "icdo:8071/3",
          "comments": []
        },
        "Adenocarcinoma": {
          "meaning": "icdo:8140/3",
          "comments": []
        },
        "Papillary adenocarcinoma": {
          "meaning": "icdo:8260/3",
          "comments": []
        },
        "Malignant melanoma": {
          "meaning": "icdo:8720/3",
          "comments": []
        },
        "Spindle cell melanoma": {
          "meaning": "icdo:8772/3",
          "comments": []
        },
        "Mixed tumor, malignant": {
          "meaning": "icdo:8940/3",
          "comments": []
        },
        "Marginal zone B-cell lymphoma": {
          "meaning": "icdo:9699/3",
          "comments": []
        },
        "Metaplastic carcinoma": {
          "meaning": "icdo:8575/3",
          "comments": []
        },
        "Rhabdomyosarcoma": {
          "meaning": "icdo:8900/3",
          "comments": []
        },
        "Malignant lymphoma": {
          "meaning": "icdo:9590/3",
          "comments": []
        },
        "Hodgkin lymphoma": {
          "meaning": "icdo:9650/3",
          "comments": []
        },
        "Hodgkin lymphoma, mixed cellularity": {
          "meaning": "icdo:9652/3",
          "comments": []
        },
        "Hodgkin lymphoma, lymphocytic deplet.": {
          "meaning": "icdo:9653/3",
          "comments": []
        },
        "Hodgkin lymphoma, nodular sclerosis": {
          "meaning": "icdo:9663/3",
          "comments": []
        },
        "ML, small B lymphocytic": {
          "meaning": "icdo:9670/3",
          "comments": []
        },
        "ML, large B-cell, diffuse, immunoblastic": {
          "meaning": "icdo:9684/3",
          "comments": []
        },
        "Burkitt lymphoma": {
          "meaning": "icdo:9687/3",
          "comments": []
        },
        "Follicular lymphoma": {
          "meaning": "icdo:9690/3",
          "comments": []
        },
        "Mature T-cell lymphoma": {
          "meaning": "icdo:9702/3",
          "comments": []
        },
        "Precursor cell lymphoblastic lymphoma": {
          "meaning": "icdo:9727/3",
          "comments": []
        },
        "Plasmacytoma": {
          "meaning": "icdo:9731/3",
          "comments": []
        },
        "Langerhans cell histiocytosis": {
          "meaning": "icdo:9751/3",
          "comments": []
        },
        "B lymphoblastic leukemia/lymphoma": {
          "meaning": "icdo:9811/3",
          "comments": []
        },
        "Clear cell adenocarcinoma": {
          "meaning": "icdo:8310/3",
          "comments": []
        },
        "Cystadenocarcinoma": {
          "meaning": "icdo:8440/3",
          "comments": []
        },
        "Fibrosarcoma": {
          "meaning": "icdo:8810/3",
          "comments": []
        },
        "Carcinosarcoma": {
          "meaning": "icdo:8980/3",
          "comments": []
        },
        "Solid carcinoma": {
          "meaning": "icdo:8230/3",
          "comments": []
        },
        "Sarcoma": {
          "meaning": "icdo:8800/3",
          "comments": []
        },
        "Liposarcoma": {
          "meaning": "icdo:8850/3",
          "comments": []
        },
        "Leiomyosarcoma": {
          "meaning": "icdo:8890/3",
          "comments": []
        },
        "Transitional Cell Carcinoma": {
          "meaning": "icdo:8120/3",
          "comments": []
        },
        "Small Cell Carcinoma": {
          "meaning": "icdo:8041/3",
          "comments": []
        },
        "Embryonal Carcinoma": {
          "meaning": "icdo:9070/3",
          "comments": []
        },
        "Chordoma": {
          "meaning": "icdo:9370/3",
          "comments": []
        },
        "Medullary Carcinoma": {
          "meaning": "icdo:8510/3",
          "comments": []
        },
        "Stromal Sarcoma": {
          "meaning": "icdo:8935/3",
          "comments": []
        },
        "Micropapillary Carcinoma": {
          "meaning": "icdo:8265/3",
          "comments": []
        },
        "Mucinous Cystadenocarcinoma": {
          "meaning": "icdo:8470/3",
          "comments": []
        },
        "Intraductal Carcinoma, Noninfiltrating": {
          "meaning": "icdo:8500/2",
          "comments": []
        },
        "Intracystic Carcinoma": {
          "meaning": "icdo:8504/3",
          "comments": []
        },
        "Hepatocellular Carcinoma": {
          "meaning": "icdo:8170/3",
          "comments": []
        },
        "Comedocarcinoma": {
          "meaning": "icdo:8501/3",
          "comments": []
        },
        "Papillary Cystadenocarcinoma": {
          "meaning": "icdo:8450/3",
          "comments": []
        },
        "Intraductal Oncocytic Papillary Neoplasm": {
          "meaning": "icdo:8455/2",
          "comments": []
        },
        "Synovial Sarcoma": {
          "meaning": "icdo:9040/3",
          "comments": []
        },
        "Clear Cell Sarcoma, NOS (Except of Kidney M-)": {
          "meaning": "icdo:9044/3",
          "comments": []
        },
        "Teratoma, Malignant": {
          "meaning": "icdo:9080/3",
          "comments": []
        },
        "Neuroblastoma": {
          "meaning": "icdo:9500/3",
          "comments": []
        },
        "Medulloepithelioma": {
          "meaning": "icdo:9501/3",
          "comments": []
        },
        "Neuroepithelioma": {
          "meaning": "icdo:9503/3",
          "comments": []
        },
        "Chondrosarcoma": {
          "meaning": "icdo:9220/3",
          "comments": []
        },
        "Thymoma, Malignant": {
          "meaning": "icdo:8580/3",
          "comments": []
        },
        "Thymic Carcinoma": {
          "meaning": "icdo:8586/3",
          "comments": []
        },
        "Cutaneous T-cell Lymphoma": {
          "meaning": "icdo:9709/3",
          "comments": []
        },
        "Seminoma": {
          "meaning": "icdo:9061/3",
          "comments": []
        },
        "Osteosarcoma": {
          "meaning": "icdo:9180/3",
          "comments": []
        },
        "Immunoproliferative Disease": {
          "meaning": "icdo:9760/3",
          "comments": []
        },
        "Heavy Chain Disease": {
          "meaning": "icdo:9762/3",
          "comments": []
        },
        "Leukemia": {
          "meaning": "icdo:9800/3",
          "comments": []
        },
        "Acute Leukemia": {
          "meaning": "icdo:9801/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia, B/Myeloid": {
          "meaning": "icdo:9808/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia, T/Myeloid": {
          "meaning": "icdo:9809/3",
          "comments": []
        },
        "Lymphoid Leukemia": {
          "meaning": "icdo:9820/3",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia, L2 Type": {
          "meaning": "icdo:9828/3",
          "comments": []
        },
        "Prolymphocytic Leukemia": {
          "meaning": "icdo:9832/3",
          "comments": []
        },
        "Precursor Cell Lymphoblastic Leukemia": {
          "meaning": "icdo:9835/3",
          "comments": []
        },
        "Myeloid Leukemia": {
          "meaning": "icdo:9860/3",
          "comments": []
        },
        "Chronic Myeloid Leukemia": {
          "meaning": "icdo:9863/3",
          "comments": []
        },
        "Therapy-related Acute Myeloid Leukemia": {
          "meaning": "icdo:9920/3",
          "comments": []
        },
        "Chronic Myelomonocytic Leukemia": {
          "meaning": "icdo:9945/3",
          "comments": []
        },
        "Chronic Myeloproliferative Disease": {
          "meaning": "icdo:9960/3",
          "comments": []
        },
        "Therapy-related Myelodysplastic Syndrome": {
          "meaning": "icdo:9987/3",
          "comments": []
        },
        "Myelodysplastic Syndrome": {
          "meaning": "icdo:9989/3",
          "comments": []
        },
        "Precancerous Melanosis": {
          "meaning": "icdo:8741/2",
          "comments": []
        },
        "Dermatofibrosarcoma": {
          "meaning": "icdo:8832/3",
          "comments": []
        },
        "Lobular Carcinoma": {
          "meaning": "icdo:8520/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Keratinizing, in Situ": {
          "meaning": "icdo:8071/2",
          "comments": []
        },
        "Basal Cell Carcinoma": {
          "meaning": "icdo:8090/3",
          "comments": []
        },
        "Infiltrating Basal Cell Carcinoma": {
          "meaning": "icdo:8092/3",
          "comments": []
        },
        "Adenocarcinoma, HPV-independent": {
          "meaning": "icdo:8484/3",
          "comments": []
        },
        "Nephroblastoma": {
          "meaning": "icdo:8960/3",
          "comments": []
        },
        "Retinoblastoma": {
          "meaning": "icdo:9510/3",
          "comments": []
        },
        "Fibroma": {
          "meaning": "icdo:8810/0",
          "comments": []
        },
        "Lipoma": {
          "meaning": "icdo:8850/0",
          "comments": []
        },
        "Angiolipoma": {
          "meaning": "icdo:8861/0",
          "comments": []
        },
        "Teratoma": {
          "meaning": "icdo:9080/1",
          "comments": []
        },
        "Dermoid Cyst": {
          "meaning": "icdo:9084/0",
          "comments": []
        },
        "Hemangioma": {
          "meaning": "icdo:9120/0",
          "comments": []
        },
        "Hemangiopericytoma": {
          "meaning": "icdo:9150/1",
          "comments": []
        },
        "Meningioma": {
          "meaning": "icdo:9530/0",
          "comments": []
        },
        "Meningiomatosis": {
          "meaning": "icdo:9530/1",
          "comments": []
        },
        "Paraganglioma": {
          "meaning": "icdo:8680/1",
          "comments": []
        },
        "Astrocytoma": {
          "meaning": "icdo:9400/3",
          "comments": []
        },
        "Glioblastoma": {
          "meaning": "icdo:9440/3",
          "comments": []
        },
        "Oligodendroglioma": {
          "meaning": "icdo:9450/3",
          "comments": []
        },
        "Embryonal Tumor with Multilayered Rosettes": {
          "meaning": "icdo:9478/3",
          "comments": []
        },
        "Ganglioglioma": {
          "meaning": "icdo:9505/1",
          "comments": []
        },
        "Neurofibroma": {
          "meaning": "icdo:9540/0",
          "comments": []
        },
        "Neurofibromatosis": {
          "meaning": "icdo:9540/1",
          "comments": []
        },
        "Neurilemoma": {
          "meaning": "icdo:9560/0",
          "comments": []
        },
        "Neuroma": {
          "meaning": "icdo:9570/0",
          "comments": []
        },
        "Perineurioma": {
          "meaning": "icdo:9571/0",
          "comments": []
        },
        "Choroid Plexus Papilloma": {
          "meaning": "icdo:9390/0",
          "comments": []
        },
        "Medulloblastoma": {
          "meaning": "icdo:9470/3",
          "comments": []
        },
        "Cerebellar Sarcoma": {
          "meaning": "icdo:9480/3",
          "comments": []
        },
        "Leiomyoma": {
          "meaning": "icdo:8890/0",
          "comments": []
        },
        "Smooth Muscle Tumor": {
          "meaning": "icdo:8897/1",
          "comments": []
        },
        "Rhabdomyoma": {
          "meaning": "icdo:8900/0",
          "comments": []
        },
        "Hemangioendothelioma": {
          "meaning": "icdo:9130/1",
          "comments": []
        },
        "Follicular Adenocarcinoma": {
          "meaning": "icdo:8330/3",
          "comments": []
        },
        "Clear Cell Tumor": {
          "meaning": "icdo:8005/0",
          "comments": []
        },
        "Adenoma": {
          "meaning": "icdo:8140/0",
          "comments": []
        },
        "Papillary Adenoma": {
          "meaning": "icdo:8260/0",
          "comments": []
        },
        "Pituitary Adenoma": {
          "meaning": "icdo:8272/0",
          "comments": []
        },
        "Pituitary Carcinoma": {
          "meaning": "icdo:8272/3",
          "comments": []
        },
        "Granular Cell Tumor": {
          "meaning": "icdo:9580/0",
          "comments": []
        },
        "Pinealoma": {
          "meaning": "icdo:9360/1",
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
    "InsuranceTypeEnum": {
      "permissible_values": {
        "Public": {
          "meaning": "",
          "comments": []
        },
        "Private": {
          "meaning": "",
          "comments": []
        },
        "Military": {
          "meaning": "",
          "comments": []
        },
        "No Insurance": {
          "meaning": "",
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
        "Plasma": {
          "meaning": "ncit:C185204",
          "comments": []
        },
        "Serum": {
          "meaning": "ncit:C178987",
          "comments": []
        },
        "Urine": {
          "meaning": "ncit:C13283",
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
    "StageSystemEnum": {
      "permissible_values": {
        "AIDS-Related Kaposi Sarcoma Stage": {
          "meaning": "ncit:C134969",
          "comments": []
        },
        "AJCC v6 Stage": {
          "meaning": "ncit:C90529",
          "comments": []
        },
        "AJCC v7 Stage": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC v8 Stage": {
          "meaning": "ncit:C132248",
          "comments": []
        },
        "Ann Arbor": {
          "meaning": "ncit:C54179",
          "comments": []
        },
        "Children's Oncology Group": {
          "meaning": "ncit:C39353",
          "comments": []
        },
        "Children's Oncology Group Liver Tumor Staging System": {
          "meaning": "ncit:C177630",
          "comments": []
        },
        "Children's Oncology Group Neuroblastoma Risk Group Staging System": {
          "meaning": "ncit:C177631",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Retinoblastoma Risk Group Staging System": {
          "meaning": "ncit:C177633",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System": {
          "meaning": "ncit:C140271",
          "comments": []
        },
        "EVANS": {
          "meaning": "ncit:C85407",
          "comments": []
        },
        "Enneking Staging System": {
          "meaning": "ncit:C140258",
          "comments": []
        },
        "FIGO": {
          "meaning": "ncit:C125738",
          "comments": []
        },
        "INRGSS": {
          "meaning": "ncit:C133427",
          "comments": []
        },
        "INSS": {
          "meaning": "ncit:C85416",
          "comments": []
        },
        "Intergroup Rhabdomyosarcoma Study Group Clinical Staging and Grouping System": {
          "meaning": "ncit:C148010",
          "comments": []
        },
        "International Retinoblastoma Staging System": {
          "meaning": "",
          "comments": []
        },
        "International Society of Pediatric Oncology Staging System": {
          "meaning": "ncit:C140270",
          "comments": []
        },
        "Lugano Stage": {
          "meaning": "ncit:C141147",
          "comments": []
        },
        "PRETEXT Staging System": {
          "meaning": "ncit:C141133",
          "comments": []
        },
        "Pediatric Oncology Group Neuroblastoma Staging System": {
          "meaning": "ncit:C85423",
          "comments": []
        },
        "Reese-Ellsworth Staging System": {
          "meaning": "",
          "comments": []
        },
        "St. Jude Stage": {
          "meaning": "ncit:C141216",
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
        "Fertility Preservation And Outcomes Of Fertility Treatment Registries": {
          "meaning": "",
          "comments": []
        },
        "National Fertility Preservation Database": {
          "meaning": "",
          "comments": []
        },
        "NIH 000106": {
          "meaning": "",
          "comments": []
        },
        "NIH 000715": {
          "meaning": "",
          "comments": []
        },
        "De-Identified Clinical Data Of Patients Seen At Indiana University": {
          "meaning": "",
          "comments": []
        },
        "De-Identified Patients Seen For Oncofertility At Cincinnati Children'S Hospital Medical Center": {
          "meaning": "",
          "comments": []
        },
        "National Oncofertility Database": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OtcConversionReasonEnum": {
      "permissible_values": {
        "Purpose of Fertility Presevation Only": {
          "meaning": "",
          "comments": []
        },
        "Secondary To Surgical Complication": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OtcSurgicalTechniqueEnum": {
      "permissible_values": {
        "Laparotomy Only": {
          "meaning": "",
          "comments": []
        },
        "Laparascopy Only": {
          "meaning": "",
          "comments": []
        },
        "Laparoscopy Converted to Laparotomy": {
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
    "DiagnosisEnum": {
      "permissible_values": {
        "Adamantinomatous Craniopharyngioma": {
          "meaning": "ncit:C4726",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Craniopharyngioma'"
          ]
        },
        "Adenocarcinoma, NOS": {
          "meaning": "icdo:8140/3",
          "comments": []
        },
        "Adenoma, NOS": {
          "meaning": "icdo:8140/0",
          "comments": []
        },
        "Adenosarcoma": {
          "meaning": "icdo:8933/3",
          "comments": []
        },
        "Angiocentric Glioma": {
          "meaning": "icdo:9431/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Low-Grade Glioma'"
          ]
        },
        "Angiomyosarcoma": {
          "meaning": "icdo:8894/3",
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
        "Atypical Choroid Plexus Papilloma": {
          "meaning": "ncit:C53686",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Choroid Plexus Tumors'"
          ]
        },
        "Carcinoma, NOS": {
          "meaning": "icdo:8010/3",
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
        "Choriocarcinoma": {
          "meaning": "ncit:C2948",
          "comments": []
        },
        "Clear cell sarcoma, NOS": {
          "meaning": "icdo:9044/3",
          "comments": []
        },
        "Craniopharyngioma": {
          "meaning": "icdo:9350/1",
          "comments": []
        },
        "Cystadenocarcinoma, NOS": {
          "meaning": "icdo:8440/3",
          "comments": []
        },
        "Dedifferentiated Liposarcoma": {
          "meaning": "ncit:C3704",
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
        "Epithelioid Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "ncit:C6561",
          "comments": []
        },
        "Ewing Sarcoma": {
          "meaning": "icdo:9260/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Fibroblastic Osteosarcoma": {
          "meaning": "ncit:C4020",
          "comments": []
        },
        "Fibrolipoma": {
          "meaning": "icdo:8851/0",
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
        "Gangliocytoma": {
          "meaning": "icdo:9492/0",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Glioneuronal and Neuronal Tumors'"
          ]
        },
        "Ganglioneuroblastoma": {
          "meaning": "icdo:9490/3",
          "comments": []
        },
        "Ganglioneuroma": {
          "meaning": "icdo:9490/0",
          "comments": []
        },
        "Gastroblastoma": {
          "meaning": "icdo:8976/3",
          "comments": []
        },
        "Germinoma": {
          "meaning": "ncit:C3753",
          "comments": []
        },
        "Gliofibroma": {
          "meaning": "icdo:9442/1",
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
        "Hemangioma, NOS": {
          "meaning": "icdo:9120/0",
          "comments": []
        },
        "Hemangiopericytoma, NOS": {
          "meaning": "icdo:9150/1",
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
        "Histiocytic Sarcoma": {
          "meaning": "ncit:C27349",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Hodgkin Lymphoma, NOS": {
          "meaning": "icdo:9650/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nodular Sclerosis, NOS": {
          "meaning": "icdo:9663/3",
          "comments": []
        },
        "Infantile Fibrosarcoma": {
          "meaning": "icdo:8814/3",
          "comments": []
        },
        "Intimal Sarcoma": {
          "meaning": "icdo:9137/3",
          "comments": []
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
        "Kaposi Sarcoma": {
          "meaning": "icdo:9140/3",
          "comments": []
        },
        "Leiomyosarcoma, NOS": {
          "meaning": "icdo:8890/3",
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
        "Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "icdo:9540/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Medullomyoblastoma": {
          "meaning": "icdo:9472/3",
          "comments": []
        },
        "Meningioma, NOS": {
          "meaning": "icdo:9530/0",
          "comments": []
        },
        "Mesenchymal Chondrosarcoma": {
          "meaning": "icdo:9240/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Mixed Germ Cell Tumor": {
          "meaning": "ncit:C4290",
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
        "Neuroma, NOS": {
          "meaning": "icdo:9570/0",
          "comments": []
        },
        "Neurothekeoma": {
          "meaning": "icdo:9562/0",
          "comments": []
        },
        "Oligodendroblastoma": {
          "meaning": "icdo:9460/3",
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
        "Parosteal Osteosarcoma": {
          "meaning": "icdo:9192/3",
          "comments": []
        },
        "Perineurioma, NOS": {
          "meaning": "icdo:9571/0",
          "comments": []
        },
        "Periosteal Osteosarcoma": {
          "meaning": "icdo:9193/3",
          "comments": []
        },
        "Pheochromocytoma": {
          "meaning": "icdo:8700/3",
          "comments": []
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
        "Plasmacytoma, NOS": {
          "meaning": "icdo:9731/3",
          "comments": []
        },
        "Pleomorphic Xanthoastrocytoma": {
          "meaning": "icdo:9424/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'High-Grade Glioma'"
          ]
        },
        "Pleomorphic Liposarcoma": {
          "meaning": "icdo:8854/3",
          "comments": []
        },
        "Polymorphic PTLD": {
          "meaning": "icdo:9971/3",
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
        "Rhabdomyoma, NOS": {
          "meaning": "icdo:8900/0",
          "comments": []
        },
        "Rhabdomyosarcoma, NOS": {
          "meaning": "icdo:8900/3",
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
        "Spongioneuroblastoma": {
          "meaning": "icdo:9504/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, NOS": {
          "meaning": "icdo:8070/3",
          "comments": []
        },
        "Subependymoma": {
          "meaning": "icdo:9383/1",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Ependymoma'"
          ]
        },
        "Sympathetic Paraganglioma": {
          "meaning": "icdo:8681/3",
          "comments": []
        },
        "Teratocarcinoma": {
          "meaning": "icdo:9081/3",
          "comments": []
        },
        "Neoplasm, Malignant": {
          "meaning": "icdo:8000/3",
          "comments": []
        },
        "Tumor Cells, Malignant": {
          "meaning": "icdo:8001/3",
          "comments": []
        },
        "Malignant Tumor, Small Cell Type": {
          "meaning": "icdo:8002/3",
          "comments": []
        },
        "Malignant Tumor, Giant Cell Type": {
          "meaning": "icdo:8003/3",
          "comments": []
        },
        "Malignant Tumor, Spindle Cell Type": {
          "meaning": "icdo:8004/3",
          "comments": []
        },
        "Malignant Tumor, Clear Cell Type": {
          "meaning": "icdo:8005/3",
          "comments": []
        },
        "Carcinoma In Situ, NOS": {
          "meaning": "icdo:8010/2",
          "comments": []
        },
        "Epithelioma, Malignant": {
          "meaning": "icdo:8011/3",
          "comments": []
        },
        "Large Cell Carcinoma, NOS": {
          "meaning": "icdo:8012/3",
          "comments": []
        },
        "Large Cell Neuroendocrine Carcinoma": {
          "meaning": "icdo:8013/3",
          "comments": []
        },
        "Large Cell Carcinoma With Rhabdoid Phenotype": {
          "meaning": "icdo:8014/3",
          "comments": []
        },
        "Glassy Cell Carcinoma": {
          "meaning": "icdo:8015/3",
          "comments": []
        },
        "Carcinoma, Undifferentiated Type, NOS": {
          "meaning": "icdo:8020/3",
          "comments": []
        },
        "Carcinoma, Anaplastic Type, NOS": {
          "meaning": "icdo:8021/3",
          "comments": []
        },
        "Pleomorphic Carcinoma": {
          "meaning": "icdo:8022/3",
          "comments": []
        },
        "Giant Cell And Spindle Cell Carcinoma": {
          "meaning": "icdo:8030/3",
          "comments": []
        },
        "Giant Cell Carcinoma": {
          "meaning": "icdo:8031/3",
          "comments": []
        },
        "Spindle Cell Carcinoma": {
          "meaning": "icdo:8032/3",
          "comments": []
        },
        "Pseudosarcomatous Carcinoma": {
          "meaning": "icdo:8033/3",
          "comments": []
        },
        "Polygonal Cell Carcinoma": {
          "meaning": "icdo:8034/3",
          "comments": []
        },
        "Carcinoma With Osteoclast-Like Giant Cells": {
          "meaning": "icdo:8035/3",
          "comments": []
        },
        "Papillary Carcinoma In Situ": {
          "meaning": "icdo:8050/2",
          "comments": []
        },
        "Papillary Carcinoma, NOS": {
          "meaning": "icdo:8050/3",
          "comments": []
        },
        "Verrucous Carcinoma, NOS": {
          "meaning": "icdo:8051/3",
          "comments": []
        },
        "Papillary Squamous Cell Carcinoma, Non-Invasive": {
          "meaning": "icdo:8052/2",
          "comments": []
        },
        "Papillary Squamous Cell Carcinoma": {
          "meaning": "icdo:8052/3",
          "comments": []
        },
        "Squamous Cell Carcinoma In Situ, NOS": {
          "meaning": "icdo:8070/2",
          "comments": []
        },
        "Sq. Cell Carcinoma, Keratinizing, NOS": {
          "meaning": "icdo:8071/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Lg. Cell, Non-Ker.": {
          "meaning": "icdo:8072/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Sm. Cell, Non-Ker.": {
          "meaning": "icdo:8073/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Spindle Cell": {
          "meaning": "icdo:8074/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, Adenoid": {
          "meaning": "icdo:8075/3",
          "comments": []
        },
        "Sq. Cell Carc. In Situ With Question. Stromal Invas.": {
          "meaning": "icdo:8076/2",
          "comments": []
        },
        "Sq. Cell Carcinoma, Micro-Invasive": {
          "meaning": "icdo:8076/3",
          "comments": []
        },
        "Squamous Cell Carcinoma With Horn Formation": {
          "meaning": "icdo:8078/3",
          "comments": []
        },
        "Bowen Disease": {
          "meaning": "icdo:8081/2",
          "comments": []
        },
        "Lymphoepithelial Carcinoma": {
          "meaning": "icdo:8082/3",
          "comments": []
        },
        "Basaloid Squamous Cell Carcinoma": {
          "meaning": "icdo:8083/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, Clear Cell Type": {
          "meaning": "icdo:8084/3",
          "comments": []
        },
        "Adenocarcinoma In Situ": {
          "meaning": "icdo:8140/2",
          "comments": []
        },
        "Scirrhous Adenocarcinoma": {
          "meaning": "icdo:8141/3",
          "comments": []
        },
        "Superficial Spreading Adenocarcinoma": {
          "meaning": "icdo:8143/3",
          "comments": []
        },
        "Basal Cell Adenocarcinoma": {
          "meaning": "icdo:8147/3",
          "comments": []
        },
        "Adenoid Cystic Carcinoma": {
          "meaning": "icdo:8200/3",
          "comments": []
        },
        "Cribriform Carcinoma In Situ": {
          "meaning": "icdo:8201/2",
          "comments": []
        },
        "Cribriform Carcinoma": {
          "meaning": "icdo:8201/3",
          "comments": []
        },
        "Adenocarcinoma With Mixed Subtypes": {
          "meaning": "icdo:8255/3",
          "comments": []
        },
        "Papillary Adenocarcinoma, NOS": {
          "meaning": "icdo:8260/3",
          "comments": []
        },
        "Adenocarcinoma In Situ In Villous Adenoma": {
          "meaning": "icdo:8261/2",
          "comments": []
        },
        "Adenocarcinoma In Villous Adenoma": {
          "meaning": "icdo:8261/3",
          "comments": []
        },
        "Villous Adenocarcinoma": {
          "meaning": "icdo:8262/3",
          "comments": []
        },
        "Adenocarcinoma In Situ In Tubulovillous Adenoma": {
          "meaning": "icdo:8263/2",
          "comments": []
        },
        "Adenocarcinoma In Tubulovillous Adenoma": {
          "meaning": "icdo:8263/3",
          "comments": []
        },
        "Mucoepidermoid Carcinoma": {
          "meaning": "icdo:8430/3",
          "comments": []
        },
        "Mucinous Adenocarcinoma": {
          "meaning": "icdo:8480/3",
          "comments": []
        },
        "Mucin-Producing Adenocarcinoma": {
          "meaning": "icdo:8481/3",
          "comments": []
        },
        "Melanoma In Situ": {
          "meaning": "icdo:8720/2",
          "comments": []
        },
        "Malignant Melanoma, NOS": {
          "meaning": "icdo:8720/3",
          "comments": []
        },
        "Nodular Melanoma": {
          "meaning": "icdo:8721/3",
          "comments": []
        },
        "Balloon Cell Melanoma": {
          "meaning": "icdo:8722/3",
          "comments": []
        },
        "Malignant Melanoma, Regressing": {
          "meaning": "icdo:8723/3",
          "comments": []
        },
        "Amelanotic Melanoma": {
          "meaning": "icdo:8730/3",
          "comments": []
        },
        "Superficial Spreading Melanoma": {
          "meaning": "icdo:8743/3",
          "comments": []
        },
        "Desmoplastic Melanoma, Malignant": {
          "meaning": "icdo:8745/3",
          "comments": []
        },
        "Mucosal Lentiginous Melanoma": {
          "meaning": "icdo:8746/3",
          "comments": []
        },
        "Mixed Epithel. & Spindle Cell Melanoma": {
          "meaning": "icdo:8770/3",
          "comments": []
        },
        "Epithelioid Cell Melanoma": {
          "meaning": "icdo:8771/3",
          "comments": []
        },
        "Spindle Cell Melanoma, NOS": {
          "meaning": "icdo:8772/3",
          "comments": []
        },
        "Mixed Tumor, Malignant, NOS": {
          "meaning": "icdo:8940/3",
          "comments": []
        },
        "Carcinoma In Pleomorphic Adenoma": {
          "meaning": "icdo:8941/3",
          "comments": []
        },
        "Marginal Zone B-Cell Lymphoma, NOS": {
          "meaning": "icdo:9699/3",
          "comments": []
        },
        "Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma": {
          "meaning": "icdo:9823/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, HPV-Positive": {
          "meaning": "icdo:8085/3",
          "comments": []
        },
        "Squamous Cell Carcinoma, HPV-Negative": {
          "meaning": "icdo:8086/3",
          "comments": []
        },
        "Adenosquamous Carcinoma": {
          "meaning": "icdo:8560/3",
          "comments": []
        },
        "Epithelial-Myoepithelial Carcinoma": {
          "meaning": "icdo:8562/3",
          "comments": []
        },
        "Adenocarcinoma With Squamous Metaplasia": {
          "meaning": "icdo:8570/3",
          "comments": []
        },
        "Adenocarcinoma With Cartilaginous & Oss. Metaplasia": {
          "meaning": "icdo:8571/3",
          "comments": []
        },
        "Adenocarcinoma With Spindle Cell Metaplasia": {
          "meaning": "icdo:8572/3",
          "comments": []
        },
        "Adenocarcinoma With Apocrine Metaplasia": {
          "meaning": "icdo:8573/3",
          "comments": []
        },
        "Adenocarcinoma With Neuroendocrine Differentiation": {
          "meaning": "icdo:8574/3",
          "comments": []
        },
        "Metaplastic Carcinoma, NOS": {
          "meaning": "icdo:8575/3",
          "comments": []
        },
        "Myofibroblastic Sarcoma": {
          "meaning": "icdo:8825/3",
          "comments": []
        },
        "Pleomorphic Rhabdomyosarcoma, Adult Type": {
          "meaning": "icdo:8901/3",
          "comments": []
        },
        "Mixed Type Rhabdomyosarcoma": {
          "meaning": "icdo:8902/3",
          "comments": []
        },
        "Embryonal Rhabdomyosarcoma": {
          "meaning": "icdo:8910/3",
          "comments": []
        },
        "Spindle Cell Rhabdomyosarcoma": {
          "meaning": "icdo:8912/3",
          "comments": []
        },
        "Malignant Lymphoma, NOS": {
          "meaning": "icdo:9590/3",
          "comments": []
        },
        "Malignant Lymphoma, Non-Hodgkin": {
          "meaning": "icdo:9591/3",
          "comments": []
        },
        "Composite Hodgkin and Non-Hodgkin Lymphoma": {
          "meaning": "icdo:9596/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocyte-Rich": {
          "meaning": "icdo:9651/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Mixed Cellularity, NOS": {
          "meaning": "icdo:9652/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocytic Deplet., NOS": {
          "meaning": "icdo:9653/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocytic Deplet., Diffuse Fibrosis": {
          "meaning": "icdo:9654/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Lymphocytic Deplet., Reticular": {
          "meaning": "icdo:9655/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nodular Lymphocyte Predom.": {
          "meaning": "icdo:9659/3",
          "comments": []
        },
        "Hodgkin Granuloma [Obs]": {
          "meaning": "icdo:9661/3",
          "comments": []
        },
        "Hodgkin Sarcoma [Obs]": {
          "meaning": "icdo:9662/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nod. Scler., Cellular Phase": {
          "meaning": "icdo:9664/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nod. Scler., Grade 1": {
          "meaning": "icdo:9665/3",
          "comments": []
        },
        "Hodgkin Lymphoma, Nod. Scler., Grade 2": {
          "meaning": "icdo:9667/3",
          "comments": []
        },
        "ML, Small B Lymphocytic, NOS": {
          "meaning": "icdo:9670/3",
          "comments": []
        },
        "ML, Lymphoplasmacytic": {
          "meaning": "icdo:9671/3",
          "comments": []
        },
        "Mantle Cell Lymphoma": {
          "meaning": "icdo:9673/3",
          "comments": []
        },
        "ML, Mixed Sm. and Lg. Cell, Diffuse": {
          "meaning": "icdo:9675/3",
          "comments": []
        },
        "ML, Large B-Cell, Diffuse": {
          "meaning": "icdo:9680/3",
          "comments": []
        },
        "ML, Large B-Cell, Diffuse, Immunoblastic, NOS": {
          "meaning": "icdo:9684/3",
          "comments": []
        },
        "Burkitt Lymphoma, NOS": {
          "meaning": "icdo:9687/3",
          "comments": []
        },
        "T-Cell Histiocyte Rich Large B-Cell Lymphoma": {
          "meaning": "icdo:9688/3",
          "comments": []
        },
        "Follicular Lymphoma, NOS": {
          "meaning": "icdo:9690/3",
          "comments": []
        },
        "Follicular Lymphoma, Grade 2": {
          "meaning": "icdo:9691/3",
          "comments": []
        },
        "Follicular Lymphoma, Grade 1": {
          "meaning": "icdo:9695/3",
          "comments": []
        },
        "Follicular Lymphoma, Grade 3": {
          "meaning": "icdo:9698/3",
          "comments": []
        },
        "Sezary Syndrome": {
          "meaning": "icdo:9701/3",
          "comments": []
        },
        "Mature T-Cell Lymphoma, NOS": {
          "meaning": "icdo:9702/3",
          "comments": []
        },
        "Angioimmunoblastic T-Cell Lymphoma": {
          "meaning": "icdo:9705/3",
          "comments": []
        },
        "Anaplastic Large Cell Lymphoma, T-Cell and Null Cell Type": {
          "meaning": "icdo:9714/3",
          "comments": []
        },
        "Anaplastic Large Cell Lymphoma, ALK Negative": {
          "meaning": "icdo:9715/3",
          "comments": []
        },
        "NK/T-Cell Lymphoma, Nasal and Nasal-Type": {
          "meaning": "icdo:9719/3",
          "comments": []
        },
        "Systemic EBV Pos. T-Cell Lymphoproliferative Disease of Childhood": {
          "meaning": "icdo:9724/3",
          "comments": []
        },
        "Precursor Cell Lymphoblastic Lymphoma, NOS": {
          "meaning": "icdo:9727/3",
          "comments": []
        },
        "Precursor B-Cell Lymphoblastic Lymphoma": {
          "meaning": "icdo:9728/3",
          "comments": []
        },
        "Precursor T-Cell Lymphoblastic Lymphoma": {
          "meaning": "icdo:9729/3",
          "comments": []
        },
        "Plasmacytoma, Extramedullary": {
          "meaning": "icdo:9734/3",
          "comments": []
        },
        "Plasmablastic Lymphoma": {
          "meaning": "icdo:9735/3",
          "comments": []
        },
        "ALK Positive Large B-Cell Lymphoma": {
          "meaning": "icdo:9737/3",
          "comments": []
        },
        "Lrg B-Cell Lymphoma in HHV8-Assoc. Multicentric Castleman DZ": {
          "meaning": "icdo:9738/3",
          "comments": []
        },
        "Mast Cell Sarcoma": {
          "meaning": "icdo:9740/3",
          "comments": []
        },
        "Malignant Mastocytosis": {
          "meaning": "icdo:9741/3",
          "comments": []
        },
        "Erdhiem-Chester Disease": {
          "meaning": "icdo:9749/3",
          "comments": []
        },
        "Malignant Histiocytosis": {
          "meaning": "icdo:9750/3",
          "comments": []
        },
        "Langerhans Cell Histiocytosis, NOS": {
          "meaning": "icdo:9751/3",
          "comments": []
        },
        "Langerhans Cell Histiocytosis, Disseminated": {
          "meaning": "icdo:9754/3",
          "comments": []
        },
        "Langerhans Cell Sarcoma": {
          "meaning": "icdo:9756/3",
          "comments": []
        },
        "Interdigitating Dendritic Cell Sarcoma": {
          "meaning": "icdo:9757/3",
          "comments": []
        },
        "Follicular Dendritic Cell Sarcoma": {
          "meaning": "icdo:9758/3",
          "comments": []
        },
        "Fibroblastic Reticular Cell Tumor": {
          "meaning": "icdo:9759/3",
          "comments": []
        },
        "Lymphomatoid Granulomatosis, Grade 3": {
          "meaning": "icdo:9766/3",
          "comments": []
        },
        "B Lymphoblastic Leukemia/Lymphoma, NOS": {
          "meaning": "icdo:9811/3",
          "comments": []
        },
        "Leukemia/Lymphoma with t(9;22)(q34;q11.2);BCR-ABL1": {
          "meaning": "icdo:9812/3",
          "comments": []
        },
        "Leukemia/Lymphoma with t(v;11q23);MLL Rearranged": {
          "meaning": "icdo:9813/3",
          "comments": []
        },
        "Leukemia/Lymphoma with t(12;21)(p13;q22);TEL-AML1(ETV6-RUNX1)": {
          "meaning": "icdo:9814/3",
          "comments": []
        },
        "B Lymphoblastic Leukemia/Lymphoma with Hyperdiploidy": {
          "meaning": "icdo:9815/3",
          "comments": []
        },
        "Leukemia/Lymphoma with Hypodiploidy (Hypodiploid ALL)": {
          "meaning": "icdo:9816/3",
          "comments": []
        },
        "B Lymphoblastic Leukemia/Lymphoma with t(5;14)(q31;q32);IL3-IGH": {
          "meaning": "icdo:9817/3",
          "comments": []
        },
        "Leukemia/Lymphoma with t(1;19)(q23;p13.3);E2A PBX1 (TCF3 PBX1)": {
          "meaning": "icdo:9818/3",
          "comments": []
        },
        "B-Lymphocytic Leukemia/Lymphoma, BCR-ABL1-Like": {
          "meaning": "icdo:9819/3",
          "comments": []
        },
        "T-Cell Large Granular Lymphocytic Leukemia": {
          "meaning": "icdo:9831/3",
          "comments": []
        },
        "T Lymphoblastic Leukemia/Lymphoma": {
          "meaning": "icdo:9837/3",
          "comments": []
        },
        "Myeloid and Lymphoid Neoplasms with PDGFRB Rearrangement": {
          "meaning": "icdo:9965/3",
          "comments": []
        },
        "Myeloid and Lymphoid Neoplasm with FGFR1 Abnormalities": {
          "meaning": "icdo:9967/3",
          "comments": []
        },
        "Myelodysplastic/Myeloproliferative Neoplasm, Unclassifiable": {
          "meaning": "icdo:9975/3",
          "comments": []
        },
        "Clear Cell Adenocarcinoma, NOS": {
          "meaning": "icdo:8310/3",
          "comments": []
        },
        "Acinar Cell Carcinoma": {
          "meaning": "icdo:8550/3",
          "comments": []
        },
        "Acinar Cell Cystadenocarcinoma": {
          "meaning": "icdo:8551/3",
          "comments": []
        },
        "Fascial Fibrosarcoma": {
          "meaning": "icdo:8813/3",
          "comments": []
        },
        "Carcinosarcoma, Nos": {
          "meaning": "icdo:8980/3",
          "comments": []
        },
        "Carcinosarcoma, Embryonal Type": {
          "meaning": "icdo:8981/3",
          "comments": []
        },
        "Malignant Myoepithelioma": {
          "meaning": "icdo:8982/3",
          "comments": []
        },
        "Trabecular Adenocarcinoma": {
          "meaning": "icdo:8190/3",
          "comments": []
        },
        "Duct Carcinoma In Situ, Solid Type": {
          "meaning": "icdo:8230/2",
          "comments": []
        },
        "Solid Carcinoma, Nos": {
          "meaning": "icdo:8230/3",
          "comments": []
        },
        "Carcinoma Simplex": {
          "meaning": "icdo:8231/3",
          "comments": []
        },
        "Oxyphilic Adenocarcinoma": {
          "meaning": "icdo:8290/3",
          "comments": []
        },
        "Invasive Carcinoma Of No Special Type": {
          "meaning": "icdo:8500/3",
          "comments": []
        },
        "Secretory Carcinoma Of No Special Type": {
          "meaning": "icdo:8502/3",
          "comments": []
        },
        "Polymorphous Low Grade Adenocarcinoma": {
          "meaning": "icdo:8525/3",
          "comments": []
        },
        "Warthin Tumor, Malignant": {
          "meaning": "icdo:8561/3",
          "comments": []
        },
        "Sarcoma, Nos": {
          "meaning": "icdo:8800/3",
          "comments": []
        },
        "Spindle Cell Sarcoma": {
          "meaning": "icdo:8801/3",
          "comments": []
        },
        "Giant Cell Sarcoma": {
          "meaning": "icdo:8802/3",
          "comments": []
        },
        "Small Cell Sarcoma": {
          "meaning": "icdo:8803/3",
          "comments": []
        },
        "Epithelioid Sarcoma": {
          "meaning": "icdo:8804/3",
          "comments": []
        },
        "Undifferentiated Sarcoma": {
          "meaning": "icdo:8805/3",
          "comments": []
        },
        "Liposarcoma, Nos": {
          "meaning": "icdo:8850/3",
          "comments": []
        },
        "Liposarcoma, Well Differentiated": {
          "meaning": "icdo:8851/3",
          "comments": []
        },
        "Round Cell Liposarcoma": {
          "meaning": "icdo:8853/3",
          "comments": []
        },
        "Mixed Type Liposarcoma": {
          "meaning": "icdo:8855/3",
          "comments": []
        },
        "Fibroblastic Liposarcoma": {
          "meaning": "icdo:8857/3",
          "comments": []
        },
        "Epithelioid Leiomyosarcoma": {
          "meaning": "icdo:8891/3",
          "comments": []
        },
        "Mesenchymoma, Malignant": {
          "meaning": "icdo:8990/3",
          "comments": []
        },
        "Embryonal Sarcoma": {
          "meaning": "icdo:8991/3",
          "comments": []
        },
        "Transitional Cell Carcinoma In Situ": {
          "meaning": "icdo:8120/2",
          "comments": []
        },
        "Transitional Cell Carcinoma, Nos": {
          "meaning": "icdo:8120/3",
          "comments": []
        },
        "Schneiderian Carcinoma": {
          "meaning": "icdo:8121/3",
          "comments": []
        },
        "Trans. Cell Carcinoma, Spindle Cell": {
          "meaning": "icdo:8122/3",
          "comments": []
        },
        "Basaloid Carcinoma": {
          "meaning": "icdo:8123/3",
          "comments": []
        },
        "Cloacogenic Carcinoma": {
          "meaning": "icdo:8124/3",
          "comments": []
        },
        "Mal. Melanoma In Giant Pigmented Nevus": {
          "meaning": "icdo:8761/3",
          "comments": []
        },
        "Small Cell Carcinoma, Nos": {
          "meaning": "icdo:8041/3",
          "comments": []
        },
        "Small Cell Carcinoma, Fusiform Cell": {
          "meaning": "icdo:8043/3",
          "comments": []
        },
        "Embryonal Carcinoma, Nos": {
          "meaning": "icdo:9070/3",
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
        "Chordoma, Nos": {
          "meaning": "icdo:9370/3",
          "comments": []
        },
        "Chondroid Chordoma": {
          "meaning": "icdo:9371/3",
          "comments": []
        },
        "Dedifferentiated Chordoma": {
          "meaning": "icdo:9372/3",
          "comments": []
        },
        "Combined Small Cell Carcinoma": {
          "meaning": "icdo:8045/3",
          "comments": []
        },
        "Carcinoma, Diffuse Type": {
          "meaning": "icdo:8145/3",
          "comments": []
        },
        "Mixed Neuroendocrine Non-Neuroendocrine Neoplasm": {
          "meaning": "icdo:8154/3",
          "comments": []
        },
        "Carcinoid Tumor, Malignant": {
          "meaning": "icdo:8240/3",
          "comments": []
        },
        "Composite Carcinoid": {
          "meaning": "icdo:8244/3",
          "comments": []
        },
        "Neuroendocrine Carcinoma": {
          "meaning": "icdo:8246/3",
          "comments": []
        },
        "Neuroendocrine Tumor": {
          "meaning": "icdo:8249/3",
          "comments": []
        },
        "Linitis Plastica": {
          "meaning": "icdo:8142/3",
          "comments": []
        },
        "Intestinal-Type Adenoma, High Grade": {
          "meaning": "icdo:8144/2",
          "comments": []
        },
        "Adenocarcinoma, Intestinal Type": {
          "meaning": "icdo:8144/3",
          "comments": []
        },
        "Gastrinoma, Malignant": {
          "meaning": "icdo:8153/3",
          "comments": []
        },
        "Somatostatinoma, Malignant": {
          "meaning": "icdo:8156/3",
          "comments": []
        },
        "Adenocarcinoma In Situ In Adenomatous Polyp": {
          "meaning": "icdo:8210/2",
          "comments": []
        },
        "Adenocarcinoma In Adenomatous Polyp": {
          "meaning": "icdo:8210/3",
          "comments": []
        },
        "Tubular Adenocarcinoma": {
          "meaning": "icdo:8211/3",
          "comments": []
        },
        "Serrated Dysplasia, High Grade": {
          "meaning": "icdo:8213/2",
          "comments": []
        },
        "Parietal Cell Carcinoma": {
          "meaning": "icdo:8214/3",
          "comments": []
        },
        "Adenocarcinoma In Situ In Familial Polyp. Coli": {
          "meaning": "icdo:8220/2",
          "comments": []
        },
        "Adenocarcinoma In Adenoma. Polyposis Coli": {
          "meaning": "icdo:8220/3",
          "comments": []
        },
        "Adenocarc. In Situ In Mult. Adenomatous Polyps": {
          "meaning": "icdo:8221/2",
          "comments": []
        },
        "Adenocarcinoma In Mult. Adenomatous Polyps": {
          "meaning": "icdo:8221/3",
          "comments": []
        },
        "Enterochromaffin Cell Carcinoid": {
          "meaning": "icdo:8241/3",
          "comments": []
        },
        "Enterochromaffin-Like Cell Tumor, Malignant": {
          "meaning": "icdo:8242/3",
          "comments": []
        },
        "Goblet Cell Carcinoid": {
          "meaning": "icdo:8243/3",
          "comments": []
        },
        "Adenocarcinoid Tumor": {
          "meaning": "icdo:8245/3",
          "comments": []
        },
        "Signet Ring Cell Carcinoma": {
          "meaning": "icdo:8490/3",
          "comments": []
        },
        "Medullary Carcinoma, Nos": {
          "meaning": "icdo:8510/3",
          "comments": []
        },
        "Medullary Carcinoma With Lymphoid Stroma": {
          "meaning": "icdo:8512/3",
          "comments": []
        },
        "Hepatoid Adenocarcinoma": {
          "meaning": "icdo:8576/3",
          "comments": []
        },
        "Carcinofibroma": {
          "meaning": "icdo:8934/3",
          "comments": []
        },
        "Stromal Sarcoma, Nos": {
          "meaning": "icdo:8935/3",
          "comments": []
        },
        "Gastrointestinal Stromal Sarcoma": {
          "meaning": "icdo:8936/3",
          "comments": []
        },
        "Multiple Myeloma": {
          "meaning": "icdo:9732/3",
          "comments": []
        },
        "Glucagonoma, Malignant": {
          "meaning": "icdo:8152/3",
          "comments": []
        },
        "Enteroglucagonoma, Malignant": {
          "meaning": "icdo:8157/3",
          "comments": []
        },
        "Pancreatobiliary-Type Carcinoma": {
          "meaning": "icdo:8163/3",
          "comments": []
        },
        "Extra-Adrenal Paraganglioma, Malignant": {
          "meaning": "icdo:8693/3",
          "comments": []
        },
        "Intestinal T-Cell Lymphoma": {
          "meaning": "icdo:9717/3",
          "comments": []
        },
        "Immunoproliferative Small Intestinal Disease": {
          "meaning": "icdo:9764/3",
          "comments": []
        },
        "Serrated Adenocarcinoma": {
          "meaning": "icdo:8213/3",
          "comments": []
        },
        "Micropapillary Carcinoma, Nos": {
          "meaning": "icdo:8265/3",
          "comments": []
        },
        "Mucinous Cystadenocarcinoma, Non-Invasive": {
          "meaning": "icdo:8470/2",
          "comments": []
        },
        "Mucinous Cystadenocarcinoma, Nos": {
          "meaning": "icdo:8470/3",
          "comments": []
        },
        "Papillary Mucinous Cystadenocarcinoma": {
          "meaning": "icdo:8471/3",
          "comments": []
        },
        "High Grade Appendiceal Mucinous Neoplasm": {
          "meaning": "icdo:8480/2",
          "comments": []
        },
        "Squamous Intraepithelial Neoplasia, Grade Iii": {
          "meaning": "icdo:8077/2",
          "comments": []
        },
        "Adenocarcinoma Of Anal Glands": {
          "meaning": "icdo:8215/3",
          "comments": []
        },
        "Intraductal Carcinoma, Noninfiltrating, Nos": {
          "meaning": "icdo:8500/2",
          "comments": []
        },
        "Noninfiltrating Intraductal Papillary Adenocarcinoma": {
          "meaning": "icdo:8503/2",
          "comments": []
        },
        "Intraductal Papillary Adenocarcinoma With Invasion": {
          "meaning": "icdo:8503/3",
          "comments": []
        },
        "Noninfiltrating Intracystic Carcinoma": {
          "meaning": "icdo:8504/2",
          "comments": []
        },
        "Intracystic Carcinoma, Nos": {
          "meaning": "icdo:8504/3",
          "comments": []
        },
        "Paget Disease, Extramammary": {
          "meaning": "icdo:8542/3",
          "comments": []
        },
        "Bile Duct Cystadenocarcinoma": {
          "meaning": "icdo:8161/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Nos": {
          "meaning": "icdo:8170/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Fibrolamellar": {
          "meaning": "icdo:8171/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Scirrhous": {
          "meaning": "icdo:8172/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Spindle Cell Variant": {
          "meaning": "icdo:8173/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Clear Cell Type": {
          "meaning": "icdo:8174/3",
          "comments": []
        },
        "Hepatocellular Carcinoma, Pleomorphic Type": {
          "meaning": "icdo:8175/3",
          "comments": []
        },
        "Comb. Hepatocel. Carcinoma & Cholangiocarcinoma": {
          "meaning": "icdo:8180/3",
          "comments": []
        },
        "Comedocarcinoma, Non-Infiltrating": {
          "meaning": "icdo:8501/2",
          "comments": []
        },
        "Comedocarcinoma, Nos": {
          "meaning": "icdo:8501/3",
          "comments": []
        },
        "Intraductal Micropapillary Carcinoma": {
          "meaning": "icdo:8507/2",
          "comments": []
        },
        "Cystic Hypersecretory Carcinoma": {
          "meaning": "icdo:8508/3",
          "comments": []
        },
        "Kupffer Cell Sarcoma": {
          "meaning": "icdo:9124/3",
          "comments": []
        },
        "Hemangioendothelioma, Malignant": {
          "meaning": "icdo:9130/3",
          "comments": []
        },
        "Epithelioid Hemangioendothelioma, Malignant": {
          "meaning": "icdo:9133/3",
          "comments": []
        },
        "Hepatosplenic Gamma-Delta Cell Lymphoma": {
          "meaning": "icdo:9716/3",
          "comments": []
        },
        "Klatskin Tumor": {
          "meaning": "icdo:8162/3",
          "comments": []
        },
        "Glandular Intraepithelial Neoplasia, Grade Iii": {
          "meaning": "icdo:8148/2",
          "comments": []
        },
        "Islet Cell Carcinoma": {
          "meaning": "icdo:8150/3",
          "comments": []
        },
        "Insulinoma, Malignant": {
          "meaning": "icdo:8151/3",
          "comments": []
        },
        "Vipoma": {
          "meaning": "icdo:8155/3",
          "comments": []
        },
        "Acth-Producing Tumor": {
          "meaning": "icdo:8158/3",
          "comments": []
        },
        "Mixed Cell Adenocarcinoma": {
          "meaning": "icdo:8323/3",
          "comments": []
        },
        "Serous Cystadenocarcinoma": {
          "meaning": "icdo:8441/3",
          "comments": []
        },
        "Papillary Cystadenocarcinoma, Nos": {
          "meaning": "icdo:8450/3",
          "comments": []
        },
        "Solid Pseudopapillary Carcinoma": {
          "meaning": "icdo:8452/3",
          "comments": []
        },
        "Intraductal Papillary-Mucinous Carcinoma, Non-Inv.": {
          "meaning": "icdo:8453/2",
          "comments": []
        },
        "Intraductal Papillary-Mucinous Carcinoma, Invasive": {
          "meaning": "icdo:8453/3",
          "comments": []
        },
        "Intraductal Oncocytic Papillary Neoplasm, Nos": {
          "meaning": "icdo:8455/2",
          "comments": []
        },
        "Intraductal Oncocytic Papillary Neoplasms With Associated Invasive": {
          "meaning": "icdo:8455/3",
          "comments": []
        },
        "Duct Carcinoma, Desmoplastic Type": {
          "meaning": "icdo:8514/3",
          "comments": []
        },
        "Infiltrating Ductular Carcinoma": {
          "meaning": "icdo:8521/3",
          "comments": []
        },
        "Mixed Acinar Ductal Carcinoma": {
          "meaning": "icdo:8552/3",
          "comments": []
        },
        "Papillary Trans. Cell Carcinoma, Non-Invasive": {
          "meaning": "icdo:8130/2",
          "comments": []
        },
        "Papillary Trans. Cell Carcinoma": {
          "meaning": "icdo:8130/3",
          "comments": []
        },
        "Transitional Cell Carcinoma, Micropapillary": {
          "meaning": "icdo:8131/3",
          "comments": []
        },
        "Alveolar Adenocarcinoma": {
          "meaning": "icdo:8251/3",
          "comments": []
        },
        "Granular Cell Carcinoma": {
          "meaning": "icdo:8320/3",
          "comments": []
        },
        "Endometrioid Carcinoma": {
          "meaning": "icdo:8380/3",
          "comments": []
        },
        "Apocrine Adenocarcinoma": {
          "meaning": "icdo:8401/3",
          "comments": []
        },
        "Fibrous Histiocytoma, Malignant": {
          "meaning": "icdo:8830/3",
          "comments": []
        },
        "Alveolar Rhabdomyosarcoma": {
          "meaning": "icdo:8920/3",
          "comments": []
        },
        "Rhabdomyosarcoma With Ganglionic Differentiation": {
          "meaning": "icdo:8921/3",
          "comments": []
        },
        "Mullerian Mixed Tumor": {
          "meaning": "icdo:8950/3",
          "comments": []
        },
        "Mesodermal Mixed Tumor": {
          "meaning": "icdo:8951/3",
          "comments": []
        },
        "Synovial Sarcoma, Nos": {
          "meaning": "icdo:9040/3",
          "comments": []
        },
        "Synovial Sarcoma, Spindle Cell": {
          "meaning": "icdo:9041/3",
          "comments": []
        },
        "Synovial Sarcoma, Epithelioid Cell": {
          "meaning": "icdo:9042/3",
          "comments": []
        },
        "Synovial Sarcoma, Biphasic": {
          "meaning": "icdo:9043/3",
          "comments": []
        },
        "Clear Cell Sarcoma, Nos (Except Of Kidney M-": {
          "meaning": "icdo:9044/3",
          "comments": []
        },
        "Germ Cell Tumor, Nonseminomatous": {
          "meaning": "icdo:9065/3",
          "comments": []
        },
        "Teratoma, Malignant, Nos": {
          "meaning": "icdo:9080/3",
          "comments": []
        },
        "Malignant Teratoma, Undiff.": {
          "meaning": "icdo:9082/3",
          "comments": []
        },
        "Malignant Teratoma, Intermediate": {
          "meaning": "icdo:9083/3",
          "comments": []
        },
        "Teratoma With Malig. Transformation": {
          "meaning": "icdo:9084/3",
          "comments": []
        },
        "Choriocarcinoma Combined W/ Other Germ Cell Elements": {
          "meaning": "icdo:9101/3",
          "comments": []
        },
        "Trophoblastic Tumor, Epithelioid": {
          "meaning": "icdo:9105/3",
          "comments": []
        },
        "Mesonephroma, Malignant": {
          "meaning": "icdo:9110/3",
          "comments": []
        },
        "Hemangiopericytoma, Malignant": {
          "meaning": "icdo:9150/3",
          "comments": []
        },
        "Malignant Giant Cell Tumor Of Soft Parts": {
          "meaning": "icdo:9251/3",
          "comments": []
        },
        "Malignant Tenosynovial Giant Cell Tumor": {
          "meaning": "icdo:9252/3",
          "comments": []
        },
        "Neuroblastoma, Nos": {
          "meaning": "icdo:9500/3",
          "comments": []
        },
        "Medulloepithelioma, Nos": {
          "meaning": "icdo:9501/3",
          "comments": []
        },
        "Teratoid Medulloepithelioma": {
          "meaning": "icdo:9502/3",
          "comments": []
        },
        "Neuroepithelioma, Nos": {
          "meaning": "icdo:9503/3",
          "comments": []
        },
        "Ganglioglioma, Anaplastic": {
          "meaning": "icdo:9505/3",
          "comments": []
        },
        "Neurilemmoma, Malignant": {
          "meaning": "icdo:9560/3",
          "comments": []
        },
        "MpnsT With Rhabdomyoblastic Differentiation": {
          "meaning": "icdo:9561/3",
          "comments": []
        },
        "Perineurioma, Malignant": {
          "meaning": "icdo:9571/3",
          "comments": []
        },
        "Nut Carcinoma": {
          "meaning": "icdo:8023/3",
          "comments": []
        },
        "Biphenotypic Sinonasal Sarcoma": {
          "meaning": "icdo:9045/3",
          "comments": []
        },
        "Chondrosarcoma, Nos": {
          "meaning": "icdo:9220/3",
          "comments": []
        },
        "Juxtacortical Chondrosarcoma": {
          "meaning": "icdo:9221/3",
          "comments": []
        },
        "Olfactory Neurogenic Tumor": {
          "meaning": "icdo:9520/3",
          "comments": []
        },
        "Olfactory Neurcytoma": {
          "meaning": "icdo:9521/3",
          "comments": []
        },
        "Olfactory Neuroblastoma": {
          "meaning": "icdo:9522/3",
          "comments": []
        },
        "Olfactory Neuroepithelioma": {
          "meaning": "icdo:9523/3",
          "comments": []
        },
        "Non-Small Cell Carcinoma": {
          "meaning": "icdo:8046/3",
          "comments": []
        },
        "Oat Cell Carcinoma": {
          "meaning": "icdo:8042/3",
          "comments": []
        },
        "Small Cell Carcinoma, Intermediate Cell": {
          "meaning": "icdo:8044/3",
          "comments": []
        },
        "Lepidic Adenocarcinoma": {
          "meaning": "icdo:8250/3",
          "comments": []
        },
        "Bronchiolo-Alveolar Carcinoma, Non-Mucinous": {
          "meaning": "icdo:8252/3",
          "comments": []
        },
        "Invasive Mucinous Adenocarcinoma": {
          "meaning": "icdo:8253/3",
          "comments": []
        },
        "Mixed Invasive Mucinous And Non-Mucinous Adenocarcinoma": {
          "meaning": "icdo:8254/3",
          "comments": []
        },
        "Pulmonary Blastoma": {
          "meaning": "icdo:8972/3",
          "comments": []
        },
        "Pleuropulmonary Blastoma": {
          "meaning": "icdo:8973/3",
          "comments": []
        },
        "Adenocarcinoma In Situ, Non-Mucinous": {
          "meaning": "icdo:8250/2",
          "comments": []
        },
        "Adenocarcinoma In Situ, Mucinous": {
          "meaning": "icdo:8253/2",
          "comments": []
        },
        "Minimally Invasive Adenocarcinoma, Non-Mucinous": {
          "meaning": "icdo:8256/3",
          "comments": []
        },
        "Minimally Invasive Adenocarcinoma, Mucinous": {
          "meaning": "icdo:8257/3",
          "comments": []
        },
        "Fetal Adenocarcinoma": {
          "meaning": "icdo:8333/3",
          "comments": []
        },
        "Pecoma, Malignant": {
          "meaning": "icdo:8714/3",
          "comments": []
        },
        "Pulmonary Myxoid Sarcoma With Ewsr1-Creb1 Translocation": {
          "meaning": "icdo:8842/3",
          "comments": []
        },
        "Mesothelioma, In Situ": {
          "meaning": "icdo:9050/2",
          "comments": []
        },
        "Mesothelioma, Malignant": {
          "meaning": "icdo:9050/3",
          "comments": []
        },
        "Fibrous Mesothelioma, Malignant": {
          "meaning": "icdo:9051/3",
          "comments": []
        },
        "Epithel. Mesothelioma, Mal.": {
          "meaning": "icdo:9052/3",
          "comments": []
        },
        "Mesothelioma, Biphasic, Malignant": {
          "meaning": "icdo:9053/3",
          "comments": []
        },
        "Primary Effusion Lymphoma": {
          "meaning": "icdo:9678/3",
          "comments": []
        },
        "Mediastinal Large B-Cell Lymphoma": {
          "meaning": "icdo:9679/3",
          "comments": []
        },
        "Thymoma, Malignant, Nos": {
          "meaning": "icdo:8580/3",
          "comments": []
        },
        "Thymoma, Type A, Malignant": {
          "meaning": "icdo:8581/3",
          "comments": []
        },
        "Thymoma, Type Ab, Malignant": {
          "meaning": "icdo:8582/3",
          "comments": []
        },
        "Thymoma, Type B1, Malignant": {
          "meaning": "icdo:8583/3",
          "comments": []
        },
        "Thymoma, Type B2, Malignant": {
          "meaning": "icdo:8584/3",
          "comments": []
        },
        "Thymoma, Type B3, Malignant": {
          "meaning": "icdo:8585/3",
          "comments": []
        },
        "Thymic Carcinoma, Nos": {
          "meaning": "icdo:8586/3",
          "comments": []
        },
        "Spindle Epithelial Tumor With Thymus-Like Element": {
          "meaning": "icdo:8588/3",
          "comments": []
        },
        "Carcinoma Showing Thymus-Like Element": {
          "meaning": "icdo:8589/3",
          "comments": []
        },
        "Germ Cell Tumors With Associated Hematological Malignancy": {
          "meaning": "icdo:9086/3",
          "comments": []
        },
        "Splenic Marginal Zone B-Cell Lymphoma": {
          "meaning": "icdo:9689/3",
          "comments": []
        },
        "Mycosis Fungoides": {
          "meaning": "icdo:9700/3",
          "comments": []
        },
        "Subcutaneous Panniculitis-Like T-Cell Lymphoma": {
          "meaning": "icdo:9708/3",
          "comments": []
        },
        "Cutaneous T-Cell Lymphoma, Nos": {
          "meaning": "icdo:9709/3",
          "comments": []
        },
        "Primary Cutan. Cd30+ T-Cell Lymphoprolif. Disorder": {
          "meaning": "icdo:9718/3",
          "comments": []
        },
        "Paraganglioma, Malignant": {
          "meaning": "icdo:8680/3",
          "comments": []
        },
        "Myxoid Pleomorphic Liposarcoma": {
          "meaning": "icdo:8859/3",
          "comments": []
        },
        "Seminoma, Nos": {
          "meaning": "icdo:9061/3",
          "comments": []
        },
        "Seminoma, Anaplastic": {
          "meaning": "icdo:9062/3",
          "comments": []
        },
        "Spermatocytic Seminoma": {
          "meaning": "icdo:9063/3",
          "comments": []
        },
        "Peripheral Neuroectodermal Tumor": {
          "meaning": "icdo:9364/3",
          "comments": []
        },
        "Askin Tumor": {
          "meaning": "icdo:9365/3",
          "comments": []
        },
        "Periosteal Fibrosarcoma": {
          "meaning": "icdo:8812/3",
          "comments": []
        },
        "Osteosarcoma, Nos": {
          "meaning": "icdo:9180/3",
          "comments": []
        },
        "Telangiectatic Osteosarcoma": {
          "meaning": "icdo:9183/3",
          "comments": []
        },
        "Osteosarcoma In Paget Disease": {
          "meaning": "icdo:9184/3",
          "comments": []
        },
        "Small Cell Osteosarcoma": {
          "meaning": "icdo:9185/3",
          "comments": []
        },
        "Central Osteosarcoma": {
          "meaning": "icdo:9186/3",
          "comments": []
        },
        "Instrosseous Well Differentiated Osteosarcoma": {
          "meaning": "icdo:9187/3",
          "comments": []
        },
        "High Grade Surface Osteosarcoma": {
          "meaning": "icdo:9194/3",
          "comments": []
        },
        "Intracortical Osteosarcoma": {
          "meaning": "icdo:9195/3",
          "comments": []
        },
        "Chondroblastoma, Malignant": {
          "meaning": "icdo:9230/3",
          "comments": []
        },
        "Myxoid Chondrosarcoma": {
          "meaning": "icdo:9231/3",
          "comments": []
        },
        "Clear Cell Chondrosarcoma": {
          "meaning": "icdo:9242/3",
          "comments": []
        },
        "Dedifferentiated Chondrosarcoma": {
          "meaning": "icdo:9243/3",
          "comments": []
        },
        "Giant Cell Tumor Of Bone, Malignant": {
          "meaning": "icdo:9250/3",
          "comments": []
        },
        "Adamantinoma Of Long Bones": {
          "meaning": "icdo:9261/3",
          "comments": []
        },
        "Odontogenic Tumor, Malignant": {
          "meaning": "icdo:9270/3",
          "comments": []
        },
        "Ameloblastic Odontosarcoma": {
          "meaning": "icdo:9290/3",
          "comments": []
        },
        "Ameloblastoma, Malignant": {
          "meaning": "icdo:9310/3",
          "comments": []
        },
        "Ameloblastic Fibrosarcoma": {
          "meaning": "icdo:9330/3",
          "comments": []
        },
        "Odontogenic Carcinosarcoma": {
          "meaning": "icdo:9342/3",
          "comments": []
        },
        "Ghost Cell Odontogenic Carcinoma": {
          "meaning": "icdo:9302/3",
          "comments": []
        },
        "Clear Cell Odontogenic Carcinoma": {
          "meaning": "icdo:9341/3",
          "comments": []
        },
        "Round Cell Sarcoma With Ewsr1-Non-Ets Fusions": {
          "meaning": "icdo:9366/3",
          "comments": []
        },
        "Cic-Rearranged Sarcoma": {
          "meaning": "icdo:9367/3",
          "comments": []
        },
        "Sarcoma With Bcor Genetic Alterations": {
          "meaning": "icdo:9368/3",
          "comments": []
        },
        "Plasma Cell Leukemia": {
          "meaning": "icdo:9733/3",
          "comments": []
        },
        "Mast Cell Leukemia": {
          "meaning": "icdo:9742/3",
          "comments": []
        },
        "Immunoproliferative Disease, Nos": {
          "meaning": "icdo:9760/3",
          "comments": []
        },
        "Waldenstrom Macroglobulinemia": {
          "meaning": "icdo:9761/3",
          "comments": []
        },
        "Heavy Chain Disease, Nos": {
          "meaning": "icdo:9762/3",
          "comments": []
        },
        "Leukemia, Nos": {
          "meaning": "icdo:9800/3",
          "comments": []
        },
        "Acute Leukemia, Nos": {
          "meaning": "icdo:9801/3",
          "comments": []
        },
        "Acute Biphenotypic Leukemia": {
          "meaning": "icdo:9805/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia With T(9;22)(Q34;Q11.2);Bcr-Abl1": {
          "meaning": "icdo:9806/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia With T(V;11Q23);Mll Rearranged": {
          "meaning": "icdo:9807/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia, B/Myeloid, Nos": {
          "meaning": "icdo:9808/3",
          "comments": []
        },
        "Mixed Phenotype Acute Leukemia, T/Myeloid, Nos": {
          "meaning": "icdo:9809/3",
          "comments": []
        },
        "Lymphoid Leukemia, Nos": {
          "meaning": "icdo:9820/3",
          "comments": []
        },
        "Burkitt Cell Leukemia": {
          "meaning": "icdo:9826/3",
          "comments": []
        },
        "Adult T-Cell Leukemia/Lymphoma (Htlv-1 Pos.)": {
          "meaning": "icdo:9827/3",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia, L2 Type, Nos": {
          "meaning": "icdo:9828/3",
          "comments": []
        },
        "Prolymphocytic Leukemia, Nos": {
          "meaning": "icdo:9832/3",
          "comments": []
        },
        "Prolymphocytic Leukemia, B-Cell Type": {
          "meaning": "icdo:9833/3",
          "comments": []
        },
        "Prolymphocytic Leukemia, T-Cell Type": {
          "meaning": "icdo:9834/3",
          "comments": []
        },
        "Precursor Cell Lymphoblastic Leukemia, Nos": {
          "meaning": "icdo:9835/3",
          "comments": []
        },
        "Precursor B-Cell Lymphoblastic Leukemia": {
          "meaning": "icdo:9836/3",
          "comments": []
        },
        "Acute Myeloid Leukemia, M6 Type": {
          "meaning": "icdo:9840/3",
          "comments": []
        },
        "Myeloid Leukemia, Nos": {
          "meaning": "icdo:9860/3",
          "comments": []
        },
        "Chronic Myeloid Leukemia, Nos": {
          "meaning": "icdo:9863/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With T(6;9)(P23;Q34) Dek-Nup214": {
          "meaning": "icdo:9865/3",
          "comments": []
        },
        "Acute Promyelocytic Leuk.,T(15;17)(Q22;Q11-12)": {
          "meaning": "icdo:9866/3",
          "comments": []
        },
        "Acute Myelomonocytic Leukemia": {
          "meaning": "icdo:9867/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Inv(3)(Q21Q26.2) Or": {
          "meaning": "icdo:9869/3",
          "comments": []
        },
        "Acute Basophilic Leukemia": {
          "meaning": "icdo:9870/3",
          "comments": []
        },
        "Ac. Myelomonocytic Leuk. W Abn. Mar. Eosinophils": {
          "meaning": "icdo:9871/3",
          "comments": []
        },
        "Acute Myeloid Leukemia, Minimal Differentiation": {
          "meaning": "icdo:9872/3",
          "comments": []
        },
        "Acute Myeloid Leukemia Without Maturation": {
          "meaning": "icdo:9873/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Maturation": {
          "meaning": "icdo:9874/3",
          "comments": []
        },
        "Chronic Myelogenous Leukemia, Bcr/Abl Positive": {
          "meaning": "icdo:9875/3",
          "comments": []
        },
        "Atypical Chronic Myeloid Leuk., Bcr/Abl Negative": {
          "meaning": "icdo:9876/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Mutated Npm1": {
          "meaning": "icdo:9877/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Biallelic Mutations Of Cebpa": {
          "meaning": "icdo:9878/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Mutated Runx1": {
          "meaning": "icdo:9879/3",
          "comments": []
        },
        "Acute Monocytic Leukemia": {
          "meaning": "icdo:9891/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Multilineage Dysplasia": {
          "meaning": "icdo:9895/3",
          "comments": []
        },
        "Acute Myeloid Leukemia, T(8;21)(Q22;Q22)": {
          "meaning": "icdo:9896/3",
          "comments": []
        },
        "Acute Myeloid Leukemia, 11Q23 Abnormalities": {
          "meaning": "icdo:9897/3",
          "comments": []
        },
        "Myeloid Leukemia Associated With Down Syndrome": {
          "meaning": "icdo:9898/3",
          "comments": []
        },
        "Acute Megakaryoblastic Leukemia": {
          "meaning": "icdo:9910/3",
          "comments": []
        },
        "Acute Myeloid Leukemia (Megakaryoblastic) With": {
          "meaning": "icdo:9911/3",
          "comments": []
        },
        "Acute Myeloid Leukemia With Bcr-Abl1": {
          "meaning": "icdo:9912/3",
          "comments": []
        },
        "Therapy-Related Acute Myeloid Leukemia, Nos": {
          "meaning": "icdo:9920/3",
          "comments": []
        },
        "Myeloid Sarcoma": {
          "meaning": "icdo:9930/3",
          "comments": []
        },
        "Acute Panmyelosis With Myelofibrosis": {
          "meaning": "icdo:9931/3",
          "comments": []
        },
        "Hairy Cell Leukemia": {
          "meaning": "icdo:9940/3",
          "comments": []
        },
        "Chronic Myelomonocytic Leukemia, Nos": {
          "meaning": "icdo:9945/3",
          "comments": []
        },
        "Juvenile Myelomonocytic Leukemia": {
          "meaning": "icdo:9946/3",
          "comments": []
        },
        "Aggressive Nk-Cell Leukemia": {
          "meaning": "icdo:9948/3",
          "comments": []
        },
        "Polycythemia Vera": {
          "meaning": "icdo:9950/3",
          "comments": []
        },
        "Chronic Myeloproliferative Disease, Nos": {
          "meaning": "icdo:9960/3",
          "comments": []
        },
        "Myelosclerosis With Myeloid Metaplasia": {
          "meaning": "icdo:9961/3",
          "comments": []
        },
        "Essential Thrombocythemia": {
          "meaning": "icdo:9962/3",
          "comments": []
        },
        "Chronic Neutrophilic Leukemia": {
          "meaning": "icdo:9963/3",
          "comments": []
        },
        "Hypereosinophilic Syndrome": {
          "meaning": "icdo:9964/3",
          "comments": []
        },
        "Refractory Anemia": {
          "meaning": "icdo:9980/3",
          "comments": []
        },
        "Refractory Anemia With Sideroblasts": {
          "meaning": "icdo:9982/3",
          "comments": []
        },
        "Refractory Anemia With Excess Blasts": {
          "meaning": "icdo:9983/3",
          "comments": []
        },
        "Refract. Anemia With Excess Blasts In Transformation": {
          "meaning": "icdo:9984/3",
          "comments": []
        },
        "Refractory Cytopenia With Multilineage Dysplasia": {
          "meaning": "icdo:9985/3",
          "comments": []
        },
        "Myelodysplastic Syndr. With 5Q Deletion Syndrome": {
          "meaning": "icdo:9986/3",
          "comments": []
        },
        "Therapy-Related Myelodysplastic Syndrome, Nos": {
          "meaning": "icdo:9987/3",
          "comments": []
        },
        "Myelodysplastic Syndrome, Nos": {
          "meaning": "icdo:9989/3",
          "comments": []
        },
        "Refractory Neutropenia": {
          "meaning": "icdo:9991/3",
          "comments": []
        },
        "Refractory Thrombocytopenia": {
          "meaning": "icdo:9992/3",
          "comments": []
        },
        "Myelodysplastic Syndrome With Ring Sideroblasts And Multilineage": {
          "meaning": "icdo:9993/3",
          "comments": []
        },
        "Trichilemmocarcinoma": {
          "meaning": "icdo:8102/3",
          "comments": []
        },
        "Pilomatrix Carcinoma": {
          "meaning": "icdo:8110/3",
          "comments": []
        },
        "Merkel Cell Carcinoma": {
          "meaning": "icdo:8247/3",
          "comments": []
        },
        "Skin Appendage Carcinoma": {
          "meaning": "icdo:8390/3",
          "comments": []
        },
        "Sweat Gland Adenocarcinoma": {
          "meaning": "icdo:8400/3",
          "comments": []
        },
        "Nodular Hidradenoma, Malignant": {
          "meaning": "icdo:8402/3",
          "comments": []
        },
        "Malignant Eccrine Spiradenoma": {
          "meaning": "icdo:8403/3",
          "comments": []
        },
        "Sclerosing Sweat Duct Carcinoma": {
          "meaning": "icdo:8407/3",
          "comments": []
        },
        "Eccrine Papillary Adenocarcinoma": {
          "meaning": "icdo:8408/3",
          "comments": []
        },
        "Eccrine Poroma, Malignant": {
          "meaning": "icdo:8409/3",
          "comments": []
        },
        "Sebaceous Adenocarcinoma": {
          "meaning": "icdo:8410/3",
          "comments": []
        },
        "Eccrine Adenocarcinoma": {
          "meaning": "icdo:8413/3",
          "comments": []
        },
        "Ceruminous Adenocarcinoma": {
          "meaning": "icdo:8420/3",
          "comments": []
        },
        "Mal. Melanoma In Junctional Nevus": {
          "meaning": "icdo:8740/3",
          "comments": []
        },
        "Precancerous Melanosis, NOS": {
          "meaning": "icdo:8741/2",
          "comments": []
        },
        "Mal. Melanoma In Precan. Melanosis": {
          "meaning": "icdo:8741/3",
          "comments": []
        },
        "Lentigo Maligna": {
          "meaning": "icdo:8742/2",
          "comments": []
        },
        "Lentigo Maligna Melanoma": {
          "meaning": "icdo:8742/3",
          "comments": []
        },
        "Superficial Spreading Melanoma, In Situ": {
          "meaning": "icdo:8743/2",
          "comments": []
        },
        "Acral Lentiginous Melanoma, Malig.": {
          "meaning": "icdo:8744/3",
          "comments": []
        },
        "Blue Nevus, Malignant": {
          "meaning": "icdo:8780/3",
          "comments": []
        },
        "Dermatofibrosarcoma, Nos": {
          "meaning": "icdo:8832/3",
          "comments": []
        },
        "Pigmented Dermatofibrosarcoma Protuberans": {
          "meaning": "icdo:8833/3",
          "comments": []
        },
        "Primary Cutaneous Follicle Centre Lymphoma": {
          "meaning": "icdo:9597/3",
          "comments": []
        },
        "Hydroa Vacciniforme-Like Lymphoma": {
          "meaning": "icdo:9725/3",
          "comments": []
        },
        "Primary Cutaneous Gamma-Delta T-Cell Lymphoma": {
          "meaning": "icdo:9726/3",
          "comments": []
        },
        "Granular Cell Tumor, Malignant": {
          "meaning": "icdo:9580/3",
          "comments": []
        },
        "Alveolar Soft Part Sarcoma": {
          "meaning": "icdo:9581/3",
          "comments": []
        },
        "Low-Grade Serous Carcinoma": {
          "meaning": "icdo:8460/3",
          "comments": []
        },
        "High-Grade Serous Carcinoma": {
          "meaning": "icdo:8461/3",
          "comments": []
        },
        "Endometrial Stromal Sarcoma": {
          "meaning": "icdo:8930/3",
          "comments": []
        },
        "Endometrial Stromal Sarcoma, Low Grade": {
          "meaning": "icdo:8931/3",
          "comments": []
        },
        "Myeloid And Lymphoid Neoplasms With Pdgfrb Re Arrangement": {
          "meaning": "icdo:9966/3",
          "comments": []
        },
        "Myeloid/Lymphoid Neoplasm With Pcm1-Jak2": {
          "meaning": "icdo:9968/3",
          "comments": []
        },
        "Lipid-Rich Carcinoma": {
          "meaning": "icdo:8314/3",
          "comments": []
        },
        "Glycogen-Rich Carcinoma": {
          "meaning": "icdo:8315/3",
          "comments": []
        },
        "Invasive Micropapillary Carcinoma": {
          "meaning": "icdo:8507/3",
          "comments": []
        },
        "Solid Papillary Carcinoma In Situ": {
          "meaning": "icdo:8509/2",
          "comments": []
        },
        "Solid Papillary Carcinoma With Invasion": {
          "meaning": "icdo:8509/3",
          "comments": []
        },
        "Atypical Medullary Carcinoma": {
          "meaning": "icdo:8513/3",
          "comments": []
        },
        "Pleomorphic Lobular Carcinoma In Situ": {
          "meaning": "icdo:8519/2",
          "comments": []
        },
        "Lobular Carcinoma In Situ": {
          "meaning": "icdo:8520/2",
          "comments": []
        },
        "Lobular Carcinoma, Nos": {
          "meaning": "icdo:8520/3",
          "comments": []
        },
        "Intraductal And Lobular In Situ Carcinoma": {
          "meaning": "icdo:8522/2",
          "comments": []
        },
        "Infiltrating Duct And Lobular Carcinoma": {
          "meaning": "icdo:8522/3",
          "comments": []
        },
        "Infiltr. Duct Mixed With Other Types Of Carcinoma, In Situ": {
          "meaning": "icdo:8523/2",
          "comments": []
        },
        "Infiltr. Duct Mixed With Other Types Of Carcinoma": {
          "meaning": "icdo:8523/3",
          "comments": []
        },
        "Infiltrating Lobular Mixed With Other Types Of Carc.": {
          "meaning": "icdo:8524/3",
          "comments": []
        },
        "Inflammatory Carcinoma": {
          "meaning": "icdo:8530/3",
          "comments": []
        },
        "Paget Disease, Mammary": {
          "meaning": "icdo:8540/3",
          "comments": []
        },
        "Paget Dis. & Infil. Duct Carcinoma": {
          "meaning": "icdo:8541/3",
          "comments": []
        },
        "Paget Disease And Intraductal Ca.": {
          "meaning": "icdo:8543/3",
          "comments": []
        },
        "Adenomyoepithelioma With Carcinoma": {
          "meaning": "icdo:8983/3",
          "comments": []
        },
        "Phyllodes Tumor, Malignant": {
          "meaning": "icdo:9020/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Keratinizing, Nos, In Situ": {
          "meaning": "icdo:8071/2",
          "comments": []
        },
        "Basal Cell Carcinoma, Nos": {
          "meaning": "icdo:8090/3",
          "comments": []
        },
        "Multifocal Superficial Basal Cell Carcinoma": {
          "meaning": "icdo:8091/3",
          "comments": []
        },
        "Infiltrating Basal Cell Carcinoma, Nos": {
          "meaning": "icdo:8092/3",
          "comments": []
        },
        "Basal Cell Carcinoma, Fibroepithelial": {
          "meaning": "icdo:8093/3",
          "comments": []
        },
        "Basosquamous Carcinoma": {
          "meaning": "icdo:8094/3",
          "comments": []
        },
        "Metatypical Carcinoma": {
          "meaning": "icdo:8095/3",
          "comments": []
        },
        "Basal Cell Carcinoma, Nodular": {
          "meaning": "icdo:8097/3",
          "comments": []
        },
        "Adenoid Basal Cell Carcinoma": {
          "meaning": "icdo:8098/3",
          "comments": []
        },
        "Mucinous Adenocarcinoma, Endocervical Type": {
          "meaning": "icdo:8482/3",
          "comments": []
        },
        "Adenocarcinoma, Hpv-Associated": {
          "meaning": "icdo:8483/3",
          "comments": []
        },
        "Phyllodes Tumor, Malignant (9092/3)": {
          "meaning": "icdo:9092/3",
          "comments": []
        },
        "Sq. Cell Carcinoma, Lg. Cell, Non-Ker., In Situ": {
          "meaning": "icdo:8072/2",
          "comments": []
        },
        "Adenocarcinoma, Endocervical Type": {
          "meaning": "icdo:8384/3",
          "comments": []
        },
        "Adenocarcinoma, Hpv-Independent, Nos": {
          "meaning": "icdo:8484/3",
          "comments": []
        },
        "Endometrioid Intraepithelial Neoplasia": {
          "meaning": "icdo:8380/2",
          "comments": []
        },
        "Endometrioid Adenofibroma, Malignant": {
          "meaning": "icdo:8381/3",
          "comments": []
        },
        "Endometrioid Adenocarcinoma, Secretory Variant": {
          "meaning": "icdo:8382/3",
          "comments": []
        },
        "Endometrioid Adenocarcinoma, Ciliated Cell Variant": {
          "meaning": "icdo:8383/3",
          "comments": []
        },
        "Serous Tubal Intraepithelial Carcinoma": {
          "meaning": "icdo:8441/2",
          "comments": []
        },
        "Mesonephric-Like Adenocarcinoma": {
          "meaning": "icdo:9111/3",
          "comments": []
        },
        "Clear Cell Adenocarcinofibroma": {
          "meaning": "icdo:8313/3",
          "comments": []
        },
        "Serous Cystadenoma, Borderline Malignancy (C56.9)": {
          "meaning": "icdo:8442/1",
          "comments": []
        },
        "Papillary Cystadenoma, Borderline Malignancy (C56.9)": {
          "meaning": "icdo:8451/1",
          "comments": []
        },
        "Non-Invasive Low Grade Serous Carcinoma": {
          "meaning": "icdo:8460/2",
          "comments": []
        },
        "Serous Papillary Cystic Tumor Of Borderline Malignancy (C56.9)": {
          "meaning": "icdo:8462/1",
          "comments": []
        },
        "Mucinous Cystic Tumor Of Borderline Malignancy (C56.9)": {
          "meaning": "icdo:8472/1",
          "comments": []
        },
        "Papillary Mucinous Cystadenoma, Borderline Malignancy (C56.9)": {
          "meaning": "icdo:8473/1",
          "comments": []
        },
        "Seromucinous Carcinoma": {
          "meaning": "icdo:8474/3",
          "comments": []
        },
        "Ovarian Stromal Tumor, Mal.": {
          "meaning": "icdo:8590/3",
          "comments": []
        },
        "Thecoma, Malignant": {
          "meaning": "icdo:8600/3",
          "comments": []
        },
        "Granulosa Cell Tumor, Malignant": {
          "meaning": "icdo:8620/3",
          "comments": []
        },
        "Granulosa Cell-Theca Cell Tumor, Mal.": {
          "meaning": "icdo:8621/3",
          "comments": []
        },
        "Androblastoma, Malignant": {
          "meaning": "icdo:8630/3",
          "comments": []
        },
        "Sertoli-Leydig Cell Tumor, Poorly Differentiated": {
          "meaning": "icdo:8631/3",
          "comments": []
        },
        "Gynandroblastoma, Malignant": {
          "meaning": "icdo:8632/3",
          "comments": []
        },
        "Sertoli-Leydig Cl Tum., P.D. W Heterologous Elements": {
          "meaning": "icdo:8634/3",
          "comments": []
        },
        "Steroid Cell Tumor, Malignant": {
          "meaning": "icdo:8670/3",
          "comments": []
        },
        "Brenner Tumor, Malignant": {
          "meaning": "icdo:9000/3",
          "comments": []
        },
        "Serous Adenocarcinofibroma": {
          "meaning": "icdo:9014/3",
          "comments": []
        },
        "Mucinous Adenocarcinofibroma": {
          "meaning": "icdo:9015/3",
          "comments": []
        },
        "Struma Ovarii, Malignant": {
          "meaning": "icdo:9090/3",
          "comments": []
        },
        "Malignant Placental Site Trophoblastic Tumor": {
          "meaning": "icdo:9104/3",
          "comments": []
        },
        "Warty Carcinoma": {
          "meaning": "icdo:8054/3",
          "comments": []
        },
        "Queyrat Erythroplasia": {
          "meaning": "icdo:8080/2",
          "comments": []
        },
        "Sertoli Cell Carcinoma": {
          "meaning": "icdo:8640/3",
          "comments": []
        },
        "Leydig Cell Tumor, Malignant": {
          "meaning": "icdo:8650/3",
          "comments": []
        },
        "Intratubular Malignant Germ Cells": {
          "meaning": "icdo:9064/2",
          "comments": []
        },
        "Malignant Teratoma, Trophoblastic": {
          "meaning": "icdo:9102/3",
          "comments": []
        },
        "Hereditary Leiomyomatosis And Rcc-Associated Renal Cell Carcinoma": {
          "meaning": "icdo:8311/3",
          "comments": []
        },
        "Renal Cell Carcinoma": {
          "meaning": "icdo:8312/3",
          "comments": []
        },
        "Cyst-Associated Renal Cell Carcinoma": {
          "meaning": "icdo:8316/3",
          "comments": []
        },
        "Renal Cell Carcinoma, Chromophobe Type": {
          "meaning": "icdo:8317/3",
          "comments": []
        },
        "Renal Cell Carcinoma, Sarcomatoid": {
          "meaning": "icdo:8318/3",
          "comments": []
        },
        "Collecting Duct Carcinoma": {
          "meaning": "icdo:8319/3",
          "comments": []
        },
        "Malignant Cystic Nephroma": {
          "meaning": "icdo:8959/3",
          "comments": []
        },
        "Nephroblastoma, Nos": {
          "meaning": "icdo:8960/3",
          "comments": []
        },
        "Malignant Rhabdoid Tumor": {
          "meaning": "icdo:8963/3",
          "comments": []
        },
        "Clear Cell Sarcoma Of Kidney": {
          "meaning": "icdo:8964/3",
          "comments": []
        },
        "Spindle Cell Melanoma, Type A": {
          "meaning": "icdo:8773/3",
          "comments": []
        },
        "Spindle Cell Melanoma, Type B": {
          "meaning": "icdo:8774/3",
          "comments": []
        },
        "Retinoblastoma, Nos": {
          "meaning": "icdo:9510/3",
          "comments": []
        },
        "Retinoblastoma, Differentiated": {
          "meaning": "icdo:9511/3",
          "comments": []
        },
        "Retinoblastoma, Undifferentiated": {
          "meaning": "icdo:9512/3",
          "comments": []
        },
        "Retinoblastoma, Diffuse": {
          "meaning": "icdo:9513/3",
          "comments": []
        },
        "Neoplasm, Benign": {
          "meaning": "icdo:8000/0",
          "comments": []
        },
        "Neoplasm, Uncertain Whether Benign Or Malignant": {
          "meaning": "icdo:8000/1",
          "comments": []
        },
        "Tumor Cells, Benign": {
          "meaning": "icdo:8001/0",
          "comments": []
        },
        "Tumor Cells, Uncertain Whether Benign Or Malignant": {
          "meaning": "icdo:8001/1",
          "comments": []
        },
        "Diffuse Melanocytosis": {
          "meaning": "icdo:8728/0",
          "comments": []
        },
        "Meningeal Melanocytoma": {
          "meaning": "icdo:8728/1",
          "comments": []
        },
        "Meningeal Melanomatosis": {
          "meaning": "icdo:8728/3",
          "comments": []
        },
        "Soft Tissue Tumor, Benign": {
          "meaning": "icdo:8800/0",
          "comments": []
        },
        "Fibroma, Nos": {
          "meaning": "icdo:8810/0",
          "comments": []
        },
        "Lipoma, Nos": {
          "meaning": "icdo:8850/0",
          "comments": []
        },
        "Angiolipoma, Nos": {
          "meaning": "icdo:8861/0",
          "comments": []
        },
        "Teratoma, Benign": {
          "meaning": "icdo:9080/0",
          "comments": []
        },
        "Teratoma, NOS": {
          "meaning": "icdo:9080/1",
          "comments": []
        },
        "Dermoid Cyst, NOS": {
          "meaning": "icdo:9084/0",
          "comments": []
        },
        "Cavernous Hemangioma": {
          "meaning": "icdo:9121/0",
          "comments": []
        },
        "Hemangiopericytoma, Benign": {
          "meaning": "icdo:9150/0",
          "comments": []
        },
        "Meningiomatosis, NOS": {
          "meaning": "icdo:9530/1",
          "comments": []
        },
        "Meningioma, Malignant": {
          "meaning": "icdo:9530/3",
          "comments": []
        },
        "Meningothelial Meningioma": {
          "meaning": "icdo:9531/0",
          "comments": []
        },
        "Fibrous Meningioma": {
          "meaning": "icdo:9532/0",
          "comments": []
        },
        "Psammomatous Meningioma": {
          "meaning": "icdo:9533/0",
          "comments": []
        },
        "Angiomatous Meningioma": {
          "meaning": "icdo:9534/0",
          "comments": []
        },
        "Transitional Meningioma": {
          "meaning": "icdo:9537/0",
          "comments": []
        },
        "Clear Cell Meningioma": {
          "meaning": "icdo:9538/1",
          "comments": []
        },
        "Papillary Meningioma": {
          "meaning": "icdo:9538/3",
          "comments": []
        },
        "Atypical Meningioma": {
          "meaning": "icdo:9539/1",
          "comments": []
        },
        "Meningeal Sarcomatosis": {
          "meaning": "icdo:9539/3",
          "comments": []
        },
        "Paraganglioma, Nos": {
          "meaning": "icdo:8680/1",
          "comments": []
        },
        "Solitary Fibrous Tumor/Hemangiopericytoma Grade 2": {
          "meaning": "icdo:8815/1",
          "comments": []
        },
        "Venous Hemangioma": {
          "meaning": "icdo:9122/0",
          "comments": []
        },
        "Capillary Hemangioma": {
          "meaning": "icdo:9131/0",
          "comments": []
        },
        "Glioma, Malignant": {
          "meaning": "icdo:9380/3",
          "comments": []
        },
        "Gliomatosis Cerebri": {
          "meaning": "icdo:9381/3",
          "comments": []
        },
        "Mixed Glioma": {
          "meaning": "icdo:9382/3",
          "comments": []
        },
        "Supependymal Giant Cell Astrocytoma": {
          "meaning": "icdo:9384/1",
          "comments": []
        },
        "Diffuse Midline Glioma, H3 K27M-Mutant": {
          "meaning": "icdo:9385/3",
          "comments": []
        },
        "Sellar Ependymoma": {
          "meaning": "icdo:9391/1",
          "comments": []
        },
        "Ependymoma, NOS": {
          "meaning": "icdo:9391/3",
          "comments": []
        },
        "Ependymoma, Anaplastic": {
          "meaning": "icdo:9392/3",
          "comments": []
        },
        "Papillary Ependymoma": {
          "meaning": "icdo:9393/3",
          "comments": []
        },
        "Ependymoma, Rela Fusion-Positive": {
          "meaning": "icdo:9396/3",
          "comments": []
        },
        "Astrocytoma, Anaplastic": {
          "meaning": "icdo:9401/3",
          "comments": []
        },
        "Protoplasmic Astrocytoma": {
          "meaning": "icdo:9410/3",
          "comments": []
        },
        "Gemistocytic Astrocytoma": {
          "meaning": "icdo:9411/3",
          "comments": []
        },
        "Desmoplastic Infantile Astrocytoma": {
          "meaning": "icdo:9412/1",
          "comments": []
        },
        "Fibrillary Astrocytoma": {
          "meaning": "icdo:9420/3",
          "comments": []
        },
        "Polar Spongioblastoma": {
          "meaning": "icdo:9423/3",
          "comments": []
        },
        "Glioblastoma, Nos": {
          "meaning": "icdo:9440/3",
          "comments": []
        },
        "Giant Cell Glioblastoma": {
          "meaning": "icdo:9441/3",
          "comments": []
        },
        "Chordoid Glioma": {
          "meaning": "icdo:9444/1",
          "comments": []
        },
        "Glioblastoma, Idh-Mutant": {
          "meaning": "icdo:9445/3",
          "comments": []
        },
        "Oligodendroglioma, Nos": {
          "meaning": "icdo:9450/3",
          "comments": []
        },
        "Oligodendroglioma, Anaplastic": {
          "meaning": "icdo:9451/3",
          "comments": []
        },
        "Medulloblastoma, Wnt-Activated": {
          "meaning": "icdo:9475/3",
          "comments": []
        },
        "Medulloblastoma, Shh-Activated And Tp53-Mutant": {
          "meaning": "icdo:9476/3",
          "comments": []
        },
        "Medulloblastoma, Non-Wnt/Non-Shh": {
          "meaning": "icdo:9477/3",
          "comments": []
        },
        "Embryonal Tumor With Multilayered Rosettes, Nos": {
          "meaning": "icdo:9478/3",
          "comments": []
        },
        "Multinodular And Vascolating Neuronal Tumor": {
          "meaning": "icdo:9505/0",
          "comments": []
        },
        "Ganglioglioma, Nos": {
          "meaning": "icdo:9505/1",
          "comments": []
        },
        "Atypical Teratoid/Rhabdoid Tumor": {
          "meaning": "icdo:9508/3",
          "comments": []
        },
        "Neurofibroma, Nos": {
          "meaning": "icdo:9540/0",
          "comments": []
        },
        "Neurofibromatosis, Nos": {
          "meaning": "icdo:9540/1",
          "comments": []
        },
        "Melanotic Neurofibroma": {
          "meaning": "icdo:9541/0",
          "comments": []
        },
        "Plexiform Neurofibroma": {
          "meaning": "icdo:9550/0",
          "comments": []
        },
        "Neurilemoma, Nos": {
          "meaning": "icdo:9560/0",
          "comments": []
        },
        "Melanotic Schwannoma": {
          "meaning": "icdo:9560/1",
          "comments": []
        },
        "Choroid Plexus Papilloma, NOS": {
          "meaning": "icdo:9390/0",
          "comments": []
        },
        "Choroid Plexus Papilloma, Malignant": {
          "meaning": "icdo:9390/3",
          "comments": []
        },
        "Centrol Neurocytoma": {
          "meaning": "icdo:9506/1",
          "comments": []
        },
        "Medulloblastoma, Nos": {
          "meaning": "icdo:9470/3",
          "comments": []
        },
        "Desmoplastic Medulloblastoma": {
          "meaning": "icdo:9471/3",
          "comments": []
        },
        "Large Cell Medulloblastoma": {
          "meaning": "icdo:9474/3",
          "comments": []
        },
        "Cerebellar Sarcoma, NOS": {
          "meaning": "icdo:9480/3",
          "comments": []
        },
        "Dysplastic Gangliocytoma Of Cerebellum (Lhermitte-Duclos)": {
          "meaning": "icdo:9493/0",
          "comments": []
        },
        "Multinodular And Vacuolating Neuronal Tumor": {
          "meaning": "icdo:9509/0",
          "comments": []
        },
        "Atypical Lipoma": {
          "meaning": "icdo:8850/1",
          "comments": []
        },
        "Leiomyoma, Nos": {
          "meaning": "icdo:8890/0",
          "comments": []
        },
        "Leiomyomatosis, NOS": {
          "meaning": "icdo:8890/1",
          "comments": []
        },
        "Smooth Muscle Tumor, NOS": {
          "meaning": "icdo:8897/1",
          "comments": []
        },
        "Hemangioendothelioma, Benign": {
          "meaning": "icdo:9130/0",
          "comments": []
        },
        "Follicular Adenocarcinoma, NOS": {
          "meaning": "icdo:8330/3",
          "comments": []
        },
        "Follicular Adenocarcinoma Well Diff.": {
          "meaning": "icdo:8331/3",
          "comments": []
        },
        "Follicular Adenocarcinoma Trabecular": {
          "meaning": "icdo:8332/3",
          "comments": []
        },
        "Follicular Carcinoma, Minimally Invasive": {
          "meaning": "icdo:8335/3",
          "comments": []
        },
        "Insular Carcinoma": {
          "meaning": "icdo:8337/3",
          "comments": []
        },
        "Follicular Thyroid Carcinoma (Ftc), Encapsulated Angioinvasive": {
          "meaning": "icdo:8339/3",
          "comments": []
        },
        "Papillary Carcinoma, Follicular Variant": {
          "meaning": "icdo:8340/3",
          "comments": []
        },
        "Papillary Microcarcinoma": {
          "meaning": "icdo:8341/3",
          "comments": []
        },
        "Papillary Carcinoma, Oxyphilic Cell": {
          "meaning": "icdo:8342/3",
          "comments": []
        },
        "Non-Invasive Efvptc": {
          "meaning": "icdo:8343/2",
          "comments": []
        },
        "Papillary Carcinoma, Encapsulated": {
          "meaning": "icdo:8343/3",
          "comments": []
        },
        "Papillary Carcinoma, Columnar Cell": {
          "meaning": "icdo:8344/3",
          "comments": []
        },
        "Medullary Carcinoma With Amyloid Stroma": {
          "meaning": "icdo:8345/3",
          "comments": []
        },
        "Mixed Medullary-Follicular Carcinoma": {
          "meaning": "icdo:8346/3",
          "comments": []
        },
        "Mixed Medullary-Papillary Carcinoma": {
          "meaning": "icdo:8347/3",
          "comments": []
        },
        "Nonencapsulated Sclerosing Carcinoma": {
          "meaning": "icdo:8350/3",
          "comments": []
        },
        "Adrenal Cortical Carcinoma": {
          "meaning": "icdo:8370/3",
          "comments": []
        },
        "Water-Clear Cell Adenocarcinoma": {
          "meaning": "icdo:8322/3",
          "comments": []
        },
        "Clear Cell Tumor, NOS": {
          "meaning": "icdo:8005/0",
          "comments": []
        },
        "Epithelial Tumor, Benign": {
          "meaning": "icdo:8010/0",
          "comments": []
        },
        "Monomorphic Adenoma": {
          "meaning": "icdo:8146/0",
          "comments": []
        },
        "Papillary Adenoma, NOS": {
          "meaning": "icdo:8260/0",
          "comments": []
        },
        "Chromophobe Adenoma": {
          "meaning": "icdo:8270/0",
          "comments": []
        },
        "Chromophobe Carcinoma": {
          "meaning": "icdo:8270/3",
          "comments": []
        },
        "Pituitary Adenoma, NOS": {
          "meaning": "icdo:8272/0",
          "comments": []
        },
        "Pituitary Carcinoma, NOS": {
          "meaning": "icdo:8272/3",
          "comments": []
        },
        "Pituitary Blastoma": {
          "meaning": "icdo:8273/3",
          "comments": []
        },
        "Acidophil Adenoma": {
          "meaning": "icdo:8280/0",
          "comments": []
        },
        "Acidophil Carcinoma": {
          "meaning": "icdo:8280/3",
          "comments": []
        },
        "Mixed Acidophil-Basophil Adenoma": {
          "meaning": "icdo:8281/0",
          "comments": []
        },
        "Mixed Acidophil-Basophil Carcinoma": {
          "meaning": "icdo:8281/3",
          "comments": []
        },
        "Oxyphilic Adenoma": {
          "meaning": "icdo:8290/0",
          "comments": []
        },
        "Basophil Adenoma": {
          "meaning": "icdo:8300/0",
          "comments": []
        },
        "Basophil Carcinoma": {
          "meaning": "icdo:8300/3",
          "comments": []
        },
        "Clear Cell Adenoma": {
          "meaning": "icdo:8310/0",
          "comments": []
        },
        "Mixed Cell Adenoma": {
          "meaning": "icdo:8323/0",
          "comments": []
        },
        "Granular Cell Tumor, NOS": {
          "meaning": "icdo:9580/0",
          "comments": []
        },
        "Granular Cell Tumor Of The Sellar Region": {
          "meaning": "icdo:9582/0",
          "comments": []
        },
        "Pinealoma, NOS": {
          "meaning": "icdo:9360/1",
          "comments": []
        },
        "Pineoblastoma": {
          "meaning": "icdo:9362/3",
          "comments": []
        },
        "Papillary Tumor Of Pineal Region": {
          "meaning": "icdo:9395/3",
          "comments": []
        },
        "Parasympathetic Paraganglioma": {
          "meaning": "icdo:8682/3",
          "comments": []
        },
        "Middle Ear Paraganglioma": {
          "meaning": "icdo:8690/3",
          "comments": []
        },
        "Aortic Body Tumor, Malignant": {
          "meaning": "icdo:8691/3",
          "comments": []
        },
        "Carotid Body Tumor, Malignant": {
          "meaning": "icdo:8692/3",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Ultrasound": {
          "meaning": "ncit:C64384",
          "comments": []
        }
      }
    },
    "SpermatogoniaDensityUnitEnum": {
      "permissible_values": {
        "count/tubule": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OtcSurgicalEnergySourceEnum": {
      "permissible_values": {
        "Ligasure Bipolar": {
          "meaning": "",
          "comments": []
        },
        "Harmonic Bipolar": {
          "meaning": "",
          "comments": []
        },
        "Monopolar": {
          "meaning": "",
          "comments": []
        },
        "None / Cold Scissor": {
          "meaning": "",
          "comments": []
        },
        "Cold Scissor Converted to Ligasure Bipolar": {
          "meaning": "",
          "comments": []
        },
        "Cold Scissor Converted to Harmonic Bipolar": {
          "meaning": "",
          "comments": []
        },
        "Cold Scissor Converted to Monopolar": {
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
    "GenderIdentityEnum": {
      "permissible_values": {
        "Asked But Declined": {
          "meaning": "",
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
        "Male-To-Female Transgender": {
          "meaning": "SCTID: 33791000087105",
          "comments": []
        },
        "Female-To-Male Transgender": {
          "meaning": "SCTID: 407377005",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
        "FPRH": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Bleeding": {
          "meaning": "",
          "comments": []
        },
        "Fever": {
          "meaning": "",
          "comments": []
        },
        "Pain": {
          "meaning": "",
          "comments": []
        },
        "Infection": {
          "meaning": "ncit:C128320",
          "comments": []
        }
      }
    },
    "MenstrualStatusEnum": {
      "permissible_values": {
        "Menstruating, Regular": {
          "meaning": "",
          "comments": []
        },
        "Menstruating, Irregular": {
          "meaning": "",
          "comments": []
        },
        "Not Menstruating": {
          "meaning": "",
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
    "SurgeonTypeEnum": {
      "permissible_values": {
        "Adult Urologist": {
          "meaning": "",
          "comments": []
        },
        "Pediatric Urologist": {
          "meaning": "",
          "comments": []
        },
        "Adult General": {
          "meaning": "",
          "comments": []
        },
        "Pediatric General": {
          "meaning": "",
          "comments": []
        },
        "Adult Gynecologist": {
          "meaning": "",
          "comments": []
        },
        "Pediatric Gynecologist": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "LaboratoryResultEnum": {
      "permissible_values": {
        "Positive": {
          "meaning": "ncit:C38758",
          "comments": []
        },
        "Negative": {
          "meaning": "ncit:C38757",
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
    "MaritalStatusEnum": {
      "permissible_values": {
        "Divorced": {
          "meaning": "ncit:C51776",
          "comments": []
        },
        "Domestic Partnership": {
          "meaning": "ncit:C53262",
          "comments": []
        },
        "Married": {
          "meaning": "ncit:C51773",
          "comments": []
        },
        "Never Married": {
          "meaning": "ncit:C51774",
          "comments": []
        },
        "Separated": {
          "meaning": "ncit:C156541",
          "comments": []
        },
        "Widowed": {
          "meaning": "ncit:C51775",
          "comments": []
        },
        "Marital or Civil Status Not Disclosed": {
          "meaning": "ncit:C150742",
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
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Abdominal Wall": {
          "meaning": "ncit:C28256",
          "comments": []
        },
        "Acetabulum": {
          "meaning": "ncit:C32042",
          "comments": []
        },
        "Adjacent Organ": {
          "meaning": "ncit:C180347",
          "comments": []
        },
        "Adrenal Gland": {
          "meaning": "ncit:C12666",
          "comments": []
        },
        "Anal/Perianal": {
          "meaning": "ncit:C99148",
          "comments": []
        },
        "Ankle": {
          "meaning": "ncit:C32078",
          "comments": []
        },
        "Ankle Joint": {
          "meaning": "ncit:C32078",
          "comments": []
        },
        "Anterior Skull Base": {
          "meaning": "ncit:C180372",
          "comments": []
        },
        "Anus": {
          "meaning": "ncit:C43362",
          "comments": []
        },
        "Appendix": {
          "meaning": "ncit:C12380",
          "comments": []
        },
        "Ascitic Fluid": {
          "meaning": "ncit:C159203",
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
        "Axillary Nodes": {
          "meaning": "ncit:C12904",
          "comments": []
        },
        "Basal Ganglia-Thalamus": {
          "meaning": "ncit:C158080",
          "comments": []
        },
        "Basin": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Bladder": {
          "meaning": "ncit:C12414",
          "comments": []
        },
        "Bladder/Prostate": {
          "meaning": "ncit:C12410",
          "comments": []
        },
        "Bone Face": {
          "meaning": "ncit:C63706",
          "comments": []
        },
        "Bone Foot": {
          "meaning": "ncit:C13068",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Bone Shoulder Girdle": {
          "meaning": "ncit:C33547",
          "comments": []
        },
        "Bone or Bone Marrow": {
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
        "Brain/Leptomeninges": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Breast": {
          "meaning": "ncit:C12971",
          "comments": []
        },
        "Bronchus": {
          "meaning": "ncit:C12683",
          "comments": []
        },
        "Buttock": {
          "meaning": "ncit:C89806",
          "comments": []
        },
        "Calcaneum": {
          "meaning": "ncit:C32250",
          "comments": []
        },
        "Carpal Bone": {
          "meaning": "ncit:C12688",
          "comments": []
        },
        "Cauda Equina Spinal Cord": {
          "meaning": "ncit:C12689",
          "comments": []
        },
        "Celiac Nodes": {
          "meaning": "ncit:C65166",
          "comments": []
        },
        "Central Nervous System": {
          "meaning": "ncit:C12438",
          "comments": []
        },
        "Cerebellum": {
          "meaning": "ncit:C12445",
          "comments": []
        },
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Cervical Nodes": {
          "meaning": "ncit:C32298",
          "comments": []
        },
        "Cervical Spine": {
          "meaning": "ncit:C69313",
          "comments": []
        },
        "Cervical Vertebra": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Cervix": {
          "meaning": "ncit:C12311",
          "comments": []
        },
        "Cheek": {
          "meaning": "ncit:C13070",
          "comments": []
        },
        "Chest": {
          "meaning": "ncit:C25389",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Choroid": {
          "meaning": "",
          "comments": []
        },
        "Clavicle": {
          "meaning": "ncit:C24203",
          "comments": []
        },
        "Coccyx": {
          "meaning": "ncit:C12696",
          "comments": []
        },
        "Colon": {
          "meaning": "ncit:C12382",
          "comments": []
        },
        "Cranium": {
          "meaning": "ncit:C12697",
          "comments": []
        },
        "Cutaneous": {
          "meaning": "ncit:C13316",
          "comments": []
        },
        "Dermis": {
          "meaning": "ncit:C12701",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Dorsal Spine": {
          "meaning": "ncit:C32472",
          "comments": []
        },
        "Dorsal Vertebra": {
          "meaning": "ncit:C12693",
          "comments": []
        },
        "Duodenum": {
          "meaning": "ncit:C12263",
          "comments": []
        },
        "Elbow": {
          "meaning": "ncit:C32497",
          "comments": []
        },
        "Elbow Joint": {
          "meaning": "ncit:C32497",
          "comments": []
        },
        "Epididymis": {
          "meaning": "ncit:C12328",
          "comments": []
        },
        "Epitrochlear Nodes": {
          "meaning": "ncit:C98182",
          "comments": []
        },
        "Esophagus": {
          "meaning": "ncit:C12389",
          "comments": []
        },
        "Ethmoid Bone": {
          "meaning": "ncit:C12711",
          "comments": []
        },
        "Extra CNS": {
          "meaning": "",
          "comments": []
        },
        "Eyelid": {
          "meaning": "ncit:C12713",
          "comments": []
        },
        "Face": {
          "meaning": "ncit:C13071",
          "comments": []
        },
        "Facial Region": {
          "meaning": "ncit:C13071",
          "comments": []
        },
        "Fallopian Tube": {
          "meaning": "ncit:C12403",
          "comments": []
        },
        "Female Reproductive System Part": {
          "meaning": "ncit:C13039",
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
        "Fibular Head": {
          "meaning": "ncit:C32719",
          "comments": []
        },
        "Finger": {
          "meaning": "ncit:C32608",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Foot Bone": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Foot Joint": {
          "meaning": "ncit:C32623",
          "comments": []
        },
        "Foot Phalanges": {
          "meaning": "ncit:C52772",
          "comments": []
        },
        "Forearm": {
          "meaning": "ncit:C32628",
          "comments": []
        },
        "Fourth Ventricle": {
          "meaning": "ncit:C12828",
          "comments": []
        },
        "Frontal Bone": {
          "meaning": "ncit:C32635",
          "comments": []
        },
        "Frontal Cortex": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Frontal Lobe": {
          "meaning": "ncit:C12352",
          "comments": []
        },
        "Gallbladder": {
          "meaning": "ncit:C12377",
          "comments": []
        },
        "Gastrointestinal Tract": {
          "meaning": "ncit:C34082",
          "comments": []
        },
        "Groin": {
          "meaning": "ncit:C12726",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hand Bone": {
          "meaning": "ncit:C52771",
          "comments": []
        },
        "Hand Joint": {
          "meaning": "ncit:C32868",
          "comments": []
        },
        "Hand Phalanges": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Head": {
          "meaning": "ncit:C12419",
          "comments": []
        },
        "Head and Neck": {
          "meaning": "",
          "comments": []
        },
        "Heart": {
          "meaning": "ncit:C12727",
          "comments": []
        },
        "Hilar Nodes": {
          "meaning": "ncit:C134731",
          "comments": []
        },
        "Hip": {
          "meaning": "ncit:C64193",
          "comments": []
        },
        "Hip/Inguinal Region": {
          "meaning": "ncit:C12726",
          "comments": []
        },
        "Humerus": {
          "meaning": "ncit:C12731",
          "comments": []
        },
        "Hypodermis": {
          "meaning": "ncit:C92441",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "ncit:C12246",
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
        "Ilium": {
          "meaning": "ncit:C32765",
          "comments": []
        },
        "Inferior Limb": {
          "meaning": "ncit:C12982",
          "comments": []
        },
        "Infraclavicular Lymph Node": {
          "meaning": "ncit:C63705",
          "comments": []
        },
        "Infraclavicular Nodes": {
          "meaning": "ncit:C63705",
          "comments": []
        },
        "Infratemporal Fossa/Pterygopalatine": {
          "meaning": "",
          "comments": []
        },
        "Infratemporal Fossa/Pterygopalatine and Parapharyngeal Area": {
          "meaning": "",
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
        "Intra-Abdominal": {
          "meaning": "ncit:C12726",
          "comments": []
        },
        "Intraperitoneal": {
          "meaning": "ncit:C13352",
          "comments": []
        },
        "Intrathoracic": {
          "meaning": "ncit:C105579",
          "comments": []
        },
        "Intraspinal": {
          "meaning": "ncit:C96908",
          "comments": []
        },
        "Ischium": {
          "meaning": "ncit:C32884",
          "comments": []
        },
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Knee": {
          "meaning": "ncit:C32898",
          "comments": []
        },
        "Knee Joint": {
          "meaning": "ncit:C32899",
          "comments": []
        },
        "Lacrimal Bone": {
          "meaning": "ncit:C32906",
          "comments": []
        },
        "Larynx": {
          "meaning": "ncit:C12420",
          "comments": []
        },
        "Lateral Ventricle": {
          "meaning": "ncit:C12834",
          "comments": []
        },
        "Leg": {
          "meaning": "ncit:C32974",
          "comments": []
        },
        "Leptomeningeal": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Liver/Biliary Tract": {
          "meaning": "ncit:C12678",
          "comments": []
        },
        "Lower Arm": {
          "meaning": "",
          "comments": []
        },
        "Lower Extremity": {
          "meaning": "ncit:C12742",
          "comments": []
        },
        "Lower Leg": {
          "meaning": "",
          "comments": []
        },
        "Lower Limb, NOS": {
          "meaning": "ncit:C12742",
          "comments": []
        },
        "Lower Spine": {
          "meaning": "ncit:C69314",
          "comments": []
        },
        "Lumbar Spinal Cord": {
          "meaning": "ncit:C12895",
          "comments": []
        },
        "Lumbar Spine": {
          "meaning": "ncit:C69314",
          "comments": []
        },
        "Lumbar Vertebra": {
          "meaning": "ncit:C45874",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Lung/Pleura": {
          "meaning": "ncit:C12469",
          "comments": []
        },
        "Lymph Node": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Lymphatic Basin": {
          "meaning": "ncit:C94547",
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
        "Medulla": {
          "meaning": "ncit:C12442",
          "comments": []
        },
        "Meninges": {
          "meaning": "ncit:C12348",
          "comments": []
        },
        "Mesenteric Nodes": {
          "meaning": "ncit:C77641",
          "comments": []
        },
        "Metacarpals": {
          "meaning": "ncit:C12751",
          "comments": []
        },
        "Metacarpus": {
          "meaning": "ncit:C12751",
          "comments": []
        },
        "Metatarsals": {
          "meaning": "ncit:C12752",
          "comments": []
        },
        "Metatarsus": {
          "meaning": "ncit:C12752",
          "comments": []
        },
        "Midbrain": {
          "meaning": "ncit:C12510",
          "comments": []
        },
        "Middle Ear": {
          "meaning": "ncit:C12274",
          "comments": []
        },
        "Muscle": {
          "meaning": "",
          "comments": []
        },
        "Nasal Bone": {
          "meaning": "ncit:C33157",
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
        "Nasal Septum": {
          "meaning": "ncit:C33160",
          "comments": []
        },
        "Nasopharynx": {
          "meaning": "ncit:C12423",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Occipital Bone": {
          "meaning": "ncit:C12757",
          "comments": []
        },
        "Occipital Lobe": {
          "meaning": "ncit:C12355",
          "comments": []
        },
        "Omentum": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Omentum/Peritoneum": {
          "meaning": "ncit:C33209",
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
        "Optic Nerve Head, Intra-Laminar": {
          "meaning": "",
          "comments": []
        },
        "Optic Nerve Head, Pre-Laminar": {
          "meaning": "",
          "comments": []
        },
        "Oral Cavity": {
          "meaning": "ncit:C12421",
          "comments": []
        },
        "Orbit": {
          "meaning": "ncit:C12347",
          "comments": []
        },
        "Oropharynx": {
          "meaning": "ncit:C12762",
          "comments": []
        },
        "Other Extremity": {
          "meaning": "",
          "comments": []
        },
        "Other Face": {
          "meaning": "",
          "comments": []
        },
        "Other GU Non-Bladder/Prostate": {
          "meaning": "",
          "comments": []
        },
        "Other Head and Neck": {
          "meaning": "",
          "comments": []
        },
        "Other Orbit": {
          "meaning": "",
          "comments": []
        },
        "Other Parameningeal": {
          "meaning": "",
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
        "Paraaortic Lymph Node": {
          "meaning": "ncit:C77643",
          "comments": []
        },
        "Paranasal Sinuses": {
          "meaning": "ncit:C12763",
          "comments": []
        },
        "Parapharyngeal Area": {
          "meaning": "ncit:C162818",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "ncit:C129461",
          "comments": []
        },
        "Paratesticular": {
          "meaning": "ncit:C162491",
          "comments": []
        },
        "Parathyroid": {
          "meaning": "",
          "comments": []
        },
        "Parietal Bone": {
          "meaning": "ncit:C12766",
          "comments": []
        },
        "Parietal Cortex": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Parietal Lobe": {
          "meaning": "ncit:C12354",
          "comments": []
        },
        "Parotid": {
          "meaning": "ncit:C12427",
          "comments": []
        },
        "Patella": {
          "meaning": "ncit:C33282",
          "comments": []
        },
        "Pectoral Nodes": {
          "meaning": "ncit:C120322",
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
        "Perineum": {
          "meaning": "ncit:C33301",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": [
            "(ews) ConsortiumNote: Included so that peritoneal effusions can be reported."
          ]
        },
        "Pineal": {
          "meaning": "ncit:C12398",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": [
            "(ews) ConsortiumNote: Included so that pleural effusions can be reported.",
            "(os) ConsortiumNote: Included so that pleural effusions can be reported."
          ]
        },
        "Pleural Effusion": {
          "meaning": "ncit:C3331",
          "comments": []
        },
        "Pons": {
          "meaning": "ncit:C12511",
          "comments": []
        },
        "Popliteal Nodes": {
          "meaning": "ncit:C53146",
          "comments": []
        },
        "Preauricular Lymph Node": {
          "meaning": "ncit:C103429",
          "comments": []
        },
        "Prostate": {
          "meaning": "ncit:C12410",
          "comments": []
        },
        "Radius Bone": {
          "meaning": "ncit:C12777",
          "comments": []
        },
        "Rectum": {
          "meaning": "ncit:C12390",
          "comments": []
        },
        "Regional Lymph Nodes": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Rib": {
          "meaning": "ncit:C12782",
          "comments": []
        },
        "Sacral Region": {
          "meaning": "ncit:C33508",
          "comments": []
        },
        "Sacrococcygeal": {
          "meaning": "ncit:C33506",
          "comments": []
        },
        "Salivary Gland": {
          "meaning": "ncit:C12426",
          "comments": []
        },
        "Sacrum": {
          "meaning": "ncit:C33508",
          "comments": []
        },
        "Scalp": {
          "meaning": "ncit:C89807",
          "comments": []
        },
        "Shoulder": {
          "meaning": "ncit:C12783",
          "comments": []
        },
        "Shoulder Girdle": {
          "meaning": "ncit:C33547",
          "comments": []
        },
        "Shoulder Joint": {
          "meaning": "ncit:C33548",
          "comments": []
        },
        "Skin": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Skull, NOS": {
          "meaning": "ncit:C12789",
          "comments": []
        },
        "Small Intestine": {
          "meaning": "ncit:C12386",
          "comments": []
        },
        "Soft Tissue": {
          "meaning": "ncit:C12471",
          "comments": []
        },
        "Sphenoid Bone": {
          "meaning": "ncit:C12790",
          "comments": []
        },
        "Spinal Cord": {
          "meaning": "ncit:C12464",
          "comments": []
        },
        "Spine": {
          "meaning": "ncit:C12998",
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
        "Sternum": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Stomach": {
          "meaning": "ncit:C12391",
          "comments": []
        },
        "Stroma of Iris": {
          "meaning": "",
          "comments": []
        },
        "Superior Maxilla": {
          "meaning": "ncit:C33682",
          "comments": []
        },
        "Supraclavicular Lymph Node": {
          "meaning": "ncit:C12903",
          "comments": []
        },
        "Supraclavicular Nodes": {
          "meaning": "ncit:C12903",
          "comments": []
        },
        "Suprasellar Pituitary": {
          "meaning": "ncit:C95445",
          "comments": []
        },
        "Suprasellar/Neurohypophyseal": {
          "meaning": "ncit:C42602",
          "comments": []
        },
        "Talus": {
          "meaning": "ncit:C52799",
          "comments": []
        },
        "Tarsal Bone": {
          "meaning": "ncit:C12796",
          "comments": []
        },
        "Tarsals": {
          "meaning": "ncit:C12796",
          "comments": []
        },
        "Temporal Bone": {
          "meaning": "ncit:C12797",
          "comments": []
        },
        "Temporal Cortex": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Temporal Lobe": {
          "meaning": "ncit:C12353",
          "comments": []
        },
        "Testis": {
          "meaning": "ncit:C12412",
          "comments": []
        },
        "Thalamus": {
          "meaning": "ncit:C12459",
          "comments": []
        },
        "Thigh": {
          "meaning": "ncit:C33763",
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
        "Thoracic Vertebra": {
          "meaning": "ncit:C12798",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
          "comments": []
        },
        "Thymus": {
          "meaning": "ncit:C12433",
          "comments": []
        },
        "Thyroid": {
          "meaning": "ncit:C12400",
          "comments": []
        },
        "Tibia": {
          "meaning": "ncit:C12800",
          "comments": []
        },
        "Toe": {
          "meaning": "ncit:C33788",
          "comments": []
        },
        "Tonsil": {
          "meaning": "ncit:C12802",
          "comments": []
        },
        "Trachea": {
          "meaning": "ncit:C12428",
          "comments": []
        },
        "Trabecular Meshwork": {
          "meaning": "",
          "comments": []
        },
        "Trunk": {
          "meaning": "ncit:C33816",
          "comments": []
        },
        "Ulna": {
          "meaning": "ncit:C12809",
          "comments": []
        },
        "Upper Airway": {
          "meaning": "ncit:C33839",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "ncit:C32141",
          "comments": []
        },
        "Upper Extremity": {
          "meaning": "ncit:C12671",
          "comments": []
        },
        "Upper Limb, NOS": {
          "meaning": "ncit:C12671",
          "comments": []
        },
        "Ureter": {
          "meaning": "ncit:C12416",
          "comments": []
        },
        "Urogenital": {
          "meaning": "ncit:C25350",
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
        "Vasculo-Nervous": {
          "meaning": "ncit:C74603",
          "comments": []
        },
        "Viscera": {
          "meaning": "ncit:C28287",
          "comments": []
        },
        "Vulva": {
          "meaning": "ncit:C12408",
          "comments": []
        },
        "Waldeyer's Ring": {
          "meaning": "ncit:C73468",
          "comments": []
        },
        "Wrist": {
          "meaning": "ncit:C33894",
          "comments": []
        },
        "Wrist Joint": {
          "meaning": "ncit:C33895",
          "comments": []
        },
        "Zygomatic Bone": {
          "meaning": "ncit:C33897",
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
    "TransportMediaEnum": {
      "permissible_values": {
        "Cooper Surgical (OFC Transport Media)": {
          "meaning": "",
          "comments": []
        },
        "Lactated Ringers": {
          "meaning": "ncit:C65149",
          "comments": []
        },
        "Modified Human Tubal Fluid, NOS": {
          "meaning": "ncit:C65149",
          "comments": []
        },
        "Irvine Modified Human Tubal Fluid": {
          "meaning": "ncit:C65149",
          "comments": []
        },
        "Irvine Modified Human Tubal FluidOrigio Handling Media": {
          "meaning": "",
          "comments": []
        },
        "Custodiol": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ReasonDeclinedFertilityPreservationEnum": {
      "permissible_values": {
        "Cost": {
          "meaning": "",
          "comments": []
        },
        "No Time": {
          "meaning": "",
          "comments": []
        },
        "Sexual Orientation": {
          "meaning": "",
          "comments": []
        },
        "Not Interested": {
          "meaning": "",
          "comments": []
        },
        "Contraindicated": {
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
    "ProcedureClassEnum": {
      "permissible_values": {
        "Fertility Tissue Preservation": {
          "meaning": "",
          "comments": []
        },
        "Fertility Preserved Tissue Utilization": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TissueTypeUtilizedEnum": {
      "permissible_values": {
        "Cryopreserved Ovarian Tissue": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Embryo": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Oocyte": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Ovarian Tissue Oocyte": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Ejaculated Sperm": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Testicular Tissue Sperm": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved TESE/TESA Sperm": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Testicular Tissue ": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "FreezingMethodEnum": {
      "permissible_values": {
        "Vitrification": {
          "meaning": "",
          "comments": []
        },
        "Controlled Slow Rate Freezing": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OocyteOrEmbryoSourceEnum": {
      "permissible_values": {
        "Autologous Egg": {
          "meaning": "",
          "comments": []
        },
        "Autologous Embryo": {
          "meaning": "",
          "comments": []
        },
        "Donated Embryo": {
          "meaning": "",
          "comments": []
        },
        "Donated Egg": {
          "meaning": "",
          "comments": []
        },
        "Autologous Ovarian Tissue": {
          "meaning": "",
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
    "TranspositionOrganEnum": {
      "permissible_values": {
        "Ovaries": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Uterus": {
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
    "OtcStripsWeightUnitEnum": {
      "permissible_values": {
        "mg": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MenstrualPhaseEnum": {
      "permissible_values": {
        "Early Follicular": {
          "meaning": "",
          "comments": []
        },
        "Mid/Late Follicular": {
          "meaning": "",
          "comments": []
        },
        "Follicular": {
          "meaning": "",
          "comments": []
        },
        "Luteal": {
          "meaning": "",
          "comments": []
        },
        "Periovulatory": {
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
    "VolumeUnitEnum": {
      "permissible_values": {
        "cm^3": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MedicationEnum": {
      "permissible_values": {
        "Ixabepilone": {
          "meaning": "rxcui:10485",
          "comments": []
        },
        "Iobenguane I-131": {
          "meaning": "rxcui:10485",
          "comments": []
        },
        "6 Thioguanine": {
          "meaning": "rxcui:10485",
          "comments": []
        },
        "6 Mercaptopurine": {
          "meaning": "rxcui:103",
          "comments": []
        },
        "Alemtuzumab": {
          "meaning": "rxcui:117055",
          "comments": []
        },
        "Aspacytarabine": {
          "meaning": "ncit:C1614",
          "comments": []
        },
        "Axitinib": {
          "meaning": "rxcui:1242999",
          "comments": []
        },
        "Bevacizumab": {
          "meaning": "rxcui:253337",
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
        "Cabozantinib": {
          "meaning": "ncit:C52200",
          "comments": []
        },
        "Capecitabine": {
          "meaning": "rxcui:194000",
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
        "Cetrotide": {
          "meaning": "rxcui:284693",
          "comments": []
        },
        "Cisplatin": {
          "meaning": "rxcui:2555",
          "comments": []
        },
        "Chlorambucil": {
          "meaning": "rxcui:2346",
          "comments": []
        },
        "Combination Estrogen/Progestin Hormonal Contraception": {
          "meaning": "ncit:C91717",
          "comments": []
        },
        "Contraceptive Patch": {
          "meaning": "rxcui:220714",
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
        "Cytarabine": {
          "meaning": "rxcui:3041",
          "comments": []
        },
        "Dabrafenib": {
          "meaning": "rxcui:1424911",
          "comments": []
        },
        "Actinomycin": {
          "meaning": "rxcui:3100",
          "comments": []
        },
        "Daunorubicin": {
          "meaning": "rxcui:3109",
          "comments": []
        },
        "Depo Provera": {
          "meaning": "rxcui:202886",
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
        "Entrectinib": {
          "meaning": "rxcui:2197862",
          "comments": []
        },
        "Epirubicin": {
          "meaning": "rxcui:3995",
          "comments": []
        },
        "Eribulin": {
          "meaning": "rxcui:1045453",
          "comments": []
        },
        "Estradiol": {
          "meaning": "rxcui:4083",
          "comments": []
        },
        "Etoposide": {
          "meaning": "rxcui:4179",
          "comments": []
        },
        "Ganilreix": {
          "meaning": "rxcui:35825",
          "comments": []
        },
        "Gemcitabine": {
          "meaning": "rxcui:12574",
          "comments": []
        },
        "Goserelin": {
          "meaning": "rxcui:50610",
          "comments": []
        },
        "Human Chorionic Gonadotropin (hCG)": {
          "meaning": "ncit:C528",
          "comments": []
        },
        "Human Menopausal Gonadotropin (hMG)": {
          "meaning": "ncit:C2274",
          "comments": []
        },
        "Hydroxyurea": {
          "meaning": "rxcui:5552",
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
        "Ipilimumab": {
          "meaning": "ncit:C2654",
          "comments": []
        },
        "Larotrectinib": {
          "meaning": "rxcui:2105628",
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
        "Leuprolide Acetate": {
          "meaning": "rxcui:203217",
          "comments": []
        },
        "Lomustine": {
          "meaning": "rxcui:6466",
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
        "Methotrexate": {
          "meaning": "rxcui:6851",
          "comments": []
        },
        "Mitoxantrone": {
          "meaning": "rxcui:7005",
          "comments": []
        },
        "Nab-Paclitaxel": {
          "meaning": "ncit:C2688",
          "comments": []
        },
        "Nelarabine": {
          "meaning": "rxcui:274771",
          "comments": []
        },
        "Nitrogen Mustard": {
          "meaning": "rxcui:6674",
          "comments": []
        },
        "Nivolumab": {
          "meaning": "rxcui:1597876",
          "comments": []
        },
        "Nuva Ring": {
          "meaning": "rxcui:1367439",
          "comments": []
        },
        "Oxaliplatin": {
          "meaning": "rxcui:32592",
          "comments": []
        },
        "Pazopanib": {
          "meaning": "rxcui:714438",
          "comments": []
        },
        "Pegylated Liposomal Doxorubicin Hydrochloride": {
          "meaning": "ncit:C1555",
          "comments": []
        },
        "Pembrolizumab": {
          "meaning": "rxcui:1547545",
          "comments": []
        },
        "Procarbazine": {
          "meaning": "rxcui:8702",
          "comments": []
        },
        "Progestin Implant": {
          "meaning": "",
          "comments": []
        },
        "Progestin-Only Pills": {
          "meaning": "",
          "comments": []
        },
        "Progestogen": {
          "meaning": "ncit:C2296",
          "comments": []
        },
        "Progestational Intrauterine Device": {
          "meaning": "ncit:C184790",
          "comments": []
        },
        "Recombinant FSH": {
          "meaning": "ncit:C1822",
          "comments": []
        },
        "Rituximab": {
          "meaning": "rxcui:121191",
          "comments": []
        },
        "Selpercatinib": {
          "meaning": "rxcui:2370147",
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
        "Testosterone": {
          "meaning": "rxcui:10379",
          "comments": []
        },
        "Thiotepa": {
          "meaning": "rxcui:10473",
          "comments": []
        },
        "Treosulfan": {
          "meaning": "rxcui:38508",
          "comments": []
        },
        "Triptorelin": {
          "meaning": "rxcui:38782",
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
        },
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
    "FertilityConsultOutcomeEnum": {
      "permissible_values": {
        "Sperm Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Oocyte Or Embryo Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Testicular Tissue Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Ovarian Tissue Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Declined Fertility Preservation Consult": {
          "meaning": "",
          "comments": []
        },
        "No Fertility Preservation Available": {
          "meaning": "",
          "comments": []
        },
        "No Fertility Preservation Indicated": {
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
    "ConsortiumEnum": {
      "permissible_values": {
        "RHOPE": {
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
        }
      }
    },
    "SiteClassificationEnum": {
      "permissible_values": {
        "Metastatic": {
          "meaning": "ncit:C3261",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "",
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
    "LaboratoryTestEnum": {
      "permissible_values": {
        "Absolute Neutrophil Count (ANC)": {
          "meaning": "ncit:C63321",
          "comments": []
        },
        "Anti-Mullerian Hormone (AMH)": {
          "meaning": "ncit:C120625",
          "comments": []
        },
        "Antral Follicle Count": {
          "meaning": "ncit:C97213",
          "comments": []
        },
        "Estradiol": {
          "meaning": "ncit:C74782",
          "comments": []
        },
        "Follicle-Stimulating Hormone (FSH)": {
          "meaning": "",
          "comments": []
        },
        "Free Testosterone": {
          "meaning": "ncit:C74785",
          "comments": []
        },
        "hCG": {
          "meaning": "ncit:C75387",
          "comments": []
        },
        "Hemoglobin": {
          "meaning": "ncit:C64848",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Inhibin-B": {
          "meaning": "ncit:C2276",
          "comments": []
        },
        "Luteinizing Hormone Test": {
          "meaning": "ncit:C74790",
          "comments": []
        },
        "Platelets": {
          "meaning": "ncit:C51951",
          "comments": [
            "(fa) ConsortiumNote: CBC"
          ]
        },
        "Progesterone": {
          "meaning": "ncit:C74791",
          "comments": []
        },
        "Prolactin": {
          "meaning": "ncit:C74870",
          "comments": []
        },
        "Total Testosterone": {
          "meaning": "ncit:C74793",
          "comments": []
        },
        "WBC": {
          "meaning": "ncit:C51948",
          "comments": []
        }
      }
    },
    "FertilityConsultIneligibleReasonEnum": {
      "permissible_values": {
        "Observation Only": {
          "meaning": "",
          "comments": []
        },
        "Palliative Or <20% Expected Survival": {
          "meaning": "",
          "comments": []
        },
        "Severe Cognitive Delay": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "FertilityProcedureEnum": {
      "permissible_values": {
        "Cryopreserved Ovarian Tissue Reimplantation": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Testicular Cell Reimplantation": {
          "meaning": "",
          "comments": []
        },
        "Cryopreserved Testicular Tissue Reimplantation": {
          "meaning": "",
          "comments": []
        },
        "Embryo Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Epidydimal Sperm Aspiration": {
          "meaning": "",
          "comments": []
        },
        "Oocyte Cryopreservation": {
          "meaning": "",
          "comments": []
        },
        "Oocyte Retrieval from Transplanted Ovarian Tissue": {
          "meaning": "",
          "comments": []
        },
        "Oophoropexy": {
          "meaning": "",
          "comments": []
        },
        "OTC, Cortical Strip": {
          "meaning": "",
          "comments": []
        },
        "OTC, Oophorectomy": {
          "meaning": "",
          "comments": []
        },
        "OTC, Partial Oophorectomy": {
          "meaning": "",
          "comments": []
        },
        "Semen Collection": {
          "meaning": "",
          "comments": []
        },
        "Sperm Retrieval from Transplanted Testicular Cells": {
          "meaning": "",
          "comments": []
        },
        "Sperm Retrieval from Transplanted Testicular Tissue": {
          "meaning": "",
          "comments": []
        },
        "Testicular Sperm Aspiration": {
          "meaning": "",
          "comments": []
        },
        "Testicular Sperm Extraction, Micro TESE": {
          "meaning": "",
          "comments": []
        },
        "Testicular Sperm Extraction, TESE": {
          "meaning": "",
          "comments": []
        },
        "Testicular Tissue Cryopreservation, Orchiectomy": {
          "meaning": "",
          "comments": []
        },
        "Testicular Tissue Cryopreservation, Partial Orchiectomy/Biopsy": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "RetrievalMethodEnum": {
      "permissible_values": {
        "Abdominal Ultrasound Guided": {
          "meaning": "",
          "comments": []
        },
        "Transvaginal Ultrasound Scanning (TVUS) Guided": {
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
        "Consolidation": {
          "meaning": "ncit:C15679",
          "comments": []
        },
        "Fertility Preservation Therapy": {
          "meaning": "ncit:C71326",
          "comments": []
        },
        "Fertility Utilization": {
          "meaning": "",
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
        },
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
    "SemenAbnormalityEnum": {
      "permissible_values": {
        "Oligospermia": {
          "meaning": "",
          "comments": []
        },
        "Severe Oligospermia": {
          "meaning": "",
          "comments": []
        },
        "Azoospermia": {
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
    "BirthWeightUnitEnum": {
      "permissible_values": {
        "g": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ReligionTypeEnum": {
      "permissible_values": {
        "None": {
          "meaning": "ncit:C41132",
          "comments": []
        },
        "Christian": {
          "meaning": "ncit:C176033",
          "comments": []
        },
        "Buddhist": {
          "meaning": "ncit:C103284",
          "comments": []
        },
        "Hindu": {
          "meaning": "ncit:C103291",
          "comments": []
        },
        "Jewish": {
          "meaning": "ncit:C211623",
          "comments": []
        },
        "Muslim": {
          "meaning": "ncit:C103285",
          "comments": []
        },
        "Sikh": {
          "meaning": "ncit:C176036",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "EndometrialStripeThicknessUnitEnum": {
      "permissible_values": {
        "mm": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "OocyteOrEmbryoStateEnum": {
      "permissible_values": {
        "Fresh": {
          "meaning": "",
          "comments": []
        },
        "Thawed": {
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
        "Intraperitoneal": {
          "meaning": "",
          "comments": []
        },
        "Intrathecal": {
          "meaning": "ncit:C173292",
          "comments": []
        },
        "Oral": {
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
        "IRS >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Stage 4": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 0": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 1a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 1b": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 2a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 2b": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 3a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 3b": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 4a": {
          "meaning": "",
          "comments": []
        },
        "IRSS >> Group 4b": {
          "meaning": "",
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
        },
        "System NOS, L1": {
          "meaning": "",
          "comments": []
        },
        "System NOS, L2": {
          "meaning": "",
          "comments": []
        },
        "System NOS, M": {
          "meaning": "",
          "comments": []
        },
        "System NOS, MS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SiteFindingEnum": {
      "permissible_values": {
        "Cyst": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AeGradeSystemEnum": {
      "permissible_values": {
        "Clavien-Dindo Classification": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "TissueTypeEnum": {
      "permissible_values": {
        "Oocyte": {
          "meaning": "ncit:C12598",
          "comments": []
        },
        "Embryo": {
          "meaning": "",
          "comments": []
        },
        "Ovarian Cortical Tissue": {
          "meaning": "",
          "comments": []
        },
        "Testicular Tissue": {
          "meaning": "ncit:C33758",
          "comments": []
        },
        "Sperm": {
          "meaning": "",
          "comments": []
        },
        "Epididymal Sperm": {
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
    "MonitorMethodEnum": {
      "permissible_values": {
        "Abdominal Ultrasound": {
          "meaning": "",
          "comments": []
        },
        "Transvaginal Ultrasound Scanning (TVUS)": {
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
    "FollicleDensityUnitEnum": {
      "permissible_values": {
        "count/mm2": {
          "meaning": "",
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
    "FertilityConsultEligibilityEnum": {
      "permissible_values": {
        "Eligible": {
          "meaning": "",
          "comments": []
        },
        "Ineligible": {
          "meaning": "",
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
        "Mismatch": {
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
    "ExposureEnum": {
      "permissible_values": {
        "Alcohol": {
          "meaning": "ncit:C168296",
          "comments": []
        },
        "Marijuana": {
          "meaning": "",
          "comments": []
        },
        "Tobacco": {
          "meaning": "ncit:C18059",
          "comments": []
        },
        "Not Reported": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "AeGradeEnum": {
      "permissible_values": {
        "Clavien-Dindo, Grade I": {
          "meaning": "ncit:C121447",
          "comments": []
        },
        "Clavien-Dindo, Grade II": {
          "meaning": "ncit:C121447",
          "comments": []
        },
        "Clavien-Dindo, Grade III": {
          "meaning": "ncit:C121449",
          "comments": []
        },
        "Clavien-Dindo, Grade IIIa": {
          "meaning": "ncit:C121450",
          "comments": []
        },
        "Clavien-Dindo, Grade IIIb": {
          "meaning": "ncit:C121451",
          "comments": []
        },
        "Clavien-Dindo, Grade IV": {
          "meaning": "ncit:C121452",
          "comments": []
        },
        "Clavien-Dindo, Grade IVa": {
          "meaning": "ncit:C121453",
          "comments": []
        },
        "Clavien-Dindo, Grade IVb": {
          "meaning": "ncit:C121454",
          "comments": []
        },
        "Clavien-Dindo, Grade V": {
          "meaning": "ncit:C121455",
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
        },
        "Off Therapy": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "ProcedureEnum": {
      "permissible_values": {
        "Abdominal Myomectomy": {
          "meaning": "",
          "comments": []
        },
        "Hysterectomy": {
          "meaning": "ncit:C15256",
          "comments": []
        },
        "Hysteroscopy": {
          "meaning": "",
          "comments": []
        },
        "Oophorectomy, NOS": {
          "meaning": "ncit:C15291",
          "comments": []
        },
        "Orchiectomy": {
          "meaning": "",
          "comments": []
        },
        "Dialysis": {
          "meaning": "",
          "comments": []
        },
        "Endometrial Ablation/Resection": {
          "meaning": "",
          "comments": []
        },
        "Kidney Surgery, NOS": {
          "meaning": "",
          "comments": []
        },
        "Kidney Transplant": {
          "meaning": "",
          "comments": []
        },
        "None": {
          "meaning": "",
          "comments": []
        },
        "Oophorectomy, Complete": {
          "meaning": "",
          "comments": []
        },
        "Oophorectomy, Partial": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneal Lymph Node Dissection": {
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
    "LaboratoryTestResultUnitEnum": {
      "permissible_values": {
        "mIU/mL": {
          "meaning": "",
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
        "pg/mL": {
          "meaning": "ncit:C67327",
          "comments": []
        },
        "pmol/l": {
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