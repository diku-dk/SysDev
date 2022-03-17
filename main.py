import sys
from PyQt6 import QtWidgets
from Employee import Employee
from NewEmployeeGUI import NewEmployeeGUI


def main():

    list_employees = []
    emp1 = Employee("Anders", "Andersen", "100181-0101", "+4512121212", "anders.andersen@company.com")
    list_employees.append(emp1)
    print(emp1)
    print("changing phone number")
    emp1.set_phone("+4533333333")
    print(emp1)
    emp2 = Employee("Bente", "Bentsen", "020282-0202", "+4566666666", "bente.bentsen@company.com")
    list_employees.append(emp2)
    print(emp2)
    print("Marrying Anders and Bente")
    emp2.set_last_name("Andersen")
    emp2.set_email("bente.andersen@company.com")
    print(emp2)

    print(f"The cpr-number of {emp2.get_first_name()} {emp2.get_last_name()} is {emp2.get_cpr_number()}")
    print(f"{emp2.get_first_name()} is {emp2.get_age()} years old")

    print("-"*30+"\nWe now have the following employees")
    for e in list_employees:
        print(e)

    app = QtWidgets.QApplication(sys.argv)
    NewEmployeeGUI(list_employees)
    app.exec()

    print("-" * 30 + "\nWe now have the following employees")
    for e in list_employees:
        print(e)


if __name__ == '__main__':
    main()
