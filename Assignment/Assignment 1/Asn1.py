##
# @Name Cloudy Young
# @Student Number 
# @Description Draw graphics according to your coordinate


#user input
print("**Tip: whole graphics can be shown if x > 235 and y > 260")
x = int(input("Input x value: ")) #user input
y = int(input("Input y value: ")) #user input


#import everything from SimpleGraphics library
from SimpleGraphics import *

#background and window title
setWindowTitle("Assignment 1")
background(255, 255, 255)



## @name convertCoordinates
#  @param args
#  @return array
#  @description change all fixed coordinates with user input

def convertCoordinates(*args):

	#declare variable
	ret = []
	arr = []

	#convert parameters into an array variable
	if(len(args) == 1):
		# if there is only one paramter, then directly store as a single variable
		arr = args[0]
	else:
		# if there are several paramters, then store as an array
		arr = list(args)

	print(arr)

	# for each coordinate, add x-axis with x and y-axis with y so the graph is in the center
	for coor in range(len(arr)):
		if(coor %2 == 0):
			ret.append(int(arr[coor] - 60 - 222 + x))
		elif(coor %2 != 0):
			ret.append(int(arr[coor] - 66 - 262 + y))

	#return the converted array
	return ret



# background text
setWidth(2)
setFont("Microsoft YaHei UI Light", 70)
setColor(176, 199, 243)

textPosition = convertCoordinates([400, 380])
text(textPosition[0], textPosition[1], "CLOUDYYOUNG")



# neck & neck shadow & collarbone

neckOutline = [492, 580, 388, 441, 293, 439, 286, 433, 284, 414, 288, 407, 308, 402, 312, 322, 213, 312, 183, 338, 193, 357, 199, 372, 202, 386, 204, 402, 205, 415, 206, 435, 207, 448, 175, 484, 156, 583]

setColor(254, 245, 233)
polygon(convertCoordinates(neckOutline))


neckShadowOutline = [286, 433, 284, 414, 288, 407, 308, 402, 312, 322, 213, 312, 183, 338, 193, 357, 199, 372, 202, 386, 204, 402, 205, 415, 206, 435, 207, 448, 175, 484, 179, 480, 209, 484, 237, 482, 245, 481, 253, 478, 256, 477, 261, 475, 266, 471, 270, 468, 273, 465, 276, 463, 279, 459, 281, 454, 283, 449, 284, 442, 285, 436]

setColor(255, 221, 200)
polygon(convertCoordinates(neckShadowOutline))

setColor(169, 118, 101)
curve(convertCoordinates(neckOutline))

collarboneOutline1 = [235, 425, 246, 448, 253, 466, 259, 477, 267, 491]
collarboneOutline2 = [285, 471, 281, 482, 282, 490]

curve(convertCoordinates(collarboneOutline1))
curve(convertCoordinates(collarboneOutline2))


# shirt

