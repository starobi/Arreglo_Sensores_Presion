#This program plots 8 the reading of 8 sensors according to the times lapsed in seconds

import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import serial
import time
import csv
from PyQt5.QtWidgets import *
from datetime import datetime

#Configuration Serial Port
serial=0 #Quiero Comunicación Serial?
if(serial==1):
    puerto = "COM8"
    baudrate = 57600
    ser = serial.Serial(puerto, baudrate)

#Initialization Sample variable
sample = []
sample.append([0])    #Time
sample.append([0])    #Sensor 1
sample.append([0])    #Sensor 2
sample.append([0])    #Sensor 3
sample.append([0])    #Sensor 4
sample.append([0])    #Sensor 5
sample.append([0])    #Sensor 6
sample.append([0])    #Sensor 7
sample.append([0])    #Sensor 8
count_sample=9

#Initialization Plot
app = pg.QtGui.QApplication([])
window=QWidget()
layout=QVBoxLayout()
plotWidget=pg.PlotWidget()
plotWidget.setTitle("Sensors")
plotWidget.addLegend() #Add legends of Sensores colors
plotWidget.setLabel(axis='left', text='Voltage', units=None, unitPrefix=None)
plotWidget.setLabel(axis='bottom', text='Time', units='s', unitPrefix=None)
layout.addWidget(plotWidget)
window.setLayout(layout)
window.show()

# w = pg.GraphicsLayoutWidget(title="Sensors", show=True,size=(1000,10000)) #GraphicLayout
# p = w.addPlot(title="Sensors' Samples") #PlotItem
# p.addLegend()
# p.setLabel(axis='left', text='Voltage', units=None, unitPrefix=None)
# p.setLabel(axis='bottom', text='Time', units='s', unitPrefix=None)

#Checar que hace graphiclayourwidget
#que hace addplot
#SE hace un item plot
sensor=[]
labels=['Sensor 1','Sensor 2','Sensor 3','Sensor 4','Sensor 5','Sensor 6','Sensor 7','Sensor 8']
#'''
sensor1=plotWidget.plot(pen=(1, 8), name=labels[0])
sensor2=plotWidget.plot(pen=(2, 8), name=labels[1])
sensor3=plotWidget.plot(pen=(3, 8), name=labels[2])
sensor4=plotWidget.plot(pen=(4, 8), name=labels[3])
sensor5=plotWidget.plot(pen=(5, 8), name=labels[4])
sensor6=plotWidget.plot(pen=(6, 8), name=labels[5])
sensor7=plotWidget.plot(pen=(7, 8), name=labels[6])
sensor8=plotWidget.plot(pen=(8, 8), name=labels[7])

#CSV file initialization
date=datetime.now()
file_name="{}-{}-{}_{}_{}hrs_Test.csv".format(date.year,date.month,date.day,date.hour,date.minute)
csv_file = open(file_name,'w',newline='',encoding="utf-8")
csv_writer = csv.writer(csv_file,delimiter=',') #In an English OS works with ',' but in Spanisch, works with 'tab'
csv_writer.writerow(['Time','Sensor 1','Sensor 2','Sensor 3','Sensor 4','Sensor 5','Sensor 6','Sensor 7','Sensor 8'])

count_sample=9
frames=50

def Update():
    global sensor, sample,count_sample,frames,initial_time
    try:
        if(serial==1):
            line = ser.readline().decode('utf-8')
            if line == '\n':
                sensor1.setData(sample[0], sample[1])
                sensor2.setData(sample[0], sample[2])
                sensor3.setData(sample[0], sample[3])
                sensor4.setData(sample[0], sample[4])
                sensor5.setData(sample[0], sample[5])
                sensor6.setData(sample[0], sample[6])
                sensor7.setData(sample[0], sample[7])
                sensor8.setData(sample[0], sample[8])
                count_sample = 0
                actual_time=round(time.time()-initial_time,3)
                sample[0].append(actual_time)
                if len(sample[0]) > frames:
                    for i in range(0,9):
                        sample[i].pop(0)
            if 0 < count_sample <= 8:
                sample[count_sample].append(int(line))
            count_sample = count_sample + 1
        else:
            actual_time = round(time.time() - initial_time,3)
            sample[0].append(actual_time)
            numbers = [10, 20, 30, 40, 50, 60, 70, 80]
            for x in range(1, 9):
                sample[x].append(numbers[x - 1])
            sensor1.setData(sample[0], sample[1])
            sensor2.setData(sample[0], sample[2])
            sensor3.setData(sample[0], sample[3])
            sensor4.setData(sample[0], sample[4])
            sensor5.setData(sample[0], sample[5])
            sensor6.setData(sample[0], sample[6])
            sensor7.setData(sample[0], sample[7])
            sensor8.setData(sample[0], sample[8])
            csv_writer.writerow([sample[0][-1],sample[1][-1],sample[2][-1],sample[3][-1],sample[4][-1],sample[5][-1],sample[6][-1],sample[7][-1],sample[8][-1]])

    except:
        pass



    #Actualizamos los datos y refrescamos la gráfica.
    pg.QtGui.QGuiApplication.processEvents()

initial_time=time.time()
while ((time.time()-initial_time)<=10): Update() #Actualizamos lo rápido que podamos.
csv_file.close()
app.exec_()