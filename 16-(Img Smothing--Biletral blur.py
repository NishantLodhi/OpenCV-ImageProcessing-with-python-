""" This is not the case for the bilateral filter, cv2.bilateralFilter(), 
which was defined for, and is highly effective at noise removal while preserving edges. 
But the operation is slower compared to other filters."""
"""The bilateral filter also uses a Gaussian filter in the space domain,
 but it also uses one more (multiplicative) 
Gaussian filter component which is a function of pixel intensity differences"""

#---------4-------Biletral blur---------
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
cv2.imshow("original",img)

blur = cv2.bilateralFilter(img,9,75,75)

cv2.imshow("Blur",blur)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)