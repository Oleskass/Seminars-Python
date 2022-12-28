class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        matr = ''
        for i in self.my_matrix:
            for j in i:
                matr += f'{j} '
            matr += '\n'
        return matr

    def __add__(self, other):
        matrix_sum = ''
        for i in range(len(self.my_matrix)):
            m = []
            for j in range(len(other.my_matrix)):
                m.append(
                    int(self.my_matrix[i][j]) + int(other.my_matrix[i][j]))
            matrix_sum = matrix_sum + str(m) + '\n'
        return matrix_sum


obj_1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
obj_2 = Matrix([[4, 5, 6], [7, 8, 9], [3, 6, 9]])
print(obj_1 + obj_2)
