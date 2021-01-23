my_list = []

while True:
    sym = input('Enter "stop" to stop the process or something to make the list bigger: ')

    if sym.lower() == 'stop':
        print('The dict has completed.')
        break
    my_list.append(sym)

for i in range(0, len(my_list), 2):
    if i == len(my_list) - 1:
        break
    x = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = x

print(my_list)
