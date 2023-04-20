number = [1, 2, 3]
print(number)
print(*number)  # unpacking operator

values = list(range(5))
print(values)

# values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

# more tricks to  use unpacking operator
first = [1, 2]
second = [3]
value = [*first, *"abc", *second]
print(value)

# Unpacking dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
