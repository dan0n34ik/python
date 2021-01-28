def int_func(word):
    for i in word:
        if (ord(i) < 97 or ord(i) > 122) and ord(i) != 32:
            return 'Нужно было вводить маленькими латинскими буквами.'
    return word.title()


word1 = input('Введите строку маленькими латинскими буквами через пробел: ')
print(int_func(word1))
