#!/usr/bin/env python3
import pandas as pd
from functools import reduce

df = pd.read_csv("./data/house_rent.csv")
# print(df.head())

# Calculate Total Rent for kolkata
city = "Kolkata"
city_rents = df[df["City"] == city]["Rent"]
print(city_rents.head())

# Calculate the total rent 
total_rent = reduce(lambda x,y: x+y, city_rents)
print(f"Total rent for {city}: {total_rent}")