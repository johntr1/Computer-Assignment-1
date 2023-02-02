
from scipy import spatial
def construct_fast_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
    tree=spatial.cKDTree(coord_list)
    indices=tree.query_ball_point(coord_list, r=radius)
    for j in indices:
        for i in j:
            if j > i:
                continue
            append.li_indices([j i])
            distance = math.sqrt((coord_list[0][j] - coord_list[0][i]) ** 2 + (coord_list[1][j] - coord_list[1][i]) ** 2)
            append.li_distance(distance)
    print(indices)
    return li_indices, li_distance

    tree.query_ball_point()