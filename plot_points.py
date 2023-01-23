# Function name: plot_points
# Input:
# coord_list : A list of coordinates from the function read_coordinate_files
# Output:
# Plots the data

# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np


def plot_points(coord_list, indices):
    # Define empty lists
    x = []
    y = []
    # Loops through the array and appends appropriate coordinates in appropriate list
    for i in range(0, len(coord_list)):
        x.append(coord_list[i, 0])
        y.append(coord_list[i, 1])

    # Plots the function
    plt.plot(x, y)
    plt.show()
