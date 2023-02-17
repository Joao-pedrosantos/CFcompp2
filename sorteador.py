from random import *


def sortear():
    comandos = ['00 00 00 00', '00 00 AA 00', 'AA 00 00', '00 AA 00', '00 00 AA', '00 AA', 'AA 00', '00', 'FF']
    txbuffer = []
    bytearray = [bytes.fromhex(i) for i in comandos]
    qtd = randint(10, 31)
    for i in range(qtd):
        txbuffer.append(choice(bytearray))
        txbuffer[i].upper()
        print(f'Comando {i+1}: {txbuffer[i]} ou {txbuffer[i].hex().upper()}')
    return txbuffer