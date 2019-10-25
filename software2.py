
import sounddevice as sd
from scipy.signal import kaiserord, lfilter, firwin
from suaBibSignal import *
import matplotlib.pyplot as plt
import numpy as np

#######################################

# Capta o áudio
# Modula com a portadora
# Filtra

# Grava o áudio
# Demodula com a portadora
# Filtra

#######################################

class Software2: 

    def __init__(self):
        self.frequency = 44100
        self.sd = sd
        self.np = np
        self.duration = 2
        self.samples = 2 * 44100
        self.plt = plt
        self.signal = signalMeu()

    def SDdefault(self):
        self.sd.default.samplerate = 1/44100
        self.sd.default.channels = 2
        
    def recordAudio(self):
        self.audio = self.sd.rec(self.samples, self.frequency, channels=1)
        self.sd.wait()
        self.audioRec = []
        time = np.linspace(0,1,88200)        

        # for i in range(0, len(self.audio)):
        #     self.audioRec.append(self.audio[i])

        # print(len(self.audioRec))

        # print(self.audioRec


        for i in self.audio:
            for z in i:
                self.audioRec.append(z)

        print(len(self.audioRec))
        print(len(time))

        plt.plot(time, self.audioRec)
        plt.show()



    def generateCarrier(self):
        self.carrier = self.signal.generateSin(14000,1,5,self.frequency)

    def normalizeAudio(self):

        self.maxAudio = self.np.abs(max(self.audioRec))
        self.minAudio = self.np.abs(min(self.audioRec))

        self.audioNormalized = []

        if self.maxAudio > self.minAudio:
            self.audioNormalized = self.audioRec/self.maxAudio
        
        elif self.maxAudio < self.minAudio:
            self.audioNormalized = self.audioRec/self.minAudio

        else:
            self.audioNormalized = self.audioRec/self.maxAudio

    def demoduleAudio(self):
        self.signalmodule = []
        for i in range(0, len(self.carrier)):
            self.signalmodule.append(self.carrier[i] * self.audioNormalized[i])

    def filterAudio(self):
        self.nyq = 44100/ 2
        self.width = 5 / self.nyq
        self.ripple_db = 60
        self.N, self.beta = kaiserord(self.ripple_db, self.width)
        self.cutoff_hz = 4000
        self.taps = firwin(self.N, self.cutoff_hz/self.nyq, window=('kaiser', self.beta))
        self.audioFiltered = lfilter(self.taps, 1, self.signalmodule)

    def executeAudio(self):

        self.execAudio = []

        for i in self.audioFiltered:
            for z in i:
                self.execAudio.append(z)  

        self.sd.play(self.execAudio,self.frequency)
        self.sd.wait()

    def graphCapturedSignal(self):
        self.xf, self.yf = self.signal.calcFFT(self.audioNormalized, self.frequency)
        self.plt.figure("F(y)")
        self.plt.plot(self.xf,self.yf)
        self.plt.grid()
        self.plt.title('Fourier captured audio')
        self.plt.show()

    def graphDemodulatedSignal(self):
        self.xf, self.yf = self.signal.calcFFT(self.execAudio, self.frequency)
        self.plt.figure("F(y)")
        self.plt.plot(self.xf,self.yf)
        self.plt.grid()
        self.plt.title('Fourier demodulated audio')
        self.plt.show()

    def main(self):

        self.SDdefault()
        self.recordAudio()
        self.generateCarrier()
        self.normalizeAudio()
        self.demoduleAudio()
        self.filterAudio()
        self.executeAudio()
        # self.graphCapturedSignal()
        self.graphDemodulatedSignal()


decode = Software2()

decode.main()






