from profession import Profession

class Beauty_profession(Profession):
    def __init__(self, name: str):
        super().__init__(name, regulated_profession=False)
        self.__service_list = []
        self.__certificates = []

    def add_service_list(self, service_list):
        """
        Function let's to add new type of service
        :return: list of services
        """
        for i in service_list:
            self.__service_list.append(i)
        return self.__service_list

    def show_service_list(self):
        """
        Function let's to see all services
        :return:
        """
        for i in self.__service_list:
            print(i)


if __name__ == '__main__':
    colorist = Beauty_profession("colorist")
    service = ["cutting", "coloring", "styling"]
    colorist.add_service_list(service)
    colorist.show_service_list()
