#!/usr/bin/env python3
# Using Heapq to find top 10 expensive rentals

import pandas as pd
import heapq

df = pd.read_csv("./data/house_rent.csv")

df["Rent"] = pd.to_numeric(df["Rent"],errors="coerce")

top_10_expensive = heapq.nlargest(
    10,
    df.to_dict('records'),
    key=lambda x: x["Rent"]
)

for i, house in enumerate(top_10_expensive, 1):
    print(f"{i}. City: {house['City']}, Area: {house['Area Locality']}, Rent: {house['Rent']}")