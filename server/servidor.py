from enlace import *
import time
import numpy as np
from random import *
comandos_recebidos = []
comeco = b'\x0a'
fim = b'\x0f'
serialName = "COM6"

def main():
    try:
        com1 = enlace(serialName)
        com1.enable()
        print("esperando 1 byte de sacrifício")
        tamanho, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)
        print("byte de sacrificio recebido")

        i =0
        recebendo = True
        print('inicio da transmissão')
        while recebendo:
            if i == 0:
                print("esperando o começo")
                com1.rx.clearBuffer()
                com1.sendData(np.asarray(comeco))
                com1.rx.clearBuffer()
                time.sleep(.1)
                print("começou")
            else:
                print(f'loop {i}')
                numero = com1.getData(1)
                
                numeroint = int.from_bytes(numero[0], byteorder='big')
                print(numero)
                rxBuffer, nRx = com1.getData(numeroint)

                info = com1.getData(numeroint)
                #print(f'aqui tem o suposto comando {nRx}')
                #print("recebeu {} bytes" .format(len(rxBuffer)))    
                #print("recebeu {}" .format(rxBuffer))

                if info == fim:
                    com1.sendData(np.asarray(fim))
                    break
            i += 1
    
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
    print("Comunicação encerrada")
    com1.disable()
    print(comandos_recebidos)

if __name__ == "__main__":
    main()
