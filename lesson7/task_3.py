class Cell:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __add__(self, other):
        return f'{self.p_1} + {other.p_1} = {self.p_1 + other.p_1}'

    def __sub__(self, other):
        if self.p_1 - other.p_1 <= 0:
            return f'{self.p_1} - {other.p_1} меньше или равно нулю.'
        return f'{self.p_1} - {other.p_1} = {self.p_1 - other.p_1}'

    def __mul__(self, other):
        return f'{self.p_1} * {other.p_1} = {self.p_1 * other.p_1}'

    def __truediv__(self, other):
        return f'{self.p_1} / {other.p_1} = {self.p_1 // other.p_1}'

    def make_order(self, rows):
        self.make_order_str = ''
        count = self.p_1
        for i in range(self.p_1 // rows + 1):
            if count < rows:
                self.make_order_str += '\033[31m' + '*' + '\033[0m' * count
            else:
                self.make_order_str += '\033[31m*\033[0m' * rows + '\n'
            count -= rows
        return self.make_order_str


cell1 = Cell(13)
cell2 = Cell(12)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(4))
