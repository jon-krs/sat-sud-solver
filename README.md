# SAT-based Sudoku Solver

## Project Overview
This project develops a simple program to translate partially solved Sudoku puzzles into CNF (Conjunctive Normal Form) formulas, making the CNF satisfiable if and only if the Sudoku puzzle can be solved. This involves creating two main programs: `sud2sat` and `sat2sud`, which convert Sudoku puzzles to CNF and vice versa, respectively. Also included is a full testing suite to generate reports on and analyze data collected from the miniSAT api.

## Team Members
- Member 1: Jonathan Best, V00954981
- Member 2: Logan Johnson, V00955568

## Tools and Environment
- **Language**: Python
- **Execution Environment**: linux.csc.uvic.ca
- **Dependencies**: miniSAT (Available on linux.csc.uvic.ca)

## Content
- **sud2sat.py**: Reads a Sudoku puzzle and converts it into a CNF formula suitable for the miniSAT SAT solver.
- **sat2sud.py**: Converts the output from miniSAT back into a solved Sudoku puzzle.
- **sud2sat2.py**: Adds **efficient encoding** to the minimal encoding in sud2sat.
- **sat2sud2.py**: Converts the output from miniSAT back into a solved Sudoku puzzle.
- **sud2sat3.py**: Adds **extended encoding** to the efficient encoding in sud2sat2.
- **sat2sud3.py**: Converts the output from miniSAT back into a solved Sudoku puzzle.
- **main_testing_driver.py**: Drives testing suite for all versions, creates, analyzes, and saves statistics from miniSAT.

## Usage
- **sud2sat.py**: 
    - 'python sud2sat.py < sudoku_encoding.txt > cnf_encoding.cnf'
- **sat2sud.py**: 
    - 'python sat2sud.py < miniSAT_output.txt > sudoku_solution.txt'
- **sud2sat2.py**: 
    - 'python sud2sat2.py < sudoku_encoding.txt > cnf_encoding.cnf'
- **sat2sud2.py**: 
    - 'python sat2sud2.py < miniSAT_output.txt > sudoku_solution.txt'
- **sud2sat3.py**: 
    - 'python sud2sat3.py < sudoku_encoding.txt > cnf_encoding.cnf'
- **sat2sud3.py**: 
    - 'python sat2sud3.py < miniSAT_output.txt > sudoku_solution.txt'
- **main_testing_driver.py**: 
    - In testing folder: 'python main_testing_driver.py'
    - Saves:
        - 'project_euler_test_stat_results_{version}.txt' - analyzed results from easy puzzles at Project Euler
        - 'top95_test_stat_results_{version}.txt' - analyzed results from hard puzzles at Top95
        - 'sudoku_output_{version}.txt' - completed sudoku puzzles in readable form from easy puzzles at Project Euler
        - 'hard_sudoku_output_{version}.txt' - completed sudoku puzzles in readable form from hard puzzles at Top95
        - 'stat_{version}.txt' - miniSAT stats from easy puzzles at Project Euler
        - 'hard_stat_{version}.txt' - miniSAT stats from hard puzzles at Top95
