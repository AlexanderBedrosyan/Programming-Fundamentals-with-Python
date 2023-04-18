from math import floor

centuries = int(input())

# 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes

years = centuries * 100
days = floor(years * 365.2422)
hours = 24 * days
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
