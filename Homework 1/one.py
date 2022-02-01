import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


fig = plt.figure(1)

t = np.linspace(0,50,1000)
s = 2+3*np.cos(500*np.pi*t)+2*np.cos(1000*np.pi*t)+3*np.sin(2000*np.pi*t)
plt.plot(t, s)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Plot of continuous period signal')
plt.show()

###############################
SAMPLE_RATE = 1000
DURATION = 1
N = SAMPLE_RATE * DURATION

yf = fft(s)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(abs(xf), np.abs(yf))
plt.title('Digital Fast Fourier transform')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()