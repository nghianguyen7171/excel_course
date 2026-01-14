---
title: Lab 1 Instructions - Excel Basics
layout: default
---

<div class="lab-instructions-page">

<section id="lab-header" class="lab-hero">
<h1>Lab 1: Excel Basics with Product Inventory Dataset</h1>
<p class="lab-subtitle">Master essential Excel formulas, conditional logic, and VLOOKUP with hands-on practice</p>
</section>


<section id="excel-vs-sheets" class="lab-section">
## Important: Excel vs Google Sheets

This lab can be completed using either **Microsoft Excel** (desktop application) or **Google Sheets** (web-based). Most formulas work the same way, but there are some differences in formatting and array formulas:

### Key Differences:

| Feature | Microsoft Excel | Google Sheets |
|---------|----------------|---------------|
| **Format Cells** | Right-click → Format Cells → Currency | Toolbar "123" dropdown → Currency, or Format → Number → Currency |
| **Array Formulas** | Requires Ctrl+Shift+Enter (Windows) or Cmd+Shift+Enter (Mac) | Works automatically, no special keystroke needed |
| **Keyboard Shortcut for Currency** | Ctrl+Shift+4 (Windows) or Cmd+Shift+4 (Mac) | Same: Ctrl+Shift+4 (Windows) or Cmd+Shift+4 (Mac) |

### Instructions Format:
Throughout this lab, instructions will be shown as:
- **Excel:** [Microsoft Excel instructions]
- **Google Sheets:** [Google Sheets instructions]

If instructions are the same for both, they will be shown without labels.

---

</section>

<section id="dataset-overview" class="lab-section">
## Dataset Overview

### Introduction
This lab uses a **Product Inventory** dataset - a simplified, single-table dataset designed to help you master Excel basics. Unlike complex datasets with thousands of rows, this inventory dataset is manageable and allows you to verify your formulas manually.

**Note:** If you're using Google Sheets, you can upload the `Product-Inventory.xlsx` file to Google Drive and open it with Google Sheets. Google Sheets will automatically convert the Excel file format.

### Dataset Structure
The workbook contains two sheets:

1. **Inventory Sheet** (Main data table)
   - Contains 50 products with the following columns:
     - **Product ID**: Unique identifier (e.g., PRD-001, PRD-002)
     - **Product Name**: Name of the product
     - **Category**: Product category (Electronics, Clothing, Food, Books, Sports)
     - **Supplier Code**: Supplier identifier (SUP-A, SUP-B, SUP-C, SUP-D)
     - **Unit Price**: Price per unit (in dollars)
     - **Quantity in Stock**: Current inventory quantity
     - **Reorder Level**: Minimum quantity before reordering is needed
     - **Supplier Name**: Full supplier name

2. **Suppliers Sheet** (Lookup table)
   - Contains supplier information for VLOOKUP exercises:
     - **Supplier Code**: Supplier identifier
     - **Supplier Name**: Full supplier name

### Learning Objectives
By completing this lab, you will:
- Master basic Excel formulas (SUM, AVERAGE, COUNT, MAX, MIN)
- Understand conditional logic (IF, COUNTIF)
- Learn VLOOKUP for data lookup operations
- Distinguish between relative and absolute cell references
- Apply formulas to answer real business questions

---

</section>

<section id="function-reference" class="lab-section">
## Function Reference: Detailed Explanations

This section provides comprehensive explanations of all functions used in this lab. Refer to this section when you need to understand how a function works, its syntax, parameters, and usage.

---

<div class="function-category">
<h3>Basic Aggregation Functions</h3>

<div class="function-card">
<h4>SUM Function</h4>
**Purpose:** Adds all numbers in a specified range or set of cells.

**Syntax:**
```
=SUM(number1, [number2], [number3], ...)
=SUM(range)
=SUM(range1, range2, ...)
```

**Parameters:**
- `number1, number2, ...`: Individual numbers or cell references to add
- `range`: A range of cells (e.g., E2:E51)

**Examples:**
- `=SUM(E2:E51)` - Sums all values in cells E2 through E51
- `=SUM(10, 20, 30)` - Returns 60
- `=SUM(E2:E51, F2:F51)` - Sums values from two different ranges

**Notes:**
- SUM ignores text and empty cells
- Can sum up to 255 individual arguments
- Works with arrays: `=SUM(E2:E51*F2:F51)` multiplies corresponding cells then sums results

**Use Cases:**
- Calculate total sales, total inventory value, total expenses
- Sum values across multiple ranges
- Perform calculations within the SUM function

---

</div>

<div class="function-card">
<h4>AVERAGE Function</h4>
**Purpose:** Calculates the arithmetic mean (average) of a set of numbers.

**Syntax:**
```
=AVERAGE(number1, [number2], [number3], ...)
=AVERAGE(range)
```

**Parameters:**
- `number1, number2, ...`: Individual numbers or cell references
- `range`: A range of cells containing numbers

