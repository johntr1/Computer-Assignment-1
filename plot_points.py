# Function name: plot_points
# Input:
# coord_list : A list of coordinates from the function read_coordinate_files
# Output:
# Plots the data

# Import the necessary libraries
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def plot_points(coord_list, indices, path):
    # Define empty lists
    x = []
    y = []
    li = []
    x_path = []
    y_path = []

    # Loops through the array and appends appropriate coordinates in appropriate list
    for i, element in enumerate(coord_list):
        x.append(element[0])
        y.append(element[1])

    # Appending the connecting line coordinates to a list in a for loop
    for j, ind_element in enumerate(indices):
        x1 = x[ind_element[0]]
        x2 = x[ind_element[1]]
        y1 = y[ind_element[0]]
        y2 = y[ind_element[1]]
        li.append([(x1, y1), (x2, y2)])

    # Appending the x and y coordinates for the given path
    for k, path_element in enumerate(path):
        x_path.append(x[path_element])
        y_path.append(y[path_element])


    # Use the function LineCollection to further optimize the program
    lc = LineCollection(li, colors='grey')
    fig, ax = plt.subplots()
    # Add the Linecollection to the axis so that it shows in the figure
    ax.add_collection(lc)

    # Plot the red dots in the graph
    plt.plot(x, y, 'o', color='red')
    plt.plot(x_path, y_path, color='blue', linewidth='2.5')
    plt.show()
