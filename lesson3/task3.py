def my_func(var1, var2, var3):
    my_list = [var1, var2, var3]
    a = my_list.pop(my_list.index(max(my_list)))
    b = my_list.pop(my_list.index(max(my_list)))

    return a + b


try:
    num1 = int(input('Введи 1 число: '))
    num2 = int(input('Введи 2 число: '))
    num3 = int(input('Введи 2 число: '))

    print(my_func(num1, num2, num3))
except ValueError:
    print('Я же просил число.')