**Examples:**
- `=AVERAGE(E2:E51)` - Calculates average of all values in E2:E51
- `=AVERAGE(10, 20, 30, 40)` - Returns 25 (100/4)

**Notes:**
- Ignores empty cells and text values
- AVERAGE = SUM of values / COUNT of numeric values
- Returns #DIV/0! if no numeric values found

**Use Cases:**
- Find average price, average sales, average score
- Compare individual values to the average
- Calculate central tendency for data analysis

---

</div>

<div class="function-card">
<h4>COUNT Function</h4>
**Purpose:** Counts the number of cells in a range that contain numbers.

**Syntax:**
```
=COUNT(value1, [value2], ...)
=COUNT(range)
```

**Parameters:**
- `value1, value2, ...`: Individual values or cell references
- `range`: A range of cells to count

**Examples:**
- `=COUNT(E2:E51)` - Counts how many cells in E2:E51 contain numbers
- `=COUNT(A1:A10)` - If A1:A10 has 7 numbers and 3 text values, returns 7

**Notes:**
- Only counts numeric values (numbers, dates, times)
- Ignores text, logical values (TRUE/FALSE), and empty cells
- Use COUNTA if you want to count all non-empty cells including text

**Use Cases:**
- Count numeric entries in a dataset
- Count how many products have prices
- Count completed entries in a form

---

</div>

<div class="function-card">
<h4>COUNTA Function</h4>
**Purpose:** Counts the number of cells in a range that are not empty (counts numbers, text, dates, logical values, and errors).

**Syntax:**
```
=COUNTA(value1, [value2], ...)
=COUNTA(range)
```

**Parameters:**
- `value1, value2, ...`: Individual values or cell references
- `range`: A range of cells to count

**Examples:**
- `=COUNTA(A2:A51)` - Counts all non-empty cells in A2:A51 (including text like Product IDs)
- `=COUNTA(A1:B10)` - Counts all non-empty cells in the range A1:B10

**Notes:**
- Counts any non-empty cell: numbers, text, dates, TRUE/FALSE, error values
- Only ignores truly empty cells
- Use this when you need total count including text values

**Use Cases:**
- Count total number of products (including text IDs)
- Count total entries in a form (regardless of data type)
- Count all non-blank cells in a dataset

---

</div>

<div class="function-card">
<h4>MAX Function</h4>
**Purpose:** Returns the largest (maximum) value from a set of numbers.

**Syntax:**
```
=MAX(number1, [number2], ...)
=MAX(range)
```

**Parameters:**
- `number1, number2, ...`: Individual numbers or cell references
- `range`: A range of cells containing numbers

**Examples:**
- `=MAX(E2:E51)` - Returns the highest value in range E2:E51
- `=MAX(10, 25, 5, 30)` - Returns 30

**Notes:**
- Ignores text and empty cells
- Works with dates and times (returns most recent date/time)
- Returns 0 if no numbers found (not an error)

**Use Cases:**
- Find highest price, maximum sales, peak value
- Identify outliers or extremes in data
- Compare values to maximum

---

</div>

<div class="function-card">
<h4>MIN Function</h4>
**Purpose:** Returns the smallest (minimum) value from a set of numbers.

**Syntax:**
```
=MIN(number1, [number2], ...)
=MIN(range)
```

**Parameters:**
- `number1, number2, ...`: Individual numbers or cell references
- `range`: A range of cells containing numbers

**Examples:**
- `=MIN(E2:E51)` - Returns the lowest value in range E2:E51
- `=MIN(10, 25, 5, 30)` - Returns 5

**Notes:**
- Ignores text and empty cells
- Works with dates and times (returns earliest date/time)
- Returns 0 if no numbers found (not an error)

**Use Cases:**
- Find lowest price, minimum sales, lowest score
- Identify minimum threshold values
- Calculate range: MAX - MIN

---

</div>

<div class="function-category">
<h3>Conditional Functions</h3>

<div class="function-card">
<h4>IF Function</h4>
**Purpose:** Performs a logical test and returns one value if TRUE, another if FALSE.

**Syntax:**
```
=IF(logical_test, value_if_true, value_if_false)
```

**Parameters:**
- `logical_test`: A condition that evaluates to TRUE or FALSE (e.g., F2<G2, A1>100)
- `value_if_true`: Value returned if condition is TRUE
- `value_if_false`: Value returned if condition is FALSE

**Examples:**
- `=IF(F2<G2, "Reorder", "OK")` - Returns "Reorder" if F2 is less than G2, otherwise "OK"
- `=IF(E2>100, "Expensive", "Affordable")` - Returns "Expensive" if price > 100
- `=IF(A1="Yes", 1, 0)` - Returns 1 if A1 contains "Yes", otherwise 0

**Nested IF Examples:**
- `=IF(J2>5000, "High", IF(J2>2000, "Medium", "Low"))` - Three-level classification
  - If J2 > 5000, returns "High"
  - Else if J2 > 2000, returns "Medium"
  - Else returns "Low"

