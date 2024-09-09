#!/usr/bin/env python3
"""module that solves the nqueeens puzzle"""
import sys


def is_safe(queen_pos, queens_placed):
    """
    Check if the current queen can be placed in queen_position
    such that it does not attack any queens placed so far.
    """
    curr_row, curr_column = queen_pos
    for row, col in enumerate(queens_placed):
        if col == curr_column or abs(curr_column - col) == abs(curr_row - row):
            return False
    return True


def solve_nqueens(n, row=0, queens_placed=[]):
    """
    Solve the N Queens problem using backtracking.
    """
    if row == n:
        print([[i, queens_placed[i]]for i in range(n)])
        return
    for col in range(n):
        if is_safe((row, col), queens_placed):
            solve_nqueens(n, row + 1, queens_placed + [col])


def main():
    """Code's main entry point"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
