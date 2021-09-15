
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial
puerto = "COM7"
baudrate = 57600
ser = serial.Serial(puerto, baudrate)
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Grafica en tiempo real")
p = win.addPlot(title="Grafica tiempo real")
curva = p.plot(pen='y')
p.setRange(yRange=[0, 1024])
dataX = [] # Array's para guardar los datos
dataY = []
lastY = 0
def Update():
    global curva, dataX, dataY, lastY,nuevoDato
    # Leemos la nueva línea
    line = ser.readline()
    try:
        nuevoDato = int(line.decode('utf-8'))
    except:
        pass
    #Agregamos los datos al array
    dataX.append(lastY)
    dataY.append(nuevoDato)
    lastY = lastY + 1
    # Limitamos a mostrar solo 300 muestras
    if len(dataX) > 300:
        dataX = dataX[:-1]
        dataY = dataY[:-1]
    #Actualizamos los datos y refrescamos la gráfica.
    curva.setData(dataX, dataY)
    QtGui.QApplication.processEvents()
while True: Update() #Actualizamos todo lo rápido que podamos.
pg.QtGui.QApplication.exec_()