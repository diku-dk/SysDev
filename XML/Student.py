from datetime import date
from stdnum.dk import cpr


class Student:
    """
    student class holds attributes and methods for a student
    For this example we won't be using private attributes
    """

    def __init__(self, first_name: str, last_name: str, cpr_number: str, phone: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        try:
            self.cpr_number = cpr_number
            cpr.get_birth_date(cpr.compact(self.cpr_number))

        except:
            raise TypeError("Bad cpr_number")
        self.phone = phone
        self.email = email

    def get_first_name(self): return self.first_name

    def set_first_name(self, new_first_name): self.first_name = new_first_name

    def get_last_name(self): return self.last_name

    def set_last_name(self, new_last_name): self.last_name = new_last_name

    def get_cpr_number(self): return self.cpr_number

    def set_cpr_number(self, new_cpr): self.cpr_number = new_cpr

    def get_phone(self): return self.phone

    def set_phone(self, new_phone): self.phone = new_phone

    def get_email(self): return self.email

    def set_email(self, new_email): self.email = new_email

    def get_age(self):
        cpr_compact = cpr.compact(self.cpr_number)
        today_date = date.today()
        birth_date = cpr.get_birth_date(cpr_compact)
        age_date = today_date - birth_date
        return int(age_date.days / 365.2425)

    def __str__(self):
        return f"first_name:{self.first_name},last_name:{self.last_name}, cpr:{self.cpr_number}" \
               f", phone:{self.phone}, mail:{self.email}, age: {self.get_age()}"
