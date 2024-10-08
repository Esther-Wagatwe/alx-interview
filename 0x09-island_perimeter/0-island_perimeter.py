#!/usr/bin/python3
"""Module for Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Parameters:
    grid (list of list of int): A rectangular grid containing integers
                                 (0 for water and 1 for land).

    Returns:
    int: The perimeter of the island. If the grid contains no land,
         the perimeter is 0.
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
