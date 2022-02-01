import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

n = np.arange(0,500,1)
x = []

for i in range(len(n)):
    if n[i] <500:
        x.append(20)


mu, sigma = 0, 1 # mean and standard deviation
np.random.seed(0)
s = np.random.normal(mu, sigma**2, 500)

noise = x + s

#Apply a normalized (mean 0, standard deviation 1)

mean = sum(noise)/len(noise)
standard_deviation = math.sqrt( sum( (noise - mean)**2 ) / len(noise))
noise1 = (noise-mean)/(standard_deviation)

plt.plot(n,x)
plt.plot(n,noise)
plt.plot(n,noise1)
plt.title('Visualize both x(k) and x\'(k)')
plt.legend(['Discrete signal x(k) = 20','Random noise n(k)','normalized (mean 0, standard deviation 1)'])
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.show()