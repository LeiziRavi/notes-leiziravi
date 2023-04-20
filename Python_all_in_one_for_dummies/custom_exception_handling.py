class Error(Exception):
    """Base class for other Exceptions"""
    pass

# now define your exception as a subclass of Error


class EmptyFileError(Error):
    pass


try:
    # Open the file name people.csv
    thefile = open("people_copy.csv")
    print(thefile.tell())
    # Count the number of lines in the file.
    line_count = len(thefile.readlines())
    # If there is fewer than 2 lines, raise exception.
    if line_count < 2:
        raise EmptyFileError


# Handles missing file error.
except FileNotFoundError:
    print("\nThere is no people.csv file here")

# Handles my custom error for too few rows
except EmptyFileError:
    print("\nYour people.csv file doesn't have enough stuff.")

# Handles my custom error for too few rows.
except Exception as err:
    # Show the error.
    print("\n\nFailed: The error was " + str(err))
    # Close the file.
    thefile.close()

# Otherwise, if nothing bad happens by now, just keep going.
else:
    print(thefile.tell())
    # File must be open by now if we got here.
    print('\n')  # Print a blank line
    thefile.seek(0)
    print(thefile.tell())

    # Print each line from the file.
    for one_line in thefile:
        print(one_line)



        
    thefile.close()
    print('success!')
