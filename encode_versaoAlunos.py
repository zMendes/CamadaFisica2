

#importe as bibliotecas
from suaBibSignal import*
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import keyboard
import sys


def pickNumber(number):

    if number =="0":
        return 941, 1336
    elif number =="1":
        return 697, 1209
    elif number =="2":
        return 697, 1336
    elif number =="3":
        return 697, 1477
    elif number =="4":
        return 770, 1209
    elif number =="5":
        return 770, 1336
    elif number =="6":
        return 770, 1477
    elif number =="7":
        return 852, 1209
    elif number =="8":
        return 852, 1336
    elif number =="9":
        return 852, 1477
    elif number =="a":
        return 697, 1663
    elif number =="b":
        return 770, 1663
    elif number =="c":
        return 852, 1663
    elif number =="d":
        return 941, 1663
    elif number =="x":
        return 941, 1209
    elif number =="#":
        return 941, 14770
    else: return 0,0
        

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def main():
    print("Esperando tecla ser pressionada:")
    key = False
    signal = signalMeu() 
    tone = []
    gainX  = 0.2
    gainY  = 0.2
    time = 5
    fs = 44100
    

    key = keyboard.read_key()


    input = key
    f1, f2 = pickNumber(key)
    print(f1,f2)
    
        
    #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    x1,sen1 = signal.generateSin(f1,gainX,time,fs)
    x2,sen2 = signal.generateSin(f2,gainX,time,fs)
    

    for i in range(len(sen1)):
        tone.append(sen1[i]+sen2[i]) 
    #plt.plot(x1[0:100], sen1[0:100])
    #plt.show()

      
    

    print("Gerando Tom referente ao símbolo : {}".format(input))
    
    #plt.plot(x1, sen1)
    #plt.plot(x2, sen2)
    #plt.show()
    sd.play(tone, fs)
    sd.wait()

while (True):
    main()
