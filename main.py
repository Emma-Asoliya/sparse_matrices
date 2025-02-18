import re
from collections import defaultdict

class SparseMatrix:
    def __init__(self, file_path):
        self.matrix = defaultdict(int)
        self.num_rows = 0
        self.num_cols = 0
        self.load_from_file(file_path)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                slef.num_rows = int(re.search(r'\d+', lines[0]).group())
                self.num_cols = int(re.search(r'\d+', lines[1]).group())

                for line in lines[2:]:
                    match = re.match(r'\((d+, \s*(\d+), \s*(-?\d+)\)', line)
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

    def __add__(self, other);
        if self.num_rows != other.num_rows or self.num-cols != other.num_cols:
            raise ValueError('Matrices must have the same dimensions to be added')
        
        result = SparseMatrix.create_empty(self.num_rows, self.num_cols)
        result.matrix = self.matrix.copy()

        for (row, col), value in other.matrix.items():
            result.matrix[(row, col)] += value

        return result
    
    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError(Wrong matrix dimensions for multiplication')
    
        result = SparseMatrix.create_empty(self.num_rows, other.num_cols)

        for (row, col), value in self.matrix.items():
        for k in range(other.num_cols):
            result.matrix[(row, k)] += value * other.get_element(col, k)

        return result


    @staticmethod
    def create_empty(rows, cols):
        obj = SparseMatrix.__new__(SparseMatrix)
        obj.matrix = defaultdict(int)
        obj.num_rows = rows
        obj.num_cols = cols
        return obj