shirtOutline = [511, 590, 503, 562, 488, 518, 485, 490, 476, 474, 469, 458, 462, 450, 451, 442, 440, 435, 428, 432, 414, 433, 400, 435, 378, 437, 356, 435, 340, 433, 323, 427, 319, 427, 296, 429, 310, 587, 196, 451, 187, 464, 172, 481, 161, 494, 147, 503, 135, 513, 121, 523, 110, 530, 96, 537, 88, 542, 78, 555, 75, 566, 71, 577, 69, 590]
shirtCollarOutline = [207, 435, 206, 428, 205, 426, 198, 427, 192, 431, 190, 437, 182, 457, 182, 457, 196, 481, 210, 511, 219, 532, 229, 552, 241, 576, 249, 590, 259, 603, 259, 604, 265, 588, 273, 577, 282, 566, 291, 562, 293, 562, 293, 565, 292, 566, 296, 567, 301, 570, 309, 580, 311, 587, 312, 588, 310, 570, 310, 552, 315, 526, 315, 522, 317, 522, 323, 524, 333, 531, 340, 542, 357, 576, 358, 577, 357, 559, 355, 546, 347, 510, 343, 499, 336, 481, 328, 463, 320, 449, 303, 422, 302, 421, 285, 422, 285, 422, 289, 439, 298, 493, 299, 514, 300, 530, 304, 548, 305, 550, 282, 522, 261, 499, 248, 481, 232, 465, 215, 446, 207, 437, 200, 431]
shirtCollarShadowOutline1 = [205, 427, 206, 436, 205, 437, 246, 480, 233, 483, 222, 483, 207, 483, 196, 483, 196, 482, 182, 456, 182, 455, 191, 434, 198, 428, 206, 426]
shirtCollarShadowOutline2 = [285, 422, 302, 422, 311, 436, 308, 440, 301, 443, 294, 446, 291, 448, 285, 423]
shirtShadowOutline1 = [192, 456, 182, 472, 169, 487, 155, 498, 137, 511, 126, 519, 110, 530, 92, 541, 83, 552, 78, 559, 102, 556, 118, 547, 130, 542, 142, 536, 155, 527, 166, 521, 177, 512, 185, 504, 194, 496, 204, 484]
shirtShadowOutline2 = [306, 426, 321, 427, 340, 433, 357, 436, 371, 438, 385, 444, 394, 449, 402, 454, 408, 461, 406, 467, 403, 472, 397, 476, 390, 478, 379, 480, 365, 478, 353, 475, 341, 470, 332, 465, 325, 458, 315, 441]
shirtShadowOutline3 = [186, 466, 178, 476, 225, 550, 243, 569, 270, 612, 298, 575, 311, 581, 329, 551, 344, 553, 298, 441, 306, 537, 304, 560, 206, 461]

setColor(255, 255, 255)
polygon(convertCoordinates(shirtOutline))

setColor(242, 242, 242)
polygon(convertCoordinates(shirtShadowOutline1))

setColor(247, 247, 247)
polygon(convertCoordinates(shirtShadowOutline2))

setColor(235, 235, 235)
polygon(convertCoordinates(shirtShadowOutline3))

setColor(126, 78, 3)
curve(convertCoordinates(shirtOutline))

setColor(176, 199, 243)
polygon(convertCoordinates(shirtCollarOutline))
polygon(convertCoordinates([345, 503, 356, 532, 357, 555])) # details

setColor(141, 171, 221)
polygon(convertCoordinates(shirtCollarShadowOutline1))
polygon(convertCoordinates(shirtCollarShadowOutline2))

setColor(126, 78, 3)
curve(convertCoordinates(shirtCollarOutline))
line(convertCoordinates(183, 456, 169, 484)) # details
line(convertCoordinates(477, 489, 491, 529)) # details
line(convertCoordinates(303, 427, 332, 424)) # details
line(convertCoordinates(331, 521, 357, 577)) # details
line(convertCoordinates(312, 583, 311, 600)) # details
line(convertCoordinates(343, 498, 362, 549)) # details
line(convertCoordinates(356, 531, 357, 560)) # details
line(convertCoordinates(299, 466, 300, 475)) # details
line(convertCoordinates(310, 570, 313, 562)) # details



# face & skin
faceOutline = [341, 149, 376, 206, 375, 236, 361, 273, 360, 309, 361, 335, 357, 356, 344, 371, 337, 380, 327, 403, 321, 407, 310, 410, 277, 408, 242, 396, 216, 383, 187, 347, 184, 340, 133, 279, 129, 237, 139, 174]

setColor(254, 245, 230)
setOutline("")
polygon(convertCoordinates(faceOutline))

setColor(169, 118, 101)
curve(convertCoordinates(faceOutline))


# face shadow & skin shadow
faceShadowOutline = [175, 228, 182, 288, 361, 268, 374, 232, 373, 200]
setColor(255, 221, 200)
polygon(convertCoordinates(faceShadowOutline))


# mouth
mouthOutline = [320, 359, 311, 361, 300, 360, 291, 359, 283, 355, 275, 351, 270, 347]

