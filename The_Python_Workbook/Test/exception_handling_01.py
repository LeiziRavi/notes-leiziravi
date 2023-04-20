# Read the file name from the user
fname = input("Enter the file name: ")

# Attempt to open the file
try:
    inf = open(fname, "r")
except FileNotFoundError:
    # Display an error message and quit if the file was not opened successfully
    print("'%s' could not opened. Quitting...")
    quit()
    