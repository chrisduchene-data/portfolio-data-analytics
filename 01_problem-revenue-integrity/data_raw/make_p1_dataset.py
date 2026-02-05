import pandas as pd
import numpy as np
from datetime import date

np.random.seed(7)

dates = pd.date_range(date(2025, 10, 1), date(2025, 12, 31), freq="D")
properties = ["RW_NYC"]
departments = ["slots", "tables", "hotel", "fnb", "retail"]

rows = []
for d in dates:
    dow = d.dayofweek  # 0=Mon
    weekend_boost = 1.25 if dow >= 4 else 1.0

    for prop in properties:
        for dept in departments:
            base = {
                "slots": 450000,
                "tables": 180000,
                "hotel": 120000,
                "fnb": 80000,
                "retail": 25000
            }[dept]

            noise = np.random.normal(0, base * 0.08)
            gross = max(0, (base * weekend_boost) + noise)

            promo = 0.0
            # Promo weekends in November
            if d.month == 11 and d.day in [8, 9, 15, 16, 22, 23]:
                promo = gross * np.random.uniform(0.03, 0.08)

            net = gross - promo
            tx = int(max(1, np.random.normal(1000 if dept in ["slots", "fnb"] else 300, 60)))

            source = {
                "slots": "slots_system",
                "tables": "table_system",
                "hotel": "hotel_pms",
                "fnb": "pos",
                "retail": "pos"
            }[dept]

            rows.append([d.date(), prop, dept, round(gross, 2), round(promo, 2), round(net, 2), tx, source])

df = pd.DataFrame(rows, columns=[
    "revenue_date", "property", "department", "gross_revenue", "promo_cost", "net_revenue", "transactions", "source_system"
])

# Inject realistic mess:
# 1) Missing days for hotel/fnb
missing_days = [date(2025, 10, 14), date(2025, 11, 3), date(2025, 12, 7)]
df = df[~((df["revenue_date"].isin(missing_days)) & (df["department"].isin(["hotel", "fnb"])))]

# 2) Duplicate a day (double-load)
dup_day = date(2025, 11, 16)
df = pd.concat([df, df[df["revenue_date"] == dup_day]], ignore_index=True)

# 3) One negative value (bad feed / adjustment)
bad_row_idx = df.sample(1, random_state=12).index[0]
df.loc[bad_row_idx, "gross_revenue"] = -abs(df.loc[bad_row_idx, "gross_revenue"])
df.loc[bad_row_idx, "net_revenue"] = df.loc[bad_row_idx, "gross_revenue"] - df.loc[bad_row_idx, "promo_cost"]

# 4) Big spike in slots (event day)
spike_day = date(2025, 12, 20)
mask = (df["revenue_date"] == spike_day) & (df["department"] == "slots")
df.loc[mask, "gross_revenue"] *= 1.75
df.loc[mask, "net_revenue"] = df.loc[mask, "gross_revenue"] - df.loc[mask, "promo_cost"]

out = "p1_daily_revenue_raw.csv"
df.to_csv(out, index=False)
print(f"Saved: {out} | rows={len(df)}")