setColor(169, 118, 101)
curve(convertCoordinates(mouthOutline))
line(convertCoordinates(321, 357, 313, 359)) # details



# face tattoo
tattoo1Outline = [255, 314, 235, 320, 254, 326]
tattoo2Outline = [250, 332, 226, 322, 236, 343]
tattoo3Outline = [219, 325, 205, 337, 232, 344]
tattoo4Outline = [206, 345, 226, 369, 228, 348]

setColor(255, 198, 177)
polygon(convertCoordinates(tattoo1Outline))
polygon(convertCoordinates(tattoo2Outline))
polygon(convertCoordinates(tattoo3Outline))
polygon(convertCoordinates(tattoo4Outline))


# headwear: bear
bearOutline = [303, 118, 303, 105, 306, 96, 309, 92, 313, 90, 316, 88, 320, 86, 341, 87, 346, 88, 351, 91, 355, 93, 358, 96, 360, 99, 362, 102, 367, 120, 368, 126, 367, 130, 364, 136, 361, 140, 358, 142, 355, 145, 352, 147, 324, 147]

setColor(127, 81, 58)
polygon(convertCoordinates(bearOutline))

setColor(91, 43, 21)
curve(convertCoordinates(bearOutline))

setColor(127, 81, 58)
coordinate = convertCoordinates([322, 71])
ellipse(coordinate[0], coordinate[1], 24, 23) #bear ear 1
coordinate = convertCoordinates([358, 99])
ellipse(coordinate[0], coordinate[1], 24, 25) #bear ear 2

setColor(89, 42, 22)
coordinate = convertCoordinates([326, 97])
ellipse(coordinate[0], coordinate[1], 8, 8) #bear eye 1
coordinate = convertCoordinates([349, 112])
ellipse(coordinate[0], coordinate[1], 8, 8) #bear eye 2

setColor(255, 255, 255)
setOutline(91, 43, 21)
coordinate = convertCoordinates([323, 109])
ellipse(coordinate[0], coordinate[1], 22, 25) #mouth area

setColor(91, 43, 21)
coordinate = convertCoordinates([332, 115])
ellipse(coordinate[0], coordinate[1], 8, 8) #bear nose
line(convertCoordinates(335, 118, 332, 124)) #bear mouth



# hair & hair shadow & hair highlight & hair cover

