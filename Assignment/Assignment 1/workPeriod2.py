##
# Code from Thursday's tutorial discussing the elements of Part-1 of the Assignment-1
##

from SimpleGraphics import *

#retrieving the 'x' and 'y' coordinates from the user to place the face on the canvas
x_coordinate=int(input('Enter the x cordinate for the face'))
y_coordinate=int(input('Enter the y cordinate for the face'))

text(x_coordinate, y_coordinate, "User gave this point")

#draw the shape of the face
## Describing how you centre the shape been drawn
ellipse(x_coordinate-150, y_coordinate-150, 300, 300) # Subtract the half of the size of the shape in 'x' and 'y' cordinate

##Re-locate this according to you
#draw eyes in the face using the rectange
rect(x_coordinate-150, y_coordinate-150, 50, 50)

"""
NOT SUPPOSED TO UNDERSTAND THE BELOW PART
Just to retrieve the coordinates where you left click your mouse
These 'x' and 'y' coordinates can be used later in the python script to add more shapes
"""
while not rightButtonPressed():
    #update to run properly
    update()
    if leftButtonPressed():
        x,y=mousePos()
        text(x, y, "Boom....")
        #get coordinates of where the click was
        print(mousePos())
