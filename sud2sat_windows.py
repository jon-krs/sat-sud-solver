import sys #needed to test on Windows

def encode_variable(i, j, k):
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1

def add_sudoku_rules(cnf):
    # Each entry has at least one number
    for x in range(1, 10):
        for y in range(1, 10):
            cnf.append([encode_variable(x, y, z) for z in range(1, 10)] + [0]) # Add '0' at the end

    # Each number appears at most once in each row
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 9):
                for i in range(x + 1, 10):
                    cnf.append([-encode_variable(x, y, z), -encode_variable(i, y, z), 0])

    # Each number appears at most once in each column
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y + 1, 10):
                    cnf.append([-encode_variable(x, y, z), -encode_variable(x, i, z), 0])

    # Each number appears at most once in each 3x3 sub-grid
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
    # Replace wildcards with '0' and flatten the puzzle
    flattened_puzzle = puzzle.replace('.', '0').replace('*', '0').replace('?', '0').replace('x', '0')
    flattened_puzzle = ''.join(flattened_puzzle.split())  # Removing any whitespace or newline characters

    for i in range(9):
        for j in range(9):
            k = int(flattened_puzzle[i * 9 + j])
            if k != 0:  # Skip if it's a '0'
                cnf.append([encode_variable(i + 1, j + 1, k), 0])  # Append 0 to the end of the clause

def sudoku_to_cnf(puzzle):
    cnf = []
    add_sudoku_rules(cnf)
    add_puzzle_clauses(cnf, puzzle)
    return cnf

def format_dimacs(cnf):
    # Count the number of variables and clauses
    num_variables = 81 * 9  # Since each of the 81 cells can contain one of 9 numbers
    num_clauses = len(cnf)

    # Start with the DIMACS header
    dimacs = f"p cnf {num_variables} {num_clauses}\n"

    # Add each clause in CNF to the DIMACS formatted string
    for clause in cnf:
        # Each clause is a list of integers ending with 0
        dimacs += " ".join(map(str, clause)) + "\n"

    return dimacs.strip()


def main(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        puzzle = file.read().strip()

    cnf = sudoku_to_cnf(puzzle)
    dimacs_format = format_dimacs(cnf)

    with open(output_file_path, 'w') as file:
        file.write(dimacs_format)

if __name__ == "__main__":
    input_file = sys.argv[1]  # First argument is input file path
    output_file = sys.argv[2]  # Second argument is output file path
    main(input_file, output_file)
    #main() may need to change to this when running on linux
