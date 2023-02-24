from enlace import *
import time
import numpy as np
from random import *
comandos_recebidos = []
comeco = b'\x0a'
fim = b'\x0f'
serialName = "COM8"
vivo = b'\xf0'
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
        qt = -1
        check = 0
        recebendo = True
        while recebendo:
            numero, lixo = com1.getData(1)
            numeroint = int.from_bytes(numero, byteorder='big')
            com1.sendData(np.asarray(vivo))
            if numero == fim:
                print('achei o fim')
                recebi = len(comandos_recebidos).to_bytes(1, byteorder='big')
                com1.sendData(np.asarray(fim))
                time.sleep(.1)
                com1.sendData(np.asarray(recebi))
                #recebendo = False
                break

            qt += 1
            print(f'numero de comandos ate agora {qt}')
            #teste.append(numeroint)
            info, lixo = com1.getData(numeroint)
            comandos_recebidos.append(info)
            print(f'recebeu a seguinte informacao {info}')
            comandos_recebidos.append(info)


    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        print("Comunicação encerrada")


if __name__ == "__main__":
    main()