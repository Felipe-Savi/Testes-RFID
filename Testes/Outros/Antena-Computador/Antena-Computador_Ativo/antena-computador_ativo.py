'''
Mostra valores da antena
'''

import serial

ser = serial.Serial('COM3')

while True:
    if ser.in_waiting:
        bs = ser.read(ser.in_waiting)

        bs = '/'.join([f'{b:x}' for b in bs])
        print(bs)

