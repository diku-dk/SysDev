from PyQt6 import QtWidgets, uic
from Employee import Employee


class NewEmployeeGUI(QtWidgets.QWidget):
    def __init__(self, list_employee_before: list):       #
        super(NewEmployeeGUI, self).__init__()      # MyFirstAppUi must be the same as the name of the class
        uic.loadUi('UI/NewEmployee.ui', self)      # MyFirstAppGUI.ui is the name of your ui file


        self.list_employee = list_employee_before

        print("-" * 30 + "\nStarting the GUI we have the following employees")
        for e in self.list_employee:
            print(e)

        self.pushButtonOK.clicked.connect(self.ok_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)
        self.pushButtonCancel.clicked.connect(self.cancel_button_pressed)

        self.show()

    def ok_button_pressed(self):
        # This is executed when the OK button is pressed
        # lets concatenate the values from alle the input fields and write
        # the result in the textEdit field we created:

        print("OK button pressed!")

        # get all the values from the input fields
        name = self.firstNameLineEdit.text()
        last_name = self.lastNameLineEdit.text()
        cpr_number = self.cPRNumberLineEdit.text()
        phone = self.phoneLineEdit.text()
        email = self.emailLineEdit.text()

        # Try to create an employee object with the above parameters
        try:
            employee = Employee(name, last_name, cpr_number, phone, email)

            print("Employee:", employee)

            # Let us update the list off employees and print it

            self.list_employee.append(employee)

        except Exception as e:
            print("Arrgh! Something went wrong!!", e)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Input error")
            msg.setText("Badly formatted input!")
            msg.setDetailedText(str(e))
            msg.exec()
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()

        print("-" * 30 + "\nWe now have the following employees")
        for e in self.list_employee:
            print(e)

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
            self.close()  # This will close the main GUI
        else:
            print("No!")
