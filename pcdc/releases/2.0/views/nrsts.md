---
layout: default
title: Non-rhabdomyosarcoma Soft Tissue Sarcomas
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*NRSTS View*

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
- **Non-rhabdomyosarcoma Soft Tissue Sarcomas**
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The NRSTS view of the PCDC data model represents consensus data modeling by an international group of pediatric non-rhabdomyosarcoma soft tissue sarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors.


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

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | `StudyIdEnum` |  |
| `urls` | `string` |  |

## StudySubgroupAssignment

| Slot | Range | Description |
|---|---|---|
| `subgroup_type` | `SubgroupTypeEnum` |  |
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
| `efs_censor_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-efscensorstatusenum')">EfsCensorStatusEnum</button> |  |

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
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |
| `histology_grade` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-histologygradeenum')">HistologyGradeEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |
| `measurement1` | `decimal` |  |
| `measurement2` | `decimal` |  |
| `measurement3` | `decimal` |  |
| `measurement_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lesionmeasurementunitenum')">LesionMeasurementUnitEnum</button> |  |
| `tumor_size` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tumorsizeenum')">TumorSizeEnum</button> |  |
| `invasiveness` | `InvasivenessEnum` |  |
| `depth` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-depthenum')">DepthEnum</button> |  |

<div class="domain-heading">Intervention</div>

## RadiationTherapy

| Slot | Range | Description |
|---|---|---|
| `age_at_rt_start` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `rt_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtsiteenum')">RtSiteEnum</button> |  |
| `energy_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-energytypeenum')">EnergyTypeEnum</button> |  |
| `technique` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-techniqueenum')">TechniqueEnum</button> |  |
| `rt_dose` | `decimal` |  |
| `rt_dose_unit` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-rtdoseunitenum')">RtDoseUnitEnum</button> |  |
| `boost_dose` | `decimal` |  |
| `num_fraction` | `integer` |  |
| `fraction_dose` | `decimal` |  |
| `fraction_dose_unit` | `FractionDoseUnitEnum` |  |

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `tx_prior_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-txpriorresponseenum')">TxPriorResponseEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `necrosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-necrosisenum')">NecrosisEnum</button> |  |
| `necrosis_pct` | `decimal` |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |
| `smn_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-smnsiteenum')">SmnSiteEnum</button> |  |

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
| `genetic_analysis_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-geneticanalysisspecimenenum')">GeneticAnalysisSpecimenEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `cytodifferentiation` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-cytodifferentiationenum')">CytodifferentiationEnum</button> |  |
| `mitotic_rate` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mitoticrateenum')">MitoticRateEnum</button> |  |

