with open('learning.txt', encoding='utf-8') as fl:
    my_dict = {}
    for i in fl.readlines():
        summ = 0
        spl_li = i.split()
        for j in spl_li[1:]:
            num = ''
            for k in j:
                if k == '(' or k == '-':
                    break
                num += k
            if num != '-' and num != '':
                summ += int(num)
        my_dict.update({spl_li[0][:-1]: summ})

print(my_dict)
