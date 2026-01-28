---
title: Lab 2 Instructions - Data Import & Cleaning
layout: default
---

<div class="lab-instructions-page">

<section id="lab-header" class="lab-hero">
<h1>Lab 2: Data Import & Cleaning with Store Sales Orders</h1>
<p class="lab-subtitle">Import from CSV/Excel, clean data with Power Query, and handle missing values.</p>
</section>

<section id="excel-vs-sheets" class="lab-section">
## Important: Excel vs Google Sheets

This lab is designed for **Microsoft Excel** and **Power Query**. Get Data and the Power Query Editor are Excel-specific. Google Sheets uses different tools (e.g. Connect to data, Import). Students should use **Excel** for these exercises.

---

</section>

<section id="dataset-overview" class="lab-section">
## Dataset Overview

### Introduction

This lab uses a **Store Sales Orders** dataset — a synthetic table with **200+ rows** and deliberate data quality issues so you can practice importing, cleaning, and handling missing values with Power Query.

### Dataset Files

The Lab 2 dataset is available from:

1. **Google Drive (recommended):** [**Lab 2 Dataset — Google Drive**](https://drive.google.com/drive/folders/1F92S9FEN5SWvUQsEXIs9c1J4q90uARCm?usp=sharing) — contains `Lab2-StoreOrders.csv` and `Lab2-StoreOrders.xlsx`. Download both to a folder on your computer before starting.

2. **Course website (alternative):**
   - [**Lab2-StoreOrders.csv**]({{ site.baseurl }}/datasets/files/Lab2-StoreOrders.csv) — for *Import from CSV* exercises.
   - [**Lab2-StoreOrders.xlsx**]({{ site.baseurl }}/datasets/files/Lab2-StoreOrders.xlsx) — for *Import from Excel* exercises.

3. **Student package:** The **Lab-2-Dataset** folder (if provided) contains the same files plus extended instructions (**WithKeys** and **NoKeys** versions). Use those files the same way.

Download or locate both files before starting. Use the CSV for *Import from CSV* and the Excel file for *Import from Excel*.

### Variables

| Column | Intended type | Description |
|--------|---------------|-------------|
| OrderID | Text | Unique order identifier (e.g. ORD-1001) |
| OrderDate | Date | Order date (stored as text in the source) |
| Customer | Text | Customer name |
| Category | Text | Product category (Electronics, Clothing, Food, Books, Sports) |
| Amount | Number | Order amount (some rows stored as text) |
| Quantity | Number | Quantity (some rows stored as text) |
| Region | Text | Sales region (North, South, East, West) |
| Notes | Text | Optional notes (many blanks) |

### Data Quality Notes

The dataset contains intentional issues for practice:

- **Duplicates:** Some duplicate rows.
- **Wrong types:** Order dates stored as text; Amount and Quantity stored as text in several rows.
- **Trim/Clean:** Leading and trailing spaces in Customer, Category, and Region.
- **Missing values:** Blanks in Region (a few rows) and Notes (many rows).
- **Blank rows:** A few fully blank rows.
- **Replace Values:** Inconsistent Category values (e.g. "Electronics", " electronics ", "ELECTRONICS").

### Learning Objectives

By completing this lab, you will:

- Import data from CSV and Excel using Get Data (Power Query).
- Use the Power Query Editor to change data types, remove duplicates, filter rows, and replace values.
- Apply Trim and Clean, remove blank rows, and add a conditional column to flag missing values.
- Load cleaned data to a worksheet (and optionally to the Data Model) and refresh queries.

---

</section>

<section id="pq-reference" class="lab-section">
## Power Query & Excel Quick Reference

Use this section as a quick reference for menu paths. Refer to the Week 3 slides and [1] Ch. 2–3 for more detail.

<h3>Import Data</h3>

<h4>Import CSV</h4>
<pre><code>Data → Get Data → From File → From Text/CSV → Load / Transform Data</code></pre>

<h4>Import Excel</h4>
<pre><code>Data → Get Data → From File → From Excel Workbook → Select Sheet/Table → Load / Transform Data</code></pre>

<h4>Import Web</h4>
<pre><code>Data → Get Data → From Other Sources → From Web → Enter URL → Transform Data</code></pre>

<h3>Open Power Query Editor</h3>
<pre><code>Data → Get Data → Transform Data</code></pre>
<p>or</p>
<pre><code>Data → Queries &amp; Connections → Right-click Query → Edit</code></pre>

<h3>Data Type</h3>
<pre><code>Power Query Editor → Transform → Data Type</code></pre>

<h3>Remove Duplicates</h3>
<pre><code>Power Query Editor → Home → Remove Rows → Remove Duplicates</code></pre>

<h3>Filter Rows</h3>
<pre><code>Column Header → Filter Dropdown → Text / Number / Date Filters</code></pre>

<h3>Replace Values</h3>
<pre><code>Power Query Editor → Transform → Replace Values</code></pre>

<h3>Trim / Clean Text</h3>
<pre><code>Power Query Editor → Transform → Format → Trim
Power Query Editor → Transform → Format → Clean</code></pre>

<h3>Remove Blank Rows</h3>
<pre><code>Power Query Editor → Home → Remove Rows → Remove Blank Rows</code></pre>

<h3>Conditional Column (Flag Missing)</h3>
<pre><code>Power Query Editor → Add Column → Conditional Column</code></pre>

<h3>Load Data</h3>

<h4>Load to Worksheet</h4>
<pre><code>Power Query Editor → Close &amp; Load</code></pre>

<h4>Load to Data Model</h4>
<pre><code>Power Query Editor → Close &amp; Load To…
→ Only Create Connection
→ Add this data to the Data Model</code></pre>

<h3>Refresh Data</h3>
<pre><code>Data → Refresh All</code></pre>
<p>or</p>
<pre><code>Data → Queries &amp; Connections → Right-click Query → Refresh</code></pre>

---

</section>

<section id="exercises" class="lab-section">
<h2>Lab Exercises</h2>

<p class="exercise-intro">The following exercises guide you through importing, cleaning, and loading the Store Sales Orders data with Power Query. Each exercise includes a question, step-by-step instructions, and a brief answer.</p>

<section id="part-a" class="exercise-section">
<h3>Part A: Import Data</h3>

<div class="exercise-card">
<h4>Exercise A1: Import from CSV</h4>

**Question:** Import the Store Sales Orders data from CSV and open the Power Query Editor. What do you see in the preview (column types, obvious issues)?

**Instructions:**

1. **Excel:** Data → Get Data → From File → From Text/CSV.
2. Select `Lab2-StoreOrders.csv` (in the folder where you saved it). Click **Transform Data** (not Load).
3. In the Power Query Editor, check the data types shown in the column headers and scan for duplicates, blanks, or odd formatting.

**Answer:** You should see columns such as OrderID, OrderDate, Customer, Category, Amount, Quantity, Region, Notes. Some types may be detected as Text (e.g. OrderDate, or Amount/Quantity in certain rows). You may notice duplicate rows, blank rows, extra spaces in text, and missing values in Region and Notes.

---

</div>

<div class="exercise-card">
<h4>Exercise A2: Import from Excel</h4>

**Question:** Import the same dataset from the Excel workbook and open the Power Query Editor.

**Instructions:**

1. **Excel:** Data → Get Data → From File → From Excel Workbook.
2. Select `Lab2-StoreOrders.xlsx`, then choose the **Orders** sheet (or table). Click **Transform Data**.
3. Confirm the structure matches the CSV import.

**Answer:** The Orders sheet has the same columns and rows as the CSV. You can use either source for the cleaning exercises; use one consistently for Part B–D.

---

</div>

<div class="exercise-card">
<h4>Exercise A3 (optional): Import from Web</h4>

**Question:** Import a small table from a web page using Get Data → From Web.

**Instructions:**

1. **Excel:** Data → Get Data → From Other Sources → From Web.
2. Enter a URL that contains an HTML table (e.g. a simple reference table). Use **Transform Data** to preview and clean if needed.
3. Document the URL and the steps you used.

**Answer:** "Import from Web" is covered in the Week 3 slides. Use any stable URL with a table; the goal is to practice the From Web workflow.

---

</div>

</section>

<section id="part-b" class="exercise-section">
<h3>Part B: Power Query Transformations</h3>

<div class="exercise-card">
<h4>Exercise B1: Change Data Types</h4>

**Question:** Set correct data types for OrderDate, Amount, and Quantity.

**Instructions:**

1. In the Power Query Editor, select the **OrderDate** column. Transform → Data Type → Date (or Date/Time). Use the correct locale if prompted.
2. Select **Amount** → Transform → Data Type → Decimal Number (or Currency if appropriate).
3. Select **Quantity** → Transform → Data Type → Whole Number.
4. Check for any columns still detected as Text that should be numeric; fix them.

**Answer:** After changing types, OrderDate supports date filters and sorting; Amount and Quantity can be used in calculations and aggregates.

---

</div>

<div class="exercise-card">
<h4>Exercise B2: Remove Duplicates</h4>

**Question:** Remove duplicate rows and note how many rows were removed.

**Instructions:**

1. Select all columns (or the key columns you use for duplicates, e.g. OrderID).
2. Home → Remove Rows → Remove Duplicates.
3. Check the row count before and after; record the number of rows removed.

**Answer:** The dataset contains duplicate rows. After removing duplicates, the row count decreases; the exact number depends on your selection (all columns vs. key columns).

---

</div>

<div class="exercise-card">
<h4>Exercise B3: Filter Rows</h4>

**Question:** Use the column filter dropdowns to inspect or exclude certain values (e.g. blanks or a specific Category/Region).

**Instructions:**

1. Click the filter icon on a column header (e.g. Category or Region).
2. Use Text Filters or “Remove Empty” (or equivalent) to filter out blanks if needed, or filter to a single category for inspection.
3. Remove or adjust the filter as needed for later steps (e.g. you may remove blank rows via Home → Remove Rows → Remove Blank Rows instead).

**Answer:** Filtering helps you inspect subsets of the data. Use it to confirm blanks or specific categories before standardizing values.

---

</div>

<div class="exercise-card">
<h4>Exercise B4: Replace Values</h4>

**Question:** Standardize the Category column (e.g. replace "ELECTRONICS", " electronics " with "Electronics").

**Instructions:**

1. Select the **Category** column. Transform → Replace Values.
2. Replace each variant (e.g. "ELECTRONICS", " electronics ") with the standard form "Electronics". Repeat for other categories (Clothing, Food, Books, Sports) as needed.
3. Alternatively, use a Conditional Column or multiple Replace Values steps.

**Answer:** After replacing values, Category has consistent capitalization and spacing, making it suitable for grouping and reporting.

---

</div>

<div class="exercise-card">
<h4>Exercise B5: Trim and Clean</h4>

**Question:** Apply Trim to Customer, Category, and Region; use Clean if you encounter non-printable characters.

**Instructions:**

1. Select **Customer**. Transform → Format → Trim. Repeat for **Category** and **Region**.
2. If any column has non-printable characters (e.g. from imported web or text data), use Transform → Format → Clean on that column.

**Answer:** Trim removes leading and trailing spaces; Clean removes non-printable characters. Both improve consistency for text columns.

---

</div>

</section>

<section id="part-c" class="exercise-section">
<h3>Part C: Missing Values</h3>

<div class="exercise-card">
<h4>Exercise C1: Remove Blank Rows</h4>

**Question:** Remove fully blank rows and note the change in row count.

**Instructions:**

1. Home → Remove Rows → Remove Blank Rows.
2. Compare the row count before and after.

**Answer:** Blank rows are removed. The number of rows deleted equals the number of fully blank rows in the table.

---

</div>

<div class="exercise-card">
<h4>Exercise C2: Flag Missing Notes</h4>

**Question:** Add a conditional column that flags rows where Notes is null or blank, without deleting those rows.

**Instructions:**

1. Add Column → Conditional Column.
2. Set **Column name** (e.g. `Notes_Missing`). If **Notes** is null or equals `""`, output `Yes` (or `True`); otherwise `No` (or `False`).
3. Load the query and confirm the new column appears.

**Answer:** The new column identifies rows with missing Notes. You can use it for analysis or reporting while keeping all rows.

---

</div>

<div class="exercise-card">
<h4>Exercise C3: Document Your Strategy</h4>

**Question:** In one or two sentences, state how you handled missing values in Region and Notes (e.g. removed blank rows, flagged missing, left as-is).

**Answer:** Example: “We removed fully blank rows, flagged missing Notes with a conditional column, and kept Region as-is (including blanks) for filtering. We did not impute values.”

---

</div>

</section>

<section id="part-d" class="exercise-section">
<h3>Part D: Load and Refresh</h3>

<div class="exercise-card">
<h4>Exercise D1: Load to Worksheet</h4>

**Question:** Load the cleaned data into an Excel table in a new sheet.

**Instructions:**

1. In the Power Query Editor, **Close & Load**.
2. Ensure the query has a clear name (e.g. `StoreOrders_Cleaned`). Rename it in Queries & Connections if needed.

**Answer:** The cleaned data appears as a table in a new worksheet. You can use it for further analysis or PivotTables.

---

</div>

<div class="exercise-card">
<h4>Exercise D2 (optional): Load to Data Model</h4>

**Question:** Create a connection that loads the data into the Data Model only (no worksheet).

**Instructions:**

1. Duplicate the query or create a new one from the same source. **Close & Load To…**
2. Choose **Only Create Connection** and check **Add this data to the Data Model**.
3. Confirm in Data → Queries & Connections that the query exists and is connected to the Data Model.

**Answer:** The data is available for PivotTables and DAX via the Data Model, without a separate table on a sheet.

---

</div>

<div class="exercise-card">
<h4>Exercise D3: Refresh Data</h4>

**Question:** Refresh the query after changing the source file and confirm the change appears.

**Instructions:**

1. Close the workbook or ensure the source CSV/Excel is not locked. Add a new row to the source file (or change an existing value), then save.
2. In Excel, Data → Refresh All (or right-click the query → Refresh).
3. Verify that the updated data appears in the loaded table.

**Answer:** Refresh replays the query steps on the current source. Use it when source files are updated regularly.

---

</div>

</section>

</section>

<section id="verification" class="lab-section">
## Verification & Expected Results

### Quick Verification Checklist

After completing all exercises, verify:

- [ ] Data imported from CSV and from Excel (and optionally from Web).
- [ ] OrderDate, Amount, and Quantity have correct data types.
- [ ] Duplicates removed; row count change documented.
- [ ] Category standardized; Trim (and Clean if needed) applied to text columns.
- [ ] No fully blank rows; optional Notes_Missing (or similar) column added.
- [ ] Query loaded to worksheet (and optionally to Data Model).
- [ ] Refresh works after updating the source file.

### Common Errors & Troubleshooting

<div class="error-card">
<h4>Date stays as text after Change Type</h4>
<p><strong>Cause:</strong> Format or locale mismatch; column contains invalid dates.</p>
<p><strong>Fix:</strong> Use Transform → Data Type → Date and choose the correct locale. Ensure all values are valid dates; fix or remove problematic rows if needed.</p>
</div>

<div class="error-card">
<h4>Wrong step order or duplicate steps</h4>
<p><strong>Cause:</strong> Steps applied in the wrong order or applied twice.</p>
<p><strong>Fix:</strong> In Applied Steps, delete or reorder steps as needed. Re-run the query to preview results.</p>
</div>

<div class="error-card">
<h4>Refresh fails</h4>
<p><strong>Cause:</strong> Source file moved, renamed, or open elsewhere; connection settings incorrect.</p>
<p><strong>Fix:</strong> Ensure the source path is correct, the file is not locked by another app, and the connection uses the right file path. Re-import if necessary.</p>
</div>

---

</section>

<section id="conclusion" class="lab-section">
## Conclusion

Congratulations! You have completed Lab 2 covering:

- Import from CSV and Excel (and optionally Web) using Get Data.
- Power Query transformations: Change Type, Remove Duplicates, Filter Rows, Replace Values, Trim, Clean, Remove Blank Rows.
- Handling missing values: Remove Blank Rows, Conditional Column to flag missing, and documenting your strategy.
- Loading to a worksheet (and optionally the Data Model) and refreshing queries.

### Next Steps

- Use the cleaned Store Sales Orders data for EDA and PivotTables in later labs.
- Practice the same workflow on other datasets (e.g. Titanic, project topic data).
- Prepare for **Group Progress Report 2:** data quality assessment, cleaning methodology, and preliminary data structure documentation (see course schedule).

---

**Lab Completed:** _________________  
**Date:** _________________  
**Instructor Signature:** _________________

</section>

</div>
