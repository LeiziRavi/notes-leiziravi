"""
    Write a program that computes the perimeter of a polygon. Begin by reading the
    x and y coordinates for the first point on the perimeter of the polygon from the
    user. Then continue reading pairs of values until the user enters a blank line for the
    x-coordinate. Each time you read an additional coordinate you should compute the
    distance to the previous point and add it to the perimeter. When a blank line is entered
    for the x-coordinate your program should add the distance from the last point back
    to the first point to the perimeter. Then the perimeter should be displayed. Sample
    input and output values are shown below. The input values entered by the user are
    shown in bold.

        Enter the first x-coordinate: 0
        Enter the first y-coordinate: 0
        Enter the next x-coordinate (blank to quit): 1
        Enter the next y-coordinate: 0
        Enter the next x-coordinate (blank to quit): 0
        Enter the next y-coordinate: 1
        Enter the next x-coordinate (blank to quit):
        The perimeter of that polygon is 3.414213562373095

"""

import math
x_cord = int(input("Enter first x-cordinate: "))
y_cord = int(input("Enter first y-cordinate: "))

# print(type(x_cord), type(y_cord))

x_first = x_cord
y_first = y_cord

# print(type(x_first), type(y_first))

x_next = input("Enter next x-cordinate (blank to quit): ")

perimeter = 0

while x_next != "":
    y_next = input("Enter next y-cordinate: ")

    x_dist = int(x_next) - int(x_cord)
    y_dist = int(y_next) - int(y_cord)
    perimeter = perimeter + \
        math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))

    x_cord = int(x_next)
    y_cord = int(y_next)

    x_next = input("Enter next x-cordinate (blank to quit): ")

perimeter = perimeter + \
    math.sqrt(math.pow((x_cord - x_first), 2) +
              math.pow((y_cord - y_first), 2))

print("Perimeter of entered polygon: ", perimeter)