hairOutline = [215, 95, 229, 92, 242, 90, 253, 90, 260, 91, 271, 93, 277, 94, 285, 94, 291, 94, 296, 93, 299, 92, 304, 91, 309, 89, 306, 92, 302, 94, 298, 96, 294, 98, 290, 99, 293, 101, 297, 102, 302, 105, 307, 108, 312, 112, 316, 115, 322, 118, 332, 125, 345, 139, 353, 146, 358, 152, 363, 160, 367, 169, 372, 183, 382, 205, 391, 217, 395, 221, 401, 223, 403, 224, 394, 223, 385, 220, 378, 216, 370, 209, 364, 198, 369, 209, 378, 217, 380, 217, 380, 226, 383, 231, 387, 239, 393, 246, 398, 247, 390, 246, 382, 241, 377, 237, 372, 231, 369, 226, 371, 221, 374, 214, 371, 221, 369, 230, 366, 238, 362, 242, 360, 243, 356, 248, 359, 241, 360, 235, 360, 232, 358, 226, 356, 227, 350, 233, 347, 238, 343, 241, 338, 246, 335, 248, 338, 242, 338, 235, 338, 228, 337, 221, 337, 216, 339, 205, 340, 195, 340, 189, 340, 180, 339, 172, 337, 167, 339, 175, 340, 189, 339, 201, 337, 210, 336, 219, 331, 228, 328, 235, 323, 245, 318, 253, 311, 258, 301, 265, 295, 265, 293, 265, 297, 252, 300, 235, 301, 217, 299, 201, 297, 195, 299, 211, 297, 221, 294, 236, 289, 243, 283, 248, 279, 249, 276, 251, 273, 251, 277, 246, 279, 236, 280, 228, 280, 221, 279, 213, 278, 206, 278, 217, 275, 226, 271, 232, 265, 237, 255, 243, 242, 246, 235, 248, 233, 248, 236, 243, 237, 237, 238, 233, 237, 229, 237, 228, 233, 235, 226, 242, 220, 249, 213, 253, 207, 258, 206, 258, 207, 252, 207, 246, 208, 242, 201, 245, 194, 258, 184, 278, 182, 289, 184, 339, 187, 346, 199, 368, 188, 356, 186, 377, 181, 365, 172, 359, 160, 354, 134, 340, 124, 335, 120, 326, 124, 337, 129, 344, 138, 351, 137, 351, 124, 345, 116, 337, 109, 329, 105, 322, 99, 313, 96, 306, 96, 299, 96, 291, 97, 281, 99, 274, 96, 284, 96, 297, 95, 307, 98, 322, 98, 322, 92, 313, 88, 305, 84, 293, 80, 280, 77, 265, 77, 246, 78, 232, 79, 222, 88, 207, 81, 213, 69, 220, 60, 226, 66, 218, 72, 209, 96, 160, 100, 153, 105, 149, 95, 151, 86, 148, 79, 146, 77, 146, 93, 144, 104, 140, 118, 133, 127, 127, 137, 119, 157, 106, 175, 100, 191, 97, 204, 96, 214, 96, 219, 95]
hairOutline2 = [266, 128, 287, 144, 296, 155, 303, 166, 307, 175]
hairOutline3 = [266, 128, 275, 135, 275, 137, 284, 149, 291, 163]
hairOutline4 = [238, 138, 237, 160, 230, 177, 210, 207, 208, 210, 211, 191, 211, 167, 212, 163, 207, 181, 201, 200, 194, 218]
hairOutline5 = [142, 157, 130, 194, 129, 215, 131, 225, 131, 227, 133, 216, 143, 192, 151, 173, 156, 165, 157, 164, 150, 181, 149, 194, 150, 210, 151, 218, 156, 225]

setColor(109, 76, 61)
polygon(convertCoordinates(hairOutline))


hairShadowOutline1 = [126, 128, 114, 137, 105, 158, 99, 185, 95, 213, 96, 257, 90, 268, 87, 283, 90, 302, 96, 318, 95, 302, 101, 311, 104, 302, 111, 321, 120, 330, 126, 335, 152, 348, 170, 357, 179, 363, 185, 370, 187, 359, 189, 356, 196, 364, 192, 355, 186, 347, 175, 319, 151, 313, 141, 300, 140, 282, 141, 259, 158, 275, 150, 249, 152, 226, 149, 207, 150, 180, 133, 217, 133, 225, 129, 204, 131, 189, 138, 166, 147, 149]
hairShadowOutline2 = [201, 197, 193, 208, 178, 247, 188, 239, 184, 256, 176, 278, 172, 290, 182, 288, 182, 287, 186, 275, 194, 257, 212, 209, 212, 192, 211, 173]
hairShadowOutline3 = [232, 176, 218, 200, 211, 226, 224, 218, 231, 225, 241, 222, 248, 225, 256, 226, 264, 235, 274, 227, 279, 218, 280, 232, 290, 224, 297, 218, 298, 205, 301, 197, 306, 210, 307, 222, 314, 209, 316, 196, 313, 186, 308, 174, 300, 162, 291, 151, 286, 144, 278, 138, 273, 133, 283, 150, 294, 179, 294, 189, 283, 181, 275, 186, 265, 183, 250, 186, 242, 175, 236, 173, 231, 176, 223, 190]
hairShadowOutline4 = [238, 91, 255, 91, 274, 94, 285, 94, 301, 93, 291, 99, 306, 108, 327, 122, 321, 127, 328, 142, 334, 157, 283, 106, 275, 102, 238, 92]
hairShadowOutline5 = [331, 166, 327, 191, 327, 211, 325, 239, 335, 220, 340, 198, 338, 218, 347, 205, 347, 192, 340, 176, 336, 185]
hairShadowOutline6 = [346, 141, 344, 149, 344, 170, 350, 187, 350, 214, 360, 194, 372, 203, 383, 211, 389, 215, 378, 200, 373, 186, 368, 173, 363, 163, 353, 149]
hairShadowOutline7 = [367, 214, 359, 225, 360, 237, 360, 246, 368, 236, 372, 224, 370, 217, 365, 214]
setColor(92, 64, 50)
polygon(convertCoordinates(hairShadowOutline1))
curve(convertCoordinates(hairShadowOutline1))
polygon(convertCoordinates(hairShadowOutline2))
curve(convertCoordinates(hairShadowOutline2))
polygon(convertCoordinates(hairShadowOutline3))
curve(convertCoordinates(hairShadowOutline3))
polygon(convertCoordinates(hairShadowOutline4))
curve(convertCoordinates(hairShadowOutline4))
polygon(convertCoordinates(hairShadowOutline5))
curve(convertCoordinates(hairShadowOutline5))
polygon(convertCoordinates(hairShadowOutline6))
curve(convertCoordinates(hairShadowOutline6))
polygon(convertCoordinates(hairShadowOutline7))
curve(convertCoordinates(hairShadowOutline7))

