#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
File: 0-minoperations.py
Function: minOperations
Description: This function calculates the fewest number of operations
            needed to result in exactly n H characters in the file
"""


def minOperations(n: int) -> int:
    # If n is less than or equal to 1, return 0 as it's impossible
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            # If divisible, add the divisor to operations
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
