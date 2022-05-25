from Model.Employee import Employee
from Model.Language import Language


class Teacher(Employee):
    """
    represents a Teacher at a university
    """

    language: Language = None
    language_list: list(Language) = []

    def __init__(self, language_list):
        self.language_list.append(language_list)

    def add_language(self, new_language):
        self.language_list.append(Language(new_language))