hairCoverOutline1 = [110, 248, 117, 306, 135, 317, 129, 298, 127, 284, 113, 252]
setColor(109, 76, 61)
polygon(convertCoordinates(hairCoverOutline1))
curve(convertCoordinates(hairCoverOutline1))


hairHighlightoutline1 = [85, 257, 85, 238, 89, 222, 94, 205, 93, 202, 91, 202, 87, 205, 85, 214, 82, 227, 82, 238, 82, 246]
hairHighlightoutline2 = [139, 154, 133, 168, 129, 185, 127, 199, 128, 207, 130, 195, 133, 178, 138, 165, 143, 154]
hairHighlightoutline3 = [157, 161, 152, 173, 150, 189, 150, 205, 151, 217, 158, 227, 162, 229, 164, 232, 156, 212, 156, 202, 157, 176, 163, 161]
hairHighlightoutline4 = [267, 127, 282, 135, 293, 144, 302, 152, 306, 160, 310, 166, 312, 174, 312, 183, 305, 169, 298, 159, 292, 152, 285, 142, 276, 135, 270, 130]
hairHighlightoutline5 = [334, 190, 332, 177, 327, 169, 327, 160, 328, 158, 333, 160, 335, 164, 337, 170, 336, 174, 336, 179, 335, 183]
hairHighlightoutline6 = [362, 180, 358, 171, 354, 163, 347, 153, 344, 147, 345, 142, 346, 142, 350, 145, 355, 149, 359, 156, 361, 163, 360, 170, 362, 174]
hairHighlightoutline7 = [230, 116, 231, 130, 231, 146, 229, 162, 227, 173, 224, 186, 233, 170, 237, 158, 238, 145, 237, 133, 235, 121]
setColor(175, 137, 114)
polygon(convertCoordinates(hairHighlightoutline1))
curve(convertCoordinates(hairHighlightoutline1))
polygon(convertCoordinates(hairHighlightoutline2))
curve(convertCoordinates(hairHighlightoutline2))
polygon(convertCoordinates(hairHighlightoutline3))
curve(convertCoordinates(hairHighlightoutline3))
polygon(convertCoordinates(hairHighlightoutline4))
curve(convertCoordinates(hairHighlightoutline4))
polygon(convertCoordinates(hairHighlightoutline5))
curve(convertCoordinates(hairHighlightoutline5))
polygon(convertCoordinates(hairHighlightoutline6))
curve(convertCoordinates(hairHighlightoutline6))
polygon(convertCoordinates(hairHighlightoutline7))
curve(convertCoordinates(hairHighlightoutline7))
coordinate = convertCoordinates([119, 209])
ellipse(coordinate[0], coordinate[1], 8, 22)
coordinate = convertCoordinates([182, 189])
ellipse(coordinate[0], coordinate[1], 13, 24)
coordinate = convertCoordinates([249, 185])
ellipse(coordinate[0], coordinate[1], 12, 16)
coordinate = convertCoordinates([275, 175])
ellipse(coordinate[0], coordinate[1], 19, 20)

