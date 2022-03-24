import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Lenna.jpg')

redChannel = img[:, :, 0]
greenChannel =  img[:, :, 1]
blueChannel =  img[:, :, 2]

# NTSC approach
LennaGray = np.dot(0.299, redChannel) + np.dot(0.587,greenChannel) + np.dot(0.114,blueChannel)

plt.imshow(LennaGray, cmap = plt.get_cmap('gray'))
plt.axis("off")
plt.savefig('LennaGray.jpg')
plt.title('RGB to gray')
plt.show()
print(LennaGray.min(), LennaGray.max())    # 8-bit gray image

#Q1_2

downscale = np.zeros(shape=(64,64))
for i in range(64):
    for j in range(64):
        downscale[i,j] = LennaGray[i*4, j*4]

plt.imshow(downscale, cmap = plt.get_cmap('gray'))
plt.savefig('downscaled_gray_scale.jpg')
plt.title('downscaled image.jpg')
