'''
Day 9:
'''
# 1. Take a number from user and check whether it is prime or not. Use parameters to send the number to function.

# Eg. Enter a number 3
# 3 is prime

def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num//i, "is", num)
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
numb = int(input("Enter a number: "))
prime(numb)

# 2. Write a function to print n factorial. Take n value as user input and pass as a parameter
# Eg. Enter a number 5
# 120

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number : "))
print(f"factorial of {n} is {factorial(n)}")
