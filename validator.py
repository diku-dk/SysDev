from stdnum.dk import cpr


def validate_name(input_name: str, max_length: int) -> bool:
    valid: bool = False
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
    return valid


def validate_street_name(street_name: str) -> bool:
    """
    function to validate street name
    :param street_name:
    :return: bool
    """
    # street name must be at least two alphabetic characters long
    # allow for white spaces like in "Store Kongensgade"
    # more clever matching can be done wth regexp....

    street_name_stripped = street_name.replace(" ", "")
    valid = len(street_name) >= 2 and street_name_stripped.isalpha()
    return valid


def validate_street_number(street_number: str) -> bool:
    """
    function to validate street number
    :param street_number:
    :return: bool
    """
    # street number must be digits

    return street_number.isdigit()


def validate_zip_code(zip_code: str) -> bool:
    """
    function to validate zip code
    :param zip_code:
    :return: bool
    """

    valid: bool = False
    # zipcode must be exactly four digits

    valid = zip_code.isdigit() and len(zip_code) == 4
    return valid


def validate_city_name(city_name: str) -> bool:
    """
    function to validate city name
    :param city_name:
    :return: bool
    """
    valid: bool = True
    # City must be at least two alphabetic characters long
    # allow for white spaces like in "København Ø"
    city_name_stripped = city_name.replace(" ", "")
    valid = valid and (len(city_name) >= 2)
    valid = valid and city_name_stripped.isalpha()

    return valid


def validate_cpr_number(input_cpr: str) -> bool:
    """
    function to validate cpr number
    :param input_cpr:
    :return: bool
    """
    valid: bool = False

    # check if the format is valid - use a function from "stdnum.dk.cpr"
    # note that the function requires the '-' to be removed first
    input_cpr = cpr.compact(input_cpr)
    valid = cpr.is_valid(input_cpr)
    # check if the cpr checksum is valid (modulus 11 rule) -
    # see the calculation done in https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/dk/cpr.py
    # You might want to remove this check if you in your future project want to be able to
    # enter bogus cpr numbers
    valid = valid and (cpr.checksum(input_cpr) == 0)
    return valid

