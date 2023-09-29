from medical import Medical


class Doctor(Medical):
    def __init__(self, name: str):
        """
        Initialisation

        """
        super().__init__(name)
        self.__family_doctor = None
        self.__age_of_internship = None

    def appoint_family_doctor(self, family_doctor: bool):
        """
        Function assigns to doctor a value "Family doctor"(true or false)

        """
        self.__family_doctor = family_doctor

    def change_age_of_internship(self, new_ages: int):
        """
        Function changes ages of internship

        """
        self.__age_of_internship = new_ages


if __name__ == '__main__':
    dentist = Doctor("dentist")
    dentist.appoint_family_doctor(True)
    dentist.change_age_of_internship(10)
