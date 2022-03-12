# import date to store dates
from datetime import date


class Holidays:
    __holidays: list[date] = []   # a private attribute is prefixed by two underscores in Python

    def __init__(self=None):
        self.__holidays: list[date] = []    # a new object of the type Holidays is created as an empty list

    def add_holiday(self, holiday: date):    # public method to add a holiday to the list of holidays
        if holiday not in self.__holidays:   # if it is not already in the list
            self.__holidays.append(holiday)

    def remove_holiday(self, holiday: date):  # public method to add a holiday to the list of holidays
        if holiday in self.__holidays:        # if it is found in the list
            self.__holidays.remove(holiday)

    def contains_day(self, holiday: date):  # public method to tell if date is in the list of holidays
        return holiday in self.__holidays
    
    def __str__(self):
        output = f"Number of holidays: {len(self.__holidays)} \n"
        output = output + "The holidays are \n"
        output += ', '.join(h.strftime("%d/%m/%Y") for h in self.__holidays)
        return output
