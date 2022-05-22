from lxml import objectify
from Student import Student
from Course import Course


class Elements:
    @staticmethod
    def create_student(student_obj: Student):
        # define the name of the xml element
        student = objectify.Element("student")
        # add the attributes
        # note the decoupling of the XML tag names from the object attributes
        # (compared to the first example)
        student.fornavn = student_obj.get_first_name()
        student.efternavn = student_obj.get_last_name()
        student.cpr_nummer = student_obj.get_cpr_number()
        student.telefon = student_obj.get_phone()
        student.elpost = student_obj.get_email()
        return student

    @staticmethod
    def create_course(course_obj: Course):
        course = objectify.Element("kursus")
        course.fakultet = course_obj.get_faculty()
        course.kursusID = course_obj.get_course_id()
        course.kursusnavn = course_obj.get_course_name()
        # note that we haven't appended the student list - it will be handled elsewhere
        return course