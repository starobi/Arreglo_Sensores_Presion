#Example of Matplotlib

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading as threading#Que es Threading
import numpy as np #Que es NP

fig = plt.figure(figsize=(10,8))

sample = []
sample.append([0.0])    #Time
sample.append([0.0])    #Sensor 1

def getData(out_data):
    with serial.Serial("\\.\COM7", 57600) as ser:
        while True:
            try:
                count=1
                line = ser.readline().decode('utf-8')
                out_data[1].append(int(line))
                if len(sample[1]) <= 5:
                    out_data[1].pop(0)
            except:
                pass

dataCollector = threading.Thread(target = getData, args = (sample))
dataCollector.start()

def update_line(num, hl,data):
    dx = np.array(range(leng(data[0])))
    dy = np.array(data[1])
    hl.set_data(dx,dy)
    return hl,

hl, = plt.plot(sample[0],sample[1])
plt.xlim(0,200)
plt.ylim(0,1024)

#line_ani = animation.FuncAnimation(Que figura?,que funcion se va a ejecutar?, fargs=(hl, sample),interval=cada cuando?ms, blit=False)
line_ani = animation.FuncAnimation(fig,update_line, fargs=(hl, sample),interval=50, blit=False)

plt.show()

dataCollector.join()

#https://www.youtube.com/watch?v=Ercd-Ip5PfQ&t=1s Referencia

