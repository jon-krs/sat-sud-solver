# SAT-based Sudoku Solver

## Project Overview
This project aims to develop a simple program to translate partially solved Sudoku puzzles into CNF (Conjunctive Normal Form) formulas, making the CNF satisfiable if and only if the Sudoku puzzle can be solved. This involves creating two main programs: `sud2sat` and `sat2sud`, which convert Sudoku puzzles to CNF and vice versa, respectively.

## Team Members
- Member 1: Jonathan Best, V00954981
- Member 2: Logan Johnson, V00955568

## Tools and Environment
- **Language**: Python
- **Execution Environment**: linux.csc.uvic.ca
- **Dependencies**: miniSAT (Available on linux.csc.uvic.ca)

## Usage
- **sud2sat**: Reads a Sudoku puzzle and converts it into a CNF formula suitable for the miniSAT SAT solver.
- **sat2sud**: Converts the output from miniSAT back into a solved Sudoku puzzle.
