from PyQt6 import QtWidgets, uic
from Model.ActiveSystem import Employee
from Model.ActiveSystem import ActiveSystem


class SearchEmployeeGUI(QtWidgets.QWidget):

    search_employee: Employee = None

    def __init__(self):
        super(SearchEmployeeGUI, self).__init__()
        uic.loadUi('View/SearchEmployee.ui', self)

        self.pushButtonSearch.clicked.connect(self.search_button_pressed)
        self.pushButtonOK.clicked.connect(self.ok_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)
        self.pushButtonCancel.clicked.connect(self.cancel_button_pressed)

        self.show()

    def search_button_pressed(self):
        # This is executed when the Search button is pressed
        # lets find the person in the list if persons by
        # looking up the cpr-number

        search_cpr = self.cPRNumberLineEdit.text()
        print("Search cpr:", search_cpr)

        for e in ActiveSystem.get_employee_list():
            print(e.get_cpr_number())
            if e.get_cpr_number() == search_cpr:
                self.firstNameLineEdit.setText(e.get_first_name())
                self.lastNameLineEdit.setText(e.get_last_name())
                self.cPRNumberLineEdit_2.setText(e.get_cpr_number())
                self.phoneLineEdit.setText(e.get_phone())
                self.emailLineEdit.setText(e.get_email())
                # assign the internal search employee to the one found
                self.search_employee = e
                print("search_employee: ", self.search_employee)
                break

    def ok_button_pressed(self):
        # This is executed when the OK button is pressed
        # Let us set the current person to be the one we looked up

        print("OK button pressed!")

        print("search_employee at OK: ", self.search_employee)

        if self.search_employee is not None:
            ActiveSystem.set_current_employee(self.search_employee)

        # You could create an alert message here stating if no employee was found

        print("-" * 30 + "\nThe Model has the following employees")
        for e in ActiveSystem.get_employee_list():
            print(e)

        print("-" * 30 + "\nModel has the active employee ")
        print(ActiveSystem.get_current_employee())

        # If started from the stacked widget we want to return to the default window:
        if type(self.parent()) == QtWidgets.QStackedWidget:
            self.parent().setCurrentIndex(0)

        self.close()

    def clear_button_pressed(self):
        # This method is used in order to clear all input fields.
        # A simple, but naive approach will be to call
        # .clear() for all input fields, e.g. self.firstNameLineEdit.clear()
        # however this will require that we maintain the method if we add
        # more fields. A better approach would probably be to find all fields of type
        # LineEdit and clear them!
        # But first present the user with a warning message by using QMessagebox

        print('Clear button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Clear fields", "All input fields will be cleared")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            self.search_employee = None
            # Find all fields of type QLineEdit
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()
        else:
            print("No!")

    def cancel_button_pressed(self):

        print('Cancel button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Exit form?", "Are you done entering employees?")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")

            print("-" * 30 + "\nThe Model has the following employees")
            for e in ActiveSystem.get_employee_list():
                print(e)

            print("-" * 30 + "\nModel has the active employee ")
            print(ActiveSystem.get_current_employee())

            print(type(self.parent()))
            if type(self.parent()) == QtWidgets.QStackedWidget:
                self.parent().setCurrentIndex(0)
            self.close()  # This will close the widget

        else:
            print("No!")
