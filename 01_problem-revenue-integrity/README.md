# Project 1 — Revenue Integrity & Performance Analysis (Hospitality/Casino)

## Overview
This project analyzes Q4 2025 multi-department revenue performance for a hospitality and casino operation using a structured analytics workflow built in Python and Power BI.

The objective was to validate revenue integrity, identify operational risks, analyze performance trends, and deliver management-ready reporting and recommendations.

---

## Business Problem
Daily revenue reporting is vulnerable to missing data, late adjustments, and unexpected spikes or drops. This project builds a repeatable process to validate daily revenue, flag anomalies, and produce reliable management reporting.

---

## Key Questions
1. Are there missing dates or missing departments?
2. Do totals reconcile between source systems and reporting tables?
3. Which days show unusual spikes or drops compared to normal patterns?
4. What is the most likely operational reason behind each exception?
5. How can reporting accuracy and performance monitoring be improved?

---

## Success Metrics
- 100% date coverage (no missing days)
- Automated exception flags
- Reduced duplicate and invalid records
- Clear documentation for management review
- Executive-ready dashboard

---

## Executive Summary
This project reviews Q4 2025 revenue performance across key departments using a custom analytics workflow built in Python and Power BI.

I began by analyzing raw transaction data that included common real-world issues such as duplicate records, missing entries, and negative revenue values. These issues were identified, reviewed, and corrected to create a clean, reliable reporting dataset.

Using this validated data, I developed an executive dashboard to track total revenue, transaction volume, department performance, and revenue trends over time. Slot operations consistently produced the highest revenue, followed by table games and hospitality services.

Revenue remained steady throughout most of the quarter, with predictable increases on weekends and during promotional periods. A notable spike in late December aligned with expected seasonal demand.

By implementing data quality controls, reporting discrepancies were reduced by approximately 1%, improving confidence in financial reporting and supporting more accurate performance evaluation.

---

## Revenue Performance Insights
I analyzed revenue trends across all departments from October through December 2025 to understand performance patterns, seasonality, and operational drivers.

Slot operations were the primary revenue driver throughout the quarter, followed by table games. Hotel, food and beverage, and retail operations provided stable supporting revenue.

Revenue increased during weekends and promotional periods, particularly in November and December. Performance remained stable through most of the quarter, with stronger growth entering the holiday season.

Average daily revenue showed limited volatility, supporting reliable short-term forecasting and operational planning.

---

## Data Integrity & Risk Findings
The raw dataset contained several integrity issues, including duplicate records, missing departmental reporting days, and negative revenue values caused by system adjustments or feed errors.

A duplicate load in mid-November resulted in overstated revenue and distorted trend analysis. These records were isolated and removed.

Missing reporting days within hotel and food and beverage departments reduced visibility into operational performance.

One instance of negative revenue was identified and corrected to ensure accurate net reporting.

After implementing validation rules and exception handling, inaccurate records were reduced by approximately 1%.

---

## Business Recommendations
- Implement automated validation checks at data ingestion
- Establish standardized exception reporting
- Prioritize investment in high-performing departments
- Optimize hospitality and retail margins
- Adopt the executive dashboard for recurring management review

These actions support stronger financial controls and improved operational focus.

---

## Financial Impact Estimate
Data validation reduced inaccurate reporting by approximately 1%, preventing potential misstatements of tens of thousands of dollars per quarter.

Improved performance visibility supports incremental revenue gains of 1–3% through better resource allocation and promotional targeting.

Standardized monitoring reduces manual reconciliation time by an estimated 5–10 hours per month.

Overall, the project delivers measurable value through improved accuracy, efficiency, and risk reduction.

---

## Duplicate Revenue Records Detected & Resolved

### Issue Identified
Duplicate records were found for specific combinations of revenue date, property, and department.

### Impact
- Raw table row count: 459  
- Clean table row count: 454  
- Total duplicates removed: 5  

Duplicates occurred on **2025-11-16** across multiple departments.

### Resolution
- Identified duplicates using validation logic
- Created a clean reporting dataset
- Logged issues for audit tracking

### Evidence
See `outputs/p1_duplicate_flags.png`

---

## Deliverables
- Python data generation and validation pipeline
- Cleaned and validated CSV datasets
- Power BI executive dashboard
- Data integrity documentation
- Executive case study report

---

## Tools & Technologies
- Python (Pandas, NumPy)
- Power BI Desktop
- DAX
- Power Query
- Git
- GitHub

---

## Project Files
- `make_p1_dataset.py` — Data generation and cleaning
- `outputs/clean_revenue_data.csv` — Validated dataset
- `outputs/revenue_integrity_dashboard.pbix` — Power BI dashboard
- `outputs/p1_duplicate_flags.png` — Duplicate evidence

---

## Dashboard Preview
_Add screenshot to: outputs/screenshots/dashboard.png_
portfolio-data-analytics>
