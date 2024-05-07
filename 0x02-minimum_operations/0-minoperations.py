#!/usr/bin/python3

"""
    Determine the minimum operations for a given character count.
"""


def minOperations(n):
    """
        A Function to determine the minimum operations needed to produce 'n' 'H' characters in a file. Args: n - Number of characters to be displayed. Returns: Minimum operations count.
    """

    init = 1
    prompt = 0
    counter = 0
    while init < n:
        remainder = n - init
        if (remainder % init == 0):
            prompt = init
            init += prompt
            counter += 2
        else:
            init += prompt
            counter += 1
    return counter
