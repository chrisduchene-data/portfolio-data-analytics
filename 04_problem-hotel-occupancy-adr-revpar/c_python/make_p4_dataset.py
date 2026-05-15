import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=180)
hotels = ["Hotel A", "Hotel B", "Hotel C"]

data = []

for date in dates:
    for hotel in hotels:
        rooms_available = np.random.randint(180, 250)
        occupancy_rate = np.random.uniform(0.6, 0.95)
        rooms_sold = int(rooms_available * occupancy_rate)
        
        adr = np.random.uniform(120, 300)
        room_revenue = rooms_sold * adr
        
        data.append([
            date,
            hotel,
            rooms_available,
            rooms_sold,
            adr,
            room_revenue
        ])

df = pd.DataFrame(data, columns=[
    "date",
    "hotel",
    "rooms_available",
    "rooms_sold",
    "average_daily_rate",
    "room_revenue"
])

df.to_csv("p4_hotel_raw.csv", index=False)

print("Dataset created: p4_hotel_raw.csv")