setColor(81, 49, 2)
curve(convertCoordinates(hairOutline))

setColor(81, 49, 2)
curve(convertCoordinates(hairOutline2)) # details
curve(convertCoordinates(hairOutline3)) # details
curve(convertCoordinates(hairOutline4)) # details
curve(convertCoordinates(hairOutline5)) # details



# ear

earOutline = [182, 290, 176, 280, 171, 277, 164, 274, 157, 278, 151, 287, 151, 292, 151, 299, 153, 309, 156, 318, 161, 323, 167, 329, 172, 331, 175, 337, 180, 345, 185, 346, 189, 344]
earOutline2 = [183, 299, 174, 293, 166, 293, 161, 298, 161, 303]
earOutline3 = [177, 295, 174, 293, 168, 298, 166, 304, 166, 308]
earOutline4 = [169, 308, 171, 312, 171, 314, 179, 320, 185, 323, 188, 325, 189, 329]
earshadowOutline = [183, 298, 170, 292, 166, 292, 162, 295, 161, 300, 164, 304, 167, 307, 168, 308, 172, 314, 176, 318, 182, 321, 185, 322, 187, 318, 185, 309, 184, 302]

setColor(254, 245, 230)
setOutline("")
polygon(convertCoordinates(earOutline))

setColor(81, 49, 2)
curve(convertCoordinates(earOutline))

setColor(254, 234, 218)
polygon(convertCoordinates(earshadowOutline))
curve(convertCoordinates(earshadowOutline))

setColor(169, 118, 101)
curve(convertCoordinates(earOutline2))
curve(convertCoordinates(earOutline3))
curve(convertCoordinates(earOutline4))



# headwear: duck

duckOutline = [161, 83, 147, 86, 135, 95, 129, 104, 127, 113, 127, 122, 129, 132, 131, 140, 133, 146, 137, 150, 140, 154, 144, 157, 148, 160, 150, 160, 154, 162, 158, 162, 161, 162, 165, 162, 168, 162, 172, 162, 171, 161, 174, 159, 177, 158,182, 155, 193, 147, 197, 141, 199, 134, 200, 121, 199, 113, 195, 105, 189, 96, 183, 91, 177, 86, 169, 83, 162, 83, 156, 83, 150, 85]
duckMouthOutline1 = [168, 128, 163, 131, 162, 134, 161, 136, 162, 138, 166, 139, 170, 138, 173, 136, 176, 132, 177, 129, 173, 127, 168, 128]
duckMouthOutline2 = [162, 138, 162, 143, 166, 145, 171, 145, 175, 143, 180, 141, 182, 137, 182, 133, 179, 132, 175, 132]

setColor(255, 233, 95)
setOutline(115, 61, 23)
polygon(convertCoordinates(duckOutline))

setColor(115, 61, 23)
curve(convertCoordinates(duckOutline))

setColor(115, 61, 23)
coordinate = convertCoordinates([145, 117])
ellipse(coordinate[0], coordinate[1], 12, 12) #duck eye 1
coordinate = convertCoordinates([170, 104])
ellipse(coordinate[0], coordinate[1], 12, 12) #duck eye 2


setColor(245, 123, 40)
polygon(convertCoordinates(duckMouthOutline2))

setColor(191, 54, 8)
curve(convertCoordinates(duckMouthOutline2))

setColor(245, 123, 40)
polygon(convertCoordinates(duckMouthOutline1))

setColor(191, 54, 8)
curve(convertCoordinates(duckMouthOutline1))


# eye brows

