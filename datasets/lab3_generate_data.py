"""
Lab 3 Dataset Generator: Medical EDA Practice

Generates a synthetic medical dataset for Week 5/6 (EDA + PivotTables + basic inference).

Outputs:
  - Medical-EDA.csv
  - Medical-EDA.xlsx

Schema:
  PatientID, VisitDate, Age, Sex, Region, HospitalUnit, DiagnosisGroup,
  TreatmentGroup, BaselineSBP, FollowupSBP, LDL, HbA1c, BMI,
  AdherenceScore, LengthOfStay, Readmission30d, Notes

Embedded quality issues:
  - Duplicates: 3 exact duplicate rows
  - Blank rows: 2 fully blank rows
  - Wrong types: LDL and AdherenceScore as text in selected rows
  - Inconsistent text: DiagnosisGroup/TreatmentGroup/Region capitalization and spaces
  - Missing values: Region and HbA1c in selected rows
  - Outliers: a few implausible BMI/LengthOfStay values
"""

from pathlib import Path
import csv
import random

import pandas as pd

SEED = 73
random.seed(SEED)

OUT_DIR = Path(__file__).resolve().parent / "files"
LAB3_DATASET = Path(__file__).resolve().parent.parent.parent / "student desk" / "Lab-3-Dataset"

N = 240
REGIONS = ["North", "South", "East", "West"]
UNITS = ["Cardiology", "Endocrinology", "Pulmonology", "General"]
DIAG = ["Hypertension", "Diabetes", "Respiratory"]
SEXES = ["Female", "Male"]
TEXT_NUMERIC_ROWS = set(range(6, N, 11))
MISSING_REGION_ROWS = {17, 38, 71, 99, 128, 166, 207}
MISSING_HBA1C_ROWS = {12, 47, 84, 121, 155, 198, 223}
DUPLICATE_SOURCE_ROWS = (45, 120, 189)
BLANK_INSERT_AFTER = (80, 205)


def _treatment(diagnosis: str, i: int) -> str:
    # Alternate treatment groups while keeping balance by diagnosis.
    if diagnosis == "Hypertension":
        return "A" if i % 2 == 0 else "B"
    if diagnosis == "Diabetes":
        return "A" if i % 3 != 0 else "B"
    return "B" if i % 4 == 0 else "A"


def build_rows():
    rows = []
    for i in range(N):
        diagnosis = DIAG[i % len(DIAG)]
        treatment = _treatment(diagnosis, i)
        region = REGIONS[i % len(REGIONS)]
        unit = UNITS[i % len(UNITS)]
        sex = SEXES[i % 2]

        # Core demographics and dates.
        age = random.randint(30, 82)
        month = (i % 12) + 1
        day = (i % 28) + 1
        visit_date = f"2025-{month:02d}-{day:02d}"

        # Baselines differ slightly by diagnosis.
        baseline_sbp = round(random.gauss(146 if diagnosis == "Hypertension" else 136, 13), 1)
        ldl = round(random.gauss(145 if diagnosis != "Respiratory" else 125, 25), 1)
        hba1c = round(random.gauss(7.4 if diagnosis == "Diabetes" else 5.9, 0.8), 2)
        bmi = round(random.gauss(27.8, 4.2), 1)
        adherence = round(max(45, min(99, random.gauss(81, 10))), 1)

        # Treatment A has slightly better SBP follow-up on average (for p-value practice).
        improve = random.gauss(13.0, 5.2) if treatment == "A" else random.gauss(8.8, 5.6)
        followup_sbp = round(max(95, baseline_sbp - improve), 1)

        # Clinical outcomes.
        los = max(1, int(round(random.gauss(4.8 if treatment == "A" else 6.0, 1.8))))
        readm = 1 if (treatment == "B" and random.random() < 0.24) or (treatment == "A" and random.random() < 0.14) else 0

        # Inject text inconsistencies.
        if i % 9 == 0:
            region = f"  {region.lower()}  "
        if i % 10 == 4:
            diagnosis = f" {diagnosis.upper()} "
        if i % 13 == 2:
            treatment = treatment.lower()

        # Missing values.
        if i in MISSING_REGION_ROWS:
            region = ""
        if i in MISSING_HBA1C_ROWS:
            hba1c = ""

        # Mixed numeric types as text.
        ldl_value = f"{ldl}" if i in TEXT_NUMERIC_ROWS else ldl
        adh_value = f" {adherence} " if i in TEXT_NUMERIC_ROWS else adherence

        # A few outliers.
        if i in {53, 174}:
            bmi = 52.5
        if i in {61, 199}:
            los = 28

        notes = "" if i % 4 == 1 else f"Follow-up note {i}"

        rows.append(
            {
                "PatientID": f"PT-{2001 + i}",
                "VisitDate": visit_date,
                "Age": age,
                "Sex": sex,
                "Region": region,
                "HospitalUnit": unit,
                "DiagnosisGroup": diagnosis,
                "TreatmentGroup": treatment,
                "BaselineSBP": baseline_sbp,
                "FollowupSBP": followup_sbp,
                "LDL": ldl_value,
                "HbA1c": hba1c,
                "BMI": bmi,
                "AdherenceScore": adh_value,
                "LengthOfStay": los,
                "Readmission30d": readm,
                "Notes": notes,
            }
        )

    # Insert duplicate rows.
    for idx in DUPLICATE_SOURCE_ROWS:
        rows.insert(idx + 1, rows[idx].copy())

    # Insert fully blank rows.
    blank = {k: "" for k in rows[0].keys()}
    for pos in BLANK_INSERT_AFTER:
        if pos <= len(rows):
            rows.insert(pos, blank.copy())

    return rows


def _write_csv_excel(rows, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "Medical-EDA.csv"
    excel_path = out_dir / "Medical-EDA.xlsx"
    cols = list(rows[0].keys())

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(cols)
        for row in rows:
            if all(row[k] == "" for k in cols):
                w.writerow([""] * len(cols))
            else:
                w.writerow([row[c] for c in cols])

    # Keep mixed types for intended cleaning practice.
    pd.DataFrame(rows, columns=cols).to_excel(excel_path, index=False, sheet_name="MedicalEDA")
    return csv_path, excel_path


def main():
    rows = build_rows()
    for out_dir in (OUT_DIR, LAB3_DATASET):
        csv_p, xlsx_p = _write_csv_excel(rows, out_dir)
        print(f"Wrote {csv_p} and {xlsx_p}")
    print(f"Rows: {len(rows)} (includes {len(DUPLICATE_SOURCE_ROWS)} duplicates, {len(BLANK_INSERT_AFTER)} blank rows)")


if __name__ == "__main__":
    main()
