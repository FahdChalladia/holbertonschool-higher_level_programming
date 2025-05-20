#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
