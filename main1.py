import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.sparse import csr_matrix

from read_coordinate_file import *
from plot_points import *
from construct_graph_connections import *
from construct_graph import *
from find_shortest_path import *


filename = 'HungaryCities.txt'
radius = 0.005
start_node = 311
end_node = 702

print("Read_coordinate_file")
start = time.time()
coord_list = read_coordinate_file(filename)  # M

print("construct_graph_connections")

li_indices, li_distance = construct_graph_connections(coord_list, radius)  # J

# N is the amount of cities
N=len(coord_list)
print(N)

graph=construct_graph(li_indices, li_distance, N)  # M


print("find_shortest_path")
path, path_distance = find_shortest_path(graph, start_node, end_node)

print("plot_points")
plot_points(coord_list, li_indices, path)

end = time.time()
print(end-start)

construct_fast_graph_connections(coord_list, radius)
