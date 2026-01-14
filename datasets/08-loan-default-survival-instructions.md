---
title: Loan Default Survival Analysis Dataset Instructions
layout: default
---

# Loan Default Survival Analysis Dataset Instructions

## Dataset Overview

This dataset contains loan information with time-to-event data for survival analysis. The dataset includes 5,000 loans with information about borrowers, loan characteristics, and survival outcomes (default or censored).

## Variables Description

### Identification
- **loan_id**: Unique identifier for each loan (1-5000)

### Loan Characteristics
- **loan_amount**: Loan amount in USD (integer)
- **interest_rate**: Annual interest rate percentage (decimal)
- **term_months**: Loan term in months (36 or 60)
- **loan_grade**: Loan grade assigned by lender (A, B, C, D, E, F, G)
- **loan_purpose**: Purpose of the loan (debt_consolidation, credit_card, home_improvement, major_purchase, other)

### Borrower Characteristics
- **credit_score**: Borrower's credit score (300-850)
- **annual_income**: Borrower's annual income in USD (integer)
- **employment_length**: Length of employment (<1 year, 1-3 years, 3-5 years, 5-10 years, >10 years)
- **home_ownership**: Home ownership status (RENT, OWN, MORTGAGE)

### Survival Analysis Variables
- **time_to_default**: Time until default or censoring (months, 1 to term_months)
- **defaulted**: Event indicator (1 = defaulted, 0 = censored/completed)
- **censored**: Censoring indicator (1 = censored, 0 = defaulted)

## Survival Analysis Notes

- **Event**: Loan default (defaulted = 1)
- **Time**: Months from loan origination to default or end of observation period
- **Censoring**: Loans that completed their term without defaulting are censored (censored = 1, defaulted = 0)
- **Censored observations**: Loans still active at the end of their term (completed successfully)

## Data Quality

- No missing values
- All variables are properly formatted
- Time-to-event data is complete and valid
- Event indicators are binary (0/1)

## Use Cases

This dataset is suitable for:
- Calculating survival probabilities (non-default rates) over time
- Identifying risk factors for loan default
- Comparing default risk across borrower segments
- Creating Kaplan-Meier survival curves
- Analyzing the impact of loan characteristics on time to default

## Excel Analysis Tips

- Use PivotTables to calculate survival probabilities by time periods
- Create charts to visualize survival curves
- Use conditional formulas (COUNTIFS, SUMIFS) to analyze default rates by segment
- Compare survival across different loan grades, purposes, or borrower characteristics
