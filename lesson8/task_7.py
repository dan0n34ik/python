class OperationsWithComplexNumbers:
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __add__(self, other):
        return self.complex_number + other.complex_number

    def __mul__(self, other):
        return self.complex_number * other.complex_number


complex_num1 = OperationsWithComplexNumbers((5+2j))
complex_num2 = OperationsWithComplexNumbers((1+2j))
print(str(complex_num1 * complex_num2).replace('j', 'i'))
print(str(complex_num1 + complex_num2).replace('j', 'i'))
