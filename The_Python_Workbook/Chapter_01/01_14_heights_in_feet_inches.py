in_feet = input("Enter feet_height: ")
in_inch = input("Enter inch height: ")

feet_to_inch = float(in_feet) * 12

totat_height = float(in_inch) + feet_to_inch

to_centi = totat_height * 2.54

print(
    f"The height {in_feet} feet and {in_inch} inches is equal to: {to_centi} cms")
