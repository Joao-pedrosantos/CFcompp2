from random import *
comandos = ['00 00 00 00', '00 00 AA 00', 'AA 00 00', '00 AA 00', '00 00 AA', '00 AA', 'AA 00', '00', 'FF']
txbuffer = []
def sortear():
    qtd = randint(10, 31)
    for i in range(qtd):
        txbuffer.append(choice(comandos))
        print(f'Comando {i+1}: {txbuffer[i]}')
    return txbuffer


print(sortear())