"""3 -
Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
Ця функція намалює простий прямокутник заданої висоти та ширини, використовуючи character для друку ліній.
Наприклад, display_box(5, 4, 'x') має вивести наступне:

xxxxx

x x

x x

xxxxx
"""


def display_box(width: int, height: int, character="*"):
    for i in range(1, height + 1):
        if i == 1 or i == (height):
            print(character * width)
        else:
            spase = " " * (width - 2)
            print(character + spase + character)


if __name__ == '__main__':
    display_box(5, 10, "/")
    display_box(7, 5, "#")
