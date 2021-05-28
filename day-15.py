import numpy as np
# Day 15:
# 1. Write a NumPy program to print the NumPy version in your system.  
print(f"Numpy version is {np.__version__}")
print()
# 2. Write a NumPy program to convert a list of numeric value into a two-dimensional NumPy array. 
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32]
# Two-dimensional NumPy array: [ [ 12.23 13.32 100. 36.32 ] ]
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a=np.array([l]) 
print("Two-dimensional NumPy array:",a)
print()
# 3.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]
x =  np.arange(2, 11).reshape(3,3)
print(x)
