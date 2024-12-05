from datetime import date, timedelta

# Get the current date and assign it to the variable 'today'
today = date.today()

weekday = 1

# Calculate the offset needed to go back to the most recent weekday
# This is done by finding the difference between the current weekday and target weekday, and taking modulo 7
offset = (today.weekday() - weekday) % 7

# Calculate the date of the most recent weekday by subtracting the offset from the current date
last_weekday = today - timedelta(days=offset)

# Print the date of the most recent weekday
print(last_weekday) 
