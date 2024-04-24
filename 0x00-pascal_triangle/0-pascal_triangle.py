#!/usr/bin/python3
"""Returns a list of lists of integers representing Pascal's triangle of n"""

def generate_pascal_triangle(n):
    """Generates a list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []
    else:
        triangle = [[] for row in range(n)]
        for row in range(n):
            for col in range(row + 1):
                if col < row:
                    if col == 0:
                        triangle[row].append(1)
                    else:
                        triangle[row].append(triangle[row - 1][col] + triangle[row - 1][col - 1])
                elif col == row:
                    triangle[row].append(1)
        return triangle

