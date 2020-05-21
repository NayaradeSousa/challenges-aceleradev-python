"""
Code refactoring for improve security, standard and good practices in case of company expansion.
################################ Challenge Aceleradev Python ##########################################################
- Protect the Employee class from being instantiated directly.
- Make the implementation of the methods of the Employee class mandatory, implement them if necessary.
- Protect the department attribute of the Manager class so that it is accessed only through the get_department method.
- Correct the methods so that the inheritance works correctly.
- Protect the sales attribute of the Seller class so that it is not directly accessed, create a method called
get_sales to return the value of the attribute and put_sales to add values to that attribute, remembering that
sales are cumulative
- Implement the get_department method that returns the department name and set_department that changes the
department name for the Manager and Seller classes
- Standardize an 8-hour workload for all employees.
The calculation of the Seller's calc_bonus method must be calculated by the total sales times 0.15
#######################################################################################################################
"""
# This library is to make the Employee class abstract.
from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


# Abstract class - this prevent directly access
class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department
        self.hours = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__department.name

    def set_departament(self, new_depart):
        self.__department.name = new_depart


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return self.hours


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_hours(self):
        return self.hours

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, new_sale):
        self.__sales += new_sale


# Instantiating
if __name__ == '__main__':
    rh = Department('rh', 123)
    sales = Department('sales', 456)
    maria = Manager(789, 'Maria', 3500)
    leandro = Manager(1011, 'Leandro', 5000)
    paulo = Seller(1213, 'Paulo', 4500)
    print("****************************************************************")
    print(f"Your department is {maria.get_departament()}.")
    print(f"Your department is {leandro.get_departament()}.")
    print(f"Your department is {paulo.get_departament()}.")
    print("****************************************************************")
    print(f"{maria.name}, you must work {maria.get_hours()} hours by day.")
    print(f"{leandro.name}, you must work {leandro.get_hours()} hours by day.")
    print(f"{paulo.name}, you must work {paulo.get_hours()} hours by day.")
    print("****************************************************************")
    paulo.put_sales(900)
    paulo.put_sales(10)

    print(f"{maria.name} your salary is: {maria.salary} and your bonus this month is R${maria.calc_bonus()}.")
    print(f"{leandro.name} your salary is: {leandro.salary} and your bonus this month is R${leandro.calc_bonus()}.")
    print(f"{paulo.name} your salary is: {paulo.salary} and your bonus this month is R${paulo.calc_bonus()}.")
    print("****************************************************************")
