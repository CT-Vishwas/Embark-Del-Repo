#!/usr/bin/env python3
# Rent Trend per month
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/house_rent.csv")
df["Posted On"] = pd.to_datetime(df["Posted On"], errors="coerce")

df["Month"] = df["Posted On"].dt.to_period("M")

monthly_average_rent = df.groupby(["City", "Month"])["Rent"].mean().reset_index()
print(monthly_average_rent)

pivot_data = monthly_average_rent.pivot(index="Month", columns="City", values="Rent")
plt.figure(figsize=(12,6))
for city in pivot_data.columns:
    plt.plot(pivot_data.index.astype(str), pivot_data[city], marker='o', label=city)

plt.xticks(rotation=45)
plt.title("Average Rent Trend Per Month by City")
plt.xlabel("Month")
plt.ylabel("Average Rent")
plt.legend()
plt.grid(True)
plt.show()