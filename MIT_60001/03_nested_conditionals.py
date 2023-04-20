x = 8
if x % 2 == 0:
    if x % 3 == 0:
        print("x is divisible by 2 and 3")
    else:
        print("x is divisible by 2 but not divisible by 3")
elif x % 3 == 0:
    print("x is divisible by 3 but not by 2")
