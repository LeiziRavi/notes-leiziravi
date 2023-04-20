# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

from sys import getsizeof
values = (x * 2 for x in range(100000))
print("gen: ", getsizeof(values))
# gen:  112
print(len(values))  # object of type 'generator' has no len()
# becoz we can only access these items/ these values, when we iterate over a generator object.


# values = [x * 2 for x in range(100000)]
# print("list: ", getsizeof(values))
# list:  800984
# When we are dealing with potentially large data sets or infinite stream of data, use a generator
# expression to create a generator object.