**Notes:**
- Can nest up to 64 IF functions (though readability decreases with more nesting)
- Logical operators: =, <, >, <=, >=, <>
- Can use AND/OR functions for complex conditions: `=IF(AND(A1>10, B1<20), "OK", "No")`

**Use Cases:**
- Categorize data (High/Medium/Low, Pass/Fail)
- Flag conditions (Reorder needed, Alert, Warning)
- Conditional calculations based on criteria

---

</div>

<div class="function-card">
<h4>COUNTIF Function</h4>
**Purpose:** Counts the number of cells within a range that meet a single criterion.

**Syntax:**
```
=COUNTIF(range, criteria)
```

**Parameters:**
- `range`: The range of cells to evaluate
- `criteria`: The condition that defines which cells to count (can be number, expression, text, or cell reference)

**Examples:**
- `=COUNTIF(C2:C51, "Electronics")` - Counts cells containing exactly "Electronics"
- `=COUNTIF(E2:E51, ">100")` - Counts cells greater than 100
- `=COUNTIF(I2:I51, "Reorder")` - Counts cells containing "Reorder"
- `=COUNTIF(C2:C51, A10)` - Counts cells matching value in cell A10

**Criteria Examples:**
- Text: `"Electronics"`, `"High"`
- Number: `100`
- Comparison: `">100"`, `"<50"`, `">=200"`
- Wildcards: `"*Electronics*"` (contains Electronics), `"E*"` (starts with E)
- Cell reference: `A10` (uses value in A10)

**Notes:**
- Criteria must be in quotes for text and operators (">100")
- Use cell references (A10) to make formulas dynamic
- Case-sensitive for text (in Excel, not in Google Sheets by default)

**Use Cases:**
- Count how many products match a category
- Count items above/below threshold
- Count occurrences of specific values
- Frequency analysis

---

</div>

<div class="function-card">
<h4>COUNTIFS Function</h4>
**Purpose:** Counts the number of cells that meet multiple criteria across different ranges.

**Syntax:**
```
=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

**Parameters:**
- `criteria_range1`: First range to evaluate
- `criteria1`: First condition
- `criteria_range2, criteria2, ...`: Additional range/criteria pairs (up to 127 pairs)

**Examples:**
- `=COUNTIFS(C2:C51, "Electronics", I2:I51, "Reorder")` - Counts products that are Electronics AND need Reorder
- `=COUNTIFS(E2:E51, ">100", F2:F51, "<50")` - Counts where price > 100 AND quantity < 50

**Notes:**
- All criteria must be TRUE (AND logic)
- Each criteria_range must have the same number of rows/columns
- Can combine different types of criteria (text, numbers, comparisons)

**Use Cases:**
- Count items meeting multiple conditions
- Multi-dimensional filtering and counting
- Complex conditional counting

---

</div>

<div class="function-card">
<h4>SUMIF Function</h4>
**Purpose:** Sums the values in a range that meet a single criterion.

**Syntax:**
```
=SUMIF(range, criteria, [sum_range])
```

**Parameters:**
- `range`: Range of cells to evaluate against criteria
- `criteria`: Condition that defines which cells to sum
- `sum_range`: (Optional) Range of cells to sum. If omitted, sums the cells in range

**Examples:**
- `=SUMIF(C2:C51, "Electronics", I2:I51)` - Sums values in I2:I51 where C2:C51 equals "Electronics"
- `=SUMIF(E2:E51, ">100")` - Sums all values in E2:E51 that are greater than 100
- `=SUMIF(C2:C51, A10, E2:E51)` - Sums E2:E51 where C2:C51 matches cell A10

**Notes:**
- sum_range must be the same size as range
- If sum_range is omitted, sums the cells in range itself
- Criteria follow same rules as COUNTIF (quotes for text/operators)

**Use Cases:**
- Sum values for specific categories
- Conditional summing based on criteria
- Calculate category totals

---

</div>

<div class="function-card">
<h4>AVERAGEIF Function</h4>
**Purpose:** Calculates the average of values in a range that meet a single criterion.

**Syntax:**
```
=AVERAGEIF(range, criteria, [average_range])
```

**Parameters:**
- `range`: Range of cells to evaluate against criteria
- `criteria`: Condition that defines which cells to average
- `average_range`: (Optional) Range to average. If omitted, averages the cells in range

**Examples:**
- `=AVERAGEIF(C2:C51, "Electronics", E2:E51)` - Averages E2:E51 where C2:C51 equals "Electronics"
- `=AVERAGEIF(C2:C51, A10, E2:E51)` - Averages prices where category matches A10
- `=AVERAGEIF(E2:E51, ">100")` - Averages all values in E2:E51 greater than 100

**Notes:**
- average_range must be the same size as range
- Returns #DIV/0! if no cells match criteria
- Criteria follow same rules as COUNTIF

**Use Cases:**
- Calculate average by category
- Average values meeting specific conditions
- Compare category averages

---

</div>

<div class="function-card">
<h4>SUMPRODUCT Function</h4>
**Purpose:** Multiplies corresponding components in arrays and returns the sum of those products.

**Syntax:**
```
=SUMPRODUCT(array1, [array2], [array3], ...)
```

**Parameters:**
- `array1, array2, ...`: Arrays (ranges) of equal size to multiply and sum

**Examples:**
- `=SUMPRODUCT(E2:E51, F2:E51)` - Multiplies each price by quantity, then sums all results
- `=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))` - Multiplies E*F where C="Electronics", then sums
- `=SUMPRODUCT((A2:A10>50)*(B2:B10))` - Sums B2:B10 where A2:A10 > 50

**Notes:**
- Arrays must be the same size
- Can use boolean logic: `(condition)*array` converts TRUE/FALSE to 1/0
- More powerful than SUMIF for complex conditions
- Works great for conditional multiplication and summing

**Advanced Usage:**
- `=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))` breaks down as:
  1. `(C2:C51="Electronics")` creates array of TRUE/FALSE
  2. Multiplies TRUE/FALSE (treated as 1/0) by prices and quantities
  3. Only non-zero results remain (where condition is TRUE)
  4. Sums all products

**Use Cases:**
- Calculate weighted sums
- Conditional multiplication and summing
- Complex multi-condition calculations
- Alternative to array formulas

---

</div>

<div class="function-category">
<h3>Lookup Functions</h3>

<div class="function-card">
<h4>VLOOKUP Function</h4>
**Purpose:** Searches for a value in the first column of a table and returns a value in the same row from a specified column.

**Syntax:**
```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

