'''
Day-10
Recursive function
'''
# factorial of a number using Recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = int(input("Enter a number"))
print("The factorial of", num, "is", factorial(num))


# Fibonacci of n using Recursive function
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number "))
print(fibonacci(n))