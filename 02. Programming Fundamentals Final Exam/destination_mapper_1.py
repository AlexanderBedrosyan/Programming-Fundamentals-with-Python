import re

pattern = r'([\=\/])([A-Z][a-zA-Z]{2,})\1'

location_map = input()
locations_found = re.findall(pattern, location_map)

list_of_locations = []
travel_points = []

for i in range(len(locations_found)):
    travel_points.append(len(locations_found[i][1]))
    list_of_locations.append(locations_found[i][1])

print(f"Destinations: {', '.join(list_of_locations)}")
print(f"Travel Points: {sum(travel_points)}")