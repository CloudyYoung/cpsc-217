
age = 0

while(age >= 0):

	age = float(input('Enter an age in human years: '))

	if age >= 2:
		youngAge = 2
		adultAge = age - 2
	else:
		youngAge = age
		adultAge = 0

	dogAge = youngAge * 10.5 + adultAge * 4.0

	if age >= 0:
		print('That’s equivalent to', dogAge, 'dog years.')