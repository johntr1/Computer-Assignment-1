import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

# Om du ser detta har jag fixat så att det inte finns dubletter. Det är därför directed=False nu

def find_shortest_path(graph, start_node, end_node):
    dist_matrix, predecessors = shortest_path(graph, method='D', directed=False, return_predecessors=True, indices=start_node)
    path_distance = dist_matrix[end_node]
    print(path_distance)
    print(predecessors)

    # Var uttråkad på kvällen så kodade lite här
    path = [end_node]
    i = end_node
    while i != start_node:
        node = predecessors[i]
        path.append(node)
        i = predecessors[i]

    path.reverse()
    return path, path_distance





