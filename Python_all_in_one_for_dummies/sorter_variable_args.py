def sorter(*args):
    """ Pass in any number of arguments seperated by commas
    Inside the function, they treated as a tuple named args """
    # The passed-in
    # Create a list from the passed-tuple
    newlist = list(args)
    # Sort and show the list.
    newlist.sort()
    print(newlist)

sorter(1, 0.001, 10000, -900, 2)
sorter(1, 5, 7, 9, 6, 2, 6, 10)