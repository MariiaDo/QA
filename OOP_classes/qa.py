from it_spesialist import IT_spesialist


class Qa(IT_spesialist):
    def __init__(self, name: str, years_experience: int, english_level: str, automation: bool = False):
        """
        initialisation function

        """
        super().__init__(name, years_experience, english_level)
        self.__years_experience = years_experience
        self.__english_level = english_level
        self.__automation = automation
        self.__programming_languages = []

    @property
    def automation(self):
        """
        getter automation
        """
        return self.__automation

    @automation.setter
    def automation(self, new_automation):
        """
        setter automation
        """
        self.__automation = new_automation

    def add_programming_languages(self, new_programming_language):
        """
        Add a programming language
        """
        self.__programming_languages.append(new_programming_language)

    def show_programming_languages(self):
        """
        Returns a list of programming languages
        """
        return self.__programming_languages

    def show_expected_salary(self):
        print(f"Зарплата у {self.name} будет норм")


if __name__ == '__main__':
    qa = Qa('qa', 10, "upper")
    qa.automation = True
    qa.add_programming_languages("python")
    print(qa.automation, qa.show_programming_languages())
    qa.show_expected_salary()
