---
title: Healthcare Costs & Utilization Analysis Dataset Instructions
layout: default
---

# Healthcare Costs & Utilization Analysis Dataset Instructions

## Dataset Overview

This dataset contains healthcare cost and utilization data including patient demographics, medical conditions, treatment types, costs, length of stay, and provider information. The dataset is rich in categorical and numerical variables, making it ideal for segmentation analysis and comparative visualizations.

## Variables Description

### Patient Demographics
- **patient_id**: Unique identifier for each patient (1-3000)
- **age**: Patient age in years (18-90)
- **gender**: Patient gender (Male, Female)
- **region**: Geographic region (North, South, East, West, Central)

### Insurance & Financial
- **insurance_type**: Insurance coverage type (Private, Medicare, Medicaid, Self-pay)
- **total_cost**: Total healthcare cost in USD (decimal)
- **insurance_payment**: Amount paid by insurance in USD (decimal)
- **patient_payment**: Amount paid by patient in USD (decimal)
- **cost_per_visit**: Average cost per visit in USD (decimal)

### Medical Information
- **diagnosis**: Primary diagnosis (Diabetes, Hypertension, Heart Disease, Respiratory, Orthopedic, Cancer, Mental Health, Other)
- **treatment_type**: Type of treatment received (Medication, Surgery, Therapy, Emergency, Outpatient, Rehabilitation)
- **provider_type**: Healthcare provider type (Hospital, Clinic, Specialist, Emergency Room)

### Utilization Metrics
- **length_of_stay**: Length of hospital stay in days (1-30)
- **number_of_visits**: Number of healthcare visits (1-15)
- **readmission_30days**: Readmission within 30 days (1=yes, 0=no)

### Time Information
- **admission_year**: Year of admission (2021, 2022, 2023)
- **admission_month**: Month of admission (1-12)

## Use Cases

This dataset is suitable for:
- Analyzing healthcare costs across different patient demographics
- Comparing utilization rates by medical condition and treatment type
- Identifying cost drivers and high-cost patient segments
- Creating comparative visualizations of cost patterns
- Building interactive dashboards for cost exploration
- Segmenting patients by cost categories and utilization patterns
- Analyzing readmission rates and their relationship to costs

## Excel Analysis Tips

- Use PivotTables to summarize costs by diagnosis, region, or treatment type
- Create comparative bar charts showing costs across different groups
- Use SUMIFS, COUNTIFS, AVERAGEIFS for conditional cost analysis
- Build interactive dashboards with slicers for filtering by multiple dimensions
- Create cost heat maps by region and diagnosis
- Analyze cost trends over time using admission year and month
- Segment patients into cost categories (low, medium, high) for analysis
- Compare readmission rates and their impact on costs
