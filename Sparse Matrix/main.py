class SparseMatrix:
    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.cols = 0
        self.data = []

    def create_matrix(self):
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of columns: "))

        for i in range(self.rows):
            row = list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split()))
            if len(row) != self.cols:
                raise ValueError("Invalid number of columns")
            self.matrix.append(row)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != 0:
                    self.data.append((i, j, self.matrix[i][j]))

    def transpose(self):
        transposed_data = [(j, i, val) for i, j, val in self.data]
        self.data = transposed_data
        self.rows, self.cols = self.cols, self.rows

    def change_element(self, row, col, new_val):
        for i, (r, c, val) in enumerate(self.data):
            if r == row and c == col:
                self.data[i] = (row, col, new_val)
                break

        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 0:
                    for k, (r, c, val) in enumerate(self.data):
                        if r == i and c == j:
                            self.matrix[i][j] = val
                            break


sparse_matrix = SparseMatrix()
sparse_matrix.create_matrix()


sparse_matrix.transpose()
print("Transposed matrix:")
for row in sparse_matrix.matrix:
    print(row)


row = int(input("Enter the row index to change: "))
col = int(input("Enter the column index to change: "))
new_val = int(input("Enter the new value: "))
sparse_matrix.change_element(row, col, new_val)


print("Updated matrix:")
for row in sparse_matrix.matrix:
    print(row)
