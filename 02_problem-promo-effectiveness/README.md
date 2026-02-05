# Promo Effectiveness Analysis

## 📌 Project Overview
This project analyzes casino promotional campaigns to evaluate marketing effectiveness across channels, campaigns, and properties.

The goal is to understand:
- Which campaigns generate the highest return
- Which channels perform best
- How budget reallocation could improve ROI

This analysis simulates real-world marketing performance data and applies SQL-based analytics to support business decision making.

---

## 📊 Dataset Description
Source data contains daily promotional activity with the following fields:

- promo_date
- property
- campaign
- channel
- promo_spend
- promo_revenue
- redemptions

The dataset includes intentional data quality issues such as missing days and inconsistent entries to simulate real operational environments.

---

## ⚙️ Tools & Technologies
- PostgreSQL
- DBeaver
- SQL (CTEs, Aggregations, Joins)
- Python (Data Generation)
- GitHub (Version Control)

---

## 🧹 Data Preparation & Quality Checks

### Missing Date Validation
A calendar table was generated using `generate_series` to identify missing promotional days.

Result:
- 245 missing promo days detected

### Row Validation
Row counts and date ranges were verified to ensure data integrity before analysis.

---

## 📈 Promo Performance Summary

Promotional performance was summarized by:

- Property
- Campaign
- Channel

Metrics calculated:
- Total Spend
- Total Revenue
- ROI
- Average Redemptions

A summary table (`p2_promo_summary`) was created to support performance evaluation.

---

## 🏆 Channel Performance Analysis

Channel-level performance:

| Channel | ROI |
|---------|-----|
| App     | 2.79 |
| Onsite  | 2.79 |
| SMS     | 2.77 |
| Email   | 2.71 |

Mobile App and Onsite campaigns delivered the highest returns.

---

## 💡 Budget Reallocation Simulation

A reallocation model was built to test shifting spend from lower-performing channels to higher-performing ones.

Scenarios tested:

| Reallocation % | Projected Gain |
|---------------|------------
