with open('sotrudniki.txt', encoding='utf-8') as file1:
    summ = 0
    for i in file1.readlines():
        summ += float(i.split()[1])
        if float(i.split()[1]) < 20000.0:
            print(i.split()[0])
    file1.seek(0)
    print(summ / len(file1.readlines()))
