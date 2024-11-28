# Import the calendar module
import calendar
# Create a TextCalendar object starting from Sunday as the first day of the week
cal = calendar.TextCalendar(calendar.SUNDAY)

year = int(input('Enter the year:'))

# Specify the formatting parameters for the year calendar
# year
# column width: 2
# lines per week: 1
# number of spaces between month columns: 1
# 3: number of months per column
# Generate the formatted year calendar for the year using the specified parameters
print(cal.formatyear(year, 2, 1, 1, 3))
