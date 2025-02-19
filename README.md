Data_Structure_And_Algorithms
Sparse Matrix Operations
Overview
This project implements Sparse Matrix Operations in Python. The program supports:

Reading sparse matrices from text files
Performing addition, subtraction, and multiplication on sparse matrices
Storing results in an output file
The SparseMatrix class efficiently stores and manipulates matrices using a dictionary representation to save memory by only keeping track of nonzero elements.

Features
Sparse Matrix Representation: Stores nonzero values using a dictionary
Matrix Operations: Supports addition, subtraction, and multiplication
File Input and Output: Reads matrix data from files and saves results to files
Command-Line Interface: Users can interactively provide input file paths and choose operations

Installation & Requirements
This project requires Python 3.7+.

1️⃣ Clone the Repository
git clone https://github.com/Emma-Asoliya/sparse_matrices.git
cd main.py
2️⃣ Run the Program
python main.py

Usage

Run the main.py script.

Enter the operation you want to perform:

1 for Addition

2 for Subtraction

3 for Multiplication

The result will be saved in result_matrix.txt.

Example Input Format

rows=5
cols=5
(0, 1, 10)
(2, 3, -5)
(4, 0, 20)
