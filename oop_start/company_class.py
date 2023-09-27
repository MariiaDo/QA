"""1 -

Create a class describing any company. For example, Toshiba or Apple"""
from datetime import datetime


class Company:

    def __init__(self, name: str, industry: str = "automotive", company_type: str = "public company",
                 ipo: bool = True):
        """
        Initialization
        :param name: str (required parameter)
        :param industry: str = "automotive"
        :param company_type: str = "public company"
        :param ipo: bool = True
        """
        self.__name = name
        self.__industry = industry
        self.__company_type = company_type
        self.__ipo = ipo
        self.__capital = None
        self.__list_of_products = []
        self.__quantity_of_employees = None
        self.__private_access = {'login': 'mari', 'passw': '1234'}

    @staticmethod
    def show_date_of_viewing_information():
        """
        Static method. Prints the current date and time
        """
        current_datetime = datetime.now()
        print(current_datetime)

    @classmethod
    def from_dict(cls, dict_company):
        """
        Method for changing class structure. Add profit
        """
        return cls(dict_company.get('name'), dict_company.get('industry'), dict_company.get('company_type'),
                   dict_company.get('profit'))

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
    def industry(self):
        """
        getter industry
        """
        return self.__industry

    @industry.setter
    def industry(self, new_industry):
        """
        setter industry
        """
        self.__industry = new_industry

    @property
    def company_type(self):
        """
        getter company_type
        """
        return self.__company_type

    @company_type.setter
    def company_type(self, new_company_type):
        """
        setter company_type
        """
        self.__company_type = new_company_type

    def add_product(self, product):
        """
        Add a new product, which company produces
        """
        self.__list_of_products.append(product)

    def show_products(self):
        """
        Returns a list of all products that the company produces
        """
        return self.__list_of_products

    def __str__(self):
        """
        Description of the string function for an object
        """
        return f"{self.__name} {self.__company_type} {self.__ipo}"

    def __repr__(self):
        """
        Description of the repr function for an object
        """
        return f"Company: {self.__name}, Products: {self.__list_of_products})"

    def __access_check(self, login, passw):
        """
        Access check utility function. Just for using inside the class
        """

        if self.__private_access['login'] == login and self.__private_access['passw'] == passw:
            return True
        else:
            return False

    def ipo_change(self, login: str, passw: str, new_value: bool):
        """
        Change current ipo, if you have enough access. Return bool value
        """

        if self.__access_check(login, passw) is True:
            self.__ipo = new_value
        else:
            print("not enough access")

    def ipo_check(self):
        """
        check current ipo value. Return bool
        """
        return self.__ipo


if __name__ == '__main__':
    daimler = Company("Daimler")
    daimler.show_date_of_viewing_information()
    print(daimler.company_type)
    daimler.company_type = "privat company"
    print(daimler.company_type)
    daimler.add_product("passenger car")
    daimler.add_product("truck")
    print(daimler.show_products())
    print(str(daimler))
    print(repr(daimler))
    daimler.ipo_change("mari", '1234', False)
    print(daimler.ipo_check())
    dict_daimler = {'name': 'daimler', 'industry': 'automotive', 'company_type': 'public', 'profit': '1000000'}
    daimler2 = Company.from_dict(dict_daimler)
    print(str(daimler2))