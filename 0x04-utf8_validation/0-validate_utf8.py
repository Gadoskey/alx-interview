#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
Description: This module contains a function to validate if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given list of integers represents a valid UTF-8 encoding.

    Parameters:
        data (list): A list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    for num in data:
        # Only look at the least significant 8 bits
        byte = num & 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes for the character
            if (byte >> 7) == 0b0:
                # 1-byte character (0xxxxxxx)
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                remaining_bytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            # Check that the byte starts with '10xxxxxx'
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # All characters should be complete, so no remaining bytes expected
    return remaining_bytes == 0
