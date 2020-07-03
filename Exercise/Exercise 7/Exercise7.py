
import re

name = input("Enter the name of a file: ")
content = open(name, "r").read()

print("That file contains", len(re.findall(r"[\,|\s]\S", content)) + 1, "values.")
