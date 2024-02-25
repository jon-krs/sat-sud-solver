#!/usr/bin/env python3
import subprocess
import os
import glob

def run_commands(prefix='grid', sudoku_output_file='sudoku_output.txt', stat_file_name='stat.txt', version=1):
    files = [f for f in os.listdir('.') if f.startswith(prefix) and f.endswith('.txt') and '_output' not in f]
    num_files = len(files)

    if version != 1:
        sud2sat_script = f'../sud2sat{version}.py'
        sat2sud_script = f'../sat2sud{version}.py'
    else:
        sud2sat_script = f'../sud2sat.py'
        sat2sud_script = f'../sat2sud.py'

    for i in range(1, num_files + 1): 
        number_str = str(i).zfill(2)
        
        grid_file = f'{prefix}_{number_str}.txt'
        cnf_file = f'{prefix}_{number_str}_v{version}.cnf'
        output_file = f'{prefix}_{number_str}_output_v{version}.txt'

        # Generate CNF file
        with open(grid_file, 'r') as grid_input, open(cnf_file, 'w') as cnf_output:
            subprocess.run(['python', sud2sat_script], stdin=grid_input, stdout=cnf_output)

        # Call MiniSAT to solve the CNF
        with open(output_file, 'w') as minisat_output:
            subprocess.run(['minisat', cnf_file, output_file], stdout=subprocess.PIPE)

        # Append header for stat_file_name information
        with open(stat_file_name, 'a') as stat_file:
            stat_file.write(f"\n{'='*20}\nminiSAT stat output for test {prefix} {number_str} Version {version}\n{'='*20}\n")
            subprocess.run(['minisat', cnf_file, output_file], stdout=stat_file, stderr=stat_file)

        # Convert to Sudoku solution
        with open(output_file, 'r') as sat_input, open(sudoku_output_file, 'a') as sudoku_output:
            sudoku_output.write(f"\n{'='*20}\nsudoku output for test {prefix} {number_str} Version {version}\n{'='*20}\n")
            subprocess.run(['python', sat2sud_script], stdin=sat_input, stdout=sudoku_output)

def generate_files():
    subprocess.run(['python', 'project_euler_testing_file_generator.py'])
    subprocess.run(['python', 'top95_hard_testing_file_generator.py'])

def delete_generated_files():
    # Generate patterns for all versions
    versions = [1, 2, 3]
    patterns = []

    for v in versions:
        patterns.extend([
            f'grid_*.txt',
            f'hard_grid_*.txt',
            f'grid_*_v{v}.cnf',
            f'grid_*_output_v{v}.txt',
            f'hard_grid_*_v{v}.cnf',
            f'hard_grid_*_output_v{v}.txt'
        ])
    
    # Delete files matching the patterns
    for pattern in patterns:
        for filename in glob.glob(pattern):
            os.remove(filename)

def clean_data():
    # Generate patterns for all versions
    versions = [1, 2, 3]
    patterns = []

    for v in versions:
        patterns.extend([
            f'stat_v{v}.txt',
            f'sudoku_output_v{v}.txt',
            f'hard_stat_v{v}.txt',
            f'hard_sudoku_output_v{v}.txt',
            f'project_euler_test_stat_results_v{v}.txt',
            f'top95_test_stat_results_v{v}.txt'
        ])
    
    # Delete files matching the patterns
    for pattern in patterns:
        for filename in glob.glob(pattern):
            os.remove(filename)

def main():
    # Clean any previous results data
    clean_data()

    # Generate testing files
    generate_files()

    # Program versions (sud2sat, sud2sat2, sud2sat3, ...)
    versions = [1, 2, 3]
    for version in versions:
        # Project Euler tests (50)
        run_commands(sudoku_output_file=f'sudoku_output_v{version}.txt', stat_file_name=f'stat_v{version}.txt', version=version)

        # Top95 tests (95) 
        run_commands(prefix='hard_grid', sudoku_output_file=f'hard_sudoku_output_v{version}.txt', stat_file_name=f'hard_stat_v{version}.txt', version=version)

    # Delete testing files
    delete_generated_files()

if __name__ == '__main__':
    main()