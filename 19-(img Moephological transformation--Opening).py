"""Opening is just another name of erosion followed by dilation. 
It is useful in removing noise, as we explained above. Here we use the function, 
cv2.morphologyEx()"""

import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("res_opening",opening)   
cv2.waitKey(0)