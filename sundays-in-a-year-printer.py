# Import the date class and the timedelta class from the datetime module
from datetime import date, timedelta

# Define a function named all_sundays that takes a year as input
def all_sundays(year):
    # Set dt to January 1st of the given year
    dt = date(year, 1, 1)
    # Move dt to the first Sunday of the given year
    dt += timedelta(days=6 - dt.weekday())  
    # Iterate through all Sundays of the given year
    while dt.year == year:
        # Yield the current date (dt) as a result
        yield dt
        # Move to the next Sunday by adding 7 days
        dt += timedelta(days=7)

year = 2020

# Iterate through all Sundays of the year 2020 using the all_sundays function
for s in all_sundays(year):
    # Print each Sunday
    print(s)
