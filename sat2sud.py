#!/usr/bin/env python3
import sys

def decode_variable_assignment(number_SAT):
    """
    Reverse encodes a number from SAT solver to Sudoku cell 
    coordinates (i,j) with cell digit k.
    """
    k = (number_SAT - 1) % 9 + 1
    
    # Simulate zero-based indexing.
    n = (number_SAT - 1) // 9

    j = (n) % 9 + 1  # Column
    i = (n) // 9 + 1  # Row

    return (i, j, k)

def convert_output(output):
    """
    Handles SAT output, checking for satisfiability and if satisfiable, 
    converts the SAT solution to a Sudoku puzzle.
    """
    if not output or output[0] != 'SAT':
        print("This puzzle is unsatisfiable.")

        return None
    
    grid = [[0 for _ in range(9)] for _ in range(9)]

    for variable in output[1:-1]:
        if int(variable) > 0:
            i, j, k = decode_variable_assignment(int(variable))
            grid[i-1][j-1] = k
    
    return grid

def print_sudoku(grid):
    """
    Prints Sudoku grid in 9x9 matrix view.
    """
    if grid is None:
        print("No Sudoku grid to display.")
    else:
        for row in grid:
            print(' '.join(str(cell) for cell in row))

def main():
    minisat_output = sys.stdin.read().strip().split()

    is_puzzle_sat = minisat_output[0]
    sudoku_result = convert_output(minisat_output) if is_puzzle_sat else None

    print_sudoku(sudoku_result) if sudoku_result != None else print("This puzzle is unsatisfiable.")

if __name__ == "__main__":
     main()