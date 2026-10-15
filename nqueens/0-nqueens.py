#!/usr/bin/python3
"""Solve the N queens puzzle."""
import sys


def n_not_valid_():
    """Check whether the command-line argument is valid."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return True

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return True

    if N < 4:
        print("N must be at least 4")
        return True

    return False


def is_safe(board, current_row, current_col):
    """Check whether a queen can be placed at a given position."""
    for queen in board:
        queen_row = queen[0]
        queen_col = queen[1]

        if queen_col == current_col:
            return False

        if abs(queen_row - current_row) == abs(
                queen_col - current_col):
            return False

    return True


def solve_n_queens(row, n, board):
    """Find and print all solutions using backtracking."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append((row, col))
            solve_n_queens(row + 1, n, board)
            board.pop()


if __name__ == "__main__":
    if n_not_valid_():
        sys.exit(1)

    N = int(sys.argv[1])
    solve_n_queens(0, N, [])
