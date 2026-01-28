"""
Lab 2 Dataset Generator: Store Sales Orders

Generates a synthetic dataset with deliberate data quality issues for practicing
Power Query import, cleaning, and missing-value handling (Week 3 / Lab 2).

Outputs:
  - Lab2-StoreOrders.csv
  - Lab2-StoreOrders.xlsx

Schema:
  OrderID (text), OrderDate (stored as text), Customer (text), Category (text),
  Amount (numeric, some as text), Quantity (numeric, some as text),
  Region (text), Notes (text)

Embedded issues (for instructors):
  - Duplicates: 4 exact duplicate rows (original indices 39, 79, 119, 159)
  - OrderDate: all stored as text (YYYY-MM-DD)
  - Amount/Quantity as text: ~12% of rows (every 8th from 5)
  - Trim/Clean: Customer, Category, Region have leading/trailing spaces
  - Missing: Region blank ~5%; Notes blank ~30% (i % 3 == 1)
  - Blank rows: 4 fully blank rows inserted
  - Replace Values: Category has "Electronics", " electronics ", "ELECTRONICS", etc.
"""

from pathlib import Path
import csv
import random

import pandas as pd

SEED = 42
random.seed(SEED)

OUT_DIR = Path(__file__).resolve().parent / "files"
LAB2_DATASET = Path(__file__).resolve().parent.parent.parent / "student desk" / "Lab-2-Dataset"

N = 200
CATEGORIES = ["Electronics", "Clothing", "Food", "Books", "Sports"]
REGIONS = ["North", "South", "East", "West"]
TEXT_NUMERIC_ROWS = set(range(5, N, 8))
MISSING_REGION_ROWS = {10, 30, 50, 70, 90, 110, 130, 150, 170, 190}
DUPLICATE_SOURCE_ROWS = (39, 79, 119, 159)
BLANK_INSERT_AFTER = (50, 102, 154, 206)


def build_rows():
    rows = []
    for i in range(N):
        base_cat = CATEGORIES[i % len(CATEGORIES)]
        amt = round(random.uniform(15, 250), 2)
        qty = random.randint(1, 10)
        yr, mon, day = 2024, (i % 12) + 1, (i % 28) + 1
        date_str = f"{yr}-{mon:02d}-{day:02d}"
        customer = ["Alice Chen", "Bob Smith", "Carol Lee", "Dan Park", "Eva Kim"][i % 5]
        region = REGIONS[i % len(REGIONS)]
        category = base_cat

        if i % 4 == 0:
            customer = "  " + customer + "  "
        if i % 5 == 1:
            category = " " + base_cat.lower() + " "
        elif i % 5 == 2 and base_cat == "Electronics":
            category = "ELECTRONICS"
        if i % 3 == 0:
            region = "  " + region + "  "
        if i in MISSING_REGION_ROWS:
            region = ""
        notes = "" if i % 3 == 1 else f"Order note {i}"

        amount_val = str(amt) if i in TEXT_NUMERIC_ROWS else amt
        qty_val = str(qty) if i in TEXT_NUMERIC_ROWS else qty

        rows.append({
            "OrderID": f"ORD-{1001 + i}",
            "OrderDate": date_str,
            "Customer": customer,
            "Category": category,
            "Amount": amount_val,
            "Quantity": qty_val,
            "Region": region,
            "Notes": notes,
        })

    # Insert duplicates
    for idx in DUPLICATE_SOURCE_ROWS:
        rows.insert(idx + 1, rows[idx].copy())

    # Insert blank rows
    blank = {k: "" for k in rows[0].keys()}
    for pos in BLANK_INSERT_AFTER:
        if pos <= len(rows):
            rows.insert(pos, blank.copy())

    return rows


def _write_csv_excel(rows, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "Lab2-StoreOrders.csv"
    excel_path = out_dir / "Lab2-StoreOrders.xlsx"

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(["OrderID", "OrderDate", "Customer", "Category", "Amount", "Quantity", "Region", "Notes"])
        for i, r in enumerate(rows):
            if all(r[k] == "" for k in r):
                w.writerow(["", "", "", "", "", "", "", ""])
                continue
            amt, qty = r["Amount"], r["Quantity"]
            aout = str(amt) if isinstance(amt, str) and amt and not amt.isspace() else (float(amt) if isinstance(amt, (int, float)) else amt)
            qout = str(qty) if isinstance(qty, str) and qty and not qty.isspace() else (int(qty) if isinstance(qty, (int, float)) else qty)
            w.writerow([r["OrderID"], r["OrderDate"], r["Customer"], r["Category"], aout, qout, r["Region"], r["Notes"]])

    excel_rows = []
    for i, r in enumerate(rows):
        row = r.copy()
        if isinstance(row["Amount"], str) and row["Amount"] and not row["Amount"].isspace():
            pass
        elif row["OrderID"]:
            row["Amount"] = float(row["Amount"]) if isinstance(row["Amount"], str) else row["Amount"]
        if isinstance(row["Quantity"], str) and row["Quantity"] and not row["Quantity"].isspace():
            pass
        elif row["OrderID"]:
            row["Quantity"] = int(float(row["Quantity"])) if isinstance(row["Quantity"], str) else row["Quantity"]
        excel_rows.append(row)

    df = pd.DataFrame(excel_rows)
    df.to_excel(excel_path, index=False, sheet_name="Orders")
    return csv_path, excel_path


def main():
    rows = build_rows()
    n_dup = len(DUPLICATE_SOURCE_ROWS)
    n_blank = len(BLANK_INSERT_AFTER)

    for out_dir in [OUT_DIR, LAB2_DATASET]:
        csv_p, xl_p = _write_csv_excel(rows, out_dir)
        print(f"Wrote {csv_p} and {xl_p}")

    print(f"Rows: {len(rows)} (includes {n_dup} duplicates, {n_blank} blank rows)")


if __name__ == "__main__":
    main()
