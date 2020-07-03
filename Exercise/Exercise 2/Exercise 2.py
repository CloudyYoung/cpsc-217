#import everything from SimpleGraphics library
from SimpleGraphics import *

#set window property: title, background color, size
setWindowTitle('Exercise 2')
background(0, 191, 255) # draw sky
resize(700, 500)

#draw sun
setFill(255, 255, 0)
setOutline(255, 255, 0)
ellipse(550, -125, 275, 275)

#draw grass ground
setFill(0, 128, 0)
setOutline(0, 128, 0)
rect(0, 400, 700, 300)

#draw clouds
setFill(255, 255, 255)
setOutline(255, 255, 255)
ellipse(150, 50, 50, 50)
ellipse(150, 80, 50, 50)
ellipse(120, 50, 50, 50)
ellipse(180, 80, 50, 50)
ellipse(120, 80, 50, 50)
ellipse(90, 80, 50, 50)

#draw house body
setFill(244, 164, 96)
setOutline(244, 164, 96)
rect(200, 250, 300, 175)

#draw house roof
setFill(160, 82, 45)
setOutline(160, 82, 45)
polygon(175, 250, 350, 150, 525, 250)

#draw house door
setFill(165, 42, 42)
setOutline(165, 42, 42)
rect(235, 300, 100, 125)

#draw house window
setFill(255, 165, 0)
setOutline(255, 165, 0)
rect(360, 300, 105, 100)

#draw house window frame
setOutline(205, 133, 63)
line(360, 350, 465, 350)
line(412.5, 300, 412.5, 400)

#draw my name
setOutline(0, 0, 0)
text(650, 480, "Cloudy Young")


update()
