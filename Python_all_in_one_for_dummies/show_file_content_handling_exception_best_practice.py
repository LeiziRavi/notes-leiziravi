class Error(Exception):
    """Base class for other Exceptions"""
    pass

# now define your exception as a subclass of Error
class EmptyFileError(Error):
    pass

try:
    # Open the file name people.csv
    thefile = open('people.csv')
    lines = len(thefile.readlines())
    if lines < 2:
        raise EmptyFileError 

# Watch for common error and stop program if it happens.
except FileNotFoundError:
    print("Sorry, I don't see a file named people.csv here")

except EmptyFileError:
    print("File is empty.")
# Catch any unexpected error and stop program if one happens.

except Exception as err:
    print(err)
# Otherwise, if nothing bad happens by now, just keep going.

else:
    thefile.seek(0)
    # File must be open by now if we got here.
    print('\n') # Print a blank line
    # Print each line from the file.
    for one_line in thefile.readlines():
        print(one_line)
    thefile.close()
    print('success!')