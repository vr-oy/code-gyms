# Import the datetime module
import datetime


year = int(input('Enter the year:'))
num_of_dates = int(input('Enter the number of dates to print:'))
interval = int(input('Enter the number of days between dates:'))

# Define a function named every_20_days that takes a date object (date) as input
def every_n_days(interval,date):
    # Print the starting date
    print('Starting Date: {d}'.format(d=date))
    # Print a message indicating the next 12 days
    print("Next %s days :" % num_of_dates )

    for _ in range(num_of_dates):
        # Add n days to the current date
        date = date + datetime.timedelta(days=interval)
        # Print the resulting date
        print('{d}'.format(d=date))

# Define a date object representing the date
dt = datetime.date(year, 1, 1)

# Call the every_20_days function with the specified date object
every_n_days(interval , dt)
