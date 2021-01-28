summ = 0
flag = False

while True:
    nums = input('Введите "Q" чтобы выйти или числа через пробел чтобы продолжить: ')
    for i in nums.split():
        if i.upper() == 'Q':
            flag = True
            break
        try:
            summ += int(i)
        except ValueError:
            print('Можно вводить только числа или специальный символ "Q"!')
    print(summ)
    if flag:
        break
