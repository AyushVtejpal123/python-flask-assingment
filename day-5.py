# Assignment for For Loops

# 1. From range n to m, print all the numbers divisible by 5 and 7 both

start_num = int(input("please enter the starting number : "))
end_num = int(input("please enter the ending number : "))
i = start_num
for i in range(end_num):
    if i % 7 == 0 and i % 5 == 0:
        print(i, " is divisible by 7 and 5.")
    i += 1
# 2. Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms
# Given:
# number_of_terms = 5
# So series will become 2 + 22 + 222 + 2222 + 22222
# Expected output:
# 24690
# Hint: 'a'*2 = 'aa'
num = int(input("Please enter a number:"))
res = 0
st = '2'
for i in range(1, num+1):
    a = int(st * i)
    res += a
print(res)
########### Assignment for While Loops

# 3. Take integer inputs from user until he/she presses q(Ask to press q to quit after every integer input). Print the sum of all numbers. (Use while loop)
sum = 0
c = 0
while 1:
    num = int(input("Enter a  numbers"))
    c = c+1
    sum = sum+num
    print("Press q when you are done inputting the numbers or y to continue")
    m = input()
    if m == 'q':
        break

print("Average", sum/c)
print("Sum", sum)


# 4.  Write a loop to find the factorial of any number
# The factorial(symbol: !) means to multiply all whole numbers from our chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:

# 120
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial = factorial*i
       print("The factorial of", num, "is", num*i)
# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e
st = input("Please Enter some text :")
for i in range(len(st)):
    end_value = '-'
    if st[i] == ' ' or i == len(st)-1 or st[i+1] == ' ':
        end_value = ''
    if i % 2 == 0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i].lower(), end=end_value)
print()
num = 5
res = 0
st = '2'
for i in range(1, num+1):
    a = int(st * i)
    res += a

print(res)
