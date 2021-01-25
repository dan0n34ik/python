my_list = []
count = 1
stop = input('Введите "стоп" чтобы остановиться или "следующий товар" чтобы продолжить заполнение: ')

while True:
    if stop != 'следующий товар' and stop != 'стоп' and count != 1:
        stop = input('Введите "стоп" чтобы остановиться или "следующий товар" чтобы продолжить заполнение: ')
    if stop.lower() == 'стоп':
        break
    elif stop.lower() == 'следующий товар':
        name = input('Введите название товара: ')
        cost = int(input('Введите цену товара в рублях: '))
        how_many = int(input('Введите количество товара: '))
        edin = input('Введите в какой единице измерения считается этот товар: ')
        my_list.append((count, {'название': name, 'цена': cost, 'количество': how_many, 'ед. измерения': edin}))
        stop = ''
        count += 1
    else:
        while True:
            print('Я же говорил либо "следующий товар", либо "стоп"')
            stop = input('Введите "стоп" чтобы остановиться или "следующий товар" чтобы продолжить заполнение: ')
            if stop.lower != 'стоп' or stop.lower() != 'следующий товар':
                break
count1 = 1

for a in my_list:
    if count1 != count:
        print(a, end=',\n')
    elif count1 == count:
        print(a)

my_dict = {'название': [], 'цена': [], 'количество': [], 'ед. измерения': []}

for i in my_list:
    name1 = i[1]['название']
    my_dict['название'].append(name1)
    cost1 = i[1]['цена']
    my_dict['цена'].append(cost1)
    how_many1 = i[1]['количество']
    my_dict['количество'].append(how_many1)
    edin1 = i[1]['ед. измерения']
    my_dict['ед. измерения'].append(edin1)

count1 = 1

for j in my_dict.items():
    if count1 != 4:
        print(f'"{j[0]}": {j[1]}', end=',\n')
    else:
        print(f'"{j[0]}": {j[1]}')

    count1 += 1
