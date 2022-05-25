from PyQt6 import QtWidgets, uic
from Model.Employee import Employee
from Model.ActiveSystem import ActiveSystem


class NewEmployeeGUI(QtWidgets.QWidget):
    def __init__(self):
        super(NewEmployeeGUI, self).__init__()      
        uic.loadUi('View/NewEmployee.ui', self)
        print("NewEmployeeGUI called")
        print("-" * 30 + "\nGUI: We have the following employees in the active model")
        for e in ActiveSystem.get_employee_list():
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

            ActiveSystem.add_employee(employee)
            empdao=ActiveSystem.get_dao()
            empdao.insert_employee(employee)

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

        print("-" * 30 + "\nThe Model has the following employees")
        for e in ActiveSystem.get_employee_list():
            print(e)

        print("-" * 30 + "\nModel has the active employee ")
        print(ActiveSystem.get_current_employee())

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
            print(type(self.parent()))
            if type(self.parent()) == QtWidgets.QStackedWidget:
                self.parent().setCurrentIndex(0)
            self.close()  # This will close Widget

        else:
            print("No!")
