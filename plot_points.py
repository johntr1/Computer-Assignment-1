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

    # Plot the connecting lines by connecting each indices with a for loop
    for i in range(len(indices)):
        x1 = x[indices[i][0]]
        x2 = x[indices[i][1]]
        y1 = y[indices[i][0]]
        y2 = y[indices[i][1]]
        plt.plot([x1, x2], [y1, y2], color='grey', linewidth=1)
    # Plot the red dots in the graph
    plt.plot(x, y, 'o', color='red')
    plt.show()
