"""
A very basic graph which will be developed to read, display and predict data, this is currently a class which just tests
the waters of matplotlib's visual display
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

# Select the style


# Read the data from the csv file
data = pd.read_csv('C:/Users/robbi/Python/maths/countries.csv')


# Create comparison conditions
us = data[data.country == 'United States']
china = data[data.country == 'China']

# Create an average growth per year
us_growth = us.population / us.population.iloc[0] * 100
china_growth = china.population / china.population.iloc[0] * 100

# Plot the x and y values onto the graph
plt.plot(us.year, us_growth, label="United States population")
plt.plot(china.year, china_cgrowth, label="Chinese population")

# Some title names for the graph
plt.title("Country growth")
plt.ylabel("Percentage growth")
plt.xlabel("Year")

# Display the legend
plt.legend()
plt.grid(True)

# Show the graph
plt.show()


# Generate some random data to test out the csv read
def data():
    i = 0
    while i < 20:
        i += 1
        print(i,",",randint(1,20))
