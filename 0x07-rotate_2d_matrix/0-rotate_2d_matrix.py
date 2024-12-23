#!/usr/bin/python3
"""
  Author: Yusuf Mustapha Opeyemi
  Desc: An algorithm that rotates a `n x n 2D matrix` 90 degrees clockwise.
"""


"""Steps:
    Step 1: Transpose the matrix -

      The transpose of a matrix is an operation that flips
      the matrix over its diagonal. Specifically, for a given matrix,
      it converts the row indices to column indices and vice versa.

      SYNTAX: matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

              You can also use NumPy: matrix.T or matrix.transpose()
              Quite easier. Try it out?




      In simpler terms:
        The first row becomes the first column.
        The second row becomes the second column, and so on.

       [[1 2 3]          [[1 4 7]

        [4 5 6]   --->    [2 5 8]

        [7 8 9]]          [3 6 9]]

    Step 2: Reverse each row -
      [1, 4, 7] becomes [7, 4, 1]
      [2, 5, 8] becomes [8, 5, 2]
      [3, 6, 9] becomes [9, 6, 3]
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Arg:
        matrix: List[List[int]], the matrix to rotate
    """
    n = len(matrix)

    # Transpose the matrix manually using Simultaneous Assignment
    # In other instances you can use numpy though, Quite easier to use
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()


"""
  How TRANSPOSE Helps in Rotation:

    In the rotate 90 degrees clockwise algorithm,
    the transpose step helps "flip" the matrix over its diagonal,
    and then reversing the rows completes the 90-degree rotation.
    This is why transposing is a key step

    Why simultaneous assignment was used instead of sequential:

    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            VS

    matrix[i][j] = matrix[j][i]
    matrix[j][i] = matrix[i][j]

    Here's the issue:

    In the second line, we're trying to assign matrix[j][i] = matrix[i][j]
    after the first assignment has already changed matrix[i][j].
    This would overwrite the value of matrix[j][i] with the
    new value of matrix[i][j], which isn't the desired behavior.
    We're losing the original value of matrix[i][j]
    before it can be assigned to matrix[j][i].

    Conclusion:
      Simultaneous assignment (using the tuple syntax) is correct
      and ensures that the values are swapped without losing any data.
      Sequential assignment would lead to errors because
      the second value is overwritten before the swap can occur.
"""
