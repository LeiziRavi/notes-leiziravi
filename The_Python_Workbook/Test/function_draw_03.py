# Draw a box  outlined with astericks and filled with spaces
# @param width the width of the box
# @param height the height of the box

# Default values for outline and fill, so that in case * and " " is used, no argument needs to be passed.
def drawBox(width, height, outline="*", fill=" "):
    # A box that is smaller than 2x2 cannot be drawn by this function
    if width < 2 or height < 2:
        print("Error: The width or height is too small.")
        quit()

    # Draw the top of the box
    print(outline * width)

    # Draw the sides of the box
    for i in range(height-2):
        print(outline + fill * (width-2) + outline)

    # draw the bottom of the box
    print(outline * width)


drawBox(7, 5, "@", ".")
print("=======================================")
drawBox(7, 5)