**Parameters:**
- `lookup_value`: The value to search for (must be in first column of table_array)
- `table_array`: The table of data to search (must include lookup column and return column)
- `col_index_num`: Column number in table_array to return (1 = first column, 2 = second column, etc.)
- `range_lookup`: (Optional) TRUE for approximate match, FALSE for exact match. Default is TRUE.

**Examples:**
- `=VLOOKUP(B26, Inventory!A2:H51, 8, FALSE)` - Finds B26 in column A, returns value from column H (8th column)
- `=VLOOKUP("PRD-015", Inventory!A2:H51, 5, FALSE)` - Finds "PRD-015", returns Unit Price (5th column)
- `=VLOOKUP(D2, Suppliers!A2:B5, 2, FALSE)` - Looks up D2 in Suppliers sheet, returns Supplier Name

**Important Rules:**
1. **Lookup value must be in the first column** of table_array
2. **Column index counts from the left** of table_array, not the worksheet
3. **Use FALSE for exact match** with text lookups
4. **Use TRUE (or omit) for approximate match** with sorted numeric data

**How VLOOKUP Works:**
1. Searches for lookup_value in the first column of table_array
2. Finds matching row (exact or approximate depending on range_lookup)
3. Moves to the column specified by col_index_num
4. Returns the value at that intersection

**Column Index Explanation:**
If table_array is `A2:H51`:
- Column 1 = Column A (Product ID)
- Column 2 = Column B (Product Name)
- Column 3 = Column C (Category)
- Column 5 = Column E (Unit Price)
- Column 8 = Column H (Supplier Name)

**Common Errors:**
- **#N/A**: Lookup value not found (check spelling, ensure value exists)
- **#REF!**: Column index number exceeds table columns (e.g., col_index_num = 10 but only 8 columns)
- **Wrong value**: Using approximate match (TRUE) when exact match (FALSE) needed

**Use Cases:**
- Look up product information by ID
- Retrieve related data from lookup tables
- Join data from different sheets
- Create reference tables and reports

---

</div>

</section>

<!-- TEMPORARILY HIDDEN - Lab Exercises section (to be enabled in the future)
<section id="exercises" class="lab-section">
<h2>Lab Exercises</h2>

<p class="exercise-intro">The following exercises will guide you through practical applications of Excel functions. Each exercise includes a question, step-by-step instructions, and explanations.</p>

<section id="part-a" class="exercise-section">
<h3>Part A: Basic Formulas</h3>

<div class="exercise-card">
<h4>Exercise A1: SUM Function</h4>
**Question:** What is the total value of all inventory? (Total value = Unit Price × Quantity for each product, then sum all)

**Instructions:**
1. Create a new sheet called "Analysis"
2. In cell A1, type: `Total Inventory Value`
3. In cell B1, enter the formula: `=SUM(Inventory!E2:E51*Inventory!F2:F51)`
   - **Excel:** This is an array formula. After typing, press **Ctrl+Shift+Enter** (Windows) or **Cmd+Shift+Enter** (Mac)
   - **Google Sheets:** Array formulas work automatically - just press Enter
4. Format cell B1 as Currency:
   - **Excel:** Right-click cell B1 → Format Cells → Number → Currency
   - **Google Sheets:** Select cell B1 → Click "123" dropdown in toolbar → Currency, OR Format → Number → Currency

