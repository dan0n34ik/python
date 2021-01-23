my_list = [7, 5, 3, 3, 2]

while True:
    new_num = input('Введите число или "стоп" чтобы остановиться: ')
    if new_num.lower() == 'стоп':
        break
    count = int(new_num)
    for i in my_list:
        if count > i:
            my_list.insert(my_list.index(i), count)
            break

for i in my_list:
    print(i, sep=', ')
