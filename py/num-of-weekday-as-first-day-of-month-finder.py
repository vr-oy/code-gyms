# Import the datetime class from the datetime module
from datetime import datetime

# Initialize a counter to count occurrences of Monday being the first day of the month
count = 0

# Define a range of months from 1 to 12
months = range(1, 13)

week_day = 0
start_year = 2015
end_year = 2019

for year in range(start_year, end_year + 1):
    # Iterate over each month in the range
    for month in months:
        # Check if the first day of the month (year, month, 1) falls on the weekday
        if datetime(year, month, 1).weekday() == week_day:
            # If the first day of the month is a Monday, increment the counter
            count += 1

# Print the total count of occurrences where Monday is the first day of the month
print(count)
