from beauty_profession import Beauty_profession


class Colorist(Beauty_profession):
    def __init__(self, name: str):
        """
        Initialisation

        """
        super().__init__(name)
        self.__coloring_techniques = []
        self.__work_on_materials = []

    def add_coloring_techniques(self, new_coloring_techniques):
        """
        Function let's to add new type of coloring_techniques
        :return: list of coloring_techniques
        """
        for i in new_coloring_techniques:
            self.__coloring_techniques.append(i)
        return self.__coloring_techniques

    def show_coloring_techniques(self):
        """
        Function let's to see coloring_techniques
        :return:
        """
        for i in self.__coloring_techniques:
            print(i)

    def show_expected_salary(self):  # polimorphism
        print(f"Зарплата у {self.name} зависит от количества клиентов. Сколько сделаешь, столько и будет")

if __name__ == '__main__':
    colorist = Colorist("colorist")
    coloring_techniques = ["air-touch", "total blond"]
    colorist.add_coloring_techniques(coloring_techniques)
    colorist.show_coloring_techniques()