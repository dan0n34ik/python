def my_func(x, y):
    x_st = 1
    for i in range(abs(y)):
        x_st *= x
    print(x ** y)
    print(1 / x_st)


try:
    x1 = float(input('Введите действительное положительное число: '))
    if x1 < 0:
        print('Надо было ввести положительное число.')
    else:
        y1 = int(input('Введите целое отрицательное число: '))
        if y1 >= 0:
            print('Надо было ввести отрицательное число.')
        else:
            my_func(x1, y1)
except ValueError:
    print('Я же просил число.')
