# Read the file name from the user and open the file
fname = input("Where will the numbers will be stored? ")
outf = open(fname, "a")

# Read the maximum value that will be written
limit = int(input("What is the maximum value? "))

# Write the numbers to numbers to the file with one number on each line
for num in range(1, limit+1):
    outf.write(str(num) + "\n")

# Close the file
outf.close()