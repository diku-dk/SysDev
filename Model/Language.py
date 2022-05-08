from enum import Enum, unique


@unique
class Language(Enum):
    """
    Class for enumerating course languages
    """

    DANISH = 1
    ENGLISH = 2
