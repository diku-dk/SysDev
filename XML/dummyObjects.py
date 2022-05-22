from Student import Student
from Course import Course
from Courses import Courses


class dummyObjects:

    @staticmethod
    def create():
        studentList1 = []
        studentList2 = []
        student1 = Student("Anders", "Andersen", "100181-0101", "+4512121212", "anders.andersen@company.com")
        studentList1.append(student1)
        student2 = Student("Bente", "Bentsen", "020282-0202", "+4566666666", "bente.bentsen@company.com")
        studentList1.append(student2)
        student3 = Student("Calle", "Callesen", "020283-0203", "+4566666213", "calle.callesen@company.com")
        studentList2.append(student3)
        student4 = Student("Ditte", "Dittesen", "020280-0242", "+4534666213", "ditte.dittesen@company.com")
        studentList2.append(student4)

        courseA = Course("DTU", "R080T", "Teknik for læger", studentList1)
        courseB = Course("KU", "D0CT3R", "Sundhed for ingeniører", studentList2)

        courseList = Courses()
        courseList.append_course(courseA)
        courseList.append_course(courseB)

        return courseList
