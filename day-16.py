# Day 16:

import pandas as pd

# 1. Write a Pandas program to convert a dictionary to a Pandas series.
# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# Converted series:
# a 100
# b 200
# c 300
# d 400
# e 800
# dtype: int64

d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)

# 2. Write a Pandas program to get the powers of an array values element-wise. 
# Note: First array elements raised to powers from second array
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# Expected Output:
# X Y Z
# 0 78 84 86
# 1 85 94 97
# 2 96 89 96
# 3 80 83 72
# 4 86 86 83

df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

# 3. Use any 5 pandas function on a excel dataset imported as a dataframe.
