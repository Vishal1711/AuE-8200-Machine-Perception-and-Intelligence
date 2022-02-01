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

#######################################
# Normalize within range of 0 and 1
# max_ = max(noise)
# min_ = min(noise)
# noise = (noise- min_)/(max_ - min_)
#######################################

#Apply a normalized (mean 0, standard deviation 1)

mean = sum(noise)/len(noise)
standard_deviation = math.sqrt( sum( (noise - mean)**2 ) / len(noise))
noise1 = (noise-mean)/(standard_deviation)

y = np.pad(noise, pad_width=1)
h3k = [0.2709,0.44198,0.27901]
h11k =  [0.000003, 0.000229, 0.005977, 0.060598, 0.24173, 0.382925, 0.24173, 0.060598, 0.005977, 0.000229, 0.000003]


plt.plot(n,noise1)
#plt.plot(n,k)



def convolve_1d(signal, kernel):

    n_sig = y.size
    n_ker = len(h3k)
    n_conv = n_sig - n_ker + 1
    rev_kernel = kernel[::-1].copy()
    result = np.zeros(n_conv)
    for i_conv in range(n_conv):
        result[i_conv] = np.dot(signal[i_conv: i_conv + n_ker], rev_kernel)
    return result

x1 = convolve_1d(y,h3k)


plt.plot(n, noise)
plt.plot(n, x1)
plt.plot(n,x)
plt.title('x(k), and y(k) based on kernel window size 3')
plt.legend(['normalized (mean 0, standard deviation 1)','x\'(k)','y(k) based on kernel window size 3','x(k) = 20'])
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.show()