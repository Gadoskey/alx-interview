#!/usr/bin/python3
"""
Author: Yusuf Mustapha Opeyemi
Desc: An algorithm that determines the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total.

    Args:
        coins: List[int], the list of the values of the coins
        total: int, the target amount to achieve

    Returns:
        int: The minimum number of coins required to meet the total,
             or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    num_coins = 0
    remaining_total = total

    for coin in coins:
        if remaining_total <= 0:
            break
        # Use as many of the current coin as possible
        count = remaining_total // coin
        num_coins += count
        remaining_total -= coin * count

    # Check if the total was met
    if remaining_total == 0:
        return num_coins
    return -1
