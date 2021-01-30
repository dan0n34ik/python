from math import factorial


def fact(num):
    for i in range(1, num + 1):
        yield factorial(i)


n = int(input('Введите число: '))
for el in fact(n):
    print(el)
