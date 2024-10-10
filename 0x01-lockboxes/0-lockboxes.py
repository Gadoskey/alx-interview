#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
File: 0-lockboxes.py
Function: canUnlockAll
Description: This function determines if all boxes in a list of lists can be unlocked. 
Each box may contain keys to other boxes. We start with box 0 unlocked and use the keys 
found inside boxes to open others. The function returns True if all boxes can be opened, 
else returns False.
"""

def canUnlockAll(boxes):
    """
        A func that determines if all boxes in a list of lists can be unlocked.
    """
    n = len(boxes)  # Total number of boxes
    opened = [False] * n  # List to track which boxes have been opened
    opened[0] = True  # Box 0 is always open
    keys = [0]  # Start with the key to box 0
    
    while keys:
        key = keys.pop()  # Get the last key
        if not opened[key]:  # If the box corresponding to the key is not open
            opened[key] = True  # Mark the box as opened
            for new_key in boxes[key]:  # Get keys from this box
                if new_key < n and not opened[new_key]:  # If the key is valid and the box is not yet opened
                    keys.append(new_key)  # Add this key to the list

    return all(opened)  # Return True if all boxes are opened, else False
