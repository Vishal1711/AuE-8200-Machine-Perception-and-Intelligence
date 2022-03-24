# import numpy as np  # This is to deal with numbers and arrays
# import cv2 as cv  # This is to deal with images
# from matplotlib import pyplot as plt
#
# Image = cv.imread("LennaGray.jpg", 0)
# Image_Height = Image.shape[0]
# Image_Width = Image.shape[1]
# Histogram = np.zeros([256], np.int32)
#
# for x in range(0, Image_Height):
#     for y in range(0, Image_Width):
#         Histogram[Image[x, y]] += 1
#
#
# print(Histogram.dtype)
# plt.plot(Histogram)
# # plt.title("GrayScale Histogram")
# # plt.xlabel("Intensity Level")
# # plt.ylabel("Intensity Frequency")
# # plt.savefig("Histogram_GrayScale.jpg")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img = np.array(Image.open('Lenna.jpg'))

redChannel = img[:, :, 0]
greenChannel =  img[:, :, 1]
blueChannel =  img[:, :, 2]

# NTSC approach
LennaGray = np.dot(0.299, redChannel) + np.dot(0.587,greenChannel) + np.dot(0.114,blueChannel)
LennaGray = LennaGray.astype(int)


histogram = np.zeros(256)
x = np.arange(0,256,1)
m = (LennaGray.shape[0])
n = (LennaGray.shape[1])

for i in range(0,m):
    for j in range(0,n):
        value = LennaGray[i][j]
        histogram[value] = histogram[value] + 1
plt.figure(1)
plt.plot(x,histogram)
plt.title('LennaGray Histogram graph')
plt.xlabel('Pixel Value from 0 to 255')
plt.ylabel('Pixel Frequency')
plt.show()


################################################################################################
#Question 2
current = 0
histogram_array1 = np.zeros(256)
for i in range(0,n):
    current = current + histogram[i]
    histogram_array1[i] = current

plt.figure(2)
plt.plot(x,histogram_array1)
plt.title('LennaGray Cumulative Histogram graph')
plt.xlabel('Pixel Value from 0 to 255')
plt.ylabel('Pixel Frequency')
plt.show()


##############################################################################################
#Question 3

intensity = np.zeros(shape=(256,))
pixels = m * n

# insert the count of intensities in the intensity array
for row in LennaGray:
    for pixel in row:
        intensity[pixel] += 1



size = m * n
# create an array which store the probabilities of counting of intensities
probability_intensity = intensity / float(size)

# calculating commutative distribution function
cumulative_distribution_function = np.zeros(shape=(256,))
t_cumulative_distribution_function = np.zeros(shape=(256,))

value = 0
for i in range(0, len(probability_intensity)):
    cumulative_distribution_function[i] = value + probability_intensity[i]
    value = cumulative_distribution_function[i]

for i in range(0, len(cumulative_distribution_function)):
    t_cumulative_distribution_function[i] = round(i * cumulative_distribution_function[i])

imag_after_histogram_equalization = np.zeros(LennaGray.shape)

for row_index in range(0, len(LennaGray)):
    for col_index in range(0, len(img[0])):
        imag_after_histogram_equalization[row_index][col_index] = \
            t_cumulative_distribution_function[LennaGray[row_index][col_index]]

histogram_equalization = np.zeros(256)

for i in range(0, len(LennaGray)):
    for j in range(0, len(LennaGray)):
        value = int(imag_after_histogram_equalization[i,j])
        histogram_equalization[value] += 1

plt.figure(3)
plt.bar(range(256) , histogram_equalization, 0.5)
plt.title('Histogram equalization graph')
plt.xlabel('Value of bins')
plt.ylabel('Frequency of Intensity')
plt.show()

plt.figure(4)
plt.title('Histogram equalization for Lenna image')
fit = plt.imshow(imag_after_histogram_equalization, cmap = plt.get_cmap('gray'))
plt.show()