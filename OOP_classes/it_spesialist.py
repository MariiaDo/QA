from profession import Profession


class IT_spesialist(Profession):
    def __init__(self, name: str, years_experience: int, english_level: str):
        super().__init__(name, regulated_profession=False)
        self.__years_experience = years_experience
        self.__english_level = english_level
        self.__company_type = None
        self.__linkedin = ""

    @property
    def years_experience(self):
        """
        getter years_experience
        """
        return self.__years_experience

    @years_experience.setter
    def years_experience(self, new_years_experience: int):
        """
        setter years_experience
        """
        self.__years_experience = new_years_experience

    @property
    def english_level(self):
        """
        getter english_level
        """
        return self.__english_level

    @english_level.setter
    def english_level(self, new_english_level: str):
        """
        setter english_level
        """
        self.__english_level = new_english_level


if __name__ == '__main__':
    qa = IT_spesialist("qa", 5, "intermediate")
    qa.years_experience = 6
    qa.english_level = "upper-intermediate"
    print(qa.years_experience, qa.english_level)
