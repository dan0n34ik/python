class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


nums = input('Введите два числа через пробел: ')
num1, num2 = int(nums.split()[0]), int(nums.split()[1])

try:
    if num2 == 0:
        raise DivisionByZeroError('На ноль делить нельзя!!!')
    print(num1 / num2)
except DivisionByZeroError as err:
    print('\033[31m' + str(err) + '\033[0m')
