from lxml import etree, objectify
from io import BytesIO
from Courses import Courses
from Elements import Elements


class CoursesToXml:
    def __init__(self, courses: Courses):
        self.courses = courses

    def write_file(self):

        root = etree.Element("kurser")
        for course in self.courses.get_courses():
            course_element = Elements.create_course(course)
            root.append(course_element)
            # create studerende as sub element to the course element

            studerende =  objectify.SubElement(course_element,"studerende")

            # Add all the student items to the student element

            for student in course.get_students():
                # create the student xml element from the student object
                student_element = Elements.create_student(student)
                # append the studetn xml element to the students list element.
                studerende.append(student_element)

        # Do some cleanup
        # remove lxml annotation
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        # create the xml string
        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        # Write the xml string to a file
        try:
            with open("courses.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass
