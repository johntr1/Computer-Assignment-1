import numpy as np
import matplotlib.pyplot as plt

from read_coordinate_file import *
from plot_points import *
from construct_graph_connections import *


filename = 'SampleCoordinates.txt'
radius = 0.08
coord_list = read_coordinate_file(filename)  # M

li_indices, li_distance = construct_graph_connections(coord_list, radius)  # J

plot_points(coord_list, li_indices)

construct_graph(indices, distance, N)  # M

csr_matrix((data, ij), shape=(M, N))

find_shortest_path(graph, start_node, end_node)

plot_points(coord_list, indices, path)

construct_fast_graph_connections(coord_list, radius)
