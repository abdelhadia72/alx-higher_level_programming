#!/usr/bin/python3
""" read/write from file """


def pascal_triangle(n):
    """
    pascal_triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0], [0] + pascal[-1])])
    return pascal
