#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n <= 1:
        return 0

    # keeps track of the total number of operations needed.
    operations = 0

    # the current factor we are testing to divide the number n
    factor = 2

    while n > 1:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1

        operations += count * factor
        factor += 1

    return operations
