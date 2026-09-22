#!/usr/bin/python3
"""
Module containing the minOperations function.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach n H characters.

    Args:
        n (int): The number of H characters to obtain.

    Returns:
        int: The minimum number of operations needed, or 0 if n <= 1.
    """
    if n <= 1:
        return 0

    total_operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            total_operations += divisor
            n //= divisor
        else:
            divisor += 1

    return total_operations
