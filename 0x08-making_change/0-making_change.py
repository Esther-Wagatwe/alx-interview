#!/usr/bin/python3
"""Module for making change."""


def makeChange(coins, total):
    """Function that makes change for a given total,
    using the least amount of coins."""
    if total <= 0:
        return 0

    arr = [float('inf')] * (total + 1)

    arr[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                arr[i] = min(arr[i], arr[i - coin] + 1)

    return arr[total] if arr[total] != float('inf') else -1