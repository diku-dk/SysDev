from Employee import Employee


class AdminPersonal(Employee):
    """
    Represents an employee at an educational institution
    AdminPersonal will have a set of course request to process, and can accept a course request or deny it

    """
    def __init__(self, institute_id, course_requests: list):
        self.__instituteID = institute_id
        self.__course_requests = course_requests
