"""Image blurring is achieved by convolving the image with a low-pass filter kernel. 
It is useful for removing noise. It actually removes high frequency content (e.g: noise, edges)
from the image resulting in edges being blurred when this is filter is applied."""

"""This is done by the function cv2.blur() or cv2.boxFilter(). This is done by convolving the image with a normalized box filter. 
It simply takes the average of all the pixels under kernel area and
 replaces the central element with this average. """

#OpenCV provides mainly four types of blurring techniques.

#.........1------------------AVERAGING---------------
 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
cv2.imshow("original",img)

blur = cv2.blur(img,(5,5))  #matrix of 5x5

cv2.imshow("Blur",blur)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)


