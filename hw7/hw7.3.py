class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            return 'Отрицательное значение!'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row=3):
        new_cell = []
        ce = self.cells
        for el in range(row):
            n = 0
            for el in range(ce):
                if n < row:
                    new_cell.append('*')
                    n += 1
                    ce -= 1
                else:
                    continue
            if ce != 0:
                new_cell.append('\\n')
        return ''.join(new_cell)

    def __str__(self):
        return f'Клетка с количеством ячеек: {self.cells}'


a = Cell(15)
print(a.make_order())
b = Cell(4)
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)
