from itertools import cycle, count

start_num = int(input('Введите 1 число: '))

for i in count(start_num):
    if i > 10:
        break
    print(i)

print('-' * 100)

my_list = [1, 45, 50, 2, 4]

c = 0
for i in cycle(my_list):
    if c > 9:
        break
    if c != 9:
        print(i, end=', ')
    elif c == 9:
        print(i)
    c += 1
