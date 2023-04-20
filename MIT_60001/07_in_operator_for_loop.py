total = 0
# For statement can be used in conjunction with the in operator to conveniently iterate over characters of a sting
for c in '5436':
    # Sums the digits in the string denoted by the literal '5436' and prints the total
    total = total + int(c)
print(total)


# Let s be a string that contains a sequence of decimal numbers seperated by commas, e.g. s = '1.23, 2.4, 3.123'. Write a program that prints the sum of the numbers in s.

# Method 01
sum = 0
s = '1.23, 2.4, 3.123'
for d in s.split(","):
    sum = sum + float(d)
print(sum)

# Method 02
sumAll = 0
temp = ''
s = '1.23, 2.4, 3.123'
for c in s:
    if c != ',':
        temp = temp + c
    else:
        sumAll = sumAll + float(temp)
        temp = ''
sumAll = sumAll + float(temp)
print(sumAll)
