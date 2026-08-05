---
layout: default
title: Neuroblastoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*NBL View*

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
- **Neuroblastoma**
- [Nasopharyngeal Carcinoma](npc)
- [Non-rhabdomyosarcoma Soft Tissue Sarcomas](nrsts)
- [Osteosarcoma](os)
- [Cancer Predisposition](pre)
- [Retinoblastoma](rb)
- [Rhabdomyosarcoma](rms)

</details>

The NBL view of the PCDC data model represents consensus data modeling by an international group of pediatric neuroblastoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Neuroblastoma Risk Group (INRG). It is based on the collective requirements of its contributors.


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

## StudyMetadata

| Slot | Range | Description |
|---|---|---|
| `study_id` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-studyidenum')">StudyIdEnum</button> |  |
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
| `efs_censor_status` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-efscensorstatusenum')">EfsCensorStatusEnum</button> |  |
| `age_at_censor_status` | `integer` |  |

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
| `revised_inpc` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-revisedinpcenum')">RevisedInpcEnum</button> |  |

## DiseaseCharacteristics

| Slot | Range | Description |
|---|---|---|
| `initial_treatment_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-initialtreatmentcategoryenum')">InitialTreatmentCategoryEnum</button> |  |
| `mki` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mkienum')">MkiEnum</button> |  |

## DiseaseSiteAssessment

| Slot | Range | Description |
|---|---|---|
| `age_at_disease_site_assessment` | `integer` |  |
| `tumor_state` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `disease_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diseasesiteenum')">DiseaseSiteEnum</button> |  |
| `site_other` | `string` |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `stage` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-stageenum')">StageEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `cycle_number` | `decimal` |  |
| `response_category` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsecategoryenum')">ResponseCategoryEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `mibg_score_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-mibgscoretypeenum')">MibgScoreTypeEnum</button> |  |
| `mibg_score` | `decimal` |  |

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
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | `AlterationEnum` |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |
| `hgvs_protein` | `string` |  |
| `dna_index` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-dnaindexenum')">DnaIndexEnum</button> |  |
| `dna_index_numeric` | `decimal` |  |
| `allelic_ratio` | `decimal` |  |

## LaboratoryTest

| Slot | Range | Description |
|---|---|---|
| `age_at_lab` | `integer` |  |
| `laboratory_test` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-laboratorytestenum')">LaboratoryTestEnum</button> |  |
| `result_numeric` | `decimal` |  |

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
<tr><td><code>Treatment-Related Mortality</code></td><td><code>ncit:C166165</code></td><td>D4CGNote: Use the Adverse Events table for any additional details. Do not use CAUSE_OF_DEATH_DETAIL.</td></tr>
<tr><td><code>Other</code></td><td><code>ncit:C17649</code></td><td></td></tr>
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
<tr><td><code>INRG</code></td><td><code>ncit:C192762</code></td><td></td></tr>
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
<tr><td><code>Ganglioneuroblastoma, Intermixed (Schwannian Stroma-Rich)</code></td><td><code>ncit:C42057</code></td><td></td></tr>
<tr><td><code>Ganglioneuroblastoma, Nodular (Composite)</code></td><td><code>ncit:C42058</code></td><td></td></tr>
<tr><td><code>Ganglioneuroma (Schwannian Stroma-Dominant), Maturing Subtype</code></td><td><code>ncit:C42064</code></td><td></td></tr>
<tr><td><code>Neuroblastoma (Schwannian Stroma Poor)</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>NBL</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Adrenal Gland</code></td><td><code>ncit:C12666</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Central Nervous System</code></td><td><code>ncit:C12438</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Liver</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Skin</code></td><td><code>ncit:C12470</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-dnaindexenum" class="enum-modal" onclick="closeEnumModal('enum-modal-dnaindexenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-dnaindexenum')">×</button>
<h3><code>DnaIndexEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>DNA Index &lt;/= 1 (Hypodiploid, Diploid)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>DNA Index &gt;1 (Hyperdiploid)</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Blood</code></td><td><code>ncit:C17610</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Cerebrospinal Fluid</code></td><td><code>ncit:C12692</code></td><td></td></tr>
<tr><td><code>Lymph Node</code></td><td><code>ncit:C12745</code></td><td></td></tr>
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
<tr><td><code>INPC &gt;&gt; Differentiating</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INPC &gt;&gt; Undifferentiated or Poorly Differentiated</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(nbl) ConsortiumNote: Use for 'Cannot be determined'</td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-initialtreatmentcategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-initialtreatmentcategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-initialtreatmentcategoryenum')">×</button>
<h3><code>InitialTreatmentCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Conventional-dose chemotherapy (2-8 cycles) plus surgery</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intensive multi-modality therapy: no stem cell or bone marrow transplant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intensive multi-modality therapy: plus stem cell or bone marrow transplant</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intensive multi-modality therapy: plus stem cell or bone marrow transplant and anti-GD2 antibody</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intensive multi-modality therapy: specific type unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>None (observation)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Surgery alone</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Ferritin</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LDH</code></td><td><code>ncit:C64855</code></td><td></td></tr>
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

