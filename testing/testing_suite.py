import subprocess
import os

def run_commands(prefix='grid', sudoku_output_file='sudoku_output.txt', stat_file_name='stat.txt'):
    files = [f for f in os.listdir('.') if f.startswith(prefix) and f.endswith('.txt') and '_output' not in f]
    num_files = len(files)

    for i in range(1, num_files + 1): 
        number_str = str(i).zfill(2)
        
        grid_file = f'{prefix}_{number_str}.txt'
        cnf_file = f'{prefix}_{number_str}.cnf'
        output_file = f'{prefix}_{number_str}_output.txt'

        # 1. Generate CNF file
        with open(grid_file, 'r') as grid_input, open(cnf_file, 'w') as cnf_output:
            subprocess.run(['python', '../sud2sat.py'], stdin=grid_input, stdout=cnf_output)

        # 2. Call MiniSAT to solve the CNF
        with open(output_file, 'w') as minisat_output:
            subprocess.run(['minisat', cnf_file, output_file], stdout=subprocess.PIPE)

        # Append header for stat_file_name information
        with open(stat_file_name, 'a') as stat_file:
            stat_file.write(f"\n{'='*20}\nminiSAT stat output for test {prefix} {number_str}\n{'='*20}\n")
            subprocess.run(['minisat', cnf_file, output_file], stdout=stat_file, stderr=stat_file)

        # 3. Convert to Sudoku solution
        with open(output_file, 'r') as sat_input, open(sudoku_output_file, 'a') as sudoku_output:
            subprocess.run(['python', '../sat2sud.py'], stdin=sat_input, stdout=sudoku_output)

def main():
    # Project Euler tests (50)
    run_commands()

    # Top95 tests (95)
    run_commands(prefix='hard_grid', sudoku_output_file='hard_sudoku_output.txt', stat_file_name='hard_stat.txt')

if __name__ == '__main__':
    main()