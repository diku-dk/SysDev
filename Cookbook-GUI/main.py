# First import the needed Libraries for creating af QT Application using

from PyQt6 import QtWidgets, uic
import sys

# Create a class for your userInterface
# name of the class (here MyFirstAppUi) must be referenced in the super call


class MyFirstAppUi(QtWidgets.QMainWindow):
    # first define the constructor/initializer
    # __init__ is built-in so-called dunder (double underscore) method
    def __init__(self):
        super(MyFirstAppUi, self).__init__()   # MyFirstAppUi must be the same as the name of the class
        uic.loadUi('MyFirstAppGUI.ui', self)      # MyFirstAppGUI.ui is the name of your ui file

        # Now define the linking between all your GUI objects (widgets) and the
        # associated methods. E.g. what method (function) is called when the
        # 'OK' button is pressed.
        # Remember that you named the two buttons 'pushButtonOK' and 'pushButtonClear'

        self.pushButtonOK.clicked.connect(self.ok_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)

        # Don't forget this line! If you do forget, the GUI won't be visible!!

        self.show()

    def ok_button_pressed(self):
        # This is executed when the OK button is pressed
        # lets concatenate the values from alle the input fields and write
        # the result in the textEdit field we created:
        print("OK button pressed!")

        # get all the values from the input fields
        name = self.firstNameLineEdit.text()
        surname = self.surnameLineEdit.text()
        cpr_number = self.cPRNumberLineEdit.text()
        street = self.streetLineEdit.text()
        street_number = self.streetNumberLineEdit.text()
        ext = self.extLineEdit.text()
        zip_code = self.zipCodeLineEdit.text()
        city = self.cityLineEdit.text()

        address1 = " ".join((street, street_number, ext))
        address2 = " ".join((zip_code, city))

        # Build the output text

        output_text = "Name:\t"+name+" "+surname \
            + "\n\nCPR-Number:\t"+cpr_number \
            + "\n\nAddress:\t"+address1 \
            + "\n\n\t"+address2

        self.plainTextEdit.setPlainText(output_text)

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyFirstAppUi()
    app.exec()
