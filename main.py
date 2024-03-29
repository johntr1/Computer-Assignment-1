# DAT171 Computer Assignment 1
# 2023-02-03
# John Tran
# Martin Diderholm

# Imports used in all the different functions
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import math
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from scipy import spatial
from tabulate import tabulate

# Fixed variables given by the assignment
filename = 'GermanyCities.txt'

if filename=='GermanyCities.txt':
    radius = 0.0025
    start_node = 31
    end_node = 2
elif filename=='HungaryCities.txt':
    radius=0.005
    start_node=311
    end_node=702
elif filename=='SampleCoordinates.txt':
    radius=0.08
    start_node=0
    end_node=5


# Collection of all written functions for this assignment
def read_coordinate_file(filename): #Skriva om så att allt händer i en loop och inte uppdelat flera fråga om detta.
    """This function reads a given file and parses the result into an array:
           FILENAME (string): The name of the file which the data is taken from.

       Returns:
           coord_list (ndarray): A 2D ndarray with the x and y coordinates of the cities.
       """
    # Open file in read mode and get data
    with open(f'{filename}', mode='r') as file:
        line = file.readline()
        R = 1
        # An empty string that can save the degree coordinates in
        list=[]
        while line:  # Removes everything that's not a number
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('\n', ',')
            # Adds it to a long string
            # Splits the string and removes the last string which is empty
            line = line.split(',')
            line.pop()
            line[0] = float(line[0])
            line[1] = float(line[1])


            x = R * np.pi * line[1] / 180
            y = R * np.log(np.tan(np.pi / 4 + np.pi * line[0] / 360))

            list = list + [[x,y]]
            line = file.readline()
    # Defines the right shape of the array and makes it with float as values
    coor=np.array(list, dtype=float)
    return coor


def construct_graph_connections(coord_list, radius):
    """This function computes all connections between the cities' coordinates given a radius.
    Parameters:
        coord_list (ndarray): 2D ndarray of the cities' coordinates
        RADIUS (float): Number that describes the allowed radius between two cities to establish a connection

    Returns:
        li_indices (ndarray): A 2D ndarray with the connected cities' indices
        li_distance (ndarray): An ndarray with the distance between the connected distance
    """

    # Define empty lists
    li_indices = []
    li_distance = []

    # Loops through the enumerated coord_list twice with nestled loops
    for i, i_element in enumerate(coord_list):
        for j, j_element in enumerate(coord_list):
            # Checks for reverse order duplicates and skips if true
            if i >= j:
                continue
            # Define the x and y for the distance formula for readability
            x1 = i_element[0]
            y1 = i_element[1]
            x2 = j_element[0]
            y2 = j_element[1]
            # Distance formula: distance=√((x2 – x1)² + (y2 – y1)²) (taken from maths book)
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            # Checks if the distance between the two cities are fulfilling the radius requirement
            # Appends the list of indices and the distance between them if true
            if distance <= radius:
                li_indices.append([i, j])
                li_distance.append(distance)
    # Convert the lists to ndarrays
    li_indices = np.array(li_indices)
    li_distance = np.array(li_distance)
    return li_indices, li_distance


def construct_fast_graph_connections(coord_list, radius):
    """This function computes all connections between the cities' coordinates given a radius.
    Parameters:
        coord_list (ndarray): 2D ndarray of the cities' coordinates
        RADIUS (float): Number that describes the allowed radius between two cities to establish a connection

    Returns:
        li_indices (ndarray): A 2D ndarray with the connected cities' indices
        li_distance (ndarray): An ndarray with the distance between the connected distance
    """

    li_indices = []
    li_distance = []
    # Makes a KDTree then finds the points which are within the radius for each point
    tree = spatial.cKDTree(coord_list)
    indices = tree.query_ball_point(coord_list, r=radius)
    # For loop that converts the information to later make an array
    # also calculates and matches the distance with the connections
    for a, j in enumerate(indices):
        for i in j:
            if a > i:
                continue
            li_indices.append([a, i])
            distance = math.sqrt(
                (coord_list[a][0] - coord_list[i][0]) ** 2 + (coord_list[a][1] - coord_list[i][1]) ** 2)
            li_distance.append(distance)

    li_indices = np.array(li_indices)
    li_distance = np.array(li_distance)
    return li_indices, li_distance


