# Read the file name from the user and open the file

fname = input("Enter the file name to display: ")
inf = open(fname, "r")

# initialize the line number
num = 1

# Display each line in the file, preceded by its line number
line = inf.readline()
while line != "":
    print("%d: %s" % (num, line))

    # increment the line number and read the next line
    num  = num + 1
    line = inf.readline()


# Close the file
inf.close()
