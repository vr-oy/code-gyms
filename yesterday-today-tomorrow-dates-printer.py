# Import the datetime module
import datetime 

# Get the current date using datetime.date.today()
today = datetime.date.today()

# Calculate yesterday's date by subtracting 1 day from today's date using timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)

# Calculate tomorrow's date by adding 1 day to today's date using timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1) 

# Print yesterday's date
print('Yesterday : ', yesterday)

# Print today's date
print('Today : ', today)

# Print tomorrow's date
print('Tomorrow : ', tomorrow)
