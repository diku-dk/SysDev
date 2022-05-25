import pytest
from Model.Employee import Employee

@pytest.fixture
def my_emp():
    return Employee("Anders", "Andersen", "100181-0101", "+4512121212", "anders.andersen@company.com")


def test_get_age(my_emp):

    assert my_emp.get_age() == 41


