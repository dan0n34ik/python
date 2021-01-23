my_seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month_number = int(input('Введи номер месяца(только цифра): '))

while month_number > 12:
    print('Существует только 12 месяцев. Можешь придумать свой новый. Но у меня пока только 12.')
    month_number = int(input('Введите новое число: '))

for i in my_seasons_dict.items():
    if i[1][0] == month_number or i[1][1] == month_number or i[1][2] == month_number:
        print(i[0])
        break
