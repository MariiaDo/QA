from abc import ABC, abstractmethod
class Profession(ABC):

    def __init__(self, name: str, regulated_profession: bool = False):
        """
        Initialization
        :param name: str (required parameter)
        """
        self.__name = name
        self.__regulated_profession = regulated_profession
        self.__expected_salary = None
        self.__skills = []

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

    def add_skills(self, new_skill):
        """
        Add a new skill
        """
        self.__skills.append(new_skill)

    def show_skills(self):
        """
        Returns a list of prof skills
        """
        return self.__skills

    def __str__(self):
        return f"{self.__dict__}"

    @abstractmethod
    def show_expected_salary(self):
        pass
"""
if __name__ == '__main__':
    qa = Profession("qa")
    print(qa.name)
    qa.name = "software tester"
    print(qa.name)
    skills = ["manual tasting", "analitical skills"]
    qa.add_skills(skills)
    print(qa.show_skills())
"""