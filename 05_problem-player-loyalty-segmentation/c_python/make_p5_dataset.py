import pandas as pd
import numpy as np
from faker import Faker
import random
from pathlib import Path

fake = Faker()

np.random.seed(42)
random.seed(42)

# -----------------------------
# Generate Fake Player Data
# -----------------------------

player_ids = range(1001, 1301)

tiers = ["Bronze", "Silver", "Gold", "Platinum"]

data = []

for player_id in player_ids:

    visits = np.random.randint(1, 60)

    theo_win = round(np.random.uniform(100, 25000), 2)

    actual_win = round(theo_win * np.random.uniform(0.7, 1.3), 2)

    tier = random.choices(
        tiers,
        weights=[40, 30, 20, 10],
        k=1
    )[0]

    age = np.random.randint(21, 80)

    state = random.choice([
        "NY", "NJ", "CT", "PA", "FL",
        "CA", "MA", "TX"
    ])

    data.append([
        player_id,
        fake.name(),
        age,
        state,
        visits,
        theo_win,
        actual_win,
        tier
    ])

# -----------------------------
# Create DataFrame
# -----------------------------

columns = [
    "player_id",
    "player_name",
    "age",
    "state",
    "visits",
    "theoretical_win",
    "actual_win",
    "loyalty_tier"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# Export CSV
# -----------------------------

output_path = Path("../data_raw/p5_player_loyalty_raw.csv")

df.to_csv(output_path, index=False)

print("P5 dataset created successfully.")
