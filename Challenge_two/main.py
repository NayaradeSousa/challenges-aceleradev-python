"""
Code refactoring for improve security, standard and good practices in case of company expansion.
"""
# This library is to make the Employee class abstract.
from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        return self.hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return 8

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, new_sale):
        self.__sales += new_sale

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department


# Instantiating
if __name__ == '__main__':
    rh = Department('rh', 123)
    sales = Department('sales', 456)
    maria = Manager(789, 'Maria', 3500)
    leandro = Manager(1011, 'Leandro', 5000)
    paulo = Seller(1213, 'Paulo', 4500)
    print("****************************************************************")
    print(f"Your department is {maria.get_departament()}")
    print(f"Your department is {leandro.get_departament()}")
    print(f"Your department is {paulo.get_departament()}")
    print("****************************************************************")
    print(f"{maria.name}, you must work {maria.get_hours()} hours by day.")
    print(f"{leandro.name}, you must work {leandro.get_hours()} hours by day.")
    print(f"{paulo.name}, you must work {paulo.get_hours()} hours by day.")
    print("****************************************************************")
    paulo.put_sales(900)
    paulo.put_sales(10)

    print(f"{maria.name} your salary is: {maria.salary} and your bonus this month is R${maria.calc_bonus()}")
    print(f"{leandro.name} your salary is: {leandro.salary} and your bonus this month is R${leandro.calc_bonus()}")
    print(f"{paulo.name} your salary is: {paulo.salary} and your bonus this month is R${paulo.calc_bonus()}")
    print("****************************************************************")
