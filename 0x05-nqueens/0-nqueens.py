#!/usr/bin/python3
"""
Author: Gadoskey
Description: This module contains a function to solve the N queens problem.
"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on the board at the given row and column.
    """
    for c in range(col):
        if board[c] == row or \
           board[c] - c == row - col or \
           board[c] + c == row + col:
            return False
    return True


def solve_nqueens(n, col, board, solutions):
    """
    Recursively try to place queens in columns.
    """
    if col == n:
        # If all queens are placed, store the solution
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_nqueens(n, col + 1, board, solutions)
            board[col] = -1  # Backtrack


def main():
    """
    Parse input arguments, validate them, and solve the N-queens problem.
    """
    # Validate the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N is an integer and is at least 4
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-queens problem and print each solution
    solutions = []
    board = [-1] * n  # -1 means no queen placed in that column
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
