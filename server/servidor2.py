from enlace import *
import time
import numpy as np
from random import *
comandos_recebidos = []
comeco = b'\x0a'
fim = b'\x0f'
serialName = "COM7"
teste = []
def main():
    try:
        com1 = enlace(serialName)
        com1.enable()
        print("esperando 1 byte de sacrifício")
        bsacr  = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)
        print(bsacr[0])
        print("byte de sacrificio recebido")

        recebendo = True
        while recebendo:
            numero, lixo = com1.getData(1)
            print(numero)
            numeroint = int.from_bytes(numero, byteorder='big')
            teste.append(numeroint)
            info = com1.getData(numeroint)
            if info == fim:
                com1.sendData(np.asarray(fim))
                print("terminou")
                recebendo = False
                break
            comandos_recebidos.append(info)
        print(len(comandos_recebidos))            

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        print("Comunicação encerrada")


if __name__ == "__main__":
    main()