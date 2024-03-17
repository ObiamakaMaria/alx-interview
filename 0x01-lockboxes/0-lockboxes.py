#!/usr/bin/python3

"""
This function determines if a box can be opened with a list of keys
stored in boxes containing list of lists
"""


def canUnlockAll(boxes):
    """
    Checking if boxes can be unlocked
    Args:
    boxes: list of lists
    Returns: True OR False
    """
    unlocked = {}
    start = 0

    for everybox in boxes:
        if len(everybox) == 0 or start == 0:
            unlocked[start] = "unlocked"
        for key in everybox:
            if key < len(boxes) and key != start:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        start += 1
    return False
