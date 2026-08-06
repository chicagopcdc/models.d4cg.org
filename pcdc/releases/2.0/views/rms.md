---
layout: default
title: Rhabdomyosarcoma
nav_exclude: true
search_exclude: true
---


# Data Model `pcdc-2.0`

*RMS View*

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
- [Retinoblastoma](rb)
- **Rhabdomyosarcoma**

</details>

The RMS view of the PCDC data model represents consensus data modeling by an international group of pediatric rhabdomyosarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors.


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

## SurvivalCharacteristics

| Slot | Range | Description |
|---|---|---|
| `age_at_lkss` | `integer` |  |
| `lkss` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-lkssenum')">LkssEnum</button> |  |
| `cause_of_death` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-causeofdeathenum')">CauseOfDeathEnum</button> |  |
| `cause_of_death_other` | `string` |  |

<div class="domain-heading">Disease_Attributes</div>

## Diagnosis

| Slot | Range | Description |
|---|---|---|
| `age_at_diag_assessment` | `integer` |  |
| `diagnosis_basis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisbasisenum')">DiagnosisBasisEnum</button> |  |
| `diagnosis` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-diagnosisenum')">DiagnosisEnum</button> |  |

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
| `invasiveness` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-invasivenessenum')">InvasivenessEnum</button> |  |
| `nodal_pathology` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nodalpathologyenum')">NodalPathologyEnum</button> |  |
| `nodal_clinical` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-nodalclinicalenum')">NodalClinicalEnum</button> |  |
| `parameningeal_extension` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |

## Staging

| Slot | Range | Description |
|---|---|---|
| `age_at_staging` | `integer` |  |
| `tnm_finding` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-tnmfindingenum')">TnmFindingEnum</button> |  |
| `group` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-groupenum')">GroupEnum</button> |  |

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

## SurgicalProcedures

| Slot | Range | Description |
|---|---|---|
| `age_at_procedure` | `integer` |  |
| `procedure_performed` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `site_classification` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-siteclassificationenum')">SiteClassificationEnum</button> |  |
| `procedure_site` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-proceduresiteenum')">ProcedureSiteEnum</button> |  |
| `site_other` | `string` |  |
| `mass_present` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `viable_tumor_specimen` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `viable_tumor_margin` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button> |  |
| `margins` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-marginsenum')">MarginsEnum</button> |  |

<div class="domain-heading">Monitoring</div>

## SubjectResponse

| Slot | Range | Description |
|---|---|---|
| `age_at_response` | `integer` |  |
| `tx_prior_response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-txpriorresponseenum')">TxPriorResponseEnum</button> |  |
| `response_method` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responsemethodenum')">ResponseMethodEnum</button> |  |
| `response` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-responseenum')">ResponseEnum</button> |  |
| `anaplasia` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `anaplasia_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-anaplasiatypeenum')">AnaplasiaTypeEnum</button> |  |
| `anaplasia_pct_numeric` | `decimal` |  |

## SubsequentMalignantNeoplasm

| Slot | Range | Description |
|---|---|---|
| `age_at_smn` | `integer` |  |

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
| `gene_panel_size` | `GenePanelSizeEnum` |  |
| `alteration_presence` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-presentabsentenum')">PresentAbsentEnum</button> |  |
| `alteration` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationenum')">AlterationEnum</button> |  |
| `alteration_type` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button> |  |
| `alteration_effect` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button> |  |
| `chromosome` | <button type="button" class="enum-button" onclick="openEnumModal('enum-modal-chromosomeenum')">ChromosomeEnum</button> |  |
| `gene` | `string` |  |
| `gene_fusion_partner` | `string` |  |

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
<tr><td><code>Other-FOXO1 Gene Fusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PAX3-FOXO1 Gene Fusion</code></td><td><code>ncit:C99712</code></td><td></td></tr>
<tr><td><code>PAX3-Other Gene Fusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>PAX7-FOXO1 Gene Fusion</code></td><td><code>ncit:C99363</code></td><td></td></tr>
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

<div id="enum-modal-anaplasiatypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-anaplasiatypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-anaplasiatypeenum')">×</button>
<h3><code>AnaplasiaTypeEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Diffuse</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Focal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td>(cns) ConsortiumNote: Deceased-due to unknown causes.<br>(fa) ConsortiumNote: Deceased-due to unknown causes.</td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td>(cns) ConsortiumNote: Deceased-causes unavailable.<br>(fa) ConsortiumNote: Deceased-causes unavailable.</td></tr>
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
<tr><td><code>Alveolar rhabdomyosarcoma (ARMS)</code></td><td><code></code></td><td>(rms) ConsortiumNote: If multiple histological findings, include one observation per histological finding.</td></tr>
<tr><td><code>Botryoid rhabdomyosarcoma (BRMS)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Embryonal rhabdomyosarcoma (ERMS)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleomorphic rhabdomyosarcoma (PRMS)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma (RMS), inadequate tissue for classification</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma (RMS), not classifiable</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Rhabdomyosarcoma (RMS), with Mixed Embryonal and Alveolar Features</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Spindle cell</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>RMS</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Bladder</code></td><td><code>ncit:C12414</code></td><td></td></tr>
<tr><td><code>Bladder/Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Cheek</code></td><td><code>ncit:C13070</code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C12745</code></td><td></td></tr>
<tr><td><code>Eyelid</code></td><td><code>ncit:C12713</code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Forearm</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Knee</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Liver/Biliary Tract</code></td><td><code>ncit:C12678</code></td><td></td></tr>
<tr><td><code>Lower Leg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Middle Ear</code></td><td><code>ncit:C12274</code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code>ncit:C12421</code></td><td></td></tr>
<tr><td><code>Orbit</code></td><td><code>ncit:C12347</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Paranasal Sinuses</code></td><td><code>ncit:C12763</code></td><td></td></tr>
<tr><td><code>Parapharyngeal Area</code></td><td><code>ncit:C162818</code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code>ncit:C129461</code></td><td></td></tr>
<tr><td><code>Paratesticular</code></td><td><code>ncit:C162491</code></td><td></td></tr>
<tr><td><code>Parathyroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parotid</code></td><td><code>ncit:C12427</code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code>ncit:C33301</code></td><td></td></tr>
<tr><td><code>Pleural Effusion</code></td><td><code>ncit:C3331</code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code>ncit:C12783</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code>ncit:C12471</code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Thyroid</code></td><td><code>ncit:C12400</code></td><td></td></tr>
<tr><td><code>Trunk</code></td><td><code>ncit:C33816</code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code>ncit:C32141</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code>ncit:C12405</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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

<div id="enum-modal-groupenum" class="enum-modal" onclick="closeEnumModal('enum-modal-groupenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-groupenum')">×</button>
<h3><code>GroupEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>IRS &gt;&gt; Group I</code></td><td><code></code></td><td>(rms) ConsortiumNote: Tied to AGE_AT_STAGING.</td></tr>
<tr><td><code>IRS &gt;&gt; Group II NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Group IIA</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Group IIB</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Group IIC</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Group III</code></td><td><code></code></td><td></td></tr>
<tr><td><code>IRS &gt;&gt; Group IV</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code>ncit:C17998</code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-invasivenessenum" class="enum-modal" onclick="closeEnumModal('enum-modal-invasivenessenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-invasivenessenum')">×</button>
<h3><code>InvasivenessEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>T1 Staging Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>T2 Staging Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>TX Staging Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Gross Total Resection, Unknown Margins</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Incomplete Resection</code></td><td><code>ncit:C182305</code></td><td></td></tr>
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

<div id="enum-modal-nodalclinicalenum" class="enum-modal" onclick="closeEnumModal('enum-modal-nodalclinicalenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-nodalclinicalenum')">×</button>
<h3><code>NodalClinicalEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>N0 Stage Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>N1 Stage FInding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NX Stage Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-nodalpathologyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-nodalpathologyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-nodalpathologyenum')">×</button>
<h3><code>NodalPathologyEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>N0 Stage Finding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>N1 Stage FInding</code></td><td><code></code></td><td></td></tr>
<tr><td><code>NX Stage Finding</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Present</code></td><td><code>ncit:C25566</code></td><td></td></tr>
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
<tr><td><code>Abdomen</code></td><td><code>ncit:C12664</code></td><td></td></tr>
<tr><td><code>Anal/Perianal</code></td><td><code>ncit:C99148</code></td><td></td></tr>
<tr><td><code>Bladder</code></td><td><code>ncit:C12414</code></td><td></td></tr>
<tr><td><code>Bladder/Prostate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code>ncit:C12431</code></td><td></td></tr>
<tr><td><code>Bone or Bone Marrow</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code>ncit:C12366</code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code>ncit:C12311</code></td><td></td></tr>
<tr><td><code>Cheek</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code>ncit:C160424</code></td><td></td></tr>
<tr><td><code>Eyelid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Forearm</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code>ncit:C12246</code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine and Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Knee</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code>ncit:C12420</code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C32974</code></td><td></td></tr>
<tr><td><code>Liver/Biliary Tract</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Leg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Middle Ear</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code>ncit:C12424</code></td><td></td></tr>
<tr><td><code>Nasal Cavity and Paranasal Sinuses</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code>ncit:C12423</code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code>ncit:C12421</code></td><td></td></tr>
<tr><td><code>Orbit</code></td><td><code>ncit:C12347</code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code>ncit:C12762</code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Paranasal Sinuses</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paratesticular</code></td><td><code>ncit:C162491</code></td><td></td></tr>
<tr><td><code>Parotid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleural Effusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code>ncit:C12410</code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C12298</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code>ncit:C89807</code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code>ncit:C25203</code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code>ncit:C33763</code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Thyroid and Parathyroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trunk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code>ncit:C32141</code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code>ncit:C12405</code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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

<div id="enum-modal-responsemethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-responsemethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-responsemethodenum')">×</button>
<h3><code>ResponseMethodEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Imaging</code></td><td><code>ncit:C17220</code></td><td></td></tr>
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
<tr><td><code>Anal/Perianal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bladder/Prostate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone Marrow</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone or Bone Marrow</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Bone, NOS</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Brain</code></td><td><code>ncit:C12439</code></td><td></td></tr>
<tr><td><code>Cervix</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Cheek</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Distant Lymph Nodes</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Eyelid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Foot</code></td><td><code>ncit:C32622</code></td><td></td></tr>
<tr><td><code>Forearm</code></td><td><code>ncit:C32628</code></td><td></td></tr>
<tr><td><code>Hand</code></td><td><code>ncit:C32712</code></td><td></td></tr>
<tr><td><code>Hypopharynx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Infratemporal Fossa/Pterygopalatine and Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Kidney</code></td><td><code>ncit:C12415</code></td><td></td></tr>
<tr><td><code>Knee</code></td><td><code>ncit:C32898</code></td><td></td></tr>
<tr><td><code>Larynx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Leg</code></td><td><code>ncit:C12392</code></td><td></td></tr>
<tr><td><code>Liver/Biliary Tract</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lower Leg</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Lung</code></td><td><code>ncit:C12468</code></td><td></td></tr>
<tr><td><code>Middle Ear</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal Cavity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasal Cavity and Paranasal Sinuses</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Nasopharynx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Neck</code></td><td><code>ncit:C13063</code></td><td></td></tr>
<tr><td><code>Oral Cavity</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Orbit</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Oropharynx</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Ovary</code></td><td><code>ncit:C12404</code></td><td></td></tr>
<tr><td><code>Paranasal Sinuses</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Parapharyngeal Area</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paraspinal</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Paratesticular</code></td><td><code>ncit:C162491</code></td><td></td></tr>
<tr><td><code>Parotid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pelvis, NOS</code></td><td><code>ncit:C12767</code></td><td></td></tr>
<tr><td><code>Perineum</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Pleural Effusion</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Prostate</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Retroperitoneum</code></td><td><code>ncit:C28256</code></td><td></td></tr>
<tr><td><code>Scalp</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Shoulder</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Soft Tissue</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thigh</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Thorax</code></td><td><code>ncit:C12799</code></td><td></td></tr>
<tr><td><code>Thyroid and Parathyroid</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Trunk</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Upper Arm</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Uterus</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Vagina</code></td><td><code>ncit:C12407</code></td><td></td></tr>
<tr><td><code>Vulva</code></td><td><code>ncit:C12408</code></td><td></td></tr>
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
<tr><td><code>Regional Nodes</code></td><td><code></code></td><td>(npc) ConsortiumNote: Includes 'PTV2' and 'PTV3'</td></tr>
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
<tr><td><code>ARST0331</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0431</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST08P1</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS-IV-2002</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS2002P</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS91</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9602</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9802</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9803</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ICG RMS96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MMT95</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MTS2008</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RMS 4.99</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RMS2005</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>ARST0331:Regimen I</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0331:Regimen II</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0431:High Risk Rhabdomyosarcoma</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531:Arm I (Chemotherapy, Radiotherapy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST0531:Arm II (Chemotherapy, Radiotherapy)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ARST08P1:Group 1 (Chemotherapy, Radiation Therapy, Cixutumumab)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS-IV-2002</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS2002P:HR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS2002P:LR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS2002P:SR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS2002P:VHR</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS91</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS96:High Dose Therapy (HDT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>CWS96:Oral Maintenance Therapy (OMT)</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9602:Subgroup A</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9602:Subgroup B</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9802</code></td><td><code></code></td><td></td></tr>
<tr><td><code>D9803</code></td><td><code></code></td><td></td></tr>
<tr><td><code>ICG RMS96</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MMT95</code></td><td><code></code></td><td></td></tr>
<tr><td><code>MTS2008</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RMS 4.99</code></td><td><code></code></td><td></td></tr>
<tr><td><code>RMS2005</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Brachytherapy</code></td><td><code>ncit:C15195</code></td><td></td></tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="enum-modal-tnmfindingenum" class="enum-modal" onclick="closeEnumModal('enum-modal-tnmfindingenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-tnmfindingenum')">×</button>
<h3><code>TnmFindingEnum</code></h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Permissible Value</th><th>Meaning</th><th>Comments</th></tr></thead>
<tbody>
<tr><td><code>Favorable Site, M0</code></td><td><code></code></td><td>(rms) ConsortiumNote: Tied to AGE_AT_STAGING.</td></tr>
<tr><td><code>Metastases, ML</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other site, any T, a, N0, M0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Other site, any T, a, N1, M0, any T, b, N0/N1, M0</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Unknown</code></td><td><code></code></td><td></td></tr>
<tr><td><code>Not Reported</code></td><td><code></code></td><td></td></tr>
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
<tr><td><code>Not Reported</code></td><td><code>ncit:C43234</code></td><td></td></tr>
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
    "rms": {
      "name": "rms",
      "title": "Rhabdomyosarcoma",
      "description": "The RMS view of the PCDC data model represents consensus data modeling by an international group of pediatric rhabdomyosarcoma experts and is maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the International Soft Tissue Sarcoma Consortium (INSTRuCT). It is based on the collective requirements of its contributors."
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
        "cause_of_death",
        "cause_of_death_other"
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
    "GeneticAnalysis": {
      "slots": [
        "age_at_genetic_analysis",
        "gene_panel_size",
        "alteration_presence",
        "alteration",
        "alteration_type",
        "alteration_effect",
        "chromosome",
        "gene",
        "gene_fusion_partner"
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
        "tnm_finding",
        "group"
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
        "site_classification",
        "disease_site",
        "site_other",
        "measurement1",
        "measurement2",
        "measurement3",
        "measurement_unit",
        "tumor_size",
        "invasiveness",
        "nodal_pathology",
        "nodal_clinical",
        "parameningeal_extension"
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
        "procedure_performed",
        "site_classification",
        "procedure_site",
        "site_other",
        "mass_present",
        "viable_tumor_specimen",
        "viable_tumor_margin",
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
        "rt_dose_unit"
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
        "response_method",
        "response",
        "anaplasia",
        "anaplasia_type",
        "anaplasia_pct_numeric"
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
        "age_at_smn"
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
    "mass_present": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rms"
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
    "age_at_smn": {
      "slot_uri": "ncit:C168860",
      "range": "integer",
      "comments": [],
      "annotations": {
        "tier_priority": "all_groups"
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
    "anaplasia": {
      "slot_uri": "",
      "range": "PresentAbsentEnum",
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
    "gene_panel_size": {
      "slot_uri": "",
      "range": "GenePanelSizeEnum",
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
    "procedure_performed": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {}
    },
    "anaplasia_pct_numeric": {
      "slot_uri": "",
      "range": "decimal",
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
    "tx_prior_response": {
      "slot_uri": "",
      "range": "TxPriorResponseEnum",
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
    "nodal_pathology": {
      "slot_uri": "",
      "range": "NodalPathologyEnum",
      "comments": [],
      "annotations": {}
    },
    "invasiveness": {
      "slot_uri": "",
      "range": "InvasivenessEnum",
      "comments": [],
      "annotations": {}
    },
    "cause_of_death_other": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_priority": "rb"
      }
    },
    "nodal_clinical": {
      "slot_uri": "",
      "range": "NodalClinicalEnum",
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
    "response_method": {
      "slot_uri": "ncit:C178148",
      "range": "ResponseMethodEnum",
      "comments": [],
      "annotations": {
        "tier_mandatory": "hl",
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
    "viable_tumor_specimen": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rms"
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
    "biospecimen_media": {
      "slot_uri": "",
      "range": "string",
      "comments": [],
      "annotations": {
        "tier_optional": "rms_v2.0-approved"
      }
    },
    "tnm_finding": {
      "slot_uri": "",
      "range": "TnmFindingEnum",
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
    "procedure_site": {
      "slot_uri": "ncit:C157120",
      "range": "ProcedureSiteEnum",
      "comments": [],
      "annotations": {
        "tier_priority": "fa,lt",
        "tier_optional": "ls"
      }
    },
    "anaplasia_type": {
      "slot_uri": "",
      "range": "AnaplasiaTypeEnum",
      "comments": [],
      "annotations": {}
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
    "group": {
      "slot_uri": "",
      "range": "GroupEnum",
      "comments": [],
      "annotations": {
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
    "parameningeal_extension": {
      "slot_uri": "",
      "range": "YesNoEnum",
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
    "viable_tumor_margin": {
      "slot_uri": "",
      "range": "YesNoEnum",
      "comments": [],
      "annotations": {
        "tier_optional": "rms"
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
    "DiseaseSiteEnum": {
      "permissible_values": {
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Anal/Perianal": {
          "meaning": "ncit:C99148",
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
        "Cervix": {
          "meaning": "ncit:C12311",
          "comments": []
        },
        "Cheek": {
          "meaning": "ncit:C13070",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C12745",
          "comments": []
        },
        "Eyelid": {
          "meaning": "ncit:C12713",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Forearm": {
          "meaning": "ncit:C32628",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "ncit:C12246",
          "comments": []
        },
        "Infratemporal Fossa/Pterygopalatine": {
          "meaning": "",
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
        "Larynx": {
          "meaning": "ncit:C12420",
          "comments": []
        },
        "Leg": {
          "meaning": "ncit:C32974",
          "comments": []
        },
        "Liver/Biliary Tract": {
          "meaning": "ncit:C12678",
          "comments": []
        },
        "Lower Leg": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Middle Ear": {
          "meaning": "ncit:C12274",
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
        "Neck": {
          "meaning": "ncit:C13063",
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
        "Ovary": {
          "meaning": "ncit:C12404",
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
        "Parotid": {
          "meaning": "ncit:C12427",
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
        "Pleural Effusion": {
          "meaning": "ncit:C3331",
          "comments": []
        },
        "Prostate": {
          "meaning": "ncit:C12410",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
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
        "Soft Tissue": {
          "meaning": "ncit:C12471",
          "comments": []
        },
        "Thigh": {
          "meaning": "ncit:C33763",
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
        "Trunk": {
          "meaning": "ncit:C33816",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "ncit:C32141",
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
    "TnmFindingEnum": {
      "permissible_values": {
        "Favorable Site, M0": {
          "meaning": "",
          "comments": [
            "(rms) ConsortiumNote: Tied to AGE_AT_STAGING."
          ]
        },
        "Metastases, ML": {
          "meaning": "",
          "comments": []
        },
        "Other site, any T, a, N0, M0": {
          "meaning": "",
          "comments": []
        },
        "Other site, any T, a, N1, M0, any T, b, N0/N1, M0": {
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
    "ResponseMethodEnum": {
      "permissible_values": {
        "Imaging": {
          "meaning": "ncit:C17220",
          "comments": []
        }
      }
    },
    "AlterationEnum": {
      "permissible_values": {
        "Other-FOXO1 Gene Fusion": {
          "meaning": "",
          "comments": []
        },
        "PAX3-FOXO1 Gene Fusion": {
          "meaning": "ncit:C99712",
          "comments": []
        },
        "PAX3-Other Gene Fusion": {
          "meaning": "",
          "comments": []
        },
        "PAX7-FOXO1 Gene Fusion": {
          "meaning": "ncit:C99363",
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
        "Anal/Perianal": {
          "meaning": "",
          "comments": []
        },
        "Bladder": {
          "meaning": "",
          "comments": []
        },
        "Bladder/Prostate": {
          "meaning": "",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "",
          "comments": []
        },
        "Bone or Bone Marrow": {
          "meaning": "",
          "comments": []
        },
        "Bone, NOS": {
          "meaning": "",
          "comments": []
        },
        "Brain": {
          "meaning": "ncit:C12439",
          "comments": []
        },
        "Cervix": {
          "meaning": "",
          "comments": []
        },
        "Cheek": {
          "meaning": "",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "",
          "comments": []
        },
        "Eyelid": {
          "meaning": "",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Forearm": {
          "meaning": "ncit:C32628",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "",
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
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Knee": {
          "meaning": "ncit:C32898",
          "comments": []
        },
        "Larynx": {
          "meaning": "",
          "comments": []
        },
        "Leg": {
          "meaning": "ncit:C12392",
          "comments": []
        },
        "Liver/Biliary Tract": {
          "meaning": "",
          "comments": []
        },
        "Lower Leg": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Middle Ear": {
          "meaning": "",
          "comments": []
        },
        "Nasal Cavity": {
          "meaning": "",
          "comments": []
        },
        "Nasal Cavity and Paranasal Sinuses": {
          "meaning": "",
          "comments": []
        },
        "Nasopharynx": {
          "meaning": "",
          "comments": []
        },
        "Neck": {
          "meaning": "ncit:C13063",
          "comments": []
        },
        "Oral Cavity": {
          "meaning": "",
          "comments": []
        },
        "Orbit": {
          "meaning": "",
          "comments": []
        },
        "Oropharynx": {
          "meaning": "",
          "comments": []
        },
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Paranasal Sinuses": {
          "meaning": "",
          "comments": []
        },
        "Parapharyngeal Area": {
          "meaning": "",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "",
          "comments": []
        },
        "Paratesticular": {
          "meaning": "ncit:C162491",
          "comments": []
        },
        "Parotid": {
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
        "Pleural Effusion": {
          "meaning": "",
          "comments": []
        },
        "Prostate": {
          "meaning": "",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C28256",
          "comments": []
        },
        "Scalp": {
          "meaning": "",
          "comments": []
        },
        "Shoulder": {
          "meaning": "",
          "comments": []
        },
        "Soft Tissue": {
          "meaning": "",
          "comments": []
        },
        "Thigh": {
          "meaning": "",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
          "comments": []
        },
        "Thyroid and Parathyroid": {
          "meaning": "",
          "comments": []
        },
        "Trunk": {
          "meaning": "",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "",
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
        "Vulva": {
          "meaning": "ncit:C12408",
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
    "NodalClinicalEnum": {
      "permissible_values": {
        "N0 Stage Finding": {
          "meaning": "",
          "comments": []
        },
        "N1 Stage FInding": {
          "meaning": "",
          "comments": []
        },
        "NX Stage Finding": {
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
        "ARST0331": {
          "meaning": "",
          "comments": []
        },
        "ARST0431": {
          "meaning": "",
          "comments": []
        },
        "ARST0531": {
          "meaning": "",
          "comments": []
        },
        "ARST08P1": {
          "meaning": "",
          "comments": []
        },
        "CWS-IV-2002": {
          "meaning": "",
          "comments": []
        },
        "CWS2002P": {
          "meaning": "",
          "comments": []
        },
        "CWS91": {
          "meaning": "",
          "comments": []
        },
        "CWS96": {
          "meaning": "",
          "comments": []
        },
        "D9602": {
          "meaning": "",
          "comments": []
        },
        "D9802": {
          "meaning": "",
          "comments": []
        },
        "D9803": {
          "meaning": "",
          "comments": []
        },
        "ICG RMS96": {
          "meaning": "",
          "comments": []
        },
        "MMT95": {
          "meaning": "",
          "comments": []
        },
        "MTS2008": {
          "meaning": "",
          "comments": []
        },
        "RMS 4.99": {
          "meaning": "",
          "comments": []
        },
        "RMS2005": {
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
    "DiagnosisEnum": {
      "permissible_values": {
        "Alveolar rhabdomyosarcoma (ARMS)": {
          "meaning": "",
          "comments": [
            "(rms) ConsortiumNote: If multiple histological findings, include one observation per histological finding."
          ]
        },
        "Botryoid rhabdomyosarcoma (BRMS)": {
          "meaning": "",
          "comments": []
        },
        "Embryonal rhabdomyosarcoma (ERMS)": {
          "meaning": "",
          "comments": []
        },
        "Pleomorphic rhabdomyosarcoma (PRMS)": {
          "meaning": "",
          "comments": []
        },
        "Rhabdomyosarcoma (RMS), inadequate tissue for classification": {
          "meaning": "",
          "comments": []
        },
        "Rhabdomyosarcoma (RMS), not classifiable": {
          "meaning": "",
          "comments": []
        },
        "Rhabdomyosarcoma (RMS), with Mixed Embryonal and Alveolar Features": {
          "meaning": "",
          "comments": []
        },
        "Spindle cell": {
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
        "Abdomen": {
          "meaning": "ncit:C12664",
          "comments": []
        },
        "Anal/Perianal": {
          "meaning": "ncit:C99148",
          "comments": []
        },
        "Bladder": {
          "meaning": "ncit:C12414",
          "comments": []
        },
        "Bladder/Prostate": {
          "meaning": "",
          "comments": []
        },
        "Bone Marrow": {
          "meaning": "ncit:C12431",
          "comments": []
        },
        "Bone or Bone Marrow": {
          "meaning": "",
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
        "Cervix": {
          "meaning": "ncit:C12311",
          "comments": []
        },
        "Cheek": {
          "meaning": "",
          "comments": []
        },
        "Distant Lymph Nodes": {
          "meaning": "ncit:C160424",
          "comments": []
        },
        "Eyelid": {
          "meaning": "",
          "comments": []
        },
        "Foot": {
          "meaning": "ncit:C32622",
          "comments": []
        },
        "Forearm": {
          "meaning": "ncit:C32628",
          "comments": []
        },
        "Hand": {
          "meaning": "ncit:C32712",
          "comments": []
        },
        "Hypopharynx": {
          "meaning": "ncit:C12246",
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
        "Kidney": {
          "meaning": "ncit:C12415",
          "comments": []
        },
        "Knee": {
          "meaning": "ncit:C32898",
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
        "Liver/Biliary Tract": {
          "meaning": "",
          "comments": []
        },
        "Lower Leg": {
          "meaning": "",
          "comments": []
        },
        "Lung": {
          "meaning": "ncit:C12468",
          "comments": []
        },
        "Middle Ear": {
          "meaning": "",
          "comments": []
        },
        "Nasal Cavity": {
          "meaning": "ncit:C12424",
          "comments": []
        },
        "Nasal Cavity and Paranasal Sinuses": {
          "meaning": "",
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
        "Ovary": {
          "meaning": "ncit:C12404",
          "comments": []
        },
        "Paranasal Sinuses": {
          "meaning": "",
          "comments": []
        },
        "Parapharyngeal Area": {
          "meaning": "",
          "comments": []
        },
        "Paraspinal": {
          "meaning": "",
          "comments": []
        },
        "Paratesticular": {
          "meaning": "ncit:C162491",
          "comments": []
        },
        "Parotid": {
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
        "Pleural Effusion": {
          "meaning": "",
          "comments": []
        },
        "Prostate": {
          "meaning": "ncit:C12410",
          "comments": []
        },
        "Retroperitoneum": {
          "meaning": "ncit:C12298",
          "comments": []
        },
        "Scalp": {
          "meaning": "ncit:C89807",
          "comments": []
        },
        "Shoulder": {
          "meaning": "ncit:C25203",
          "comments": []
        },
        "Soft Tissue": {
          "meaning": "",
          "comments": []
        },
        "Thigh": {
          "meaning": "ncit:C33763",
          "comments": []
        },
        "Thorax": {
          "meaning": "ncit:C12799",
          "comments": []
        },
        "Thyroid and Parathyroid": {
          "meaning": "",
          "comments": []
        },
        "Trunk": {
          "meaning": "",
          "comments": []
        },
        "Upper Arm": {
          "meaning": "ncit:C32141",
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
    "AnaplasiaTypeEnum": {
      "permissible_values": {
        "Diffuse": {
          "meaning": "",
          "comments": []
        },
        "Focal": {
          "meaning": "",
          "comments": []
        },
        "Unknown": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "DiseaseGroupEnum": {
      "permissible_values": {
        "RMS": {
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
        "ARST0331:Regimen I": {
          "meaning": "",
          "comments": []
        },
        "ARST0331:Regimen II": {
          "meaning": "",
          "comments": []
        },
        "ARST0431:High Risk Rhabdomyosarcoma": {
          "meaning": "",
          "comments": []
        },
        "ARST0531:Arm I (Chemotherapy, Radiotherapy)": {
          "meaning": "",
          "comments": []
        },
        "ARST0531:Arm II (Chemotherapy, Radiotherapy)": {
          "meaning": "",
          "comments": []
        },
        "ARST08P1:Group 1 (Chemotherapy, Radiation Therapy, Cixutumumab)": {
          "meaning": "",
          "comments": []
        },
        "CWS-IV-2002": {
          "meaning": "",
          "comments": []
        },
        "CWS2002P:HR": {
          "meaning": "",
          "comments": []
        },
        "CWS2002P:LR": {
          "meaning": "",
          "comments": []
        },
        "CWS2002P:SR": {
          "meaning": "",
          "comments": []
        },
        "CWS2002P:VHR": {
          "meaning": "",
          "comments": []
        },
        "CWS91": {
          "meaning": "",
          "comments": []
        },
        "CWS96:High Dose Therapy (HDT)": {
          "meaning": "",
          "comments": []
        },
        "CWS96:Oral Maintenance Therapy (OMT)": {
          "meaning": "",
          "comments": []
        },
        "D9602:Subgroup A": {
          "meaning": "",
          "comments": []
        },
        "D9602:Subgroup B": {
          "meaning": "",
          "comments": []
        },
        "D9802": {
          "meaning": "",
          "comments": []
        },
        "D9803": {
          "meaning": "",
          "comments": []
        },
        "ICG RMS96": {
          "meaning": "",
          "comments": []
        },
        "MMT95": {
          "meaning": "",
          "comments": []
        },
        "MTS2008": {
          "meaning": "",
          "comments": []
        },
        "RMS 4.99": {
          "meaning": "",
          "comments": []
        },
        "RMS2005": {
          "meaning": "",
          "comments": []
        }
      }
    },
    "MarginsEnum": {
      "permissible_values": {
        "Gross Total Resection, Unknown Margins": {
          "meaning": "",
          "comments": []
        },
        "Incomplete Resection": {
          "meaning": "ncit:C182305",
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
    "InvasivenessEnum": {
      "permissible_values": {
        "T1 Staging Finding": {
          "meaning": "",
          "comments": []
        },
        "T2 Staging Finding": {
          "meaning": "",
          "comments": []
        },
        "TX Staging Finding": {
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
    "GroupEnum": {
      "permissible_values": {
        "IRS >> Group I": {
          "meaning": "",
          "comments": [
            "(rms) ConsortiumNote: Tied to AGE_AT_STAGING."
          ]
        },
        "IRS >> Group II NOS": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Group IIA": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Group IIB": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Group IIC": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Group III": {
          "meaning": "",
          "comments": []
        },
        "IRS >> Group IV": {
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
    "NodalPathologyEnum": {
      "permissible_values": {
        "N0 Stage Finding": {
          "meaning": "",
          "comments": []
        },
        "N1 Stage FInding": {
          "meaning": "",
          "comments": []
        },
        "NX Stage Finding": {
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