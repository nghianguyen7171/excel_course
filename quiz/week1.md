---
title: Week 1 Quiz - Excel Basics
layout: default
---

{::nomarkdown}
<div class="quiz-page">
<section id="week1-quiz" class="quiz-section">
  <div class="quiz-hero">
    <h1>Week 1's Quiz</h1>
    <p class="quiz-subtitle">Test your knowledge of basic formulas, conditional logic, and lookup functions.</p>
  </div>

  <form id="quiz-form" class="quiz-form">
  <div class="quiz-grid">
    <!-- Q1 -->
      <div class="quiz-card" data-question="1" data-correct="B">
      <h3>Q1. SUM & Multiplication</h3>
      <p>You need total revenue from a single-row record where Unit Price is in E2 and Quantity is in F2. Which formula is correct?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q1" value="A">
            <span>A) <code>=SUM(E2*F2)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q1" value="B">
            <span>B) <code>=E2*F2</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q1" value="C">
            <span>C) <code>=SUM(E2,F2)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q1" value="D">
            <span>D) <code>=SUM(E2:F2)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="1">Submit Answer</button>
        <div class="quiz-answer" id="answer-1" style="display: none;">
        <p><strong>Answer:</strong> B) <code>=E2*F2</code></p>
        <p><strong>Explanation:</strong> For a single row, multiply Unit Price by Quantity directly. SUM is unnecessary unless summing multiple rows.</p>
        </div>
    </div>

    <!-- Q2 -->
      <div class="quiz-card" data-question="2" data-correct="B">
      <h3>Q2. COUNT vs COUNTA</h3>
      <p>Column A has Product IDs (text) and blank cells. You want to count how many products are listed. Which function?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q2" value="A">
            <span>A) <code>=COUNT(A2:A100)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q2" value="B">
            <span>B) <code>=COUNTA(A2:A100)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q2" value="C">
            <span>C) <code>=COUNTIF(A2:A100,">0")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q2" value="D">
            <span>D) <code>=SUM(A2:A100)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="2">Submit Answer</button>
        <div class="quiz-answer" id="answer-2" style="display: none;">
        <p><strong>Answer:</strong> B) <code>=COUNTA(A2:A100)</code></p>
        <p><strong>Explanation:</strong> COUNTA counts non-empty cells, including text Product IDs; COUNT only counts numbers.</p>
        </div>
    </div>

    <!-- Q3 -->
      <div class="quiz-card" data-question="3" data-correct="B">
      <h3>Q3. IF for Stock Status</h3>
      <p>Quantity is in F2 and Reorder Level in G2. Which formula flags <em>Reorder</em> when stock is below the level?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q3" value="A">
            <span>A) <code>=IF(F2>G2,"Reorder","OK")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q3" value="B">
            <span>B) <code>=IF(F2<G2,"Reorder","OK")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q3" value="C">
            <span>C) <code>=IF(F2=G2,"Reorder","OK")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q3" value="D">
            <span>D) <code>=IF(G2-F2,"Reorder","OK")</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="3">Submit Answer</button>
        <div class="quiz-answer" id="answer-3" style="display: none;">
        <p><strong>Answer:</strong> B) <code>=IF(F2<G2,"Reorder","OK")</code></p>
        <p><strong>Explanation:</strong> Reorder is needed when Quantity (F2) is less than Reorder Level (G2).</p>
        </div>
    </div>

    <!-- Q4 (with table example) -->
      <div class="quiz-card" data-question="4" data-correct="C">
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
        <p>Assume the table range is <code>A2:D100</code> with Product ID in column A (1st column), Product Name in column B (2nd column), Category in column C (3rd column), and Supplier Name in column D (4th column). Which formula correctly returns the Supplier Name for Product ID "PRD-015"?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q4" value="A">
            <span>A) <code>=VLOOKUP("PRD-015",A2:D100,2,FALSE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q4" value="B">
            <span>B) <code>=VLOOKUP("PRD-015",A2:D100,3,FALSE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q4" value="C">
            <span>C) <code>=VLOOKUP("PRD-015",A2:D100,4,FALSE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q4" value="D">
            <span>D) <code>=VLOOKUP("PRD-015",A2:D100,1,FALSE)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="4">Submit Answer</button>
        <div class="quiz-answer" id="answer-4" style="display: none;">
        <p><strong>Answer:</strong> C) <code>=VLOOKUP("PRD-015",A2:D100,4,FALSE)</code></p>
        <p><strong>Explanation:</strong> Supplier Name is in the 4th column of the range; use column index 4 with exact match (FALSE).</p>
        </div>
    </div>

    <!-- Q5 -->
      <div class="quiz-card" data-question="5" data-correct="C">
      <h3>Q5. COUNTIFS for Multiple Conditions</h3>
      <p>Count Electronics products that also need Reorder (Stock Status column I). Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q5" value="A">
            <span>A) <code>=COUNTIF(C2:C51,"Electronics")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q5" value="B">
            <span>B) <code>=COUNTIF(I2:I51,"Reorder")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q5" value="C">
            <span>C) <code>=COUNTIFS(C2:C51,"Electronics",I2:I51,"Reorder")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q5" value="D">
            <span>D) <code>=COUNTIFS(I2:I51,"Reorder",C2:C51,"")</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="5">Submit Answer</button>
        <div class="quiz-answer" id="answer-5" style="display: none;">
        <p><strong>Answer:</strong> C) <code>=COUNTIFS(C2:C51,"Electronics",I2:I51,"Reorder")</code></p>
        <p><strong>Explanation:</strong> COUNTIFS applies AND logic across ranges; both category and status must match.</p>
        </div>
    </div>

    <!-- Q6 -->
      <div class="quiz-card" data-question="6" data-correct="C">
      <h3>Q6. AVERAGEIF for Category Price</h3>
      <p>Average Unit Price for category in cell A10 (categories listed in C2:C51, prices in E2:E51). Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q6" value="A">
            <span>A) <code>=AVERAGE(E2:E51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q6" value="B">
            <span>B) <code>=AVERAGEIF(E2:E51,A10,C2:C51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q6" value="C">
            <span>C) <code>=AVERAGEIF(C2:C51,A10,E2:E51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q6" value="D">
            <span>D) <code>=AVERAGEIFS(E2:E51,C2:C51,A10)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="6">Submit Answer</button>
        <div class="quiz-answer" id="answer-6" style="display: none;">
        <p><strong>Answer:</strong> C) <code>=AVERAGEIF(C2:C51,A10,E2:E51)</code></p>
        <p><strong>Explanation:</strong> AVERAGEIF(criteria_range, criteria, average_range) averages prices where category matches A10.</p>
        </div>
    </div>

    <!-- Q7 -->
      <div class="quiz-card" data-question="7" data-correct="B">
      <h3>Q7. SUMPRODUCT for Category Value</h3>
      <p>Total inventory value for Electronics (Category in C, Unit Price in E, Quantity in F). Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q7" value="A">
            <span>A) <code>=SUMIF(C2:C51,"Electronics",E2:E51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q7" value="B">
            <span>B) <code>=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q7" value="C">
            <span>C) <code>=SUM(E2:E51*F2:F51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q7" value="D">
            <span>D) <code>=SUMIFS(E2:E51,C2:C51,"Electronics",F2:F51,"Electronics")</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="7">Submit Answer</button>
        <div class="quiz-answer" id="answer-7" style="display: none;">
        <p><strong>Answer:</strong> B) <code>=SUMPRODUCT((C2:C51="Electronics")*(E2:E51)*(F2:F51))</code></p>
        <p><strong>Explanation:</strong> SUMPRODUCT multiplies price and quantity only for rows where category matches, then sums the results.</p>
        </div>
      </div>

      <!-- Q8 -->
      <div class="quiz-card" data-question="8" data-correct="D">
        <h3>Q8. MIN and MAX Functions</h3>
        <p>You want to find the lowest unit price in range E2:E51. Which formula is correct?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q8" value="A">
            <span>A) <code>=MINIMUM(E2:E51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q8" value="B">
            <span>B) <code>=MIN(E2:E51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q8" value="C">
            <span>C) <code>=SMALL(E2:E51,1)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q8" value="D">
            <span>D) Both B and C are correct</span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="8">Submit Answer</button>
        <div class="quiz-answer" id="answer-8" style="display: none;">
          <p><strong>Answer:</strong> D) Both B and C are correct</p>
          <p><strong>Explanation:</strong> MIN(E2:E51) and SMALL(E2:E51,1) both return the minimum value. MIN is more straightforward for this purpose.</p>
        </div>
      </div>

      <!-- Q9 -->
      <div class="quiz-card" data-question="9" data-correct="A">
        <h3>Q9. SUMIF Function</h3>
        <p>Sum all quantities (F2:F51) where the category (C2:C51) is "Electronics". Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q9" value="A">
            <span>A) <code>=SUMIF(C2:C51,"Electronics",F2:F51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q9" value="B">
            <span>B) <code>=SUMIF(F2:F51,C2:C51,"Electronics")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q9" value="C">
            <span>C) <code>=SUMIF(C2:C51,F2:F51,"Electronics")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q9" value="D">
            <span>D) <code>=SUMIF("Electronics",C2:C51,F2:F51)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="9">Submit Answer</button>
        <div class="quiz-answer" id="answer-9" style="display: none;">
          <p><strong>Answer:</strong> A) <code>=SUMIF(C2:C51,"Electronics",F2:F51)</code></p>
          <p><strong>Explanation:</strong> SUMIF syntax is SUMIF(criteria_range, criteria, sum_range). The criteria range comes first, then the criteria, then the range to sum.</p>
        </div>
      </div>

      <!-- Q10 -->
      <div class="quiz-card" data-question="10" data-correct="A">
        <h3>Q10. Nested IF Function</h3>
        <p>Create a formula that returns "High" if quantity (F2) > 100, "Medium" if > 50, otherwise "Low". Which is correct?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q10" value="A">
            <span>A) <code>=IF(F2>100,"High",IF(F2>50,"Medium","Low"))</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q10" value="B">
            <span>B) <code>=IF(F2>50,"Medium",IF(F2>100,"High","Low"))</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q10" value="C">
            <span>C) <code>=IF(F2>100,"High","Medium",IF(F2>50,"Low"))</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q10" value="D">
            <span>D) <code>=IF(F2>50,"Low",IF(F2>100,"High","Medium"))</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="10">Submit Answer</button>
        <div class="quiz-answer" id="answer-10" style="display: none;">
          <p><strong>Answer:</strong> A) <code>=IF(F2>100,"High",IF(F2>50,"Medium","Low"))</code></p>
          <p><strong>Explanation:</strong> Check the highest threshold first (100), then the next (50), then default to "Low". Order matters in nested IF statements.</p>
        </div>
      </div>

      <!-- Q11 -->
      <div class="quiz-card" data-question="11" data-correct="B">
        <h3>Q11. Absolute Cell Reference</h3>
        <p>You want to copy a formula from B2 that multiplies A2 by a tax rate in cell $C$1. Which formula in B2 ensures C1 stays fixed when copied down?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q11" value="A">
            <span>A) <code>=A2*C1</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q11" value="B">
            <span>B) <code>=A2*$C$1</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q11" value="C">
            <span>C) <code>=A2*$C1</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q11" value="D">
            <span>D) <code>=$A$2*C1</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="11">Submit Answer</button>
        <div class="quiz-answer" id="answer-11" style="display: none;">
          <p><strong>Answer:</strong> B) <code>=A2*$C$1</code></p>
          <p><strong>Explanation:</strong> $C$1 is an absolute reference that locks both row and column, so it won't change when copied. A2 is relative and will adjust.</p>
        </div>
      </div>

      <!-- Q12 -->
      <div class="quiz-card" data-question="12" data-correct="B">
        <h3>Q12. COUNTIF with Wildcards</h3>
        <p>Count products in C2:C51 where the category name starts with "Elect". Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q12" value="A">
            <span>A) <code>=COUNTIF(C2:C51,"Elect")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q12" value="B">
            <span>B) <code>=COUNTIF(C2:C51,"Elect*")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q12" value="C">
            <span>C) <code>=COUNTIF(C2:C51,"*Elect")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q12" value="D">
            <span>D) <code>=COUNTIF(C2:C51,"Electronics")</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="12">Submit Answer</button>
        <div class="quiz-answer" id="answer-12" style="display: none;">
          <p><strong>Answer:</strong> B) <code>=COUNTIF(C2:C51,"Elect*")</code></p>
          <p><strong>Explanation:</strong> The asterisk (*) is a wildcard that matches any characters. "Elect*" matches any text starting with "Elect".</p>
        </div>
      </div>

      <!-- Q13 -->
      <div class="quiz-card" data-question="13" data-correct="B">
        <h3>Q13. VLOOKUP Approximate Match</h3>
        <p>You have a lookup table with discount thresholds. For a purchase amount in A10, you want to find the discount rate using approximate match. The lookup table is in E2:F5 (amounts in E, rates in F), sorted ascending. Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q13" value="A">
            <span>A) <code>=VLOOKUP(A10,E2:F5,2,FALSE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q13" value="B">
            <span>B) <code>=VLOOKUP(A10,E2:F5,2,TRUE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q13" value="C">
            <span>C) <code>=VLOOKUP(A10,E2:F5,1,TRUE)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q13" value="D">
            <span>D) <code>=VLOOKUP(A10,F2:E5,2,TRUE)</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="13">Submit Answer</button>
        <div class="quiz-answer" id="answer-13" style="display: none;">
          <p><strong>Answer:</strong> B) <code>=VLOOKUP(A10,E2:F5,2,TRUE)</code></p>
          <p><strong>Explanation:</strong> TRUE enables approximate match (or omit it). Column index 2 returns the discount rate. The table must be sorted ascending for approximate match to work correctly.</p>
        </div>
      </div>

      <!-- Q14 -->
      <div class="quiz-card" data-question="14" data-correct="D">
        <h3>Q14. SUMIFS with Multiple Criteria</h3>
        <p>Sum quantities (F2:F51) where category (C2:C51) is "Electronics" AND unit price (E2:E51) is greater than 50. Which formula?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q14" value="A">
            <span>A) <code>=SUMIFS(F2:F51,C2:C51,"Electronics",E2:E51,">50")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q14" value="B">
            <span>B) <code>=SUMIFS(F2:F51,E2:E51,">50",C2:C51,"Electronics")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q14" value="C">
            <span>C) <code>=SUMIF(C2:C51,"Electronics",F2:F51)*SUMIF(E2:E51,">50",F2:F51)</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q14" value="D">
            <span>D) Both A and B are correct</span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="14">Submit Answer</button>
        <div class="quiz-answer" id="answer-14" style="display: none;">
          <p><strong>Answer:</strong> D) Both A and B are correct</p>
          <p><strong>Explanation:</strong> SUMIFS applies AND logic to all criteria. The order of criteria pairs doesn't matter, as long as each pair is (criteria_range, criteria).</p>
        </div>
      </div>

      <!-- Q15 -->
      <div class="quiz-card" data-question="15" data-correct="A">
        <h3>Q15. VLOOKUP Error Handling</h3>
        <p>You use VLOOKUP to find a product, but some product IDs don't exist. You want to show "Not Found" instead of #N/A. Which formula wraps the VLOOKUP?</p>
        <div class="quiz-options">
          <label class="quiz-option">
            <input type="radio" name="q15" value="A">
            <span>A) <code>=IFERROR(VLOOKUP(A2,D2:E100,2,FALSE),"Not Found")</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q15" value="B">
            <span>B) <code>=IF(VLOOKUP(A2,D2:E100,2,FALSE)="#N/A","Not Found",VLOOKUP(A2,D2:E100,2,FALSE))</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q15" value="C">
            <span>C) <code>=VLOOKUP(A2,D2:E100,2,FALSE) OR "Not Found"</code></span>
          </label>
          <label class="quiz-option">
            <input type="radio" name="q15" value="D">
            <span>D) <code>=ERROR(VLOOKUP(A2,D2:E100,2,FALSE),"Not Found")</code></span>
          </label>
        </div>
        <button type="button" class="quiz-submit-btn" data-question="15">Submit Answer</button>
        <div class="quiz-answer" id="answer-15" style="display: none;">
          <p><strong>Answer:</strong> A) <code>=IFERROR(VLOOKUP(A2,D2:E100,2,FALSE),"Not Found")</code></p>
          <p><strong>Explanation:</strong> IFERROR catches any error (including #N/A) and returns the specified value. This is cleaner than checking for specific error types.</p>
        </div>
      </div>
    </div>
  </form>
</section>
</div>
{:/nomarkdown}
