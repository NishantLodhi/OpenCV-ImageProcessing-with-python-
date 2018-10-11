# the function cv2.medianBlur() computes the median of all the pixels under 
#the kernel window and the central pixel is replaced with this median value
"""This is highly effective in removing salt-and-pepper noise. 
One interesting thing to note is that, in the Gaussian and box filters, 
the filtered value for the central element can be a value which may not exist in the original image. 
However this is not the case in median filtering, 
since the central element is always replaced by some pixel value in the image. 
This reduces the noise effectively. The kernel size must be a positive odd integer."""

#---------3-------Median blur---------
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
cv2.imshow("original",img)

median = cv2.medianBlur(img,5) 

cv2.imshow("Blur",median)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)