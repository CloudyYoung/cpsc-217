
letter = input("Input your current letter grade: ")

letter = letter.upper()

if letter == 'A':
	gp = 4.0
elif letter == 'B':
	gp = 3.0
elif letter == 'C':
	gp = 2.0
elif letter == 'D':
	gp = 1.0
elif letter == 'F':
	gp = 0.0
else:
	gp = -1.0

if gp >= 0.0:
	print("A(n)", letter, "is equal to", gp, "grade points")
else
	print("Unvalid input")
