---
layout: default
title: Cancer Predisposition
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*PRE View*

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
- **Cancer Predisposition**
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The PRE view of the PCDC data model represents consensus data modeling by an international group of cancer predisposition experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Consortium for Childhood Cancer Predisposition (C3P). It is based on the collective requirements of its contributors.


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

## MedicalHistory

| Slot | Range | Description |
|---|---|---|
| `age_at_condition` | `integer` |  |
| `medical_history_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button> |  |
| `condition_other` | `string` |  |

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
| `age_at_enrollment` | `integer` |  |
| `urls` | `string` |  |

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
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `path_morph_reporting` | `string` |  |
| `morph_code_text` | `string` |  |
| `morph_code` | `string` |  |
| `morph_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-morphcodesystemenum')">MorphCodeSystemEnum</button> |  |
| `morph_code_system_version` | `string` |  |
| `diagnosis_conf_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisconfsourceenum')">DiagnosisConfSourceEnum</button> |  |
| `transformation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `transformation_conf_source` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-transformationconfsourceenum')">TransformationConfSourceEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `detection_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-detectionmethodenum')">DetectionMethodEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `assessment_reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-assessmentreasonenum')">AssessmentReasonEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `tumor_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorsizeenum')">TumorSizeEnum</button> |  |
| `tumor_number` | `decimal` |  |
| `top_code` | `string` |  |
| `top_code_text` | `string` |  |
| `top_code_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-topcodesystemenum')">TopCodeSystemEnum</button> |  |
| `top_code_system_version` | `string` |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `tnm_metastasis_m` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmmetastasismenum')">TnmMetastasisMEnum</button> |  |
| `group_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-groupsystemenum')">GroupSystemEnum</button> |  |
| `group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-groupenum')">GroupEnum</button> |  |
| `stage_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stagesystemenum')">StageSystemEnum</button> |  |
| `stage_system_version` | `string` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |
| `stage_text` | `string` |  |
| `kaposi_sarcoma_t` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-kaposisarcomatenum')">KaposiSarcomaTEnum</button> |  |
| `kaposi_sarcoma_i` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-kaposisarcomaienum')">KaposiSarcomaIEnum</button> |  |
| `kaposi_sarcoma_s` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-kaposisarcomasenum')">KaposiSarcomaSEnum</button> |  |

<div class="domain-heading">Intervention</div>

## ProtocolTreatmentModifications

| Slot | Range | Description |
|---|---|---|
| `age_at_modification` | `integer` |  |
| `modification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-modificationenum')">ModificationEnum</button> |  |
| `modification_other` | `string` |  |
| `modification_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-modificationbasisenum')">ModificationBasisEnum</button> |  |
| `reason` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reasonenum')">ReasonEnum</button> |  |
| `reason_other` | `string` |  |
| `toxicity_detail` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-toxicitydetailenum')">ToxicityDetailEnum</button> |  |
| `toxicity_detail_other` | `string` |  |
| `toxicity_immune` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `toxicity_infusion` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `original_agent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-originalagentenum')">OriginalAgentEnum</button> |  |
| `original_agent_other` | `string` |  |
| `sub_agent` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-subagentenum')">SubAgentEnum</button> |  |
| `sub_agent_other` | `string` |  |

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `age_at_rt_end` | `integer` |  |
| `protocol_radiation_therapy` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |
| `nephron_sparing_partial_nephrectomy` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `tumor_rupture` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `surgical_complications` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-surgicalcomplicationsenum')">SurgicalComplicationsEnum</button> |  |
| `surgical_complications_other` | `string` |  |

<div class="domain-heading">Monitoring</div>

## AdverseEvents

| Slot | Range | Description |
|---|---|---|
| `age_at_ae` | `integer` |  |
| `age_at_ae_resolved` | `integer` |  |
| `adverse_event` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-adverseeventenum')">AdverseEventEnum</button> |  |
| `modification_required` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `tox_delay` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `tox_high_grade_events` | `integer` |  |
| `tox_dose_reductions` | `integer` |  |

<div class="domain-heading">Testing</div>

## GeneticAnalysis

