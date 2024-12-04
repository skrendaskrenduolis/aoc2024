import re
import numpy as np

with open("day4_input", "r") as infile:
    # open data as np matrix
    xmas_matrix = np.matrix([[x for x in line.strip()] for line in infile])
    matrix_x_limit = xmas_matrix.shape[0]    

    # print(xmas_matrix)

    # count by looking for forward reverse XMAS in strings of each row
    # count by looking for forward reverse XMAS in strings of each column (transposed matrix)        
    horizontal_count = 0
    vertical_count = 0
    for row, column in zip(xmas_matrix.tolist(), xmas_matrix.T.tolist()):
        joined_row = "".join(row)
        joined_column = "".join(column)
        horizontal_count += len(re.findall(r"(?=(XMAS|SAMX))", joined_row))
        vertical_count += len(re.findall(r"(?=(XMAS|SAMX))", joined_column))


    # count by looking for forward reverse XMAS in strings of each diagonal (len >= 4)
    # count by looking for forward reverse XMAS in strings of each anti-diagonal (len >= 4)
    diagonal_count = 0
    anti_diagonal_count = 0
    for i in range(-matrix_x_limit+1, matrix_x_limit):
        joined_row = "".join(xmas_matrix.diagonal(i).tolist()[0])
        joined_column = "".join(np.fliplr(xmas_matrix).diagonal(i).tolist()[0])
        if len(joined_row) >= 4:
            diagonal_count += len(re.findall(r"(?=(XMAS|SAMX))", joined_row))
        if len(joined_row) >= 4:
            anti_diagonal_count += len(re.findall(r"(?=(XMAS|SAMX))", joined_column))
        
    print(horizontal_count + vertical_count + diagonal_count + anti_diagonal_count)    
    