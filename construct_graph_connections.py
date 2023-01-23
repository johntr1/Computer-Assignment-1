# Function name: construct_graph_connections
# Input:
# coord_list : a list of coordinates
# radius : radius to determine which cities connect
# Output:
# ndarray with indices of each connected city and another array with distance between them

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
            # Distance formula: distance=√((x2 – x1)² + (y2 – y1)²) (taken from maths book)
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            # Define indices as reverse to control duplicate connections
            indices = [i, j]
            indices.reverse()
            # Checks for radius and that it is not the same coordinate
            if distance <= radius and distance != 0:
                # Controls for duplicates in the indices list
                if indices in li_indices:
                    pass
                # Append the indices and distance if all requirements are met
                else:
                    li_indices.append([i, j])
                    li_distance.append(distance)

    return [li_indices, li_distance]
