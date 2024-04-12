#!/usr/bin/python3
'''
Solution for the N-Queen problem
'''

import sys

chessboard = []
n_value = 0
columns = set()
diagonal1 = set()
diagonal2 = set()
solutions = []


def main():
    '''
    Entry point for the program
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    global n_value
    n_value = sys.argv[1]
    try:
        n_value = int(n_value)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n_value < 4:
        print("N must be at least 4")
        sys.exit(1)
    global chessboard
    chessboard = [["."] * n_value for _ in range(n_value)]
    place_queens(0)
    for solution in solutions:
        output = []
        for row in solution:
            row_position = solution.index(row)
            column_position = list(row).index("Q")
            final_position = [row_position, column_position]
            output.append(final_position)
        print((output))


def place_queens(row):
    '''
    Backtracking function to place queens on the chessboard
    '''
    if row == n_value:
        board_copy = ["".join(r) for r in chessboard]
        solutions.append(board_copy)
        return
    for i in range(n_value):
        if i in columns or (row + i) in diagonal1 or (row - i) in diagonal2:
            continue

        columns.add(i)
        diagonal1.add(row + i)
        diagonal2.add(row - i)
        chessboard[row][i] = 'Q'

        place_queens(row + 1)

        columns.remove(i)
        diagonal1.remove(row + i)
        diagonal2.remove(row - i)
        chessboard[row][i] = '.'


if __name__ == "__main__":
    '''
    Execute if not imported
    '''
    main()