**Alternative Method (Easier):**
1. In the Analysis sheet, create a helper column
2. In column A (starting A2), copy Product IDs from Inventory sheet
3. In column B (starting B2), use formula: `=VLOOKUP(A2,Inventory!A:H,5,FALSE)*VLOOKUP(A2,Inventory!A:H,6,FALSE)`
4. Copy the formula down for all products
5. Sum column B: `=SUM(B2:B51)`

**Answer:** The formula calculates the total dollar value of all products in inventory by multiplying each product's unit price by its quantity and summing all results.

---

</div>

<div class="exercise-card">
<h4>Exercise A2: AVERAGE Function</h4>
**Question:** What is the average unit price across all products?

**Instructions:**
1. In Analysis sheet, cell A3, type: `Average Unit Price`
2. In cell B3, enter: `=AVERAGE(Inventory!E2:E51)`
3. Format cell B3 as Currency:
   - **Excel:** Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select cell → "123" dropdown → Currency, OR Format → Number → Currency

**Answer:** The formula calculates the average (mean) unit price by summing all unit prices and dividing by the number of products.

---

</div>

<div class="exercise-card">
<h4>Exercise A3: COUNT and COUNTA Functions</h4>
**Question:** How many products are in the inventory?

**Instructions:**
1. In Analysis sheet, cell A4, type: `Total Products`
2. In cell B4, enter: `=COUNTA(Inventory!A2:A51)`
   - COUNTA counts all non-empty cells (including text)
   - Alternative: `=COUNT(Inventory!E2:E51)` counts only numeric cells (Unit Price column)

**Answer:** COUNTA returns the total count of products. Since Product ID column contains text values, COUNTA is appropriate. COUNT would only count numeric values.

---

</div>

<div class="exercise-card">
<h4>Exercise A4: MAX and MIN Functions</h4>
**Question:** What is the highest and lowest unit price in the inventory?

**Instructions:**
1. In Analysis sheet:
   - Cell A5: `Highest Unit Price`
   - Cell B5: `=MAX(Inventory!E2:E51)`
   - Cell A6: `Lowest Unit Price`
   - Cell B6: `=MIN(Inventory!E2:E51)`
2. Format B5 and B6 as Currency:
   - **Excel:** Select both cells → Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select both cells → "123" dropdown → Currency, OR Format → Number → Currency

**Answer:** MAX returns the highest unit price; MIN returns the lowest unit price. These functions help identify price extremes in your inventory.

---

</div>

<div class="exercise-card">
<h4>Exercise A5: SUMIF Function</h4>
**Question:** What is the total inventory value for Electronics category?

**Instructions:**
1. In Analysis sheet, cell A8, type: `Electronics Total Value`
2. In cell B8, enter: `=SUMIF(Inventory!C2:C51,"Electronics",Inventory!E2:E51*Inventory!F2:F51)`
   - **Note:** For complex criteria with multiplication, use SUMPRODUCT instead (works better in both Excel and Google Sheets):
   - Better formula: `=SUMPRODUCT((Inventory!C2:C51="Electronics")*(Inventory!E2:E51)*(Inventory!F2:F51))`
3. Format as Currency:
   - **Excel:** Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select cell → "123" dropdown → Currency, OR Format → Number → Currency

**Alternative Method:**
1. Create a helper column in Inventory sheet (Column I) for Inventory Value: `=E2*F2` (Unit Price × Quantity)
2. Copy formula down
3. In Analysis sheet: `=SUMIF(Inventory!C2:C51,"Electronics",Inventory!I2:I51)`

**Answer:** SUMIF conditionally sums values where the category equals "Electronics", calculating total inventory value for that category only.

---

</div>

<div class="exercise-card">
<h4>Exercise A6: AVERAGEIF Function</h4>
**Question:** What is the average unit price for each category?

**Instructions:**
1. In Analysis sheet, starting at A10, create a table:
   ```
   Category       | Average Price
   Electronics    |
   Clothing       |
   Food           |
   Books          |
   Sports         |
   ```
2. In cell B10, enter: `=AVERAGEIF(Inventory!C2:C51,A10,Inventory!E2:E51)`
3. Copy the formula down to B14 (adjusting for each category)
4. Format all as Currency:
   - **Excel:** Select cells B10:B14 → Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select cells B10:B14 → "123" dropdown → Currency, OR Format → Number → Currency

**Answer:** AVERAGEIF calculates the average unit price for products matching each category, helping you understand pricing patterns by category.

---

</div>

</section>

<section id="part-b" class="exercise-section">
<h3>Part B: Conditional Logic</h3>

<div class="exercise-card">
<h4>Exercise B1: IF Function - Stock Status</h4>
**Question:** Which products need to be reordered? (Products where Quantity in Stock < Reorder Level)

**Instructions:**
1. In Inventory sheet, add a new column I with header "Stock Status"
2. In cell I2, enter: `=IF(F2<G2,"Reorder","OK")`
   - F2 = Quantity in Stock
   - G2 = Reorder Level
   - If Quantity < Reorder Level, returns "Reorder", otherwise "OK"
