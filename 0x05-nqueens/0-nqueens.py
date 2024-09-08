#!/usr/bin/python3
import sys

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

def queens(n, row=0, cols=[], diag1=[], diag2=[]):
    """ Recursive generator to find valid N-Queens placements """
    if row == n:
        yield cols
    else:
        for col in range(n):
            if col not in cols and (row + col) not in diag1 and (row - col) not in diag2:
                yield from queens(n, row + 1, cols + [col], diag1 + [row + col], diag2 + [row - col])

def solve(n):
    """ Solves the N Queens puzzle and prints all valid solutions """
    for solution in queens(n):
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)

solve(n)
