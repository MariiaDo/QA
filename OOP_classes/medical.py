from profession import Profession


class Medical(Profession):

    def __init__(self, name: str):
        super().__init__(name, regulated_profession=True)
        self._med_level = "None"
        self.__work_in_hospital = None

    def change_med_level(self):
        """
        Function changes med level from 3 options
        :return:
        """
        user_level = input(
            "Нажмите 1, если необходимо присвоить высший уровень, нажмите 2, если средний и 3 - если младший: ")
        if user_level == "1":
            self._med_level = "high"
        elif user_level == "2":
            self._med_level = "middle"
        else:
            self._med_level = "low"

    def show_med_level(self):
        """
        Function shows current medical level
        """
        return self._med_level


if __name__ == '__main__':
    dentist = Medical("dentist")
    dentist.change_med_level()
    print(dentist.show_med_level())
