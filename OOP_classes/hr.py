from it_spesialist import IT_spesialist


class Hr(IT_spesialist):

    def __init__(self, name: str, years_experience: int, english_level: str):
        """
            initialisation function

            """
        super().__init__(name, years_experience, english_level)
        self.__years_experience = years_experience
        self.__english_level = english_level
        self.__closed_vacancies = None
        self.__top_managers_vacancies = None

    def change_closed_vacancies(self, new_closed_vacancies: int):
        """
        Function changes closed_vacancies

        """
        self.__closed_vacancies = new_closed_vacancies

    def change_top_managers_vacancies(self, top_managers_vacancies: bool):
        """
        Function changes top_managers_vacancies

        """
        self.__top_managers_vacancies = top_managers_vacancies

    def show_expected_salary(self): # polimorphism
        print(f"Зарплата у {self.name} тоже в порядке")