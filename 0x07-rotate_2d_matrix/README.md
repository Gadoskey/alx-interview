# Rotate 2D Matrix

## Author
Yusuf Mustapha Opeyemi

## Task Overview
This task involves rotating an **n x n 2D matrix** by **90 degrees clockwise**. The goal is to perform this rotation **in-place**, meaning no additional matrix should be used. This is a common problem in technical interviews and is a good exercise to practice matrix manipulation and in-place operations.

## Problem Description
Given an `n x n` 2D matrix, rotate the matrix **90 degrees clockwise**.

### Example:

Input:
`[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]`
Output:
`[ [7, 4, 1], [8, 5, 2], [9, 6, 3] ]`

## Approach

We can solve this problem in two main steps:
1. **Transpose the matrix**: Convert rows to columns and columns to rows.
2. **Reverse each row**: After the transpose, reverse the elements of each row to complete the 90-degree rotation.

## Requirements

- **Python 3.x**

No external libraries are required.

## Usage

1. The `rotate_2d_matrix` function is implemented in a Python script.
2. A separate `main_0.py` file is used to test the function. It contains a matrix and imports the `rotate_2d_matrix` function to rotate it.
3. Make the `main_0.py` file executable and run it to see the results.

## License

This project is free to use, modify, and distribute. No restrictions apply.