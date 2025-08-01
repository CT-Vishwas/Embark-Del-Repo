#!/usr/bin/env python3

import pandas as pd
from collections import Counter

df = pd.read_csv("./data/house_rent.csv")
localitites = df["Area Locality"]

locality_counts = Counter(localitites)

top_10_localities = locality_counts.most_common(10)

for i, (locality, count) in enumerate(top_10_localities, 1):
    print(f"{i}. {locality} - {count} listings")