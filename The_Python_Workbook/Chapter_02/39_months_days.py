##
# Display number of days in a month
##

# Read the month name from the user
month = input("Enter name of month: ")

# Compute the number of days in the month.
if month.lower() in ["january", "march", "may", "july", "august", "october", "december"]:
    print(f"{month} has 31 days.")
elif month.lower() in ["april", "june", "september", "november"]:
    print(f"{month} has 30 days.")
elif month.lower() == "february":
    print(f"{month} may have 28 or 29 days.")
else:
    print(("Enter valid month name."))
