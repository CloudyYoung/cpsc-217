##
# @Name Cloudy Young
# @Student Number 
# @Description Draw hurricane plot on a map
# @Lines 77


# import SimpleGraphics library
from SimpleGraphics import *

# constant for height and width
HEIGHT = 620
WIDTH = 1022

# resize the window to the size of map, and draw the map
resize(WIDTH, HEIGHT)
img = loadImage('map.gif')
drawImage(img, 0, 0)

# constant for latitude and longitude in the unit of window pixel
LATITUDE = HEIGHT / 25
LONGITUDE = WIDTH / 45


##
# @name convLatitude
# @param latitude
# @return window pixel unit of given latitude
# @description convert the given latitude in reality into unit of window pixel
def convLatitude(latitude):
	return HEIGHT - LATITUDE * (latitude - 10)

##
# @name convLongitude
# @param longitude
# @return window pixel unit of given longitude
# @description convert the given longitude in reality into unit of window pixel
def convLongitude(longitude):
	return WIDTH - LONGITUDE * (longitude - 50)

##
# @name convWindSpeed
# @param windSpeed
# @return a list which contains color, diameter and category of given wind speed
# @description according to the given wind speed and tell its color, diameter and category
def convWindSpeed(windSpeed):
	if(windSpeed >= 157):
		color = "purple"
		diameter = 15
		category = 5
	elif(windSpeed >= 130):
		color = "red"
		diameter = 13
		category = 4
	elif(windSpeed >= 111):
		color = "orange"
		diameter = 11
		category = 3
	elif(windSpeed >= 96):
		color = "yellow"
		diameter = 9
		category = 2
	elif(windSpeed >= 74):
		color = "green"
		diameter = 7
		category = 1
	else:
		color = "white"
		diameter = 5
		category = 0
	return [color, diameter, category]


# draw latitude and longitude lines on the map
setColor('grey')
setWidth(1)

westLeft = 0
while((westLeft + 1) * LONGITUDE * 5 < WIDTH):
	westLeft += 1
	line(westLeft * LONGITUDE * 5, 0, westLeft * LONGITUDE * 5, 620)
	text(westLeft * LONGITUDE * 5 + 15, 10, str(95 - westLeft * 5) + 'W')

northTop = 0
while((northTop + 1) * LATITUDE * 5 < HEIGHT):
	northTop += 1
	line(0, northTop * LATITUDE * 5, 1022, northTop * LATITUDE * 5)
	text(15, northTop * LATITUDE * 5 - 10, str(35 - northTop * 5) + 'N')


# declare and initialize variables
latitude = 1 #top
longitude = 1 #left
windSpeed = 1

# a list stores all the given points in the while loop below
dot = []

# keep running while loop until the user input of latitude is zero
while(latitude != 0):

	# user enter latitude and initialize to the variable
	latitude = float(input("Enter latitude: "))
	
	# if latitude is not zero, continue asking for longitude and wind speed
	if(latitude != 0):
		# initialize variables and convert string into float number and use absolute value
		longitude = abs(float(input("Enter longitude: ")))
		windSpeed = abs(float(input("Enter wind speed: ")))

		# invoke convWindSpeed to get color, diameter and category
		windSpeedConv = convWindSpeed(windSpeed)
		color = windSpeedConv[0]
		diameter = windSpeedConv[1]
		category = windSpeedConv[2]
		
		# set point color and draw
		setColor(color)
		ellipse(convLongitude(longitude) - diameter / 2, convLatitude(latitude) - diameter / 2, diameter, diameter)

		# record point to the dot list
		dot.append([longitude, latitude, windSpeed, color, diameter, category])

# declare and initialize variables
maxCategory = 0
maxWindSpeed = 0

# for loop to draw lines between each points
for each in range(len(dot)):

	# if the index(which is 'each' variable) is pointing to the last element of the list, give up drawing that line because there is no more point after the last point
	if(each != len(dot) - 1):
		# compare the wind speed of current point and the next point, get the higher value by invoking max, and invoke convWindSpeed to get color of the line, and draw the line
		color = convWindSpeed(max(dot[each][2], dot[each + 1][2]))[0]
		setColor(color)
		setWidth(1)
		line(convLongitude(dot[each][0]), convLatitude(dot[each][1]), convLongitude(dot[each + 1][0]), convLatitude(dot[each + 1][1]))

	# compare the recorded max values with the current point's value, and record the higher value by invoking max
	maxCategory = max(maxCategory, dot[each][5])
	maxWindSpeed = max(maxWindSpeed, dot[each][2])

# draw the text of max category and max wind speed
setColor("white")
text(920, 35, "Max. Category: " + str(maxCategory) + "\n" + "Max. Wind Speed (mph): " + str(maxWindSpeed))
