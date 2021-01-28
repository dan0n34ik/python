def my_func(num1, num2):
    try:
        return f'{num1 / num2:.2f}'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(my_func(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