3. Copy the formula down to row 51 (double-click the fill handle or drag)

**Answer:** The IF function compares each product's quantity to its reorder level and flags products that need reordering, helping inventory management.

---

</div>

<div class="exercise-card">
<h4>Exercise B2: Nested IF Function - Priority Classification</h4>
**Question:** Categorize products as High/Medium/Low priority based on inventory value (Unit Price × Quantity)

**Instructions:**
1. First, add a helper column J with header "Inventory Value"
2. In cell J2, enter: `=E2*F2` (Unit Price × Quantity)
3. Copy formula down
4. Add column K with header "Priority"
5. In cell K2, enter nested IF:
   ```
   =IF(J2>5000,"High",IF(J2>2000,"Medium","Low"))
   ```
   - High: Inventory Value > $5,000
   - Medium: Inventory Value $2,000 - $5,000
   - Low: Inventory Value < $2,000
6. Copy formula down to row 51

**Answer:** The nested IF function creates three priority levels based on inventory value thresholds, helping prioritize inventory management efforts.

---

</div>

<div class="exercise-card">
<h4>Exercise B3: COUNTIF Function - Counting by Condition</h4>
**Question:** How many products are below reorder level?

**Instructions:**
1. In Analysis sheet, cell A16, type: `Products Needing Reorder`
2. In cell B16, enter: `=COUNTIF(Inventory!I2:I51,"Reorder")`
   - Counts cells in column I (Stock Status) that contain "Reorder"

**Answer:** COUNTIF counts products flagged as "Reorder" in the Stock Status column, providing a quick summary of inventory management needs.

---

</div>

<div class="exercise-card">
<h4>Exercise B4: Multiple COUNTIF - Count by Category</h4>
**Question:** How many products are in each category?

**Instructions:**
1. In Analysis sheet, create a table starting at A18:
   ```
   Category    | Product Count
   Electronics |
   Clothing    |
   Food        |
   Books       |
   Sports      |
   ```
2. In cell B18, enter: `=COUNTIF(Inventory!C2:C51,A18)`
3. Copy the formula down to B22
   - The formula counts how many times each category appears in column C

**Answer:** COUNTIF counts occurrences of each category, showing the distribution of products across categories.

---

</div>

<div class="exercise-card">
<h4>Exercise B5: COUNTIFS Function - Multiple Conditions</h4>
**Question:** How many Electronics products need reordering?

**Instructions:**
1. In Analysis sheet, cell A24, type: `Electronics Needing Reorder`
2. In cell B24, enter: `=COUNTIFS(Inventory!C2:C51,"Electronics",Inventory!I2:I51,"Reorder")`
   - First condition: Category = "Electronics"
   - Second condition: Stock Status = "Reorder"

**Answer:** COUNTIFS counts products that meet both conditions simultaneously, providing category-specific inventory alerts.

---

</div>

</section>

<section id="part-c" class="exercise-section">
<h3>Part C: VLOOKUP Function</h3>

<div class="exercise-card">
<h4>Exercise C1: Basic VLOOKUP - Single Lookup</h4>
**Question:** What is the supplier name for Product ID PRD-015?

**Instructions:**
1. In Analysis sheet, cell A26, type: `Lookup Product:`
2. In cell B26, enter: `PRD-015`
3. In cell A27, type: `Supplier Name:`
4. In cell B27, enter the VLOOKUP formula:
   ```
   =VLOOKUP(B26,Inventory!A2:H51,8,FALSE)
   ```
   - **B26**: Lookup value (Product ID)
   - **Inventory!A2:H51**: Table array (range to search)
   - **8**: Column index (8th column = Supplier Name)
   - **FALSE**: Exact match (required for text lookups)
5. Try different Product IDs in B26 to test the lookup

**VLOOKUP Syntax:**
```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```
- **lookup_value**: Value to search for
- **table_array**: Range containing lookup and return columns
- **col_index_num**: Column number (from left) containing return value
- **range_lookup**: FALSE for exact match, TRUE for approximate match

**Answer:** VLOOKUP searches for PRD-015 in the first column of the table and returns the corresponding Supplier Name from column 8.

---

</div>

<div class="exercise-card">
<h4>Exercise C2: VLOOKUP Across Sheets</h4>
**Question:** Look up supplier names from the Suppliers sheet using Supplier Code from Inventory sheet.

**Instructions:**
1. In Inventory sheet, we already have Supplier Name in column H, but let's practice VLOOKUP
2. Add a new column L in Inventory sheet with header "Supplier Name (VLOOKUP)"
3. In cell L2, enter:
   ```
   =VLOOKUP(D2,Suppliers!A2:B5,2,FALSE)
   ```
   - **D2**: Supplier Code to lookup
   - **Suppliers!A2:B5**: Lookup table in Suppliers sheet
   - **2**: Return value from 2nd column (Supplier Name)
   - **FALSE**: Exact match
