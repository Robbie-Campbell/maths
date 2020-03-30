"""
A very basic graph which will be developed to read, display and predict data, this is currently a class which just tests
the waters of matplotlibs visual display
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# Select the style
style.use("ggplot")

# Read the data from the csv file
x,y = np.loadtxt("C:/Users/robbi/Python/maths/data.csv",unpack=True,delimiter=",")

# Plot the x and y values onto the graph
plt.plot(x,y)

# Some random title names for the graph
plt.title("Epic Chart")
plt.ylabel("Age")
plt.xlabel("Hello there")

# Show the graph
plt.show()

# Generate some random data to test out the csv read
def data():
    i = 0
    while i < 20:
        i += 1
        print(i,",",randint(1,20))
