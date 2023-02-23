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
        print("ebaaaaaa")
        tamanho, nRx = com1.getData(1)
        tamanhoint = int.from_bytes(tamanho, byteorder='big')
        rxBuffer, nRx = com1.getData(tamanhoint)
        i = True
        print("ebaaa2")
        if comeco == rxBuffer:
            while i:
                print('inicio da transmissão')
                numero = com1.getData(1)
                info = com1.getData(numero)
                comandos_recebidos.append(info)
                print("recebeu {} bytes" .format(len(rxBuffer)))    
                print("recebeu {}" .format(rxBuffer[i]))

                if info == fim:
                    com1.sendData(np.asarray(fim))
                    i = False  
    
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
    print("Comunicação encerrada")
    com1.disable()
    print(comandos_recebidos)

if __name__ == "__main__":
    main()
