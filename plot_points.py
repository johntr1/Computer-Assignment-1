# Function name: plot_points
# Input:
# coord_list : A list of coordinates from the function read_coordinate_files
# Output:
# Plots the data

# Import the necessary libraries
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def plot_points(coord_list, indices):
    # Define empty lists
    x = []
    y = []
    li = []
    # Loops through the array and appends appropriate coordinates in appropriate list
    for i in range(0, len(coord_list)):
        x.append(coord_list[i, 0])
        y.append(coord_list[i, 1])

    # Appending the connecting line coordinates to a list in a for loop
    for j in range(len(indices)):
        x1 = x[indices[j][0]]
        x2 = x[indices[j][1]]
        y1 = y[indices[j][0]]
        y2 = y[indices[j][1]]
        li.append([(x1, y1), (x2, y2)])

    # Use the function LineCollection to further optimize the program
    lc = LineCollection(li, colors='grey')
    fig, ax = plt.subplots()
    # Add the Linecollection to the axis so that it shows in the figure
    ax.add_collection(lc)

    # Plot the red dots in the graph
    plt.plot(x, y, 'o', color='red')
    plt.show()
