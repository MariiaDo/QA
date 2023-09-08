"""1 -

Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

Лише за допомогою функцій map, lambda, zip створити та надрукувати словник квадратів цих чисел.

Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}"""

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = list((map(lambda x: int(x), str_list)))
kvadr_list = list((map(lambda x: x * x, int_list)))
new_dict = dict(zip(int_list, kvadr_list))
print(f"New dict is: {new_dict}")
