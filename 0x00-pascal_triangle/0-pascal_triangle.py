#!/usr/bin/python3
"""
function that returns a list of lists of integers representing 
the Pascal’s
"""


def pascal_triangle(n):
    """this function returns a list of lists of integers representing 
    the Pascal’s
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