<div id="enum-modal-mibgscoretypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-mibgscoretypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mibgscoretypeenum')">×</button>
<h3><code>MibgScoreTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>MIBG Curie Score</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MIBG SIOPEN Score</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-mkienum" class="enum-modal" onclick="closeEnumModal('enum-modal-mkienum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-mkienum')">×</button>
<h3><code>MkiEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>High (&gt;4% or &gt;200/5,000 cells)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Intermediate (2-4% or 100 to &lt;200/5,000 cells)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Low (&lt;2% or &lt;100/5,000 cells)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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

<div id="enum-modal-responsecategoryenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsecategoryenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsecategoryenum')">×</button>
<h3><code>ResponseCategoryEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Bone Marrow Response</code></td><td><code>ncit:C173307</code></td><td></td></tr>
<tr><td><code>Metastatic Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Overall Response</code></td><td><code>ncit:C96613</code></td><td></td></tr>
<tr><td><code>Primary Site Response</code></td><td><code>ncit:C200253</code></td><td></td></tr>
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
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; Complete Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; Mixed Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; No Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Brodeur 1993 &gt;&gt; Very Good Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Park 2017 &gt;&gt; Minimal Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Park 2017 &gt;&gt; Minor Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Park 2017 &gt;&gt; Partial Response</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Park 2017 &gt;&gt; Progressive Disease</code></td><td><code></code></td><td></td></tr>
<tr><td><code>INRC, Park 2017 &gt;&gt; Stable Disease</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-revisedinpcenum" class="enum-modal" onclick="closeEnumModal('enum-modal-revisedinpcenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-revisedinpcenum')">×</button>
<h3><code>RevisedInpcEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Favorable</code></td><td><code>ncit:C102560</code></td><td></td></tr>
<tr><td><code>Unfavorable</code></td><td><code>ncit:C102561</code></td><td></td></tr>
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
<tr><td><code>Metastatic</code></td><td><code>ncit:C3261</code></td><td></td></tr>
<tr><td><code>Primary</code></td><td><code>ncit:C8509</code></td><td></td></tr>
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
<tr><td><code>Evans &gt;&gt; Stage 1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Evans &gt;&gt; Stage 4s</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>0892</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0896</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0901</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0902</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0911</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0914</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0924</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0925</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0926</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0927</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0931</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0935</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0936</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0937</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0961</code></td><td><code></code></td><td></td></tr>
<tr><td><code>0962</code></td><td><code></code></td><td></td></tr>
<tr><td><code>09709</code></td><td><code></code></td><td></td></tr>
<tr><td><code>099</code></td><td><code></code></td><td></td></tr>
<tr><td><code>321P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>321P2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>321P3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>321P4</code></td><td><code></code></td><td></td></tr>
<tr><td><code>323P</code></td><td><code></code></td><td></td></tr>
<tr><td><code>3881</code></td><td><code></code></td><td></td></tr>
<tr><td><code>3891</code></td><td><code></code></td><td></td></tr>
<tr><td><code>3951</code></td><td><code></code></td><td></td></tr>
<tr><td><code>461</code></td><td><code></code></td><td></td></tr>
<tr><td><code>4941</code></td><td><code></code></td><td></td></tr>
<tr><td><code>4941L</code></td><td><code></code></td><td></td></tr>
<tr><td><code>7942</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8105</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8340</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8441</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8605</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8607</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8661</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8671</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8741</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8742</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8743</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8863</code></td><td><code></code></td><td></td></tr>
<tr><td><code>8970</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9000</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9047</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9072</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9075</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9082</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9140</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9243</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9244</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9248</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9262</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9272</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9275</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9280</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9284</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9285</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9340</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9341</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9342</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9343</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9346</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9347</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9360</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9361</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9372</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9375</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9376</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9382</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9464</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9466</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9470</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9571</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9572</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9579</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9581</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9640</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9670</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9675</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9900</code></td><td><code></code></td><td></td></tr>
<tr><td><code>9907</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A0935A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A09713</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3961</code></td><td><code></code></td><td></td></tr>
<tr><td><code>A3973</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AADM01P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0232</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL03B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL0434</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AALL08B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML00P2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML03P1</code></td><td><code>ncit:C168936</code></td><td></td></tr>
<tr><td><code>AAML0531</code></td><td><code>ncit:C168937</code></td><td></td></tr>
<tr><td><code>AAML05P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML07P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AAML1031</code></td><td><code>ncit:C168938</code></td><td></td></tr>
<tr><td><code>AB9804</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ABTR01B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ABTR04B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL0423</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL0431</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL05C1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL0934</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL0935</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL1031</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL1032</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL1034</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL15N1CD</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL1633</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACCL21C2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ACNS02B3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0016</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0017</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0018</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0122</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0211</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0212</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0214</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0215</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0314</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0316</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0413</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0414</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0416</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0421</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0516</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0517</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0524</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0525</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0612</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL06B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0714</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0812</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0813</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0816</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0821</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0911</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0912</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0916</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0918</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL0921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1011</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1013</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1014</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1111</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1112</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1115</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1211</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1212</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1213</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1312</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1314</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1315</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1411</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1412</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1414</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1416</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1513</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1522</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1615</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ADVL1622</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEPI07N1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AEWS07B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AGCT1531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AHEP1531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ALTE03N1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ALTE05N1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ALTE15N2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ALTE1621</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0032</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00P2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL00P3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL02P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0321</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0322</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0421</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0532</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0621</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL0931</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL09P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1021</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1221</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1232</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL12P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL17P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL1821</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANBL19P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANUR0631</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ANUR1131</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AOST06B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC14B1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621F</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621H</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621I</code></td><td><code></code></td><td></td></tr>
<tr><td><code>APEC1621SC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AREN0321</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AREN03B2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AS942</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AS972</code></td><td><code></code></td><td></td></tr>
<tr><td><code>AS9801</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B003</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B903</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B904</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B925</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B947</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B953</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B954</code></td><td><code></code></td><td></td></tr>
<tr><td><code>B973</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9501</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9602</code></td><td><code></code></td><td></td></tr>
<tr><td><code>E04</code></td><td><code></code></td><td></td></tr>
<tr><td><code>E15</code></td><td><code></code></td><td></td></tr>
<tr><td><code>E18</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ENSG5</code></td><td><code></code></td><td></td></tr>
<tr><td><code>I03</code></td><td><code></code></td><td></td></tr>
<tr><td><code>LNESG1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>N891</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB2004-HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB2005</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB2008</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB2012</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB84</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB8814</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB91</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NB97</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9462</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9480</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9485</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9641</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9749</code></td><td><code>ncit:C177340</code></td><td></td></tr>
<tr><td><code>P9761</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9772</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9851</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9963</code></td><td><code></code></td><td></td></tr>
<tr><td><code>P9972</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PEPN2011</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PEPN2111</code></td><td><code></code></td><td></td></tr>
<tr><td><code>POG-8844</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R9702</code></td><td><code></code></td><td></td></tr>
<tr><td><code>S31</code></td><td><code></code></td><td></td></tr>
<tr><td><code>S901</code></td><td><code></code></td><td></td></tr>
<tr><td><code>S912</code></td><td><code></code></td><td></td></tr>
<tr><td><code>S921</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOPEN HR-NBL1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>SIOPEN-EUNB</code></td><td><code></code></td><td></td></tr>
<tr><td><code>X0942</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Arm A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arm B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arm C</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arm D</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Arm E</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Assigned to Regimen B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Baseline Treatment with 2 cycles</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Baseline Treatment with 4 cycles</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Baseline Treatment with 8 cycles</code></td><td><code></code></td><td></td></tr>
<tr><td><code>No cisRA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-randomized conventional chemotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Non-randomly assigned Single HSCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Randomized</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Purged</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>R3</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RA only</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RA+anti-GD2</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Randomized ablative chemotherapy with BMT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Randomized conventional chemotherapy</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Randomized to Regimen B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Randomized to Single HSCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Randomized to Tandem HSCT</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Regimen A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Regimen B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unpurged</code></td><td><code></code></td><td></td></tr>
<tr><td><code>cisRA</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Stratum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Treatment Arm</code></td><td><code></code></td><td></td></tr>
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
    "nbl": {
      "name": "nbl",
      "title": "Neuroblastoma",
      "description": "The NBL view of the PCDC data model represents consensus data modeling by an international group of pediatric neuroblastoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Neuroblastoma Risk Group (INRG). It is based on the collective requirements of its contributors."
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
    "LaboratoryTest": {
      "slots": [
        "age_at_lab",
        "laboratory_test",
        "result_numeric"
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
        "genetic_analysis_specimen",
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "chromosome",
        "gene",
        "gene_fusion_partner",
        "hgvs_protein",
        "dna_index",
        "dna_index_numeric",
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
        "histology_grade",
        "revised_inpc"
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
        "site_classification",
        "disease_site",
        "site_other"
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
        "initial_treatment_category",
        "mki"
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
    "SubjectResponse": {
      "slots": [
        "cycle_number",
        "response_category",
        "response",
        "mibg_score_type",
        "mibg_score"
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
    "external_links": {
      "slot_uri": "",
      "range": "string",
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
    "alteration_type": {
      "slot_uri": "ncit:C13202",
      "range": "AlterationTypeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "aml",
        "tier_optional": "rb,ls"
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
    "dna_index_numeric": {
      "slot_uri": "ncit:C86972",
      "range": "decimal",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "external_resource_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
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
    "external_subject_submitter_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
    "external_resource_name": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
      }
    },
    "initial_treatment_category": {
      "slot_uri": "",
      "range": "InitialTreatmentCategoryEnum",
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
    "histology_grade": {
      "slot_uri": "ncit:C18000",
      "range": "HistologyGradeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa",
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
    "chromosome": {
      "slot_uri": "ncit:C13202",
      "range": "ChromosomeEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "rb,aml",
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
    "response": {
      "slot_uri": "ncit:C50995",
      "range": "ResponseEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl,npc",
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
    "age_at_disease_site_assessment": {
      "slot_uri": "ncit:C174997",
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
    "revised_inpc": {
      "slot_uri": "",
      "range": "RevisedInpcEnum",
      "comments": [],
      "annotations": {}
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
    "genetic_analysis_specimen": {
      "slot_uri": "ncit:C70713",
      "range": "GeneticAnalysisSpecimenEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,rb"
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
    "alteration_effect": {
      "slot_uri": "ncit:C204195",
      "range": "AlterationEffectEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rb,ls"
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
    "mibg_score_type": {
      "slot_uri": "",
      "range": "MibgScoreTypeEnum",
      "comments": [],
      "annotations": {}
    },
    "biospecimen_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "mibg_score": {
      "slot_uri": "",
      "range": "decimal",
      "comments": [],
      "annotations": {}
    },
    "current_qty_unit": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
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
    "hgvs_protein": {
      "slot_uri": "ncit:C97928",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,aml",
        "tier_optional": "rb,ls"
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
    "mki": {
      "slot_uri": "",
      "range": "MkiEnum",
      "comments": [],
      "annotations": {}
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
    "biospecimen_container_type": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "dna_index": {
      "slot_uri": "",
      "range": "DnaIndexEnum",
      "comments": [
        "(nbl) ConsortiumNote: If multiple statuses apply, include one observation per status."
      ],
      "annotations": {}
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
    "external_subject_id": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "ls"
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
        "INPC >> Differentiating": {
          "meaning": "",
          "comments": []
        },
        "INPC >> Undifferentiated or Poorly Differentiated": {
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
    "ResponseEnum": {
      "permissible_values": {
        "INRC, Brodeur 1993 >> Complete Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Brodeur 1993 >> Mixed Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Brodeur 1993 >> No Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Brodeur 1993 >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Brodeur 1993 >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "INRC, Brodeur 1993 >> Very Good Partial Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Park 2017 >> Minimal Disease": {
          "meaning": "",
          "comments": []
        },
        "INRC, Park 2017 >> Minor Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Park 2017 >> Partial Response": {
          "meaning": "",
          "comments": []
        },
        "INRC, Park 2017 >> Progressive Disease": {
          "meaning": "",
          "comments": []
        },
        "INRC, Park 2017 >> Stable Disease": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "SubgroupTypeEnum": {
      "permissible_values": {
        "Stratum": {
          "meaning": "",
          "comments": []
        },
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
        }
      }
    },
    "MkiEnum": {
      "permissible_values": {
        "High (>4% or >200/5,000 cells)": {
          "meaning": "",
          "comments": []
        },
        "Intermediate (2-4% or 100 to <200/5,000 cells)": {
          "meaning": "",
          "comments": []
        },
        "Low (<2% or <100/5,000 cells)": {
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
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Adrenal Gland": {
          "meaning": "ncit:C12666",
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
        "Central Nervous System": {
          "meaning": "ncit:C12438",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C12745",
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
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Pelvis, NOS": {
          "meaning": "ncit:C12767",
          "comments": []
        },
        "Skin": {
          "meaning": "ncit:C12470",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
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
    "MibgScoreTypeEnum": {
      "permissible_values": {
        "MIBG Curie Score": {
          "meaning": "",
          "comments": []
        },
        "MIBG SIOPEN Score": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "StageEnum": {
      "permissible_values": {
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
    "StudyIdEnum": {
      "permissible_values": {
        "0892": {
          "meaning": "",
          "comments": []
        },
        "0896": {
          "meaning": "",
          "comments": []
        },
        "0901": {
          "meaning": "",
          "comments": []
        },
        "0902": {
          "meaning": "",
          "comments": []
        },
        "0911": {
          "meaning": "",
          "comments": []
        },
        "0914": {
          "meaning": "",
          "comments": []
        },
        "0924": {
          "meaning": "",
          "comments": []
        },
        "0925": {
          "meaning": "",
          "comments": []
        },
        "0926": {
          "meaning": "",
          "comments": []
        },
        "0927": {
          "meaning": "",
          "comments": []
        },
        "0931": {
          "meaning": "",
          "comments": []
        },
        "0935": {
          "meaning": "",
          "comments": []
        },
        "0936": {
          "meaning": "",
          "comments": []
        },
        "0937": {
          "meaning": "",
          "comments": []
        },
        "0961": {
          "meaning": "",
          "comments": []
        },
        "0962": {
          "meaning": "",
          "comments": []
        },
        "09709": {
          "meaning": "",
          "comments": []
        },
        "099": {
          "meaning": "",
          "comments": []
        },
        "321P1": {
          "meaning": "",
          "comments": []
        },
        "321P2": {
          "meaning": "",
          "comments": []
        },
        "321P3": {
          "meaning": "",
          "comments": []
        },
        "321P4": {
          "meaning": "",
          "comments": []
        },
        "323P": {
          "meaning": "",
          "comments": []
        },
        "3881": {
          "meaning": "",
          "comments": []
        },
        "3891": {
          "meaning": "",
          "comments": []
        },
        "3951": {
          "meaning": "",
          "comments": []
        },
        "461": {
          "meaning": "",
          "comments": []
        },
        "4941": {
          "meaning": "",
          "comments": []
        },
        "4941L": {
          "meaning": "",
          "comments": []
        },
        "7942": {
          "meaning": "",
          "comments": []
        },
        "8105": {
          "meaning": "",
          "comments": []
        },
        "8340": {
          "meaning": "",
          "comments": []
        },
        "8441": {
          "meaning": "",
          "comments": []
        },
        "8605": {
          "meaning": "",
          "comments": []
        },
        "8607": {
          "meaning": "",
          "comments": []
        },
        "8661": {
          "meaning": "",
          "comments": []
        },
        "8671": {
          "meaning": "",
          "comments": []
        },
        "8741": {
          "meaning": "",
          "comments": []
        },
        "8742": {
          "meaning": "",
          "comments": []
        },
        "8743": {
          "meaning": "",
          "comments": []
        },
        "8863": {
          "meaning": "",
          "comments": []
        },
        "8970": {
          "meaning": "",
          "comments": []
        },
        "9000": {
          "meaning": "",
          "comments": []
        },
        "9047": {
          "meaning": "",
          "comments": []
        },
        "9072": {
          "meaning": "",
          "comments": []
        },
        "9075": {
          "meaning": "",
          "comments": []
        },
        "9082": {
          "meaning": "",
          "comments": []
        },
        "9140": {
          "meaning": "",
          "comments": []
        },
        "9243": {
          "meaning": "",
          "comments": []
        },
        "9244": {
          "meaning": "",
          "comments": []
        },
        "9248": {
          "meaning": "",
          "comments": []
        },
        "9262": {
          "meaning": "",
          "comments": []
        },
        "9272": {
          "meaning": "",
          "comments": []
        },
        "9275": {
          "meaning": "",
          "comments": []
        },
        "9280": {
          "meaning": "",
          "comments": []
        },
        "9284": {
          "meaning": "",
          "comments": []
        },
        "9285": {
          "meaning": "",
          "comments": []
        },
        "9340": {
          "meaning": "",
          "comments": []
        },
        "9341": {
          "meaning": "",
          "comments": []
        },
        "9342": {
          "meaning": "",
          "comments": []
        },
        "9343": {
          "meaning": "",
          "comments": []
        },
        "9346": {
          "meaning": "",
          "comments": []
        },
        "9347": {
          "meaning": "",
          "comments": []
        },
        "9360": {
          "meaning": "",
          "comments": []
        },
        "9361": {
          "meaning": "",
          "comments": []
        },
        "9372": {
          "meaning": "",
          "comments": []
        },
        "9375": {
          "meaning": "",
          "comments": []
        },
        "9376": {
          "meaning": "",
          "comments": []
        },
        "9382": {
          "meaning": "",
          "comments": []
        },
        "9464": {
          "meaning": "",
          "comments": []
        },
        "9466": {
          "meaning": "",
          "comments": []
        },
        "9470": {
          "meaning": "",
          "comments": []
        },
        "9571": {
          "meaning": "",
          "comments": []
        },
        "9572": {
          "meaning": "",
          "comments": []
        },
        "9579": {
          "meaning": "",
          "comments": []
        },
        "9581": {
          "meaning": "",
          "comments": []
        },
        "9640": {
          "meaning": "",
          "comments": []
        },
        "9670": {
          "meaning": "",
          "comments": []
        },
        "9675": {
          "meaning": "",
          "comments": []
        },
        "9900": {
          "meaning": "",
          "comments": []
        },
        "9907": {
          "meaning": "",
          "comments": []
        },
        "A0935A": {
          "meaning": "",
          "comments": []
        },
        "A09713": {
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
        "AADM01P1": {
          "meaning": "",
          "comments": []
        },
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
        "AAML00P2": {
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
        "AAML05P1": {
          "meaning": "",
          "comments": []
        },
        "AAML07P1": {
          "meaning": "",
          "comments": []
        },
        "AAML1031": {
          "meaning": "ncit:C168938",
          "comments": []
        },
        "AB9804": {
          "meaning": "",
          "comments": []
        },
        "ABTR01B1": {
          "meaning": "",
          "comments": []
        },
        "ABTR04B1": {
          "meaning": "",
          "comments": []
        },
        "ACCL0331": {
          "meaning": "",
          "comments": []
        },
        "ACCL0423": {
          "meaning": "",
          "comments": []
        },
        "ACCL0431": {
          "meaning": "",
          "comments": []
        },
        "ACCL05C1": {
          "meaning": "",
          "comments": []
        },
        "ACCL0934": {
          "meaning": "",
          "comments": []
        },
        "ACCL0935": {
          "meaning": "",
          "comments": []
        },
        "ACCL1031": {
          "meaning": "",
          "comments": []
        },
        "ACCL1032": {
          "meaning": "",
          "comments": []
        },
        "ACCL1034": {
          "meaning": "",
          "comments": []
        },
        "ACCL15N1CD": {
          "meaning": "",
          "comments": []
        },
        "ACCL1633": {
          "meaning": "",
          "comments": []
        },
        "ACCL21C2": {
          "meaning": "",
          "comments": []
        },
        "ACNS02B3": {
          "meaning": "",
          "comments": []
        },
        "ADVL0016": {
          "meaning": "",
          "comments": []
        },
        "ADVL0017": {
          "meaning": "",
          "comments": []
        },
        "ADVL0018": {
          "meaning": "",
          "comments": []
        },
        "ADVL0122": {
          "meaning": "",
          "comments": []
        },
        "ADVL0211": {
          "meaning": "",
          "comments": []
        },
        "ADVL0212": {
          "meaning": "",
          "comments": []
        },
        "ADVL0214": {
          "meaning": "",
          "comments": []
        },
        "ADVL0215": {
          "meaning": "",
          "comments": []
        },
        "ADVL0314": {
          "meaning": "",
          "comments": []
        },
        "ADVL0316": {
          "meaning": "",
          "comments": []
        },
        "ADVL0413": {
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
        "ADVL0421": {
          "meaning": "",
          "comments": []
        },
        "ADVL0516": {
          "meaning": "",
          "comments": []
        },
        "ADVL0517": {
          "meaning": "",
          "comments": []
        },
        "ADVL0524": {
          "meaning": "",
          "comments": []
        },
        "ADVL0525": {
          "meaning": "",
          "comments": []
        },
        "ADVL0612": {
          "meaning": "",
          "comments": []
        },
        "ADVL06B1": {
          "meaning": "",
          "comments": []
        },
        "ADVL0714": {
          "meaning": "",
          "comments": []
        },
        "ADVL0812": {
          "meaning": "",
          "comments": []
        },
        "ADVL0813": {
          "meaning": "",
          "comments": []
        },
        "ADVL0816": {
          "meaning": "",
          "comments": []
        },
        "ADVL0821": {
          "meaning": "",
          "comments": []
        },
        "ADVL0911": {
          "meaning": "",
          "comments": []
        },
        "ADVL0912": {
          "meaning": "",
          "comments": []
        },
        "ADVL0916": {
          "meaning": "",
          "comments": []
        },
        "ADVL0918": {
          "meaning": "",
          "comments": []
        },
        "ADVL0921": {
          "meaning": "",
          "comments": []
        },
        "ADVL1011": {
          "meaning": "",
          "comments": []
        },
        "ADVL1013": {
          "meaning": "",
          "comments": []
        },
        "ADVL1014": {
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
        "ADVL1115": {
          "meaning": "",
          "comments": []
        },
        "ADVL1211": {
          "meaning": "",
          "comments": []
        },
        "ADVL1212": {
          "meaning": "",
          "comments": []
        },
        "ADVL1213": {
          "meaning": "",
          "comments": []
        },
        "ADVL1312": {
          "meaning": "",
          "comments": []
        },
        "ADVL1314": {
          "meaning": "",
          "comments": []
        },
        "ADVL1315": {
          "meaning": "",
          "comments": []
        },
        "ADVL1411": {
          "meaning": "",
          "comments": []
        },
        "ADVL1412": {
          "meaning": "",
          "comments": []
        },
        "ADVL1414": {
          "meaning": "",
          "comments": []
        },
        "ADVL1416": {
          "meaning": "",
          "comments": []
        },
        "ADVL1513": {
          "meaning": "",
          "comments": []
        },
        "ADVL1522": {
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
        "AEPI07N1": {
          "meaning": "",
          "comments": []
        },
        "AEWS07B1": {
          "meaning": "",
          "comments": []
        },
        "AGCT1531": {
          "meaning": "",
          "comments": []
        },
        "AHEP1531": {
          "meaning": "",
          "comments": []
        },
        "ALTE03N1": {
          "meaning": "",
          "comments": []
        },
        "ALTE05N1": {
          "meaning": "",
          "comments": []
        },
        "ALTE15N2": {
          "meaning": "",
          "comments": []
        },
        "ALTE1621": {
          "meaning": "",
          "comments": []
        },
        "ANBL0032": {
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
        "ANBL00P2": {
          "meaning": "",
          "comments": []
        },
        "ANBL00P3": {
          "meaning": "",
          "comments": []
        },
        "ANBL02P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL0321": {
          "meaning": "",
          "comments": []
        },
        "ANBL0322": {
          "meaning": "",
          "comments": []
        },
        "ANBL0421": {
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
        "ANBL0621": {
          "meaning": "",
          "comments": []
        },
        "ANBL0931": {
          "meaning": "",
          "comments": []
        },
        "ANBL09P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL1021": {
          "meaning": "",
          "comments": []
        },
        "ANBL1221": {
          "meaning": "",
          "comments": []
        },
        "ANBL1232": {
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
        "ANBL17P1": {
          "meaning": "",
          "comments": []
        },
        "ANBL1821": {
          "meaning": "",
          "comments": []
        },
        "ANBL19P1": {
          "meaning": "",
          "comments": []
        },
        "ANUR0631": {
          "meaning": "",
          "comments": []
        },
        "ANUR1131": {
          "meaning": "",
          "comments": []
        },
        "AOST06B1": {
          "meaning": "",
          "comments": []
        },
        "APEC14B1": {
          "meaning": "",
          "comments": []
        },
        "APEC1621E": {
          "meaning": "",
          "comments": []
        },
        "APEC1621F": {
          "meaning": "",
          "comments": []
        },
        "APEC1621H": {
          "meaning": "",
          "comments": []
        },
        "APEC1621I": {
          "meaning": "",
          "comments": []
        },
        "APEC1621SC": {
          "meaning": "",
          "comments": []
        },
        "AREN0321": {
          "meaning": "",
          "comments": []
        },
        "AREN03B2": {
          "meaning": "",
          "comments": []
        },
        "AS942": {
          "meaning": "",
          "comments": []
        },
        "AS972": {
          "meaning": "",
          "comments": []
        },
        "AS9801": {
          "meaning": "",
          "comments": []
        },
        "B003": {
          "meaning": "",
          "comments": []
        },
        "B903": {
          "meaning": "",
          "comments": []
        },
        "B904": {
          "meaning": "",
          "comments": []
        },
        "B925": {
          "meaning": "",
          "comments": []
        },
        "B947": {
          "meaning": "",
          "comments": []
        },
        "B953": {
          "meaning": "",
          "comments": []
        },
        "B954": {
          "meaning": "",
          "comments": []
        },
        "B973": {
          "meaning": "",
          "comments": []
        },
        "D9501": {
          "meaning": "",
          "comments": []
        },
        "D9602": {
          "meaning": "",
          "comments": []
        },
        "E04": {
          "meaning": "",
          "comments": []
        },
        "E15": {
          "meaning": "",
          "comments": []
        },
        "E18": {
          "meaning": "",
          "comments": []
        },
        "ENSG5": {
          "meaning": "",
          "comments": []
        },
        "I03": {
          "meaning": "",
          "comments": []
        },
        "LNESG1": {
          "meaning": "",
          "comments": []
        },
        "N891": {
          "meaning": "",
          "comments": []
        },
        "NB2004-HR": {
          "meaning": "",
          "comments": []
        },
        "NB2005": {
          "meaning": "",
          "comments": []
        },
        "NB2008": {
          "meaning": "",
          "comments": []
        },
        "NB2012": {
          "meaning": "",
          "comments": []
        },
        "NB84": {
          "meaning": "",
          "comments": []
        },
        "NB8814": {
          "meaning": "",
          "comments": []
        },
        "NB91": {
          "meaning": "",
          "comments": []
        },
        "NB97": {
          "meaning": "",
          "comments": []
        },
        "P9462": {
          "meaning": "",
          "comments": []
        },
        "P9480": {
          "meaning": "",
          "comments": []
        },
        "P9485": {
          "meaning": "",
          "comments": []
        },
        "P9641": {
          "meaning": "",
          "comments": []
        },
        "P9749": {
          "meaning": "ncit:C177340",
          "comments": []
        },
        "P9761": {
          "meaning": "",
          "comments": []
        },
        "P9772": {
          "meaning": "",
          "comments": []
        },
        "P9851": {
          "meaning": "",
          "comments": []
        },
        "P9963": {
          "meaning": "",
          "comments": []
        },
        "P9972": {
          "meaning": "",
          "comments": []
        },
        "PEPN2011": {
          "meaning": "",
          "comments": []
        },
        "PEPN2111": {
          "meaning": "",
          "comments": []
        },
        "POG-8844": {
          "meaning": "",
          "comments": []
        },
        "R9702": {
          "meaning": "",
          "comments": []
        },
        "S31": {
          "meaning": "",
          "comments": []
        },
        "S901": {
          "meaning": "",
          "comments": []
        },
        "S912": {
          "meaning": "",
          "comments": []
        },
        "S921": {
          "meaning": "",
          "comments": []
        },
        "SIOPEN HR-NBL1": {
          "meaning": "",
          "comments": []
        },
        "SIOPEN-EUNB": {
          "meaning": "",
          "comments": []
        },
        "X0942": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "RevisedInpcEnum": {
      "permissible_values": {
        "Favorable": {
          "meaning": "ncit:C102560",
          "comments": []
        },
        "Unfavorable": {
          "meaning": "ncit:C102561",
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
        "Ganglioneuroblastoma, Intermixed (Schwannian Stroma-Rich)": {
          "meaning": "ncit:C42057",
          "comments": []
        },
        "Ganglioneuroblastoma, Nodular (Composite)": {
          "meaning": "ncit:C42058",
          "comments": []
        },
        "Ganglioneuroma (Schwannian Stroma-Dominant), Maturing Subtype": {
          "meaning": "ncit:C42064",
          "comments": []
        },
        "Neuroblastoma (Schwannian Stroma Poor)": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "InitialTreatmentCategoryEnum": {
      "permissible_values": {
        "Conventional-dose chemotherapy (2-8 cycles) plus surgery": {
          "meaning": "",
          "comments": []
        },
        "Intensive multi-modality therapy: no stem cell or bone marrow transplant": {
          "meaning": "",
          "comments": []
        },
        "Intensive multi-modality therapy: plus stem cell or bone marrow transplant": {
          "meaning": "",
          "comments": []
        },
        "Intensive multi-modality therapy: plus stem cell or bone marrow transplant and anti-GD2 antibody": {
          "meaning": "",
          "comments": []
        },
        "Intensive multi-modality therapy: specific type unknown": {
          "meaning": "",
          "comments": []
        },
        "None (observation)": {
          "meaning": "",
          "comments": []
        },
        "Surgery alone": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
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
    "DiseaseGroupEnum": {
      "permissible_values": {
        "NBL": {
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
    "SubgroupNameEnum": {
      "permissible_values": {
        "Arm A": {
          "meaning": "",
          "comments": []
        },
        "Arm B": {
          "meaning": "",
          "comments": []
        },
        "Arm C": {
          "meaning": "",
          "comments": []
        },
        "Arm D": {
          "meaning": "",
          "comments": []
        },
        "Arm E": {
          "meaning": "",
          "comments": []
        },
        "Assigned to Regimen B": {
          "meaning": "",
          "comments": []
        },
        "Baseline Treatment with 2 cycles": {
          "meaning": "",
          "comments": []
        },
        "Baseline Treatment with 4 cycles": {
          "meaning": "",
          "comments": []
        },
        "Baseline Treatment with 8 cycles": {
          "meaning": "",
          "comments": []
        },
        "No cisRA": {
          "meaning": "",
          "comments": []
        },
        "Non-randomized conventional chemotherapy": {
          "meaning": "",
          "comments": []
        },
        "Non-randomly assigned Single HSCT": {
          "meaning": "",
          "comments": []
        },
        "Not Randomized": {
          "meaning": "",
          "comments": []
        },
        "Purged": {
          "meaning": "",
          "comments": []
        },
        "R0": {
          "meaning": "",
          "comments": []
        },
        "R1": {
          "meaning": "",
          "comments": []
        },
        "R2": {
          "meaning": "",
          "comments": []
        },
        "R3": {
          "meaning": "",
          "comments": []
        },
        "RA only": {
          "meaning": "",
          "comments": []
        },
        "RA+anti-GD2": {
          "meaning": "",
          "comments": []
        },
        "Randomized ablative chemotherapy with BMT": {
          "meaning": "",
          "comments": []
        },
        "Randomized conventional chemotherapy": {
          "meaning": "",
          "comments": []
        },
        "Randomized to Regimen B": {
          "meaning": "",
          "comments": []
        },
        "Randomized to Single HSCT": {
          "meaning": "",
          "comments": []
        },
        "Randomized to Tandem HSCT": {
          "meaning": "",
          "comments": []
        },
        "Regimen A": {
          "meaning": "",
          "comments": []
        },
        "Regimen B": {
          "meaning": "",
          "comments": []
        },
        "Unpurged": {
          "meaning": "",
          "comments": []
        },
        "cisRA": {
          "meaning": "",
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
        "Bone Marrow Response": {
          "meaning": "ncit:C173307",
          "comments": []
        },
        "Metastatic Response": {
          "meaning": "",
          "comments": []
        },
        "Overall Response": {
          "meaning": "ncit:C96613",
          "comments": []
        },
        "Primary Site Response": {
          "meaning": "ncit:C200253",
          "comments": []
        }
      }
    },
    "ConsortiumEnum": {
      "permissible_values": {
        "INRG": {
          "meaning": "ncit:C192762",
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
        "Cerebrospinal Fluid": {
          "meaning": "ncit:C12692",
          "comments": []
        },
        "Lymph Node": {
          "meaning": "ncit:C12745",
          "comments": []
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
    "LaboratoryTestEnum": {
      "permissible_values": {
        "Ferritin": {
          "meaning": "",
          "comments": []
        },
        "LDH": {
          "meaning": "ncit:C64855",
          "comments": []
        }
      }
    },
    "DnaIndexEnum": {
      "permissible_values": {
        "DNA Index </= 1 (Hypodiploid, Diploid)": {
          "meaning": "",
          "comments": []
        },
        "DNA Index >1 (Hyperdiploid)": {
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
    }
  }
}
```

</div>