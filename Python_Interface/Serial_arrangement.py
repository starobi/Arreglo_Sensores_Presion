#Read of serial port and arrangement of data according to it's sensor

import serial
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

count_sample=9 #Identificador iniciador Sensor

with serial.Serial("\\.\COM7", 57600) as ser:
    while True:
        try:
            line=ser.readline().decode('utf-8')
            if line == '\n':
                count_sample=0
                sample[0].append(sample[0][-1]+1)
                print (sample)
            if 0< count_sample <9:
                sample[count_sample].append(int(line))
            count_sample=count_sample+1
        except:
            pass
