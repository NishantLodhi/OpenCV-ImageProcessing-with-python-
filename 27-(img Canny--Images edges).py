#Canny Edge Detection
#OpenCV functions for that : cv2.Canny()
"""Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny 
in 1986. It is a multi-stage algorithm and we will go through each stages.
Noise Reduction
Since edge detection is susceptible to noise in the image, first step is to remove the noise 
in the image with a 5x5 Gaussian filter. We have already seen this in previous chapters.
Finding Intensity Gradient of the Image
Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction 
to get first derivative in horizontal direction (G_x) and vertical direction (G_y)"""


#-----------------------------------code---------------------
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg',0) #import in gray
edges = cv2.Canny(img,100,200) #apply canny function
cv2.imshow("canny",edges)

plt.subplot(121),plt.imshow(img,cmap = 'gray')  #plot the images
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
