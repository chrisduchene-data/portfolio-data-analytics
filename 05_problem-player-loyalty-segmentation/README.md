# Player Loyalty Segmentation Dashboard

## Business Problem

Casino and hospitality organizations rely heavily on player loyalty programs to understand customer behavior, maximize gaming revenue, and improve player retention. Leadership teams need visibility into which player segments generate the highest value, how frequently players visit, and which geographic markets contribute the most revenue.

This project simulates a player loyalty analytics environment using SQL, Python, and Power BI to analyze customer segmentation and behavioral trends.

---

## Objective

The objective of this project was to:

- Analyze player loyalty tiers and revenue contribution
- Identify behavioral differences across player segments
- Measure visit frequency versus gaming value
- Evaluate geographic revenue distribution by state
- Build an executive-level dashboard for operational decision-making

---

## Key Business Questions

- Which loyalty tier generates the highest gaming revenue?
- Which player segments visit most frequently?
- Which geographic regions produce the strongest player value?
- Is visit frequency correlated with gaming revenue?
- How can leadership identify high-value VIP segments?
---

## Tools Used

- PostgreSQL
- DBeaver
- Python
- Pandas
- Faker
- Power BI
- DAX
- Git & GitHub

---

## Dataset Overview

The dataset simulates casino player loyalty activity and includes:

- Player ID
- Loyalty Tier
- State
- Visit Frequency
- Theoretical Win
- Actual Win
- Age Demographics

The synthetic dataset was generated using Python and loaded into PostgreSQL for SQL analysis and dashboard reporting.

---

## Key Metrics

- Total Players
- Total Actual Win
- Average Visits
- Average Theoretical Win

---

## Dashboard Features

### KPI Cards
Executive summary metrics for player value and engagement.

### Revenue by Loyalty Tier
Comparison of gaming revenue contribution across Bronze, Silver, Gold, and Platinum players.

### Player Visits by Tier
Analysis of customer engagement and visit frequency by loyalty segment.

### Revenue by State
Geographic comparison of player revenue contribution.

### Player Value vs Visit Frequency Scatterplot
Behavioral segmentation visual comparing player visit frequency against gaming value.

### Interactive State Slicer
Allows dashboard users to dynamically filter analytics by geographic market.

---

## Business Insights

- Bronze tier players generated the highest total gaming revenue due to larger population size.
- Higher loyalty tiers demonstrated strong average player value despite smaller customer counts.
- Visit frequency showed a positive relationship with player revenue contribution.
- Several geographic markets consistently outperformed others in gaming revenue generation.
- Scatterplot analysis revealed high-value player clusters useful for VIP targeting strategies.

---

## Screenshots

### Dashboard Overview

![Dashboard Screenshot](../outputs/p5_player_loyalty_dashboard.png)

---

## Files Included

### SQL
- `p5_create_table.sql`
- `p5_loyalty_analysis.sql`

### Python
- `make_p5_dataset.py`

### Power BI
- `p5_player_loyalty_dashboard.pbix`

### Dataset
- `p5_player_loyalty_raw.csv`

---

## Project Skills Demonstrated

- SQL aggregation and segmentation analysis
- Data modeling and synthetic dataset generation
- Power BI dashboard development
- DAX measure creation
- Business intelligence reporting
- Data visualization and storytelling
- GitHub project documentation
