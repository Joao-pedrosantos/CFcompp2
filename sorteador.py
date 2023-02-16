from random import *
comandos = ['00 00 00 00', '00 00 AA 00', 'AA 00 00', '00 AA 00', '00 00 AA', '00 AA', 'AA 00', '00', 'FF']
txbuffer = []
bytearray = [bytes.fromhex(i) for i in comandos]

def sortear():
    qtd = randint(10, 31)
    for i in range(qtd):
        txbuffer.append(choice(bytearray))
        print(f'Comando {i+1}: {txbuffer[i]} ou {txbuffer[i].hex()}')
    return txbuffer


print(sortear())