def construct_graph(indices, distance, N):
    """This function constructs a sparse graph (csr matrix) of the coordinates between two cities and their distance between them.
        Parameters:
            indices (ndarray): A 2D ndarray with the connected cities' indices
            distance (ndarray): An ndarray with the distance between the connected distance
            N (int) = The amount of cities

        Returns:
            csr (ndarray)= The cities connected as indexes and their distance between them as the value
        """

    # Changes the format so csr_matrix function can be used
    indices_T = indices.T
    data = distance
    row = indices_T[0][:]
    col = indices_T[1][:]
    csr = csr_matrix((data, (row, col)), shape=(N, N))
    return csr


def find_shortest_path(graph, start_node, end_node):
    """This function constructs a sparse graph (csr matrix) of the coordinates between two cities and their distance between them.
            Parameters:
                csr (ndarray)= The cities connected as indexes and their distance between them as the value
                start_node (int) = The city where the route starts
                end_node (int) = The city where the route ends

            Returns:
                path (list)= The shortest path from the start node to the end note
                path_distance (float) = The distance of the shortest path taken
            """
    # Uses the crs matrix, with directed=false as we don't have any duplicates
    # predecessors=true because we want the path taken, choosing Dijkstra’s algorithm
    dist_matrix, predecessors = shortest_path(graph, method='D', directed=False, return_predecessors=True,
                                              indices=start_node)
    path_distance = dist_matrix[end_node]

    path = [end_node]
    i = end_node
    # While loop that goes backwards using predecessors to find the path taken
    while i != start_node:
        node = predecessors[i]
        path.append(node)
        i = predecessors[i]

    path.reverse()
    return path, path_distance


def plot_points(coord_list, indices, path):
    """This function plots the cities' coordinates as red nodes, the connected lines between the connected cities as grey lines and the shortest path to take between the start city to the end city as a blue line
    Parameters:
        coord_list (ndarray): 2D ndarray of the cities' coordinates
        indices (ndarray): 2D ndarray of pairs of connected cities represented as indices
        path (list): A 1xN list that describes the shortest path from start- to end city
    Returns:
        A figure showing the shortest path between two cities in a country
    """
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

    # Plot the red dots in the graph
    fig, ax = plt.subplots()
    plt.plot(x, y, 'o', markersize=3, color='red')
    plt.title('Shortest Path')

    # Use the function LineCollection to further optimize the program
    lc = LineCollection(li, colors='grey', linewidths=0.8)
    # Add the Linecollection to the axis so that it shows in the figure
    ax.add_collection(lc)

    # Plot the shortest path
    plt.plot(x_path, y_path, color='blue', linewidth='1.5')

    plt.show()


# The main code

# For every function, a timer will be taken between each one of them. This is represented with a start = time.time()
# and an end = time.time() whereas the function is inbetween.

# Call read_coordinate_file and time its running time
start = time.time()

coord_list = read_coordinate_file(filename)

end = time.time()

read_coordinate_file_time = end - start

# Call construct_graph_connections and time its running time
start = time.time()

# Remove or comment the line below to exclude running the slower version of the function.
#li_indices, li_distance = construct_graph_connections(coord_list, radius)

end = time.time()

construct_graph_connections_time = end - start

# Call construct_fast_graph_connections and time its running time
start = time.time()

li_indices, li_distance = construct_fast_graph_connections(coord_list, radius)

end = time.time()

construct_fast_graph_connections_time = end - start

# N is the amount of cities
N = len(coord_list)

# Call construct_graph and time it
start = time.time()

graph = construct_graph(li_indices, li_distance, N)

end = time.time()

construct_graph_time = end - start

# Call find_shortest_path and time it
start = time.time()

path, path_distance = find_shortest_path(graph, start_node, end_node)

end = time.time()

find_shortest_path_time = end - start

# Call plot_points and time it
start = time.time()

plot_points(coord_list, li_indices, path)

end = time.time()

plot_points_time = end - start

# Save table with recorded times for each function to later print it out
table = [["Functions", "Time (s)"], ["read_coordinate_file", read_coordinate_file_time],
         ["construct_graph_connections", construct_graph_connections_time],
         ["construct_fast_graph_connections", construct_fast_graph_connections_time],
         ["construct_graph", construct_graph_time],
         ["find_shortest_path", find_shortest_path_time], ["plot_points", plot_points_time]]
print(tabulate(table))

print(f'The path taken is: {path}')
print(f"The path's distance is: {path_distance}")
