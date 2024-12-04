import re
import numpy as np

with open("day4_input", "r") as infile:
    # open data as np matrix
    xmas_matrix = np.matrix([[x for x in line.strip()] for line in infile])
    matrix_x_limit = xmas_matrix.shape[0]    

    # print(xmas_matrix)

    # count by looking for forward reverse XMAS in strings of each row
    horizontal_count = 0
    for row in xmas_matrix.tolist():
        joined_row = "".join(row)
        horizontal_count += len(re.findall(r"XMAS", joined_row)) + len(re.findall(r"SAMX", joined_row))
    #print(horizontal_count)

    # count by looking for forward reverse XMAS in strings of each column (transposed matrix)
    vertical_count = 0
    for row in xmas_matrix.T.tolist():
        joined_row = "".join(row)
        vertical_count += len(re.findall(r"XMAS", joined_row)) + len(re.findall(r"SAMX", joined_row))
    #print(vertical_count)


    # count by looking for forward reverse XMAS in strings of each diagonal (len >= 4)
    diagonal_count = 0
    for i in range(-matrix_x_limit+1, matrix_x_limit):
        joined_row = "".join(xmas_matrix.diagonal(i).tolist()[0])
        if len(joined_row) >= 4:
            diagonal_count += len(re.findall(r"XMAS", joined_row)) + len(re.findall(r"SAMX", joined_row))
    #print(diagonal_count)

    # count by looking for forward reverse XMAS in strings of each anti-diagonal (len >= 4)
    anti_diagonal_count = 0
    for i in range(-matrix_x_limit+1, matrix_x_limit):
        joined_row = "".join(np.fliplr(xmas_matrix).diagonal(i).tolist()[0])
        if len(joined_row) >= 4:
            anti_diagonal_count += len(re.findall(r"XMAS", joined_row)) + len(re.findall(r"SAMX", joined_row))
    # print(anti_diagonal_count)

    print(horizontal_count + vertical_count + diagonal_count + anti_diagonal_count)
    
    