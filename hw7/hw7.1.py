class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self,other):
        matr = []

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                matr.append(str(self.matrix[i][j] + other.matrix[i][j]))
                matr.append(' ')
            matr.append('\n')


        return ''.join(matr)

    def __str__(self):
        pass

m_1 = Matrix([[1,2],
              [3,4],
              [5,6]])

m_2 = Matrix([[7,8],
              [9,10],
              [11,12]])
m_3 = m_1 + m_2

print(m_3)
