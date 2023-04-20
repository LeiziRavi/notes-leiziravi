# Import the datatime module, nicknae it
import datetime as dt

# Store today's date in a variable named today
today = dt.date.today()

# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019,12,31)

# See what's in each variable
print(today)
print(last_of_teens)

print(f"{last_of_teens:%A, %B, %d, %Y}")
print(f"{today:%m/%d/%Y}")


# Working with time
midnight = dt.time()
print(midnight)
print(type(midnight))

# Time right now
right_now = dt.datetime.now()
print(right_now)

# Duration between time
new_years_day = dt.date(2019,1,1)
memorial_day = dt.date(2019,5,27)
day_between = memorial_day - new_years_day

print(day_between)
print(type(day_between))

# Using timedelta to determine date from a previous_date after specific number of days
duration = dt.timedelta(days = 146)
print(new_years_day + duration)