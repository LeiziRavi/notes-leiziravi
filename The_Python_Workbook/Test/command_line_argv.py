# The system moodule must be imported to access the command line arguments 
import sys

#Display the number of command line arguments (including the .py file)
print("The program has", len(sys.argv), \
    "command line argumnet(s).")

# Display the name of the .py file
print("The name of the .py file is", sys.argv[0])

# Determine whether or not there are additional arguments to display
if len(sys.argv) > 1:
    #Display all of the command line arguments beyond the name of the .py file
    print("The remaining arguments are:")
    for i in range(1, len(sys.argv)):
        print(" ", sys.argv[i])
else:
    print("No additional arguments were provided.")