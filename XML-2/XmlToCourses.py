from lxml import objectify
from Student import Student
from Course import Course
from Courses import Courses


class XmlToCourses:

    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> Courses:
        """"""
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        root = objectify.fromstring(xml)

        # Return attributes in element node as a dictionary
        attrib = root.attrib

        courseList = Courses()

        # Loop over all courses in the xml file
        for course in root.getchildren():
            # loop over all students for each course
            students: [Student] = []
            for studerende in course.studerende.getchildren():

                # create student object from the text attributes
                fornavn= studerende.fornavn.text
                print(fornavn)
                efternavn = studerende.efternavn.text
                print(efternavn)
                cpr_nummer = studerende.cpr_nummer.text
                print(cpr_nummer)
                telefon = studerende.telefon.text
                print(telefon)
                elpost = studerende.elpost.text
                print(elpost)
                student= Student(fornavn, efternavn, cpr_nummer, telefon, elpost)
                # append the student object to the list of students
                students.append(student)

            # create course object with the attributes and the list of students
            course_obj = Course(course.fakultet,course.kursusID,course.kursusnavn,students)
            # add the course to the course list:

            courseList.append_course(course_obj)

        return courseList