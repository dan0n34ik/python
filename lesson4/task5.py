from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_num, num):
    return prev_num * num


print(reduce(my_func, my_list))
