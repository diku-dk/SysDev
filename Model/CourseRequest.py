from datetime import date, time
from CourseLocation import CourseLocation
from Course import Course


class CourseRequest:
    """
    Request for a course on a given date and time at a given location
    """

    request_id = 0

    def __init__(self, course: Course, course_date: date, course_time: time, course_location: CourseLocation):
        self.__course = course
        self.__course_date = course_date
        self.__course_time = course_time

        self.__course_location = course_location
        CourseRequest.request_id += 1

    def __str__(self):
        return f"Request: {str(self.request_id)}, course, {str(self.__course)}," \
               f" date: {str(self.__course_date)}, time: {str(self.__course_time)}," \
               f" location, {str(self.__course_location)}"

    def set_course_date(self, course_date: date): self.__course_date = course_date
    def set_course_time(self, course_time: time): self.__course_time = course_time
    def set_course_location(self, course_location: CourseLocation): self.__course_location = course_location
    