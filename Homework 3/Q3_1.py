# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('ParkingLot.jpg',0)
#
# hist,bins = np.histogram(img.flatten(),256,[0,256])
#
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
#
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()
#
# (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imshow('bi',im_bw)
# cv2.waitKey(0)
# cv2.imwrite('binary_image.jpg', im_bw)
#
#
#
# def display_lines(image, lines):
#     line_image = np.zeros_like(image)
#     if lines is not None:
#         for line in lines:
#             x1, y1, x2, y2= line.reshape(4)
#             cv2.line(line_image, (x1,y1),(x2,y2),(255,0,0),10)
#     return line_image
#
# lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
# line_image = display_lines(lane_image, lines)

import cv2
import numpy as np
img = cv2.imread('ParkingLot.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges, 2, np.pi /180, 150, np.array([]), minLineLength=40, maxLineGap=5)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()