4. Copy formula down to row 51
5. Compare column H and column L - they should match!

**Answer:** VLOOKUP retrieves supplier names from a separate lookup table using Supplier Code, demonstrating how to join data across sheets.

---

</div>

<div class="exercise-card">
<h4>Exercise C3: VLOOKUP with Exact Match - Find Price</h4>
**Question:** Find the unit price for a specific product name.

**Instructions:**
1. In Analysis sheet, cell A29, type: `Product Name:`
2. In cell B29, enter any product name from Inventory (e.g., "Laptop")
3. In cell A30, type: `Unit Price:`
4. In cell B30, enter:
   ```
   =VLOOKUP(B29,Inventory!B2:E51,4,FALSE)
   ```
   - Looks up product name in column B
   - Returns Unit Price from column E (4th column in range B:E)
   - FALSE ensures exact match

**Note:** VLOOKUP searches the first column of the range. If looking up by Product Name, the range must start with column B (Product Name).

**Answer:** VLOOKUP finds the product name and returns its corresponding unit price, useful for price lookups and quotes.

---

</div>

<div class="exercise-card">
<h4>Exercise C4: Multiple VLOOKUP - Retrieve Multiple Fields</h4>
**Question:** Create a lookup table showing Product ID, Name, Category, and Price for specific products.

**Instructions:**
1. In Analysis sheet, create a lookup table starting at A32:
   ```
   Product ID | Product Name | Category | Unit Price
   ```
2. In cell A33, enter: `PRD-001`
3. In cell B33, retrieve Product Name:
   ```
   =VLOOKUP(A33,Inventory!A2:H51,2,FALSE)
   ```
4. In cell C33, retrieve Category:
   ```
   =VLOOKUP(A33,Inventory!A2:H51,3,FALSE)
   ```
5. In cell D33, retrieve Unit Price:
   ```
   =VLOOKUP(A33,Inventory!A2:H51,5,FALSE)
   ```
6. Format D33 as Currency:
   - **Excel:** Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select cell → "123" dropdown → Currency, OR Format → Number → Currency
7. Copy formulas down to create lookup for multiple Product IDs

**Answer:** Multiple VLOOKUP formulas retrieve different fields for the same lookup value, creating a comprehensive product information table.

---

</div>

</section>

<section id="part-d" class="exercise-section">
<h3>Part D: Cell References</h3>

<div class="exercise-card">
<h4>Exercise D1: Relative References</h4>
**Question:** Calculate inventory value (Unit Price × Quantity) for all products.

**Instructions:**
1. This exercise was partially done in Exercise B2, but let's focus on relative references
2. In Inventory sheet, ensure column J has header "Inventory Value"
3. In cell J2, enter: `=E2*F2`
4. Notice: No dollar signs - this is a relative reference
5. Copy the formula down to J51 (drag fill handle or double-click)
6. Check a few cells (J3, J4, J5) - notice the formula automatically adjusts:
   - J3 becomes: `=E3*F3`
   - J4 becomes: `=E4*F4`
   - This is relative reference behavior

**Relative Reference Behavior:**
- When copied, row and column references change relative to the new location
- Use for formulas that should adjust for each row/column
- Default reference type in Excel

**Answer:** Relative references allow the formula to adjust automatically when copied, calculating inventory value for each product using its own price and quantity.

---

</div>

<div class="exercise-card">
<h4>Exercise D2: Absolute References</h4>
**Question:** Compare each product's price to the average price (calculate difference from average).

**Instructions:**
1. First, calculate average price in Analysis sheet (from Exercise A2): `=AVERAGE(Inventory!E2:E51)`
   - Assume this is in cell B3 (result: ~$75.50, your value may vary)
2. In Inventory sheet, add column M with header "Price vs Average"
3. In cell M2, enter: `=E2-$B$3`
   - **E2**: Relative reference (will change when copied)
   - **$B$3**: Absolute reference (will stay the same when copied)
   - Dollar signs ($) lock the row and column
4. Copy formula down to M51
5. Check cells M3, M4 - notice:
   - E2 becomes E3, E4 (relative - changes)
   - $B$3 stays $B$3 (absolute - locked)

**Absolute Reference Behavior:**
- Dollar signs ($) lock row and/or column
- `$B$3`: Both row and column locked
- `$B3`: Column locked, row relative
- `B$3`: Row locked, column relative

**Answer:** Absolute references keep the average price cell constant while relative references allow comparison to each product's individual price.

---

</div>

<div class="exercise-card">
<h4>Exercise D3: Mixed References</h4>
**Question:** Create a multiplication table or practice mixed references.

**Instructions (Optional Practice):**
1. Create a simple multiplication table to understand mixed references
2. In a new area, create:
   ```
       1   2   3   4
   1
   2
   3
   4
   ```
3. In cell referencing 1×1, enter: `=$A$1*B$1`
   - $A$1: Absolute (column and row locked)
   - B$1: Mixed (row locked, column relative)
