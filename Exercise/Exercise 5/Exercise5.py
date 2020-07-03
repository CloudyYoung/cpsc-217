line = " "
lines = []

while(line != ""):
	line = input("Enter a value (blank line to quit): ")
	if line != "":
		lines.append(line)

for each in range(len(lines), 0, -1):
	print(lines[each - 1])
