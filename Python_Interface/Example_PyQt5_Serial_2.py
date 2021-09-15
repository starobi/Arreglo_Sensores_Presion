import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import serial

#Configuration Serial Port
puerto = "COM7"
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
labels=['Sensor 1','Sensor 2','Sensor 3','Sensor 4','Sensor 5','Sensor 6','Sensor 7','Sensor 8']
count_sample=9

#Initialization Plot
app = QApplication(sys.argv)
plotWidget = pg.plot(title="Sensor Samples")
plotWidget.addLegend()
for i in range(8):
    plotWidget.plot(sample[0], sample[i + 1], pen=(i + 1, 8), name=labels[i])

frames=7


def Update():
    global sample, plotWidget,count_sample,ser,frames,labels
    # Leemos la nueva línea
    try:
        line = ser.readline().decode('utf-8')
        if line == '\n':
            count_sample = 0
            if(len(sample[0]) >= frames):
                '''
                #sample[0].pop(0)
                for i in range(9):
                    plotWidget.removeItem(sample[i][-frames:])
                for i in range(8):
                    #sample[i+1].pop(0)
                    plotWidget.plot(sample[0], sample[i + 1], pen=(i + 1, 8))
                #print([sample[0],sample[1]])
                '''
            else:
                for i in range(8):
                    plotWidget.plot(sample[0], sample[i + 1], pen=(i + 1, 8))
            sample[0].append(sample[0][-1] + 1)
        if 0 < count_sample < 9:
            sample[count_sample].append(int(line))
        count_sample = count_sample + 1
    except:
        pass
    #Actualizamos los datos y refrescamos la gráfica.
    app.processEvents()
while True: Update() #Actualizamos todo lo rápido que podamos.
status = app.exec_()

#sys.exit(status)