#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import math
import  peakutils 



#funcao para transformas intensidade acustica em dB
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
    signal = signalMeu()
    #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    fs = 44100
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    sd.default.samplerate = fs#taxa de amostragem
    sd.default.channels = 1  #voce pode ter que alterar isso dependendo da sua placa
    duration = 3#tempo em segundos que ira aquisitar o sinal acustico captado pelo mic


    # faca um printo na tela dizendo que a captacao comecará em n segundos. e entao 
    #use um time.sleep para a espera
    #print("Gravação começará em 3 segundos.")
    time.sleep(2)
   #faca um print informando que a gravacao foi inicializada
    print("Gravação iniciada")
   #declare uma variavel "duracao" com a duracao em segundos da gravacao. poucos segundos ... 
   #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)
    numAmostras = duration*fs
    audio = sd.rec(numAmostras, fs, channels=1)
    sd.wait()
    print("...     FIM")
    y = []
    for i in audio:
        for z in i:
            y.append(z)   
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)
    

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    t = np.linspace(0,3,numAmostras)
    # plot do gravico  áudio vs tempo!
   
    
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = signal.calcFFT(y, fs)
    plt.figure("F(y)")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Fourier audio')
    

    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.
    
    index = peakutils.indexes(yf,0.3,100)
    print(index)
    
    f1 = xf[index[0]]
    f2 = xf[index[1]]
    n = 0

    print(f1,f2)
    line = [697, 770, 852, 941]
    col = [1209, 1336, 1477, 1633]


    for i in line:
        if (math.isclose(i, f1, abs_tol = 10)):
            peak1 = i 
    for z in col:
        if (math.isclose(z, f2, abs_tol = 10)):
            peak2 = z
    
    matriz =[['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['X', '0', '#', 'D']]


    l = line.index(peak1)
    c = col.index(peak2)
    tecla = matriz[l][c]



    print(tecla)



    #printe os picos encontrados! 
    
    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    #print a tecla.
    
  
    ## Exibe gráficos
    #plt.show()

if __name__ == "__main__":
    main()
