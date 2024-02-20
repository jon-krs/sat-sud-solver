#!/usr/bin/env python3
import sys

def encode_variable(i, j, k):
    # Encodes a Sudoku cell and a number into a unique SAT variable.
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1

def add_sudoku_rules(cnf):
    # Add Sudoku rules to the CNF.

    # Ensure each cell contains at least one number (1-9).
    for x in range(1, 10):
        for y in range(1, 10):
            cnf.append([encode_variable(x, y, z) for z in range(1, 10)] + [0])

    # Ensure each number appears at most once in each row.
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 9):
                for i in range(x + 1, 10):
                    cnf.append([-encode_variable(x, y, z), -encode_variable(i, y, z), 0])

    # Ensure each number appears at most once in each column.
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y + 1, 10):
                    cnf.append([-encode_variable(x, y, z), -encode_variable(x, i, z), 0])

    # Ensure each number appears at most once in each 3x3 sub-grid.
    for z in range(1, 10):
        for i in range(3):
            for j in range(3):
                for x in range(1, 4):
                    for y in range(1, 4):
                        for k in range(y + 1, 4):
                            cnf.append([-encode_variable(3 * i + x, 3 * j + y, z), -encode_variable(3 * i + x, 3 * j + k, z), 0])
                        for k in range(x + 1, 4):
                            for l in range(1, 4):
                                cnf.append([-encode_variable(3 * i + x, 3 * j + y, z), -encode_variable(3 * i + k, 3 * j + l, z), 0])

def add_puzzle_clauses(cnf, puzzle):
    # Add clauses for pre-filled numbers in the Sudoku puzzle.
    # Replace wildcards with '0' and flatten the puzzle.
    flattened_puzzle = puzzle.replace('.', '0').replace('*', '0').replace('?', '0').replace('x', '0')
    flattened_puzzle = ''.join(flattened_puzzle.split())  # Removing any whitespace or newline characters

    # Iterate over each cell and add a clause if the cell is not empty.
    for i in range(9):
        for j in range(9):
            k = int(flattened_puzzle[i * 9 + j])
            if k != 0:  # Skip if it's a '0'
                cnf.append([encode_variable(i + 1, j + 1, k), 0])  # Append 0 to the end of the clause

def sudoku_to_cnf(puzzle):
    # Convert a Sudoku puzzle to CNF.
    cnf = []
    add_sudoku_rules(cnf)
    add_puzzle_clauses(cnf, puzzle)
    return cnf

def format_dimacs(cnf):
    # Format the CNF into DIMACS format for SAT solvers.
    num_variables = 81 * 9  # Since each of the 81 cells can contain one of 9 numbers
    num_clauses = len(cnf)

    # Start with the DIMACS header.
    dimacs = "p cnf {} {}\n".format(num_variables, num_clauses)

    # Add each clause in CNF to the DIMACS formatted string.
    for clause in cnf:
        dimacs += " ".join(map(str, clause)) + "\n"

    return dimacs.strip()

def main():
    # Main function to read puzzle, convert to CNF, and output in DIMACS format.
    puzzle = sys.stdin.read().strip()
    cnf = sudoku_to_cnf(puzzle)
    print(format_dimacs(cnf))

if __name__ == "__main__":
     main()
