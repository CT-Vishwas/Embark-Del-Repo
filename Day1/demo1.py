#!/usr/bin/env python3
# Script to Clean Data using List Comprehensions

raw_prices = ["$23.5", "   67.9", "45.3USD", "89.95INR","90.5EUR"]

cleaned_prices = []

for item in raw_prices:
    item = item.strip().replace("$", "").replace("USD","").replace("INR","")
    try: 
        cleaned_prices.append(float(item))
    except ValueError:
        print("Conversion Error")

cleaned_prices_comp = [float(item.strip().replace("$", "").replace("USD","").replace("INR","").replace("EUR","")) for item in raw_prices if item.strip().replace("$", "").replace("USD","").replace("INR","").replcae("EUR","").replace(".", "", 1).isdigit()]
print("Cleaned Prices: ", cleaned_prices_comp)