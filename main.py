import sys
from PyQt6 import QtWidgets
from Model.Employee import Employee
from Model.ActiveSystem import ActiveSystem
from Controller.MainWindowGUI import MainWindowGUI
from Persistent.MySQLEmployeeDAO import MySQLEmployeeDAO

# This is the main file that launches the application
# A couple of employees are created and manipulated before the GUI is started


def main():

    # create a DAO (database access object)
    employeeDAO = MySQLEmployeeDAO()

    ActiveSystem.set_dao(employeeDAO)
    # set up the database (drop the existing table!)
    employeeDAO.setup()
    # start a connection to the database
    # connect to the database
    employeeDAO.connect()
    # list all entries (it should be empty)
    employeeDAO.find_all()

    # add som test persons
    emp1 = Employee("Anders", "Andersen", "100181-0101", "+4512121212", "anders.andersen@company.com")
    ActiveSystem.add_employee(emp1)
    employeeDAO.insert_employee(emp1)

    print(emp1)
    print("changing phone number")
    emp1.set_phone("+4533333333")
    print(emp1)
    # make the change persistent in the database
    employeeDAO.update_employee(emp1)

    emp2 = Employee("Bente", "Bentsen", "020282-0202", "+4566666666", "bente.bentsen@company.com")
    ActiveSystem.add_employee(emp2)
    employeeDAO.insert_employee(emp2)

    print(emp2)
    print("Marrying Anders and Bente")
    emp2.set_last_name("Andersen")
    emp2.set_email("bente.andersen@company.com")
    employeeDAO.update_employee(emp2)
    print(emp2)

    print(f"The cpr-number of {emp2.get_first_name()} {emp2.get_last_name()} is {emp2.get_cpr_number()}")
    print(f"{emp2.get_first_name()} is {emp2.get_age()} years old")

    print("-" * 30 + "\nThe Model has the following employees")
    for e in ActiveSystem.get_employee_list():
        print(e)

    print("-" * 30 + "\nModel has the active employee ")
    print(ActiveSystem.get_current_employee())


    # manipulate the two test employees inserted in the setup() method
    peter = Employee('Peter', 'Svendsen', '121299-4321', '11111111', 'peter.sv@andeby.dk')
    jakob = Employee('Jakob', 'Larson', '100469-0231', '88888888', 'jakob.larsson@dvconsulting.dk')

    employeeDAO.delete_employee(peter)
    employeeDAO.delete_employee(jakob)

    # insert jakob again (before the phone was 654321, now it is 88888888
    employeeDAO.insert_employee(jakob)
    employeeDAO.find_all()

    jakob.set_phone('123456')
    employeeDAO.update_employee(jakob)
    employeeDAO.find_all()

    jakob.set_phone('654321')
    jakob.set_last_name('Andersen')
    jakob.set_email('jakob@andersen.dk')
    employeeDAO.update_employee(jakob)
    employeeDAO.find_all()

    peter = Employee('Peter', 'Svendsen', '121299-4321', '11111111', 'peter.sv@andeby.dk')
    employeeDAO.insert_employee(peter)
    allemp= employeeDAO.find_all()
    for emp in allemp:
        print(emp)

    # There is now a discrepancy between the active and the persistent model - can you find it?

    print("Starting the GUI")



    app = QtWidgets.QApplication(sys.argv)
    main_window=MainWindowGUI()
    app.exec()

    print("The GUI is closed - printing the current employee table")
    employeeDAO.find_all()

    allemp = employeeDAO.find_all()
    for emp in allemp:
        print(emp)

    print("closing the database")
    print("take a look at the current state via MySQL workbench")

    employeeDAO.close()
    print("goodbye")

if __name__ == '__main__':
    main()
