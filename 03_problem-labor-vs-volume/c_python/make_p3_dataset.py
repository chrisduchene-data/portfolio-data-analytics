import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

# Project 3: Labor vs Volume Analysis
# Simulated Q4 2025 operating data

dates = pd.date_range(start="2025-10-01", end="2025-12-31")
departments = ["Slots", "Tables", "Hotel", "F&B"]

rows = []

for date in dates:
    for department in departments:
        volume = np.random.randint(800, 2000)
        labor_hours = volume / np.random.uniform(8, 15)
        avg_hourly_rate = np.random.uniform(18, 35)
        labor_cost = labor_hours * avg_hourly_rate

        rows.append([
            date.date(),
            department,
            volume,
            round(labor_hours, 2),
            round(avg_hourly_rate, 2),
            round(labor_cost, 2)
        ])

df = pd.DataFrame(rows, columns=[
    "work_date",
    "department",
    "volume",
    "labor_hours",
    "avg_hourly_rate",
    "labor_cost"
])

# Save to data_raw folder
base_dir = Path(__file__).resolve().parent.parent
output_path = base_dir / "data_raw" / "p3_labor_volume_raw.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Dataset created successfully: {output_path}")
print(f"Rows created: {len(df)}")