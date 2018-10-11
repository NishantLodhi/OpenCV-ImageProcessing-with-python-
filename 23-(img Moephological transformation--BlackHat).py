#It is the difference between the closing of the input image and input image.

#It is the difference between the closing of the input image and input image.

#-------------------Black hat-----------------

import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("res_blackhat",blackhat)   
cv2.waitKey(0)