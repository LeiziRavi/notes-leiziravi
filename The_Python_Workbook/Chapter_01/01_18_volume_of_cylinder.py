import math
PI = math.pi

radius = float(input("Enter the radius of base: "))
height = float(input("Enter the height of cylinder: "))

volume_of_cylinder = PI*math.pow(radius, 2)*height

print(f"Volume of cylinder with base radius {radius:.2f} and height {height:.2f} is {volume_of_cylinder:.2f}")