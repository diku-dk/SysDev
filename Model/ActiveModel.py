from Model.Employee import Employee


class ActiveModel(object):
    """
    This is the system model
    """

    list_employee: list = []
    current_employee: Employee = None

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
