import math
radius = input("Enter radius: ")

area_circle = math.pi * math.pow(float(radius), 2)
volume_sphere = 4/3 * math.pi * math.pow(float(radius), 3)


print(f"Area of a circle with radius {radius} : {area_circle}")
print(f"Volume of sphere with radius {radius} : {volume_sphere}")
