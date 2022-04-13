from Model.Employee import Employee
from Model.Language import Language


class Teacher(Employee):
    """
    represents an instructor at a university
    """

    language = Language()
    language_list = [language]

    def __init__(self, language_list):
        self.language_list.append(language_list)

    def add_language(self, new_language):
        self.language_list.append(Language(new_language))
