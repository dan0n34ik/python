with open('info.txt', 'w', encoding='utf-8') as f:
    while True:
        words = input('Enter words and "Enter" or simply "Enter" to stop: ')
        if words == '':
            break
        f.write(f'{words}\n')
