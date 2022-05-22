from lxml import etree
from XmlToObject import XmlToObject
from dummyObjects import dummyObjects
from ObjectToXml import ObjectToXml

if __name__ == "__main__":
    # Create some nested objects: a courseList with som dummy courses-each with its own list of students
    print("Creating som test objects")
    courseList = dummyObjects.create()
    # Create a prettified xml string
    print("Creating and xml file from the test objects")
    pretty_xml=ObjectToXml(courseList).to_xmlstring()
    # write the xml file
    with open("courses.xml", "wb") as f:
        f.write(pretty_xml)

    # now let us read the xml file

    print("Read the xml file")
    object_from_xml=XmlToObject('courses.xml').to_object()

    # here we take the top most object (aka the root element) it is referenced by .courses

    courses1=object_from_xml.courses

    print("\nIterating over the objects and printing them:")

    for c in iter(courses1.course):
        print("-"*30)
        print("Course: "+', '.join([c.faculty, c.courseID, c.courseName]))
        print("List of students:")
        for s in iter(c.students.student):
            print("\t"+', '.join([s.first_name, s.last_name, s.cpr_number, s.phone, s.email, ]))


    print("\nChecking documents:\n")

    dtd = etree.DTD(open('courses.dtd'))
    print("check generated courses.xml",dtd.validate(etree.parse('courses.xml')))
    print("check invalid courses_invalid.xml", dtd.validate(etree.parse('courses_invalid.xml')))




