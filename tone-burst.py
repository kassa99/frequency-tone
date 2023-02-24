import numpy as np
import sounddevice as sd

# To define the frequency and duration of the tone burst
frequency = 16000  # Hz
duration = 0.5  # seconds
fs = 44100
# Generating the samples for the tone burst using the numpy library
samples = (np.sin(2*np.pi*np.arange(44100*duration)*frequency/44100)).astype(np.float32)
# Plays the tone burst using the sounddevice library
sd.play(samples, fs)
# To wait for the tone burst to finish playing
sd.wait()
