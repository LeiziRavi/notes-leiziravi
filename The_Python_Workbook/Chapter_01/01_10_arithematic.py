from math import log10
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Sum of %d and %d : " % (a, b), a+b)
print("Difference of %d and %d : " % (a, b), a-b)
print("Product of %d and %d : " % (a, b), a*b)
print("Quotient when %d is divided by %d : " % (a, b), a/b)
print("Reminder when %d is divided by %d : " % (a, b), a % b)
print("log10 of %d :" % a, log10(a))
print("%d raised to the power of %d : " % (a, b), a**b)
