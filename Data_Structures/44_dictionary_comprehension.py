# values = []
# for x in range(5):
#     values.append(x * 2)


values = [x*2 for x in range(5)]
print(values)

values = {x*2 for x in range(5)}
print(values)


# Instead of
# values = {}
# for x in range(5):
#   values[x] = x * 2
# Use below
values = {x: x*2 for x in range(5)}
print(values)

values = (x*2 for x in range(5))
print(values)
