#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
File: 0-lockboxes.py
Function: canUnlockAll
Description: This function determines
  if all boxes in a list of lists can be unlocked.
Each box may contain keys to other boxes.
We start with box 0 unlocked and use the keys 
  found inside boxes to open others.
The function returns True if all boxes can be opened,
  else returns False.
"""

def canUnlockAll(boxes):
    # Start with box 0 unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # Box 0 is always unlocked
    
    # A list of keys you currently have, starting with keys in box 0
    keys = boxes[0]
    
    # Check which boxes can be unlocked with the keys you find
    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            # Add new keys from the newly unlocked box
            keys.extend(boxes[key])
    
    # Return True if all boxes are unlocked
    return all(unlocked)
