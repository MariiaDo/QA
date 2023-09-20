"""1 -

Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями."""


def sum_range(start: int, end: int):
    sum = 0
    for i in range(min(start, end), max(start, end) + 1):
        sum = sum + i
        i += 1
    return sum


if __name__ == '__main__':
    try:
        start = int(input("Enter start(integer): "))
        end = int(input("Enter end(integer): "))
        print(sum_range(start, end))
    except Exception as error:
        print(error)
