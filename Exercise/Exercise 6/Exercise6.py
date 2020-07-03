dictionary = {"T": "Alberta", "V": "British Columbia", "R": "Manitoba", "E": "New Brunswick", "A": "Newfoundland", "B": "Nova Scotia", "X": "Nunavut or Notrhwest Territories", "K": "Ontario", "L": "Ontario", "M": "Ontario", "N": "Ontario", "P": "Ontario", "C": "Prince Edward Island", "G": "Quebec", "H": "Quebec", "J": "Quebec", "S": "Saskatchewan", "Y": "Yukon"}
postalCode = input("Enter a 6 character postal code (A1A1A1): ")
print(dictionary[postalCode.upper()[0]])
