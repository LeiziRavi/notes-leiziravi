no_of_sides = int(input("Enter number of sides shape has: "))

if no_of_sides < 3 or no_of_sides > 10:
    print("Enter valid number. Only between 3 to 10 is valid.")
elif no_of_sides == 3:
    print(f"Trinagle has {no_of_sides} sides.")
elif no_of_sides == 4:
    print(f"Quadrilateral has {no_of_sides} sides.")
elif no_of_sides == 5:
    print(f"Pentagon has {no_of_sides} sides.")
elif no_of_sides == 6:
    print(f"Hexagon has {no_of_sides} sides.")
elif no_of_sides == 7:
    print(f"Septagon has {no_of_sides} sides.")
elif no_of_sides == 8:
    print(f"Octagon has {no_of_sides} sides.")
elif no_of_sides == 9:
    print(f"Nonagon has {no_of_sides} sides.")
elif no_of_sides == 10:
    print(f"Decagon has {no_of_sides} sides.")
