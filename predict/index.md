---
layout: default
title: Monogenic Diabetes
nav_order: 3
has_children: true
---


<div class="model-header" markdown="1">

# PREDICT Data Model `1.0`

<div class="model-meta-grid">
<div><span>Schema ID</span><span class="model-meta-value"><code>https://models.d4cg.org/predict</code></span></div>
<div><span>License</span><span class="model-meta-value">CC BY-NC 4.0</span></div>
<div><span>Concepts</span><span class="model-meta-value">11 classes · 81 slots · 47 enums</span></div>
<div><span>Community</span><span class="model-meta-value"><button type="button" class="model-meta-link" onclick="openEnumModal('enum-modal-datacontributoridenum')">12 contributors</button></span></div>
</div>

<div class="view-selector">
<label for="view-selector" class="text-delta">View</label>
<select id="view-selector" onchange="switchView(this.value)">
<option value="base" selected>base</option>
</select>
</div>

<div id="view-description" class="view-description"></div>

<details class="scope-matrix-details">
<summary class="text-delta">Scope Matrix</summary>

<div id="view-matrix-wrap" class="view-matrix-wrap">
<div class="view-matrix-title">Class Inclusion by View</div>
<div class="view-matrix-scroll">
<table class="view-matrix">
<thead>
<tr>
<th>Domain</th>
<th>Class</th>
</tr>
</thead>
<tbody>
<tr class="view-matrix-row" data-class-ref="class-demographics"><td title="Demographics">Demographics</td><td title="Demographics"><a href="#class-demographics">Demographics</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-familymedicalhistory"><td title="Demographics">Demographics</td><td title="FamilyMedicalHistory"><a href="#class-familymedicalhistory">FamilyMedicalHistory</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-medicalhistory"><td title="Demographics">Demographics</td><td title="MedicalHistory"><a href="#class-medicalhistory">MedicalHistory</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-subjectcharacteristics"><td title="Demographics">Demographics</td><td title="SubjectCharacteristics"><a href="#class-subjectcharacteristics">SubjectCharacteristics</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-timing"><td title="Demographics">Demographics</td><td title="Timing"><a href="#class-timing">Timing</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-diseasecharacteristics"><td title="Disease Attributes">Disease Attributes</td><td title="DiseaseCharacteristics"><a href="#class-diseasecharacteristics">DiseaseCharacteristics</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-treatment"><td title="Intervention">Intervention</td><td title="Treatment"><a href="#class-treatment">Treatment</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-biometrics"><td title="Testing">Testing</td><td title="Biometrics"><a href="#class-biometrics">Biometrics</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-biospecimen"><td title="Testing">Testing</td><td title="Biospecimen"><a href="#class-biospecimen">Biospecimen</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-geneticanalysis"><td title="Testing">Testing</td><td title="GeneticAnalysis"><a href="#class-geneticanalysis">GeneticAnalysis</a></td>
</tr>
<tr class="view-matrix-row" data-class-ref="class-testing"><td title="Testing">Testing</td><td title="Testing"><a href="#class-testing">Testing</a></td>
</tr>
</tbody>
</table>
</div>
</div>

</details>


<div class="view-mode-toggle">
  <span class="toggle-label">Rendered</span>
  <label class="switch">
    <input id="view-mode-checkbox" type="checkbox" onchange="switchModelMode(this.checked)">
    <span class="slider"></span>
  </label>
  <span class="toggle-label">Raw</span>
</div>


</div>

<div id="model-loading" class="raw-loading" style="display:none;">Loading…</div>

<div id="docs-model-view" markdown="1">

<div class="model-main" markdown="1">

<section id="domain-demographics" class="domain-section" data-domain="demographics" markdown="1">

<div class="domain-banner domain-demographics">
<div class="domain-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-icon lucide-user"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
<div class="domain-banner-text">
<div class="domain-heading">Demographics</div>
<p class="domain-description">Demographics contains subject identity, enrollment, study participation, longitudinal episode structure, survival status, family and medical history, and other contextual information needed to interpret records across the model.</p>
</div>
</div>

<section id="class-subjectcharacteristics" class="class-section" markdown="1">

## SubjectCharacteristics

<p class="class-description">SubjectCharacteristics captures core subject-level identifiers, data source context, and last-known survival/contact status needed to anchor all other records in the model.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="data_contributor_id"><details class="cell-details"><summary><span>data_contributor_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DataContributorIDEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-datacontributoridenum')">DataContributorIDEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="data_source"><details class="cell-details"><summary><span>data_source</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DataSourceEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-datasourceenum')">DataSourceEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="last_known_survival_status"><details class="cell-details"><summary><span>last_known_survival_status</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="LastKnownSurvivalStatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-lastknownsurvivalstatusenum')">LastKnownSurvivalStatusEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_last_contact"><details class="cell-details"><summary><span>age_last_contact</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_last_contact_unit"><details class="cell-details"><summary><span>age_last_contact_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_last_contact_precision"><details class="cell-details"><summary><span>age_last_contact_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-timing" class="class-section" markdown="1">

## Timing

<p class="class-description">Timing represents named clinical or research timepoints and their associated ages, providing the longitudinal structure used to align observations across the model.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="timepoint"><details class="cell-details"><summary><span>timepoint</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="TimepointEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-timepointenum')">TimepointEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="timing_age_at"><details class="cell-details"><summary><span>timing_age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-familymedicalhistory" class="class-section" markdown="1">

## FamilyMedicalHistory

<p class="class-description">FamilyMedicalHistory captures diabetes-related conditions reported among relatives, supporting representation of inherited patterns and familial disease context.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="relation_honest_broker_subject_id"><details class="cell-details"><summary><span>relation_honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="relation"><details class="cell-details"><summary><span>relation</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="RelationEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-relationenum')">RelationEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="condition"><details class="cell-details"><summary><span>condition</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ConditionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-conditionenum')">ConditionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="source"><details class="cell-details"><summary><span>source</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SourceEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-sourceenum')">SourceEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-demographics" class="class-section" markdown="1">

## Demographics

<p class="class-description">Demographics captures subject-level sex, race, and ethnicity information used to describe study populations and support cohort characterization.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="sex"><details class="cell-details"><summary><span>sex</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SexEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-sexenum')">SexEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="ethnicity"><details class="cell-details"><summary><span>ethnicity</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="EthnicityEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-ethnicityenum')">EthnicityEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="race"><details class="cell-details"><summary><span>race</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="RaceEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-raceenum')">RaceEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-medicalhistory" class="class-section" markdown="1">

## MedicalHistory

<p class="class-description">MedicalHistory records prior or co-occurring medical conditions for a subject, including coded condition details when available.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at"><details class="cell-details"><summary><span>age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medical_history_condition"><details class="cell-details"><summary><span>medical_history_condition</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MedicalHistoryConditionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-medicalhistoryconditionenum')">MedicalHistoryConditionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="condition_other"><details class="cell-details"><summary><span>condition_other</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="condition_code"><details class="cell-details"><summary><span>condition_code</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="code_system"><details class="cell-details"><summary><span>code_system</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="CodeSystemEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-codesystemenum')">CodeSystemEnum</button></span></td></tr></tbody></table>

</section>

</section>

<section id="domain-testing" class="domain-section" data-domain="testing" markdown="1">

<div class="domain-banner domain-testing">
<div class="domain-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-dna-icon lucide-dna"><path d="m10 16 1.5 1.5"/><path d="m14 8-1.5-1.5"/><path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993"/><path d="m16.5 10.5 1 1"/><path d="m17 6-2.891-2.891"/><path d="M2 15c6.667-6 13.333 0 20-6"/><path d="m20 9 .891.891"/><path d="M3.109 14.109 4 15"/><path d="m6.5 12.5 1 1"/><path d="m7 18 2.891 2.891"/><path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993"/></svg></div>
<div class="domain-banner-text">
<div class="domain-heading">Testing</div>
<p class="domain-description">Testing contains laboratory, pathology, genomic, functional, anthropometric, and specimen-related observations used to characterize subjects, disease biology, eligibility, monitoring, and research sample availability.</p>
</div>
</div>

<section id="class-biometrics" class="class-section" markdown="1">

## Biometrics

<p class="class-description">Biometrics captures anthropometric measurements such as height, weight, BMI, and related standardized scores used to characterize growth and body size over time.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at"><details class="cell-details"><summary><span>age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="measurement_type"><details class="cell-details"><summary><span>measurement_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MeasurementTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-measurementtypeenum')">MeasurementTypeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="measurement_numeric"><details class="cell-details"><summary><span>measurement_numeric</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="measurement_unit"><details class="cell-details"><summary><span>measurement_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MeasurementUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-measurementunitenum')">MeasurementUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="z_score"><details class="cell-details"><summary><span>z_score</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr></tbody></table>

</section>

<section id="class-biospecimen" class="class-section" markdown="1">

## Biospecimen

<p class="class-description">Biospecimen records available subject specimens by sample type, supporting linkage between clinical data and biological materials for research use.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="sample_type"><details class="cell-details"><summary><span>sample_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SampleTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-sampletypeenum')">SampleTypeEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-geneticanalysis" class="class-section" markdown="1">

## GeneticAnalysis

<p class="class-description">GeneticAnalysis captures genetic testing results, including methods, genes, alteration details, HGVS nomenclature, reported significance, allelic state, and related external references.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at"><details class="cell-details"><summary><span>age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="causative_alteration"><details class="cell-details"><summary><span>causative_alteration</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="YesNoEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="status"><details class="cell-details"><summary><span>status</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="StatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-statusenum')">StatusEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="genetic_analysis_sample_type"><details class="cell-details"><summary><span>genetic_analysis_sample_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="GeneticAnalysisSampleTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-geneticanalysissampletypeenum')">GeneticAnalysisSampleTypeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="laboratory_name"><details class="cell-details"><summary><span>laboratory_name</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="LaboratoryNameEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-laboratorynameenum')">LaboratoryNameEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="cytogenetic_location"><details class="cell-details"><summary><span>cytogenetic_location</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="method"><details class="cell-details"><summary><span>method</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MethodEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-methodenum')">MethodEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="gene"><details class="cell-details"><summary><span>gene</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="GeneEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-geneenum')">GeneEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="alteration_type"><details class="cell-details"><summary><span>alteration_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AlterationTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-alterationtypeenum')">AlterationTypeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="alteration_effect"><details class="cell-details"><summary><span>alteration_effect</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AlterationEffectEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-alterationeffectenum')">AlterationEffectEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="alteration_region"><details class="cell-details"><summary><span>alteration_region</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AlterationRegionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-alterationregionenum')">AlterationRegionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="hgvs_accession"><details class="cell-details"><summary><span>hgvs_accession</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="hgvs_coding"><details class="cell-details"><summary><span>hgvs_coding</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="hgvs_protein"><details class="cell-details"><summary><span>hgvs_protein</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="hgvs_genomic"><details class="cell-details"><summary><span>hgvs_genomic</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="iscn"><details class="cell-details"><summary><span>iscn</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="reported_significance"><details class="cell-details"><summary><span>reported_significance</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ReportedSignificanceEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-reportedsignificanceenum')">ReportedSignificanceEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="allelic_state"><details class="cell-details"><summary><span>allelic_state</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AllelicStateEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-allelicstateenum')">AllelicStateEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="maf_numeric"><details class="cell-details"><summary><span>maf_numeric</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="mosaicism"><details class="cell-details"><summary><span>mosaicism</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="YesNoEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-yesnoenum')">YesNoEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="external_ref_id"><details class="cell-details"><summary><span>external_ref_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="external_ref_id_system"><details class="cell-details"><summary><span>external_ref_id_system</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ExternalRefIDSystemEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-externalrefidsystemenum')">ExternalRefIDSystemEnum</button></span></td></tr></tbody></table>

</section>

<section id="class-testing" class="class-section" markdown="1">

## Testing

