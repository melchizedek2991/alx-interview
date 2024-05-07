#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
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
