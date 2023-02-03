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
FILENAME = 'GermanyCities.txt'
RADIUS = 0.0025
START_NODE = 31
END_NODE = 2


# Collection of all written functions for this assignment
def read_coordinate_file(FILENAME):
    # Open file in read mode and get data
    with open(f'{FILENAME}', mode='r') as file:
        line = file.readline()
        # An empty string that can save the degree coordinates in
        l = ''
        while line:  # A while loop for each line in the file
            # Removes everything that't not a number or a .
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('\n', ',')
            # Adds it to a long string
            l = l + line
            line = file.readline()
    # Splits the string and removes the last string which is empty
    l = l.split(',')
    l.pop()
    # Defines the right shape of the array and makes it with float as values
    shape = (int(len(l) / 2), 2)
    ab = np.empty(shape, dtype=float)
    n = 0
    # A for loop that fills the array with as [a b] from the list made
    for i in l:
        i = float(i)
        if n % 2 == 0:
            ab[int(n / 2)][0] = i
        else:
            ab[int(n / 2)][1] = i
        n += 1
    R = 1
    coor = np.zeros(shape, dtype=float)
    for a in range(len(ab)):
        coor[a][0] = R * np.pi * ab[a][1] / 180
        coor[a][1] = R * np.log(np.tan(np.pi / 4 + np.pi * ab[a][0] / 360))
    return coor


def construct_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
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
            # Checks for radius and that it is not the same coordinate
            if distance <= radius:
                li_indices.append([i, j])
                li_distance.append(distance)
    # Convert the lists to ndarrays
    li_indices = np.array(li_indices)
    li_distance = np.array(li_distance)
    return li_indices, li_distance


def construct_fast_graph_connections(coord_list, RADIUS):
    li_indices = []
    li_distance = []
    tree = spatial.cKDTree(coord_list)
    indices = tree.query_ball_point(coord_list, r=RADIUS)
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
    indicesT = indices.T
    data = distance
    row = indicesT[0][:]
    col = indicesT[1][:]
    csr = csr_matrix((data, (row, col)), shape=(N, N))
    return csr


def find_shortest_path(graph, start_node, end_node):
    dist_matrix, predecessors = shortest_path(graph, method='D', directed=False, return_predecessors=True,
                                              indices=start_node)
    path_distance = dist_matrix[end_node]

    path = [end_node]
    i = end_node
    while i != start_node:
        node = predecessors[i]
        path.append(node)
        i = predecessors[i]

    path.reverse()
    return path, path_distance


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


# The main code
start = time.time()

coord_list = read_coordinate_file(FILENAME)  # M

end = time.time()

read_coordinate_file_time = end - start

start = time.time()

# li_indices, li_distance = construct_graph_connections(coord_list, RADIUS) # J

li_indices, li_distance = construct_fast_graph_connections(coord_list, RADIUS)

end = time.time()

construct_graph_connections_time = end - start

# N is the amount of cities
N = len(coord_list)

start = time.time()

graph = construct_graph(li_indices, li_distance, N)  # M

end = time.time()

construct_graph_time = end - start

start = time.time()

path, path_distance = find_shortest_path(graph, START_NODE, END_NODE)

end = time.time()

find_shortest_path_time = end - start

start = time.time()

plot_points(coord_list, li_indices, path)

end = time.time()

plot_points_time = end - start

table = [["Functions", "Time (s)"], ["read_coordinate_file", read_coordinate_file_time],
         ["construct_(fast)_graph_connections", construct_graph_connections_time], ["construct_graph", construct_graph_time],
         ["find_shortest_path", find_shortest_path_time], ["plot_points", plot_points_time]]

print(tabulate(table))
