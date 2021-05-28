'''
Day-11 
'''
# File handling

# opening a file
file = open('files_data.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)

# Creating a file
file = open('hello.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


import os
cwd = os.getcwd()
print("Current working directory:", cwd)


# Changing the Current directory
print("Current working directory before")
print(os.getcwd())
print()
os.chdir('../')
print("Current working directory After")
print(os.getcwd())
print()