<p class="class-description">Testing captures laboratory, glucose-monitoring, and related clinical test results, including numeric values, units, interpretation, fasting status, and timepoint-specific testing context.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at"><details class="cell-details"><summary><span>age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="test_type"><details class="cell-details"><summary><span>test_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="TestTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-testtypeenum')">TestTypeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="testing_method"><details class="cell-details"><summary><span>testing_method</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="TestingMethodEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-testingmethodenum')">TestingMethodEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="testing_measurement_type"><details class="cell-details"><summary><span>testing_measurement_type</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="TestingMeasurementTypeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-testingmeasurementtypeenum')">TestingMeasurementTypeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="result_modifier"><details class="cell-details"><summary><span>result_modifier</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="result_numeric"><details class="cell-details"><summary><span>result_numeric</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="result_unit"><details class="cell-details"><summary><span>result_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ResultUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-resultunitenum')">ResultUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="reference_range"><details class="cell-details"><summary><span>reference_range</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="result_interpretation"><details class="cell-details"><summary><span>result_interpretation</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ResultInterpretationEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-resultinterpretationenum')">ResultInterpretationEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="fasting_status"><details class="cell-details"><summary><span>fasting_status</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="FastingStatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-fastingstatusenum')">FastingStatusEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="post_glucose_timepoint"><details class="cell-details"><summary><span>post_glucose_timepoint</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="post_glucose_timepoint_unit"><details class="cell-details"><summary><span>post_glucose_timepoint_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="PostGlucoseTimepointUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-postglucosetimepointunitenum')">PostGlucoseTimepointUnitEnum</button></span></td></tr></tbody></table>

</section>

</section>

<section id="domain-disease-attributes" class="domain-section" data-domain="disease-attributes" markdown="1">

<div class="domain-banner domain-disease-attributes">
<div class="domain-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-network-icon lucide-network"><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/></svg></div>
<div class="domain-banner-text">
<div class="domain-heading">Disease Attributes</div>
<p class="domain-description">Disease Attributes contains diagnostic, staging, anatomic, histologic, biologic, risk, extent-of-disease, and disease-site concepts used to characterize the subject's cancer or cancer-related condition.</p>
</div>
</div>

<section id="class-diseasecharacteristics" class="class-section" markdown="1">

## DiseaseCharacteristics

<p class="class-description">DiseaseCharacteristics records monogenic diabetes-related disease features, including diabetes status, hypoglycemia, ketoacidosis, glucose range metrics, diet, and exercise observations.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at"><details class="cell-details"><summary><span>age_at</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="diabetes_status"><details class="cell-details"><summary><span>diabetes_status</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DiabetesStatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-diabetesstatusenum')">DiabetesStatusEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="hypoglycemia_frequency"><details class="cell-details"><summary><span>hypoglycemia_frequency</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="HypoglycemiaFrequencyEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-hypoglycemiafrequencyenum')">HypoglycemiaFrequencyEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="severe_hypoglycemia_frequency"><details class="cell-details"><summary><span>severe_hypoglycemia_frequency</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="HypoglycemiaFrequencyEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-hypoglycemiafrequencyenum')">HypoglycemiaFrequencyEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="dka"><details class="cell-details"><summary><span>dka</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DKAEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-dkaenum')">DKAEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="time_in_range"><details class="cell-details"><summary><span>time_in_range</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="cgm_range"><details class="cell-details"><summary><span>cgm_range</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="CGMRangeEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-cgmrangeenum')">CGMRangeEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="diet"><details class="cell-details"><summary><span>diet</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DiabetesStatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-diabetesstatusenum')">DiabetesStatusEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="exercise"><details class="cell-details"><summary><span>exercise</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DiabetesStatusEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-diabetesstatusenum')">DiabetesStatusEnum</button></span></td></tr></tbody></table>

</section>

</section>

<section id="domain-intervention" class="domain-section" data-domain="intervention" markdown="1">

<div class="domain-banner domain-intervention">
<div class="domain-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-hospital-icon lucide-hospital"><path d="M12 7v4"/><path d="M14 21v-3a2 2 0 0 0-4 0v3"/><path d="M14 9h-4"/><path d="M18 11h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 21V5a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16"/></svg></div>
<div class="domain-banner-text">
<div class="domain-heading">Intervention</div>
<p class="domain-description">Intervention contains treatment and procedure records, including surgery, medications, radiation therapy, transplantation, transfusion, cellular therapy, locoregional therapy, fertility preservation procedures, and protocol treatment modifications.</p>
</div>
</div>

<section id="class-treatment" class="class-section" markdown="1">

## Treatment

<p class="class-description">Treatment captures diabetes-related medications and therapies, including medication class, name, dose, unit, route, frequency, timing, and reason for stopping treatment.</p>

<table class="model-table class-slot-table"><thead><tr><th>Slot</th><th>Description</th><th>Range</th></tr></thead><tbody><tr data-subsets="base"><td class="slot-name" title="honest_broker_subject_id"><details class="cell-details"><summary><span>honest_broker_subject_id</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="subject_characteristics"><details class="cell-details"><summary><span>subject_characteristics</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="SubjectCharacteristics"><span><code class="primitive-range">SubjectCharacteristics</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at_start"><details class="cell-details"><summary><span>age_at_start</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_at_stop"><details class="cell-details"><summary><span>age_at_stop</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="integer"><span><code class="primitive-range">integer</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_unit"><details class="cell-details"><summary><span>age_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactunitenum')">AgeLastContactUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="age_precision"><details class="cell-details"><summary><span>age_precision</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="AgeLastContactPrecisionEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-agelastcontactprecisionenum')">AgeLastContactPrecisionEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="reason_stop"><details class="cell-details"><summary><span>reason_stop</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="ReasonStopEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-reasonstopenum')">ReasonStopEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="dm_medication_class"><details class="cell-details"><summary><span>dm_medication_class</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="DMMedicationClassEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-dmmedicationclassenum')">DMMedicationClassEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_class_other"><details class="cell-details"><summary><span>medication_class_other</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MedicationClassOtherEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-medicationclassotherenum')">MedicationClassOtherEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_name"><details class="cell-details"><summary><span>medication_name</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_code"><details class="cell-details"><summary><span>medication_code</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="string"><span><code class="primitive-range">string</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_concentration"><details class="cell-details"><summary><span>medication_concentration</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MedicationConcentrationEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-medicationconcentrationenum')">MedicationConcentrationEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_dose"><details class="cell-details"><summary><span>medication_dose</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="decimal"><span><code class="primitive-range">decimal</code></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="medication_unit"><details class="cell-details"><summary><span>medication_unit</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="MedicationUnitEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-medicationunitenum')">MedicationUnitEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="frequency"><details class="cell-details"><summary><span>frequency</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="FrequencyEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-frequencyenum')">FrequencyEnum</button></span></td></tr>
<tr data-subsets="base"><td class="slot-name" title="route"><details class="cell-details"><summary><span>route</span></summary></details></td><td class="slot-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="slot-range" title="RouteEnum"><span><button type="button" class="enum-link" onclick="openEnumModal('enum-modal-routeenum')">RouteEnum</button></span></td></tr></tbody></table>

</section>

</section>

