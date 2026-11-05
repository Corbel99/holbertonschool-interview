#!/usr/bin/python3
"""Module that computes the perimeter of an island described in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 0 represents water, 1 represents land.
            Each cell is a square of side 1.

    Returns:
        int: the perimeter of the island (0 if there is no island).
    """
    perimeter = 0
    rows = len(grid)
    if rows > 0:
        cols = len(grid[0])
    else:
        cols = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
