'''
Teste com o RX e TX do conversor em curto circuito
(Ele retorna tudo o que recebe)

O Arduino está sendo usado apenas como alimentação
'''

import serial
import time

ser = serial.Serial(
    port='COM3'
#    ,
#    baudrate=9600,
#    bytesize=8,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE
)

while True:
    enviar = input('Digite o que deve ser enviado: ')
    ser.write(bytes(enviar, 'ascii'))

    time.sleep(0.100)

    if ser.in_waiting:
        print(f'Recebido: {ser.read(ser.in_waiting)}')
    else:
        print(f'Não chegou nada')


