#!/bin/bash
cp sud2sat.py sud2sat
cp sat2sud.py sat2sud
cp sud2sat2.py sud2sat2
cp sat2sud2.py sat2sud2
cp sud2sat3.py sud2sat3
cp sat2sud3.py sat2sud3
cp ./testing/main_testing_driver.py ./testing/main_testing_driver

chmod +x sud2sat
chmod +x sat2sud
chmod +x sud2sat2
chmod +x sat2sud2
chmod +x sud2sat3
chmod +x sat2sud3
chmod +x ./testing/main_testing_driver


echo "SAT-based Sudoku Solver is ready to run."