import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift
import math
import numpy as np
from scipy.io import wavfile

class My_Signal:
    def __init__(self, t=None, amplitude=None, frequency=None):
        self.amplitude = amplitude
        self.frequency = frequency
        if not (amplitude == None or frequency == None):
            self.sum = self.amplitude*np.sin(2*np.pi*self.frequency*t)
        else:
            self.sum = 0

    def set_sum(self, data):
        self.sum = data

    def add_signal(self, t, amplitude, frequency):
        self.sum = self.sum+amplitude*np.sin(2*np.pi*frequency*t)

    def add_white_noise(self, amplitude=1):
        mean = 0
        std = 1
        num_samples = self.sum.size
        noise = amplitude*np.random.normal(mean, std, size=num_samples)
        self.sum = self.sum+noise

    def add_high_frequency_noise(self, t, amplitude=1):
        hf_noise = amplitude*(np.sin(2*np.pi*8000*t)+np.sin(2*np.pi*7000*t) +
                              np.sin(2*np.pi*6000*t)+np.sin(2*np.pi*10000*t))
        self.sum = self.sum+hf_noise

    def reset_signal(self):
        try:
            self.sum = np.zeros(self.sum.size)
        except:
            self.sum = 0

class Audio_Signal:

    def __init__(self):
        self.fs=None
        self.data=None
        self.read_signal()
    def getfs(self):
        return self.fs
    def getdata(self):
        return self.data

    def read_signal(self,path="./audio/test.wav"):
        self.fs, self.data = wavfile.read(path)


class MyRIFSignal:
    def __init__(self):
        self.fs=48000
        self.signal=None
        self.duration=266240 / self.fs
        self.time = np.linspace(0., self.duration, 266240)
    def SinSignal(self,Amp,fre):
        return Amp*np.sin(2*np.pi*fre*self.time)

    def AddSignal(self,signal):
        try:
            self.signal=np.add(self.signal,signal)
        except:
           self.setsignal(signal)
    def AddWhiteNoise(self, amplitude=1):
        mean = 0
        std = 1
        num_samples = len(self.signal)
        noise = amplitude*np.random.normal(mean, std, size=num_samples)
        self.AddSignal(noise)

    def gettime(self):
        return self.time
    def getfs(self):
        return self.fs
    def getsignal(self):
        return self.signal
    def setfs(self,fs):
        self.fs=fs
    def setsignal(self,signal):
        self.signal=signal
    def setduration(self,time):
        self.duration=time
    def Reset(self):
        self.signal=None




# f_sample = 44000
# t = np.linspace(0, 1, f_sample)
# s1 = My_Signal()
# s1.add_signal(t, 20, 1000)
# s1.add_signal(t, 10, 600)
# s1.add_white_noise(20)

# xf = fftfreq(f_sample, 1/f_sample)
# fft_output2 = (fft(s1.sum))
# fft_output2 = fft_output2/np.max(fft_output2)
# plt.plot(xf, np.abs(fft_output2))
# plt.show()
