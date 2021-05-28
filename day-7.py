'''
Day 7:
'''
# 1. Give all the index values of vowels.
# Eg. "abed"
# >> 0 2
Str = input("Please enter a string")
print("The original string is : " + Str)
for ele in range(len(Str)):
    if Str[ele] in "aeiou":
       print(f"The vovels are at index of {ele} ")
# 2.
# Reverse the words of a string
# Input... hello world happy birthday
# Output... birthday happy world hello
string = input("Please enter a string")
split_str = string.split(' ') 
reversed_str = reversed(split_str)
final_str = ' '.join(reversed_str) 
print("Reversed string: ", final_str)
# 3. Remove duplicate elemnts without using set()
# Ex.
# [1, 2, 3, 3, 2, 4]
# >> [1, 2, 3, 4]
a = [2, 3, 3, 2, 5, 4, 4, 6]
print(f"orignal list is {a}")
b = []
for i in a:
    if i not in b:
        b.append(i)
print(f"after removing duplicate item from list is {b}")