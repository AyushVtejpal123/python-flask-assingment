'''
Day-17
Matplotlib
'''
import matplotlib.pyplot as plt

# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]
# plotting the data
plt.plot(x, y)
# Adding the title
plt.title("Simple Plot")
# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()


# program to show pyplot module
from matplotlib.figure import Figure 
# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4)) 
# Creating a new axes for the figure
ax = fig.add_axes([1, 1, 1, 1]) 
# Adding the data to be plotted
ax.plot([2, 3, 4, 5, 5, 6, 6], [5, 7, 1, 3, 4, 6 ,8])
plt.show()


# data to display on plots 
x = [3, 1, 3] 
y = [3, 2, 1] 
z = [1, 3, 1] 
  
# Creating figure object 
plt.figure() 
  
# addind first subplot 
plt.subplot(121) 
plt.plot(x, y) 
  
# addding second subplot 
plt.subplot(122) 
plt.plot(z, y)