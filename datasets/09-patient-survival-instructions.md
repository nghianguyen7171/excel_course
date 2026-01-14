---
title: Patient Survival Analysis Dataset Instructions
layout: default
---

# Patient Survival Analysis Dataset Instructions (GBSG2)

## Dataset Overview

This dataset is based on the German Breast Cancer Study Group 2 (GBSG2) dataset, containing information on 686 patients with primary node-positive breast cancer. The dataset includes survival times, event indicators, and various prognostic factors for survival analysis.

## Variables Description

### Survival Analysis Variables
- **time**: Survival time in days (integer)
- **status**: Event indicator (1 = death/recurrence, 0 = censored/alive)

### Patient Characteristics
- **age**: Patient age in years (integer, typically 25-80)
- **menostat**: Menopausal status (Pre, Post)

### Treatment Information
- **horTh**: Hormonal therapy (yes, no)

### Clinical Variables
- **tsize**: Tumor size in mm (integer, typically 5-60)
- **tgrade**: Tumor grade (1, 2, 3)
  - 1 = Well differentiated (low grade)
  - 2 = Moderately differentiated (intermediate grade)
  - 3 = Poorly differentiated (high grade)
- **pnodes**: Number of positive nodes (integer, 0-20)
- **progrec**: Progesterone receptor level (integer, 0-200)
- **estrec**: Estrogen receptor level (integer, 0-200)

## Survival Analysis Notes

- **Event**: Death or recurrence (status = 1)
- **Time**: Days from diagnosis/treatment to event or censoring
- **Censoring**: Patients still alive or lost to follow-up (status = 0)
- **Censored observations**: Patients who did not experience the event during the observation period

## Data Quality

- No missing values
- All variables are properly formatted
- Time-to-event data is complete and valid
- Event indicators are binary (0/1)

## Use Cases

This dataset is suitable for:
- Calculating survival probabilities over time
- Comparing survival across treatment groups (hormonal therapy)
- Identifying prognostic factors (age, tumor characteristics)
- Creating survival curves for different patient groups
- Analyzing the impact of clinical variables on patient outcomes

## Excel Analysis Tips

- Use PivotTables to calculate survival probabilities by time periods
- Create charts to visualize survival curves
- Compare survival between treatment groups (horTh: yes vs no)
- Analyze survival by tumor grade, size, or node status
- Use conditional formulas to segment patients by characteristics
- Create comparative visualizations showing survival differences

## Medical Context

This dataset represents real-world survival analysis in oncology, where understanding patient prognosis and treatment effectiveness is critical for clinical decision-making.
