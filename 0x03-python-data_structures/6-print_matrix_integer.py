#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        _ = [[(print("{:d}".format(j[1]), end='') or ((j[0] != 2 or print()) and print(
            " ", end=''))) for j in enumerate(sub)] for sub in matrix]
    else:
        print('')
