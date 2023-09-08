"""2 -

Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
 (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).

Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
Якщо введені числа не можуть бути float спіймайте ValueError
Також ловіть помилку при діленні на 0
В кожній спійманій помилці друкуйте пояснення, що пішло не так
За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором, якщо введені не вірні дані
Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
Результат виконання формули - float число з двома знаками після крапки """

class FormulaError(Exception):
    pass
class WrongOperatorError(Exception):
    pass
count = 3
while count != 0:
    try:
        expression = input("Please, enter expression like: a * b or a / b (with spaces between elements): ")
        list_expr = list(expression.split(" "))
        numbers = len(list_expr)
        if numbers != 3:
            raise FormulaError('Must be 3 elements in formula (with spaces between elements)')
        elif not (list_expr[1] == "*" or list_expr[1] == "/"):
            raise WrongOperatorError('Must be operator * or /')
        elif not (list_expr[0].isdigit() and list_expr[2].isdigit()):
            raise ValueError('The values entered are not numbers')
        elif list_expr[2] == str('0') and list_expr[1] == "/":
            raise ZeroDivisionError("Can't divide by zero")
        else:
            res = eval(expression)
            rounded_res = ("{:.2f}".format(res))
            print(rounded_res)
    except Exception as error:
        print(error)
    else:
        print("Этот блок использую для break, хотя его можно было написать и в конце блока try")
        break
    finally:
        count -= 1
        print(f"You used {3 - count} attempts out of 3.")