eyebrowsOutline1 = [274, 245, 258, 243, 243, 239, 231, 235, 216, 231, 201, 226, 199, 227, 216, 234, 217, 235, 202, 231, 201, 231, 226, 240, 241, 245, 255, 248, 267, 251, 273, 252]
eyebrowsOutline2 = [325, 249, 345, 243, 370, 235, 349, 245, 371, 239, 354, 247, 339, 250, 337, 251]

setFill(133, 72, 53)
setOutline("")
polygon(convertCoordinates(eyebrowsOutline1))
polygon(convertCoordinates(eyebrowsOutline2))


# eye balls

eyewhiteOutline1 = [228, 257, 205, 277, 202, 285, 203, 291, 208, 299, 214, 301, 221, 303, 243, 302, 248, 300, 254, 295, 259, 288, 263, 281, 266, 272, 265, 266, 262, 262, 254, 257, 243, 254, 232, 255]
eyewhiteOutline2 = [338, 265, 331, 271, 327, 280, 326, 288, 326, 296, 328, 302, 341, 307, 346, 306, 350, 301, 351, 295, 352, 287, 353, 280, 352, 273, 348, 268, 341, 264]
eyewhiteShadowOutline1 = [201, 284, 264, 279, 266, 271, 266, 267, 264, 266, 262, 261, 247, 257, 234, 254, 204, 274, 202, 282, 200, 284]
eyewhiteShadowOutline2 = [325, 286, 353, 288, 354, 282, 352, 275, 348, 269, 339, 264, 330, 269, 329, 274, 325, 285]

setColor(255, 255, 255)
polygon(convertCoordinates(eyewhiteOutline1))
curve(convertCoordinates(eyewhiteOutline1))
polygon(convertCoordinates(eyewhiteOutline2))
curve(convertCoordinates(eyewhiteOutline2))

setColor(232, 228, 227)
polygon(convertCoordinates(eyewhiteShadowOutline1))
polygon(convertCoordinates(eyewhiteShadowOutline2))


eyeballOutline1 = [211, 267, 211, 273, 211, 280, 211, 291, 216, 298, 219, 299, 224, 301, 230, 302, 243, 301, 246, 299, 248, 294, 249, 288, 250, 281, 248, 272, 246, 266, 242, 260, 236, 256, 228, 255]
eyeballOutline2 = [337, 266, 330, 272, 327, 283, 325, 290, 327, 298, 329, 302, 339, 306, 342, 297, 346, 286, 346, 278, 345, 272, 342, 266, 336, 265]
eyeballShadowOutline1 = [213, 267, 212, 273, 211, 280, 211, 283, 250, 280, 248, 272, 246, 266, 242, 260, 236, 256, 228, 255]
eyeballShadowOutline2 = [337, 266, 330, 272, 329, 283, 328, 290, 328, 287, 344, 288, 346, 286, 346, 278, 345, 272, 342, 266, 336, 265]

setColor(177, 201, 249)
polygon(convertCoordinates(eyeballOutline1))
curve(convertCoordinates(eyeballOutline1))
polygon(convertCoordinates(eyeballOutline2))
curve(convertCoordinates(eyeballOutline2))

setColor(94, 123, 165)
polygon(convertCoordinates(eyeballShadowOutline1))
curve(convertCoordinates(eyeballShadowOutline1))
polygon(convertCoordinates(eyeballShadowOutline2))
curve(convertCoordinates(eyeballShadowOutline2))


eyeballHighlightOutline1 = [225, 302, 223, 299, 230, 295, 238, 297, 236, 302]
eyeballHighlightOutline2 = [330, 294, 335, 295, 338, 301, 335, 304, 329, 302, 327, 298]

setColor(218, 230, 254)
polygon(convertCoordinates(eyeballHighlightOutline1))
curve(convertCoordinates(eyeballHighlightOutline1))
polygon(convertCoordinates(eyeballHighlightOutline2))
curve(convertCoordinates(eyeballHighlightOutline2))


