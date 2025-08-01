#!/usr/bin/env python3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


df = pd.read_csv("./data/house_rent.csv")

# Calculate Average rent per city
avg_rent_per_city = df.groupby("City")["Rent"].mean().to_dict()
print(avg_rent_per_city)

g = nx.Graph()

for city, avg_rent in avg_rent_per_city.items():
    g.add_node(city, avg_rent=avg_rent)

cities = list(avg_rent_per_city.keys())
for city1, city2 in combinations(cities,2):
    rent_diff = abs(avg_rent_per_city[city1] - avg_rent_per_city[city2])
    g.add_edge(city1, city2, weight=rent_diff)

pos = nx.spring_layout(g)
weights = [g[u][v]['weight'] for u,v in g.edges()]

plt.figure(figsize=(8,6))

nx.draw(
    g, pos, with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=10,
    width=[w/1000 for w in weights]
)

edge_labels = {(u,v): f'{w:.0f}' for u,v,w in g.edges(data="weight")}
nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)

plt.title("City Connectivity based on rent difference")
plt.show()