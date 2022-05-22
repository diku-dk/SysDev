class Course:
    """
    Naive class to represent a course at a faculty (and its list of students)
    """

    def __init__(self, faculty: str, course_id: str, course_name: str, students: list):
        self.faculty = faculty
        self.courseID = course_id
        self.courseName = course_name
        self.students = students

    def get_faculty(self): return self.faculty
    def set_faculty(self, new_faculty): self.faculty = new_faculty
    def get_course_id(self): return self.courseID
    def set_course_id(self, new_course_id): self.courseID = new_course_id
    def get_course_name(self): return self.courseName
    def set_course_name(self, new_course_name): self.courseName = new_course_name
    def get_students(self): return self.students
    def set_students(self, new_students): self.students = new_students

