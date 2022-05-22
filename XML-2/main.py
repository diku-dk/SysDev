from lxml import etree, objectify


from dummyObjects import dummyObjects
from CoursesToXml import CoursesToXml
from XmlToCourses import XmlToCourses


if __name__ == "__main__":
    # Create some nested objects: a courseList with som dummy courses-each with its own list of students
    print("Creating som test objects")
    courseList = dummyObjects.create()
    print("Write the courselist to courses.xml")
    CoursesToXml(courseList).write_file()

    print("Reading the xml file")

    courseList=XmlToCourses('courses.xml').parseXML()

    print("courseList is of type:", type(courseList))

    courses=courseList.get_courses()

    print("courses is of type:",type(courses))

    print(courses)

    print("Iterating over the objects and printing them:")

    for c in courses:
        print("-" * 30)
        print()
        print("Course: ", c.get_faculty(), c.get_course_id(), c.get_course_name())
        print("List of students:")
        for s in c.get_students():
            print("\t", s.get_first_name(),",", s.get_last_name(),",", s.get_cpr_number(),",", s.get_phone(),",", s.get_email())

    print("\nChecking documents:\n")

    dtd = etree.DTD(open('courses.dtd'))
    print("check generated courses.xml",dtd.validate(etree.parse('courses.xml')))
    print("check invalid courses_invalid.xml", dtd.validate(etree.parse('courses_invalid.xml')))




