import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

# Om du ser detta har jag fixat så att det inte finns dubletter. Det är därför directed=False nu

def find_shortest_path(graph, start_node, end_node):
    dist_matrix, predecessors = shortest_path(graph, method='D', directed=False, return_predecessors=True, indices=start_node)
    path = dist_matrix[end_node]
    print(dist_matrix)
    print(predecessors)

