'''
Day-13
inheritance
'''
# A Python program to demonstrate inheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):
	# Constructor
	def __init__(self, name):
		self.name = name
	# To get name
	def getName(self):
		return self.name
	# To check if this person is an employee
	def isEmployee(self):
		return False
class Employee(Person):
	# Here we return true
	def isEmployee(self):
		return True
emp = Person("A1")
print(emp.getName(), emp.isEmployee())

emp = Employee("A2")
print(emp.getName(), emp.isEmployee())




# Python code to demonstrate how parent constructors
# are called.
# parent class
class Person( object ):	
    	def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post
				Person.__init__(self, name, idnumber)
a = Employee('Rahul', 886012, 200000, "Intern")	
a.display()
