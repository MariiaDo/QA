"""3-ДЗ 8. Decorators, Generators

Створіть декоратор, який повертає результат функції. а також час за який вона виконана. П
ідсказка (для фіксації часу імпортуйте модуль time:  import time)"""

import time

def funk_with_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("Время старта функции: ", start_time)
        print("Время окончания функции: ", end_time)
        print("Итого функция выполнилась за: ", end_time - start_time, "сек.")
    return wrapper

@funk_with_time
def factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print("Факториал = ", factorial)


if __name__ == '__main__':
    factorial(20000)

