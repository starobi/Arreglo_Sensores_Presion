import sys
#from PyQt5.QtGui import *
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg


class MainWindow(QWidget):
    def __init__(self):
        super().__init__() #It initialize the init of the Base Class QWidget
        self.setWindowTitle("Main Menu")
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        layout=QVBoxLayout()
        print(type(layout))
        datax = [1, 2, 3, 4, 5]
        datay = [2, 4, 2, 3, 5]
        Pwidget=pg.PlotWidget()
        print(type(Pwidget.plot(datax,datay)))
        #Pwidget.set
        #self.setLayout(layout)
        # self.setCentralWidget(Pwidget)
        layout.addWidget(Pwidget)
        self.setLayout(layout)

        self.show()


def main():
    APP=QApplication(sys.argv)
    window=MainWindow()
    APP.exec_()

if __name__ == '__main__':
    main()