# Import the datetime module
import datetime
# Import the date class from the datetime module
from datetime import date

# Define a function named addYears that takes a date (d) and a number of years (years) as input
def addYears(d, years):
    # Try to return the same day of the current year with the year adjusted by 'years'
    try:
        # If the same day is possible in the adjusted year, return it
        return d.replace(year=d.year + years)
    # If adjusting the year causes a ValueError (e.g., trying to go from February 29 to March 1 in a non-leap year)
    except ValueError:
        # Calculate and return the closest possible date by adding the difference between the adjusted year's January 1st and the original year's January 1st
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

# Print the result of adding -1 year to January 1st, 2015
print(addYears(datetime.date(2015, 1, 1), -1))
# Print the result of adding 0 years to January 1st, 2015
print(addYears(datetime.date(2015, 1, 1), 0))
# Print the result of adding 2 years to January 1st, 2015
print(addYears(datetime.date(2015, 1, 1), 2))
# Print the result of adding 1 year to February 29th, 2000 (a leap year)
print(addYears(datetime.date(2000, 2, 29), 1))
