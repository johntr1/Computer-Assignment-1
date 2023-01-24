import numpy as np
import matplotlib.pyplot as plt

from read_coordinate_file import *
from plot_points import *
from construct_graph_connections import *

filename = 'SampleCoordinates.txt'
radius = 0.08
coord_list = read_coordinate_file(filename)  # M

plot_points(coord_list)  # J

li_indices, li_distance = construct_graph_connections(coord_list, radius)  # J
print(li_indices)
print(li_distance)

construct_graph(indices, distance, N)  # M

csr_matrix((data, ij), shape=(M, N))

plot_points(coord_list, indices)

find_shortest_path(graph, start_node, end_node)

plot_points(coord_list, indices, path)

construct_fast_graph_connections(coord_list, radius)