<div id="enum-modal-alterationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationenum')">×</button>
<h3><code>AlterationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>ALK Rearrangement</code></td><td><code>ncit:C129574</code></td><td></td></tr>
<tr><td><code>ASPSCR1-TFE3</code></td><td><code>ncit:C99705</code></td><td></td></tr>
<tr><td><code>BCOR ITT Rearranged</code></td><td><code></code></td><td></td></tr>
<tr><td><code>BCOR-CCNB3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CIC-DUX4</code></td><td><code>ncit:C139663</code></td><td></td></tr>
<tr><td><code>ETV6 Rearranged</code></td><td><code>ncit:C155992</code></td><td></td></tr>
<tr><td><code>EWSR1 Rearranged</code></td><td><code>ncit:C165667</code></td><td></td></tr>
<tr><td><code>EWSR1-ATF1</code></td><td><code>ncit:C99216</code></td><td></td></tr>
<tr><td><code>EWSR1-CREB1</code></td><td><code>ncit:C99249</code></td><td></td></tr>
<tr><td><code>EWSR1-ETV1</code></td><td><code>ncit:C99259</code></td><td></td></tr>
<tr><td><code>EWSR1-ETV4</code></td><td><code>ncit:C99262</code></td><td></td></tr>
<tr><td><code>EWSR1-PBX1</code></td><td><code>ncit:C139668</code></td><td></td></tr>
<tr><td><code>EWSR1-POU5F1</code></td><td><code>ncit:C99256</code></td><td></td></tr>
<tr><td><code>EWSR1-ZNF444</code></td><td><code>ncit:C139731</code></td><td></td></tr>
<tr><td><code>FOXO1 Rearranged</code></td><td><code>ncit:C175960</code></td><td></td></tr>
<tr><td><code>FUS-CREB3L2</code></td><td><code>ncit:C99283</code></td><td></td></tr>
<tr><td><code>NTRK Rearranged</code></td><td><code>ncit:C171043</code></td><td></td></tr>
<tr><td><code>ROS1 Rearranged</code></td><td><code>ncit:C130236</code></td><td></td></tr>
<tr><td><code>SMARCB1 Deleted/Mutated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SSX-SS18</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TGFBR3-MGEA5</code></td><td><code>ncit:C175987</code></td><td></td></tr>
<tr><td><code>VGLL2 Rearranged</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>INSTRuCT</code></td><td><code>ncit:C192762</code></td><td></td></tr>
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
<tr><td><code>Prephase</code></td><td><code>ncit:C168826</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-cytodifferentiationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-cytodifferentiationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-cytodifferentiationenum')">×</button>
<h3><code>CytodifferentiationEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>3</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-depthenum" class="enum-modal" onclick="closeEnumModal('enum-modal-depthenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-depthenum')">×</button>
<h3><code>DepthEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Deep</code></td><td><code>ncit:C25240</code></td><td></td></tr>
<tr><td><code>Superficial</code></td><td><code>ncit:C25239</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Adult Fibrosarcoma</code></td><td><code>ncit:C7809</code></td><td></td></tr>
<tr><td><code>Alveolar Soft-Part Sarcoma</code></td><td><code>ncit:C3750</code></td><td></td></tr>
<tr><td><code>Angiomatoid Fibrous Histiocytoma</code></td><td><code>ncit:C6494</code></td><td></td></tr>
<tr><td><code>Angiosarcoma Of Soft Tissue</code></td><td><code>ncit:C121671</code></td><td></td></tr>
<tr><td><code>Atypical Fibroxanthoma</code></td><td><code>ncit:C4246</code></td><td></td></tr>
<tr><td><code>Atypical Lipomatous Tumor</code></td><td><code>ncit:C6505</code></td><td></td></tr>
<tr><td><code>Clear Cell Sarcoma Of Soft Tissue</code></td><td><code>ncit:C3745</code></td><td></td></tr>
<tr><td><code>Composite Hemangioendothelioma</code></td><td><code>ncit:C45475</code></td><td></td></tr>
<tr><td><code>Dedifferentiated Liposarcoma</code></td><td><code>ncit:C3704</code></td><td></td></tr>
<tr><td><code>Dermatofibrosarcoma Protuberans</code></td><td><code>ncit:C4683</code></td><td></td></tr>
<tr><td><code>Desmoid-Type Fibromatosis</code></td><td><code>ncit:C9182</code></td><td></td></tr>
<tr><td><code>Desmoplastic Small Round Cell Tumor</code></td><td><code>icdo:8806/3</code></td><td></td></tr>
<tr><td><code>Ectomesenchymoma</code></td><td><code>ncit:C4716</code></td><td></td></tr>
<tr><td><code>Epithelioid Haemangioendothelioma</code></td><td><code>ncit:C3800</code></td><td></td></tr>
<tr><td><code>Epithelioid Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>ncit:C6561</code></td><td></td></tr>
<tr><td><code>Extra-Renal Rhabdoid Tumor</code></td><td><code>ncit:C6586</code></td><td></td></tr>
<tr><td><code>Extraskeletal Mesenchymal Chondrosarcoma</code></td><td><code>ncit:C27481</code></td><td></td></tr>
<tr><td><code>Extraskeletal Myxoid Chondrosarcoma</code></td><td><code>ncit:C27502</code></td><td></td></tr>
<tr><td><code>Extraskeletal Osteosarcoma</code></td><td><code>ncit:C8810</code></td><td></td></tr>
<tr><td><code>Fibrosarcomatous Dermatofibrosarcoma Protuberans</code></td><td><code>ncit:C27547</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Stromal Tumor, Malignant</code></td><td><code>ncit:C53999</code></td><td></td></tr>
<tr><td><code>Gastrointestinal Stromal Tumor, Uncertain Malignant Potential</code></td><td><code>ncit:C54000</code></td><td></td></tr>
<tr><td><code>Giant Cell Fibroblastoma</code></td><td><code>ncit:C4700</code></td><td></td></tr>
<tr><td><code>Giant Cell Tumor of Soft Tissue</code></td><td><code>ncit:C49107</code></td><td></td></tr>
<tr><td><code>Glomangiomatosis</code></td><td><code>ncit:C27496</code></td><td></td></tr>
<tr><td><code>Glomus Tumor</code></td><td><code>ncit:C27496</code></td><td></td></tr>
<tr><td><code>Hemosiderotic Fibrolipomatous Tumor</code></td><td><code>ncit:C121752</code></td><td></td></tr>
<tr><td><code>Infantile Fibrosarcoma</code></td><td><code>icdo:8814/3</code></td><td></td></tr>
<tr><td><code>Inflammatory Myofibroblastic Tumor</code></td><td><code>ncit:C6481</code></td><td></td></tr>
<tr><td><code>Intimal Sarcoma</code></td><td><code>icdo:9137/3</code></td><td></td></tr>
<tr><td><code>Kaposi Sarcoma</code></td><td><code>icdo:9140/3</code></td><td></td></tr>
<tr><td><code>Kaposiform Hemangioendothelioma</code></td><td><code>ncit:C27510</code></td><td></td></tr>
<tr><td><code>Leiomyosarcoma</code></td><td><code>ncit:C3158</code></td><td></td></tr>
<tr><td><code>Lipofibromatosis</code></td><td><code>ncit:C99180</code></td><td></td></tr>
<tr><td><code>Liposarcoma, NOS</code></td><td><code>ncit:C3194</code></td><td></td></tr>
<tr><td><code>Low-Grade Fibromyxoid Sarcoma</code></td><td><code>ncit:C45202</code></td><td></td></tr>
<tr><td><code>Low-Grade Myofibroblastic Sarcoma</code></td><td><code>ncit:C49024</code></td><td></td></tr>
<tr><td><code>Malignant Glomus Tumor</code></td><td><code>ncit:C4221</code></td><td></td></tr>
<tr><td><code>Malignant Granular Cell Tumor</code></td><td><code>ncit:C4336</code></td><td></td></tr>
<tr><td><code>Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>icdo:9540/3</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Malignant Triton Tumor</code></td><td><code>ncit:C4335</code></td><td></td></tr>
<tr><td><code>Mixed Tumor NOS, Malignant</code></td><td><code>ncit:C3729</code></td><td></td></tr>
<tr><td><code>Mixed Tumour NOS</code></td><td><code>ncit:C121786</code></td><td></td></tr>
<tr><td><code>Myoepithelioma</code></td><td><code>ncit:C40392</code></td><td></td></tr>
<tr><td><code>Myoepithelioma Carcinoma</code></td><td><code>ncit:C7596</code></td><td></td></tr>
<tr><td><code>Myxofibrosarcoma</code></td><td><code>ncit:C6496</code></td><td></td></tr>
<tr><td><code>Myxoid Liposarcoma</code></td><td><code>ncit:C27781</code></td><td></td></tr>
<tr><td><code>Myxoinflammatory Fibroblastic Sarcoma/Atypical Myxoinflammatory Fibroblastic Tumor</code></td><td><code>ncit:C49025</code></td><td></td></tr>
<tr><td><code>Ossifying Fibromyxoid Tumor</code></td><td><code>ncit:C6582</code></td><td></td></tr>
<tr><td><code>Ossifying Fibromyxoid Tumor, Malignant</code></td><td><code>ncit:C121774</code></td><td></td></tr>
<tr><td><code>Palmar/Plantar Fibromatosis</code></td><td><code>ncit:C4680</code></td><td></td></tr>
<tr><td><code>Papillary Intralymphatic Angioendothelioma</code></td><td><code>ncit:C7526</code></td><td></td></tr>
<tr><td><code>Pecoma NOS, Benign</code></td><td><code>ncit:C121791</code></td><td></td></tr>
<tr><td><code>Pecoma NOS, Malignant</code></td><td><code>ncit:C121792</code></td><td></td></tr>
<tr><td><code>Phosphaturic Mesenchymal Tumor, Benign</code></td><td><code>ncit:C121788</code></td><td></td></tr>
<tr><td><code>Phosphaturic Mesenchymal Tumor, Malignant</code></td><td><code>ncit:C121789</code></td><td></td></tr>
<tr><td><code>Pleomorphic Liposarcoma</code></td><td><code>icdo:8854/3</code></td><td></td></tr>
<tr><td><code>Plexiform Fibrohistiocytic Tumor</code></td><td><code>ncit:C6493</code></td><td></td></tr>
<tr><td><code>Pseudomyogenic Hemangioendothelioma</code></td><td><code>ncit:C121668</code></td><td></td></tr>
<tr><td><code>Retiform Hemangioendothelioma</code></td><td><code>ncit:C27511</code></td><td></td></tr>
<tr><td><code>Sclerosing Epithelioid Fibrosarcoma</code></td><td><code>ncit:C49027</code></td><td></td></tr>
<tr><td><code>Soft Tissue Chondroma</code></td><td><code>ncit:C9482</code></td><td></td></tr>
<tr><td><code>Solitary Fibrous Tumor</code></td><td><code>ncit:C7634</code></td><td>(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'</td></tr>
<tr><td><code>Solitary Fibrous Tumor, Malignant</code></td><td><code>icdo:8815/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, NOS</code></td><td><code>ncit:C3400</code></td><td></td></tr>
<tr><td><code>Tenosynovial Giant Cell Tumor Diffuse Type</code></td><td><code>ncit:C3401</code></td><td></td></tr>
<tr><td><code>Tenosynovial Giant Cell Tumor Localized Type</code></td><td><code>ncit:C6532</code></td><td></td></tr>
<tr><td><code>Tenosynovial Giant Cell Tumor Malignant</code></td><td><code>ncit:C6535</code></td><td></td></tr>
<tr><td><code>Undifferentiated Epithelioid Sarcoma</code></td><td><code>ncit:C121802</code></td><td></td></tr>
<tr><td><code>Undifferentiated Pleomorphic Sarcoma</code></td><td><code>ncit:C4247</code></td><td></td></tr>
<tr><td><code>Undifferentiated Round Cell Sarcoma</code></td><td><code>ncit:C121799</code></td><td></td></tr>
<tr><td><code>Undifferentiated Sarcoma, NOS</code></td><td><code>ncit:C121804</code></td><td></td></tr>
<tr><td><code>Undifferentiated Spindle Cell Sarcoma</code></td><td><code>ncit:C121797</code></td><td></td></tr>
<tr><td><code>Well Differentiated Liposarcoma</code></td><td><code>ncit:C6505</code></td><td></td></tr>
<tr><td><code>Epithelioid Sarcoma</code></td><td><code>icdo:8804/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Spindle Cell</code></td><td><code>icdo:9041/3</code></td><td></td></tr>
<tr><td><code>Synovial Sarcoma, Biphasic</code></td><td><code>icdo:9043/3</code></td><td></td></tr>
<tr><td><code>Pigmented Dermatofibrosarcoma Protuberans</code></td><td><code>icdo:8833/3</code></td><td></td></tr>
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
<tr><td><code>NRSTS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdominal Wall</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain/Leptomeninges</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Head</code></td><td><code>ncit:C12419</code></td><td></td></tr>
<tr><td><code>Hip</code></td><td><code>ncit:C64193</code></td><td></td></tr>
<tr><td><code>Intraperitoneal</code></td><td><code>ncit:C13352</code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code>ncit:C105579</code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lower Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code>ncit:C129461</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code>ncit:C33301</code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td>(ews) ConsortiumNote: Included so that peritoneal effusions can be reported.</td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td>(ews) ConsortiumNote: Included so that pleural effusions can be reported.<br>(os) ConsortiumNote: Included so that pleural effusions can be reported.</td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code>ncit:C12783</code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code>ncit:C32141</code></td><td></td></tr>
<tr><td><code>Urogenital</code></td><td><code>ncit:C25350</code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>Other</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-geneticanalysisspecimenenum" class="enum-modal" onclick="closeEnumModal('enum-modal-geneticanalysisspecimenenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-geneticanalysisspecimenenum')">×</button>
<h3><code>GeneticAnalysisSpecimenEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Primary Tumor</code></td><td><code>ncit:C8509</code></td><td></td></tr>
<tr><td><code>Metastatic Tumor</code></td><td><code>ncit:C3261</code></td><td></td></tr>
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
<tr><td><code>FNCLCC &gt;&gt; Grade 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FNCLCC &gt;&gt; Grade 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FNCLCC &gt;&gt; Grade 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>FNCLCC &gt;&gt; Grade GX</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3><code>MedicalHistoryConditionEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>APC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Costello</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DICER1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Li-Fraumeni Syndrome</code></td><td><code>ncit:C3476</code></td><td></td></tr>
<tr><td><code>Malignant Peripheral Nerve Sheath Tumor</code></td><td><code>ncit:C3798</code></td><td></td></tr>
<tr><td><code>NF-1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RB1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Secondary Malignancy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-mitoticrateenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mitoticrateenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mitoticrateenum')">×</button>
<h3><code>MitoticRateEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Score 1: 0-9 Mitoses per 10 HPF</code></td><td><code>ncit:C138983</code></td><td></td></tr>
<tr><td><code>Score 2: 10-19 Mitoses per 10 HPF</code></td><td><code>ncit:C138984</code></td><td></td></tr>
<tr><td><code>Score 3: &gt; 19 Mitoses per 10 HPF</code></td><td><code>ncit:C138985</code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>&lt;50% Necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;=50% Necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Score 0: No Necrosis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
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
<tr><td><code>Abdominal Wall</code></td><td><code>ncit:C77608</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain/Leptomeninges</code></td><td><code>ncit:C32979</code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code>ncit:C12971</code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code>ncit:C62484</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C160424</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Head</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hip</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraperitoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lower Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code>ncit:C12469</code></td><td></td></tr>
<tr><td><code>Retroperitoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code>ncit:C25203</code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code>ncit:C32141</code></td><td></td></tr>
<tr><td><code>Urogenital</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-responseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responseenum')">×</button>
<h3><code>ResponseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Not Evaluable</code></td><td><code>ncit:C62222</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Complete Response</code></td><td><code>ncit:C4870</code></td><td>(hl) ConsortiumNote: For HL, refers to end of chemotherapy or late response.</td></tr>
<tr><td><code>System NOS &gt;&gt; Partial Response</code></td><td><code>ncit:C18058</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Progressive Disease</code></td><td><code>ncit:C35571</code></td><td></td></tr>
<tr><td><code>System NOS &gt;&gt; Stable Disease</code></td><td><code>ncit:C18213</code></td><td></td></tr>
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
<tr><td><code>Abdominal Wall</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brain/Leptomeninges</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Breast</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chest Wall</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Distant Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Head</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Hip</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intraperitoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intrathoracic</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lower Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Peritoneum</code></td><td><code>ncit:C12770</code></td><td></td></tr>
<tr><td><code>Pleura</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Urogenital</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
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
<tr><td><code>Head and Neck</code></td><td><code>ncit:C12418</code></td><td></td></tr>
<tr><td><code>Limbs</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
<tr><td><code>&lt;=5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>&gt;5 cm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-txpriorresponseenum" class="enum-modal" onclick="closeEnumModal('enum-modal-txpriorresponseenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-txpriorresponseenum')">×</button>
<h3><code>TxPriorResponseEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Chemoradiotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Chemotherapy</code></td><td><code></code></td><td></td></tr>
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
    "nrsts": {
      "name": "nrsts",
      "title": "Non-rhabdomyosarcoma Soft Tissue Sarcomas",
      "description": "The NRSTS view of the PCDC data model represents consensus data modeling by an international group of pediatric non-rhabdomyosarcoma soft tissue sarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors."
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
        "efs_censor_status"
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
        "medical_history_condition"
      ],
      "comments": [
        "(os) ConsortiumNote: No AOST0331/EURAMOS1 data"
      ],
      "annotations": {
        "domain": "demographics"
      }
    },
    "GeneticAnalysis": {
      "slots": [
        "age_at_genetic_analysis",
        "genetic_analysis_specimen",
        "alteration",
        "cytodifferentiation",
        "mitotic_rate"
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
    "DiseaseSiteAssessment": {
      "slots": [
        "age_at_disease_site_assessment",
        "site_classification",
        "disease_site",
        "site_other",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "tumor_size",
        "invasiveness",
        "depth"
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
        "site_classification",
        "procedure_site",
        "site_other",
        "margins"
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
    "RadiationTherapy": {
      "slots": [
        "age_at_rt_start",
        "site_classification",
        "rt_site",
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
    "SubjectResponse": {
      "slots": [
        "age_at_response",
        "tx_prior_response",
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
    "SubsequentMalignantNeoplasm": {
      "slots": [
        "age_at_smn",
        "smn_site"
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
    "efs_censor_status": {
      "slot_uri": "",
      "range": "EfsCensorStatusEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "npc,os"
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
    "measurement_unit": {
      "slot_uri": "",
      "range": "LesionMeasurementUnitEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "technique": {
      "slot_uri": "ncit:C15313",
      "range": "TechniqueEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "npc",
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
    "mitotic_rate": {
      "slot_uri": "ncit:C138982",
      "range": "MitoticRateEnum",
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
    "rt_site": {
      "slot_uri": "ncit:C173281",
      "range": "RtSiteEnum",
      "comments": [],
      "annotations": {}
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
    "age_at_procedure": {
      "slot_uri": "ncit:C175008",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "age_at_disease_site_assessment": {
      "slot_uri": "ncit:C174997",
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
    "age_at_genetic_analysis": {
      "slot_uri": "ncit:C168848",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups,ls"
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
    "measurement1": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb",
        "tier_optional": "npc,ls"
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
    "site_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "lt"
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
    "genetic_analysis_specimen": {
      "slot_uri": "ncit:C70713",
      "range": "GeneticAnalysisSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
      }
    },
    "tx_prior_response": {
      "slot_uri": "",
      "range": "TxPriorResponseEnum",
      "comments": [],
      "annotations": {}
    },
    "depth": {
      "slot_uri": "ncit:C25333",
      "range": "DepthEnum",
      "comments": [],
      "annotations": {}
    },
    "cytodifferentiation": {
      "slot_uri": "",
      "range": "CytodifferentiationEnum",
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
    "current_qty_value": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "invasiveness": {
      "slot_uri": "",
      "range": "InvasivenessEnum",
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
    "biospecimen_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "measurement2": {
      "slot_uri": "ncit:C96684",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_priority": "rb",
        "tier_optional": "npc,ls"
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
    "necrosis_pct": {
      "slot_uri": "ncit:C159481",
      "range": "decimal",
      "comments": [
        "(os) ConsortiumNote: This should be the mean, not the min or max.",
        "(ews) ConsortiumNote: Include one decimal place."
      ],
      "annotations": {}
    },
    "biospecimen_media": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "procedure_site": {
      "slot_uri": "ncit:C157120",
      "range": "ProcedureSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt",
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
    "biospecimen_container_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "HistologyGradeEnum": {
      "permissible_values": {
        "FNCLCC >> Grade 1": {
          "meaning": "",
          "comments": []
        },
        "FNCLCC >> Grade 2": {
          "meaning": "",
          "comments": []
        },
        "FNCLCC >> Grade 3": {
          "meaning": "",
          "comments": []
        },
        "FNCLCC >> Grade GX": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
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
        "Prephase": {
          "meaning": "ncit:C168826",
          "comments": []
        }
      }
    },
    "MitoticRateEnum": {
      "permissible_values": {
        "Score 1: 0-9 Mitoses per 10 HPF": {
          "meaning": "ncit:C138983",
          "comments": []
        },
        "Score 2: 10-19 Mitoses per 10 HPF": {
          "meaning": "ncit:C138984",
          "comments": []
        },
        "Score 3: > 19 Mitoses per 10 HPF": {
          "meaning": "ncit:C138985",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "NecrosisEnum": {
      "permissible_values": {
        "<50% Necrosis": {
          "meaning": "",
          "comments": []
        },
        ">=50% Necrosis": {
          "meaning": "",
          "comments": []
        },
        "Score 0: No Necrosis": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Abdominal Wall": {
          "meaning": "ncit:C28256",
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
        "Brain/Leptomeninges": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Breast": {
          "meaning": "ncit:C12971",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C12745",
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
        "Head": {
          "meaning": "ncit:C12419",
          "comments": []
        },
        "Hip": {
          "meaning": "ncit:C64193",
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
        "Leg": {
          "meaning": "ncit:C32974",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Lower Arm": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "ncit:C129461",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
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
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": [
            "(ews) ConsortiumNote: Included so that pleural effusions can be reported.",
            "(os) ConsortiumNote: Included so that pleural effusions can be reported."
          ]
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Shoulder": {
          "meaning": "ncit:C12783",
          "comments": []
        },
        "Thigh": {
          "meaning": "ncit:C33763",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "ncit:C32141",
          "comments": []
        },
        "Urogenital": {
          "meaning": "ncit:C25350",
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
    "TxPriorResponseEnum": {
      "permissible_values": {
        "Chemoradiotherapy": {
          "meaning": "",
          "comments": []
        },
        "Chemotherapy": {
          "meaning": "",
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
        "ALK Rearrangement": {
          "meaning": "ncit:C129574",
          "comments": []
        },
        "ASPSCR1-TFE3": {
          "meaning": "ncit:C99705",
          "comments": []
        },
        "BCOR ITT Rearranged": {
          "meaning": "",
          "comments": []
        },
        "BCOR-CCNB3": {
          "meaning": "",
          "comments": []
        },
        "CIC-DUX4": {
          "meaning": "ncit:C139663",
          "comments": []
        },
        "ETV6 Rearranged": {
          "meaning": "ncit:C155992",
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
        "EWSR1-ETV1": {
          "meaning": "ncit:C99259",
          "comments": []
        },
        "EWSR1-ETV4": {
          "meaning": "ncit:C99262",
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
        "EWSR1-ZNF444": {
          "meaning": "ncit:C139731",
          "comments": []
        },
        "FOXO1 Rearranged": {
          "meaning": "ncit:C175960",
          "comments": []
        },
        "FUS-CREB3L2": {
          "meaning": "ncit:C99283",
          "comments": []
        },
        "NTRK Rearranged": {
          "meaning": "ncit:C171043",
          "comments": []
        },
        "ROS1 Rearranged": {
          "meaning": "ncit:C130236",
          "comments": []
        },
        "SMARCB1 Deleted/Mutated": {
          "meaning": "",
          "comments": []
        },
        "SSX-SS18": {
          "meaning": "",
          "comments": []
        },
        "TGFBR3-MGEA5": {
          "meaning": "ncit:C175987",
          "comments": []
        },
        "VGLL2 Rearranged": {
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
        "Abdominal Wall": {
          "meaning": "",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "",
          "comments": []
        },
        "Bone, NOS": {
          "meaning": "",
          "comments": []
        },
        "Brain/Leptomeninges": {
          "meaning": "",
          "comments": []
        },
        "Breast": {
          "meaning": "",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "",
          "comments": []
        },
        "Distant Nodes": {
          "meaning": "",
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
        "Head": {
          "meaning": "",
          "comments": []
        },
        "Hip": {
          "meaning": "",
          "comments": []
        },
        "Intraperitoneal": {
          "meaning": "",
          "comments": []
        },
        "Intrathoracic": {
          "meaning": "",
          "comments": []
        },
        "Leg": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Liver": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Lower Arm": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Perineum": {
          "meaning": "",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": []
        },
        "Pleura": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneal": {
          "meaning": "",
          "comments": []
        },
        "Shoulder": {
          "meaning": "",
          "comments": []
        },
        "Thigh": {
          "meaning": "",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "",
          "comments": []
        },
        "Urogenital": {
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
    "DepthEnum": {
      "permissible_values": {
        "Deep": {
          "meaning": "ncit:C25240",
          "comments": []
        },
        "Superficial": {
          "meaning": "ncit:C25239",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "CytodifferentiationEnum": {
      "permissible_values": {
        "1": {
          "meaning": "",
          "comments": []
        },
        "2": {
          "meaning": "",
          "comments": []
        },
        "3": {
          "meaning": "",
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
        "Head and Neck": {
          "meaning": "ncit:C12418",
          "comments": []
        },
        "Limbs": {
          "meaning": "",
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
        "Other": {
          "meaning": "ncit:C17649",
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
        "Other": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "ncit:C17998",
          "comments": []
        }
      }
    },
    "DiagnosisEnum": {
      "permissible_values": {
        "Adult Fibrosarcoma": {
          "meaning": "ncit:C7809",
          "comments": []
        },
        "Alveolar Soft-Part Sarcoma": {
          "meaning": "ncit:C3750",
          "comments": []
        },
        "Angiomatoid Fibrous Histiocytoma": {
          "meaning": "ncit:C6494",
          "comments": []
        },
        "Angiosarcoma Of Soft Tissue": {
          "meaning": "ncit:C121671",
          "comments": []
        },
        "Atypical Fibroxanthoma": {
          "meaning": "ncit:C4246",
          "comments": []
        },
        "Atypical Lipomatous Tumor": {
          "meaning": "ncit:C6505",
          "comments": []
        },
        "Clear Cell Sarcoma Of Soft Tissue": {
          "meaning": "ncit:C3745",
          "comments": []
        },
        "Composite Hemangioendothelioma": {
          "meaning": "ncit:C45475",
          "comments": []
        },
        "Dedifferentiated Liposarcoma": {
          "meaning": "ncit:C3704",
          "comments": []
        },
        "Dermatofibrosarcoma Protuberans": {
          "meaning": "ncit:C4683",
          "comments": []
        },
        "Desmoid-Type Fibromatosis": {
          "meaning": "ncit:C9182",
          "comments": []
        },
        "Desmoplastic Small Round Cell Tumor": {
          "meaning": "icdo:8806/3",
          "comments": []
        },
        "Ectomesenchymoma": {
          "meaning": "ncit:C4716",
          "comments": []
        },
        "Epithelioid Haemangioendothelioma": {
          "meaning": "ncit:C3800",
          "comments": []
        },
        "Epithelioid Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "ncit:C6561",
          "comments": []
        },
        "Extra-Renal Rhabdoid Tumor": {
          "meaning": "ncit:C6586",
          "comments": []
        },
        "Extraskeletal Mesenchymal Chondrosarcoma": {
          "meaning": "ncit:C27481",
          "comments": []
        },
        "Extraskeletal Myxoid Chondrosarcoma": {
          "meaning": "ncit:C27502",
          "comments": []
        },
        "Extraskeletal Osteosarcoma": {
          "meaning": "ncit:C8810",
          "comments": []
        },
        "Fibrosarcomatous Dermatofibrosarcoma Protuberans": {
          "meaning": "ncit:C27547",
          "comments": []
        },
        "Gastrointestinal Stromal Tumor, Malignant": {
          "meaning": "ncit:C53999",
          "comments": []
        },
        "Gastrointestinal Stromal Tumor, Uncertain Malignant Potential": {
          "meaning": "ncit:C54000",
          "comments": []
        },
        "Giant Cell Fibroblastoma": {
          "meaning": "ncit:C4700",
          "comments": []
        },
        "Giant Cell Tumor of Soft Tissue": {
          "meaning": "ncit:C49107",
          "comments": []
        },
        "Glomangiomatosis": {
          "meaning": "ncit:C27496",
          "comments": []
        },
        "Glomus Tumor": {
          "meaning": "ncit:C27496",
          "comments": []
        },
        "Hemosiderotic Fibrolipomatous Tumor": {
          "meaning": "ncit:C121752",
          "comments": []
        },
        "Infantile Fibrosarcoma": {
          "meaning": "icdo:8814/3",
          "comments": []
        },
        "Inflammatory Myofibroblastic Tumor": {
          "meaning": "ncit:C6481",
          "comments": []
        },
        "Intimal Sarcoma": {
          "meaning": "icdo:9137/3",
          "comments": []
        },
        "Kaposi Sarcoma": {
          "meaning": "icdo:9140/3",
          "comments": []
        },
        "Kaposiform Hemangioendothelioma": {
          "meaning": "ncit:C27510",
          "comments": []
        },
        "Leiomyosarcoma": {
          "meaning": "ncit:C3158",
          "comments": []
        },
        "Lipofibromatosis": {
          "meaning": "ncit:C99180",
          "comments": []
        },
        "Liposarcoma, NOS": {
          "meaning": "ncit:C3194",
          "comments": []
        },
        "Low-Grade Fibromyxoid Sarcoma": {
          "meaning": "ncit:C45202",
          "comments": []
        },
        "Low-Grade Myofibroblastic Sarcoma": {
          "meaning": "ncit:C49024",
          "comments": []
        },
        "Malignant Glomus Tumor": {
          "meaning": "ncit:C4221",
          "comments": []
        },
        "Malignant Granular Cell Tumor": {
          "meaning": "ncit:C4336",
          "comments": []
        },
        "Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "icdo:9540/3",
          "comments": [
            "(cns) ConsortiumNote: DIAGNOSIS_CATEGORY = 'Other'"
          ]
        },
        "Malignant Triton Tumor": {
          "meaning": "ncit:C4335",
          "comments": []
        },
        "Mixed Tumor NOS, Malignant": {
          "meaning": "ncit:C3729",
          "comments": []
        },
        "Mixed Tumour NOS": {
          "meaning": "ncit:C121786",
          "comments": []
        },
        "Myoepithelioma": {
          "meaning": "ncit:C40392",
          "comments": []
        },
        "Myoepithelioma Carcinoma": {
          "meaning": "ncit:C7596",
          "comments": []
        },
        "Myxofibrosarcoma": {
          "meaning": "ncit:C6496",
          "comments": []
        },
        "Myxoid Liposarcoma": {
          "meaning": "ncit:C27781",
          "comments": []
        },
        "Myxoinflammatory Fibroblastic Sarcoma/Atypical Myxoinflammatory Fibroblastic Tumor": {
          "meaning": "ncit:C49025",
          "comments": []
        },
        "Ossifying Fibromyxoid Tumor": {
          "meaning": "ncit:C6582",
          "comments": []
        },
        "Ossifying Fibromyxoid Tumor, Malignant": {
          "meaning": "ncit:C121774",
          "comments": []
        },
        "Palmar/Plantar Fibromatosis": {
          "meaning": "ncit:C4680",
          "comments": []
        },
        "Papillary Intralymphatic Angioendothelioma": {
          "meaning": "ncit:C7526",
          "comments": []
        },
        "Pecoma NOS, Benign": {
          "meaning": "ncit:C121791",
          "comments": []
        },
        "Pecoma NOS, Malignant": {
          "meaning": "ncit:C121792",
          "comments": []
        },
        "Phosphaturic Mesenchymal Tumor, Benign": {
          "meaning": "ncit:C121788",
          "comments": []
        },
        "Phosphaturic Mesenchymal Tumor, Malignant": {
          "meaning": "ncit:C121789",
          "comments": []
        },
        "Pleomorphic Liposarcoma": {
          "meaning": "icdo:8854/3",
          "comments": []
        },
        "Plexiform Fibrohistiocytic Tumor": {
          "meaning": "ncit:C6493",
          "comments": []
        },
        "Pseudomyogenic Hemangioendothelioma": {
          "meaning": "ncit:C121668",
          "comments": []
        },
        "Retiform Hemangioendothelioma": {
          "meaning": "ncit:C27511",
          "comments": []
        },
        "Sclerosing Epithelioid Fibrosarcoma": {
          "meaning": "ncit:C49027",
          "comments": []
        },
        "Soft Tissue Chondroma": {
          "meaning": "ncit:C9482",
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
        "Synovial Sarcoma, NOS": {
          "meaning": "ncit:C3400",
          "comments": []
        },
        "Tenosynovial Giant Cell Tumor Diffuse Type": {
          "meaning": "ncit:C3401",
          "comments": []
        },
        "Tenosynovial Giant Cell Tumor Localized Type": {
          "meaning": "ncit:C6532",
          "comments": []
        },
        "Tenosynovial Giant Cell Tumor Malignant": {
          "meaning": "ncit:C6535",
          "comments": []
        },
        "Undifferentiated Epithelioid Sarcoma": {
          "meaning": "ncit:C121802",
          "comments": []
        },
        "Undifferentiated Pleomorphic Sarcoma": {
          "meaning": "ncit:C4247",
          "comments": []
        },
        "Undifferentiated Round Cell Sarcoma": {
          "meaning": "ncit:C121799",
          "comments": []
        },
        "Undifferentiated Sarcoma, NOS": {
          "meaning": "ncit:C121804",
          "comments": []
        },
        "Undifferentiated Spindle Cell Sarcoma": {
          "meaning": "ncit:C121797",
          "comments": []
        },
        "Well Differentiated Liposarcoma": {
          "meaning": "ncit:C6505",
          "comments": []
        },
        "Epithelioid Sarcoma": {
          "meaning": "icdo:8804/3",
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
        "Pigmented Dermatofibrosarcoma Protuberans": {
          "meaning": "icdo:8833/3",
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
    "ProcedureSiteEnum": {
      "permissible_values": {
        "Abdominal Wall": {
          "meaning": "ncit:C77608",
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
        "Brain/Leptomeninges": {
          "meaning": "ncit:C32979",
          "comments": []
        },
        "Breast": {
          "meaning": "ncit:C12971",
          "comments": []
        },
        "Chest Wall": {
          "meaning": "ncit:C62484",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C160424",
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
        "Head": {
          "meaning": "",
          "comments": []
        },
        "Hip": {
          "meaning": "",
          "comments": []
        },
        "Intraperitoneal": {
          "meaning": "",
          "comments": []
        },
        "Intrathoracic": {
          "meaning": "",
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
        "Lower Arm": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Perineum": {
          "meaning": "",
          "comments": []
        },
        "Peritoneum": {
          "meaning": "ncit:C12770",
          "comments": []
        },
        "Pleura": {
          "meaning": "ncit:C12469",
          "comments": []
        },
        "Retroperitoneal": {
          "meaning": "",
          "comments": []
        },
        "Shoulder": {
          "meaning": "ncit:C25203",
          "comments": []
        },
        "Thigh": {
          "meaning": "ncit:C33763",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "ncit:C32141",
          "comments": []
        },
        "Urogenital": {
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
    "DiseaseGroupEnum": {
      "permissible_values": {
        "NRSTS": {
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
        "Relapse": {
          "meaning": "ncit:C38155",
          "comments": []
        }
      }
    },
    "MedicalHistoryConditionEnum": {
      "permissible_values": {
        "APC": {
          "meaning": "",
          "comments": []
        },
        "Costello": {
          "meaning": "",
          "comments": []
        },
        "DICER1": {
          "meaning": "",
          "comments": []
        },
        "Li-Fraumeni Syndrome": {
          "meaning": "ncit:C3476",
          "comments": []
        },
        "Malignant Peripheral Nerve Sheath Tumor": {
          "meaning": "ncit:C3798",
          "comments": []
        },
        "NF-1": {
          "meaning": "",
          "comments": []
        },
        "RB1": {
          "meaning": "",
          "comments": []
        },
        "Secondary Malignancy": {
          "meaning": "",
          "comments": []
        },
        "Other": {
          "meaning": "ncit:C17649",
          "comments": []
        }
      }
    },
    "TechniqueEnum": {
      "permissible_values": {
        "Brachytherapy": {
          "meaning": "ncit:C15195",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "INSTRuCT": {
          "meaning": "ncit:C192762",
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
        }
      }
    },
    "TumorSizeEnum": {
      "permissible_values": {
        "<=5 cm": {
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