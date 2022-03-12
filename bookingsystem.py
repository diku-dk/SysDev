from  Clinic import *
from Doctor import *
from Holidays import *
from datetime import date
from DataValidator import *


import sys
#from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QComboBox)


class BookingUI(QWidget):
    """
    A simpel one-window (QWidget) user interface to make a booking
    (or actually just search for a booking-date).
    Just do everything here - including defining hard-coded clinic, doctors and holidays
    A better way could be to instantiate a model with the list of clinics, doctors and holidays
    and then to refer to this model in the book_doctor_pressed method.
    But here we will just demonstrate how a exercise one can be extended with a GUI
    """

    # First create some holidays - check https://docs.python.org/3/library/datetime.html to
    # get and overview of how date datetime.date functions.
    d1: date = datetime.strptime("07/04/2022", "%d/%m/%Y")
    d2: date = datetime.strptime("08/04/2022", "%d/%m/%Y")
    d3: date = datetime.strptime("08/04/2022", "%d/%m/%Y")
    d4: date = datetime.strptime("09/04/2022", "%d/%m/%Y")
    d5: date = datetime.strptime("10/04/2022", "%d/%m/%Y")
    # now create an empty list of 'doctor holidays' and add a some days to the list
    doctor1_holidays = Holidays()
    doctor1_holidays.add_holiday(d1)
    doctor1_holidays.add_holiday(d2)
    doctor1_holidays.add_holiday(d4)

    # now create a doctor
    doctor1: Doctor = Doctor("A.S. Pirin", doctor1_holidays)

    # print doctor1's holidays
    print(f"{doctor1.name}'s holidays:")
    print(doctor1.list_holidays)

    # and another list of doctor-holidays and another doctor

    doctor2_holidays = Holidays()
    doctor2_holidays.add_holiday(d1)
    doctor2_holidays.add_holiday(d5)

    doctor2: Doctor = Doctor("P.A. Nodil", doctor2_holidays)

    # create a list of holidays for the a clinic

    clinic1_holidays = Holidays()
    clinic1_holidays.add_holiday(d1)
    clinic1_holidays.add_holiday(d2)
    clinic1_holidays.remove_holiday(d3)  # what happens here? can you explain
    clinic1_holidays.add_holiday(d4)

    # create a list of doctors for the clinic
    list_doctors = [doctor1, doctor2]

    # create a clinic

    clinic1: Clinic = Clinic("Nørrebrolægerne", "Nørrebrovej 27, 2100 Kbh N", clinic1_holidays, list_doctors)

    # print the list of holidays for the clinic:

    print(f"{clinic1.name}'s holidays:")
    print(clinic1.list_holidays)

    # Emulate some booking attempts and then ask for a booking date
    # I just check for the availability of a single doctor on a single clinic
    # We could also have iterated over alle doctors in the clinic and checked for their availability
    # The description of the task is a bit ambiguous.
    # Feel free to do make your own interpretation

    print("-" * 30)
    print("Attempting bookings")
    print("-" * 30)

    booking_date: date = datetime.strptime("07/04/2022", "%d/%m/%Y")
    print(f"Attempt: Booking {doctor1.name} on " + booking_date.strftime("%d/%m/%Y"))
    print(doctor1.check_available(clinic1, booking_date))

    booking_date: date = datetime.strptime("08/04/2022", "%d/%m/%Y")
    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date.strftime("%d/%m/%Y")))
    print(doctor1.check_available(clinic1, booking_date))

    booking_date: date = datetime.strptime("07/04/2022", "%d/%m/%Y")
    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date.strftime("%d/%m/%Y")))
    print(doctor1.check_available(clinic1, booking_date))

    # Now let us create at GUI
    # First let us make the constructor

    def __init__(self,parent=None):
        super().__init__(parent)

        self.cb = QComboBox()
        self.cb.addItems(h.name for h in self.list_doctors)# [self.doctor1.name, self.doctor2.name])
        self.date = QLabel('Date')
        self.result = QLabel('Result')
        self.dateEdit = QLineEdit()
        self.resultEdit = QTextEdit()
        self.button = QPushButton("Book")
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.date, 1, 0)
        self.grid.addWidget(self.dateEdit, 1, 1)
        self.grid.addWidget(self.button, 1, 2)
        self.grid.addWidget(self.result, 2, 0)
        self.grid.addWidget(self.resultEdit, 2, 1, 5, 1)
        self.grid.addWidget(self.cb,2,2)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Doctor Booking')
        # self.setStyleSheet("background-color: yellow;")   # uncomment this one for an ugly yellow background :-)
        self.button.clicked.connect(self.book_doctor_pressed)
        self.show()

    def book_doctor_pressed(self):
        print("Attempting booking")
        date_string = self.dateEdit.text()
        print("date inputted",date_string)

        # verify the input by the use of the DataValidator class
        # alert the user, if the input is faulty and clear the input field

        if not DataValidator.is_valid_date(date_string):
            # when it doesn't match the pattern (dd/mm/yyyy)
            # display a warning to the user
            self.resultEdit.append(f"{date_string} is not in the right format")

            # clear the input field and set focus on it, so it is ready for new input
            self.dateEdit.clear()
            self.dateEdit.setFocus()

        else:
            # we have a valid input - now check if the doctor is available
            print("Date is in the right format")
            date_to_check = datetime.strptime(date_string, "%d/%m/%Y")
            print("we check the date", str(date_to_check.strftime("%d/%m/%Y")))

            current_doctor_name=self.cb.currentText()
            print("current doctor: ", current_doctor_name)
            # find index of the doctor in the list of doctors.

            for index, item in enumerate(self.list_doctors):
                if item.name == current_doctor_name:
                    break

            # now we have the index

            print("index", index)

            availability_string = self.list_doctors[index].check_available(self.clinic1,date_to_check)
            self.resultEdit.append(availability_string)
            self.dateEdit.clear()
            self.dateEdit.setFocus()

if __name__ == '__main__':
    # We end here, if we run the python file from the command line - not if we include it
    # We just want to run the main method..
    # If we had made some classes, methods and functions that could be useful in other python projects
    # then the file could be imported without the main() method being run
    app = QApplication(sys.argv)
    bookingUI = BookingUI()
    sys.exit(app.exec())
