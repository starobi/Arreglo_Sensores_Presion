import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading as threading
import numpy as np

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

plt.style.use('fivethirtyeight')

'''
def getData():
    count_sample = 9  # Identificador iniciador Sensor
    with serial.Serial("\\.\COM7", 57600) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8')
                if line == '\n':
                    count_sample = 0
                    sample[0].append(sample[0][-1]+1)
                    #print(sample)
                if 0 < count_sample < 9:
                    sample[count_sample].append(int(line))
                count_sample = count_sample + 1
            except:
                pass
'''
'''
def animate(i):
    plt.cla()
    plt.plot(sample[0], sample[1], label='Sensor 1')
    plt.plot(sample[0], sample[2], label='Sensor 2')
    plt.plot(sample[0], sample[3], label='Sensor 3')
    plt.plot(sample[0], sample[4], label='Sensor 4')
    plt.plot(sample[0], sample[5], label='Sensor 5')
    plt.plot(sample[0], sample[6], label='Sensor 6')
    plt.plot(sample[0], sample[7], label='Sensor 7')
    plt.plot(sample[0], sample[8], label='Sensor 8')
    print('Holaa')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.ylim(0, 200)
'''

#dataCollector = threading.Thread(target = getData)

#plot_ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)


count=0
count_sample = 9  # Identificador iniciador Sensor
with serial.Serial("\\.\COM7", 57600) as ser:
    while count<4:
        try:
            line = ser.readline().decode('utf-8')
            if line == '\n':
                count_sample = 0
                sample[0].append(sample[0][-1] + 1)
                count=count+1
                # print(sample)
            if 0 < count_sample < 9:
                sample[count_sample].append(int(line))
            count_sample = count_sample + 1
        except:
            pass
plt.ylim(0,1024)
plt.plot(sample[0], sample[1], label='Sensor 1')
plt.show()

#dataCollector.start()
#ataCollector.join()


#https://www.youtube.com/watch?v=Ercd-Ip5PfQ&t=1s Referencia

