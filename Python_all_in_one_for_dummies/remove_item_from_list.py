# Create a list of Strigs
letters = ["A","B","C","D","C","E","C"]

# Remove "C" from the list , Only first ocurrence is deleted
letters.remove("C")

# Show me the new list
print(letters)

print("=======================================")


# Remove Item based on index
letters = ["A","B","C","D","C","E","C"]
print("Original list: ",letters)
# Remove first item
letters.pop(0)
print("letters with first item removed: ", letters)

print("=======================================")

letters = ["A","B","C","D","C","E","C"]
print("Original list: ",letters)
# Removes the last item
letters.pop()
print("letters with last item removed: ", letters)

print("=======================================")

letters = ["A","B","C","D","C","E","C"]
print("Original list: ",letters)
# Remove item at index: 4
letters.pop(3)
print("letters with index 4 item removed: ", letters)


print("=======================================")

# Removing specific item at index using del

letters = ["A","B","C","D","C","E","C"]
print("Original list: ",letters)
# Remove item at index: 5
del letters[4]
print("letters with index 5 item removed: ", letters)

# Removing entire list using del, list doesn't exist after this operation

letters = ["A","B","C","D","C","E","C"]
print("Original list: ",letters)
print("Calling del to remove entire list")
del letters
print(letters)