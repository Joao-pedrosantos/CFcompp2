from random import *


def sortear():
    comandos = ['00 00 00 00', '00 00 AA 00', 'AA 00 00', '00 AA 00', '00 00 AA', '00 AA', 'AA 00', '00', 'FF']
    txbuffer = []
    tamanho = []
    bytearray = [bytes.fromhex(i) for i in comandos]
    qtd = randint(10, 31)
    for i in range(qtd):
        escolha = choice(bytearray)
        tamanho.append(len(escolha).to_bytes(1, byteorder='big'))

        txbuffer.append(escolha)
        txbuffer[i].upper()
        print(f'Comando {i+1}: {txbuffer[i]} ou {txbuffer[i].hex().upper()} // Tamanho: {tamanho[i]} ')
    return tamanho, txbuffer

print(sortear())