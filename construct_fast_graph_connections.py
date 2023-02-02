
from scipy import spatial
def construct_fast_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
    tree=spatial.cKDTree(coord_list)
    indices=tree.query_ball_point(coord_list, r=radius)
    for j in indices:
        for i in j:
            if j < i:
                continue

    print(indices)
    return li_indices, li_distance

    tree.query_ball_point()