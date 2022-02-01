from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

f = 1000  # Frequency, in cycles per second, or Hertz
f_s = 1000  # Sampling rate, or number of measurements per second

t = np.linspace(0, 1, 2 * f_s)

x = []

for i in range(len(t)):
    if t[i] <0.500:
        x.append(0)
    else:
        x.append(1)

plt.plot(t, x)
plt.show()
X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s
plt.plot(freqs, np.abs(X))
plt.show()

x_db = 10 * np.log10(X**2)

plt.plot(t, x_db)
plt.title('Signal Power in dB')
plt.show()