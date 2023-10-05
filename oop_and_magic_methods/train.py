"""ДЗ:

1 -
Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів (необхідно додати об’єкти та
екземпляри класу вагонів). Опишіть клас Вагон разом із поїздом. Вагон повинен містити список пасажирів і дозволяти
додавати пасажирів. У Вагоні може бути наприклад не більше 10 пасажирів. Під час використання функції len у вагоні
я хочу бачити кількість пасажирів. Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива. Кожен
вагон повинен мати номер. Під час друку вагона на консолі я хочу бачити наступне «[n]», де n — номер вагона.

Реалізуйте друк потяга із завдання 2. Під час друку потяга вагони та локомотив мають відображатися на консолі у
такому форматі:

<=[HEAD]-[1]-[2]-[3]-[4]-[...]

Describe the "Train" object. The class must contain fields and a method for adding wagons (it is necessary to add
objects and instances of the wagon class). Describe the Wagon class together with the train. The carriage must contain
a list of passengers and permit add passengers For example, there can be no more than 10 passengers in a Car.
When using the len function in the carriage I want to see the number of passengers. Using len on a train,
I want to see a list of cars without a locomotive. Everyone the wagon must have a number. When printing a car
to the console, I want to see the following "[n]", where n is the car number.

Implement the print train from task 2. When printing the train, the cars and the locomotive should be displayed on the
console in in this format:

<=[HEAD]-[1]-[2]-[3]-[4]-[...]
"""


class Wagon:
    def __init__(self, name: str = "0"):
        self.__name = name
        self.__passenger = {}
        self.__passenger_count = 0

    @property
    def name(self):
        """
        getter name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        setter name
        """
        self.__name = new_name

    def __setitem__(self, key, value):
        if self.__passenger_count <= 10:
            self.__passenger[key] = value
            self.__passenger_count += 1
        else:
            raise Exception("There are many passengers")

    def __getitem__(self, key):
        return self.__passenger[key]

    def __len__(self):
        return len(self.__passenger)

    def __str__(self):
        return f"[{self.name}]"

    def show_passenger(self):
        for i in self.__passenger.values():
            print(i)


class Train:

    def __init__(self, name: str, Wagon):
        self.__name = name
        self.__wagons = Wagon()
        self.str_wag = ""

    def __setitem__(self, key, value):
        self.__wagons[key] = value
        self.str_wag += str(value) + "-"

    def __getitem__(self, key):
        return self.__wagons[key]

    def __len__(self):
        return len(self.__wagons) - 1

    def __str__(self):
        return f"{self.str_wag}"


if __name__ == '__main__':
    intercity = Train("intercity", Wagon)

    w1 = intercity[0] = Wagon("HEAD")
    w2 = intercity[1] = Wagon("1")
    w3 = intercity[2] = Wagon("2")
    w2[0] = "Alice"
    w2[1] = "Mariia"
    w2[2] = "Petr"
    w2[3] = "Alice"
    w2[4] = "Mariia"
    w2[5] = "Petr"

    w2.show_passenger()

    print("Wagon's size: ", len(w2))
    print("Train's size: ", len(intercity))
    print(w1)
    print(intercity)


