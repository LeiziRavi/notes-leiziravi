# Define a set named sample_set.
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}

# Show the whole set
print(sample_set)

# Use len to get the length of a set
print(len(sample_set))

# Use in parameter to determine if the set contains a value
print(74.95 in sample_set)

# Use add() to add one item to a set
sample_set.add(11.23)

# Use update to add a [list] to a set
sample_set.update([18, 123.45, 2.98])

print("\nSample set after .add() and .update()")
print(sample_set)

# Loop through the set and print each item right aligned and formatted.
print("\nLoop through set and print each item formatted.")
for price in sample_set:
    print(f"{price:>6.2f}")