######NOTE######
#This program is executed when the bluetooth device in configured
#
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
            ser=serial.Serial(serial_COM, 9600)
            ser.write("EXITO ".encode())
            print("Exito en",serial_COM)
