from Model.Employee import Employee
from Model.Course import Course
from Persistent.MySQLEmployeeDAO import MySQLEmployeeDAO

class ActiveSystem(object):
    """
    This is the system model
    """

    list_employee: [Employee] =  []
    list_courses: [Course] = []
    current_employee: Employee = None
    dao: MySQLEmployeeDAO = None

    @classmethod
    def add_employee(cls, e):
        cls.list_employee.append(e)

    @classmethod
    def set_current_employee(cls, c):
        cls.current_employee = c

    @classmethod
    def get_current_employee(cls):
        return cls.current_employee

    @classmethod
    def get_employee_list(cls):
        return cls.list_employee

    @classmethod
    def set_dao(cls, dao):
        cls.dao = dao

    @classmethod
    def get_dao(cls):
        return cls.dao
