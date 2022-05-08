import sys
from PyQt6 import QtWidgets
from Model.Employee import Employee
from Controller.NewEmployeeGUI import NewEmployeeGUI
from Controller.SearchEmployeeGUI import SearchEmployeeGUI
from Model.ActiveModel import ActiveModel
from Controller.MainWindowGUI import MainWindowGUI


# This is the main file that launches the application
# A couple of employees are created and manipulated before the GUI is started

def main():

    emp1 = Employee("Anders", "Andersen", "100181-0101", "+4512121212", "anders.andersen@company.com")
    ActiveModel.add_employee(emp1)
    print(emp1)
    print("changing phone number")
    emp1.set_phone("+4533333333")
    print(emp1)

    emp2 = Employee("Bente", "Bentsen", "020282-0202", "+4566666666", "bente.bentsen@company.com")
    ActiveModel.add_employee(emp2)
    print(emp2)
    print("Marrying Anders and Bente")
    emp2.set_last_name("Andersen")
    emp2.set_email("bente.andersen@company.com")
    print(emp2)

    print(f"The cpr-number of {emp2.get_first_name()} {emp2.get_last_name()} is {emp2.get_cpr_number()}")
    print(f"{emp2.get_first_name()} is {emp2.get_age()} years old")

    print("-" * 30 + "\nThe Model has the following employees")
    for e in ActiveModel.get_employee_list():
        print(e)

    print("-" * 30 + "\nModel has the active employee ")
    print(ActiveModel.get_current_employee())
    print("Starting the GUI")



    app = QtWidgets.QApplication(sys.argv)
    main_window=MainWindowGUI()
    app.exec()


if __name__ == '__main__':
    main()
