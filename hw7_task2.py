"""2 -

Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх"""


def square(side):
    p = side * 4
    s = side ** 2
    d = (side ** 2 + side ** 2) ** 0.5
    return p, s, d


if __name__ == '__main__':
    perimetr, sq, diagonal = square(5)
    print("Периметр =", perimetr, "Площадь =", sq, "Диагональ =", diagonal)
    perimetr, sq, diagonal = square(8)
    print("Периметр =", perimetr, "Площадь =", sq, "Диагональ =", diagonal)
