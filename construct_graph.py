

import numpy as np
from scipy.sparse import csr_matrix

def construct_graph(indices, distance, N):

    indicesT=indices.T
    data=distance
    row=indicesT[0][:]
    col=indicesT[1][:]
    csr=csr_matrix((data, (row, col)), shape=(900, N))

