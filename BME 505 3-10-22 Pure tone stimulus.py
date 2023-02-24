# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:26:02 2022

@author: andre
"""
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
import sounddevice as sd
import sys


    
fs = 192000 # this is the typical sammpling rate because the corresponding Nyquist freq is 22500 Hz
# and since this is well above the highest frequency noise people can hear (in class someone heard up
#to 18000), it's a good rate to capture high quality audio.
f = 70
t = np.arange(0,fs)/fs
x = 0.25*np.sin(2*np.pi*f*t)
sd.play(x,fs)