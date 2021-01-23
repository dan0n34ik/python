str_from_user = input('Введите какие-то слова через пробел: ')

list_from_split_str = str_from_user.split()
count = 1

for i in list_from_split_str:
    if len(i) < 10:
        print(f'{count}. {i}')
    else:
        print(f'{count}. {i[:11]}')
    count += 1
