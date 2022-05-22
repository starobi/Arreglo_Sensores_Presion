#Description

#Make Configuration interchangable

from PyQt5.QtWidgets import *
import pyqtgraph as pg
import serial
import time
from datetime import datetime
import csv
import os


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Test")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        # Configuration Serial Port
        self.serial = 0  # Serial Activated/Desactivated just for debugging
        if (self.serial == 1):
            try:
                bluetooth_com_name_file = open("Bluetooth_COM.txt", mode='r', encoding="utf-8")
            except:
                QMessageBox.information(self, "Information", "No COM port configuration was found. Please verify bluetooth connection first")
                return

            puerto = bluetooth_com_name_file.read()
            bluetooth_com_name_file.close()
            baudrate = 57600
            self.ser = serial.Serial(puerto, baudrate)

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
        cwd = os.getcwd()
        testsPath = os.path.join(cwd, "Tests")
        if not os.path.exists(testsPath):
            os.mkdir(testsPath)
        os.chdir(testsPath)
        date = datetime.now()
        file_name= QFileDialog.getSaveFileName(self, "Confirm Name and Location", "Tests\{}-{}-{}_{}_{}hrs_{}".format(date.year, date.month, date.day, date.hour, date.minute,self.test), "*.csv")
        if file_name[0]== "":
            return
        csv_file = open(file_name[0], 'w', newline='', encoding="utf-8")
        self.csv_writer = csv.writer(csv_file,delimiter=',')  # In an English OS works with ',' but in Spanisch, works with 'tab'
        self.csv_writer.writerow(
            ['Time', 'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7', 'Sensor 8'])

        self.count_sample = 9
        self.frames = 50  # Improve this to the acutal sample rate
        self.initial_time = time.time()
        while ((time.time() - self.initial_time) <= 10): self.Update()  # Actualizamos lo rápido que podamos.
        csv_file.close()

    def Update(self):
        try:
            if (self.serial == 1):
                line = self.ser.readline().decode('utf-8')
                if line == '\n':
                    self.sensor1.setData(self.sample[0], self.sample[1])
                    self.sensor2.setData(self.sample[0], self.sample[2])
                    self.sensor3.setData(self.sample[0], self.sample[3])
                    self.sensor4.setData(self.sample[0], self.sample[4])
                    self.sensor5.setData(self.sample[0], self.sample[5])
                    self.sensor6.setData(self.sample[0], self.sample[6])
                    self.sensor7.setData(self.sample[0], self.sample[7])
                    self.sensor8.setData(self.sample[0], self.sample[8])
                    self.count_sample = 0
                    self.actual_time = round(time.time() - self.initial_time, 3)
                    self.sample[0].append(self.actual_time)
                    if len(self.sample[0]) > self.frames:
                        for i in range(0, 9):
                            self.sample[i].pop(0)
                if 0 < self.count_sample <= 8:
                    self.sample[self.count_sample].append(int(line))
                self.count_sample = self.count_sample + 1
            else:
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

        # Actualizamos los datos y refrescamos la gráfica.
        pg.QtGui.QGuiApplication.processEvents()

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


