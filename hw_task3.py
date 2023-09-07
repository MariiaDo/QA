"""3 - Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
Виведіть словник на екран."""

my_dict_1 = {'python': 'Guido van Rossum', 'java': 'James Gosling',
             'c++': 'Bjarne Stroustrup', 'ruby': 'Yukihiro Matsumoto'}

for i in my_dict_1:
    autor = my_dict_1[i]
    print(f"My favorite programming language is {i}. It was created by {autor}.")
my_dict_1.popitem()
print(f"New dict after deleting: {my_dict_1}")



