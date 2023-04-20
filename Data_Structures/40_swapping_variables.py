x = 10
y = 11

print(f"x = {x},y = {y}")
# temp = x
# x = y
# y = temp

x, y = y, x
# Above line is equivalent to x, y = (11, 10)
print(f"x = {x},y = {y}")