eyeblackOutline1 = [220, 281, 220, 286, 222, 288, 224, 292, 227, 294, 230, 295, 233, 295, 235, 294, 239, 291, 240, 288, 242, 284, 243, 279]
eyeblackOutline2 = [327, 285, 327, 290, 327, 294, 327, 298, 330, 298, 332, 297, 334, 295, 336, 292, 337, 289, 337, 285]

setColor(94, 123, 165)
polygon(convertCoordinates(eyeblackOutline1))
curve(convertCoordinates(eyeblackOutline1))
polygon(convertCoordinates(eyeblackOutline2))
curve(convertCoordinates(eyeblackOutline2))


eyeblackHighlightOutline1 = [231, 277, 229, 278, 227, 281, 227, 285, 228, 290, 229, 291, 231, 292, 232, 291, 234, 289, 235, 286, 235, 282, 234, 279, 232, 278, 230, 277]
eyeblackHighlightOutline2 = [326, 283, 331, 285, 332, 289, 331, 294, 329, 295, 326, 295]
eyeblackHighlightOutline3 = [234, 266, 229, 263, 219, 263, 226, 267, 214, 269, 212, 275, 223, 279, 229, 272, 235, 267]
eyeblackHighlightOutline4 = [333, 270, 330, 274, 329, 278, 334, 280, 338, 278, 340, 273, 338, 271]

setColor(145, 158, 205)
polygon(convertCoordinates(eyeblackHighlightOutline3))
polygon(convertCoordinates(eyeblackHighlightOutline4))
curve(convertCoordinates(eyeblackHighlightOutline3))
curve(convertCoordinates(eyeblackHighlightOutline4))

setColor(180, 212, 253)
curve(convertCoordinates(eyeblackHighlightOutline1))
line(convertCoordinates(215, 277, 224, 279))
line(convertCoordinates(223, 268, 227, 275))
line(convertCoordinates(235, 264, 233, 275))
line(convertCoordinates(245, 273, 236, 277))
curve(convertCoordinates(eyeblackHighlightOutline2))
line(convertCoordinates(330, 275, 330, 280))
line(convertCoordinates(336, 273, 334, 280))
line(convertCoordinates(341, 280, 335, 282))


# eye lashes

eyelashOutline1 = [191, 287, 202, 274, 201, 273, 192, 280, 200, 271, 208, 263, 219, 256, 231, 251, 242, 250, 253, 252, 260, 253, 266, 256, 270, 260, 271, 261, 262, 256, 256, 254, 250, 253, 254, 255, 259, 257, 264, 260, 268, 264, 260, 260, 251, 258, 242, 258, 233, 259, 229, 259, 223, 263, 214, 270, 206, 276, 203, 281, 199, 288, 199, 283, 201, 278, 197, 280, 194, 281, 202, 273]
eyelashOutline2 = [323, 284, 323, 277, 328, 269, 332, 264, 336, 262, 340, 262, 343, 263, 346, 265, 351, 267, 353, 270, 358, 277, 358, 279, 352, 271, 356, 280, 354, 280, 354, 282, 351, 276, 348, 270, 344, 268, 340, 267, 336, 268, 333, 270, 329, 273, 326, 277, 324, 280]

setColor(133, 72, 53)
polygon(convertCoordinates(eyelashOutline1))
polygon(convertCoordinates(eyelashOutline2))
line(convertCoordinates(218, 303, 243, 302))
line(convertCoordinates(327, 301, 342, 308))

eyeballLashOutline1 = [211, 270, 209, 280, 209, 288, 213, 294, 217, 299, 224, 302]
eyeballLashOutline2 = [331, 269, 328, 279, 325, 287, 325, 292, 326, 297, 329, 301]

setWidth(1)
curve(convertCoordinates(eyeballLashOutline1))
curve(convertCoordinates(eyeballLashOutline2))


# nose

noseOutline = [327, 321, 325, 322, 324, 324, 322, 327]

setColor(169, 118, 101)
setWidth(3)
curve(convertCoordinates(noseOutline))


print("Done")