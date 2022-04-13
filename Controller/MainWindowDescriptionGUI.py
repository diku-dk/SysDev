from PyQt6 import QtWidgets, uic


class MainWindowDescriptionGUI(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindowDescriptionGUI, self).__init__()
        uic.loadUi('View/MainWindowDescription.ui', self)

        self.show()

