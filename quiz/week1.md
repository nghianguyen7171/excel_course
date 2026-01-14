---
title: Week 1 Quiz - Excel Basics
layout: default
---

<div class="quiz-page">
<section id="week1-quiz" class="quiz-section">
  <div class="quiz-hero">
    <h1>Week 1's Quiz</h1>
    <p class="quiz-subtitle">Test your knowledge of basic formulas, conditional logic, and lookup functions.</p>
  </div>

  <div class="quiz-grid">
    <!-- Q1 -->
    <div class="quiz-card">
      <h3>Q1. SUM & Multiplication</h3>
      <p>You need total revenue from a single-row record where Unit Price is in E2 and Quantity is in F2. Which formula is correct?</p>
      <ul class="quiz-options">
        <li>A) <code>=SUM(E2*F2)</code></li>
        <li>B) <code>=E2*F2</code></li>
        <li>C) <code>=SUM(E2,F2)</code></li>
        <li>D) <code>=SUM(E2:F2)</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> B) <code>=E2*F2</code></p>
        <p><strong>Explanation:</strong> For a single row, multiply Unit Price by Quantity directly. SUM is unnecessary unless summing multiple rows.</p>
      </details>
    </div>

    <!-- Q2 -->
    <div class="quiz-card">
      <h3>Q2. COUNT vs COUNTA</h3>
      <p>Column A has Product IDs (text) and blank cells. You want to count how many products are listed. Which function?</p>
      <ul class="quiz-options">
        <li>A) <code>=COUNT(A2:A100)</code></li>
        <li>B) <code>=COUNTA(A2:A100)</code></li>
        <li>C) <code>=COUNTIF(A2:A100,">0")</code></li>
        <li>D) <code>=SUM(A2:A100)</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> B) <code>=COUNTA(A2:A100)</code></p>
        <p><strong>Explanation:</strong> COUNTA counts non-empty cells, including text Product IDs; COUNT only counts numbers.</p>
      </details>
    </div>

    <!-- Q3 -->
    <div class="quiz-card">
      <h3>Q3. IF for Stock Status</h3>
      <p>Quantity is in F2 and Reorder Level in G2. Which formula flags <em>Reorder</em> when stock is below the level?</p>
      <ul class="quiz-options">
        <li>A) <code>=IF(F2>G2,"Reorder","OK")</code></li>
        <li>B) <code>=IF(F2<G2,"Reorder","OK")</code></li>
        <li>C) <code>=IF(F2=G2,"Reorder","OK")</code></li>
        <li>D) <code>=IF(G2-F2,"Reorder","OK")</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> B) <code>=IF(F2<G2,"Reorder","OK")</code></p>
        <p><strong>Explanation:</strong> Reorder is needed when Quantity (F2) is less than Reorder Level (G2).</p>
      </details>
    </div>

    <!-- Q4 (with table example) -->
    <div class="quiz-card">
      <h3>Q4. VLOOKUP with Table Example</h3>
      <p>Find the Supplier Name for Product ID <code>PRD-015</code> from this table:</p>
      <div class="quiz-table-wrapper">
        <table class="quiz-table">
          <thead>
            <tr><th>Product ID</th><th>Product Name</th><th>Category</th><th>Supplier Name</th></tr>
          </thead>
          <tbody>
            <tr><td>PRD-014</td><td>Camera</td><td>Electronics</td><td>SUP-A</td></tr>
            <tr><td>PRD-015</td><td>Headphones</td><td>Electronics</td><td>SUP-B</td></tr>
            <tr><td>PRD-016</td><td>Jacket</td><td>Clothing</td><td>SUP-C</td></tr>
          </tbody>
        </table>
      </div>
      <p>Assume the table range is <code>A2:D100</code> with Product ID in column A and Supplier Name in column D. Which formula returns the Supplier Name?</p>
      <ul class="quiz-options">
        <li>A) <code>=VLOOKUP("PRD-015",A2:D100,2,FALSE)</code></li>
        <li>B) <code>=VLOOKUP("PRD-015",A2:D100,3,FALSE)</code></li>
        <li>C) <code>=VLOOKUP("PRD-015",A2:D100,4,FALSE)</code></li>
        <li>D) <code>=VLOOKUP("PRD-015",A2:D100,1,FALSE)</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> C) <code>=VLOOKUP("PRD-015",A2:D100,4,FALSE)</code></p>
        <p><strong>Explanation:</strong> Supplier Name is in the 4th column of the range; use column index 4 with exact match (FALSE).</p>
      </details>
    </div>

    <!-- Q5 -->
    <div class="quiz-card">
      <h3>Q5. COUNTIFS for Multiple Conditions</h3>
      <p>Count Electronics products that also need Reorder (Stock Status column I). Which formula?</p>
      <ul class="quiz-options">
        <li>A) <code>=COUNTIF(C2:C51,"Electronics")</code></li>
        <li>B) <code>=COUNTIF(I2:I51,"Reorder")</code></li>
        <li>C) <code>=COUNTIFS(C2:C51,"Electronics",I2:I51,"Reorder")</code></li>
        <li>D) <code>=COUNTIFS(I2:I51,"Reorder",C2:C51,"")</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> C) <code>=COUNTIFS(C2:C51,"Electronics",I2:I51,"Reorder")</code></p>
        <p><strong>Explanation:</strong> COUNTIFS applies AND logic across ranges; both category and status must match.</p>
      </details>
    </div>

    <!-- Q6 -->
    <div class="quiz-card">
      <h3>Q6. AVERAGEIF for Category Price</h3>
      <p>Average Unit Price for category in cell A10 (categories listed in C2:C51, prices in E2:E51). Which formula?</p>
      <ul class="quiz-options">
        <li>A) <code>=AVERAGE(E2:E51)</code></li>
        <li>B) <code>=AVERAGEIF(E2:E51,A10,C2:C51)</code></li>
        <li>C) <code>=AVERAGEIF(C2:C51,A10,E2:E51)</code></li>
        <li>D) <code>=AVERAGEIFS(E2:E51,C2:C51,A10)</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> C) <code>=AVERAGEIF(C2:C51,A10,E2:E51)</code></p>
        <p><strong>Explanation:</strong> AVERAGEIF(criteria_range, criteria, average_range) averages prices where category matches A10.</p>
      </details>
    </div>

    <!-- Q7 -->
    <div class="quiz-card">
      <h3>Q7. SUMPRODUCT for Category Value</h3>
      <p>Total inventory value for Electronics (Category in C, Unit Price in E, Quantity in F). Which formula?</p>
      <ul class="quiz-options">
        <li>A) <code>=SUMIF(C2:C51,"Electronics",E2:E51)</code></li>
        <li>B) <code>=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))</code></li>
        <li>C) <code>=SUM(E2:E51*F2:F51)</code></li>
        <li>D) <code>=SUMIFS(E2:E51,C2:C51,"Electronics",F2:F51,"Electronics")</code></li>
      </ul>
      <details class="quiz-answer">
        <summary>Show answer</summary>
        <p><strong>Answer:</strong> B) <code>=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))</code></p>
        <p><strong>Explanation:</strong> SUMPRODUCT multiplies price and quantity only for rows where category matches, then sums the results.</p>
      </details>
    </div>
  </div>
</section>
</div>