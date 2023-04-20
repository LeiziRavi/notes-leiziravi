# Create a new, empty list
values = []

# Read values from the user and store them in a list until a blank line is entered
line = input("Enter a number (blank line to quit): ")
while line != "":
    num = float(line)
    values.append(num)

    line = input("Enter a number (blank to quit): ")

# Sort the values into ascending order
values.sort()

# Display the values
for v in values:
    print(v)