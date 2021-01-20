sec = int(input('Введите время в секундах: '))

hours = sec // 3600
sec = sec - hours * 3600
minuts = sec // 60
sec = sec - minuts * 60

print('%02d:%02d:%02d' % (hours, minuts, sec))
