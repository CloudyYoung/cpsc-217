#
#  CPSC 217 Exercise 4: Display a message that includes ordinal numbers
#

#
#  Put your implementation for int2ordinal here.  My implementation was 10
#  lines of code (not counting comments and blank lines).
#

def int2ordinal(number):
        if number % 10 == 1 and number % 100 != 11:
                return str(number) + "st"
        elif number % 10 == 2 and number % 100 != 12:
                return str(number) + "nd"
        elif number % 10 == 3 and number % 100 != 13:
                return str(number) + "rd"
        else:
                return str(number) + "th"




###############################################################################
#
#  Don't change any code below this point in the file.
#
###############################################################################

# Demonstrate the int2ordinal function by reading a day, month and year and
# displaying the entered values as ordinal numbers as part of a longer message.
def main():
  day = int(input("Enter a day between 1 and 31: "))
  month = int(input("Enter a month between 1 and 12: "))
  year = int(input("Enter a year between 1 and 2100: "))

  print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
        "month of the", int2ordinal(year), "year, something amazing happened!")

# Call the main function
main()
