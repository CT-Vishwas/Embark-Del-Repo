#!/usr/bin/env python3
# Grouping tenant preferences

import pandas as pd

df = pd.read_csv("./data/house_rent.csv")
tenant_counts = {}

for preference in df["Tenant Preferred"]:
    tenant_counts[preference] = tenant_counts.get(preference, 0) + 1

for k,v in tenant_counts.items():
    print(f"{k}: {v} listings")