| Slot | Range | Description |
|---|---|---|
| `age_at_genetic_analysis` | `integer` |  |
| `genetic_analysis_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysismethodenum')">GeneticAnalysisMethodEnum</button> |  |
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `genomic_source_class` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-genomicsourceclassenum')">GenomicSourceClassEnum</button> |  |
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `alteration_region` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationregionenum')">AlterationRegionEnum</button> |  |
| `cytoband` | `string` |  |
| `gene` | `string` |  |
| `hgvs_coding_transcript` | `string` |  |
| `hgvs_coding` | `string` |  |
| `hgvs_protein_transcript` | `string` |  |
| `hgvs_protein` | `string` |  |
| `parental_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-parentalstatusenum')">ParentalStatusEnum</button> |  |
| `inheritance_pattern` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-inheritancepatternenum')">InheritancePatternEnum</button> |  |
| `reported_significance` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-reportedsignificanceenum')">ReportedSignificanceEnum</button> |  |
| `reported_significance_numeric` | `integer` |  |
| `reported_significance_other` | `string` |  |
| `external_ref_id_system` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-externalrefidsystemenum')">ExternalRefIdSystemEnum</button> |  |
| `external_ref_id` | `string` |  |
| `maf_numeric` | `decimal` |  |
| `vaf_numeric` | `decimal` |  |
| `allelic_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button> |  |
| `allele_count` | `decimal` |  |
| `associated_condition` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-associatedconditionenum')">AssociatedConditionEnum</button> |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestspecimenenum')">LaboratoryTestSpecimenEnum</button> |  |
| `laboratory_test_specimen_other` | `string` |  |

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
<tr><td><code>Treatment, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>ACD Variant</code></td><td><code>ncit:C152088</code></td><td></td></tr>
<tr><td><code>ALK Variant</code></td><td><code>ncit:C81945</code></td><td></td></tr>
<tr><td><code>ANKRD26 Variant</code></td><td><code>ncit:C151909</code></td><td></td></tr>
<tr><td><code>APC Variant</code></td><td><code>ncit:C164173</code></td><td></td></tr>
<tr><td><code>ASXL1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ATM Variant</code></td><td><code>ncit:C178532</code></td><td></td></tr>
<tr><td><code>ATP7B Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BAP1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BLM Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BMPR1A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BRAF Gene</code></td><td><code>ncit:C18363</code></td><td></td></tr>
<tr><td><code>BRCA1 Variant</code></td><td><code>ncit:C131467</code></td><td></td></tr>
<tr><td><code>BRCA2 Variant</code></td><td><code>ncit:C131468</code></td><td></td></tr>
<tr><td><code>BRIP1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BUB1B Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CBL Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDC73 Variant</code></td><td><code>ncit:C164265</code></td><td></td></tr>
<tr><td><code>CDH1 Variant</code></td><td><code>ncit:C165503</code></td><td></td></tr>
<tr><td><code>CDK4 Variant</code></td><td><code>ncit:C146926</code></td><td></td></tr>
<tr><td><code>CDKN1B Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDKN1C Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CDKN2A Variant</code></td><td><code>ncit:C146926</code></td><td></td></tr>
<tr><td><code>CEBPA Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CHEK2 Variant</code></td><td><code>ncit:C173450</code></td><td></td></tr>
<tr><td><code>CREBBP Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CTR9 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DDB2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DDX41 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DICER1 Variant</code></td><td><code>ncit:C164287</code></td><td></td></tr>
<tr><td><code>DIS3L2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DKC1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EP300 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EPCAM Variant</code></td><td><code>ncit:C178537</code></td><td></td></tr>
<tr><td><code>ERCC2 Variant</code></td><td><code>ncit:C165564</code></td><td></td></tr>
<tr><td><code>ERCC3 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ERCC4 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ERCC5 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ETV6 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>EZH2 Variant</code></td><td><code>ncit:C188740</code></td><td></td></tr>
<tr><td><code>FAH Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCA Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCB Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCC Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCD2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCE Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCF Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCG Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCI Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCL Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FANCM Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FBXW7 Variant</code></td><td><code>ncit:C165603</code></td><td></td></tr>
<tr><td><code>FH Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FLCN Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GATA2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GPC3 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>GPC4 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 12q</code></td><td><code>ncit:C36441</code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 15q</code></td><td><code>ncit:C36481</code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 17q</code></td><td><code>ncit:C36484</code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 1q</code></td><td><code>ncit:C36482</code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 20q</code></td><td><code>ncit:C36480</code></td><td></td></tr>
<tr><td><code>Gain of Chromosome 9q</code></td><td><code>ncit:C36483</code></td><td></td></tr>
<tr><td><code>H19 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>HRAS Variant</code></td><td><code>ncit:C140251</code></td><td></td></tr>
<tr><td><code>IGF2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ITK Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>KCNQ1OT1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>KDM3B Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>KIT Variant</code></td><td><code>ncit:C126819</code></td><td></td></tr>
<tr><td><code>KRAS Variant</code></td><td><code>ncit:C98362</code></td><td></td></tr>
<tr><td><code>LZTR1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 13q</code></td><td><code>ncit:C36497</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 14</code></td><td><code>ncit:C36490</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 1p</code></td><td><code>ncit:C36501</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 22</code></td><td><code>ncit:C36491</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome 3p</code></td><td><code>ncit:C36502</code></td><td></td></tr>
<tr><td><code>Loss of Chromosome Y</code></td><td><code>ncit:C36599</code></td><td></td></tr>
<tr><td><code>MAP2K1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MAPK1 Variant</code></td><td><code>ncit:C187408</code></td><td></td></tr>
<tr><td><code>MAX Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MEN1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MET Variant</code></td><td><code>ncit:C136286</code></td><td></td></tr>
<tr><td><code>MLH1 Variant</code></td><td><code>ncit:C178530</code></td><td></td></tr>
<tr><td><code>MPL Variant</code></td><td><code>ncit:C126823</code></td><td></td></tr>
<tr><td><code>MRAS Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MSH2 Variant</code></td><td><code>ncit:C131462</code></td><td></td></tr>
<tr><td><code>MSH6 Variant</code></td><td><code>ncit:C178531</code></td><td></td></tr>
<tr><td><code>MUTYH Variant</code></td><td><code>ncit:C169096</code></td><td></td></tr>
<tr><td><code>Monosomy 7</code></td><td><code>ncit:c36411</code></td><td></td></tr>
<tr><td><code>NBN Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NF1 Variant</code></td><td><code>ncit:C167058</code></td><td></td></tr>
<tr><td><code>NF2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NHP2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOP10 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NOTCH3 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NRAS Variant</code></td><td><code>ncit:C98439</code></td><td></td></tr>
<tr><td><code>NSD1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NTRK1 Variant</code></td><td><code>ncit:C169007</code></td><td></td></tr>
<tr><td><code>NYNRIN Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OCA2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OCA5 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>OFD1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PALB2 Variant</code></td><td><code>ncit:C178538</code></td><td></td></tr>
<tr><td><code>PARN Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PAX5 Variant</code></td><td><code>ncit:C158140</code></td><td></td></tr>
<tr><td><code>PDGFRA Variant</code></td><td><code>ncit:C107569</code></td><td></td></tr>
<tr><td><code>PDGFRB Variant</code></td><td><code>ncit:C128173</code></td><td></td></tr>
<tr><td><code>PHOX2B Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PIK3CA Variant</code></td><td><code>ncit:C98460</code></td><td></td></tr>
<tr><td><code>PMS2 Variant</code></td><td><code>ncit:C178529</code></td><td></td></tr>
<tr><td><code>POLH Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PPP1CB Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PRKAR1A Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PTCH1 Variant</code></td><td><code>ncit:C133669</code></td><td></td></tr>
<tr><td><code>PTEN Variant</code></td><td><code>ncit:C165569</code></td><td></td></tr>
<tr><td><code>PTPN11 Variant</code></td><td><code>ncit:C169022</code></td><td></td></tr>
<tr><td><code>RAD51C Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RAF1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RASA2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RB1 Variant</code></td><td><code>ncit:C169031</code></td><td></td></tr>
<tr><td><code>RBM8A Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RECQL4 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>REST Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RET Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RIT1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPL11 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPL19 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPL26 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPL35A Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPL5 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS10 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS17 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS19 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS24 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS26 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RPS7 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RRAS Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RRAS2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RTEL1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RUNX1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SAMD9 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SAMD9L Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SBDS Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SDHA Variant</code></td><td><code>ncit:C126832</code></td><td></td></tr>
<tr><td><code>SDHAF2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SDHB Variant</code></td><td><code>ncit:C169033</code></td><td></td></tr>
<tr><td><code>SDHC Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SDHD Variant</code></td><td><code>ncit:C169036</code></td><td></td></tr>
<tr><td><code>SETBP1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SH2D1A Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SHOC2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SLC24A5 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SLC45A2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SMAD4 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SMARCA4 Variant</code></td><td><code>ncit:C142126</code></td><td></td></tr>
<tr><td><code>SMARCB1 Variant</code></td><td><code>ncit:C18394</code></td><td></td></tr>
<tr><td><code>SMARCE1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SOS1 Variant</code></td><td><code>ncit:C180788</code></td><td></td></tr>
<tr><td><code>SOS2 Variant</code></td><td><code>ncit:C199592</code></td><td></td></tr>
<tr><td><code>SPRED1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>STK11 Variant</code></td><td><code>ncit:C178533</code></td><td></td></tr>
<tr><td><code>SUFU Variant</code></td><td><code>ncit:C189843</code></td><td></td></tr>
<tr><td><code>TERC Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TERT Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TINF2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TMEM127 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TP53 Variant</code></td><td><code>ncit:C118396</code></td><td></td></tr>
<tr><td><code>TRIM28 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TRIM37 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TSC1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TSC2 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TYR Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TYRP1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trisomy 17</code></td><td><code>ncit:C37865</code></td><td></td></tr>
<tr><td><code>Trisomy 7</code></td><td><code>ncit:C36476</code></td><td></td></tr>
<tr><td><code>VHL Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WRAP53 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>WT1 Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>XIAP Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>XPA Variant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>XPC Variant</code></td><td><code>ncit:C169090</code></td><td></td></tr>
<tr><td><code>del(11p15.5)</code></td><td><code>ncit:C177306</code></td><td></td></tr>
<tr><td><code>del(9p21)</code></td><td><code>ncit:C177307</code></td><td></td></tr>
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
<tr><td><code>5' UTR</code></td><td><code>ncit:C13371</code></td><td></td></tr>
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

<div id="enum-modal-associatedconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-associatedconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-associatedconditionenum')">×</button>
<h3><code>AssociatedConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ANKRD26-Related Thrombocytopenia and Leukemia Predisposition</code></td><td><code>ncit:C178387</code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia Susceptibility - PAX5</code></td><td><code>ncit:C176907</code></td><td></td></tr>
<tr><td><code>Ataxia Telangiectasia Syndrome</code></td><td><code>ncit:C2887</code></td><td></td></tr>
<tr><td><code>Ataxia-Pancytopenia Syndrome</code></td><td><code>ncit:C176909</code></td><td></td></tr>
<tr><td><code>Attenuated Familial Adenomatous Polyposis</code></td><td><code>ncit:C6729</code></td><td></td></tr>
<tr><td><code>BAP1 Tumor Predisposition Syndrome</code></td><td><code>ncit:C172639</code></td><td></td></tr>
<tr><td><code>Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia</code></td><td><code>ncit:C34415</code></td><td></td></tr>
<tr><td><code>Birt-Hogg-Dube Syndrome</code></td><td><code>ncit:C28244</code></td><td></td></tr>
<tr><td><code>Bloom Syndrome</code></td><td><code>ncit:C2903</code></td><td></td></tr>
<tr><td><code>Bohring-Opitz Syndrome</code></td><td><code>ncit:C131533</code></td><td></td></tr>
<tr><td><code>CBL Syndrome</code></td><td><code>ncit:C176942</code></td><td></td></tr>
<tr><td><code>CDC73-Related Neoplastic Syndrome</code></td><td><code>ncit:C178382</code></td><td></td></tr>
<tr><td><code>CDH1-Associated Breast Carcinoma Syndrome</code></td><td><code>ncit:C176628</code></td><td></td></tr>
<tr><td><code>CEBPA-Related Leukemia Predisposition</code></td><td><code>ncit:C178379</code></td><td></td></tr>
<tr><td><code>CHEK2-Associated Cancer Predisposition</code></td><td><code>ncit:C176588</code></td><td></td></tr>
<tr><td><code>Carney Complex</code></td><td><code>ncit:C4705</code></td><td></td></tr>
<tr><td><code>Congenital Amegakaryocytic Thrombocytopenia</code></td><td><code>ncit:C115207</code></td><td></td></tr>
<tr><td><code>Constitutional Mismatch Repair Deficiency</code></td><td><code>ncit:C130202</code></td><td></td></tr>
<tr><td><code>Costello Syndrome</code></td><td><code>ncit:C84652</code></td><td></td></tr>
<tr><td><code>Cowden Syndrome</code></td><td><code>ncit:C3076</code></td><td></td></tr>
<tr><td><code>DDX41-Related Leukemia Predisposition</code></td><td><code>ncit:C178380</code></td><td></td></tr>
<tr><td><code>DICER1 Syndrome</code></td><td><code>ncit:C123317</code></td><td></td></tr>
<tr><td><code>Diamond-Blackfan Anemia</code></td><td><code>ncit:C176913</code></td><td></td></tr>
<tr><td><code>Dyskeratosis Congenita</code></td><td><code>ncit:C111802</code></td><td></td></tr>
<tr><td><code>ETV6-Related Thrombocytopenia and Leukemia Predisposition</code></td><td><code>ncit:C178386</code></td><td></td></tr>
<tr><td><code>Familial Adenomatous Polyposis</code></td><td><code>ncit:C3339</code></td><td></td></tr>
<tr><td><code>Familial Gastrointestinal Stromal Tumor</code></td><td><code>ncit:C176906</code></td><td></td></tr>
<tr><td><code>Familial Paraganglioma-Pheochromocytoma Syndrome</code></td><td><code>ncit:C48300</code></td><td></td></tr>
<tr><td><code>Familial Platelet Disorder and AML Syndrome</code></td><td><code>ncit:C41527</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia</code></td><td><code>ncit:C62505</code></td><td></td></tr>
<tr><td><code>GATA2 Deficiency</code></td><td><code>ncit:C126349</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Melanoma</code></td><td><code>ncit:C179472</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Meningioma</code></td><td><code>ncit:C179471</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Myofibromatosis</code></td><td><code>ncit:C179470</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Neuroblastoma</code></td><td><code>ncit:C179469</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Non-Syndromic Wilms Tumor</code></td><td><code>ncit:C178392</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Papillary Renal Cell Carcinoma</code></td><td><code>ncit:C179473</code></td><td></td></tr>
<tr><td><code>Hepatolenticular Degeneration</code></td><td><code>ncit:C84756</code></td><td></td></tr>
<tr><td><code>Hereditary Breast and Ovarian Cancer Syndrome</code></td><td><code>ncit:C41527</code></td><td></td></tr>
<tr><td><code>Hereditary Leiomyomatosis and Renal Cell Carcinoma Syndrome</code></td><td><code>ncit:C41527</code></td><td></td></tr>
<tr><td><code>Hereditary Retinoblastoma</code></td><td><code>ncit:C8495</code></td><td></td></tr>
<tr><td><code>Juvenile Polyposis Syndrome</code></td><td><code>ncit:C7754</code></td><td></td></tr>
<tr><td><code>LEOPARD Syndrome</code></td><td><code>ncit:C84820</code></td><td></td></tr>
<tr><td><code>Legius Syndrome</code></td><td><code>ncit:C176941</code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Lymphoproliferative Syndrome 1/ITK Deficiency</code></td><td><code>ncit:C126344</code></td><td></td></tr>
<tr><td><code>Lynch Syndrome</code></td><td><code>ncit:C8494</code></td><td></td></tr>
<tr><td><code>MIRAGE Syndrome</code></td><td><code>ncit:C147530</code></td><td></td></tr>
<tr><td><code>MUTYH-Associated Polyposis</code></td><td><code>ncit:C96520</code></td><td></td></tr>
<tr><td><code>Mosaic Variegated Aneuploidy Syndrome 1</code></td><td><code>ncit:C128192</code></td><td></td></tr>
<tr><td><code>Mulibrey Nanism</code></td><td><code>ncit:C84906</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 1</code></td><td><code>ncit:C3225</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 2</code></td><td><code>ncit:C123329</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 4</code></td><td><code>ncit:C157449</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis Type 1</code></td><td><code>ncit:C3273</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis Type 2</code></td><td><code>ncit:C3274</code></td><td></td></tr>
<tr><td><code>Nevoid Basal Cell Carcinoma Syndrome</code></td><td><code>ncit:C2892</code></td><td></td></tr>
<tr><td><code>Nijmegen Breakage Syndrome</code></td><td><code>ncit:C4692</code></td><td></td></tr>
<tr><td><code>Noonan Syndrome</code></td><td><code>ncit:C34854</code></td><td></td></tr>
<tr><td><code>Noonan Syndrome-Like Disorder with Loose Anagen Hair</code></td><td><code>ncit:C178129</code></td><td></td></tr>
<tr><td><code>Oculocutaneous Albinism</code></td><td><code>ncit:C84941</code></td><td></td></tr>
<tr><td><code>PIK3CA-Related Overgrowth Spectrum</code></td><td><code>ncit:C178285</code></td><td></td></tr>
<tr><td><code>Perlman Syndrome</code></td><td><code>ncit:C103144</code></td><td></td></tr>
<tr><td><code>Peutz-Jeghers Syndrome</code></td><td><code>ncit:C3324</code></td><td></td></tr>
<tr><td><code>Radial Aplasia-Thrombocytopenia Syndrome</code></td><td><code>ncit:C99038</code></td><td></td></tr>
<tr><td><code>Rhabdoid Tumor Predisposition Syndrome 1</code></td><td><code>ncit:C178393</code></td><td></td></tr>
<tr><td><code>Rhabdoid Tumor Predisposition Syndrome 2</code></td><td><code>ncit:C178394</code></td><td></td></tr>
<tr><td><code>Rothmund-Thompson Syndrome</code></td><td><code>ncit:C3335</code></td><td></td></tr>
<tr><td><code>Rubinstein-Taybi Syndrome</code></td><td><code>ncit:C75466</code></td><td></td></tr>
<tr><td><code>SAMD9L-Related Myelodysplastic Syndrome Predisposition</code></td><td><code>ncit:C178390</code></td><td></td></tr>
<tr><td><code>Schinzel-Giedion Syndrome</code></td><td><code>ncit:C129308</code></td><td></td></tr>
<tr><td><code>Schwannomatosis</code></td><td><code>ncit:C6557</code></td><td></td></tr>
<tr><td><code>Shwachman-Diamond Syndrome</code></td><td><code>ncit:C61235</code></td><td></td></tr>
<tr><td><code>Simpson-Golabi-Behmel Syndrome</code></td><td><code>ncit:C131002</code></td><td></td></tr>
<tr><td><code>Sotos Syndrome</code></td><td><code>ncit:C75019</code></td><td></td></tr>
<tr><td><code>Tuberous Sclerosis</code></td><td><code>ncit:C3424</code></td><td></td></tr>
<tr><td><code>Tyrosinemia Type I</code></td><td><code>ncit:C98641</code></td><td></td></tr>
<tr><td><code>Von Hippel-Lindau Syndrome</code></td><td><code>ncit:C3105</code></td><td></td></tr>
<tr><td><code>WT1 Syndromes</code></td><td><code>ncit:C131006</code></td><td></td></tr>
<tr><td><code>Weaver Syndrome</code></td><td><code>ncit:C125599</code></td><td></td></tr>
<tr><td><code>X-linked Lymphoproliferative Syndrome</code></td><td><code>ncit:C61246</code></td><td></td></tr>
<tr><td><code>Xeroderma Pigmentosum</code></td><td><code>ncit:C3452</code></td><td></td></tr>
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
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Unrelated to Disease or Treatment</code></td><td><code>ncit:C17649</code></td><td>(cns) ConsortiumNote: Deceased-due to other causes.<br>(fa) ConsortiumNote: Deceased-due to other causes.</td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(cns) ConsortiumNote: Deceased-causes unavailable.<br>(fa) ConsortiumNote: Deceased-causes unavailable.</td></tr>
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
<tr><td><code>C3P</code></td><td><code>ncit:C192767</code></td><td></td></tr>
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
<tr><td><code>Audiogram</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Biopsy</code></td><td><code>ncit:C15189</code></td><td></td></tr>
<tr><td><code>Blood Work</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Scan</code></td><td><code>ncit:C17646</code></td><td></td></tr>
<tr><td><code>CT Scan</code></td><td><code>ncit:C17204</code></td><td></td></tr>
<tr><td><code>Colonoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Echocardiogram</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flexible Fiberoptic Sigmoidoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Flexible sigmoidoscopy/colonoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Gallium Scan</code></td><td><code>ncit:C38087</code></td><td></td></tr>
<tr><td><code>Imaging, NOS</code></td><td><code>ncit:C17369</code></td><td></td></tr>
<tr><td><code>Lymphangiogram</code></td><td><code>ncit:C16805</code></td><td></td></tr>
<tr><td><code>MRI</code></td><td><code>ncit:C16809</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>PET Scan</code></td><td><code>ncit:C17007</code></td><td></td></tr>
<tr><td><code>PET-CT</code></td><td><code>ncit:C103512</code></td><td></td></tr>
<tr><td><code>PET-MRI</code></td><td><code>ncit:C103514</code></td><td></td></tr>
<tr><td><code>Physical Examination</code></td><td><code>ncit:C20989</code></td><td></td></tr>
<tr><td><code>Staging Laparotomy</code></td><td><code>ncit:C185327</code></td><td></td></tr>
<tr><td><code>Ultrasound</code></td><td><code>ncit:C64384</code></td><td></td></tr>
<tr><td><code>Upper endoscopy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urine Test</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Clinical</code></td><td><code>ncit:C15607</code></td><td></td></tr>
<tr><td><code>Molecular</code></td><td><code>ncit:C20826</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-diagnosisconfsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diagnosisconfsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diagnosisconfsourceenum')">×</button>
<h3><code>DiagnosisConfSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Death Certificate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Medical Record Note</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pathology Report</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Self-Report</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>PRE</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Abdominal Wall</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Acetabulum</code></td><td><code>ncit:C32042</code></td><td></td></tr>
<tr><td><code>Adrenal Gland</code></td><td><code>ncit:C12666</code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Ankle</code></td><td><code>ncit:C32078</code></td><td></td></tr>
<tr><td><code>Ankle Joint</code></td><td><code>ncit:C32078</code></td><td></td></tr>
<tr><td><code>Anterior Skull Base</code></td><td><code>ncit:C180372</code></td><td></td></tr>
<tr><td><code>Anus</code></td><td><code>ncit:C43362</code></td><td></td></tr>
<tr><td><code>Appendix</code></td><td><code>ncit:C12380</code></td><td></td></tr>
<tr><td><code>Ascitic Fluid</code></td><td><code>ncit:C159203</code></td><td></td></tr>
<tr><td><code>Axilla</code></td><td><code>ncit:C12674</code></td><td></td></tr>
<tr><td><code>Axillary Nodes</code></td><td><code>ncit:C12904</code></td><td></td></tr>
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
<tr><td><code>Celiac Nodes</code></td><td><code>ncit:C65166</code></td><td></td></tr>
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Cervical Nodes</code></td><td><code>ncit:C32298</code></td><td></td></tr>
<tr><td><code>Cervical Spine</code></td><td><code>ncit:C69313</code></td><td></td></tr>
<tr><td><code>Cervical Vertebra</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Cheek</code></td><td><code>ncit:C13070</code></td><td></td></tr>
<tr><td><code>Chest</code></td><td><code>ncit:C25389</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Clavicle</code></td><td><code>ncit:C24203</code></td><td></td></tr>
<tr><td><code>Coccyx</code></td><td><code>ncit:C12696</code></td><td></td></tr>
<tr><td><code>Colon</code></td><td><code>ncit:C12382</code></td><td></td></tr>
<tr><td><code>Cutaneous</code></td><td><code>ncit:C13316</code></td><td></td></tr>
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
<tr><td><code>Eyelid</code></td><td><code>ncit:C12713</code></td><td></td></tr>
<tr><td><code>Face</code></td><td><code>ncit:C13071</code></td><td></td></tr>
<tr><td><code>Fallopian Tube</code></td><td><code>ncit:C12403</code></td><td></td></tr>
<tr><td><code>Female Reproductive System Part</code></td><td><code>ncit:C13039</code></td><td></td></tr>
<tr><td><code>Femur</code></td><td><code>ncit:C12717</code></td><td></td></tr>
<tr><td><code>Fibula</code></td><td><code>ncit:C12718</code></td><td></td></tr>
<tr><td><code>Fibular Head</code></td><td><code>ncit:C32719</code></td><td></td></tr>
<tr><td><code>Finger</code></td><td><code>ncit:C32608</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Foot Joint</code></td><td><code>ncit:C32623</code></td><td></td></tr>
<tr><td><code>Foot Phalanges</code></td><td><code>ncit:C52772</code></td><td></td></tr>
<tr><td><code>Forearm</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Frontal Bone</code></td><td><code>ncit:C32635</code></td><td></td></tr>
<tr><td><code>Frontal Cortex</code></td><td><code>ncit:C12352</code></td><td></td></tr>
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
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Iliac Crest</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Inferior Limb</code></td><td><code>ncit:C12982</code></td><td></td></tr>
<tr><td><code>Infraclavicular Lymph Node</code></td><td><code>ncit:C63705</code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine and Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Inguinal Nodes</code></td><td><code>ncit:C32801</code></td><td></td></tr>
<tr><td><code>Intra-Abdominal</code></td><td><code>ncit:C12726</code></td><td></td></tr>
<tr><td><code>Intraperitoneal</code></td><td><code>ncit:C13352</code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code>ncit:C105579</code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Knee</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Knee Joint</code></td><td><code>ncit:C32899</code></td><td></td></tr>
<tr><td><code>Lacrimal Bone</code></td><td><code>ncit:C32906</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Liver/Biliary Tract</code></td><td><code>ncit:C12678</code></td><td></td></tr>
<tr><td><code>Lower Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Extremity</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lower Leg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Limb, NOS</code></td><td><code>ncit:C12742</code></td><td></td></tr>
<tr><td><code>Lower Spine</code></td><td><code>ncit:C69314</code></td><td></td></tr>
<tr><td><code>Lumbar Vertebra</code></td><td><code>ncit:C45874</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Mandible</code></td><td><code>ncit:C12290</code></td><td></td></tr>
<tr><td><code>Maxilla</code></td><td><code>ncit:C26470</code></td><td></td></tr>
<tr><td><code>Mediastinum</code></td><td><code>ncit:C6634</code></td><td></td></tr>
<tr><td><code>Meninges</code></td><td><code>ncit:C12348</code></td><td></td></tr>
<tr><td><code>Mesenteric Nodes</code></td><td><code>ncit:C77641</code></td><td></td></tr>
<tr><td><code>Metacarpus</code></td><td><code>ncit:C12751</code></td><td></td></tr>
<tr><td><code>Metatarsus</code></td><td><code>ncit:C12752</code></td><td></td></tr>
<tr><td><code>Middle Ear</code></td><td><code>ncit:C12274</code></td><td></td></tr>
<tr><td><code>Nasal Bone</code></td><td><code>ncit:C33157</code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasal Cavity and Paranasal Sinuses</code></td><td><code>ncit:C12763</code></td><td></td></tr>
<tr><td><code>Nasal Septum</code></td><td><code>ncit:C33160</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Occipital Bone</code></td><td><code>ncit:C12757</code></td><td></td></tr>
<tr><td><code>Omentum/Peritoneum</code></td><td><code>ncit:C33209</code></td><td></td></tr>
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
<tr><td><code>Parietal Bone</code></td><td><code>ncit:C12766</code></td><td></td></tr>
<tr><td><code>Parietal Cortex</code></td><td><code>ncit:C12354</code></td><td></td></tr>
<tr><td><code>Parotid</code></td><td><code>ncit:C12427</code></td><td></td></tr>
<tr><td><code>Patella</code></td><td><code>ncit:C33282</code></td><td></td></tr>
<tr><td><code>Pectoral Nodes</code></td><td><code>ncit:C120322</code></td><td></td></tr>
<tr><td><code>Pelvis, Ilium</code></td><td><code>ncit:C32765</code></td><td></td></tr>
<tr><td><code>Pelvis, Ischium</code></td><td><code>ncit:C32884</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Pelvis, Sacrum</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Penis</code></td><td><code>ncit:C12409</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code>ncit:C33301</code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
<tr><td><code>Pineal</code></td><td><code>ncit:C12398</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Pleural Effusion</code></td><td><code>ncit:C3331</code></td><td></td></tr>
<tr><td><code>Popliteal Nodes</code></td><td><code>ncit:C53146</code></td><td></td></tr>
<tr><td><code>Preauricular Lymph Node</code></td><td><code>ncit:C103429</code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Radius Bone</code></td><td><code>ncit:C12777</code></td><td></td></tr>
<tr><td><code>Rectum</code></td><td><code>ncit:C12390</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Rib</code></td><td><code>ncit:C12782</code></td><td></td></tr>
<tr><td><code>Sacral Region</code></td><td><code>ncit:C33508</code></td><td></td></tr>
<tr><td><code>Sacrococcygeal</code></td><td><code>ncit:C33506</code></td><td></td></tr>
<tr><td><code>Salivary Gland</code></td><td><code>ncit:C12426</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Scapula</code></td><td><code>ncit:C12744</code></td><td></td></tr>
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
<tr><td><code>Superior Maxilla</code></td><td><code>ncit:C33682</code></td><td></td></tr>
<tr><td><code>Supraclavicular Lymph Node</code></td><td><code>ncit:C12903</code></td><td></td></tr>
<tr><td><code>Suprasellar/Neurohypophyseal</code></td><td><code>ncit:C42602</code></td><td></td></tr>
<tr><td><code>Talus</code></td><td><code>ncit:C52799</code></td><td></td></tr>
<tr><td><code>Tarsal Bone</code></td><td><code>ncit:C12796</code></td><td></td></tr>
<tr><td><code>Temporal Bone</code></td><td><code>ncit:C12797</code></td><td></td></tr>
<tr><td><code>Temporal Cortex</code></td><td><code>ncit:C12353</code></td><td></td></tr>
<tr><td><code>Testis</code></td><td><code>ncit:C12412</code></td><td></td></tr>
<tr><td><code>Thalamus</code></td><td><code>ncit:C12459</code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Thoracic Vertebra</code></td><td><code>ncit:C12798</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Thyroid</code></td><td><code>ncit:C12400</code></td><td></td></tr>
<tr><td><code>Tibia</code></td><td><code>ncit:C12800</code></td><td></td></tr>
<tr><td><code>Toe</code></td><td><code>ncit:C33788</code></td><td></td></tr>
<tr><td><code>Tonsil</code></td><td><code>ncit:C12802</code></td><td></td></tr>
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

<div id="enum-modal-externalrefidsystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">×</button>
<h3><code>ExternalRefIdSystemEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>COSMIC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ClinGen</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genome Aggregation Database (gnomAD)</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Cytogenetics, NOS</code></td><td><code>ncit:C16487</code></td><td></td></tr>
<tr><td><code>DNA Methylation, Array</code></td><td><code>ncit:C165222</code></td><td></td></tr>
<tr><td><code>DNA Methylation, NOS</code></td><td><code>ncit:C16848</code></td><td></td></tr>
<tr><td><code>Expression Profiling, Nanostring</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Genotyping, NOS</code></td><td><code>ncit:C45447</code></td><td></td></tr>
<tr><td><code>PCR, MLPA</code></td><td><code>ncit:C116161</code></td><td></td></tr>
<tr><td><code>PCR, RT-PCR</code></td><td><code>ncit:C18136</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, NOS</code></td><td><code>ncit:C101293</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Targeted DNA Panel</code></td><td><code>ncit:C158253</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Total RNA</code></td><td><code>ncit:C124261</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Exome</code></td><td><code>ncit:C101295</code></td><td></td></tr>
<tr><td><code>Sequencing, NGS, Whole Genome</code></td><td><code>ncit:C101294</code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, Capillary Electrophoresis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, Gel Electrophoresis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Sequencing, Sanger, NOS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Saliva</code></td><td><code>ncit:C174119</code></td><td>(pre) ConsortiumNote: Map to Buccal Swab/Saliva</td></tr>
<tr><td><code>Primary Tumor</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Metastatic Tumor</code></td><td><code>ncit:C3261</code></td><td></td></tr>
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

<div id="enum-modal-groupenum" class="enum-modal" onclick="closeEnumModal('enum-modal-groupenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-groupenum')">×</button>
<h3><code>GroupEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
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
<tr><td><code>Reese-Ellsworth</code></td><td><code>ncit:C123333</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-inheritancepatternenum" class="enum-modal" onclick="closeEnumModal('enum-modal-inheritancepatternenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-inheritancepatternenum')">×</button>
<h3><code>InheritancePatternEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Autosomal Dominant</code></td><td><code>ncit:C94245</code></td><td></td></tr>
<tr><td><code>Autosomal Recessive</code></td><td><code>ncit:C94246</code></td><td></td></tr>
<tr><td><code>X-Linked Dominant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X-linked Recessive</code></td><td><code>ncit:C94247</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-kaposisarcomaienum" class="enum-modal" onclick="closeEnumModal('enum-modal-kaposisarcomaienum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-kaposisarcomaienum')">×</button>
<h3><code>KaposiSarcomaIEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>I0</code></td><td><code>ncit:C134979</code></td><td></td></tr>
<tr><td><code>I1</code></td><td><code>ncit:C134980</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-kaposisarcomasenum" class="enum-modal" onclick="closeEnumModal('enum-modal-kaposisarcomasenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-kaposisarcomasenum')">×</button>
<h3><code>KaposiSarcomaSEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>S0</code></td><td><code>ncit:C134982</code></td><td></td></tr>
<tr><td><code>S1</code></td><td><code>ncit:C134983</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-kaposisarcomatenum" class="enum-modal" onclick="closeEnumModal('enum-modal-kaposisarcomatenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-kaposisarcomatenum')">×</button>
<h3><code>KaposiSarcomaTEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>T0</code></td><td><code>ncit:C169110</code></td><td></td></tr>
<tr><td><code>T1</code></td><td><code>ncit:C134976</code></td><td></td></tr>
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
<tr><td><code>Cell Free DNA BCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>K2EDTA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Saliva</code></td><td><code>ncit:C174119</code></td><td></td></tr>
<tr><td><code>Stool Sample</code></td><td><code>ncit:C189125</code></td><td></td></tr>
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

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3><code>MedicalHistoryConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ANKRD26-Related Thrombocytopenia and Leukemia Predisposition</code></td><td><code>ncit:C178387</code></td><td></td></tr>
<tr><td><code>Acute Lymphoblastic Leukemia Susceptibility - PAX5</code></td><td><code>ncit:C176907</code></td><td></td></tr>
<tr><td><code>Adenomatous Polyposis Coli</code></td><td><code>ncit:C17687</code></td><td></td></tr>
<tr><td><code>Ataxia Telangiectasia Syndrome</code></td><td><code>ncit:C2887</code></td><td></td></tr>
<tr><td><code>Ataxia-Pancytopenia Syndrome</code></td><td><code>ncit:C176909</code></td><td></td></tr>
<tr><td><code>Attenuated Familial Adenomatous Polyposis</code></td><td><code>ncit:C6729</code></td><td></td></tr>
<tr><td><code>BAP1 Tumor Predisposition Syndrome</code></td><td><code>ncit:C172639</code></td><td></td></tr>
<tr><td><code>Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia</code></td><td><code>ncit:C34415</code></td><td></td></tr>
<tr><td><code>Birt-Hogg-Dube Syndrome</code></td><td><code>ncit:C28244</code></td><td></td></tr>
<tr><td><code>Bloom Syndrome</code></td><td><code>ncit:C2903</code></td><td></td></tr>
<tr><td><code>Bohring-Opitz Syndrome</code></td><td><code>ncit:C131533</code></td><td></td></tr>
<tr><td><code>CBL Syndrome</code></td><td><code>ncit:C176942</code></td><td></td></tr>
<tr><td><code>CDC73-Related Neoplastic Syndrome</code></td><td><code>ncit:C178382</code></td><td></td></tr>
<tr><td><code>CDH1-Associated Breast Carcinoma Syndrome</code></td><td><code>ncit:C176628</code></td><td></td></tr>
<tr><td><code>CEBPA-Related Leukemia Predisposition</code></td><td><code>ncit:C178379</code></td><td></td></tr>
<tr><td><code>CHEK2-Associated Cancer Predisposition</code></td><td><code>ncit:C176588</code></td><td></td></tr>
<tr><td><code>Carney Complex</code></td><td><code>ncit:C4705</code></td><td></td></tr>
<tr><td><code>Congenital Amegakaryocytic Thrombocytopenia</code></td><td><code>ncit:C115207</code></td><td></td></tr>
<tr><td><code>Constitutional Mismatch Repair Deficiency</code></td><td><code>ncit:C130202</code></td><td></td></tr>
<tr><td><code>Costello Syndrome</code></td><td><code>ncit:C84652</code></td><td></td></tr>
<tr><td><code>Cowden Syndrome</code></td><td><code>ncit:C3076</code></td><td></td></tr>
<tr><td><code>DDX41-Related Leukemia Predisposition</code></td><td><code>ncit:C178380</code></td><td></td></tr>
<tr><td><code>DICER1 Syndrome</code></td><td><code>ncit:C123317</code></td><td></td></tr>
<tr><td><code>Diamond-Blackfan Anemia</code></td><td><code>ncit:C61236</code></td><td></td></tr>
<tr><td><code>Dyskeratosis Congenita</code></td><td><code>ncit:C111802</code></td><td></td></tr>
<tr><td><code>ETV6-Related Thrombocytopenia and Leukemia Predisposition</code></td><td><code>ncit:C178386</code></td><td></td></tr>
<tr><td><code>Familial Adenomatous Polyposis</code></td><td><code>ncit:C3339</code></td><td></td></tr>
<tr><td><code>Familial Gastrointestinal Stromal Tumor</code></td><td><code>ncit:C176906</code></td><td></td></tr>
<tr><td><code>Familial Paraganglioma-Pheochromocytoma Syndrome</code></td><td><code>ncit:C190373</code></td><td></td></tr>
<tr><td><code>Familial Platelet Disorder and AML Syndrome</code></td><td><code>ncit:C162696</code></td><td></td></tr>
<tr><td><code>Fanconi Anemia</code></td><td><code>ncit:C62505</code></td><td></td></tr>
<tr><td><code>GATA2 Deficiency</code></td><td><code>ncit:C126349</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Melanoma</code></td><td><code>ncit:C179472</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Meningioma</code></td><td><code>ncit:C179471</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Myofibromatosis</code></td><td><code>ncit:C179470</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Neuroblastoma</code></td><td><code>ncit:C179469</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Non-Syndromic Wilms Tumor</code></td><td><code>ncit:C178392</code></td><td></td></tr>
<tr><td><code>Genetic Predisposition to Papillary Renal Cell Carcinoma</code></td><td><code>ncit:C179473</code></td><td></td></tr>
<tr><td><code>Hepatolenticular Degeneration</code></td><td><code>ncit:C84756</code></td><td></td></tr>
<tr><td><code>Hereditary Breast and Ovarian Cancer Syndrome</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hereditary Leiomyomatosis and Renal Cell Carcinoma Syndrome</code></td><td><code>ncit:C51302</code></td><td></td></tr>
<tr><td><code>Hereditary Retinoblastoma</code></td><td><code>ncit:C8495</code></td><td></td></tr>
<tr><td><code>Juvenile Polyposis Syndrome</code></td><td><code>ncit:C7754</code></td><td></td></tr>
<tr><td><code>LEOPARD Syndrome</code></td><td><code>ncit:C84820</code></td><td></td></tr>
<tr><td><code>Legius Syndrome</code></td><td><code>ncit:C176941</code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Lymphoproliferative Syndrome 1/ITK Deficiency</code></td><td><code>ncit:C126344</code></td><td></td></tr>
<tr><td><code>Lynch Syndrome</code></td><td><code>ncit:C8494</code></td><td></td></tr>
<tr><td><code>MIRAGE Syndrome</code></td><td><code>ncit:C147530</code></td><td></td></tr>
<tr><td><code>MUTYH-Associated Polyposis</code></td><td><code>ncit:C96520</code></td><td></td></tr>
<tr><td><code>Mosaic Variegated Aneuploidy Syndrome 1</code></td><td><code>ncit:C128192</code></td><td></td></tr>
<tr><td><code>Mulibrey Nanism</code></td><td><code>ncit:C84906</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 1</code></td><td><code>ncit:C3225</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 2</code></td><td><code>ncit:C123329</code></td><td></td></tr>
<tr><td><code>Multiple Endocrine Neoplasia Type 4</code></td><td><code>ncit:C157449</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis Type 1</code></td><td><code>ncit:C3273</code></td><td></td></tr>
<tr><td><code>Neurofibromatosis Type 2</code></td><td><code>ncit:C3274</code></td><td></td></tr>
<tr><td><code>Nevoid Basal Cell Carcinoma Syndrome</code></td><td><code>ncit:C2892</code></td><td></td></tr>
<tr><td><code>Nijmegen Breakage Syndrome</code></td><td><code>ncit:C4692</code></td><td></td></tr>
<tr><td><code>Noonan Syndrome</code></td><td><code>ncit:C34854</code></td><td></td></tr>
<tr><td><code>Noonan Syndrome-Like Disorder with Loose Anagen Hair</code></td><td><code>ncit:C178129</code></td><td></td></tr>
<tr><td><code>Oculocutaneous Albinism</code></td><td><code>ncit:C84941</code></td><td></td></tr>
<tr><td><code>PIK3CA-Related Overgrowth Spectrum</code></td><td><code>ncit:C178285</code></td><td></td></tr>
<tr><td><code>Perlman Syndrome</code></td><td><code>ncit:C103144</code></td><td></td></tr>
<tr><td><code>Peutz-Jeghers Syndrome</code></td><td><code>ncit:C43324</code></td><td></td></tr>
<tr><td><code>Radial Aplasia-Thrombocytopenia Syndrome</code></td><td><code>ncit:C99038</code></td><td></td></tr>
<tr><td><code>Rhabdoid Tumor Predisposition Syndrome 1</code></td><td><code>ncit:C178393</code></td><td></td></tr>
<tr><td><code>Rhabdoid Tumor Predisposition Syndrome 2</code></td><td><code>ncit:C178394</code></td><td></td></tr>
<tr><td><code>Rubinstein-Taybi Syndrome</code></td><td><code>ncit:C75466</code></td><td></td></tr>
<tr><td><code>SAMD9L-Related Myelodysplastic Syndrome Predisposition</code></td><td><code>ncit:C178390</code></td><td></td></tr>
<tr><td><code>Schinzel-Giedion Syndrome</code></td><td><code>ncit:C129308</code></td><td></td></tr>
<tr><td><code>Schwannomatosis</code></td><td><code>ncit:C6557</code></td><td></td></tr>
<tr><td><code>Shwachman-Diamond Syndrome</code></td><td><code>ncit:C61235</code></td><td></td></tr>
<tr><td><code>Simpson-Golabi-Behmel Syndrome</code></td><td><code>ncit:C131002</code></td><td></td></tr>
<tr><td><code>Sotos Syndrome</code></td><td><code>ncit:C75019</code></td><td></td></tr>
<tr><td><code>Tuberous Sclerosis</code></td><td><code>ncit:C3424</code></td><td></td></tr>
<tr><td><code>Tyrosinemia Type I</code></td><td><code>ncit:C98641</code></td><td></td></tr>
<tr><td><code>Von Hippel-Lindau Syndrome</code></td><td><code>ncit:C3105</code></td><td></td></tr>
<tr><td><code>WT1 Syndromes</code></td><td><code>ncit:C131006</code></td><td></td></tr>
<tr><td><code>Weaver Syndrome</code></td><td><code>ncit:C125599</code></td><td></td></tr>
<tr><td><code>X-linked Lymphoproliferative Syndrome</code></td><td><code>ncit:C61246</code></td><td></td></tr>
<tr><td><code>Xeroderma Pigmentosum</code></td><td><code>ncit:C3452</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Mosaic</code></td><td><code>ncit:C88144</code></td><td></td></tr>
<tr><td><code>Paternally Inherited</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Not Evaluated</code></td><td><code>ncit:C103424</code></td><td></td></tr>
<tr><td><code>Present</code></td><td><code>ncit:C25566</code></td><td></td></tr>
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
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Limb</code></td><td><code>ncit:C12429</code></td><td></td></tr>
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
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Local Extension</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Metastatic</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
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
<tr><td><code>AJCC, v6 &gt;&gt; Stage 0</code></td><td><code>C90529</code></td><td></td></tr>
<tr><td><code>AJCC, v6 &gt;&gt; Stage 1</code></td><td><code>C90529</code></td><td></td></tr>
<tr><td><code>AJCC, v6 &gt;&gt; Stage 2</code></td><td><code>C90529</code></td><td></td></tr>
<tr><td><code>AJCC, v6 &gt;&gt; Stage 3</code></td><td><code>C90529</code></td><td></td></tr>
<tr><td><code>AJCC, v6 &gt;&gt; Stage 4</code></td><td><code>C90529</code></td><td></td></tr>
<tr><td><code>AJCC, v7 &gt;&gt; Stage 0</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC, v7 &gt;&gt; Stage 1</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC, v7 &gt;&gt; Stage 2</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC, v7 &gt;&gt; Stage 3</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC, v7 &gt;&gt; Stage 4</code></td><td><code>ncit:C90530</code></td><td></td></tr>
<tr><td><code>AJCC, v8 &gt;&gt; Stage 0</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>AJCC, v8 &gt;&gt; Stage 1</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>AJCC, v8 &gt;&gt; Stage 2</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>AJCC, v8 &gt;&gt; Stage 3</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>AJCC, v8 &gt;&gt; Stage 4</code></td><td><code>ncit:C132248</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 1</code></td><td><code>ncit:C8071</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 2</code></td><td><code>ncit:C8116</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 3</code></td><td><code>ncit:C8129</code></td><td></td></tr>
<tr><td><code>Ann Arbor &gt;&gt; Stage 4</code></td><td><code>ncit:C8142</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Liver Tumor Staging System &gt;&gt; Stage 1</code></td><td><code>ncit:C177630</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Liver Tumor Staging System &gt;&gt; Stage 2</code></td><td><code>ncit:C177630</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Liver Tumor Staging System &gt;&gt; Stage 3</code></td><td><code>ncit:C177630</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Liver Tumor Staging System &gt;&gt; Stage 4</code></td><td><code>ncit:C177630</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Neuroblastoma Risk Group Staging System &gt;&gt; Stage L1</code></td><td><code>ncit:C177631</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Neuroblastoma Risk Group Staging System &gt;&gt; Stage L2</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Neuroblastoma Risk Group Staging System &gt;&gt; Stage M</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Neuroblastoma Risk Group Staging System &gt;&gt; Stage MS</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System &gt;&gt; Stage 1</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System &gt;&gt; Stage 2</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System &gt;&gt; Stage 3</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System &gt;&gt; Stage 4</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Renal Cancer Staging System &gt;&gt; Stage 5</code></td><td><code>ncit:C177632</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Retinoblastoma Risk Group Staging System &gt;&gt; High Risk</code></td><td><code>ncit:C102401</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Retinoblastoma Risk Group Staging System &gt;&gt; Intermediate Risk</code></td><td><code>ncit:C102402</code></td><td></td></tr>
<tr><td><code>Children's Oncology Group Retinoblastoma Risk Group Staging System &gt;&gt; Low Risk</code></td><td><code>ncit:C102403</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System &gt;&gt; Stage 1</code></td><td><code>ncit:C198025</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System &gt;&gt; Stage 2</code></td><td><code>ncit:C198025</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System &gt;&gt; Stage 3</code></td><td><code>ncit:C198025</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System &gt;&gt; Stage 4</code></td><td><code>ncit:C198025</code></td><td></td></tr>
<tr><td><code>Childrens Oncology Group/National Wilms Tumor Study Group Staging System &gt;&gt; Stage 5</code></td><td><code>ncit:C198025</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 1</code></td><td><code>ncit:C27966</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 2</code></td><td><code>ncit:C28054</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 3</code></td><td><code>ncit:C27970</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 4</code></td><td><code>ncit:C27971</code></td><td></td></tr>
<tr><td><code>COG &gt;&gt; Stage 4S</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Enneking Staging System &gt;&gt; Stage 1a</code></td><td><code>ncit:C146701</code></td><td></td></tr>
<tr><td><code>Enneking Staging System &gt;&gt; Stage 1b</code></td><td><code>ncit:C146702</code></td><td></td></tr>
<tr><td><code>Enneking Staging System &gt;&gt; Stage 2a</code></td><td><code>ncit:C146703</code></td><td></td></tr>
<tr><td><code>Enneking Staging System &gt;&gt; Stage 2b</code></td><td><code>ncit:C146704</code></td><td></td></tr>
<tr><td><code>Enneking Staging System &gt;&gt; Stage 3</code></td><td><code>ncit:C146705</code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 4s</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>International Society of Pediatric Oncology Staging System &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>International Society of Pediatric Oncology Staging System &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>International Society of Pediatric Oncology Staging System &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>International Society of Pediatric Oncology Staging System &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>International Society of Pediatric Oncology Staging System &gt;&gt; Stage 5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 1</code></td><td><code>ncit:C141180</code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 1E</code></td><td><code>ncit:C141181</code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 2</code></td><td><code>ncit:C141182</code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 2E</code></td><td><code>ncit:C141183</code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 3</code></td><td><code>ncit:C141186</code></td><td></td></tr>
<tr><td><code>Lugano Stage &gt;&gt; Stage 4</code></td><td><code>ncit:C141187</code></td><td></td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 1992 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2005-COG &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, 2017 &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group I</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group II</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group III</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>PRETEXT, NOS &gt;&gt; Group IV</code></td><td><code></code></td><td>(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'</td></tr>
<tr><td><code>St. Jude Stage &gt;&gt; Stage 1</code></td><td><code>C141218</code></td><td></td></tr>
<tr><td><code>St. Jude Stage &gt;&gt; Stage 2</code></td><td><code>C141219</code></td><td></td></tr>
<tr><td><code>St. Jude Stage &gt;&gt; Stage 3</code></td><td><code>C141220</code></td><td></td></tr>
<tr><td><code>St. Jude Stage &gt;&gt; Stage 4</code></td><td><code>C141221</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>International Society of Pediatric Oncology Staging System</code></td><td><code>ncit:C140270</code></td><td></td></tr>
<tr><td><code>Lugano Stage</code></td><td><code>ncit:C141147</code></td><td></td></tr>
<tr><td><code>PRETEXT Staging System</code></td><td><code>ncit:C141133</code></td><td></td></tr>
<tr><td><code>Pediatric Oncology Group Neuroblastoma Staging System</code></td><td><code>ncit:C85423</code></td><td></td></tr>
<tr><td><code>St. Jude Stage</code></td><td><code>ncit:C141216</code></td><td></td></tr>
<tr><td><code>Toronto Childhood Cancer Stage Guidelines</code></td><td><code>ncit:C197985</code></td><td></td></tr>
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
<tr><td><code>C3P Registry</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-surgicalcomplicationsenum" class="enum-modal" onclick="closeEnumModal('enum-modal-surgicalcomplicationsenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-surgicalcomplicationsenum')">×</button>
<h3><code>SurgicalComplicationsEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bleed</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intra-operative Tumor Rupture</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Urgent Surgery for ICP</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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

<div id="enum-modal-transformationconfsourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-transformationconfsourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-transformationconfsourceenum')">×</button>
<h3><code>TransformationConfSourceEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Confirmed Based On Pathology</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Applicable</code></td><td><code>ncit:C48660</code></td><td></td></tr>
<tr><td><code>Suspected Based On Imaging</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>&lt;0.5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0.5-1 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>1-5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&lt;=5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&lt;=3mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;3mm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
    "pre": {
      "name": "pre",
      "title": "Cancer Predisposition",
      "description": "The PRE view of the PCDC data model represents consensus data modeling by an international group of cancer predisposition experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Consortium for Childhood Cancer Predisposition (C3P). It is based on the collective requirements of its contributors."
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
    "MedicalHistory": {
      "slots": [
        "age_at_condition",
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
        "laboratory_test_specimen",
        "laboratory_test_specimen_other"
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
        "genomic_source_class",
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "alteration_region",
        "cytoband",
        "gene",
        "hgvs_coding_transcript",
        "hgvs_coding",
        "hgvs_protein_transcript",
        "hgvs_protein",
        "parental_status",
        "inheritance_pattern",
        "reported_significance",
        "reported_significance_numeric",
        "reported_significance_other",
        "external_ref_id_system",
        "external_ref_id",
        "maf_numeric",
        "vaf_numeric",
        "allelic_state",
        "allele_count",
        "associated_condition"
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
        "path_morph_reporting",
        "morph_code_text",
        "morph_code",
        "morph_code_system",
        "morph_code_system_version",
        "diagnosis_conf_source",
        "transformation",
        "transformation_conf_source"
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
        "tnm_metastasis_m",
        "group_system",
        "group",
        "stage_system",
        "stage_system_version",
        "stage",
        "stage_text",
        "kaposi_sarcoma_t",
        "kaposi_sarcoma_i",
        "kaposi_sarcoma_s"
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
        "assessment_reason",
        "disease_site",
        "site_other",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "tumor_size",
        "tumor_number",
        "top_code",
        "top_code_text",
        "top_code_system",
        "top_code_system_version"
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
        "procedure_site",
        "site_other",
        "margins",
        "nephron_sparing_partial_nephrectomy",
        "tumor_rupture",
        "surgical_complications",
        "surgical_complications_other"
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
    "ProtocolTreatmentModifications": {
      "slots": [
        "age_at_modification",
        "modification",
        "modification_other",
        "modification_basis",
        "reason",
        "reason_other",
        "toxicity_detail",
        "toxicity_detail_other",
        "toxicity_immune",
        "toxicity_infusion",
        "original_agent",
        "original_agent_other",
        "sub_agent",
        "sub_agent_other"
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
        "protocol_radiation_therapy"
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
    "AdverseEvents": {
      "slots": [
        "age_at_ae",
        "age_at_ae_resolved",
        "adverse_event",
        "modification_required",
        "tox_delay",
        "tox_high_grade_events",
        "tox_dose_reductions"
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
    "modification_required": {
      "slot_uri": "ncit:C55606",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
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
    "allele_count": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
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
    "genetic_analysis_specimen": {
      "slot_uri": "ncit:C70713",
      "range": "GeneticAnalysisSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "surgical_complications_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "surgical_complications": {
      "slot_uri": "ncit:C164157",
      "range": "SurgicalComplicationsEnum",
      "comments": [],
      "annotations": {}
    },
    "modification_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "original_agent_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
    },
    "modification": {
      "slot_uri": "ncit:C185632",
      "range": "ModificationEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "npc"
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
    "toxicity_infusion": {
      "slot_uri": "ncit:C185649",
      "range": "YesNoEnum",
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
    "tumor_rupture": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "toxicity_detail_other": {
      "slot_uri": "",
      "range": "string",
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
    "tox_dose_reductions": {
      "slot_uri": "",
      "range": "integer",
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
    "stage_system_version": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt,npc"
      }
    },
    "tox_delay": {
      "slot_uri": "",
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
    "path_morph_reporting": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "sub_agent": {
      "slot_uri": "ncit:C185634",
      "range": "SubAgentEnum",
      "comments": [],
      "annotations": {}
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
    "associated_condition": {
      "slot_uri": "",
      "range": "AssociatedConditionEnum",
      "comments": [],
      "annotations": {}
    },
    "parental_status": {
      "slot_uri": "",
      "range": "ParentalStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
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
    "kaposi_sarcoma_i": {
      "slot_uri": "C134978",
      "range": "KaposiSarcomaIEnum",
      "comments": [],
      "annotations": {}
    },
    "reported_significance_numeric": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
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
    "modification_basis": {
      "slot_uri": "ncit:C93529",
      "range": "ModificationBasisEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc"
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
    "inheritance_pattern": {
      "slot_uri": "ncit:C45827",
      "range": "InheritancePatternEnum",
      "comments": [],
      "annotations": {}
    },
    "nephron_sparing_partial_nephrectomy": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "toxicity_immune": {
      "slot_uri": "ncit:C63814",
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
    "tox_high_grade_events": {
      "slot_uri": "",
      "range": "integer",
      "comments": [],
      "annotations": {}
    },
    "transformation_conf_source": {
      "slot_uri": "",
      "range": "TransformationConfSourceEnum",
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
    "tumor_number": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa"
      }
    },
    "transformation": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "kaposi_sarcoma_s": {
      "slot_uri": "C134981",
      "range": "KaposiSarcomaSEnum",
      "comments": [],
      "annotations": {}
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
    "sub_agent_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "reason": {
      "slot_uri": "ncit:C185636",
      "range": "ReasonEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc"
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
    "disease_presence": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
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
    "hgvs_coding_transcript": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "kaposi_sarcoma_t": {
      "slot_uri": "C134970",
      "range": "KaposiSarcomaTEnum",
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
    "stage_text": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "reason_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {}
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
    "toxicity_detail": {
      "slot_uri": "ncit:C185693",
      "range": "ToxicityDetailEnum",
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
    "diagnosis_conf_source": {
      "slot_uri": "",
      "range": "DiagnosisConfSourceEnum",
      "comments": [],
      "annotations": {}
    }
  },
  "enums": {
    "DiagnosisBasisEnum": {
      "permissible_values": {
        "Clinical": {
          "meaning": "ncit:C15607",
          "comments": []
        },
        "Molecular": {
          "meaning": "ncit:C20826",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "InheritancePatternEnum": {
      "permissible_values": {
        "Autosomal Dominant": {
          "meaning": "ncit:C94245",
          "comments": []
        },
        "Autosomal Recessive": {
          "meaning": "ncit:C94246",
          "comments": []
        },
        "X-Linked Dominant": {
          "meaning": "",
          "comments": []
        },
        "X-linked Recessive": {
          "meaning": "ncit:C94247",
          "comments": []
        }
      }
    },
    "AnthropometricMeasurementTypeEnum": {
      "permissible_values": {
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
    "MorphCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
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
    "TransformationConfSourceEnum": {
      "permissible_values": {
        "Confirmed Based On Pathology": {
          "meaning": "",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "Suspected Based On Imaging": {
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
        }
      }
    },
    "KaposiSarcomaSEnum": {
      "permissible_values": {
        "S0": {
          "meaning": "ncit:C134982",
          "comments": []
        },
        "S1": {
          "meaning": "ncit:C134983",
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
        },
        "Unknown": {
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
        "Axillary Nodes": {
          "meaning": "ncit:C12904",
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
        "Celiac Nodes": {
          "meaning": "ncit:C65166",
          "comments": []
        },
        "Central Nervous System": {
          "meaning": "ncit:C12438",
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
        "Cutaneous": {
          "meaning": "ncit:C13316",
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
        "Eyelid": {
          "meaning": "ncit:C12713",
          "comments": []
        },
        "Face": {
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
        "Frontal Bone": {
          "meaning": "ncit:C32635",
          "comments": []
        },
        "Frontal Cortex": {
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
        "Hypopharynx": {
          "meaning": "ncit:C12246",
          "comments": []
        },
        "Iliac Crest": {
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
        "Leg": {
          "meaning": "ncit:C32974",
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
        "Lumbar Vertebra": {
          "meaning": "ncit:C45874",
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
        "Meninges": {
          "meaning": "ncit:C12348",
          "comments": []
        },
        "Mesenteric Nodes": {
          "meaning": "ncit:C77641",
          "comments": []
        },
        "Metacarpus": {
          "meaning": "ncit:C12751",
          "comments": []
        },
        "Metatarsus": {
          "meaning": "ncit:C12752",
          "comments": []
        },
        "Middle Ear": {
          "meaning": "ncit:C12274",
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
        "Omentum/Peritoneum": {
          "meaning": "ncit:C33209",
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
        "Parietal Bone": {
          "meaning": "ncit:C12766",
          "comments": []
        },
        "Parietal Cortex": {
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
        "Pelvis, Sacrum": {
          "meaning": "ncit:C33508",
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
        "Scalp": {
          "meaning": "ncit:C89807",
          "comments": []
        },
        "Scapula": {
          "meaning": "ncit:C12744",
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
        "Superior Maxilla": {
          "meaning": "ncit:C33682",
          "comments": []
        },
        "Supraclavicular Lymph Node": {
          "meaning": "ncit:C12903",
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
        "Temporal Bone": {
          "meaning": "ncit:C12797",
          "comments": []
        },
        "Temporal Cortex": {
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
        "Thoracic Vertebra": {
          "meaning": "ncit:C12798",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
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
    "AlterationRegionEnum": {
      "permissible_values": {
        "5' UTR": {
          "meaning": "ncit:C13371",
          "comments": []
        }
      }
    },
    "SurgicalComplicationsEnum": {
      "permissible_values": {
        "Bleed": {
          "meaning": "",
          "comments": []
        },
        "Intra-operative Tumor Rupture": {
          "meaning": "",
          "comments": []
        },
        "Not Applicable": {
          "meaning": "ncit:C48660",
          "comments": []
        },
        "Urgent Surgery for ICP": {
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
        "Cell Free DNA BCT": {
          "meaning": "",
          "comments": []
        },
        "K2EDTA": {
          "meaning": "",
          "comments": []
        },
        "Saliva": {
          "meaning": "ncit:C174119",
          "comments": []
        },
        "Stool Sample": {
          "meaning": "ncit:C189125",
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
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        }
      }
    },
    "AlterationEnum": {
      "permissible_values": {
        "ACD Variant": {
          "meaning": "ncit:C152088",
          "comments": []
        },
        "ALK Variant": {
          "meaning": "ncit:C81945",
          "comments": []
        },
        "ANKRD26 Variant": {
          "meaning": "ncit:C151909",
          "comments": []
        },
        "APC Variant": {
          "meaning": "ncit:C164173",
          "comments": []
        },
        "ASXL1 Variant": {
          "meaning": "",
          "comments": []
        },
        "ATM Variant": {
          "meaning": "ncit:C178532",
          "comments": []
        },
        "ATP7B Variant": {
          "meaning": "",
          "comments": []
        },
        "BAP1 Variant": {
          "meaning": "",
          "comments": []
        },
        "BLM Variant": {
          "meaning": "",
          "comments": []
        },
        "BMPR1A": {
          "meaning": "",
          "comments": []
        },
        "BRAF Gene": {
          "meaning": "ncit:C18363",
          "comments": []
        },
        "BRCA1 Variant": {
          "meaning": "ncit:C131467",
          "comments": []
        },
        "BRCA2 Variant": {
          "meaning": "ncit:C131468",
          "comments": []
        },
        "BRIP1 Variant": {
          "meaning": "",
          "comments": []
        },
        "BUB1B Variant": {
          "meaning": "",
          "comments": []
        },
        "CBL Variant": {
          "meaning": "",
          "comments": []
        },
        "CDC73 Variant": {
          "meaning": "ncit:C164265",
          "comments": []
        },
        "CDH1 Variant": {
          "meaning": "ncit:C165503",
          "comments": []
        },
        "CDK4 Variant": {
          "meaning": "ncit:C146926",
          "comments": []
        },
        "CDKN1B Variant": {
          "meaning": "",
          "comments": []
        },
        "CDKN1C Variant": {
          "meaning": "",
          "comments": []
        },
        "CDKN2A Variant": {
          "meaning": "ncit:C146926",
          "comments": []
        },
        "CEBPA Variant": {
          "meaning": "",
          "comments": []
        },
        "CHEK2 Variant": {
          "meaning": "ncit:C173450",
          "comments": []
        },
        "CREBBP Variant": {
          "meaning": "",
          "comments": []
        },
        "CTR9 Variant": {
          "meaning": "",
          "comments": []
        },
        "DDB2 Variant": {
          "meaning": "",
          "comments": []
        },
        "DDX41 Variant": {
          "meaning": "",
          "comments": []
        },
        "DICER1 Variant": {
          "meaning": "ncit:C164287",
          "comments": []
        },
        "DIS3L2 Variant": {
          "meaning": "",
          "comments": []
        },
        "DKC1 Variant": {
          "meaning": "",
          "comments": []
        },
        "EP300 Variant": {
          "meaning": "",
          "comments": []
        },
        "EPCAM Variant": {
          "meaning": "ncit:C178537",
          "comments": []
        },
        "ERCC2 Variant": {
          "meaning": "ncit:C165564",
          "comments": []
        },
        "ERCC3 Variant": {
          "meaning": "",
          "comments": []
        },
        "ERCC4 Variant": {
          "meaning": "",
          "comments": []
        },
        "ERCC5 Variant": {
          "meaning": "",
          "comments": []
        },
        "ETV6 Variant": {
          "meaning": "",
          "comments": []
        },
        "EZH2 Variant": {
          "meaning": "ncit:C188740",
          "comments": []
        },
        "FAH Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCA Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCB Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCC Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCD2 Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCE Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCF Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCG Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCI Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCL Variant": {
          "meaning": "",
          "comments": []
        },
        "FANCM Variant": {
          "meaning": "",
          "comments": []
        },
        "FBXW7 Variant": {
          "meaning": "ncit:C165603",
          "comments": []
        },
        "FH Variant": {
          "meaning": "",
          "comments": []
        },
        "FLCN Variant": {
          "meaning": "",
          "comments": []
        },
        "GATA2 Variant": {
          "meaning": "",
          "comments": []
        },
        "GPC3 Variant": {
          "meaning": "",
          "comments": []
        },
        "GPC4 Variant": {
          "meaning": "",
          "comments": []
        },
        "Gain of Chromosome 12q": {
          "meaning": "ncit:C36441",
          "comments": []
        },
        "Gain of Chromosome 15q": {
          "meaning": "ncit:C36481",
          "comments": []
        },
        "Gain of Chromosome 17q": {
          "meaning": "ncit:C36484",
          "comments": []
        },
        "Gain of Chromosome 1q": {
          "meaning": "ncit:C36482",
          "comments": []
        },
        "Gain of Chromosome 20q": {
          "meaning": "ncit:C36480",
          "comments": []
        },
        "Gain of Chromosome 9q": {
          "meaning": "ncit:C36483",
          "comments": []
        },
        "H19 Variant": {
          "meaning": "",
          "comments": []
        },
        "HRAS Variant": {
          "meaning": "ncit:C140251",
          "comments": []
        },
        "IGF2 Variant": {
          "meaning": "",
          "comments": []
        },
        "ITK Variant": {
          "meaning": "",
          "comments": []
        },
        "KCNQ1OT1 Variant": {
          "meaning": "",
          "comments": []
        },
        "KDM3B Variant": {
          "meaning": "",
          "comments": []
        },
        "KIT Variant": {
          "meaning": "ncit:C126819",
          "comments": []
        },
        "KRAS Variant": {
          "meaning": "ncit:C98362",
          "comments": []
        },
        "LZTR1 Variant": {
          "meaning": "",
          "comments": []
        },
        "Loss of Chromosome 13q": {
          "meaning": "ncit:C36497",
          "comments": []
        },
        "Loss of Chromosome 14": {
          "meaning": "ncit:C36490",
          "comments": []
        },
        "Loss of Chromosome 1p": {
          "meaning": "ncit:C36501",
          "comments": []
        },
        "Loss of Chromosome 22": {
          "meaning": "ncit:C36491",
          "comments": []
        },
        "Loss of Chromosome 3p": {
          "meaning": "ncit:C36502",
          "comments": []
        },
        "Loss of Chromosome Y": {
          "meaning": "ncit:C36599",
          "comments": []
        },
        "MAP2K1 Variant": {
          "meaning": "",
          "comments": []
        },
        "MAPK1 Variant": {
          "meaning": "ncit:C187408",
          "comments": []
        },
        "MAX Variant": {
          "meaning": "",
          "comments": []
        },
        "MEN1 Variant": {
          "meaning": "",
          "comments": []
        },
        "MET Variant": {
          "meaning": "ncit:C136286",
          "comments": []
        },
        "MLH1 Variant": {
          "meaning": "ncit:C178530",
          "comments": []
        },
        "MPL Variant": {
          "meaning": "ncit:C126823",
          "comments": []
        },
        "MRAS Variant": {
          "meaning": "",
          "comments": []
        },
        "MSH2 Variant": {
          "meaning": "ncit:C131462",
          "comments": []
        },
        "MSH6 Variant": {
          "meaning": "ncit:C178531",
          "comments": []
        },
        "MUTYH Variant": {
          "meaning": "ncit:C169096",
          "comments": []
        },
        "Monosomy 7": {
          "meaning": "ncit:c36411",
          "comments": []
        },
        "NBN Variant": {
          "meaning": "",
          "comments": []
        },
        "NF1 Variant": {
          "meaning": "ncit:C167058",
          "comments": []
        },
        "NF2 Variant": {
          "meaning": "",
          "comments": []
        },
        "NHP2 Variant": {
          "meaning": "",
          "comments": []
        },
        "NOP10 Variant": {
          "meaning": "",
          "comments": []
        },
        "NOTCH3 Variant": {
          "meaning": "",
          "comments": []
        },
        "NRAS Variant": {
          "meaning": "ncit:C98439",
          "comments": []
        },
        "NSD1 Variant": {
          "meaning": "",
          "comments": []
        },
        "NTRK1 Variant": {
          "meaning": "ncit:C169007",
          "comments": []
        },
        "NYNRIN Variant": {
          "meaning": "",
          "comments": []
        },
        "OCA2 Variant": {
          "meaning": "",
          "comments": []
        },
        "OCA5 Variant": {
          "meaning": "",
          "comments": []
        },
        "OFD1 Variant": {
          "meaning": "",
          "comments": []
        },
        "PALB2 Variant": {
          "meaning": "ncit:C178538",
          "comments": []
        },
        "PARN Variant": {
          "meaning": "",
          "comments": []
        },
        "PAX5 Variant": {
          "meaning": "ncit:C158140",
          "comments": []
        },
        "PDGFRA Variant": {
          "meaning": "ncit:C107569",
          "comments": []
        },
        "PDGFRB Variant": {
          "meaning": "ncit:C128173",
          "comments": []
        },
        "PHOX2B Variant": {
          "meaning": "",
          "comments": []
        },
        "PIK3CA Variant": {
          "meaning": "ncit:C98460",
          "comments": []
        },
        "PMS2 Variant": {
          "meaning": "ncit:C178529",
          "comments": []
        },
        "POLH Variant": {
          "meaning": "",
          "comments": []
        },
        "PPP1CB Variant": {
          "meaning": "",
          "comments": []
        },
        "PRKAR1A Variant": {
          "meaning": "",
          "comments": []
        },
        "PTCH1 Variant": {
          "meaning": "ncit:C133669",
          "comments": []
        },
        "PTEN Variant": {
          "meaning": "ncit:C165569",
          "comments": []
        },
        "PTPN11 Variant": {
          "meaning": "ncit:C169022",
          "comments": []
        },
        "RAD51C Variant": {
          "meaning": "",
          "comments": []
        },
        "RAF1 Variant": {
          "meaning": "",
          "comments": []
        },
        "RASA2 Variant": {
          "meaning": "",
          "comments": []
        },
        "RB1 Variant": {
          "meaning": "ncit:C169031",
          "comments": []
        },
        "RBM8A Variant": {
          "meaning": "",
          "comments": []
        },
        "RECQL4 Variant": {
          "meaning": "",
          "comments": []
        },
        "REST Variant": {
          "meaning": "",
          "comments": []
        },
        "RET Variant": {
          "meaning": "",
          "comments": []
        },
        "RIT1 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPL11 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPL19 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPL26 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPL35A Variant": {
          "meaning": "",
          "comments": []
        },
        "RPL5 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS10 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS17 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS19 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS24 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS26 Variant": {
          "meaning": "",
          "comments": []
        },
        "RPS7 Variant": {
          "meaning": "",
          "comments": []
        },
        "RRAS Variant": {
          "meaning": "",
          "comments": []
        },
        "RRAS2 Variant": {
          "meaning": "",
          "comments": []
        },
        "RTEL1 Variant": {
          "meaning": "",
          "comments": []
        },
        "RUNX1 Variant": {
          "meaning": "",
          "comments": []
        },
        "SAMD9 Variant": {
          "meaning": "",
          "comments": []
        },
        "SAMD9L Variant": {
          "meaning": "",
          "comments": []
        },
        "SBDS Variant": {
          "meaning": "",
          "comments": []
        },
        "SDHA Variant": {
          "meaning": "ncit:C126832",
          "comments": []
        },
        "SDHAF2 Variant": {
          "meaning": "",
          "comments": []
        },
        "SDHB Variant": {
          "meaning": "ncit:C169033",
          "comments": []
        },
        "SDHC Variant": {
          "meaning": "",
          "comments": []
        },
        "SDHD Variant": {
          "meaning": "ncit:C169036",
          "comments": []
        },
        "SETBP1 Variant": {
          "meaning": "",
          "comments": []
        },
        "SH2D1A Variant": {
          "meaning": "",
          "comments": []
        },
        "SHOC2 Variant": {
          "meaning": "",
          "comments": []
        },
        "SLC24A5 Variant": {
          "meaning": "",
          "comments": []
        },
        "SLC45A2 Variant": {
          "meaning": "",
          "comments": []
        },
        "SMAD4 Variant": {
          "meaning": "",
          "comments": []
        },
        "SMARCA4 Variant": {
          "meaning": "ncit:C142126",
          "comments": []
        },
        "SMARCB1 Variant": {
          "meaning": "ncit:C18394",
          "comments": []
        },
        "SMARCE1 Variant": {
          "meaning": "",
          "comments": []
        },
        "SOS1 Variant": {
          "meaning": "ncit:C180788",
          "comments": []
        },
        "SOS2 Variant": {
          "meaning": "ncit:C199592",
          "comments": []
        },
        "SPRED1 Variant": {
          "meaning": "",
          "comments": []
        },
        "STK11 Variant": {
          "meaning": "ncit:C178533",
          "comments": []
        },
        "SUFU Variant": {
          "meaning": "ncit:C189843",
          "comments": []
        },
        "TERC Variant": {
          "meaning": "",
          "comments": []
        },
        "TERT Variant": {
          "meaning": "",
          "comments": []
        },
        "TINF2 Variant": {
          "meaning": "",
          "comments": []
        },
        "TMEM127 Variant": {
          "meaning": "",
          "comments": []
        },
        "TP53 Variant": {
          "meaning": "ncit:C118396",
          "comments": []
        },
        "TRIM28 Variant": {
          "meaning": "",
          "comments": []
        },
        "TRIM37 Variant": {
          "meaning": "",
          "comments": []
        },
        "TSC1 Variant": {
          "meaning": "",
          "comments": []
        },
        "TSC2 Variant": {
          "meaning": "",
          "comments": []
        },
        "TYR Variant": {
          "meaning": "",
          "comments": []
        },
        "TYRP1 Variant": {
          "meaning": "",
          "comments": []
        },
        "Trisomy 17": {
          "meaning": "ncit:C37865",
          "comments": []
        },
        "Trisomy 7": {
          "meaning": "ncit:C36476",
          "comments": []
        },
        "VHL Variant": {
          "meaning": "",
          "comments": []
        },
        "WRAP53 Variant": {
          "meaning": "",
          "comments": []
        },
        "WT1 Variant": {
          "meaning": "",
          "comments": []
        },
        "XIAP Variant": {
          "meaning": "",
          "comments": []
        },
        "XPA Variant": {
          "meaning": "",
          "comments": []
        },
        "XPC Variant": {
          "meaning": "ncit:C169090",
          "comments": []
        },
        "del(11p15.5)": {
          "meaning": "ncit:C177306",
          "comments": []
        },
        "del(9p21)": {
          "meaning": "ncit:C177307",
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
        "Mosaic": {
          "meaning": "ncit:C88144",
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
        "AJCC, v6 >> Stage 0": {
          "meaning": "C90529",
          "comments": []
        },
        "AJCC, v6 >> Stage 1": {
          "meaning": "C90529",
          "comments": []
        },
        "AJCC, v6 >> Stage 2": {
          "meaning": "C90529",
          "comments": []
        },
        "AJCC, v6 >> Stage 3": {
          "meaning": "C90529",
          "comments": []
        },
        "AJCC, v6 >> Stage 4": {
          "meaning": "C90529",
          "comments": []
        },
        "AJCC, v7 >> Stage 0": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC, v7 >> Stage 1": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC, v7 >> Stage 2": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC, v7 >> Stage 3": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC, v7 >> Stage 4": {
          "meaning": "ncit:C90530",
          "comments": []
        },
        "AJCC, v8 >> Stage 0": {
          "meaning": "ncit:C132248",
          "comments": []
        },
        "AJCC, v8 >> Stage 1": {
          "meaning": "ncit:C132248",
          "comments": []
        },
        "AJCC, v8 >> Stage 2": {
          "meaning": "ncit:C132248",
          "comments": []
        },
        "AJCC, v8 >> Stage 3": {
          "meaning": "ncit:C132248",
          "comments": []
        },
        "AJCC, v8 >> Stage 4": {
          "meaning": "ncit:C132248",
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
        "Children's Oncology Group Liver Tumor Staging System >> Stage 1": {
          "meaning": "ncit:C177630",
          "comments": []
        },
        "Children's Oncology Group Liver Tumor Staging System >> Stage 2": {
          "meaning": "ncit:C177630",
          "comments": []
        },
        "Children's Oncology Group Liver Tumor Staging System >> Stage 3": {
          "meaning": "ncit:C177630",
          "comments": []
        },
        "Children's Oncology Group Liver Tumor Staging System >> Stage 4": {
          "meaning": "ncit:C177630",
          "comments": []
        },
        "Children's Oncology Group Neuroblastoma Risk Group Staging System >> Stage L1": {
          "meaning": "ncit:C177631",
          "comments": []
        },
        "Children's Oncology Group Neuroblastoma Risk Group Staging System >> Stage L2": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Neuroblastoma Risk Group Staging System >> Stage M": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Neuroblastoma Risk Group Staging System >> Stage MS": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System >> Stage 1": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System >> Stage 2": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System >> Stage 3": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System >> Stage 4": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Renal Cancer Staging System >> Stage 5": {
          "meaning": "ncit:C177632",
          "comments": []
        },
        "Children's Oncology Group Retinoblastoma Risk Group Staging System >> High Risk": {
          "meaning": "ncit:C102401",
          "comments": []
        },
        "Children's Oncology Group Retinoblastoma Risk Group Staging System >> Intermediate Risk": {
          "meaning": "ncit:C102402",
          "comments": []
        },
        "Children's Oncology Group Retinoblastoma Risk Group Staging System >> Low Risk": {
          "meaning": "ncit:C102403",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System >> Stage 1": {
          "meaning": "ncit:C198025",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System >> Stage 2": {
          "meaning": "ncit:C198025",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System >> Stage 3": {
          "meaning": "ncit:C198025",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System >> Stage 4": {
          "meaning": "ncit:C198025",
          "comments": []
        },
        "Childrens Oncology Group/National Wilms Tumor Study Group Staging System >> Stage 5": {
          "meaning": "ncit:C198025",
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
        "Enneking Staging System >> Stage 1a": {
          "meaning": "ncit:C146701",
          "comments": []
        },
        "Enneking Staging System >> Stage 1b": {
          "meaning": "ncit:C146702",
          "comments": []
        },
        "Enneking Staging System >> Stage 2a": {
          "meaning": "ncit:C146703",
          "comments": []
        },
        "Enneking Staging System >> Stage 2b": {
          "meaning": "ncit:C146704",
          "comments": []
        },
        "Enneking Staging System >> Stage 3": {
          "meaning": "ncit:C146705",
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
        "Evans >> Stage 4s": {
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
        "International Society of Pediatric Oncology Staging System >> Stage 1": {
          "meaning": "",
          "comments": []
        },
        "International Society of Pediatric Oncology Staging System >> Stage 2": {
          "meaning": "",
          "comments": []
        },
        "International Society of Pediatric Oncology Staging System >> Stage 3": {
          "meaning": "",
          "comments": []
        },
        "International Society of Pediatric Oncology Staging System >> Stage 4": {
          "meaning": "",
          "comments": []
        },
        "International Society of Pediatric Oncology Staging System >> Stage 5": {
          "meaning": "",
          "comments": []
        },
        "Lugano Stage >> Stage 1": {
          "meaning": "ncit:C141180",
          "comments": []
        },
        "Lugano Stage >> Stage 1E": {
          "meaning": "ncit:C141181",
          "comments": []
        },
        "Lugano Stage >> Stage 2": {
          "meaning": "ncit:C141182",
          "comments": []
        },
        "Lugano Stage >> Stage 2E": {
          "meaning": "ncit:C141183",
          "comments": []
        },
        "Lugano Stage >> Stage 3": {
          "meaning": "ncit:C141186",
          "comments": []
        },
        "Lugano Stage >> Stage 4": {
          "meaning": "ncit:C141187",
          "comments": []
        },
        "PRETEXT, 1992 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 1992 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2005-COG >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, 2017 >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group I": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group II": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group III": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "PRETEXT, NOS >> Group IV": {
          "meaning": "",
          "comments": [
            "(lt) ConsortiumNote: STAGE_SYSTEM = 'PRETEXT Staging System'"
          ]
        },
        "St. Jude Stage >> Stage 1": {
          "meaning": "C141218",
          "comments": []
        },
        "St. Jude Stage >> Stage 2": {
          "meaning": "C141219",
          "comments": []
        },
        "St. Jude Stage >> Stage 3": {
          "meaning": "C141220",
          "comments": []
        },
        "St. Jude Stage >> Stage 4": {
          "meaning": "C141221",
          "comments": []
        },
        "System NOS >> Stage 0": {
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
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
          "comments": []
        },
        "Not Applicable": {
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
    "AssociatedConditionEnum": {
      "permissible_values": {
        "ANKRD26-Related Thrombocytopenia and Leukemia Predisposition": {
          "meaning": "ncit:C178387",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia Susceptibility - PAX5": {
          "meaning": "ncit:C176907",
          "comments": []
        },
        "Ataxia Telangiectasia Syndrome": {
          "meaning": "ncit:C2887",
          "comments": []
        },
        "Ataxia-Pancytopenia Syndrome": {
          "meaning": "ncit:C176909",
          "comments": []
        },
        "Attenuated Familial Adenomatous Polyposis": {
          "meaning": "ncit:C6729",
          "comments": []
        },
        "BAP1 Tumor Predisposition Syndrome": {
          "meaning": "ncit:C172639",
          "comments": []
        },
        "Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia": {
          "meaning": "ncit:C34415",
          "comments": []
        },
        "Birt-Hogg-Dube Syndrome": {
          "meaning": "ncit:C28244",
          "comments": []
        },
        "Bloom Syndrome": {
          "meaning": "ncit:C2903",
          "comments": []
        },
        "Bohring-Opitz Syndrome": {
          "meaning": "ncit:C131533",
          "comments": []
        },
        "CBL Syndrome": {
          "meaning": "ncit:C176942",
          "comments": []
        },
        "CDC73-Related Neoplastic Syndrome": {
          "meaning": "ncit:C178382",
          "comments": []
        },
        "CDH1-Associated Breast Carcinoma Syndrome": {
          "meaning": "ncit:C176628",
          "comments": []
        },
        "CEBPA-Related Leukemia Predisposition": {
          "meaning": "ncit:C178379",
          "comments": []
        },
        "CHEK2-Associated Cancer Predisposition": {
          "meaning": "ncit:C176588",
          "comments": []
        },
        "Carney Complex": {
          "meaning": "ncit:C4705",
          "comments": []
        },
        "Congenital Amegakaryocytic Thrombocytopenia": {
          "meaning": "ncit:C115207",
          "comments": []
        },
        "Constitutional Mismatch Repair Deficiency": {
          "meaning": "ncit:C130202",
          "comments": []
        },
        "Costello Syndrome": {
          "meaning": "ncit:C84652",
          "comments": []
        },
        "Cowden Syndrome": {
          "meaning": "ncit:C3076",
          "comments": []
        },
        "DDX41-Related Leukemia Predisposition": {
          "meaning": "ncit:C178380",
          "comments": []
        },
        "DICER1 Syndrome": {
          "meaning": "ncit:C123317",
          "comments": []
        },
        "Diamond-Blackfan Anemia": {
          "meaning": "ncit:C176913",
          "comments": []
        },
        "Dyskeratosis Congenita": {
          "meaning": "ncit:C111802",
          "comments": []
        },
        "ETV6-Related Thrombocytopenia and Leukemia Predisposition": {
          "meaning": "ncit:C178386",
          "comments": []
        },
        "Familial Adenomatous Polyposis": {
          "meaning": "ncit:C3339",
          "comments": []
        },
        "Familial Gastrointestinal Stromal Tumor": {
          "meaning": "ncit:C176906",
          "comments": []
        },
        "Familial Paraganglioma-Pheochromocytoma Syndrome": {
          "meaning": "ncit:C48300",
          "comments": []
        },
        "Familial Platelet Disorder and AML Syndrome": {
          "meaning": "ncit:C41527",
          "comments": []
        },
        "Fanconi Anemia": {
          "meaning": "ncit:C62505",
          "comments": []
        },
        "GATA2 Deficiency": {
          "meaning": "ncit:C126349",
          "comments": []
        },
        "Genetic Predisposition to Melanoma": {
          "meaning": "ncit:C179472",
          "comments": []
        },
        "Genetic Predisposition to Meningioma": {
          "meaning": "ncit:C179471",
          "comments": []
        },
        "Genetic Predisposition to Myofibromatosis": {
          "meaning": "ncit:C179470",
          "comments": []
        },
        "Genetic Predisposition to Neuroblastoma": {
          "meaning": "ncit:C179469",
          "comments": []
        },
        "Genetic Predisposition to Non-Syndromic Wilms Tumor": {
          "meaning": "ncit:C178392",
          "comments": []
        },
        "Genetic Predisposition to Papillary Renal Cell Carcinoma": {
          "meaning": "ncit:C179473",
          "comments": []
        },
        "Hepatolenticular Degeneration": {
          "meaning": "ncit:C84756",
          "comments": []
        },
        "Hereditary Breast and Ovarian Cancer Syndrome": {
          "meaning": "ncit:C41527",
          "comments": []
        },
        "Hereditary Leiomyomatosis and Renal Cell Carcinoma Syndrome": {
          "meaning": "ncit:C41527",
          "comments": []
        },
        "Hereditary Retinoblastoma": {
          "meaning": "ncit:C8495",
          "comments": []
        },
        "Juvenile Polyposis Syndrome": {
          "meaning": "ncit:C7754",
          "comments": []
        },
        "LEOPARD Syndrome": {
          "meaning": "ncit:C84820",
          "comments": []
        },
        "Legius Syndrome": {
          "meaning": "ncit:C176941",
          "comments": []
        },
        "Li-Fraumeni Syndrome": {
          "meaning": "ncit:C3476",
          "comments": []
        },
        "Lymphoproliferative Syndrome 1/ITK Deficiency": {
          "meaning": "ncit:C126344",
          "comments": []
        },
        "Lynch Syndrome": {
          "meaning": "ncit:C8494",
          "comments": []
        },
        "MIRAGE Syndrome": {
          "meaning": "ncit:C147530",
          "comments": []
        },
        "MUTYH-Associated Polyposis": {
          "meaning": "ncit:C96520",
          "comments": []
        },
        "Mosaic Variegated Aneuploidy Syndrome 1": {
          "meaning": "ncit:C128192",
          "comments": []
        },
        "Mulibrey Nanism": {
          "meaning": "ncit:C84906",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 1": {
          "meaning": "ncit:C3225",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 2": {
          "meaning": "ncit:C123329",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 4": {
          "meaning": "ncit:C157449",
          "comments": []
        },
        "Neurofibromatosis Type 1": {
          "meaning": "ncit:C3273",
          "comments": []
        },
        "Neurofibromatosis Type 2": {
          "meaning": "ncit:C3274",
          "comments": []
        },
        "Nevoid Basal Cell Carcinoma Syndrome": {
          "meaning": "ncit:C2892",
          "comments": []
        },
        "Nijmegen Breakage Syndrome": {
          "meaning": "ncit:C4692",
          "comments": []
        },
        "Noonan Syndrome": {
          "meaning": "ncit:C34854",
          "comments": []
        },
        "Noonan Syndrome-Like Disorder with Loose Anagen Hair": {
          "meaning": "ncit:C178129",
          "comments": []
        },
        "Oculocutaneous Albinism": {
          "meaning": "ncit:C84941",
          "comments": []
        },
        "PIK3CA-Related Overgrowth Spectrum": {
          "meaning": "ncit:C178285",
          "comments": []
        },
        "Perlman Syndrome": {
          "meaning": "ncit:C103144",
          "comments": []
        },
        "Peutz-Jeghers Syndrome": {
          "meaning": "ncit:C3324",
          "comments": []
        },
        "Radial Aplasia-Thrombocytopenia Syndrome": {
          "meaning": "ncit:C99038",
          "comments": []
        },
        "Rhabdoid Tumor Predisposition Syndrome 1": {
          "meaning": "ncit:C178393",
          "comments": []
        },
        "Rhabdoid Tumor Predisposition Syndrome 2": {
          "meaning": "ncit:C178394",
          "comments": []
        },
        "Rothmund-Thompson Syndrome": {
          "meaning": "ncit:C3335",
          "comments": []
        },
        "Rubinstein-Taybi Syndrome": {
          "meaning": "ncit:C75466",
          "comments": []
        },
        "SAMD9L-Related Myelodysplastic Syndrome Predisposition": {
          "meaning": "ncit:C178390",
          "comments": []
        },
        "Schinzel-Giedion Syndrome": {
          "meaning": "ncit:C129308",
          "comments": []
        },
        "Schwannomatosis": {
          "meaning": "ncit:C6557",
          "comments": []
        },
        "Shwachman-Diamond Syndrome": {
          "meaning": "ncit:C61235",
          "comments": []
        },
        "Simpson-Golabi-Behmel Syndrome": {
          "meaning": "ncit:C131002",
          "comments": []
        },
        "Sotos Syndrome": {
          "meaning": "ncit:C75019",
          "comments": []
        },
        "Tuberous Sclerosis": {
          "meaning": "ncit:C3424",
          "comments": []
        },
        "Tyrosinemia Type I": {
          "meaning": "ncit:C98641",
          "comments": []
        },
        "Von Hippel-Lindau Syndrome": {
          "meaning": "ncit:C3105",
          "comments": []
        },
        "WT1 Syndromes": {
          "meaning": "ncit:C131006",
          "comments": []
        },
        "Weaver Syndrome": {
          "meaning": "ncit:C125599",
          "comments": []
        },
        "X-linked Lymphoproliferative Syndrome": {
          "meaning": "ncit:C61246",
          "comments": []
        },
        "Xeroderma Pigmentosum": {
          "meaning": "ncit:C3452",
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
    "ExternalRefIdSystemEnum": {
      "permissible_values": {
        "COSMIC": {
          "meaning": "",
          "comments": []
        },
        "ClinGen": {
          "meaning": "",
          "comments": []
        },
        "Genome Aggregation Database (gnomAD)": {
          "meaning": "",
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
        "St. Jude Stage": {
          "meaning": "ncit:C141216",
          "comments": []
        },
        "Toronto Childhood Cancer Stage Guidelines": {
          "meaning": "ncit:C197985",
          "comments": []
        },
        "Unknown": {
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
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        },
        "Not Reported": {
          "meaning": "ncit:C43234",
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
        },
        "Unknown": {
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
        "C3P Registry": {
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
    "TopCodeSystemEnum": {
      "permissible_values": {
        "ICD-O": {
          "meaning": "ncit:C160903",
          "comments": []
        }
      }
    },
    "DetectionMethodEnum": {
      "permissible_values": {
        "Audiogram": {
          "meaning": "",
          "comments": []
        },
        "Biopsy": {
          "meaning": "ncit:C15189",
          "comments": []
        },
        "Blood Work": {
          "meaning": "",
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
        "Colonoscopy": {
          "meaning": "",
          "comments": []
        },
        "Echocardiogram": {
          "meaning": "",
          "comments": []
        },
        "Flexible Fiberoptic Sigmoidoscopy": {
          "meaning": "",
          "comments": []
        },
        "Flexible sigmoidoscopy/colonoscopy": {
          "meaning": "",
          "comments": []
        },
        "Gallium Scan": {
          "meaning": "ncit:C38087",
          "comments": []
        },
        "Imaging, NOS": {
          "meaning": "ncit:C17369",
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
        "Upper endoscopy": {
          "meaning": "",
          "comments": []
        },
        "Urine Test": {
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
        "Not Evaluated": {
          "meaning": "ncit:C103424",
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
        "Reese-Ellsworth": {
          "meaning": "ncit:C123333",
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
        }
      }
    },
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Limb": {
          "meaning": "ncit:C12429",
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
        "Cytogenetics, NOS": {
          "meaning": "ncit:C16487",
          "comments": []
        },
        "DNA Methylation, Array": {
          "meaning": "ncit:C165222",
          "comments": []
        },
        "DNA Methylation, NOS": {
          "meaning": "ncit:C16848",
          "comments": []
        },
        "Expression Profiling, Nanostring": {
          "meaning": "",
          "comments": []
        },
        "Genotyping, NOS": {
          "meaning": "ncit:C45447",
          "comments": []
        },
        "PCR, MLPA": {
          "meaning": "ncit:C116161",
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
        "Sequencing, Sanger, Capillary Electrophoresis": {
          "meaning": "",
          "comments": []
        },
        "Sequencing, Sanger, Gel Electrophoresis": {
          "meaning": "",
          "comments": []
        },
        "Sequencing, Sanger, NOS": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "KaposiSarcomaIEnum": {
      "permissible_values": {
        "I0": {
          "meaning": "ncit:C134979",
          "comments": []
        },
        "I1": {
          "meaning": "ncit:C134980",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "PRE": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiagnosisConfSourceEnum": {
      "permissible_values": {
        "Death Certificate": {
          "meaning": "",
          "comments": []
        },
        "Medical Record Note": {
          "meaning": "",
          "comments": []
        },
        "Pathology Report": {
          "meaning": "",
          "comments": []
        },
        "Self-Report": {
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
    "GroupEnum": {
      "permissible_values": {
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
    "KaposiSarcomaTEnum": {
      "permissible_values": {
        "T0": {
          "meaning": "ncit:C169110",
          "comments": []
        },
        "T1": {
          "meaning": "ncit:C134976",
          "comments": []
        }
      }
    },
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "ANKRD26-Related Thrombocytopenia and Leukemia Predisposition": {
          "meaning": "ncit:C178387",
          "comments": []
        },
        "Acute Lymphoblastic Leukemia Susceptibility - PAX5": {
          "meaning": "ncit:C176907",
          "comments": []
        },
        "Adenomatous Polyposis Coli": {
          "meaning": "ncit:C17687",
          "comments": []
        },
        "Ataxia Telangiectasia Syndrome": {
          "meaning": "ncit:C2887",
          "comments": []
        },
        "Ataxia-Pancytopenia Syndrome": {
          "meaning": "ncit:C176909",
          "comments": []
        },
        "Attenuated Familial Adenomatous Polyposis": {
          "meaning": "ncit:C6729",
          "comments": []
        },
        "BAP1 Tumor Predisposition Syndrome": {
          "meaning": "ncit:C172639",
          "comments": []
        },
        "Beckwith-Wiedemann Syndrome/Isolated Hemihyperplasia": {
          "meaning": "ncit:C34415",
          "comments": []
        },
        "Birt-Hogg-Dube Syndrome": {
          "meaning": "ncit:C28244",
          "comments": []
        },
        "Bloom Syndrome": {
          "meaning": "ncit:C2903",
          "comments": []
        },
        "Bohring-Opitz Syndrome": {
          "meaning": "ncit:C131533",
          "comments": []
        },
        "CBL Syndrome": {
          "meaning": "ncit:C176942",
          "comments": []
        },
        "CDC73-Related Neoplastic Syndrome": {
          "meaning": "ncit:C178382",
          "comments": []
        },
        "CDH1-Associated Breast Carcinoma Syndrome": {
          "meaning": "ncit:C176628",
          "comments": []
        },
        "CEBPA-Related Leukemia Predisposition": {
          "meaning": "ncit:C178379",
          "comments": []
        },
        "CHEK2-Associated Cancer Predisposition": {
          "meaning": "ncit:C176588",
          "comments": []
        },
        "Carney Complex": {
          "meaning": "ncit:C4705",
          "comments": []
        },
        "Congenital Amegakaryocytic Thrombocytopenia": {
          "meaning": "ncit:C115207",
          "comments": []
        },
        "Constitutional Mismatch Repair Deficiency": {
          "meaning": "ncit:C130202",
          "comments": []
        },
        "Costello Syndrome": {
          "meaning": "ncit:C84652",
          "comments": []
        },
        "Cowden Syndrome": {
          "meaning": "ncit:C3076",
          "comments": []
        },
        "DDX41-Related Leukemia Predisposition": {
          "meaning": "ncit:C178380",
          "comments": []
        },
        "DICER1 Syndrome": {
          "meaning": "ncit:C123317",
          "comments": []
        },
        "Diamond-Blackfan Anemia": {
          "meaning": "ncit:C61236",
          "comments": []
        },
        "Dyskeratosis Congenita": {
          "meaning": "ncit:C111802",
          "comments": []
        },
        "ETV6-Related Thrombocytopenia and Leukemia Predisposition": {
          "meaning": "ncit:C178386",
          "comments": []
        },
        "Familial Adenomatous Polyposis": {
          "meaning": "ncit:C3339",
          "comments": []
        },
        "Familial Gastrointestinal Stromal Tumor": {
          "meaning": "ncit:C176906",
          "comments": []
        },
        "Familial Paraganglioma-Pheochromocytoma Syndrome": {
          "meaning": "ncit:C190373",
          "comments": []
        },
        "Familial Platelet Disorder and AML Syndrome": {
          "meaning": "ncit:C162696",
          "comments": []
        },
        "Fanconi Anemia": {
          "meaning": "ncit:C62505",
          "comments": []
        },
        "GATA2 Deficiency": {
          "meaning": "ncit:C126349",
          "comments": []
        },
        "Genetic Predisposition to Melanoma": {
          "meaning": "ncit:C179472",
          "comments": []
        },
        "Genetic Predisposition to Meningioma": {
          "meaning": "ncit:C179471",
          "comments": []
        },
        "Genetic Predisposition to Myofibromatosis": {
          "meaning": "ncit:C179470",
          "comments": []
        },
        "Genetic Predisposition to Neuroblastoma": {
          "meaning": "ncit:C179469",
          "comments": []
        },
        "Genetic Predisposition to Non-Syndromic Wilms Tumor": {
          "meaning": "ncit:C178392",
          "comments": []
        },
        "Genetic Predisposition to Papillary Renal Cell Carcinoma": {
          "meaning": "ncit:C179473",
          "comments": []
        },
        "Hepatolenticular Degeneration": {
          "meaning": "ncit:C84756",
          "comments": []
        },
        "Hereditary Breast and Ovarian Cancer Syndrome": {
          "meaning": "",
          "comments": []
        },
        "Hereditary Leiomyomatosis and Renal Cell Carcinoma Syndrome": {
          "meaning": "ncit:C51302",
          "comments": []
        },
        "Hereditary Retinoblastoma": {
          "meaning": "ncit:C8495",
          "comments": []
        },
        "Juvenile Polyposis Syndrome": {
          "meaning": "ncit:C7754",
          "comments": []
        },
        "LEOPARD Syndrome": {
          "meaning": "ncit:C84820",
          "comments": []
        },
        "Legius Syndrome": {
          "meaning": "ncit:C176941",
          "comments": []
        },
        "Li-Fraumeni Syndrome": {
          "meaning": "ncit:C3476",
          "comments": []
        },
        "Lymphoproliferative Syndrome 1/ITK Deficiency": {
          "meaning": "ncit:C126344",
          "comments": []
        },
        "Lynch Syndrome": {
          "meaning": "ncit:C8494",
          "comments": []
        },
        "MIRAGE Syndrome": {
          "meaning": "ncit:C147530",
          "comments": []
        },
        "MUTYH-Associated Polyposis": {
          "meaning": "ncit:C96520",
          "comments": []
        },
        "Mosaic Variegated Aneuploidy Syndrome 1": {
          "meaning": "ncit:C128192",
          "comments": []
        },
        "Mulibrey Nanism": {
          "meaning": "ncit:C84906",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 1": {
          "meaning": "ncit:C3225",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 2": {
          "meaning": "ncit:C123329",
          "comments": []
        },
        "Multiple Endocrine Neoplasia Type 4": {
          "meaning": "ncit:C157449",
          "comments": []
        },
        "Neurofibromatosis Type 1": {
          "meaning": "ncit:C3273",
          "comments": []
        },
        "Neurofibromatosis Type 2": {
          "meaning": "ncit:C3274",
          "comments": []
        },
        "Nevoid Basal Cell Carcinoma Syndrome": {
          "meaning": "ncit:C2892",
          "comments": []
        },
        "Nijmegen Breakage Syndrome": {
          "meaning": "ncit:C4692",
          "comments": []
        },
        "Noonan Syndrome": {
          "meaning": "ncit:C34854",
          "comments": []
        },
        "Noonan Syndrome-Like Disorder with Loose Anagen Hair": {
          "meaning": "ncit:C178129",
          "comments": []
        },
        "Oculocutaneous Albinism": {
          "meaning": "ncit:C84941",
          "comments": []
        },
        "PIK3CA-Related Overgrowth Spectrum": {
          "meaning": "ncit:C178285",
          "comments": []
        },
        "Perlman Syndrome": {
          "meaning": "ncit:C103144",
          "comments": []
        },
        "Peutz-Jeghers Syndrome": {
          "meaning": "ncit:C43324",
          "comments": []
        },
        "Radial Aplasia-Thrombocytopenia Syndrome": {
          "meaning": "ncit:C99038",
          "comments": []
        },
        "Rhabdoid Tumor Predisposition Syndrome 1": {
          "meaning": "ncit:C178393",
          "comments": []
        },
        "Rhabdoid Tumor Predisposition Syndrome 2": {
          "meaning": "ncit:C178394",
          "comments": []
        },
        "Rubinstein-Taybi Syndrome": {
          "meaning": "ncit:C75466",
          "comments": []
        },
        "SAMD9L-Related Myelodysplastic Syndrome Predisposition": {
          "meaning": "ncit:C178390",
          "comments": []
        },
        "Schinzel-Giedion Syndrome": {
          "meaning": "ncit:C129308",
          "comments": []
        },
        "Schwannomatosis": {
          "meaning": "ncit:C6557",
          "comments": []
        },
        "Shwachman-Diamond Syndrome": {
          "meaning": "ncit:C61235",
          "comments": []
        },
        "Simpson-Golabi-Behmel Syndrome": {
          "meaning": "ncit:C131002",
          "comments": []
        },
        "Sotos Syndrome": {
          "meaning": "ncit:C75019",
          "comments": []
        },
        "Tuberous Sclerosis": {
          "meaning": "ncit:C3424",
          "comments": []
        },
        "Tyrosinemia Type I": {
          "meaning": "ncit:C98641",
          "comments": []
        },
        "Von Hippel-Lindau Syndrome": {
          "meaning": "ncit:C3105",
          "comments": []
        },
        "WT1 Syndromes": {
          "meaning": "ncit:C131006",
          "comments": []
        },
        "Weaver Syndrome": {
          "meaning": "ncit:C125599",
          "comments": []
        },
        "X-linked Lymphoproliferative Syndrome": {
          "meaning": "ncit:C61246",
          "comments": []
        },
        "Xeroderma Pigmentosum": {
          "meaning": "ncit:C3452",
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
        "C3P": {
          "meaning": "ncit:C192767",
          "comments": []
        }
      }
    },
    "AdverseEventEnum": {
      "permissible_values": {
        "Treatment, NOS": {
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
    "GeneticAnalysisSpecimenEnum": {
      "permissible_values": {
        "Saliva": {
          "meaning": "ncit:C174119",
          "comments": [
            "(pre) ConsortiumNote: Map to Buccal Swab/Saliva"
          ]
        },
        "Primary Tumor": {
          "meaning": "ncit:C8509",
          "comments": []
        },
        "Metastatic Tumor": {
          "meaning": "ncit:C3261",
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
        }
      }
    },
    "TumorSizeEnum": {
      "permissible_values": {
        "<0.5 cm": {
          "meaning": "",
          "comments": []
        },
        "0.5-1 cm": {
          "meaning": "",
          "comments": []
        },
        "1-5 cm": {
          "meaning": "",
          "comments": []
        },
        "<=5 cm": {
          "meaning": "",
          "comments": []
        },
        "<=3mm": {
          "meaning": "",
          "comments": []
        },
        ">3mm": {
          "meaning": "",
          "comments": []
        },
        ">5 cm": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
        },
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