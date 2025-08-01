#!/usr/bin/env python3
# Groupby furnishing status

import pandas as pd
from itertools import groupby

df = pd.read_csv("./data/house_rent.csv")
df_sorted = df.sort_values("Furnishing Status")

grouped_houses = groupby(df_sorted.to_dict("records"), key=lambda x: x["Furnishing Status"])

for furnishing_status, houses in grouped_houses:
    house_list = list(houses)
    print(f"{furnishing_status}: {len(house_list)} listings")