4. Copy across and down to see how mixed references work

**Answer:** Mixed references allow locking either row or column while the other remains relative, useful for creating tables and structured calculations.

---

</div>

</section>

<section id="part-e" class="exercise-section">
<h3>Part E: Comprehensive Summary Exercise</h3>

<div class="exercise-card">
<h4>Exercise E1: Create Summary Analysis Table</h4>
**Question:** Create a summary table showing for each category: total inventory value, average price, product count, and number of products needing reorder.

**Instructions:**
1. In Analysis sheet, create a summary table starting at A35:
   ```
   Category    | Total Value | Avg Price | Product Count | Need Reorder
   Electronics |
   Clothing    |
   Food        |
   Books       |
   Sports      |
   ```
2. **Total Value** (column B, starting B36):
   ```
   =SUMPRODUCT((Inventory!C2:C51=A36)*(Inventory!E2:E51)*(Inventory!F2:F51))
   ```
   - Sums Unit Price × Quantity for products matching category
3. **Avg Price** (column C, starting C36):
   ```
   =AVERAGEIF(Inventory!C2:C51,A36,Inventory!E2:E51)
   ```
4. **Product Count** (column D, starting D36):
   ```
   =COUNTIF(Inventory!C2:C51,A36)
   ```
5. **Need Reorder** (column E, starting E36):
   ```
   =COUNTIFS(Inventory!C2:C51,A36,Inventory!I2:I51,"Reorder")
   ```
6. Copy all formulas down to row 40
7. Format appropriately (currency for value and price):
   - **Excel:** Select currency columns → Right-click → Format Cells → Number → Currency
   - **Google Sheets:** Select currency columns → "123" dropdown → Currency, OR Format → Number → Currency

**Answer:** This comprehensive table combines multiple formula types (SUMPRODUCT, AVERAGEIF, COUNTIF, COUNTIFS) to provide category-level insights for inventory management decisions.

---

</div>

</section>

</section>
-- END OF TEMPORARILY HIDDEN SECTION -->

<section id="verification" class="lab-section">
## Verification & Expected Results

### Quick Verification Checklist
After completing all exercises, verify your results:

- [ ] Total Inventory Value: Should be a large dollar amount (varies by dataset)
- [ ] Average Unit Price: Should be reasonable (typically $30-$100 range)
- [ ] Total Products: Should be 50
- [ ] Stock Status: Should have some "Reorder" and some "OK" entries
- [ ] VLOOKUP: Should correctly retrieve supplier names and prices
- [ ] Category counts: Should sum to 50 (10 products per category)
- [ ] Summary table: All formulas should calculate correctly

### Common Errors & Troubleshooting

<div class="error-card">
<h4>Error: #N/A in VLOOKUP</h4>
<p><strong>Cause:</strong> Lookup value not found in first column of table array</p>
<p><strong>Fix:</strong> Check spelling, ensure lookup value exists, verify table array range</p>
</div>

<div class="error-card">
<h4>Error: #VALUE!</h4>
<p><strong>Cause:</strong> Wrong data type in formula (e.g., text in math operation)</p>
<p><strong>Fix:</strong> Ensure cells contain numbers where numeric operations are expected</p>
</div>

<div class="error-card">
<h4>Error: #REF!</h4>
<p><strong>Cause:</strong> Formula references deleted or invalid cell</p>
<p><strong>Fix:</strong> Check cell references, verify sheets exist</p>
</div>


<div class="error-card">
<h4>Formula shows as text, not calculated</h4>
<p><strong>Cause:</strong> Missing equals sign (=) at the beginning, or cell formatted as text</p>
<p><strong>Fix:</strong> Add = at the start of the formula. If still showing as text:</p>
<ul>
<li><strong>Excel:</strong> Change cell format from Text to General, then re-enter formula</li>
<li><strong>Google Sheets:</strong> Change cell format from Plain text to Automatic, then re-enter formula</li>
</ul>
</div>

<div class="error-card">
<h4>Wrong results from COUNTIF/SUMIF</h4>
<p><strong>Cause:</strong> Criteria syntax incorrect (missing quotes for text)</p>
<p><strong>Fix:</strong> Use quotes for text criteria: <code>"Electronics"</code> not <code>Electronics</code></p>
</div>

---

</section>

<section id="conclusion" class="lab-section">
## Conclusion

Congratulations! You have completed Lab 1 covering:
- ✅ Basic formulas (SUM, AVERAGE, COUNT, MAX, MIN)
- ✅ Conditional logic (IF, COUNTIF, COUNTIFS)
- ✅ VLOOKUP for data lookup
- ✅ Relative and absolute cell references
- ✅ Combining multiple formulas for analysis

### Next Steps
- Practice these formulas on different datasets
- Experiment with variations of the formulas
- Try creating your own analysis questions
- Prepare for next week's topics: PivotTables and data visualization

---

**Lab Completed:** _________________  
**Date:** _________________  
**Instructor Signature:** _________________

</section>

</div>
