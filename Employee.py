from datetime import date
from stdnum.dk import cpr

class Employee:
    """
    employee class holds attributes and methods for an employee
    not the double underscore denoting this is a private attribute.
    An exception will be raised if your code tries to access it directly
    without the use of the setters and getters
    """

    def __init__(self, first_name: str, last_name: str, cpr_number: str, phone: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cpr_number = cpr_number
        self.__phone = phone
        self.__email = email

    def get_first_name(self): return self.__first_name

    def set_first_name(self, new_first_name): self.__first_name = new_first_name

    def get_last_name(self): return self.__last_name

    def set_last_name(self, new_last_name): self.__last_name = new_last_name

    def get_cpr_number(self): return self.__cpr_number

    def set_cpr_number(self, new_cpr): self.__cpr_number = new_cpr

    def get_phone(self): return self.__phone

    def set_phone(self, new_phone): self.__phone = new_phone

    def get_email(self): return self.__email

    def set_email(self, new_email): self.__email = new_email

    def get_age(self):
        __cpr_compact = cpr.compact(self.__cpr_number)
        __today_date = date.today()
        __birth_date = cpr.get_birth_date(__cpr_compact)
        __age_date = __today_date - __birth_date
        return int(__age_date.days / 365.2425)

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}, {self.__cpr_number}" \
               f", {self.__phone}, {self.__email}, age: {self.get_age()} years"

