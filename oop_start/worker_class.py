"""
2 -

Create a class with a description of the worker. Any worker or employees.
Оцінюватиму повноту описаного класу, згідно пройденого матеріалу. Я очікую побачити чистий
код із анотаціями. Поки що ніяких зв'язків першого класу з другим.
У всіх методах я очікую побачити рядки документації з зрозумілим описом.
"""


class Worker:
    def __init__(self, name: str, company: str):
        """
        Initialization
        """
        self.__name = name
        self.__company = company
        self.__position = None
        self.__skills = []

    @property
    def name(self):
        """
        getter name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        setter name
        """
        self.__name = new_name

    @property
    def company(self):
        """
        getter company
        """
        return self.__company

    @company.setter
    def company(self, new_company):
        """
        setter company
        """
        self.__company = new_company

    def change_position(self, new_position):
        """
        Function to change current position. Can be string or None
        """
        print(f"Do you want to change current position on {new_position}?")
        inp = input("Enter Y / N: ")
        if inp == "Y" or inp == "y":
            self.__position = new_position
            return self.__position
        else:
            return print(f"Position not changed. It is still {self.__position}")

    def __str__(self):
        """
        Description of the string function for an object. Possible to use for checking any changes
        """
        return f"{self.__name} {self.__company} {self.__position}"

    def add_skills(self, list_skills):
        """
        Function let's to add new skills to worker
        :return: list of skills
        """
        for i in list_skills:
            self.__skills.append(i)
            return self.__skills

    def show_skills_info(self):
        """
        Function let's to see all worker's skills
        :return:
        """
        for i in skills:
            print(i)


if __name__ == '__main__':
    mariia = Worker("Mariia", "daimler")
    print(mariia.name)
    mariia.name = "Masha"
    print(mariia.name)
    print(mariia.company)
    mariia.company = "AnyDesk"
    print(mariia.company)
    mariia.change_position("QA automation")
    print(str(mariia))
    skills = ['python', 'selenium web-driver', 'api-test']
    mariia.add_skills(skills)
    mariia.show_skills_info()
