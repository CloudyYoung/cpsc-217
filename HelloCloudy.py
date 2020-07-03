

print('Hello Hello Hello')

print('Hello','Hello','Hello')


print('Hello' * 3)

a = "ABCDEFG"
print(a[:-1])
print(a[2:5])

b=123456

print("Hello %s" % a) #Replace with
print("Hello %d" % b)

c="Cloudy"



print("Student {0}, {1} and {2} are in A521.".format("Jim","Tina","William"))


print("{:-^10}".format("Cloudy")) #Centered text within 10 characters 居中

print("{:-<10}".format("Cloudy")) #Left aligned text within 10 chars 左对齐
print("{:->10}".format("Cloudy")) #Right aligned text within 10 chars 右对齐





# Variable types: String Double Integer Boolean

bool_isRainy = True
int_age = 9
doub_money = 98.3
str_name = "Cloudy"

# Using input
# str_myName = input("What is your name?")
# print("Hello {0}, welcome!".format(str_myName))

# int_age = int(input("What is your age?"))
# print("You are {0} years old".format(int_age))

'''
str_word = input('What is your word?')
int_times = int(input("How many times?"))
print('I', str_word * int_times, 'like you.')
'''


def ageInTenYears(a):
    
    return a+10


print(ageInTenYears(10), 'years old')



# Single line notes
'''
Multiple lines notes
'''
"""
Or double quotation mark
"""

# Conditions
# if, elif, else

def yourOccupassion(age):
    if(age < 18):
        print('You are a student')
    elif(19 < age < 26):
        print('You are a university student')
    else:
        print('You are',age,'years old')


yourOccupassion(15)
yourOccupassion(25)
yourOccupassion(35)


# Recursion
# print 1~10
def printTen(num):
    if(num>10):
        return
    else:
        print(num)
        printTen(num+1)


printTen(1)




















