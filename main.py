# Modify the program to perform minimal error checking:
# are strings only composed of non-number characters with a maximum length.
# CPR numbers and addresses will accept only formats valid in Denmark.
#
#
#
# Modify the program you created in task 4 to perform minimal error checking.
#
# Ensure that:
#
# A name can only consist of letters, not numbers.
# A name is at least a first- and last name.
# A CPR follows the format ddmmyy-XXXX.
# If the input patient data does not live up to the requirements, notify the user by printing a message.
#
# If the data fulfils the requirements, print out the patient data, age and assigned gender as in task 4.
# Consider using methods to perform your validation.
#
# Bonus requirement: Check that the CPR number is valid with Mod11.
# https://da.wikipedia.org/wiki/Modulus_11
# https://da.wikipedia.org/wiki/CPR-nummer#Kontrolciffer_(det_gamle_CPR-nummer)

from datetime import date
from stdnum.dk import cpr


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

    # keep looping until a valid name i entered
    while not valid:
        input_name = input("Name: ").strip()
        if 5 <= len(input_name) < max_length:
            # split the full name into multiple names - split default "absorbs" white spaces
            all_names = input_name.split()
            # We need to check if all names are valid
            # Start by ensuring there are at least two names in the list
            # all_names_valid is true if the length of the list is greater than 2 - otherwise false
            all_names_valid: bool = len(all_names) >= 2
            if all_names_valid:
                # now that we have split the input let us validate if all the names
                # consists purely of letters. Hmm - we don't handle names like o'Harry then
                # maybe you can refine it to do so?
                for sub_name in all_names:
                    # update the all_names_valid variable with the truth value of the next name
                    all_names_valid = all_names_valid and sub_name.isalpha()
            valid = all_names_valid
            if not valid:
                print("Not a valid name - please try again: ")
        else:
            print("Name too short")

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
        # street name must be at least two alphabetic characters long
        # allow for white spaces like in "Store Kongsgade"
        # more clever matching can be done wth regexp....
        street_name_stripped = street_name.replace(" ","")
        valid = len(street_name) >= 2 and street_name_stripped.isalpha()
        if not valid:
            print("street name must be at least two alphabetic characters long")
            print("and must consist of letters and spaces")
        # Street number must be a number
        valid = valid and street_number.isdigit()
        if not valid:
            print("Street number must be a number")
        # Zip code must be exactly 4 digits
        valid = valid and zip_code.isdigit() and len(zip_code) == 4
        if not valid:
            print("Zip code must be exactly 4 digits")
        # City must be at least two alphabetic characters long
        valid = (valid and len(city_name) >= 2 and city_name.isalpha())
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
        # check if the format is valid - use a function from "stdnum.dk.cpr"
        # note that the function requires the '-' to be removed first
        input_cpr = cpr.compact(input_cpr)
        valid = cpr.is_valid(input_cpr)
        # check if the cpr checksum is valid (modulus 11 rule) -
        # see the calculation done in https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/dk/cpr.py
        # You might want to remove this check if you in your future project want to be able to
        # enter bogus cpr numbers
        valid = valid and (cpr.checksum(input_cpr) == 0)

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
