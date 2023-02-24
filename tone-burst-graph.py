import numpy as np
import pyaudio
import matplotlib.pyplot as plt

# Define the parameters of the tone burst
duration = 1.0   # Duration of the tone burst in seconds
frequency = 20000 # Frequency of the tone burst in Hz
sample_rate = 44100 # Sampling rate of the audio signal in Hz

# Generate the audio signal for the tone burst
samples = (np.sin(2*np.pi*np.arange(sample_rate*duration)*frequency/sample_rate)).astype(np.float32)

# Calculate the frequency spectrum of the tone burst
fft_size = 2**int(np.ceil(np.log2(len(samples))))
spectrum = np.abs(np.fft.fft(samples, fft_size)[:int(fft_size/2)]) / fft_size * 2

# Plot the frequency spectrum of the tone burst
freq_axis = np.linspace(0, sample_rate/2, len(spectrum))
plt.plot(freq_axis, 20*np.log10(spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

# Play the audio signal using PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=True)
stream.write(samples)
stream.stop_stream()
stream.close()
p.terminate()
