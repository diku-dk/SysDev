from Model.CourseResponsible import CourseResponsible
from Model.Employee import Employee

# Let us introduce the use of an enumeration class for the course language :-)
from Model.Language import Language
from Model.Student import Student
from Model.Teacher import Teacher


class Course:
    """
    a University course
    """
    __course_responsible: CourseResponsible = None
    __teacher: Teacher = None
    __student_list: [Student] = []

    def __init__(self,  course_id: str, faculty: str, course_name: str, course_language: Language):

        self.__faculty: str = faculty
        self.__course_id: str = course_id
        self.__course_name: str = course_name
        self.__course_language: Language = course_language

    def __str__(self):

        __return_value: str = f"id: {self.__course_id}, faculty: {self.__faculty}, course name:{self.__course_name}, " \
                              f"course responsible: {self.__course_responsible}, " \
                              f"teacher: {self.__course_responsible}," \
                              f"language: {self.__course_language}"

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

    def get_teacher(self):
        return  self.__teacher

    def set_course_id(self, course_id: str):
        self.__course_id= course_id

    def get_course_id(self):
        return self.__course_id

    def set_course_name(self, course_name: str):
        self.__course_name= course_name

    def get_course_name(self):
        return self.__course_name


    def set_faculty(self, faculty: str):
        self.__faculty = faculty

    def get_faculty(self):
        return self.__faculty


    def add_student(self, student: Student) -> bool:

        # check if student is already in the list
        # otherwise add student
        for s in self.__student_list:
            if s.get_cpr_number() == student.get_cpr_number():
                print("Student with that cpr number is already in the list")
                return False
        self.__student_list.append(self,student)
        return True

    def remove_student(self, student: Student) -> bool:
        for s in self.__student_list:
            if s.get_cpr_number == student.get_cpr_number():
                self.__student_list.remove(s)
                print("Student removed")
                return True
        # student not found
        return False

    def get_students(self):
        return self.__student_list
