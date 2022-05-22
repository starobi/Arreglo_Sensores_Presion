from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from TestWindow_file import TestWindow
from CalibrationWindow_file import CalibrationWindow
from BluetoothWindow_file import BluetoothWindow

class MainMenu(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Main Menu")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        ###########Set Layout#############
        self.hLayout=QHBoxLayout()
        self.vLayout=QVBoxLayout()

        btnCal=QPushButton("Calibration")
        btnBlue=QPushButton("Bluetooth Configuration")
        btnTests=QPushButton("Tests")
        btnTests.clicked.connect(self.windowTest)
        btnCal.clicked.connect(self.windowCalibration)
        btnBlue.clicked.connect(self.windowBluetooth)
        label=QLabel("Sensor Pressure Array Interface")
        label.setAlignment(Qt.AlignCenter)
        self.vLayout.addStretch()
        self.vLayout.addWidget(label)
        self.vLayout.addLayout(self.hLayout)
        self.hLayout.addWidget(btnBlue)
        self.hLayout.addWidget(btnCal)
        self.vLayout.addWidget(btnTests)
        self.vLayout.addStretch()

        self.setLayout(self.vLayout)

        self.show()


    def windowCalibration(self):
        self.windowT=CalibrationWindow()

    def windowTest(self):
        self.windowT=TestWindow()

    def windowBluetooth(self):
        self.windowT=BluetoothWindow()

def main():
    App=QApplication([])
    window = MainMenu()
    App.exec_()

if __name__=='__main__':
    main()