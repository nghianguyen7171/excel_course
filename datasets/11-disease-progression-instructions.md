---
title: Disease Progression & Treatment Outcomes Dataset Instructions
layout: default
---

# Disease Progression & Treatment Outcomes Dataset Instructions

## Dataset Overview

This dataset contains clinical data from patients with a chronic disease, including baseline characteristics, treatment information, clinical measurements over time, and disease progression outcomes. The dataset contains multiple time points (longitudinal data), making it suitable for longitudinal analysis and statistical modeling.

## Dataset Structure

The dataset is organized in two sheets:

### Sheet 1: Longitudinal_Data
Contains repeated measurements for each patient across multiple visits (baseline, 3 months, 6 months, 12 months).

### Sheet 2: Patient_Summary
Contains one record per patient with baseline characteristics and final outcomes.

## Variables Description (Longitudinal_Data)

### Identification
- **patient_id**: Unique identifier for each patient (1-800)
- **visit_id**: Unique identifier for each visit (patient_id_V0, V1, V2, V3)
- **visit_month**: Months from baseline (0, 3, 6, 12)

### Patient Characteristics (constant across visits)
- **age**: Patient age in years (30-80)
- **gender**: Patient gender (Male, Female)
- **bmi**: Body Mass Index (18-45)
- **has_diabetes**: Diabetes comorbidity (1=yes, 0=no)
- **has_hypertension**: Hypertension comorbidity (1=yes, 0=no)

### Treatment Information
- **treatment_type**: Treatment assignment (Treatment A, Treatment B, Placebo)

### Disease Progression Variables
- **disease_severity**: Disease severity score (0-100, higher = more severe)
- **severity_change**: Change in severity from baseline (can be negative for improvement)
- **lab_value_1**: Clinical biomarker value (continuous)
- **lab_value_2**: Another clinical biomarker value (continuous)
- **treatment_response**: Treatment response indicator (1=improved, 0=stable/worsened)
- **adverse_event**: Adverse event occurrence (1=yes, 0=no)

## Variables Description (Patient_Summary)

### Patient Baseline Characteristics
- **patient_id**: Unique identifier
- **age**: Patient age in years
- **gender**: Patient gender
- **bmi**: Body Mass Index
- **has_diabetes**: Diabetes comorbidity
- **has_hypertension**: Hypertension comorbidity
- **treatment_type**: Treatment assignment
- **baseline_severity**: Disease severity at baseline (0-100)

### Outcome Variables
- **final_severity**: Disease severity at 12 months (0-100)
- **time_to_improvement**: Months until first improvement (3, 6, 12, or censored)
- **improved**: Improvement indicator (1=improved, 0=not improved)
- **censored**: Censoring indicator for time-to-improvement (1=censored, 0=event occurred)

## Use Cases

This dataset is suitable for:
- Exploring relationships between patient characteristics and disease outcomes
- Performing correlation analysis to identify associations with disease progression
- Building regression models to predict treatment outcomes
- Comparing treatment effectiveness across different patient groups
- Testing statistical hypotheses about relationships between variables
- Analyzing time-to-event outcomes (disease progression, treatment response)
- Conducting longitudinal analysis of disease severity over time
- Identifying prognostic factors for patient outcomes

## Excel Analysis Tips

- Use PivotTables to summarize disease severity by treatment group and visit month
- Create line charts showing disease progression over time for different treatment groups
- Use CORREL function to calculate correlations between variables
- Build regression models using Data Analysis ToolPak
- Use t-tests or ANOVA to compare treatment groups
- Analyze time-to-improvement using survival analysis techniques
- Create scatter plots to visualize relationships between baseline characteristics and outcomes
- Use conditional formulas to calculate improvement rates by group
- Compare lab values across treatment groups and time points
