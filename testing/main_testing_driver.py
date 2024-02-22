import subprocess

def run_testing_suite():
    subprocess.run(['python', 'testing_suite.py'])
    subprocess.run(['python', 'testing_suite_analysis.py'])

def main():
    # Driver for testing all versions
    run_testing_suite()

if __name__ == "__main__":
     main()