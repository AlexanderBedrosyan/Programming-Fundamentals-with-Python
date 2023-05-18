from math import floor


def calculation():
    centuries = int(input())
    years = centuries * 100
    days = floor(years * 365.2422)
    hours = 24 * days
    minutes = hours * 60
    return f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes"


print(calculation())