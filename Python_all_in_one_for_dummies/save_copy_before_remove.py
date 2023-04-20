# create a list of strings
letters = ["A","B","C","D","C","E","C"]

# make a copy of first list item then remove it from the list.
first_removed = letters.pop(0)

# make a  copy of last list item then remove it from the list.
last_removed = letters.pop()

# Show the new list.
print(letters)

# Show what's been removed.
print(first_removed + " and " + last_removed + " were removed from the list.")