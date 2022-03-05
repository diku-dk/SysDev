from datetime import date
from stdnum.dk import cpr


class Patient():
    """
    Class to hold Patient information
    """
    def __init__(self, first_name, surname, cpr_number,
                 street, street_number, street_ext, zip_code, city):
        self.first_name = first_name
        self.surname = surname
        self.cpr_number = cpr_number
        self.street = street
        self.street_number = street_number
        self.street_ext = street_ext
        self.zip_code = zip_code
        self.city =  city

    def __str__(self):
        name = f"{self.first_name} {self.surname}"
        address = f"{self.street} {self.street_number}, {self.street_ext}, {self.zip_code} {self.city}"
        age = f"{str(self.get_age())}"
        return f"Name: {name}, CPR-Number: {self.cpr_number}, Adress: {address}, Age: {age} "

    def get_age(self):
        """
        Method to return Patient Data calculated from today's date and the CPR-number
        """

        cpr_number_in = cpr.compact(self.cpr_number)
        today_date = date.today()
        birth_date = cpr.get_birth_date(cpr_number_in)
        age_date = today_date - birth_date
        return int(age_date.days/365.2425)