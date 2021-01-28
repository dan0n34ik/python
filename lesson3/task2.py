def my_func(name, surname, year_birthday, city, email, phone):
    return f'Имя: {name}, фамилия: {surname}, год рождения: {year_birthday}, город проживания: {city},' \
           f' электронная почта: {email}, номер телефона: {phone}.'


try:
    name1 = input('Введите имя: ')
    surname1 = input('Введите фамилмю: ')
    year_birthday1 = int(input('Введите год рождения: '))
    city1 = input('Введите город проживания: ')
    email1 = input('Введите адрес электронной почты: ')
    phone1 = int(input('Введите номер телефона: '))
    print(my_func(name=name1, surname=surname1, year_birthday=year_birthday1, city=city1, email=email1, phone=phone1))
except ValueError:
    print('Error!')
