WEIGHT_WIDGETS = 0.075
WEIGHT_GIZMOS = 0.112

widgets = int(input("Enter number of widgets: "))
gizmos = int(input("Enter number of gizmos: "))

total_weight = (WEIGHT_WIDGETS*widgets) + (WEIGHT_GIZMOS*gizmos)
print("Total weight of parts: %.2f kg" % total_weight)
