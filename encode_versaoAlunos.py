

#importe as bibliotecas
from suaBibSignal import*
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys


def pickNumber():
    number = input("Escolha o número que você deseja enviar:")
    if number =="0":
        return 941, 1336, number
    elif number =="1":
        return 697, 1209, number
    elif number =="2":
        return 697, 1336, number
    elif number =="3":
        return 697, 1477, number
    elif number =="4":
        return 770, 1209, number
    elif number =="5":
        return 770, 1336, number
    elif number =="6":
        return 770, 1477, number
    elif number =="7":
        return 852, 1209, number
    elif number =="8":
        return 852, 1336, number
    elif number =="9":
        return 852, 1477, number
    elif number =="a":
        return 697, 1663, number
    elif number =="b":
        return 770, 1663, number
    elif number =="c":
        return 852, 1663, number
    elif number =="d":
        return 941, 1663, number
    elif number =="x":
        return 941, 1209, number
    elif number =="#":
        return 941, 14770, number
        

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def main():
    print("Inicializando encoder")
    signal = signalMeu() 
    tone = []
    gainX  = 0.1
    gainY  = 0.1
    time = 1
    fs = 44100
    f1, f2 ,input = pickNumber()
    #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:

    
    x1,sen1 = signal.generateSin(f1,gainX,time,fs)
    x2,sen2 = signal.generateSin(f2,gainX,time,fs)
    

    for i in range(len(sen1)):
        tone.append(sen1[i]+sen2[i]) 

      
#relativo ao volume. Um ganho alto pode saturar sua placa... comece com .3    
    


    print("Gerando Tons base")
    
    #gere duas senoides para cada frequencia da tabela DTMF ! Canal x e canal y 
    #use para isso sua biblioteca (cedida)
    #obtenha o vetor tempo tb.
    #deixe tudo como array

    #printe a mensagem para o usuario teclar um numero de 0 a 9. 
    #nao aceite outro valor de entrada.
    print("Gerando Tom referente ao símbolo : {}".format(input))
    
    
    #construa o sunal a ser reproduzido. nao se esqueca de que é a soma das senoides
    
    #printe o grafico no tempo do sinal a ser reproduzido
    # reproduz o som
    print("Rodará o play")
    sd.play(tone, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()

while (True):
    main()
