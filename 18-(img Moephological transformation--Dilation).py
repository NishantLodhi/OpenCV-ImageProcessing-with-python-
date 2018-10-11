#Dialation
"""It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under
the kernel is ‘1’. So it increases the white region in the image or size of foreground object 
increases. Normally, in cases like noise removal, erosion is followed by dilation. 
Because, erosion removes white noises, but it also shrinks our object. 
So we dilate it. Since noise is gone, they won’t come back, but our object area increases."""

import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("res_dilation",dilation)   
cv2.waitKey(0)