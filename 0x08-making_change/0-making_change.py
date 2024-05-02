#!/usr/bin/python3

"""
This function calculates the minimum number of coins required
to achieve a specified total amount using a given set of coin values.
"""


def makeChange(coins, total):
    """Returns the minimum number of coins needed to reach 'total' amount"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    fewest_coins = 0

    for coin in coins:
        if total <= 0:
            break
        fewest_coins += total // coin
        total %= coin

    if total != 0:
        return -1

    return fewest_coins
