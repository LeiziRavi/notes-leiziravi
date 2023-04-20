import sys


mylist = range(1, 10000)
print(sys.getsizeof(mylist))
# 48

my_real_list = [x for x in range(1, 10000)]
print(sys.getsizeof(my_real_list))
# 85716


"""
Q: Why only 48 bytes?
Ans: It’s because the range function returns a class that only behaves like a list. 
A range is a lot more memory efficient than using an actual list of numbers.
"""
