import pandas as pd
import numpy as np
from datetime import date
import random
from pathlib import Path

# -------------------------
# Reproducibility
# -------------------------
random.seed(7)
np.random.seed(7)

# -------------------------
# Date range + dimensions
# -------------------------
start = date(2025, 9, 1)
end   = date(2025, 12, 31)
dates = pd.date_range(start, end, freq="D")

properties = ["RW_NYC"]
campaigns  = ["Fall Bonus", "Holiday Boost", "VIP Reload", "Slots Frenzy"]
channels   = ["Email", "SMS", "App", "Onsite"]

rows = []

for d in dates:
    dow = d.dayofweek
    weekend_boost = 1.15 if dow >= 4 else 1.0

    for prop in properties:
        for camp in campaigns:
            for ch in channels:
                # Spend varies by channel
                base_spend = {
                    "Email": 900,
                    "SMS": 1200,
                    "App": 1600,
                    "Onsite": 1800
                }[ch]

                spend = max(0, np.random.normal(base_spend, base_spend * 0.35))
                spend = round(spend * weekend_boost, 2)

                # Redemptions loosely tied to spend + channel
                base_red = {"Email": 120, "SMS": 170, "App": 220, "Onsite": 240}[ch]
                redemptions = int(max(1, np.random.normal(base_red, 60)))

                # Revenue tied to spend, but with noise (ROI varies a bit)
                roi = np.random.uniform(1.6, 3.8)
                revenue = round(spend * roi, 2)

                rows.append([d.date(), prop, camp, ch, spend, redemptions, revenue])

df = pd.DataFrame(rows, columns=[
    "promo_date", "property", "campaign", "channel",
    "promo_spend", "redemptions", "promo_revenue"
])

# -------------------------
# Inject realistic data issues
# -------------------------

# 1) Duplicate day (simulate double-load)
dup_day = date(2025, 11, 15)
df = pd.concat([df, df[df["promo_date"] == dup_day]], ignore_index=True)

# 2) Missing days (simulate missing feed)
missing_days = [date(2025, 10, 10), date(2025, 12, 5)]
df = df[~df["promo_date"].isin(missing_days)].copy()

# 3) Negative spend (bad record)
bad_idx = df.sample(1, random_state=22).index[0]
df.loc[bad_idx, "promo_spend"] = -abs(df.loc[bad_idx, "promo_spend"])
df.loc[bad_idx, "promo_revenue"] = round(df.loc[bad_idx, "promo_spend"] * np.random.uniform(1.6, 3.8), 2)

# 4) Revenue spike (event day)
spike_day = date(2025, 12, 20)
df.loc[df["promo_date"] == spike_day, "promo_revenue"] *= 2.5
df["promo_revenue"] = df["promo_revenue"].round(2)

# -------------------------
# Create QA flags + clean dataset
# -------------------------
raw = df.copy()

# Identify exact duplicate rows
key_cols = ["promo_date", "property", "campaign", "channel", "promo_spend", "redemptions", "promo_revenue"]
raw["is_duplicate_row"] = np.where(raw.duplicated(subset=key_cols, keep="first"), "Yes", "No")

# Negative spend flag
raw["is_negative_spend"] = np.where(raw["promo_spend"] < 0, "Yes", "No")

# Clean rules:
# - Fix negative spend -> set to 0 and recompute revenue to 0 (conservative)
# - Drop exact duplicates
clean = raw.copy()
neg_mask = clean["promo_spend"] < 0
clean.loc[neg_mask, "promo_spend"] = 0
clean.loc[neg_mask, "promo_revenue"] = 0
clean = clean.drop_duplicates(subset=key_cols).copy()

# Add calculated metrics for BI/SQL convenience
clean["roi"] = np.where(clean["promo_spend"] > 0, clean["promo_revenue"] / clean["promo_spend"], np.nan)
clean["roi"] = clean["roi"].round(4)

# -------------------------
# Save outputs (paths relative to this script)
# -------------------------
base_dir = Path(__file__).resolve().parent.parent  # 02_problem-promo-effectiveness/
raw_path   = base_dir / "data_raw" / "p2_promo_raw.csv"
clean_path = base_dir / "data_clean" / "p2_promo_clean.csv"
flags_path = base_dir / "outputs" / "p2_qa_flags.csv"

raw_path.parent.mkdir(parents=True, exist_ok=True)
clean_path.parent.mkdir(parents=True, exist_ok=True)
flags_path.parent.mkdir(parents=True, exist_ok=True)

raw.to_csv(raw_path, index=False)
clean.to_csv(clean_path, index=False)

# Keep only rows that were flagged for quick review
flags = raw[(raw["is_duplicate_row"] == "Yes") | (raw["is_negative_spend"] == "Yes")].copy()
flags.to_csv(flags_path, index=False)

print(f"Saved RAW:   {raw_path}   | rows={len(raw)}")
print(f"Saved CLEAN: {clean_path} | rows={len(clean)}")
print(f"Saved FLAGS: {flags_path} | rows={len(flags)}")
