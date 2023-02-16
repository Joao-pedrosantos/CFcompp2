from random import *
comandos = ['00 00 00 00', '00 00 AA 00', 'AA 00 00', '00 AA 00', '00 00 AA', '00 AA', 'AA 00', '00', 'FF']
enviar = []
def sortear():
    qtd = randint(10, 31)
    for i in range(qtd):
        enviar.append(choice(comandos))
        print(enviar[i])
    return enviar
print(sortear())