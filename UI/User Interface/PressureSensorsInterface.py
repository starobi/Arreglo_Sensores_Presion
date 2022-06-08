from PyQt5.QtWidgets import * #Required for User Interface
from PyQt5.QtCore import * #Required for User Interface
import pyqtgraph as pg #Required to plot Data
import serial #Required to use Serial Communication
import csv  #Required to creave CSV files
from datetime import datetime #Get the date and time
import time #Get the exact time
from infi.devicemanager import DeviceManager #Explore information of the computers devices
import os   #Create Directories and get the current direction

###########CONFIGURATION VARIABLES#########################
SerialActivated=1 #This variable works to use Serial Information to plot or not. When Developing is useful
testTime=30 #This is the time that the test will last
framesTestWindow=50 #This is the number of values desplayed on the plot before scrolling.
baudRate=230400
###########################################################

class MainMenu(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Main Menu")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        ###########Set Layout###########    ##
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
        self.close()
    def windowTest(self):
        self.windowT=TestWindow()
        self.close()
    def windowBluetooth(self):
        self.windowT=BluetoothWindow()
        self.close()
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Test")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        # Configuration Serial Port
        self.serial = SerialActivated  # Serial Activated/Desactivated just for debugging
        if (self.serial == 1):
            try:
                bluetooth_com_name_file = open("Bluetooth_COM.txt", mode='r', encoding="utf-8")
            except:
                QMessageBox.information(self, "Information", "No COM port configuration was found. Please verify bluetooth connection first")
                self.close()
                return

            puerto = bluetooth_com_name_file.read()
            bluetooth_com_name_file.close()
            try:
                self.ser = serial.Serial(puerto, baudRate)
            except:
                QMessageBox.information(self, "Information", "The Bluetooth connection had an error")
                self.close()
                return

        # Initialization Sample variable
        self.sample = [] #Array of Arrays with all Sensors samples
        self.sample.append([0])  # Time
        self.sample.append([0])  # Sensor 1
        self.sample.append([0])  # Sensor 2
        self.sample.append([0])  # Sensor 3
        self.sample.append([0])  # Sensor 4
        self.sample.append([0])  # Sensor 5
        self.sample.append([0])  # Sensor 6
        self.sample.append([0])  # Sensor 7
        self.sample.append([0])  # Sensor 8
        self.count_sample = 9

        # Initialization Plot
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setTitle("Sensors Test 1")
        self.test="Test1"
        self.plotWidget.addLegend()  # Add legends of Sensores colors
        self.plotWidget.setLabel(axis='left', text='Voltage', units=None, unitPrefix=None)
        self.plotWidget.setLabel(axis='bottom', text='Time', units='s', unitPrefix=None)
        self.setCentralWidget(self.plotWidget)

        self.sensor = [] #Array for DataPlotItem for each sensor
        labels = ['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7', 'Sensor 8']
        self.sensor1 = self.plotWidget.plot(pen=(1, 8), name=labels[0])
        self.sensor2 = self.plotWidget.plot(pen=(2, 8), name=labels[1])
        self.sensor3 = self.plotWidget.plot(pen=(3, 8), name=labels[2])
        self.sensor4 = self.plotWidget.plot(pen=(4, 8), name=labels[3])
        self.sensor5 = self.plotWidget.plot(pen=(5, 8), name=labels[4])
        self.sensor6 = self.plotWidget.plot(pen=(6, 8), name=labels[5])
        self.sensor7 = self.plotWidget.plot(pen=(7, 8), name=labels[6])
        self.sensor8 = self.plotWidget.plot(pen=(8, 8), name=labels[7])

        #Tool Bar
        tb=self.addToolBar("My Toolbar")
        test1b=QAction("Test 1",self)
        tb.addAction(test1b)
        test2b=QAction("Test 2",self)
        tb.addAction(test2b)
        test3b=QAction("Test 3",self)
        tb.addAction(test3b)
        tb.actionTriggered.connect(self.btnFunc)
        startButton=QPushButton("Start Test")
        tb.addWidget(startButton)
        startButton.clicked.connect(self.startButton)

        self.show()

    def btnFunc(self,btn):
        if btn.text()=="Test 1":
            self.plotWidget.setTitle("Sensors Test 1")
            self.test="Test1"
        elif btn.text() =="Test 2":
            self.plotWidget.setTitle("Sensors Test 2")
            self.test = "Test2"
        elif btn.text() =="Test 3":
            self.plotWidget.setTitle("Sensors Test 3")
            self.test = "Test3"
        self.plotReset()

    def startButton(self):
        self.plotReset()
        self.savecsv=True
        cwd = os.path.dirname(os.path.abspath(__file__))
        testsPath = os.path.join(cwd, "Tests")
        if not os.path.exists(testsPath):
            os.mkdir(testsPath)
        os.chdir(testsPath)
        date = datetime.now()
        file_name= QFileDialog.getSaveFileName(self, "Confirm Name and Location", "{}-{}-{}_{}_{}hrs_{}".format(date.year, date.month, date.day, date.hour, date.minute,self.test), "*.csv")
        if file_name[0]== "":
            return
        try:
            if self.csv_file.closed == True:
                self.csv_file.close()
        except NameError:
            pass
        except AttributeError:
            pass
        self.csv_file = open(file_name[0], 'w', newline='', encoding="utf-8")
        self.csv_writer = csv.writer(self.csv_file,delimiter=',')
        self.csv_writer.writerow(
            ['Time', 'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7', 'Sensor 8'])

        self.plotArray=[[],[],[],[],[],[],[],[],[]]
        self.sample_check=[]
        self.frames = framesTestWindow
        self.initial_time = time.time()
        while ((time.time() - self.initial_time) <= testTime): self.Update()  # Actualizamos lo rápido que podamos.
        if self.savecsv==True:
            for x in range(len(self.sample[1])-1):
                self.csv_writer.writerow(
                    [self.sample[0][x], self.sample[1][x], self.sample[2][x], self.sample[3][x],
                     self.sample[4][x], self.sample[5][x], self.sample[6][x], self.sample[7][x],
                     self.sample[8][x]])
            self.csv_file.close()
        self.savecsv=False

    def Update(self):
        try:
            if (self.serial == 1): #If Serial is Active
                line = self.ser.readline().decode('utf-8')
                if line == '\n':
                    if len(self.sample_check) == 8:
                        count_sample=1
                        for x in self.sample_check:
                            self.plotArray[count_sample].append(x)
                            self.sample[count_sample].append(x)
                            count_sample=count_sample+1
                        self.actual_time = round(time.time() - self.initial_time, 3)
                        self.sample[0].append(self.actual_time)
                        self.plotArray[0].append(self.actual_time)
                        self.sensor1.setData(self.plotArray[0], self.plotArray[1])
                        self.sensor2.setData(self.plotArray[0], self.plotArray[2])
                        self.sensor3.setData(self.plotArray[0], self.plotArray[3])
                        self.sensor4.setData(self.plotArray[0], self.plotArray[4])
                        self.sensor5.setData(self.plotArray[0], self.plotArray[5])
                        self.sensor6.setData(self.plotArray[0], self.plotArray[6])
                        self.sensor7.setData(self.plotArray[0], self.plotArray[7])
                        self.sensor8.setData(self.plotArray[0], self.plotArray[8])
                        pg.QtGui.QGuiApplication.processEvents() # Actualizamos los datos y refrescamos la gráfica.
                        if len(self.plotArray[0]) > self.frames:
                            for i in range(0, 9):
                                self.plotArray[i].pop(0)
                    self.sample_check=[]
                else:
                    self.sample_check.append(int(line))
            else: #Done if Serial is not active, just for debug
                self.actual_time = round(time.time() - self.initial_time, 3)
                self.sample[0].append(self.actual_time)
                numbers = [10, 20, 30, 40, 50, 60, 70, 80]
                for x in range(1, 9):
                    self.sample[x].append(numbers[x - 1])
                self.sensor1.setData(self.sample[0], self.sample[1])
                self.sensor2.setData(self.sample[0], self.sample[2])
                self.sensor3.setData(self.sample[0], self.sample[3])
                self.sensor4.setData(self.sample[0], self.sample[4])
                self.sensor5.setData(self.sample[0], self.sample[5])
                self.sensor6.setData(self.sample[0], self.sample[6])
                self.sensor7.setData(self.sample[0], self.sample[7])
                self.sensor8.setData(self.sample[0], self.sample[8])
                self.csv_writer.writerow([self.sample[0][-1], self.sample[1][-1], self.sample[2][-1], self.sample[3][-1], self.sample[4][-1], self.sample[5][-1],self.sample[6][-1], self.sample[7][-1], self.sample[8][-1]])
        except:
            pass

    def plotReset(self):
        self.sensor1.setData()
        self.sensor2.setData()
        self.sensor3.setData()
        self.sensor4.setData()
        self.sensor5.setData()
        self.sensor6.setData()
        self.sensor7.setData()
        self.sensor8.setData()
        self.sample[0].clear()
        self.sample[1].clear()
        self.sample[2].clear()
        self.sample[3].clear()
        self.sample[4].clear()
        self.sample[5].clear()
        self.sample[6].clear()
        self.sample[7].clear()
        self.sample[8].clear()

    def closeEvent(self, event):
        try:
            self.ser.close()
        except:
            pass
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.windowMain = MainMenu()

class BluetoothWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Bluetooth Options")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        self.nameBluetoothQline = QLineEdit(self)
        btnSaveDeviceName = QPushButton("Save Device Name")
        btnSaveDeviceName.clicked.connect(self.saveNameDevice)
        btnVerifyConnection = QPushButton("Verify Connection")
        btnVerifyConnection.clicked.connect(self.verifyConnection)
        hLayout.addWidget(self.nameBluetoothQline)
        hLayout.addWidget(btnSaveDeviceName)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(btnVerifyConnection)
        self.setLayout(vLayout)
        try:
            bluetooth_name_file=open("Bluetooth_device_name.txt",mode='r',encoding="utf-8")
        except:
            bluetooth_name_file=open("Bluetooth_device_name.txt",mode='x',encoding="utf-8")
            bluetooth_name_file =open("Bluetooth_device_name.txt", mode='r', encoding="utf-8")
        self.bluetooth_device_name=bluetooth_name_file.readline()
        bluetooth_name_file.close()
        self.nameBluetoothQline.setText(self.bluetooth_device_name)
        self.show()

    def verifyConnection(self):
        ####### Name Bluetooth Device######
        bluetooth_device_name = self.bluetooth_device_name
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
                        try:
                            bluetooth_com_name_file = open("Bluetooth_COM.txt", mode='w', encoding="utf-8")
                        except:
                            bluetooth_com_name_file = open("Bluetooth_COM.txt", mode='x', encoding="utf-8")
                            bluetooth_com_name_file = open("Bluetooth_COM.txt", mode='w', encoding="utf-8")
                        bluetooth_com_name_file.write(serial_COM)
                        bluetooth_com_name_file.close()
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
            mbox = QMessageBox.information(self, "Not linked device", "Bluetooth device not linked to the computer, link bluetooth device first or verify the device name")

    def saveNameDevice(self):
        self.bluetooth_device_name=self.nameBluetoothQline.text()
        bluetooth_name_file = open("Bluetooth_device_name.txt", mode='w', encoding="utf-8")
        bluetooth_name_file.write(self.bluetooth_device_name)
        bluetooth_name_file.close()
        QMessageBox.information(self, "Information", "Name saved succefully")

    def closeEvent(self, event):
        self.windowMain=MainMenu()

class CalibrationWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Calibration")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        self.show()

    def closeEvent(self, event):
        self.windowMain=MainMenu()


def main():
    App=QApplication([])
    window = MainMenu()
    App.exec_()

if __name__=='__main__':
    main()