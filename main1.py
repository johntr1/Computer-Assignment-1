import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.sparse import csr_matrix
from tabulate import tabulate

from read_coordinate_file import *
from plot_points import *
from construct_graph_connections import *
from construct_graph import *
from find_shortest_path import *


filename = 'GermanyCities.txt'
radius = 0.0025
start_node = 31
end_node = 2

start = time.time()

coord_list = read_coordinate_file(filename)  # M

end = time.time()

read_coordinate_file_time = end-start

print("construct_graph_connections")

start = time.time()

li_indices, li_distance = construct_graph_connections(coord_list, radius)  # J

end = time.time()

construct_graph_connections_time = end-start

# N is the amount of cities
N=len(coord_list)

start = time.time()

graph=construct_graph(li_indices, li_distance, N)  # M

end = time.time()

construct_graph_time = end-start

print("find_shortest_path")

start = time.time()

path, path_distance = find_shortest_path(graph, start_node, end_node)

end = time.time()

find_shortest_path_time = end-start

print("plot_points")

start = time.time()

plot_points(coord_list, li_indices, path)

end = time.time()

plot_points_time = end-start

table = [["Functions", "Time (s)"], ["read_coordinate_file", read_coordinate_file_time], ["construct_graph_connections", construct_graph_connections_time], ["construct_graph", construct_graph_time], ["find_shortest_path", find_shortest_path_time], ["plot_points", plot_points_time]]

print(tabulate(table))

start = time.time()
construct_fast_graph_connections(coord_list, radius)
end = time.time()
