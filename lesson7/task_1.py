class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.str_matrix = ''
        for i in self.matrix:
            for j in i:
                self.str_matrix += str(j) + '\t'
            self.str_matrix += '\n'
        return self.str_matrix

    def __add__(self, other):
        self.new_matrix = []
        for i in range(len(self.matrix)):
            self.new_matrix.append(self.matrix[i].copy())
            for j in range(len(self.matrix[i])):
                try:
                    self.new_matrix[i][j] += other.matrix[i][j]
                except IndexError as err:
                    return err
        return Matrix(self.new_matrix)


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1 + my_m2)
print(my_m1)
