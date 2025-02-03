# Import the date class from datetime module
from datetime import date

# Define a function called calculate_age which calculates the age based on the date of birth
def calculate_age(dtob):
    # Get the current date
    today = date.today()
    # Calculate the age by subtracting the birth year from the current year
    # Adjust the age if the birth month and day are after today's month and day
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

# Print an empty line
print()
# Print the age calculated based on the date of birth October 12, 2006
print(calculate_age(date(2006,10,12)))
# Print the age calculated based on the date of birth January 12, 1989
print(calculate_age(date(1989,1,12)))
# Print an empty line
print()
