from doctor import Doctor


class Surgeon(Doctor):

    def __init__(self, name: str):
        """
        Initialisation function
        :param name:
        """
        super().__init__(name)
        self.__access_to_operations_as_primary_surgeon = None
        self.__years_of_operating_activity = None

    def let_access_to_operations_as_primary_surgeon(self):
        """
        After execution, function assigns permission to operations as primary surgeon(value = true)

        """
        self.__access_to_operations_as_primary_surgeon = True

    def change_years_of_operating_activity(self, years: int):
        """
        Function let's to change years of operating activity

        """
        self.__years_of_operating_activity = years

    def show_years_of_operating_activity(self):
        """
        Function let's to see years of operating activity

        """
        return self.__years_of_operating_activity

    def show_expected_salary(self):  # polimorphism
        print(f"Зарплата у {self.name} вообще супер!")

if __name__ == '__main__':
    dentist = Surgeon("dentist")
    dentist.change_years_of_operating_activity(10)
    print(dentist.show_years_of_operating_activity())
    dentist.let_access_to_operations_as_primary_surgeon()
