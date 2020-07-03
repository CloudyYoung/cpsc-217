##
# @Name Cloudy Young
# @Student Number 
# @Description Draw thumbnails of a set of beautiful images with tourists and one generated image without tourists on the window
# @Lines 
# @Note Completion with A+ standard

#import 'SimpleGraphics' library for drawing on window, 'os' library for file finding and 're' library for usage of regular expression
from SimpleGraphics import *
import os, re

# @name median
# @param l
# @return median value of input list
# @description calculate the median value in a list
def median(l):
	l = sorted(l)
	if len(l) % 2 == 1:
		r = l[int(len(l) / 2)]
	else:
		r = (l[int(len(l) / 2 - 1)] + l[int(len(l) / 2)]) / 2
	return r

##
# @name loadImages
# @return image set list from user
# @description PART-1 load image set user asks into memory and resize window
def loadImages():
	imgset, abbr = [], input("Enter your picture set's abbreviation: ")

	# list all files in user current directory
	files = os.listdir(os.path.dirname(__file__))

	# filter out each file which file name starts with user's abbreviation by using regular expression, and load to image set list
	for f in files:
		if re.match(abbr + "_", f):
			imgset.append(loadImage(f))
	print(str(len(imgset)) + " images are loaded.")

	# check for image set validity, and resize the window
	if len(imgset) < 3 or len(imgset) > 16:
		print("Picture amount must be greater than 3 or smaller than 16.")
		close()
		quit()
	else:
		resize(getWidth(imgset[0]) * 2, getHeight(imgset[0]))

	return imgset

##
# @name createThumbnail
# @param image
# @return thumbnail of input image
# @description PART-2 create thumbnail for a single image
def createThumbnail(image):

	# create a new blank image has 1/4 size of input image as its thumbnail
	thumbHeight, thumbWidth = int(getHeight(image) / 4), int(getWidth(image) / 4)
	img = createImage(thumbWidth, thumbHeight)

	# for every 4x4 pixels in the input image, only take the pixel on the top left corner and put it on thumbnail
	for x in range(0, thumbWidth):
			for y in range(0, thumbHeight):
				pixel = getPixel(image, 4 * x, 4 * y)
				putPixel(img, x, y, pixel[0], pixel[1], pixel[2])

	return img

# @name drawThumbnails
# @param images
# @descrition draw thumbnails for a whole image set
def drawThumbnails(images):

	# for each image in the set, create its thumbnail and draw on the window
	for pic in range(0, len(images)):
		image = createThumbnail(images[pic])
		drawImage(image, int(pic % 4) * getWidth(image), int(pic / 4) * getHeight(image))

	print(str(len(images)) + " thumbnails are drew.")

##
# @name removeTourists
# @param images
# @description PART-3 remove all tourist
def removeTourists(images):

	# create a new blank image as non-tourist image
	print("It may take few seconds...")
	noTouristImage = createImage(getWidth(images[0]), getHeight(images[0]))

	# for each pixel on the image
	for x in range(0, getWidth(images[0])):
		for y in range(0, getHeight(images[0])):
			red, green, blue = [], [], []

			# for each image in the image set
			for pic in range(0, len(images)):

				# access rgb value of current pixel on the current image, and append to lists respectively
				pixel = getPixel(images[pic], x, y)
				red.append(pixel[0])
				green.append(pixel[1])
				blue.append(pixel[2])

			# calculate median rgb value and put it on non-tourist image
			putPixel(noTouristImage, x, y, median(red), median(green), median(blue))

	# draw final non-tourist image on the window
	drawImage(noTouristImage, getWidth(noTouristImage), 0)
	print("1 image is drew.")

# The main program loads the images, draws the thumbnails and then generates
# the tourist-free image
def main():
  images = loadImages()
  drawThumbnails(images)
  removeTourists(images)

main()
