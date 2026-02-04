# Project 1 — Revenue Integrity & Reconciliation (Hospitality/Casino)

## Business Problem
Daily revenue reporting is vulnerable to missing data, late adjustments, and unexpected spikes/drops. This project builds a repeatable process to validate daily revenue, flag anomalies, and produce a management-ready exception report.

## Key Questions
1. Are there missing dates or missing departments?
2. Do totals reconcile between source systems and reporting tables?
3. Which days show unusual spikes/drops compared to normal patterns?
4. What is the most likely operational reason behind each exception?

## Success Metrics
- 100% date coverage (no missing days)
- Automated exception flags (no manual hunting)
- Clear “why it happened” notes for management review

## Deliverables
- SQL QA checks (missing days, duplicates, invalid values)
- Power BI exception dashboard
- Python anomaly detection + summary
- 1-page executive decision memo

## Duplicate Revenue Records Detected & Resolved

### Issue Identified
During data validation, duplicate records were found for specific combinations of revenue date, property, and department.

### Impact
- Raw table row count: 459  
- Clean table row count: 454  
- Total duplicates removed: 5  

Duplicates occurred on **2025-11-16** across multiple departments.

### Resolution
- Identified duplicates using GROUP BY + HAVING COUNT(*) > 1
- Created a clean table using DISTINCT
- Logged issues in `p1_qa_flags` for audit tracking

### Evidence
See `outputs/p1_duplicate_flags.png`
