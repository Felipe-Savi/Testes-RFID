'''
Computador envia ASCII para Arduino, que incrementa e retorna
'''

import serial
import time

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=8,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

while True:
    enviar = input('Digite o que deve ser enviado: ')
    ser.write(bytes(enviar, 'ascii'))

    time.sleep(0.1)

    if ser.in_waiting:
        print(f'Recebido: {ser.read(ser.in_waiting)}')
    else:
        print(f'Não chegou nada')



