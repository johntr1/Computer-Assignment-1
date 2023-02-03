import numpy as np
import math
from scipy import spatial
def construct_fast_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
    tree=spatial.cKDTree(coord_list)
    indices=tree.query_ball_point(coord_list, r=radius)
    for a,j in enumerate(indices):
        for i in j:
            if a > i:
                continue
            li_indices.append([j, i])
            distance = math.sqrt((coord_list[a][0] - coord_list[i][0]) ** 2 + (coord_list[a][1] - coord_list[i][1]) ** 2)
            li_distance.append(distance)
    print(indices)
    return li_indices, li_distance

    tree.query_ball_point()