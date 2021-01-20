viruchka = int(input('Введите выручку фирмы: '))
izderzhki = int(input('Введите издержки фирмы: '))
prib = viruchka - izderzhki

if viruchka > izderzhki:
    print(f'Фирма отработала с прибылью {prib} рублей.')
    sotr = int(input('Сколько сотрудников у этой фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {prib / sotr}')
else:
    print('У этой фирмы нет прибыли.')
