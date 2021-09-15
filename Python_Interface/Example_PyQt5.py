import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np

app = QApplication(sys.argv)
plotWidget = pg.plot(title="Sensor Samples")
x = np.arange(1000)
y = np.random.normal(size=(8, 999))
print(y)
for i in range(8):
    plotWidget.plot(x, y[i], pen=(i,8))
status = app.exec_()
#sys.exit(status)