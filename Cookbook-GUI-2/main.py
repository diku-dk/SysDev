# This is the main executable - you can rename it to what you want

from MyFirstAppUi import *
import sys

if __name__ == '__main__':
    # create an empty patient list which we can pass to the MyFirstAppUi object (window)
    # a list in Python is mutable, so we can store updates made in the GUI in it.

    patient_list=[]

    # let us print the list
    output_text=""
    print("patient list before start:")
    for p in patient_list:
        output_text += str(p) + "\n"
    print(output_text)

    app = QtWidgets.QApplication(sys.argv)
    window = MyFirstAppUi(patient_list)
    app.exec()

    # If the main gui is exited (via file-> exit) we end here!
    # let us print the patients...
    output_text = ""
    print("patient list after exit:")
    for p in patient_list:
        print(type(p))
        output_text += str(p) + "\n"

    print(output_text)


