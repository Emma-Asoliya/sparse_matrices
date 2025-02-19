import re
from collections import defaultdict

class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        self.matrix = defaultdict(int)
        self.num_rows = num_rows
        self.num_cols = num_cols
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.num_rows = int(re.search(r'\d+', lines[0]).group())
                self.num_cols = int(re.search(r'\d+', lines[1]).group())

                for line in lines[2:]:
                    match = re.match(r'\((\d+),\s*(\d+),\s*(-?\d+)\)', line)  
                    if match:
                        row, col, value = map(int, match.groups())
                        self.matrix[(row, col)] = value
        except Exception as e:
            raise ValueError(f'Error loading matrix from file {file_path}: {e}')
        
    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)
    
    def set_element(self, row, col, value):
        if value == 0:
            self.matrix.pop((row, col), None)
        else:
            self.matrix[(row, col)] = value

    def __add__(self, other):
        max_rows = max(self.num_rows, other.num_rows)
        max_cols = max(self.num_cols, other.num_cols)

        result = SparseMatrix(num_rows=max_rows, num_cols=max_cols)

        for (row, col), value in self.matrix.items():
            result.matrix[(row, col)] += value

        for (row, col), value in other.matrix.items():
            result.matrix[(row, col)] += value

        return result

    def __sub__(self, other):
        max_rows = max(self.num_rows, other.num_rows)
        max_cols = max(self.num_cols, other.num_cols)
        
        result = SparseMatrix(num_rows=max_rows, num_cols=max_cols)

        for (row, col), value in self.matrix.items():
            result.matrix[(row, col)] += value

        for (row, col), value in other.matrix.items():
            result.matrix[(row, col)] -= value

        return result
    
    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError('Wrong matrix dimensions for multiplication')
    
        result = SparseMatrix(self.num_rows, other.num_cols)

        for (row, col), value in self.matrix.items():
            for k in range(other.num_cols):
                result.matrix[(row, k)] += value * other.get_element(col, k)

        return result
    
    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (row, col), value in sorted(self.matrix.items()):
                file.write(f"({row}, {col}, {value})\n")


def main():
    file1 = 'easy_sample_02_1.txt'
    file2 = 'easy_sample_03_1.txt'

    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    print(f'Matrix 1: {matrix1.num_rows}x{matrix1.num_cols}')
    print(f'Matrix 2: {matrix2.num_rows}x{matrix2.num_cols}')

    operation = input("Select an option: 1. Add, 2. Subtract, 3. Multiply: ").strip().lower()
    output_file = "result_matrix.txt"

    if operation == '1' or operation == 'add':
        result = matrix1 + matrix2
    elif operation == '2' or operation == 'subtract':
        result = matrix1 - matrix2
    elif operation == '3' or operation == 'multiply':
        try:
            result = matrix1 * matrix2
        except ValueError as e:
            print(f"Error: {e}")
            return
    else:
        print('Invalid operation')
        return

    result.save_to_file(output_file)
    print(f'Result saved to {output_file}')


if __name__ == "__main__":
    main()
