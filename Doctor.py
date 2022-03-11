from Clinic import *
from Holidays import *
from datetime import date


class Doctor:

    def __init__(self,name, list_holidays: Holidays):
        self.name = name
        self.list_holidays = list_holidays

    def __str__(self):
        return f"Name: {self.name}, Holidays: {self.list_holidays}"

    def check_available(self, clinic: Clinic, booking_date: date):
        """
        Check's if a doctor is available on the given date at the given clinic
        If the booking_date is in the list of clinic holidays, then no doctors can be booked
        If the booking_date is in the doctors list of holidays, then the doctor can't be booked
        Otherwise the doctor is available

        :param clinic:  of type Clinic
        :param booking_date: of type date
        :return: string with information about availability
        """
        if clinic.list_holidays.contains_day(booking_date):
            return f"The clinic is closed on {booking_date} "
        elif self.list_holidays.contains_day(booking_date):
            return f"{self.name} is on holiday on {booking_date}"
        else:
            return f"{self.name} is available on {booking_date}"
