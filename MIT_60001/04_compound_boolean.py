x = 1
y = 3
z = 5

if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if x > y and x > z:
        print('x is largest odd number.')
    elif y > z:
        print('y is largest odd number')
    else:
        ('z is largest odd number')
elif x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    if x < y and x < z:
        print('x is least number.')
    elif y < z:
        print('y is least number')
    else:
        ('z is least number')
