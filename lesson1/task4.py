number = int(input('Введите целое положительное число: '))
biggest = 0

while number != 0:
    if number % 10 > biggest:
        biggest = number % 10
    number //= 10

print(biggest)
