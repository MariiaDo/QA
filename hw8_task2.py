"""2-ДЗ 8. Decorators, Generators

Створіть функцію, яка може повертати квадрати парних чисел у діапазоні від 0 до 1000000000 включно.
Рішення має працювати і не фрізити комп’ютер."""


def kvadr_big_num(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            yield i * i


if __name__ == '__main__':
    for i in kvadr_big_num(1000000000):
        print(i)
