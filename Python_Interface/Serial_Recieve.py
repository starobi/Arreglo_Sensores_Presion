#Read from serial port

import serial

with serial.Serial("\\.\COM7", 57600) as ser:
    while True:
        line = ser.readline().decode('utf-8')
        print(line)

