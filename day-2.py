'''
Day 2 :-

Assignment

Create a small program 

1. Take variables with values of different types

2. Print these in different lines and with appropriate messages (use .format())

3. Practice Type conversion functions
(str(), int(), etc)
'''
# Creating Variables
name = "Ayush.v.tejpal"
age = 13
ProgrammingInPython = True
# Runned suceesfully
print("Name is {} . I'm {} years old .\n".format(name, age))
#  before changes
print(name)
# <module>
# ValueError: invalid literal for int() with base 10: 'Ayush.v.tejpal'
# Error of changing str into int
# Error will come here
# After changes
int(name)   
print(name)
# Runned suceesfully
# Before changes
print(age)
# After changes
str(age)
print(age)
