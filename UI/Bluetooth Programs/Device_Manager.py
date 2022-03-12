######NOTE######
#This program is executed when the bluetooth device in configured
#This is the process of Validation of BLuetooth Conection
#
from infi.devicemanager import DeviceManager
import serial
####### Name Bluetooth Device######
bluetooth_device_name="=HOLA"
###################################

dm = DeviceManager()
dm.root.rescan()
devices = dm.all_devices
bluetooth_device=[]
serial_over_bluetooth_devices= []
serial_COM=""
for device in devices:
    if bluetooth_device_name in device.__str__():
        bluetooth_device.append(device)
    if "Standard Serial over Bluetooth link" in device.__str__():
        serial_over_bluetooth_devices.append(device)
if bluetooth_device.__len__() == 1:
    bluetooth_id=(bluetooth_device[0].hardware_ids[0][-12:])
    for device in serial_over_bluetooth_devices:
        if bluetooth_id in device.instance_id:
            serial_COM="COM"+device.friendly_name[-2]
            try:
                ser=serial.Serial(serial_COM, 9600)
            except:
                print(
"""The Bluetooth Port is not connected

Solutions:
*Verify that the Measuring Device is turned on and linked to the computer
*Erase the bluetooth device from the computer and link it again""")
            else:
                ser.write("bluetooth_test ".encode())
                print("Bluetooth working Correclty")
else:
    print("Bluetooth device not linked to the computer link bluetooth device first")
