"""1-ДЗ 8. Decorators, Generators

Створіть декоратор, який виводить в консоль назву викликаної функції. Наприклад, створіть пару функцій
для арифметичних операцій підсумовування та множення. Під час виклику цих функцій має бути повернутий
результат операції, а ім’я викликаної функції має відображатися на консолі разом із результатом.
Маленька підказка (__name__)"""


def funk_name(func):
    def wrapper(*args):
        func(*args)
        print(func.__name__)

    return wrapper


@funk_name
def my_sum(a, b):
    print(a + b, end=" ")


@funk_name
def my_mult(a, b):
    print(a * b, end=" ")


if __name__ == '__main__':
    my_sum(5, 10)
    my_mult(15, 14)
