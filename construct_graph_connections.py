# Function name: construct_graph_connections
# Input:
# coord_list : a list of coordinates
# radius : radius to determine which cities connect
# Output:
# ndarray with indices of each connected city and another array with distance between them
import numpy as np
def construct_graph_connections(coord_list, radius):
    li_indices = []
    li_distance = []
    for i, i_element in enumerate(coord_list):
        for j, j_element in enumerate(coord_list):
            # Checks for reverse order duplicates and skips if true
            if i >= j:
                continue
            # Define the x and y for the distance formula for readability
            x1 = i_element[0]
            y1 = i_element[1]
            x2 = j_element[0]
            y2 = j_element[1]
            # Distance formula: distance=√((x2 – x1)² + (y2 – y1)²) (taken from maths book)
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            # Checks for radius and that it is not the same coordinate
            if distance <= radius:
                li_indices.append([i, j])
                li_distance.append(distance)
    # Convert the lists to ndarrays
    li_indices = np.array(li_indices)
    li_distance = np.array(li_distance)
    return li_indices, li_distance

