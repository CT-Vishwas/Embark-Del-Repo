#!/usr/bin/env python3
# Grouping tenant preferences

import pandas as pd
from collections import defaultdict

df = pd.read_csv("./data/house_rent.csv")
# Approach 1
# tenant_counts = {}

# for preference in df["Tenant Preferred"]:
#     tenant_counts[preference] = tenant_counts.get(preference, 0) + 1

# for k,v in tenant_counts.items():
#     print(f"{k}: {v} listings")

# Approach 2
tenant_counts = defaultdict(int)

for preference in df["Tenant Preferred"]:
    tenant_counts[preference] += 1

print(dict(tenant_counts))