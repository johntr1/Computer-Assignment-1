import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.sparse import csr_matrix

from read_coordinate_file import *
from plot_points import *
from construct_graph_connections import *
from construct_graph import *
from find_shortest_path import *


filename = 'SampleCoordinates.txt'
radius = 0.08
start_node = 0
end_node = 5
path = [0, 4, 3, 5]

print("Read_coordinate_file")
start = time.time()
coord_list = read_coordinate_file(filename)  # M

print("construct_graph_connections")

li_indices, li_distance = construct_graph_connections(coord_list, radius)  # J

N=len(li_indices)
print(N)

graph=construct_graph(li_indices, li_distance, N)  # M

end = time.time()

print(end-start)

find_shortest_path(graph, start_node, end_node)

plot_points(coord_list, li_indices, path)

construct_fast_graph_connections(coord_list, radius)
