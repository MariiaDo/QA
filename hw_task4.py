"""4 - написати власну функцію map, використовуючи callback"""


def own_map(fanc, x):
    return list([fanc(i) for i in x])


if __name__ == '__main__':
    my_list1 = [10, 24, 3, 7, 11]
    my_list2 = [3, -4, 7, 5, 2, 3]

    print(own_map(lambda x: x * 2, my_list1))
    print(own_map(lambda x: x ** 2, my_list2))
