import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy import signal

n = np.arange(0,1000,1)

x = []

for i in range(len(n)):
    if n[i] <500:
        x.append(0)
    else:
        x.append(1)


plt.plot(n,x)
plt.title('Visualize the discrete signal')
plt.xlabel('Time in microseconds')
plt.ylabel('Amplitude')
plt.show()

##########################################

SAMPLE_RATE = 1000
DURATION = 1
N = SAMPLE_RATE * DURATION

yf = fft(x)
xf = fftfreq(N, 1 / SAMPLE_RATE)
_min = min(yf)
_max = max(yf)
print(_max)
print(_min)

plt.plot(abs(xf), np.abs(yf))
plt.title('Digital Fast Fourier transform (Amplitude and f)')
plt.xlabel('Frequency in kHz')
plt.ylabel('FFT of Amplitude')
plt.show()

# -3dB bandwidth frequencies (f_low, f_high) in frequency spectrum.
x_db = 10 * np.log10(yf**2)

plt.plot(n, x_db)
plt.title('Signal Power in dB')
plt.show()