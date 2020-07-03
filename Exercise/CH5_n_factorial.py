n = int(input("N VALUE: "))

output = 1
for each in range(n):
	output *= each + 1

print("The factorial of", n, "is", output)