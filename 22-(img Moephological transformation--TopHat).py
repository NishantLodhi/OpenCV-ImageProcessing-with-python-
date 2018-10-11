#It is the difference between input image and Opening of the image. 
#Below example is done for a 9x9 kernel.


#---------------Top Hat-------------------


import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("res_top",tophat)   
cv2.waitKey(0)