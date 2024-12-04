import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

with open("day4_input", "r") as infile:
    # open data as np matrix
    xmas_matrix = np.matrix([[x for x in line.strip()] for line in infile])
    #print(xmas_matrix)

    # perform 3x3 sliding window search
    v_total = sliding_window_view(xmas_matrix, (3,3))
    #print(v_total.shape)

    # iterate over reshaped sliding window list and extract diagonal and anti-diagonal
    x_shapes = 0
    for v in v_total.reshape(-1, 3, 3):
        v_diag = "".join(v.diagonal())
        v_antidiag = "".join(np.fliplr(v).diagonal())
        if (v_diag == "SAM" or v_diag == "MAS") and (v_antidiag == "SAM" or v_antidiag == "MAS"):
            x_shapes += 1
    print(x_shapes)