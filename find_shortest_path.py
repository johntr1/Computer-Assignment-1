import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path


def find_shortest_path(graph, start_node, end_node):
    dist_matrix, predecessors = shortest_path(graph, method='D', directed=True, return_predecessors=True, indices=start_node)
    path = dist_matrix[end_node]
    print(dist_matrix)
    print(predecessors)
    #print(predecessors)
