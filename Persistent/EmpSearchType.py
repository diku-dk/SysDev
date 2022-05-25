from enum import unique, Enum


@unique
class EmpSearchType(Enum):
    """
    Class for enumerating course languages
    """

    CPR = 1
    FIRSTNAME = 2
    LASTNAME = 3
    PHONE = 4
    EMAIL = 5