'''
Day-12
'''
# OPPS

# A simple example class
class Test:
    def fun(self):
        print("Hello")
obj = Test()
obj.fun()

# A Sample class with init method
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello', self.name)
 
p = Person('Ayush')
p.say_hi()

# Python program to show that the variables with a value
# assigned in class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
  
# Class for Computer Science Student
class CSStudent:
    stream = 'cse'            
    def __init__(self, roll):
        self.roll = roll      
a = CSStudent(101)
b = CSStudent(102)
print(a.stream)
print(b.stream)
print(a.roll) 
print(CSStudent.stream) 