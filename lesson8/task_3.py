class OnlyNumbersError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_only_for_nums = []
while True:
    num = input('Введите число или "stop": ')
    if num == 'stop':
        print(list_only_for_nums)
        break
    try:
        for i in num:
            if ord(i) < 49 or ord(i) > 57:
                raise OnlyNumbersError('Можно вводить только цифры!!!')
        list_only_for_nums.append(int(num))
    except OnlyNumbersError as err:
        print('\033[31m' + str(err) + '\033[0m')
