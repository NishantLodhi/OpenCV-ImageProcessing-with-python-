# It is done with the function, cv2.GaussianBlur().
"""We should specify the width and height of the kernel which should be positive and odd. 
We also should specify the standard deviation in the X and Y directions, 
sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. 
Gaussian filtering is highly effective in removing Gaussian noise from the image."""
#create a Gaussian kernel with the function, cv2.getGaussianKernel().


#------------2---------Gausian blur---------------

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
cv2.imshow("original",img)

blur = cv2.GaussianBlur(img,(5,5),0)  #matrix of 5x5

cv2.imshow("Blur",blur)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)