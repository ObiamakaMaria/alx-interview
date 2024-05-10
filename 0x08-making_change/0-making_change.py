#!/usr/bin/python3

"""
This function calculates the minimum number of coins required
to achieve a specified total amount using a given set of coin values.
"""


def makeChange(coins, total):
    """return the fewest coins needed to meet total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    min_req = 0
    for coin in coins:
        if total <= 0:
            break
        min_req += total // coin
        total %= coin
    if total != 0:
        return -1
    return min_req
