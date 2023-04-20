from math import pi, sin, cos, acos

t1, g1 = input("Enter longitude and latitude of point one (in deg): ").split()
t2, g2 = input("Enter longitude and latitude of point two (in deg): ").split()

t1 = float(t1) * pi / 180
t2 = float(t2) * pi / 180
g1 = float(g1) * pi / 180
g2 = float(g2) * pi / 180

distance = 6371.01 * acos((sin(t1) * sin(t2)) +
                          (cos(t1) * cos(t2) * cos(g1-g2)))
print(
    f"Distance between two points ({t1},{g1}) and ({t2},{g2}) is {distance}km")
