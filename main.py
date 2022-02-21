# Write unit tests for last week exercise
# Rewrite last week's exercise in order be able to do unit test
# by splitting the input functions in an input part and a validator part.
# The unit tests can then be done on the validator functions.
#
# The validator functions have been put into a separate python file
# that we need to import in order to use them

from datetime import date
from stdnum.dk import cpr

# import our validator functions
import validator


def get_name() -> str:
    """
    A function to read the name from user input
    We assume all names are at least two characters long
    and a patient must have at least two names, separated by at least one space
    so the input must be at least 5 characters long (incl. space).
    We support a maximum of 80 characters in the full name
    :return: full name of the person
    """
    max_length: int = 80
    valid: bool = False
    #  list to hold all the names
    all_names: [] = []
    # keep looping until a valid name is entered
    while not valid:
        input_name = input("Name: ").strip()
        # use our validator function to validate the name
        valid = validator.validate_name(input_name, max_length)
        if not valid:
            print("Not a valid name - please try again: ")
    full_name = " ".join(all_names)
    return full_name


def get_address() -> str:
    """
    Function to read and validate address from user input
    :return: full address
    """
    valid: bool = False
    street_name: str = ""
    street_number: str = ""
    zip_code: str = ""
    city_name: str = ""

    print("Please enter the patients address.")
    while not valid:
        # let us get the 4 minimum needed strings from the user
        # we don't handle extensions like 3.tv
        street_name = input("Street: ").strip()
        street_number = input("Street number: ").strip()
        zip_code = input("Postal code: ").strip()
        city_name = input("City: ").strip()
        # Check street name
        valid = validator.validate_street_name(street_name)
        if not valid:
            print("street name must be at least two alphabetic characters long")
            print("and must consist of letters and spaces")
        valid = valid and validator.validate_street_number(street_number)
        if not valid:
            print("Street number must be a number")
        valid = valid and validator.validate_zip_code(zip_code)
        if not valid:
            print("Zip code must be exactly 4 digits")
        valid = valid and validator.validate_city_name(city_name)
        if not valid:
            print("City must be at least two alphabetic characters long")
        if not valid:
            print("Not a valid Address. Please try again: ")

    full_address: str = street_name + " " + street_number + ", " + zip_code + " " + city_name
    return full_address


def get_cpr() -> str:
    """
    get_cpr reads the cpr number from input. The cpr-number can contain a '-'
    the function returns the cpr number in compact form (without the '-')
    """
    valid: bool = False
    input_cpr = ""

    while not valid:
        input_cpr = input("Please enter the patients cpr: ").strip()
        valid = validator.validate_cpr_number(input_cpr)

    return input_cpr


def gender(number: str) -> str:
    # remove the potential dash from the cpr number
    number = cpr.compact(number)
    # Grab the last digit of the cpr - string,
    # convert it to an integer
    last_digit_in_cpr: int = int(number[9])
    if last_digit_in_cpr % 2 == 0:
        return "female"
    else:
        return "male"


def age(cpr_number_in: str) -> int:
    cpr_number_in = cpr.compact(cpr_number_in)
    today_date = date.today()
    birth_date = cpr.get_birth_date(cpr_number_in)
    age_date = today_date - birth_date
    return int(age_date.days/365.2425)


if __name__ == '__main__':

    name: str
    cpr_number: str
    address: str

    print("Please enter the patients name, cpr-number and address.")
    name = get_name()
    cpr_number = get_cpr()
    address = get_address()
    # use cpr.format to print the cpr-number with '-'
    print("name", name)
    print("cpr", cpr.format(cpr_number))
    print("address", address)
    print("The patients name: " + name + ", cpr: " + cpr.format(cpr_number) + ", address: " + address)

    birth_date_retrieved = cpr.get_birth_date(cpr.compact(cpr_number))
    print("Patients birth date: " + str(birth_date_retrieved))
    print("Patients age is " + str(age(cpr_number)) + " years")
    print("The patient is a " + gender(cpr_number))
