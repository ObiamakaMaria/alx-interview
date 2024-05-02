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
<<<<<<< HEAD
    min_coins = 0
    
=======
    fewest_coins = 0

>>>>>>> 99875fdfe3d1e35d4b197dcf0b05ed8def7c138e
    for coin in coins:
        if total <= 0:
            break
        min_coins += total // coin
        total %= coin

    if total != 0:
        return -1
<<<<<<< HEAD
    
    return min_coins
=======

    return fewest_coins

>>>>>>> 99875fdfe3d1e35d4b197dcf0b05ed8def7c138e