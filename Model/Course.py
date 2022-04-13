from CourseResponsible import CourseResponsible
from Model.Employee import Employee

# Let us introduce the use of an enumeration class for the course language :-)
from Language import Language


class Course:
    """
    a University course
    """
    __course_responsible: CourseResponsible = None
    __teacher = None

    def __init__(self, course_id: str, course_name: str, course_language: Language):

        self.__course_id: str = course_id
        self.__course_name: str = course_name
        self.__course_language: Language = course_language

    def __str__(self):

        __return_value: str = f"id: {self.__course_id}, {self.__course_name}, " \
                              f"course responsible: {self.__course_responsible}, " \
                              f"teacher: {self.__course_responsible},"

    def set_course_responsible(self, responsible: CourseResponsible):
        self.__course_responsible = responsible

    def get_course_responsible(self):
        return self.__course_responsible

    def set_course_language(self, language: Language):
        self.__course_language = language

    def get_course_language(self):
        return self.__course_language

    def set_teacher(self, teacher: Employee):
        self.__teacher = teacher

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name
