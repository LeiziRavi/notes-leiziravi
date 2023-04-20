# Sets : a collection with no duplicates.

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# Basic Operations ==>
# second.add(5)
# second.remove(5)
# len(second)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# can not access element using sets, and are un-ordered collection of elements
if 1 in first:
    print("yes")
