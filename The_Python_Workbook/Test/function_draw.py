# Draw a box  outlined with astericks and filled with spaces
# @param width the width of the box
# @param height the height of the box

def drawBox(width, height):
    # A box that is smaller than 2x2 cannot be drawn by this function
    if width < 2 or height < 2:
        print("Error: The width or height is too small.")
        quit()

    # Draw the top of the box
    print("*" * width)

    # Draw the sides of the box
    for i in range(height-2):
        print("*" + " " * (width-2) + "*")

    # draw the bottom of the box
    print("*" * width)


drawBox(5, 3)
