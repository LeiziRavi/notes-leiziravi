# Compute the sum of the integers from 0 up to and including n using recursion
# @param n the maximum value to include in the sum
# @return the sum of the integers from 0 up to and including n
def sum_to(n):
    if n<=0:
        return 0 # Base Case
    else:
        return n + sum_to(n-1) # Recursive case

# Compute the sum of the integers from 0 up to and including the value entered by the user
num = int(input("Enter a non-negative integer: "))
total = sum_to(num)
print("The total of the integers from 0 up to and including", \
    num, "is", total)
