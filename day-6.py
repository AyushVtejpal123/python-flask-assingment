'''
 Day 6.
Common part -> Create a list of n numbers
'''
# Q1. Count even numbers and odd numbers
list1 = [10, 21, 4, 45, 66, 93, 1]
for num in list1:
    if num % 2 == 0:
        even_no = num
        print("Even number's are :")
        print("Even number in list are {}".format(even_no))
    else:
        odd_no = num
        print("Odd number 's are:")
        print("Odd number in list are {}".format(odd_no))
# Q2. Tell max and min of the list(without using any inbuilt function like max(), min())
arr = [10, 21, 4, 45, 66, 93, 1]
min = arr[0]
for a in arr:
    if a < min:
        min = a
print("The minimum number in the list is: ", min)
max = arr[0]
for a in arr:
    if a > max:
        max = a
print("The maximum number in the lit is: ", max)
# Q3. Check whether the whole list is palindrome or not(eg. [1, 2, 1] gives yes for palindrome while [1, 2, 2] doesn't
palindromeOrNot = [1, 2, 3]
check = palindromeOrNot.reverse()
if palindromeOrNot==check:
    print("It is a Palindrome ")
else:
    print("It is not a Palindrome ")
# Q4. Print the numbers which are palindrome inside the list
arr = []
num = int(input("Enter number of elements in list: "))
for i in range(0, num):
    ele = int(input("Enter elements: "))
    arr.append(ele)
print("Palindrome numbers are:")
for i in arr:
    num = str(i)
    if("".join(reversed(num)) == num):
        print(i)
