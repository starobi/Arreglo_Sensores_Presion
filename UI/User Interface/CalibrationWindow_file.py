from PyQt5.QtWidgets import *

class CalibrationWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Calibration")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.show()