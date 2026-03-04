---
title: Lab 3 Instructions - Medical EDA, CI, and p-values
layout: default
---

<div class="lab-instructions-page">

<section id="lab-header" class="lab-hero">
<h1>Lab 3: Medical EDA with Confidence Intervals and p-values</h1>
<p class="lab-subtitle">Load and clean medical data, run descriptive analysis, segment with PivotTables, and practice CI/p-value interpretation in Excel.</p>
</section>

<section id="excel-only" class="lab-section">
## Important: Excel vs Google Sheets

This lab is designed for **Microsoft Excel**. You may use formulas in both tools, but menu paths for **Power Query**, **PivotTables**, and some statistical options are Excel-specific.

---

</section>

<section id="dataset-overview" class="lab-section">
## Dataset Overview

### Introduction

This lab uses a synthetic **Medical EDA** dataset (patient-level records) created for Week 5 content:

- Descriptive statistics
- Summary tables
- Data segmentation
- PivotTables
- Introductory confidence intervals (95% CI) and p-values

### Dataset Files

1. **Google Drive (recommended):** [**Lab 2/3 Dataset Folder**](https://drive.google.com/drive/folders/1F92S9FEN5SWvUQsEXIs9c1J4q90uARCm?usp=sharing)
2. **Course website (alternative):**
   - [**Medical-EDA.csv**]({{ site.baseurl }}/datasets/files/Medical-EDA.csv)
   - [**Medical-EDA.xlsx**]({{ site.baseurl }}/datasets/files/Medical-EDA.xlsx)
3. **Student package:** `student desk/Lab-3-Dataset/` (if provided)

### Variables

| Column | Type | Description |
|--------|------|-------------|
| PatientID | Text | Unique patient ID |
| VisitDate | Date/Text | Visit date (some rows need type fixes) |
| Age | Number | Age in years |
| Sex | Text | Female/Male |
| Region | Text | North/South/East/West (inconsistent spacing/case in some rows) |
| HospitalUnit | Text | Clinical unit |
| DiagnosisGroup | Text | Hypertension/Diabetes/Respiratory (inconsistent case in some rows) |
| TreatmentGroup | Text | A/B (some lowercase values) |
| BaselineSBP | Number | Baseline systolic blood pressure |
| FollowupSBP | Number | Follow-up systolic blood pressure |
| LDL | Number/Text | LDL cholesterol (mixed numeric/text in some rows) |
| HbA1c | Number | Glycemic marker (some missing values) |
| BMI | Number | Body Mass Index |
| AdherenceScore | Number/Text | Medication adherence score (mixed numeric/text in some rows) |
| LengthOfStay | Number | Days in hospital |
| Readmission30d | Binary (0/1) | 30-day readmission indicator |
| Notes | Text | Optional notes |

### Data Quality Notes

- Duplicate records
- Blank rows
- Mixed text/number types (LDL, AdherenceScore)
- Inconsistent category formatting (Region, DiagnosisGroup, TreatmentGroup)
- Missing values (Region, HbA1c)
- Outliers (BMI, LengthOfStay)

### Learning Objectives

By the end of this lab, you can:

- Import and clean medical data in Excel
- Produce descriptive statistics and segmented summaries
- Build PivotTables for subgroup analysis
- Compute and interpret 95% CIs
- Compute and interpret p-values for simple comparisons

---

</section>

<section id="quick-reference" class="lab-section">
## Quick Reference (Week 5 Skills)

- Import: `Data -> Get Data -> From File -> From Text/CSV` or `From Excel Workbook`
- Open query again: `Data -> Queries & Connections -> Right-click query -> Edit`
- PivotTable: `Insert -> PivotTable`
- Pivot grouping: right-click date/number field -> Group
- Pivot filters: Report Filter and optional Slicer
- Pivot design: Subtotals, Grand Totals, Report Layout
- Pivot calculated field: PivotTable Analyze -> Fields, Items, & Sets -> Calculated Field
- Refresh: `Data -> Refresh All`
- 95% CI formula: `mean +/- t* * (SD / sqrt(n))`
- Two-sample p-value: `=T.TEST(rangeA, rangeB, 2, 3)`
- Categorical p-value (optional): `=CHISQ.TEST(actual_range, expected_range)`

---

</section>

<section id="exercises" class="lab-section">
## Lab Exercises

<section id="part-a" class="exercise-section">
<h3>Part A: Load and Clean</h3>

### Exercise A1: Import and Inspect
**Question:** Import `Medical-EDA.csv` (or `.xlsx`) and identify at least 4 quality issues.

**Instructions:**
1. Import with **Transform Data**.
2. Inspect data types and scan columns for missing values and inconsistent categories.
3. Record at least 4 issues found.

**Answer:** Typical issues: duplicate rows, blank rows, mixed text/number in `LDL` and `AdherenceScore`, inconsistent `Region/DiagnosisGroup/TreatmentGroup`, missing `Region/HbA1c`, and outliers in `BMI/LengthOfStay`.

---

### Exercise A2: Clean Core Columns
**Question:** Clean data so all key columns are analysis-ready.

**Instructions:**
1. Remove fully blank rows.
2. Remove duplicates (all columns).
3. Trim text columns: `Region`, `DiagnosisGroup`, `TreatmentGroup`.
4. Replace category variants (e.g., `a` -> `A`, `b` -> `B`, uppercase/lowercase diagnosis labels -> standard labels).
5. Set data types:
   - `VisitDate` -> Date
   - `Age`, `BaselineSBP`, `FollowupSBP`, `LDL`, `HbA1c`, `BMI`, `AdherenceScore`, `LengthOfStay` -> Number
   - `Readmission30d` -> Whole Number

**Answer:** A clean table should have standardized categories, valid types, and no blank/duplicate rows.

---

</section>

<section id="part-b" class="exercise-section">
<h3>Part B: Descriptive Statistics</h3>

### Exercise B1: Overall Summary
**Question:** Build a summary table for `BaselineSBP`, `FollowupSBP`, `LDL`, and `BMI`.

**Instructions:**
1. On a new sheet, create a table with metrics: Mean, Median, SD, Min, Max, N.
2. Use formulas such as:
   - `AVERAGE(range)`
   - `MEDIAN(range)`
   - `STDEV.S(range)`
   - `MIN(range)`, `MAX(range)`
   - `COUNT(range)`

**Answer:** Your summary should show lower average `FollowupSBP` than `BaselineSBP` and plausible central values for LDL/BMI after cleaning.

---

### Exercise B2: Segment by Treatment
**Question:** Compare `FollowupSBP` and `LengthOfStay` between Treatment A and B.

**Instructions:**
1. Use `AVERAGEIFS` (or PivotTable) to compute mean by treatment.
2. Report group means side-by-side.

**Answer:** In this synthetic dataset, Treatment A typically has lower follow-up SBP and shorter stay on average than Treatment B.

---

</section>

<section id="part-c" class="exercise-section">
<h3>Part C: Summary Tables and Segmentation</h3>

### Exercise C1: COUNTIFS and AVERAGEIFS
**Question:** Create a segmented summary by Region and DiagnosisGroup.

**Instructions:**
1. Build a small matrix of counts: `COUNTIFS(Region, r, DiagnosisGroup, d)`.
2. Build another matrix of means: `AVERAGEIFS(FollowupSBP, Region, r, DiagnosisGroup, d)`.

**Answer:** You should obtain subgroup-level counts and mean follow-up SBP values suitable for EDA interpretation.

---

### Exercise C2: Readmission Segmentation
**Question:** Compare readmission rates by TreatmentGroup and Sex.

**Instructions:**
1. Compute subgroup readmission rate: `AVERAGEIFS(Readmission30d, TreatmentGroup, g, Sex, s)`.
2. Convert to percent format.

**Answer:** Readmission percentages are expected to differ by treatment group; record subgroup differences.

---

</section>

<section id="part-d" class="exercise-section">
<h3>Part D: PivotTables</h3>

### Exercise D1: PivotTable 1 (Clinical Outcome by Treatment)
**Question:** Summarize `FollowupSBP` and `LengthOfStay` by `TreatmentGroup`.

**Instructions:**
1. Insert PivotTable from clean table.
2. Rows: `TreatmentGroup`
3. Values: Average of `FollowupSBP`, Average of `LengthOfStay`

**Answer:** PivotTable should clearly compare treatment outcomes.

---

### Exercise D2: PivotTable 2 (Readmission by Region and Diagnosis)
**Question:** Build a segmented PivotTable for readmission.

**Instructions:**
1. Rows: `Region`
2. Columns: `DiagnosisGroup`
3. Values: Average of `Readmission30d` (format as %)
4. Optional Filter: `Sex`

**Answer:** You should identify combinations with relatively higher readmission rates.

---

### Exercise D3: PivotTable 3 (Time Grouping by Month/Quarter)
**Question:** Group patient visits by month/quarter and summarize average follow-up SBP.

**Instructions:**
1. Create a new PivotTable from the clean table.
2. Rows: `VisitDate`
3. Values: Average of `FollowupSBP`
4. Right-click any date in the PivotTable -> **Group** -> select `Months` (and optionally `Quarters`).
5. Add `TreatmentGroup` to Filters to compare A vs B after grouping.

**Answer:** You should see monthly/quarterly trends in follow-up SBP and be able to compare trends by treatment using filters.

---

### Exercise D4: Pivot Layout, Filters, and Slicers
**Question:** Improve readability and interactivity of a PivotTable.

**Instructions:**
1. Start from PivotTable 1 or 2.
2. Turn on/off **Subtotals** and **Grand Totals** (PivotTable Design tab).
3. Change **Report Layout** (Compact/Outline/Tabular) and choose the clearest format.
4. Add at least one report filter (e.g., `Sex` or `HospitalUnit`).
5. Optional: Insert a **Slicer** for `TreatmentGroup` and test interactive filtering.

**Answer:** A good Pivot report is readable, consistently formatted, and easy to explore with filters/slicers.

---

### Exercise D5 (optional): Calculated Field in PivotTable
**Question:** Add a calculated field for SBP improvement (`BaselineSBP - FollowupSBP`) in a PivotTable.

**Instructions:**
1. Open a PivotTable built from the cleaned data.
2. PivotTable Analyze -> **Fields, Items, & Sets** -> **Calculated Field**.
3. Name: `SBP_Improvement`.
4. Formula: `=BaselineSBP - FollowupSBP`
5. Add `TreatmentGroup` as Rows and summarize average `SBP_Improvement`.

**Answer:** Positive values indicate reduction from baseline to follow-up. Compare mean improvement by treatment group.

---

</section>

<section id="part-e" class="exercise-section">
<h3>Part E: Confidence Intervals and p-values</h3>

### Exercise E1: 95% CI for Mean FollowupSBP (Overall)
**Question:** Calculate the 95% CI for mean `FollowupSBP`.

**Instructions:**
1. Compute:
   - `mean = AVERAGE(range)`
   - `sd = STDEV.S(range)`
   - `n = COUNT(range)`
2. Compute t critical:
   - `t_star = T.INV.2T(0.05, n-1)`
3. Margin of error:
   - `ME = t_star * sd / SQRT(n)`
4. CI bounds:
   - `Lower = mean - ME`
   - `Upper = mean + ME`

**Answer:** Report CI as `[Lower, Upper]`. Interpretation: we are 95% confident the population mean follow-up SBP lies in this interval.

---

### Exercise E2: 95% CI by Treatment Group
**Question:** Compute separate 95% CIs for Treatment A and B (FollowupSBP).

**Instructions:**
1. Filter or reference each treatment group separately.
2. Repeat E1 formulas for each group.
3. Compare intervals qualitatively (overlap vs separation).

**Answer:** Treatment A and B should show different interval centers; discuss whether separation appears meaningful.

---

### Exercise E3: p-value for Difference in Means (Treatment A vs B)
**Question:** Is `FollowupSBP` different between Treatment A and B?

**Instructions:**
1. Put group ranges in two columns (A and B).
2. Use:
   - `=T.TEST(rangeA, rangeB, 2, 3)`
   - `2` = two-tailed, `3` = unequal variances (Welch)
3. Decision rule:
   - If `p < 0.05`, reject equal-means null hypothesis.

**Answer:** Report p-value and decision. Example interpretation: “p < 0.05 suggests a statistically significant difference in mean follow-up SBP between treatment groups.”

---

### Exercise E4 (optional): p-value for Categorical Association
**Question:** Is 30-day readmission associated with TreatmentGroup?

**Instructions:**
1. Build a 2x2 observed table (`TreatmentGroup` x `Readmission30d`) using `COUNTIFS` or PivotTable.
2. Build expected counts table.
3. Use `CHISQ.TEST(observed_range, expected_range)`.

**Answer:** Report p-value and interpretation at alpha = 0.05.

---

</section>

<section id="part-f" class="exercise-section">
<h3>Part F: Short Interpretation</h3>

### Exercise F1: Mini report paragraph
**Question:** Write 5-8 sentences summarizing findings.

**Instructions:**
Include:
1. One descriptive-statistics insight
2. One segmentation/PivotTable insight
3. One CI statement
4. One p-value statement
5. One practical implication for healthcare decision-making

**Answer:** A strong response clearly distinguishes descriptive findings from inferential findings and states both statistical and practical meaning.

---

</section>
</section>

<section id="verification" class="lab-section">
## Verification Checklist

- [ ] Cleaned dataset loaded in Excel
- [ ] Descriptive statistics table completed
- [ ] At least 2 segmented summary tables completed
- [ ] At least 3 PivotTables completed (including one grouped by month/quarter)
- [ ] At least one Pivot filter (or slicer) used
- [ ] Optional calculated field tested (`SBP_Improvement`)
- [ ] 95% CI computed correctly (overall and by treatment)
- [ ] p-value test completed and interpreted correctly
- [ ] Mini report paragraph completed

---

</section>

<section id="troubleshooting" class="lab-section">
## Common Errors and Fixes

- **Numbers treated as text**
  - Fix with data type conversion in Power Query or `VALUE()` in Excel.
- **Date not recognized**
  - Check locale and source format; re-parse date column.
- **T.TEST returns error**
  - Ensure both ranges are numeric and contain no text blanks.
- **CHISQ.TEST error**
  - Observed and expected ranges must have same shape and non-zero expected counts.

---

</section>

<section id="conclusion" class="lab-section">
## Conclusion

You practiced the full Week 5 EDA workflow on medical data:

- Load and clean
- Descriptive and segmented summaries
- PivotTables
- Confidence intervals and p-values

These outputs feed directly into Group Progress Report 3 and prepare you for later visualization and statistical-analysis weeks.

</section>

</div>
