from logging import error


number = int(input("Enter a number: "))
div = 0
try:
    div = 3/number
except ZeroDivisionError:
    print(error, "number cannot be zero") 