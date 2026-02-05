import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

# Date range
start = date(2025, 9, 1)
end = date(2025, 12, 31)

dates = pd.date_range(start, end)

properties = ["RW_NYC"]
campaigns = ["Fall Bonus", "Holiday Boost", "VIP Reload", "Slots Frenzy"]
channels = ["Email", "SMS", "App", "Onsite"]

rows = []

for d in dates:
    for camp in campaigns:
        spend = round(random.uniform(500, 5000), 2)
        redemptions = random.randint(50, 500)
        revenue = round(spend * random.uniform(1.5, 4.0), 2)

        rows.append([
            d.date(),
            random.choice(properties),
            camp,
            random.choice(channels),
            spend,
            redemptions,
            revenue
        ])

df = pd.DataFrame(rows, columns=[
    "promo_date",
    "property",
    "campaign",
    "channel",
    "promo_spend",
    "redemptions",
    "promo_revenue"
])

# Inject problems

# 1. Duplicate day
dup_day = date(2025, 11, 15)
df = pd.concat([df, df[df["promo_date"] == dup_day]])

# 2. Missing days
missing = [date(2025, 10, 10), date(2025, 12, 5)]
df = df[~df["promo_date"].isin(missing)]

# 3. Negative spend
bad_idx = df.sample(1, random_state=22).index[0]
df.loc[bad_idx, "promo_spend"] = -abs(df.loc[bad_idx, "promo_spend"])

# 4. Revenue spike
spike_day = date(2025, 12, 20)
mask = df["promo_date"] == spike_day
df.loc[mask, "promo_revenue"] *= 2.5

# Save
out = "../data_raw/p2_promo_raw.csv"
df.to_csv(out, index=False)

print(f"Saved: {out} | rows={len(df)}")



