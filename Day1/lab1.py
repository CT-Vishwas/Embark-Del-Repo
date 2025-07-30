#!/usr/bin/env python3
# Given a list of Products
 
products = [
	{"name": "Laptop", "price": 1200, "category": "Electronics"},
	{"name": "Mouse", "price": 25, "category": "Electronics"},
	{"name": "Desk Chair", "price": 150, "category": "Furniture"},
	{"name": "Keyboard", "price": 75, "category": "Electronics"},
	{"name": "Monitor", "price": 300, "category": "Electronics"},
]
 
# Sort products by price (ascending), then by name (ascending).
sorted_products = sorted(products, key=lambda p: (p["name"], -p["price"]), reverse=True)
print("Sorted Products: ", sorted_products)

# Filter products that are in 'Electronics' category and cost more than $100.
# filtered_products = [
#     p
#     for p in products
#     if p["category"] == "Electronics" and p["price"] > 100
# ]

# print("Filtered Products: ", filtered_products)

