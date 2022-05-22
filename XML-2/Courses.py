from datetime import date
from stdnum.dk import cpr
from Course import Course


class Courses:
    """
    class to represent a list of Courses
    """

    def __init__(self):
        self.courses = []

    def append_course(self, course: Course):
        self.courses.append(course)

    def get_courses(self): return self.courses