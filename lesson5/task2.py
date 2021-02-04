with open('my_file.txt', encoding='utf-8') as my_f:
    print(f'Количество строк: {len(my_f.readlines())}')
    my_f.seek(0)
    count = 1
    for i in my_f.readlines():
        print(f'{count} строка: {len(i.split())} слова')
        count += 1
