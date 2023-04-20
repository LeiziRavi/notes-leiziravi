# Read the file name from the user and open the file
fname = input("Enter the file name: ")
inf = open(fname, "r")

# initialize the total
total = 0
# Total the values in the file
line = inf.readline()
while line != "":
    total = total + float(line)
    line = inf.readline()

# Close the file
inf.close()

# Display the result
print("The total of the values in", fname, "is", total)