countries = input().split(", ")
cities = input().split(", ")

for i, ch in zip(countries, cities):
    print(f"{i} -> {ch}")