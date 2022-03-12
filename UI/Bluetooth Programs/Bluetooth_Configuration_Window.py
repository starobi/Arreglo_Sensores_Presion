import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from infi.devicemanager import DeviceManager
import serial


class BluetoothWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Bluetooth Options")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.vLayout = QVBoxLayout()
        btnVerifyConnection = QPushButton("Verify Connection")
        btnVerifyConnection.clicked.connect(self.verifyConnection)
        self.vLayout.addWidget(btnVerifyConnection)
        self.setLayout(self.vLayout)
        self.show()

    def verifyConnection(self):
        ####### Name Bluetooth Device######
        bluetooth_device_name = "=HOLA"
        ###################################

        dm = DeviceManager()
        dm.root.rescan()
        devices = dm.all_devices
        bluetooth_device = []
        serial_over_bluetooth_devices = []
        serial_COM = ""
        for device in devices:
            if bluetooth_device_name in device.__str__():
                bluetooth_device.append(device)
            if "Standard Serial over Bluetooth link" in device.__str__():
                serial_over_bluetooth_devices.append(device)
        if bluetooth_device.__len__() == 1:
            bluetooth_id = (bluetooth_device[0].hardware_ids[0][-12:])
            for device in serial_over_bluetooth_devices:
                if bluetooth_id in device.instance_id:
                    serial_COM = "COM" + device.friendly_name[-2]
                    try:
                        ser = serial.Serial(serial_COM, 9600)
                    except:
                        mbox = QMessageBox.information(self, "Failed Connection",
"""Bluetooth port connection could not be established

Solutions:
*Verify that the Measuring Device is turned on and linked to the computer
*Erase the bluetooth device from the computer and link it again""")
                    else:
                        ser.write("bluetooth_test ".encode())
                        mbox = QMessageBox.information(self, "", "Bluetooth working Correclty")
        else:
            mbox = QMessageBox.information(self, "Not linked device", "Bluetooth device not linked to the computer, link bluetooth device first")


def main():
    App=QApplication(sys.argv)
    window = BluetoothWindow()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()