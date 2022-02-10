# Create a program that registers patient data:
# Name and CPR number and address, and determines the patient age and his/her gender
# 1. Create a new Python Project in Pycharm
# 2. In the main method, create variables to store patient data. Name, CPR and Address.
#    Consider what data types should each variable be bound to.
# 3. Extend the program so the user can input Patient data: Name, CPR and Address.
# 4. Extend the program to output the age of the patient.
# 5. Determine the assigned gender of the patient
# 6. Print out the information to the console

from datetime import date

from stdnum.exceptions import *
from stdnum.util import clean


# inspired by https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/dk/cpr.py

def compact(number):
    """Convert the number to the minimal representation. This strips the
    number of any valid separators and removes surrounding whitespace."""
    return clean(number, ' -').strip()


def get_birthdate(number):
    """Split the date parts from the number and return the birthdate."""
    # remove the potential dash from the cpr number
    number = compact(number)
    day = int(number[0:2])
    month = int(number[2:4])
    year = int(number[4:6])
    if number[6] in '5678' and year >= 58:
        year += 1800
    elif number[6] in '0123' or (number[6] in '49' and year >= 37):
        year += 1900
    else:
        year += 2000
    try:
        return date(year, month, day)
    except ValueError:
        raise InvalidComponent('The number does not contain valid birth date information.')


def gender(number: int) -> str:
    # remove the potential dash from the cpr number
    number = compact(number)
    # Grab the last digit of the cpr - string,
    # convert it to an integer
    last_digit_in_cpr: int = int(number[9])

    if last_digit_in_cpr % 2 == 0:
        return "female"
    else:
        return "male"


if __name__ == '__main__':
    name: str
    cpr: str
    address: str

    print("Please enter the patients name, cpr-number and address.")
    name = input("Name: ")
    cpr = input("CPR: ")
    address = input("Address:")
    print("The patients name: " + name + ", cpr: " + cpr + ", address: " + address)
    today = date.today()
    birth_date = get_birthdate(cpr)
    print("Patients birth date: "+ str(birth_date))
    print("Today is: " + str(today))
    age = today - birth_date
    print("Patients age is "+str(int(age.days/365.2425)) + " years")
    print("The patient is a "+gender(cpr))
