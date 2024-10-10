#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
File: 0-pascal_triangle.py
Function: pascal_triangle
Description: This function creates the pascal triangle
"""


def pascal_triangle(n):
    """
        A func that returns a list of ints repr the Pascal's triangle of n
    """
    matrix = []     # A list of lists or outer list
    if n <= 0:
        return (matrix)     # Return matrix - an empty list if n <= 0
    for i in range(n):
        innerList = []      # Create an inner list
        for j in range(i + 1):
            if j == 0 or j == i:  # First and last elements are always 1
                innerList.append(1)
            else:
                # Sum the two elements from the previous row
                innerList.append(matrix[i - 1][j - 1] + matrix[i - 1][j])

        matrix.append(innerList)    # Append the inner list to matrix

    # Return matrix
    return (matrix)
