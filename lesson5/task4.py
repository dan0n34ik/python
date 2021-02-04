nums_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('nums.txt', encoding='utf-8') as f:
    with open('russian_nums.txt', 'w', encoding='utf-8') as my_f:
        for i in f.readlines():
            my_f.write(f'{nums_dict[i.split()[0]]}\n')
