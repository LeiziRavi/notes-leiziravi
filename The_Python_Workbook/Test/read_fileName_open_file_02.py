# Read the file name from the user and open the file
from re import L
from sys import flags


fname = input("Enter the file name: ")
inf = open(fname, "r")

# initialize the total
total = 0
lines = inf.readlines()

# Total the values in the file
for line in lines:
    total = total + float(line)

# Close the file
inf.close()

# Display the result
print("The total of the values in", fname, "is", total)