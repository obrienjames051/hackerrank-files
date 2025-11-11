# basic functions:

course = 'Python for Beginners'
print(course.replace('for', '4'))  # Replaces 'for' with '4' in the string
print(course.upper())  # Converts the string to uppercase
print(course.find('P'))  # Finds the index of 'P' in the string
print('Python' in course)  # Checks if 'Python' is in the string, returns boolean

price = 5
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print(not price > 10)
# logical operators: and, or, not - all work as above


#-------------------------------------------------------------------------------------
# basic maths:

print(10/3) # gives decimal
print(10//3) # gives integer
print(10%3) # gives remainder
print(10**3) # gives power

x = 10
x += 3  # Equivalent to x = x + 3
y = 3 > 2 # returns boolean
# == - equal to
# != - not equal to
# <= - less than or equal to


#-------------------------------------------------------------------------------------
# loops:

x = 1
while x <= 5: # a while loop runs as long as the condition is true
    print(x * '*')
    x += 1

for i in range(5): # a for loop iterates over a sequence of numbers
    print(i * '*')


#-------------------------------------------------------------------------------------
#list functions:

numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adds 6 to the end of the list
numbers.insert(6, 7) # Inserts 7 at index 6
numbers.remove(3)  # Removes the first occurrence of 3
print(1 in numbers)  # Checks if 1 is in the list, returns boolean
print(len(numbers))  # Returns the length of the list
print(numbers[1]) # Accesses the element at index 1

for number in numbers:
    print(number)  # Prints each number in the list

Nums = range(5, 10, 2) # Creates a range from 5 to 10 with a step of 2 e.g., 5, 7, 9

NUMBERS = (1, 2, 3) # () defines a tuple, elements in a tuple cannot be changed
NUMBERS.count(2)  # Counts occurrences of 2 in the tuple


#-------------------------------------------------------------------------------------
# string module:

import string

print (string.ascii_letters) #gives all letters of the alphabet lowercase then upper
print (string.ascii_lowercase) #gives all lowercase letters
print (string.ascii_uppercase) #gives all uppercase letters
print (string.digits) #gives all digits 0-9
print (string.punctuation) #gives all punctuation !"#$ etc...