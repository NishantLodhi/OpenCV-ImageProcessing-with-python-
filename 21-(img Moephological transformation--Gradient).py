#Gradient
#It is the difference between dilation and erosion of an image.


import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("res_gradient",gradient)   
cv2.waitKey(0)