<div id="enum-modal-agelastcontactprecisionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-agelastcontactprecisionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-agelastcontactprecisionenum')">×</button>
<h3>AgeLastContactPrecisionEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Approximate"><details class="cell-details"><summary><span>Approximate</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Exact"><details class="cell-details"><summary><span>Exact</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-agelastcontactunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-agelastcontactunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-agelastcontactunitenum')">×</button>
<h3>AgeLastContactUnitEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Years"><details class="cell-details"><summary><span>Years</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Months"><details class="cell-details"><summary><span>Months</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Weeks"><details class="cell-details"><summary><span>Weeks</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Days"><details class="cell-details"><summary><span>Days</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-allelicstateenum" class="enum-modal" onclick="closeEnumModal('enum-modal-allelicstateenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-allelicstateenum')">×</button>
<h3>AllelicStateEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Homozygous"><details class="cell-details"><summary><span>Homozygous</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Heterozygous"><details class="cell-details"><summary><span>Heterozygous</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Compound Heterozygous"><details class="cell-details"><summary><span>Compound Heterozygous</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-alterationeffectenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationeffectenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationeffectenum')">×</button>
<h3>AlterationEffectEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Frameshift"><details class="cell-details"><summary><span>Frameshift</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Missense"><details class="cell-details"><summary><span>Missense</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Stop Gain (Nonsense)"><details class="cell-details"><summary><span>Stop Gain (Nonsense)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="None (Inframe)"><details class="cell-details"><summary><span>None (Inframe)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-alterationregionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationregionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationregionenum')">×</button>
<h3>AlterationRegionEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Splice Site"><details class="cell-details"><summary><span>Splice Site</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="5' UTR"><details class="cell-details"><summary><span>5' UTR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="3' UTR"><details class="cell-details"><summary><span>3' UTR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-alterationtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-alterationtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-alterationtypeenum')">×</button>
<h3>AlterationTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Chromosome Arm Gain"><details class="cell-details"><summary><span>Chromosome Arm Gain</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Chromosome Arm Loss"><details class="cell-details"><summary><span>Chromosome Arm Loss</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Substitution"><details class="cell-details"><summary><span>Substitution</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Deletion"><details class="cell-details"><summary><span>Deletion</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Insertion"><details class="cell-details"><summary><span>Insertion</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Indel"><details class="cell-details"><summary><span>Indel</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Duplication"><details class="cell-details"><summary><span>Duplication</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-cgmrangeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-cgmrangeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-cgmrangeenum')">×</button>
<h3>CGMRangeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Standard"><details class="cell-details"><summary><span>Standard</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Non-Standard"><details class="cell-details"><summary><span>Non-Standard</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-codesystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-codesystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-codesystemenum')">×</button>
<h3>CodeSystemEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="CTCAE"><details class="cell-details"><summary><span>CTCAE</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ICD-9"><details class="cell-details"><summary><span>ICD-9</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ICD-10"><details class="cell-details"><summary><span>ICD-10</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="SNOMED-CT"><details class="cell-details"><summary><span>SNOMED-CT</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-conditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-conditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-conditionenum')">×</button>
<h3>ConditionEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Prediabetes"><details class="cell-details"><summary><span>Prediabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Type 1 Diabetes"><details class="cell-details"><summary><span>Type 1 Diabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Type 2 Diabetes"><details class="cell-details"><summary><span>Type 2 Diabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Monogenic Diabetes"><details class="cell-details"><summary><span>Monogenic Diabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Gestational Diabetes"><details class="cell-details"><summary><span>Gestational Diabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Diabetes, NOS"><details class="cell-details"><summary><span>Diabetes, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-dkaenum" class="enum-modal" onclick="closeEnumModal('enum-modal-dkaenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-dkaenum')">×</button>
<h3>DKAEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Yes - Hyperglycermic DKA"><details class="cell-details"><summary><span>Yes - Hyperglycermic DKA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Yes - Euglycemic DKA"><details class="cell-details"><summary><span>Yes - Euglycemic DKA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="No"><details class="cell-details"><summary><span>No</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-dmmedicationclassenum" class="enum-modal" onclick="closeEnumModal('enum-modal-dmmedicationclassenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-dmmedicationclassenum')">×</button>
<h3>DMMedicationClassEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Insulin, Rapid-Acting"><details class="cell-details"><summary><span>Insulin, Rapid-Acting</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Insulin, Long-Acting"><details class="cell-details"><summary><span>Insulin, Long-Acting</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Insulin, Intermediate-Acting"><details class="cell-details"><summary><span>Insulin, Intermediate-Acting</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Insulin, Combination"><details class="cell-details"><summary><span>Insulin, Combination</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Insulin, NOS"><details class="cell-details"><summary><span>Insulin, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Biguanide"><details class="cell-details"><summary><span>Biguanide</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sulfonylurea"><details class="cell-details"><summary><span>Sulfonylurea</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Meglitinide"><details class="cell-details"><summary><span>Meglitinide</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Thiazolidinedione"><details class="cell-details"><summary><span>Thiazolidinedione</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Dipeptidylpeptidase 4 Inhibitor"><details class="cell-details"><summary><span>Dipeptidylpeptidase 4 Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sodium-Glucose Co-Transporter 2 Inhibitor"><details class="cell-details"><summary><span>Sodium-Glucose Co-Transporter 2 Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GLP-1 Receptor Agonist"><details class="cell-details"><summary><span>GLP-1 Receptor Agonist</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Dual GLP-1/GIP Receptor Agonist"><details class="cell-details"><summary><span>Dual GLP-1/GIP Receptor Agonist</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Amylin Analog"><details class="cell-details"><summary><span>Amylin Analog</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Alpha-Glucosidase Inhibitor"><details class="cell-details"><summary><span>Alpha-Glucosidase Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Bile Acid-Binding Resin"><details class="cell-details"><summary><span>Bile Acid-Binding Resin</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-datacontributoridenum" class="enum-modal" onclick="closeEnumModal('enum-modal-datacontributoridenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-datacontributoridenum')">×</button>
<h3>DataContributorIDEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="UChicago Monogenic Diabetes Research Group"><details class="cell-details"><summary><span>UChicago Monogenic Diabetes Research Group</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Barbara Davis Center / UColorado"><details class="cell-details"><summary><span>Barbara Davis Center / UColorado</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Baylor"><details class="cell-details"><summary><span>Baylor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Boston Children's"><details class="cell-details"><summary><span>Boston Children's</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Cincinnati Children's Hospital"><details class="cell-details"><summary><span>Cincinnati Children's Hospital</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Indiana"><details class="cell-details"><summary><span>Indiana</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="MGH"><details class="cell-details"><summary><span>MGH</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Maryland"><details class="cell-details"><summary><span>Maryland</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Michigan"><details class="cell-details"><summary><span>Michigan</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Nebraska"><details class="cell-details"><summary><span>Nebraska</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="NorthShore"><details class="cell-details"><summary><span>NorthShore</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="WashU"><details class="cell-details"><summary><span>WashU</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-datasourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-datasourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-datasourceenum')">×</button>
<h3>DataSourceEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Self-Reported"><details class="cell-details"><summary><span>Self-Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="EHR"><details class="cell-details"><summary><span>EHR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-diabetesstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-diabetesstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-diabetesstatusenum')">×</button>
<h3>DiabetesStatusEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Yes"><details class="cell-details"><summary><span>Yes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="No"><details class="cell-details"><summary><span>No</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-ethnicityenum" class="enum-modal" onclick="closeEnumModal('enum-modal-ethnicityenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-ethnicityenum')">×</button>
<h3>EthnicityEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Hispanic or Latino"><details class="cell-details"><summary><span>Hispanic or Latino</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Hispanic or Latino"><details class="cell-details"><summary><span>Not Hispanic or Latino</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-externalrefidsystemenum" class="enum-modal" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-externalrefidsystemenum')">×</button>
<h3>ExternalRefIDSystemEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="ClinGen"><details class="cell-details"><summary><span>ClinGen</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ClinVar"><details class="cell-details"><summary><span>ClinVar</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-fastingstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-fastingstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-fastingstatusenum')">×</button>
<h3>FastingStatusEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Fasting"><details class="cell-details"><summary><span>Fasting</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Non-Fasting"><details class="cell-details"><summary><span>Non-Fasting</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Random"><details class="cell-details"><summary><span>Random</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-frequencyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-frequencyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-frequencyenum')">×</button>
<h3>FrequencyEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Once per day"><details class="cell-details"><summary><span>Once per day</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Two times a day"><details class="cell-details"><summary><span>Two times a day</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Three times a day"><details class="cell-details"><summary><span>Three times a day</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Four times a day"><details class="cell-details"><summary><span>Four times a day</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="As needed"><details class="cell-details"><summary><span>As needed</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Before every meal"><details class="cell-details"><summary><span>Before every meal</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Before meals and at bedtime"><details class="cell-details"><summary><span>Before meals and at bedtime</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Every night at bedtime"><details class="cell-details"><summary><span>Every night at bedtime</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Every week"><details class="cell-details"><summary><span>Every week</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-geneenum" class="enum-modal" onclick="closeEnumModal('enum-modal-geneenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-geneenum')">×</button>
<h3>GeneEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="6q24-Related Abnormalities"><details class="cell-details"><summary><span>6q24-Related Abnormalities</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ABCC8"><details class="cell-details"><summary><span>ABCC8</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="CEL"><details class="cell-details"><summary><span>CEL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="CFTR"><details class="cell-details"><summary><span>CFTR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="DCAF17"><details class="cell-details"><summary><span>DCAF17</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="EIF2AK3"><details class="cell-details"><summary><span>EIF2AK3</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="FOXP3"><details class="cell-details"><summary><span>FOXP3</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GATA4"><details class="cell-details"><summary><span>GATA4</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GATA6"><details class="cell-details"><summary><span>GATA6</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GCK"><details class="cell-details"><summary><span>GCK</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GLIS3"><details class="cell-details"><summary><span>GLIS3</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="HNF1A"><details class="cell-details"><summary><span>HNF1A</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="HNF1B"><details class="cell-details"><summary><span>HNF1B</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="HNF4A"><details class="cell-details"><summary><span>HNF4A</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IAPP (Amylin)"><details class="cell-details"><summary><span>IAPP (Amylin)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IER3IP1"><details class="cell-details"><summary><span>IER3IP1</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IGF2/Russell Silver Syndrome"><details class="cell-details"><summary><span>IGF2/Russell Silver Syndrome</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IL2RA"><details class="cell-details"><summary><span>IL2RA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="INS"><details class="cell-details"><summary><span>INS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="INSR"><details class="cell-details"><summary><span>INSR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="KCNJ11"><details class="cell-details"><summary><span>KCNJ11</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="LRBA"><details class="cell-details"><summary><span>LRBA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mtDNA"><details class="cell-details"><summary><span>mtDNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="NEUROD1"><details class="cell-details"><summary><span>NEUROD1</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PAX4"><details class="cell-details"><summary><span>PAX4</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PCBD1"><details class="cell-details"><summary><span>PCBD1</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PDX1 (IPF1)"><details class="cell-details"><summary><span>PDX1 (IPF1)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PTF1A"><details class="cell-details"><summary><span>PTF1A</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="RFX6"><details class="cell-details"><summary><span>RFX6</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="STAT3"><details class="cell-details"><summary><span>STAT3</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="WFS1"><details class="cell-details"><summary><span>WFS1</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-geneticanalysissampletypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-geneticanalysissampletypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-geneticanalysissampletypeenum')">×</button>
<h3>GeneticAnalysisSampleTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Saliva"><details class="cell-details"><summary><span>Saliva</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Blood"><details class="cell-details"><summary><span>Blood</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Buccal"><details class="cell-details"><summary><span>Buccal</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Urine"><details class="cell-details"><summary><span>Urine</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-hypoglycemiafrequencyenum" class="enum-modal" onclick="closeEnumModal('enum-modal-hypoglycemiafrequencyenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-hypoglycemiafrequencyenum')">×</button>
<h3>HypoglycemiaFrequencyEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Once or twice in past year"><details class="cell-details"><summary><span>Once or twice in past year</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Every few months"><details class="cell-details"><summary><span>Every few months</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Once or twice a month"><details class="cell-details"><summary><span>Once or twice a month</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Once or twice a week"><details class="cell-details"><summary><span>Once or twice a week</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Daily or every other day"><details class="cell-details"><summary><span>Daily or every other day</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Never"><details class="cell-details"><summary><span>Never</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-laboratorynameenum" class="enum-modal" onclick="closeEnumModal('enum-modal-laboratorynameenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-laboratorynameenum')">×</button>
<h3>LaboratoryNameEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Ambry Genetics"><details class="cell-details"><summary><span>Ambry Genetics</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Athena"><details class="cell-details"><summary><span>Athena</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Baylor Genetics"><details class="cell-details"><summary><span>Baylor Genetics</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Blueprint"><details class="cell-details"><summary><span>Blueprint</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GeneDx"><details class="cell-details"><summary><span>GeneDx</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Invitae"><details class="cell-details"><summary><span>Invitae</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="LMG"><details class="cell-details"><summary><span>LMG</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Research Lab"><details class="cell-details"><summary><span>Research Lab</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Seattle Children's Hospital"><details class="cell-details"><summary><span>Seattle Children's Hospital</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="UCGSL"><details class="cell-details"><summary><span>UCGSL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-lastknownsurvivalstatusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-lastknownsurvivalstatusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-lastknownsurvivalstatusenum')">×</button>
<h3>LastKnownSurvivalStatusEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Alive"><details class="cell-details"><summary><span>Alive</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Dead"><details class="cell-details"><summary><span>Dead</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-measurementtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-measurementtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-measurementtypeenum')">×</button>
<h3>MeasurementTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Height/Length"><details class="cell-details"><summary><span>Height/Length</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Weight"><details class="cell-details"><summary><span>Weight</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="BMI"><details class="cell-details"><summary><span>BMI</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Raw BMI"><details class="cell-details"><summary><span>Raw BMI</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-measurementunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-measurementunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-measurementunitenum')">×</button>
<h3>MeasurementUnitEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="kg"><details class="cell-details"><summary><span>kg</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="cm"><details class="cell-details"><summary><span>cm</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="kg/m^2"><details class="cell-details"><summary><span>kg/m^2</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="percentile"><details class="cell-details"><summary><span>percentile</span></summary></details></td><td class="enum-description" title="(md_v1.3) ConsortiumNote: Use percentile as a unit when reporting pediatric BMI."><details class="cell-details"><summary><span>(md_v1.3) ConsortiumNote: Use percentile as a unit when reporting pediatric BMI.</span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-medicalhistoryconditionenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicalhistoryconditionenum')">×</button>
<h3>MedicalHistoryConditionEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Abnormal Kidney Shape, Size, Or Number"><details class="cell-details"><summary><span>Abnormal Kidney Shape, Size, Or Number</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Absent Or Missing Pancreas"><details class="cell-details"><summary><span>Absent Or Missing Pancreas</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Behavioral Difficulties"><details class="cell-details"><summary><span>Behavioral Difficulties</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Congenital Heart Defect"><details class="cell-details"><summary><span>Congenital Heart Defect</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Coronary Artery Disease"><details class="cell-details"><summary><span>Coronary Artery Disease</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Difficulty With Social Interactions"><details class="cell-details"><summary><span>Difficulty With Social Interactions</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Elevated Liver Enzymes / Lfts"><details class="cell-details"><summary><span>Elevated Liver Enzymes / Lfts</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Fatty Liver"><details class="cell-details"><summary><span>Fatty Liver</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Genitourinary Developmental Malformation Or Abnormality"><details class="cell-details"><summary><span>Genitourinary Developmental Malformation Or Abnormality</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Gestational Diabetes"><details class="cell-details"><summary><span>Gestational Diabetes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Hepatomegaly"><details class="cell-details"><summary><span>Hepatomegaly</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="High Cholesterol, NOS"><details class="cell-details"><summary><span>High Cholesterol, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="High Frequency Hearing Loss"><details class="cell-details"><summary><span>High Frequency Hearing Loss</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="High LDL"><details class="cell-details"><summary><span>High LDL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="High Total Cholesterol"><details class="cell-details"><summary><span>High Total Cholesterol</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="High Triglycerides"><details class="cell-details"><summary><span>High Triglycerides</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Hypertension"><details class="cell-details"><summary><span>Hypertension</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Hypoglycemia In Infancy"><details class="cell-details"><summary><span>Hypoglycemia In Infancy</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Intrauterine Growth Restriction"><details class="cell-details"><summary><span>Intrauterine Growth Restriction</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Liver Adenoma"><details class="cell-details"><summary><span>Liver Adenoma</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Low Frequency Hearing Loss"><details class="cell-details"><summary><span>Low Frequency Hearing Loss</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Low LDL"><details class="cell-details"><summary><span>Low LDL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Macroglossia"><details class="cell-details"><summary><span>Macroglossia</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Nephropathy"><details class="cell-details"><summary><span>Nephropathy</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Peripheral Artery Disease"><details class="cell-details"><summary><span>Peripheral Artery Disease</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Peripheral Neuropathy"><details class="cell-details"><summary><span>Peripheral Neuropathy</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Polycystic Kidney Diseasea"><details class="cell-details"><summary><span>Polycystic Kidney Diseasea</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Proteinuria"><details class="cell-details"><summary><span>Proteinuria</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Renal CystL"><details class="cell-details"><summary><span>Renal CystL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Retinopathy"><details class="cell-details"><summary><span>Retinopathy</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Small For Gestational Age"><details class="cell-details"><summary><span>Small For Gestational Age</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Small Pancreas"><details class="cell-details"><summary><span>Small Pancreas</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Stroke"><details class="cell-details"><summary><span>Stroke</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Umbilical Hernia"><details class="cell-details"><summary><span>Umbilical Hernia</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Other"><details class="cell-details"><summary><span>Other</span></summary></details></td><td class="enum-description" title="(md_v1.3) ConsortiumNote: Only select 'Other' if the condition is not related to the provided list (which are designated as 'of interest' by the PREDICT group)."><details class="cell-details"><summary><span>(md_v1.3) ConsortiumNote: Only select 'Other' if the condition is not related to the provided list (which are designated as 'of interest' by the PREDICT group).</span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-medicationclassotherenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationclassotherenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationclassotherenum')">×</button>
<h3>MedicationClassOtherEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="ACE Inhibitor"><details class="cell-details"><summary><span>ACE Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ACL Inhibitor"><details class="cell-details"><summary><span>ACL Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Angiotensin II Receptor Blockers"><details class="cell-details"><summary><span>Angiotensin II Receptor Blockers</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ANGPTL3 Inhibitor"><details class="cell-details"><summary><span>ANGPTL3 Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Antiepileptic"><details class="cell-details"><summary><span>Antiepileptic</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Antilipemic siRNA"><details class="cell-details"><summary><span>Antilipemic siRNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Beta Blocker"><details class="cell-details"><summary><span>Beta Blocker</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Calcium Channel Blocker"><details class="cell-details"><summary><span>Calcium Channel Blocker</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Cholesterol Absorption Inhibitor"><details class="cell-details"><summary><span>Cholesterol Absorption Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Coenzyme Q"><details class="cell-details"><summary><span>Coenzyme Q</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Diuretic"><details class="cell-details"><summary><span>Diuretic</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Fibrates"><details class="cell-details"><summary><span>Fibrates</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Finerenone"><details class="cell-details"><summary><span>Finerenone</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Glucagon"><details class="cell-details"><summary><span>Glucagon</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Magnesium"><details class="cell-details"><summary><span>Magnesium</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Mineralcorticoid Receptor"><details class="cell-details"><summary><span>Mineralcorticoid Receptor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Pancreatic Enzymes"><details class="cell-details"><summary><span>Pancreatic Enzymes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Pcsk9 Inhibitor"><details class="cell-details"><summary><span>Pcsk9 Inhibitor</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Psychoactive"><details class="cell-details"><summary><span>Psychoactive</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Statin"><details class="cell-details"><summary><span>Statin</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-medicationconcentrationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationconcentrationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationconcentrationenum')">×</button>
<h3>MedicationConcentrationEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="U100"><details class="cell-details"><summary><span>U100</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="U200"><details class="cell-details"><summary><span>U200</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="U300"><details class="cell-details"><summary><span>U300</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="U500"><details class="cell-details"><summary><span>U500</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Applicable"><details class="cell-details"><summary><span>Not Applicable</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-medicationunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-medicationunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-medicationunitenum')">×</button>
<h3>MedicationUnitEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Units"><details class="cell-details"><summary><span>Units</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mg"><details class="cell-details"><summary><span>mg</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mcg"><details class="cell-details"><summary><span>mcg</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="gm"><details class="cell-details"><summary><span>gm</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ml"><details class="cell-details"><summary><span>ml</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="tbsp"><details class="cell-details"><summary><span>tbsp</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="tsp"><details class="cell-details"><summary><span>tsp</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IU"><details class="cell-details"><summary><span>IU</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="puffs"><details class="cell-details"><summary><span>puffs</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Packets"><details class="cell-details"><summary><span>Packets</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mg/ml"><details class="cell-details"><summary><span>mg/ml</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="application"><details class="cell-details"><summary><span>application</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-methodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-methodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-methodenum')">×</button>
<h3>MethodEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Karyotyping"><details class="cell-details"><summary><span>Karyotyping</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Fluorescence In Situ Hybridization"><details class="cell-details"><summary><span>Fluorescence In Situ Hybridization</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="RT-PCR"><details class="cell-details"><summary><span>RT-PCR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PCR"><details class="cell-details"><summary><span>PCR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="MLPA"><details class="cell-details"><summary><span>MLPA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, Sanger, Capillary Electropheresis"><details class="cell-details"><summary><span>Sequencing, Sanger, Capillary Electropheresis</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, Sanger, Gel Electropheresis"><details class="cell-details"><summary><span>Sequencing, Sanger, Gel Electropheresis</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, Sanger, NOS"><details class="cell-details"><summary><span>Sequencing, Sanger, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Whole Genome"><details class="cell-details"><summary><span>Sequencing, NGS, Whole Genome</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, lcWGS"><details class="cell-details"><summary><span>Sequencing, NGS, lcWGS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Whole Exome"><details class="cell-details"><summary><span>Sequencing, NGS, Whole Exome</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Multi-Gene Panel"><details class="cell-details"><summary><span>Sequencing, NGS, Multi-Gene Panel</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Single Site"><details class="cell-details"><summary><span>Sequencing, NGS, Single Site</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Single Gene DNA"><details class="cell-details"><summary><span>Sequencing, NGS, Single Gene DNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Targeted DNA"><details class="cell-details"><summary><span>Sequencing, NGS, Targeted DNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Targeted RNA"><details class="cell-details"><summary><span>Sequencing, NGS, Targeted RNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, Total RNA"><details class="cell-details"><summary><span>Sequencing, NGS, Total RNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, TDS"><details class="cell-details"><summary><span>Sequencing, NGS, TDS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, NGS, NOS"><details class="cell-details"><summary><span>Sequencing, NGS, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, Methylation Array"><details class="cell-details"><summary><span>Sequencing, Methylation Array</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sequencing, Nanostring"><details class="cell-details"><summary><span>Sequencing, Nanostring</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="SNP Array"><details class="cell-details"><summary><span>SNP Array</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Array CGH"><details class="cell-details"><summary><span>Array CGH</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Genotyping, NOS"><details class="cell-details"><summary><span>Genotyping, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Cytogenetics, NOS"><details class="cell-details"><summary><span>Cytogenetics, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Other"><details class="cell-details"><summary><span>Other</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-postglucosetimepointunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-postglucosetimepointunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-postglucosetimepointunitenum')">×</button>
<h3>PostGlucoseTimepointUnitEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Minutes"><details class="cell-details"><summary><span>Minutes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-raceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-raceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-raceenum')">×</button>
<h3>RaceEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="American Indian or Alaska Native"><details class="cell-details"><summary><span>American Indian or Alaska Native</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Asian"><details class="cell-details"><summary><span>Asian</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Black or African American"><details class="cell-details"><summary><span>Black or African American</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Native Hawaiian or Other Pacific Islander"><details class="cell-details"><summary><span>Native Hawaiian or Other Pacific Islander</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="White"><details class="cell-details"><summary><span>White</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Multiracial"><details class="cell-details"><summary><span>Multiracial</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-reasonstopenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reasonstopenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reasonstopenum')">×</button>
<h3>ReasonStopEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Planned Stop"><details class="cell-details"><summary><span>Planned Stop</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="No Significant Effect"><details class="cell-details"><summary><span>No Significant Effect</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Side Effects"><details class="cell-details"><summary><span>Side Effects</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="No Insured"><details class="cell-details"><summary><span>No Insured</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Cost"><details class="cell-details"><summary><span>Cost</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-relationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-relationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-relationenum')">×</button>
<h3>RelationEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Father"><details class="cell-details"><summary><span>Father</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Mother"><details class="cell-details"><summary><span>Mother</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Son"><details class="cell-details"><summary><span>Son</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Daughter"><details class="cell-details"><summary><span>Daughter</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Brother"><details class="cell-details"><summary><span>Brother</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Sister"><details class="cell-details"><summary><span>Sister</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Spouse/Partner"><details class="cell-details"><summary><span>Spouse/Partner</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Grandfather (Paternal)"><details class="cell-details"><summary><span>Grandfather (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Grandfather (Maternal)"><details class="cell-details"><summary><span>Grandfather (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Grandmother (Paternal)"><details class="cell-details"><summary><span>Grandmother (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Grandmother (Maternal)"><details class="cell-details"><summary><span>Grandmother (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Uncle (Paternal)"><details class="cell-details"><summary><span>Uncle (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Uncle (Maternal)"><details class="cell-details"><summary><span>Uncle (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Aunt (Paternal)"><details class="cell-details"><summary><span>Aunt (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Aunt (Maternal)"><details class="cell-details"><summary><span>Aunt (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Niece"><details class="cell-details"><summary><span>Niece</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Nephew"><details class="cell-details"><summary><span>Nephew</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="First Cousin (Paternal)"><details class="cell-details"><summary><span>First Cousin (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="First Cousin (Maternal)"><details class="cell-details"><summary><span>First Cousin (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="First Cousin (Paternal/Maternal Unknown)"><details class="cell-details"><summary><span>First Cousin (Paternal/Maternal Unknown)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Grandfather (Paternal)"><details class="cell-details"><summary><span>Great-Grandfather (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Grandfather (Maternal)"><details class="cell-details"><summary><span>Great-Grandfather (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Grandmother (Paternal)"><details class="cell-details"><summary><span>Great-Grandmother (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Grandmother (Maternal)"><details class="cell-details"><summary><span>Great-Grandmother (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Uncle (Paternal)"><details class="cell-details"><summary><span>Great-Uncle (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Uncle (Maternal)"><details class="cell-details"><summary><span>Great-Uncle (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Aunt (Paternal)"><details class="cell-details"><summary><span>Great-Aunt (Paternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Great-Aunt (Maternal)"><details class="cell-details"><summary><span>Great-Aunt (Maternal)</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Other"><details class="cell-details"><summary><span>Other</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-reportedsignificanceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-reportedsignificanceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-reportedsignificanceenum')">×</button>
<h3>ReportedSignificanceEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Pathogenic"><details class="cell-details"><summary><span>Pathogenic</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Likely Pathogenic"><details class="cell-details"><summary><span>Likely Pathogenic</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Uncertain Significance"><details class="cell-details"><summary><span>Uncertain Significance</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Likely Benign"><details class="cell-details"><summary><span>Likely Benign</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Benign"><details class="cell-details"><summary><span>Benign</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-resultinterpretationenum" class="enum-modal" onclick="closeEnumModal('enum-modal-resultinterpretationenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-resultinterpretationenum')">×</button>
<h3>ResultInterpretationEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Positive"><details class="cell-details"><summary><span>Positive</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Negative"><details class="cell-details"><summary><span>Negative</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-resultunitenum" class="enum-modal" onclick="closeEnumModal('enum-modal-resultunitenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-resultunitenum')">×</button>
<h3>ResultUnitEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="%"><details class="cell-details"><summary><span>%</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mg/dL"><details class="cell-details"><summary><span>mg/dL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="U/L"><details class="cell-details"><summary><span>U/L</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="U/mL"><details class="cell-details"><summary><span>U/mL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="mmol/L"><details class="cell-details"><summary><span>mmol/L</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ng/mL"><details class="cell-details"><summary><span>ng/mL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="nmol/L"><details class="cell-details"><summary><span>nmol/L</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-routeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-routeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-routeenum')">×</button>
<h3>RouteEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Oral"><details class="cell-details"><summary><span>Oral</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Nasally"><details class="cell-details"><summary><span>Nasally</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Subcutaneous"><details class="cell-details"><summary><span>Subcutaneous</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IM"><details class="cell-details"><summary><span>IM</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="IV"><details class="cell-details"><summary><span>IV</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-sampletypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sampletypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sampletypeenum')">×</button>
<h3>SampleTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Saliva"><details class="cell-details"><summary><span>Saliva</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Blood"><details class="cell-details"><summary><span>Blood</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="DNA"><details class="cell-details"><summary><span>DNA</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Plasma"><details class="cell-details"><summary><span>Plasma</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Serum"><details class="cell-details"><summary><span>Serum</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Urine"><details class="cell-details"><summary><span>Urine</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="PBMC"><details class="cell-details"><summary><span>PBMC</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-sexenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sexenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sexenum')">×</button>
<h3>SexEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Male"><details class="cell-details"><summary><span>Male</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Female"><details class="cell-details"><summary><span>Female</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Undifferentiated"><details class="cell-details"><summary><span>Undifferentiated</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-sourceenum" class="enum-modal" onclick="closeEnumModal('enum-modal-sourceenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-sourceenum')">×</button>
<h3>SourceEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Confirmed By Genetic Test"><details class="cell-details"><summary><span>Confirmed By Genetic Test</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Clinical Diagnosis Only"><details class="cell-details"><summary><span>Clinical Diagnosis Only</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-statusenum" class="enum-modal" onclick="closeEnumModal('enum-modal-statusenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-statusenum')">×</button>
<h3>StatusEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Present"><details class="cell-details"><summary><span>Present</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Absent"><details class="cell-details"><summary><span>Absent</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-testtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-testtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-testtypeenum')">×</button>
<h3>TestTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="HbA1c"><details class="cell-details"><summary><span>HbA1c</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="C-Peptide"><details class="cell-details"><summary><span>C-Peptide</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Blood Glucose"><details class="cell-details"><summary><span>Blood Glucose</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, GAD65"><details class="cell-details"><summary><span>Autoantibodies, GAD65</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, ZnT8"><details class="cell-details"><summary><span>Autoantibodies, ZnT8</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, IA-2"><details class="cell-details"><summary><span>Autoantibodies, IA-2</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, Insulin"><details class="cell-details"><summary><span>Autoantibodies, Insulin</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, Islet Cell"><details class="cell-details"><summary><span>Autoantibodies, Islet Cell</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Autoantibodies, NOS"><details class="cell-details"><summary><span>Autoantibodies, NOS</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Total Cholesterol"><details class="cell-details"><summary><span>Total Cholesterol</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Triglycerides"><details class="cell-details"><summary><span>Triglycerides</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="HDL"><details class="cell-details"><summary><span>HDL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="LDL"><details class="cell-details"><summary><span>LDL</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Serum Magnesium"><details class="cell-details"><summary><span>Serum Magnesium</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Serum Potassium"><details class="cell-details"><summary><span>Serum Potassium</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Serum Creatinine"><details class="cell-details"><summary><span>Serum Creatinine</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Serum BUN"><details class="cell-details"><summary><span>Serum BUN</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="GFR"><details class="cell-details"><summary><span>GFR</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Urine Microalbumin"><details class="cell-details"><summary><span>Urine Microalbumin</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Urine Creatinine"><details class="cell-details"><summary><span>Urine Creatinine</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Microalbumin/Creatinine Ratio"><details class="cell-details"><summary><span>Microalbumin/Creatinine Ratio</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Urine MagnesiumSerum Potassium"><details class="cell-details"><summary><span>Urine MagnesiumSerum Potassium</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="ALT"><details class="cell-details"><summary><span>ALT</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="AST"><details class="cell-details"><summary><span>AST</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-testingmeasurementtypeenum" class="enum-modal" onclick="closeEnumModal('enum-modal-testingmeasurementtypeenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-testingmeasurementtypeenum')">×</button>
<h3>TestingMeasurementTypeEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Average High"><details class="cell-details"><summary><span>Average High</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="14-day Average"><details class="cell-details"><summary><span>14-day Average</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="30-day Average"><details class="cell-details"><summary><span>30-day Average</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="90-day Average"><details class="cell-details"><summary><span>90-day Average</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Average"><details class="cell-details"><summary><span>Average</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Average Low"><details class="cell-details"><summary><span>Average Low</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Point"><details class="cell-details"><summary><span>Point</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-testingmethodenum" class="enum-modal" onclick="closeEnumModal('enum-modal-testingmethodenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-testingmethodenum')">×</button>
<h3>TestingMethodEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Continuous Glucose Monitoring"><details class="cell-details"><summary><span>Continuous Glucose Monitoring</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Laboratory Test"><details class="cell-details"><summary><span>Laboratory Test</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Home Glucose Test"><details class="cell-details"><summary><span>Home Glucose Test</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-timepointenum" class="enum-modal" onclick="closeEnumModal('enum-modal-timepointenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-timepointenum')">×</button>
<h3>TimepointEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Prediabetes Diagnosis"><details class="cell-details"><summary><span>Prediabetes Diagnosis</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Diagnosis"><details class="cell-details"><summary><span>Diagnosis</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Relapse"><details class="cell-details"><summary><span>Relapse</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Remission"><details class="cell-details"><summary><span>Remission</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

<div id="enum-modal-yesnoenum" class="enum-modal" onclick="closeEnumModal('enum-modal-yesnoenum')">
<div class="enum-modal-content" onclick="event.stopPropagation()">
<button type="button" class="enum-modal-close" onclick="closeEnumModal('enum-modal-yesnoenum')">×</button>
<h3>YesNoEnum</h3>
<table class="model-table enum-table">
<thead><tr><th>Permissible Value</th><th>Description</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td class="enum-pv" title="Yes"><details class="cell-details"><summary><span>Yes</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="No"><details class="cell-details"><summary><span>No</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Unknown"><details class="cell-details"><summary><span>Unknown</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
<tr><td class="enum-pv" title="Not Reported"><details class="cell-details"><summary><span>Not Reported</span></summary></details></td><td class="enum-description" title=""><details class="cell-details"><summary><span></span></summary></details></td><td class="enum-meaning" title=""><span></span></td></tr>
</tbody>
</table>
</div>
</div>

</div>

</div>

<nav class="model-toc" aria-label="Model contents">
<a class="model-toc-domain" href="#domain-demographics">Demographics</a>
<a class="model-toc-class" data-subsets="" href="#class-subjectcharacteristics">SubjectCharacteristics</a>
<a class="model-toc-class" data-subsets="" href="#class-timing">Timing</a>
<a class="model-toc-class" data-subsets="" href="#class-familymedicalhistory">FamilyMedicalHistory</a>
<a class="model-toc-class" data-subsets="" href="#class-demographics">Demographics</a>
<a class="model-toc-class" data-subsets="" href="#class-medicalhistory">MedicalHistory</a>
<a class="model-toc-domain" href="#domain-testing">Testing</a>
<a class="model-toc-class" data-subsets="" href="#class-biometrics">Biometrics</a>
<a class="model-toc-class" data-subsets="" href="#class-biospecimen">Biospecimen</a>
<a class="model-toc-class" data-subsets="" href="#class-geneticanalysis">GeneticAnalysis</a>
<a class="model-toc-class" data-subsets="" href="#class-testing">Testing</a>
<a class="model-toc-domain" href="#domain-disease-attributes">Disease_Attributes</a>
<a class="model-toc-class" data-subsets="" href="#class-diseasecharacteristics">DiseaseCharacteristics</a>
<a class="model-toc-domain" href="#domain-intervention">Intervention</a>
<a class="model-toc-class" data-subsets="" href="#class-treatment">Treatment</a>
</nav>

<div id="raw-model-view" style="display:none;" markdown="1">

<div id="raw-loading" class="raw-loading" style="display:none;">Loading raw schema…</div>

<div id="raw-schema-renderer" class="json-renderer"></div>

</div>

<script id="view-metadata-payload" type="application/json">{"base": {"title": "base", "name": "base", "description": "This consensus data model was developed by an international group of monogenic diabetes experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Precision Diabetes Consortium (PREDICT). The model reflects the collective requirements of its contributors and provides a common framework for representing, harmonizing, and sharing monogenic diabetes data across research and clinical programs."}}</script>

<script id="raw-schema-payload" type="application/json">{"base": {"id": "https://models.d4cg.org/predict", "name": "predict", "title": "PREDICT Data Model", "license": "CC BY-NC 4.0", "version": 1.0, "prefixes": {"predict": "https://models.d4cg.org/predict", "linkml": "https://w3id.org/linkml/", "ncit": "http://purl.obolibrary.org/obo/NCIT_"}, "default_prefix": "predict", "default_range": "string", "imports": ["linkml:types"], "subsets": {"base": {"description": "This consensus data model was developed by an international group of monogenic diabetes experts and maintained by Data for the Common Good (D4CG) at the University of Chicago in collaboration with the Precision Diabetes Consortium (PREDICT). The model reflects the collective requirements of its contributors and provides a common framework for representing, harmonizing, and sharing monogenic diabetes data across research and clinical programs."}}, "classes": {"SubjectCharacteristics": {"description": "SubjectCharacteristics captures core subject-level identifiers, data source context, and last-known survival/contact status needed to anchor all other records in the model.", "slots": ["honest_broker_subject_id", "data_contributor_id", "data_source", "last_known_survival_status", "age_last_contact", "age_last_contact_unit", "age_last_contact_precision"], "comments": ["D4CGNote: One row per subject."], "annotations": {"domain": "demographics"}}, "Timing": {"description": "Timing represents named clinical or research timepoints and their associated ages, providing the longitudinal structure used to align observations across the model.", "slots": ["honest_broker_subject_id", "subject_characteristics", "timepoint", "timing_age_at", "age_unit", "age_precision"], "comments": ["D4CGNote: One row per subject per timepoint."], "annotations": {"domain": "demographics"}}, "FamilyMedicalHistory": {"description": "FamilyMedicalHistory captures diabetes-related conditions reported among relatives, supporting representation of inherited patterns and familial disease context.", "slots": ["honest_broker_subject_id", "subject_characteristics", "relation_honest_broker_subject_id", "relation", "condition", "source"], "comments": ["D4CGNote: One row per subject per relation per condition.", "(md_v1.3) ConsortiumNote: Only enter family members who have a history of dysglycemia."], "annotations": {"domain": "demographics"}}, "Demographics": {"description": "Demographics captures subject-level sex, race, and ethnicity information used to describe study populations and support cohort characterization.", "slots": ["honest_broker_subject_id", "subject_characteristics", "sex", "ethnicity", "race"], "comments": ["D4CGNote: One row per subject."], "annotations": {"domain": "demographics"}}, "MedicalHistory": {"description": "MedicalHistory records prior or co-occurring medical conditions for a subject, including coded condition details when available.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at", "age_unit", "age_precision", "medical_history_condition", "condition_other", "condition_code", "code_system"], "comments": ["D4CGNote: One row per subject per condition."], "annotations": {"domain": "demographics"}}, "Biometrics": {"description": "Biometrics captures anthropometric measurements such as height, weight, BMI, and related standardized scores used to characterize growth and body size over time.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at", "age_unit", "age_precision", "measurement_type", "measurement_numeric", "measurement_unit", "z_score"], "comments": ["D4CGNote: One row per subject per biometric measurement."], "annotations": {"domain": "testing"}}, "Biospecimen": {"description": "Biospecimen records available subject specimens by sample type, supporting linkage between clinical data and biological materials for research use.", "slots": ["honest_broker_subject_id", "subject_characteristics", "sample_type"], "comments": ["D4CGNote: One row per subject per sample type."], "annotations": {"domain": "testing"}}, "GeneticAnalysis": {"description": "GeneticAnalysis captures genetic testing results, including methods, genes, alteration details, HGVS nomenclature, reported significance, allelic state, and related external references.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at", "age_unit", "age_precision", "causative_alteration", "status", "genetic_analysis_sample_type", "laboratory_name", "cytogenetic_location", "method", "gene", "alteration_type", "alteration_effect", "alteration_region", "hgvs_accession", "hgvs_coding", "hgvs_protein", "hgvs_genomic", "iscn", "reported_significance", "allelic_state", "maf_numeric", "mosaicism", "external_ref_id", "external_ref_id_system"], "comments": ["D4CGNote: One row per subject per method per gene."], "annotations": {"domain": "testing"}}, "Testing": {"description": "Testing captures laboratory, glucose-monitoring, and related clinical test results, including numeric values, units, interpretation, fasting status, and timepoint-specific testing context.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at", "age_unit", "age_precision", "test_type", "testing_method", "testing_measurement_type", "result_modifier", "result_numeric", "result_unit", "reference_range", "result_interpretation", "fasting_status", "post_glucose_timepoint", "post_glucose_timepoint_unit"], "comments": ["D4CGNote: One row per subject per test type per result."], "annotations": {"domain": "testing"}}, "DiseaseCharacteristics": {"description": "DiseaseCharacteristics records monogenic diabetes-related disease features, including diabetes status, hypoglycemia, ketoacidosis, glucose range metrics, diet, and exercise observations.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at", "age_unit", "age_precision", "diabetes_status", "hypoglycemia_frequency", "severe_hypoglycemia_frequency", "dka", "time_in_range", "cgm_range", "diet", "exercise"], "comments": ["D4CGNote: One row per subject per observation."], "annotations": {"domain": "disease_attributes"}}, "Treatment": {"description": "Treatment captures diabetes-related medications and therapies, including medication class, name, dose, unit, route, frequency, timing, and reason for stopping treatment.", "slots": ["honest_broker_subject_id", "subject_characteristics", "age_at_start", "age_at_stop", "age_unit", "age_precision", "reason_stop", "dm_medication_class", "medication_class_other", "medication_name", "medication_code", "medication_concentration", "medication_dose", "medication_unit", "frequency", "route"], "comments": ["D4CGNote: One row per subject per medication class."], "annotations": {"domain": "intervention"}}}, "slots": {"honest_broker_subject_id": {"slot_uri": "", "range": "string", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "data_contributor_id": {"slot_uri": "", "range": "DataContributorIDEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "data_source": {"slot_uri": "", "range": "DataSourceEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "last_known_survival_status": {"slot_uri": "", "range": "LastKnownSurvivalStatusEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "age_last_contact": {"slot_uri": "", "range": "decimal", "comments": ["(md_v1.3) ConsortiumNote: Only applicable for survey source data"], "annotations": {"tier_priority": "md_v1.3"}}, "age_last_contact_unit": {"slot_uri": "", "range": "AgeLastContactUnitEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "age_last_contact_precision": {"slot_uri": "", "range": "AgeLastContactPrecisionEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "subject_characteristics": {"slot_uri": "", "range": "SubjectCharacteristics", "required": true, "multivalued": false}, "timepoint": {"slot_uri": "", "range": "TimepointEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "timing_age_at": {"slot_uri": "", "range": "integer", "required": true, "comments": ["(md_v1.3) ConsortiumNote: For reporting at the time of birth, report 0 day."], "annotations": {"tier_mandatory": "md_v1.3"}}, "age_at": {"slot_uri": "", "range": "integer", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "age_unit": {"slot_uri": "", "range": "AgeLastContactUnitEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "age_precision": {"slot_uri": "", "range": "AgeLastContactPrecisionEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "relation_honest_broker_subject_id": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "relation": {"slot_uri": "", "range": "RelationEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "condition": {"slot_uri": "", "range": "ConditionEnum", "comments": ["(md_v1.3) ConsortiumNotes: Only report diabetes-related conditions. Omit any other conditions from family members."], "annotations": {"tier_optional": "md_v1.3"}}, "source": {"slot_uri": "", "range": "SourceEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "sex": {"slot_uri": "", "range": "SexEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "ethnicity": {"slot_uri": "", "range": "EthnicityEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "race": {"slot_uri": "", "range": "RaceEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "medical_history_condition": {"slot_uri": "", "range": "MedicalHistoryConditionEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "condition_other": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "condition_code": {"slot_uri": "", "range": "string", "comments": ["(md_v1.3) ConsortiumNote: If you have a more specific form of a condition listed above, select the condition from the list and use this field to provide the more specific coded value. Do not use the 'Other' value."], "annotations": {"tier_optional": "md_v1.3"}}, "code_system": {"slot_uri": "", "range": "CodeSystemEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "measurement_type": {"slot_uri": "", "range": "MeasurementTypeEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "measurement_numeric": {"slot_uri": "", "range": "decimal", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "measurement_unit": {"slot_uri": "", "range": "MeasurementUnitEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "z_score": {"slot_uri": "", "range": "decimal", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "sample_type": {"slot_uri": "", "range": "SampleTypeEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "causative_alteration": {"slot_uri": "", "range": "YesNoEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "status": {"slot_uri": "", "range": "StatusEnum", "required": true, "comments": ["(md_v1.3) ConsortiumNote: Can use this field and select 'Absent' to indicate if a subject tested negative for a particular genetic variant."], "annotations": {"tier_mandatory": "md_v1.3"}}, "genetic_analysis_sample_type": {"slot_uri": "", "range": "GeneticAnalysisSampleTypeEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "laboratory_name": {"slot_uri": "", "range": "LaboratoryNameEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "cytogenetic_location": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "method": {"slot_uri": "", "range": "MethodEnum", "required": true, "comments": ["(md_v1.3) ConsortiumNote: For cases where confirmatory testing was performed, this field should be used to indicate the method of the initial test, not the confirmatory testing method."], "annotations": {"tier_mandatory": "md_v1.3"}}, "gene": {"slot_uri": "", "range": "GeneEnum", "comments": ["(md_v1.3) ConsortiumNote: Use this field for 'mtDNA' alteration."], "annotations": {"tier_optional": "md_v1.3"}}, "alteration_type": {"slot_uri": "", "range": "AlterationTypeEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "alteration_effect": {"slot_uri": "", "range": "AlterationEffectEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "alteration_region": {"slot_uri": "", "range": "AlterationRegionEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "hgvs_accession": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "hgvs_coding": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "hgvs_protein": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "hgvs_genomic": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "iscn": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "reported_significance": {"slot_uri": "", "range": "ReportedSignificanceEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "allelic_state": {"slot_uri": "", "range": "AllelicStateEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "maf_numeric": {"slot_uri": "", "range": "decimal", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "mosaicism": {"slot_uri": "", "range": "YesNoEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "external_ref_id": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "external_ref_id_system": {"slot_uri": "", "range": "ExternalRefIDSystemEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "test_type": {"slot_uri": "", "range": "TestTypeEnum", "comments": ["(md_v1.3) ConsortiumNote: Please report relevant labs at time points of dx, highest ever, most recent, and any other time periods you have bandwidth to report. For example, could report Blood Glucose value at time of dx, highest ever, and most recent. But do not necessarily need to report all values in the EMR."], "annotations": {"tier_priority": "md_v1.3"}}, "testing_method": {"slot_uri": "", "range": "TestingMethodEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "testing_measurement_type": {"slot_uri": "", "range": "TestingMeasurementTypeEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "result_modifier": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "result_numeric": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "result_unit": {"slot_uri": "", "range": "ResultUnitEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "reference_range": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "result_interpretation": {"slot_uri": "", "range": "ResultInterpretationEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "fasting_status": {"slot_uri": "", "range": "FastingStatusEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "post_glucose_timepoint": {"slot_uri": "", "range": "string", "comments": ["(md_v1.3) ConsortiumNote: Only use for glucose tolerance testing."], "annotations": {"tier_priority": "md_v1.3"}}, "post_glucose_timepoint_unit": {"slot_uri": "", "range": "PostGlucoseTimepointUnitEnum", "comments": ["(md_v1.3) ConsortiumNote: Only use for glucose tolerance testing."], "annotations": {"tier_priority": "md_v1.3"}}, "diabetes_status": {"slot_uri": "", "range": "DiabetesStatusEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "hypoglycemia_frequency": {"slot_uri": "", "range": "HypoglycemiaFrequencyEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "severe_hypoglycemia_frequency": {"slot_uri": "", "range": "HypoglycemiaFrequencyEnum", "comments": [], "annotations": {"tier_optional": "md_v1.3"}}, "dka": {"slot_uri": "", "range": "DKAEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "time_in_range": {"slot_uri": "", "range": "decimal", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "cgm_range": {"slot_uri": "", "range": "CGMRangeEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "diet": {"slot_uri": "", "range": "DiabetesStatusEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "exercise": {"slot_uri": "", "range": "DiabetesStatusEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "age_at_start": {"slot_uri": "", "range": "integer", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "age_at_stop": {"slot_uri": "", "range": "integer", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "reason_stop": {"slot_uri": "", "range": "ReasonStopEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "dm_medication_class": {"slot_uri": "", "range": "DMMedicationClassEnum", "required": true, "comments": [], "annotations": {"tier_mandatory": "md_v1.3"}}, "medication_class_other": {"slot_uri": "", "range": "MedicationClassOtherEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "medication_name": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "medication_code": {"slot_uri": "", "range": "string", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "medication_concentration": {"slot_uri": "", "range": "MedicationConcentrationEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "medication_dose": {"slot_uri": "", "range": "decimal", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "medication_unit": {"slot_uri": "", "range": "MedicationUnitEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "frequency": {"slot_uri": "", "range": "FrequencyEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}, "route": {"slot_uri": "", "range": "RouteEnum", "comments": [], "annotations": {"tier_priority": "md_v1.3"}}}, "enums": {"DataContributorIDEnum": {"permissible_values": {"UChicago Monogenic Diabetes Research Group": {"meaning": "", "comments": []}, "Barbara Davis Center / UColorado": {"meaning": "", "comments": []}, "Baylor": {"meaning": "", "comments": []}, "Boston Children's": {"meaning": "", "comments": []}, "Cincinnati Children's Hospital": {"meaning": "", "comments": []}, "Indiana": {"meaning": "", "comments": []}, "MGH": {"meaning": "", "comments": []}, "Maryland": {"meaning": "", "comments": []}, "Michigan": {"meaning": "", "comments": []}, "Nebraska": {"meaning": "", "comments": []}, "NorthShore": {"meaning": "", "comments": []}, "WashU": {"meaning": "", "comments": []}}}, "DataSourceEnum": {"permissible_values": {"Self-Reported": {"meaning": "", "comments": []}, "EHR": {"meaning": "", "comments": []}}}, "LastKnownSurvivalStatusEnum": {"permissible_values": {"Alive": {"meaning": "", "comments": []}, "Dead": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "AgeLastContactUnitEnum": {"permissible_values": {"Years": {"meaning": "", "comments": []}, "Months": {"meaning": "", "comments": []}, "Weeks": {"meaning": "", "comments": []}, "Days": {"meaning": "", "comments": []}}}, "AgeLastContactPrecisionEnum": {"permissible_values": {"Approximate": {"meaning": "", "comments": []}, "Exact": {"meaning": "", "comments": []}}}, "TimepointEnum": {"permissible_values": {"Prediabetes Diagnosis": {"meaning": "", "comments": []}, "Diagnosis": {"meaning": "", "comments": []}, "Relapse": {"meaning": "", "comments": []}, "Remission": {"meaning": "", "comments": []}}}, "RelationEnum": {"permissible_values": {"Father": {"meaning": "", "comments": []}, "Mother": {"meaning": "", "comments": []}, "Son": {"meaning": "", "comments": []}, "Daughter": {"meaning": "", "comments": []}, "Brother": {"meaning": "", "comments": []}, "Sister": {"meaning": "", "comments": []}, "Spouse/Partner": {"meaning": "", "comments": []}, "Grandfather (Paternal)": {"meaning": "", "comments": []}, "Grandfather (Maternal)": {"meaning": "", "comments": []}, "Grandmother (Paternal)": {"meaning": "", "comments": []}, "Grandmother (Maternal)": {"meaning": "", "comments": []}, "Uncle (Paternal)": {"meaning": "", "comments": []}, "Uncle (Maternal)": {"meaning": "", "comments": []}, "Aunt (Paternal)": {"meaning": "", "comments": []}, "Aunt (Maternal)": {"meaning": "", "comments": []}, "Niece": {"meaning": "", "comments": []}, "Nephew": {"meaning": "", "comments": []}, "First Cousin (Paternal)": {"meaning": "", "comments": []}, "First Cousin (Maternal)": {"meaning": "", "comments": []}, "First Cousin (Paternal/Maternal Unknown)": {"meaning": "", "comments": []}, "Great-Grandfather (Paternal)": {"meaning": "", "comments": []}, "Great-Grandfather (Maternal)": {"meaning": "", "comments": []}, "Great-Grandmother (Paternal)": {"meaning": "", "comments": []}, "Great-Grandmother (Maternal)": {"meaning": "", "comments": []}, "Great-Uncle (Paternal)": {"meaning": "", "comments": []}, "Great-Uncle (Maternal)": {"meaning": "", "comments": []}, "Great-Aunt (Paternal)": {"meaning": "", "comments": []}, "Great-Aunt (Maternal)": {"meaning": "", "comments": []}, "Other": {"meaning": "", "comments": []}}}, "ConditionEnum": {"permissible_values": {"Prediabetes": {"meaning": "", "comments": []}, "Type 1 Diabetes": {"meaning": "", "comments": []}, "Type 2 Diabetes": {"meaning": "", "comments": []}, "Monogenic Diabetes": {"meaning": "", "comments": []}, "Gestational Diabetes": {"meaning": "", "comments": {}}, "Diabetes, NOS": {"meaning": "", "comments": []}}}, "SourceEnum": {"permissible_values": {"Confirmed By Genetic Test": {"meaning": "", "comments": []}, "Clinical Diagnosis Only": {"meaning": "", "comments": []}}}, "SexEnum": {"permissible_values": {"Male": {"meaning": "", "comments": []}, "Female": {"meaning": "", "comments": []}, "Undifferentiated": {"meaning": "", "comments": []}}}, "EthnicityEnum": {"permissible_values": {"Hispanic or Latino": {"meaning": "", "comments": []}, "Not Hispanic or Latino": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "RaceEnum": {"permissible_values": {"American Indian or Alaska Native": {"meaning": "", "comments": []}, "Asian": {"meaning": "", "comments": []}, "Black or African American": {"meaning": "", "comments": []}, "Native Hawaiian or Other Pacific Islander": {"meaning": "", "comments": []}, "White": {"meaning": "", "comments": []}, "Multiracial": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "MedicalHistoryConditionEnum": {"permissible_values": {"Abnormal Kidney Shape, Size, Or Number": {"meaning": "", "comments": []}, "Absent Or Missing Pancreas": {"meaning": "", "comments": []}, "Behavioral Difficulties": {"meaning": "", "comments": []}, "Congenital Heart Defect": {"meaning": "", "comments": []}, "Coronary Artery Disease": {"meaning": "", "comments": []}, "Difficulty With Social Interactions": {"meaning": "", "comments": []}, "Elevated Liver Enzymes / Lfts": {"meaning": "", "comments": []}, "Fatty Liver": {"meaning": "", "comments": []}, "Genitourinary Developmental Malformation Or Abnormality": {"meaning": "", "comments": []}, "Gestational Diabetes": {"meaning": "", "comments": []}, "Hepatomegaly": {"meaning": "", "comments": []}, "High Cholesterol, NOS": {"meaning": "", "comments": []}, "High Frequency Hearing Loss": {"meaning": "", "comments": []}, "High LDL": {"meaning": "", "comments": []}, "High Total Cholesterol": {"meaning": "", "comments": []}, "High Triglycerides": {"meaning": "", "comments": []}, "Hypertension": {"meaning": "", "comments": []}, "Hypoglycemia In Infancy": {"meaning": "", "comments": []}, "Intrauterine Growth Restriction": {"meaning": "", "comments": []}, "Liver Adenoma": {"meaning": "", "comments": []}, "Low Frequency Hearing Loss": {"meaning": "", "comments": []}, "Low LDL": {"meaning": "", "comments": []}, "Macroglossia": {"meaning": "", "comments": []}, "Nephropathy": {"meaning": "", "comments": []}, "Peripheral Artery Disease": {"meaning": "", "comments": []}, "Peripheral Neuropathy": {"meaning": "", "comments": []}, "Polycystic Kidney Diseasea": {"meaning": "", "comments": []}, "Proteinuria": {"meaning": "", "comments": []}, "Renal CystL": {"meaning": "", "comments": []}, "Retinopathy": {"meaning": "", "comments": []}, "Small For Gestational Age": {"meaning": "", "comments": []}, "Small Pancreas": {"meaning": "", "comments": []}, "Stroke": {"meaning": "", "comments": []}, "Umbilical Hernia": {"meaning": "", "comments": []}, "Other": {"meaning": "", "comments": ["(md_v1.3) ConsortiumNote: Only select 'Other' if the condition is not related to the provided list (which are designated as 'of interest' by the PREDICT group)."]}}}, "CodeSystemEnum": {"permissible_values": {"CTCAE": {"meaning": "", "comments": []}, "ICD-9": {"meaning": "", "comments": []}, "ICD-10": {"meaning": "", "comments": []}, "SNOMED-CT": {"meaning": "", "comments": []}}}, "MeasurementTypeEnum": {"permissible_values": {"Height/Length": {"meaning": "", "comments": []}, "Weight": {"meaning": "", "comments": []}, "BMI": {"meaning": "", "comments": []}, "Raw BMI": {"meaning": "", "comments": []}}}, "MeasurementUnitEnum": {"permissible_values": {"kg": {"meaning": "", "comments": []}, "cm": {"meaning": "", "comments": []}, "kg/m^2": {"meaning": "", "comments": []}, "percentile": {"meaning": "", "comments": ["(md_v1.3) ConsortiumNote: Use percentile as a unit when reporting pediatric BMI."]}}}, "SampleTypeEnum": {"permissible_values": {"Saliva": {"meaning": "", "comments": []}, "Blood": {"meaning": "", "comments": []}, "DNA": {"meaning": "", "comments": []}, "Plasma": {"meaning": "", "comments": []}, "Serum": {"meaning": "", "comments": []}, "Urine": {"meaning": "", "comments": []}, "PBMC": {"meaning": "", "comments": []}}}, "YesNoEnum": {"permissible_values": {"Yes": {"meaning": "", "comments": []}, "No": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "StatusEnum": {"permissible_values": {"Present": {"meaning": "", "comments": []}, "Absent": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "GeneticAnalysisSampleTypeEnum": {"permissible_values": {"Saliva": {"meaning": "", "comments": []}, "Blood": {"meaning": "", "comments": []}, "Buccal": {"meaning": "", "comments": []}, "Urine": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "LaboratoryNameEnum": {"permissible_values": {"Ambry Genetics": {"meaning": "", "comments": []}, "Athena": {"meaning": "", "comments": []}, "Baylor Genetics": {"meaning": "", "comments": []}, "Blueprint": {"meaning": "", "comments": []}, "GeneDx": {"meaning": "", "comments": []}, "Invitae": {"meaning": "", "comments": []}, "LMG": {"meaning": "", "comments": []}, "Research Lab": {"meaning": "", "comments": []}, "Seattle Children's Hospital": {"meaning": "", "comments": []}, "UCGSL": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "MethodEnum": {"permissible_values": {"Karyotyping": {"meaning": "", "comments": []}, "Fluorescence In Situ Hybridization": {"meaning": "", "comments": []}, "RT-PCR": {"meaning": "", "comments": []}, "PCR": {"meaning": "", "comments": []}, "MLPA": {"meaning": "", "comments": []}, "Sequencing, Sanger, Capillary Electropheresis": {"meaning": "", "comments": []}, "Sequencing, Sanger, Gel Electropheresis": {"meaning": "", "comments": []}, "Sequencing, Sanger, NOS": {"meaning": "", "comments": []}, "Sequencing, NGS, Whole Genome": {"meaning": "", "comments": []}, "Sequencing, NGS, lcWGS": {"meaning": "", "comments": []}, "Sequencing, NGS, Whole Exome": {"meaning": "", "comments": []}, "Sequencing, NGS, Multi-Gene Panel": {"meaning": "", "comments": []}, "Sequencing, NGS, Single Site": {"meaning": "", "comments": []}, "Sequencing, NGS, Single Gene DNA": {"meaning": "", "comments": []}, "Sequencing, NGS, Targeted DNA": {"meaning": "", "comments": []}, "Sequencing, NGS, Targeted RNA": {"meaning": "", "comments": []}, "Sequencing, NGS, Total RNA": {"meaning": "", "comments": []}, "Sequencing, NGS, TDS": {"meaning": "", "comments": []}, "Sequencing, NGS, NOS": {"meaning": "", "comments": []}, "Sequencing, Methylation Array": {"meaning": "", "comments": []}, "Sequencing, Nanostring": {"meaning": "", "comments": []}, "SNP Array": {"meaning": "", "comments": []}, "Array CGH": {"meaning": "", "comments": []}, "Genotyping, NOS": {"meaning": "", "comments": []}, "Cytogenetics, NOS": {"meaning": "", "comments": []}, "Other": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "GeneEnum": {"permissible_values": {"6q24-Related Abnormalities": {"meaning": "", "comments": []}, "ABCC8": {"meaning": "", "comments": []}, "CEL": {"meaning": "", "comments": []}, "CFTR": {"meaning": "", "comments": []}, "DCAF17": {"meaning": "", "comments": []}, "EIF2AK3": {"meaning": "", "comments": []}, "FOXP3": {"meaning": "", "comments": []}, "GATA4": {"meaning": "", "comments": []}, "GATA6": {"meaning": "", "comments": []}, "GCK": {"meaning": "", "comments": []}, "GLIS3": {"meaning": "", "comments": []}, "HNF1A": {"meaning": "", "comments": []}, "HNF1B": {"meaning": "", "comments": []}, "HNF4A": {"meaning": "", "comments": []}, "IAPP (Amylin)": {"meaning": "", "comments": []}, "IER3IP1": {"meaning": "", "comments": []}, "IGF2/Russell Silver Syndrome": {"meaning": "", "comments": []}, "IL2RA": {"meaning": "", "comments": []}, "INS": {"meaning": "", "comments": []}, "INSR": {"meaning": "", "comments": []}, "KCNJ11": {"meaning": "", "comments": []}, "LRBA": {"meaning": "", "comments": []}, "mtDNA": {"meaning": "", "comments": []}, "NEUROD1": {"meaning": "", "comments": []}, "PAX4": {"meaning": "", "comments": []}, "PCBD1": {"meaning": "", "comments": []}, "PDX1 (IPF1)": {"meaning": "", "comments": []}, "PTF1A": {"meaning": "", "comments": []}, "RFX6": {"meaning": "", "comments": []}, "STAT3": {"meaning": "", "comments": []}, "WFS1": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "AlterationTypeEnum": {"permissible_values": {"Chromosome Arm Gain": {"meaning": "", "comments": []}, "Chromosome Arm Loss": {"meaning": "", "comments": []}, "Substitution": {"meaning": "", "comments": []}, "Deletion": {"meaning": "", "comments": []}, "Insertion": {"meaning": "", "comments": []}, "Indel": {"meaning": "", "comments": []}, "Duplication": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "AlterationEffectEnum": {"permissible_values": {"Frameshift": {"meaning": "", "comments": []}, "Missense": {"meaning": "", "comments": []}, "Stop Gain (Nonsense)": {"meaning": "", "comments": []}, "None (Inframe)": {"meaning": "", "comments": []}}}, "AlterationRegionEnum": {"permissible_values": {"Splice Site": {"meaning": "", "comments": []}, "5' UTR": {"meaning": "", "comments": []}, "3' UTR": {"meaning": "", "comments": []}}}, "ReportedSignificanceEnum": {"permissible_values": {"Pathogenic": {"meaning": "", "comments": []}, "Likely Pathogenic": {"meaning": "", "comments": []}, "Uncertain Significance": {"meaning": "", "comments": []}, "Likely Benign": {"meaning": "", "comments": []}, "Benign": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "AllelicStateEnum": {"permissible_values": {"Homozygous": {"meaning": "", "comments": []}, "Heterozygous": {"meaning": "", "comments": []}, "Compound Heterozygous": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}, "Not Reported": {"meaning": "", "comments": []}}}, "ExternalRefIDSystemEnum": {"permissible_values": {"ClinGen": {"meaning": "", "comments": []}, "ClinVar": {"meaning": "", "comments": []}}}, "TestTypeEnum": {"permissible_values": {"HbA1c": {"meaning": "", "comments": []}, "C-Peptide": {"meaning": "", "comments": []}, "Blood Glucose": {"meaning": "", "comments": []}, "Autoantibodies, GAD65": {"meaning": "", "comments": []}, "Autoantibodies, ZnT8": {"meaning": "", "comments": []}, "Autoantibodies, IA-2": {"meaning": "", "comments": []}, "Autoantibodies, Insulin": {"meaning": "", "comments": []}, "Autoantibodies, Islet Cell": {"meaning": "", "comments": []}, "Autoantibodies, NOS": {"meaning": "", "comments": []}, "Total Cholesterol": {"meaning": "", "comments": []}, "Triglycerides": {"meaning": "", "comments": []}, "HDL": {"meaning": "", "comments": []}, "LDL": {"meaning": "", "comments": []}, "Serum Magnesium": {"meaning": "", "comments": []}, "Serum Potassium": {"meaning": "", "comments": []}, "Serum Creatinine": {"meaning": "", "comments": []}, "Serum BUN": {"meaning": "", "comments": []}, "GFR": {"meaning": "", "comments": []}, "Urine Microalbumin": {"meaning": "", "comments": []}, "Urine Creatinine": {"meaning": "", "comments": []}, "Microalbumin/Creatinine Ratio": {"meaning": "", "comments": []}, "Urine MagnesiumSerum Potassium": {"meaning": "", "comments": []}, "ALT": {"meaning": "", "comments": []}, "AST": {"meaning": "", "comments": []}}}, "TestingMethodEnum": {"permissible_values": {"Continuous Glucose Monitoring": {"meaning": "", "comments": []}, "Laboratory Test": {"meaning": "", "comments": []}, "Home Glucose Test": {"meaning": "", "comments": []}}}, "TestingMeasurementTypeEnum": {"permissible_values": {"Average High": {"meaning": "", "comments": []}, "14-day Average": {"meaning": "", "comments": []}, "30-day Average": {"meaning": "", "comments": []}, "90-day Average": {"meaning": "", "comments": []}, "Average": {"meaning": "", "comments": []}, "Average Low": {"meaning": "", "comments": []}, "Point": {"meaning": "", "comments": []}}}, "ResultUnitEnum": {"permissible_values": {"%": {"meaning": "", "comments": []}, "mg/dL": {"meaning": "", "comments": []}, "U/L": {"meaning": "", "comments": []}, "U/mL": {"meaning": "", "comments": []}, "mmol/L": {"meaning": "", "comments": []}, "ng/mL": {"meaning": "", "comments": []}, "nmol/L": {"meaning": "", "comments": []}}}, "ResultInterpretationEnum": {"permissible_values": {"Positive": {"meaning": "", "comments": []}, "Negative": {"meaning": "", "comments": []}}}, "FastingStatusEnum": {"permissible_values": {"Fasting": {"meaning": "", "comments": []}, "Non-Fasting": {"meaning": "", "comments": []}, "Random": {"meaning": "", "comments": []}}}, "PostGlucoseTimepointUnitEnum": {"permissible_values": {"Minutes": {"meaning": "", "comments": []}}}, "DiabetesStatusEnum": {"permissible_values": {"Yes": {"meaning": "", "comments": []}, "No": {"meaning": "", "comments": []}}}, "HypoglycemiaFrequencyEnum": {"permissible_values": {"Once or twice in past year": {"meaning": "", "comments": []}, "Every few months": {"meaning": "", "comments": []}, "Once or twice a month": {"meaning": "", "comments": []}, "Once or twice a week": {"meaning": "", "comments": []}, "Daily or every other day": {"meaning": "", "comments": []}, "Never": {"meaning": "", "comments": []}}}, "DKAEnum": {"permissible_values": {"Yes - Hyperglycermic DKA": {"meaning": "", "comments": []}, "Yes - Euglycemic DKA": {"meaning": "", "comments": []}, "No": {"meaning": "", "comments": {}}}}, "CGMRangeEnum": {"permissible_values": {"Standard": {"meaning": "", "comments": []}, "Non-Standard": {"meaning": "", "comments": []}}}, "ReasonStopEnum": {"permissible_values": {"Planned Stop": {"meaning": "", "comments": []}, "No Significant Effect": {"meaning": "", "comments": []}, "Side Effects": {"meaning": "", "comments": []}, "No Insured": {"meaning": "", "comments": []}, "Cost": {"meaning": "", "comments": []}, "Unknown": {"meaning": "", "comments": []}}}, "DMMedicationClassEnum": {"permissible_values": {"Insulin, Rapid-Acting": {"meaning": "", "comments": []}, "Insulin, Long-Acting": {"meaning": "", "comments": []}, "Insulin, Intermediate-Acting": {"meaning": "", "comments": []}, "Insulin, Combination": {"meaning": "", "comments": []}, "Insulin, NOS": {"meaning": "", "comments": []}, "Biguanide": {"meaning": "", "comments": []}, "Sulfonylurea": {"meaning": "", "comments": []}, "Meglitinide": {"meaning": "", "comments": []}, "Thiazolidinedione": {"meaning": "", "comments": []}, "Dipeptidylpeptidase 4 Inhibitor": {"meaning": "", "comments": []}, "Sodium-Glucose Co-Transporter 2 Inhibitor": {"meaning": "", "comments": []}, "GLP-1 Receptor Agonist": {"meaning": "", "comments": []}, "Dual GLP-1/GIP Receptor Agonist": {"meaning": "", "comments": []}, "Amylin Analog": {"meaning": "", "comments": []}, "Alpha-Glucosidase Inhibitor": {"meaning": "", "comments": []}, "Bile Acid-Binding Resin": {"meaning": "", "comments": []}}}, "MedicationClassOtherEnum": {"permissible_values": {"ACE Inhibitor": {"meaning": "", "comments": []}, "ACL Inhibitor": {"meaning": "", "comments": []}, "Angiotensin II Receptor Blockers": {"meaning": "", "comments": []}, "ANGPTL3 Inhibitor": {"meaning": "", "comments": []}, "Antiepileptic": {"meaning": "", "comments": []}, "Antilipemic siRNA": {"meaning": "", "comments": []}, "Beta Blocker": {"meaning": "", "comments": []}, "Calcium Channel Blocker": {"meaning": "", "comments": []}, "Cholesterol Absorption Inhibitor": {"meaning": "", "comments": []}, "Coenzyme Q": {"meaning": "", "comments": []}, "Diuretic": {"meaning": "", "comments": []}, "Fibrates": {"meaning": "", "comments": []}, "Finerenone": {"meaning": "", "comments": []}, "Glucagon": {"meaning": "", "comments": []}, "Magnesium": {"meaning": "", "comments": []}, "Mineralcorticoid Receptor": {"meaning": "", "comments": []}, "Pancreatic Enzymes": {"meaning": "", "comments": []}, "Pcsk9 Inhibitor": {"meaning": "", "comments": []}, "Psychoactive": {"meaning": "", "comments": []}, "Statin": {"meaning": "", "comments": []}}}, "MedicationConcentrationEnum": {"permissible_values": {"U100": {"meaning": "", "comments": []}, "U200": {"meaning": "", "comments": []}, "U300": {"meaning": "", "comments": []}, "U500": {"meaning": "", "comments": []}, "Not Applicable": {"meaning": "", "comments": []}}}, "MedicationUnitEnum": {"permissible_values": {"Units": {"meaning": "", "comments": []}, "mg": {"meaning": "", "comments": []}, "mcg": {"meaning": "", "comments": []}, "gm": {"meaning": "", "comments": []}, "ml": {"meaning": "", "comments": []}, "tbsp": {"meaning": "", "comments": []}, "tsp": {"meaning": "", "comments": []}, "IU": {"meaning": "", "comments": []}, "puffs": {"meaning": "", "comments": []}, "Packets": {"meaning": "", "comments": []}, "mg/ml": {"meaning": "", "comments": []}, "application": {"meaning": "", "comments": []}}}, "FrequencyEnum": {"permissible_values": {"Once per day": {"meaning": "", "comments": []}, "Two times a day": {"meaning": "", "comments": []}, "Three times a day": {"meaning": "", "comments": []}, "Four times a day": {"meaning": "", "comments": []}, "As needed": {"meaning": "", "comments": []}, "Before every meal": {"meaning": "", "comments": []}, "Before meals and at bedtime": {"meaning": "", "comments": []}, "Every night at bedtime": {"meaning": "", "comments": []}, "Every week": {"meaning": "", "comments": []}}}, "RouteEnum": {"permissible_values": {"Oral": {"meaning": "", "comments": []}, "Nasally": {"meaning": "", "comments": []}, "Subcutaneous": {"meaning": "", "comments": []}, "IM": {"meaning": "", "comments": []}, "IV": {"meaning": "", "comments": []}}}}, "annotations": {"docs": {"domains": {"demographics": {"title": "Demographics", "description": "Demographics contains subject identity, enrollment, study participation, longitudinal episode structure, survival status, family and medical history, and other contextual information needed to interpret records across the model."}, "testing": {"title": "Testing", "description": "Testing contains laboratory, pathology, genomic, functional, anthropometric, and specimen-related observations used to characterize subjects, disease biology, eligibility, monitoring, and research sample availability."}, "disease_attributes": {"title": "Disease Attributes", "description": "Disease Attributes contains diagnostic, staging, anatomic, histologic, biologic, risk, extent-of-disease, and disease-site concepts used to characterize the subject's cancer or cancer-related condition."}, "intervention": {"title": "Intervention", "description": "Intervention contains treatment and procedure records, including surgery, medications, radiation therapy, transplantation, transfusion, cellular therapy, locoregional therapy, fertility preservation procedures, and protocol treatment modifications."}, "monitoring": {"title": "Monitoring", "description": "Monitoring contains response, residual disease, toxicity, late effects, subsequent neoplasms, reproductive outcomes, patient-reported outcomes, and other follow-up concepts used to evaluate disease course and treatment impact over time."}}}}}}</script>