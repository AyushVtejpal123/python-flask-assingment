'''DAY 3 : ASSIGNMENT TO PUSH ON GITHUB'''
'''
AGE CALCULATOR 
1)  calculate Age of a person - User should enter the year of birth and the program should output the age.. eg : entered value is 1990, output age is 30

'''
print("\t\tAge Calculator")
currentYear = 2021
bornYear = int(input("Enter the year in which you born? "))
age = currentYear-bornYear
print("You'r Age is {} and you 'r born in {}".format(age, bornYear))
'''
2) Simple Calculator:
	- get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers
'''
print("\t\tSimple Calculator")
FirstNo = int(input("Enter the First number :\n"))
SecondNo = int(input("Enter the Second number :\n"))
print(f"The sum of  {FirstNo }  and {SecondNo} is {FirstNo+SecondNo}")
print(f"The diffrence of {FirstNo } and {SecondNo} is {FirstNo-SecondNo}")
print(f"The product of {FirstNo } and {SecondNo} is {FirstNo*SecondNo}")
print(f"the square of {FirstNo } and {SecondNo} is {FirstNo**SecondNo}")
print(f"After dividing {FirstNo } and {SecondNo} the quotient is {FirstNo/SecondNo} in decimal numbers")
print(f"After dividing {FirstNo } and {SecondNo} the quotient is {FirstNo//SecondNo} in Integer")
print(f"After dividing {FirstNo } and {SecondNo} the remainder is {FirstNo%SecondNo} ")
