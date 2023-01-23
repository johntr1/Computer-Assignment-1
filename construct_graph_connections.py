# Function name: construct_graph_connections
# Input:
# coord_list : a list of coordinates
# radius : radius to determine which cities connect
# Output:
# ndarray with indices of each connected city and another array with distance between them
import numpy as np

coord_list = np.array([[1, 2], [2, 4], [3, 7], [4, 8]])
radius = 2


def construct_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
    for i in range(len(coord_list)):
        for j in range(len(coord_list)):
            # Define the x and y for the distance formula for readability
            x1 = coord_list[i, 0]
            y1 = coord_list[i, 1]
            x2 = coord_list[j, 0]
            y2 = coord_list[j, 1]
            # Distance formula: distance=√((x2 – x1)² + (y2 – y1)²)
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            indices = [i, j]
            indices.reverse()
            if distance <= radius and distance != 0:
                if indices in li_indices:
                    pass
                else:
                    li_indices.append([i, j])
                    li_distance.append(distance)

    print(li_indices)
    print(li_distance)


construct_graph_connections(coord_list, radius)
