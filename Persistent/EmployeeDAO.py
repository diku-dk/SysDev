from abc import abstractmethod
from Persistent.DAO import DAO
from Model.Employee import Employee
from typing import List  # needed to be able to declare list type

from Persistent.EmpSearchType import EmpSearchType


class EmployeeDAO(DAO):

    @abstractmethod
    def insert_employee(self, emp: Employee):
        pass

    @abstractmethod
    def update_employee(self, emp: Employee) -> bool:
        pass

    @abstractmethod
    def delete_employee(self, emp: Employee) -> bool:
        pass

    @abstractmethod
    def find_employee_by_property(self, search_type: EmpSearchType, value: object) -> List[Employee]:
        pass

    @abstractmethod
    def find_all(self) -> List[Employee]:
        pass

