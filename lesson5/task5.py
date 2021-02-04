with open('file1.txt', 'w+', encoding='utf-8') as f:
    summ = 0
    nums = input('Enter numbers: ')
    f.write(f'{nums}\n')
    f.seek(0)
    nums = f.readline().split()
    for i in nums:
        summ += int(i)
    print(summ)
