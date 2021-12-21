import sys
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
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

    def windowTest(self):
        self.windowT=TestWindow()
        self.close()

    def windowCalibration(self):
        self.windowT=CalibrationWindow()
        self.close()

    def windowBluetooth(self):
        self.windowT=BluetoothWindow()
        self.close()



class TestWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Test")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.show()

    def closeEvent(self, event):
        self.windowMain=MainWindow()

class BluetoothWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Bluetooth")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.show()

    def closeEvent(self, event):
        self.windowMain=MainWindow()

class CalibrationWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Calibration")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.show()

    def closeEvent(self, event):
        self.windowMain=MainWindow()

def main():
    App=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()