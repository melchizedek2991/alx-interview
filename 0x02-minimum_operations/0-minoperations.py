#!/usr/bin/python3

"""
    A method to calculate the minimum number of operations given a number of characters.
"""


def minOperations(n):
    """
        Calculates the fewest number of operations needed to achieve a result of exactly n 'H' characters in a file.
        Args:
            n: Number of characters to be displayed
        Returns:
            The number of minimum operations required.
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
