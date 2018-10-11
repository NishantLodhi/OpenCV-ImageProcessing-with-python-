#Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small 
#holes inside the foreground objects, or small black points on the object.

import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8)  
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("res_closing",closing)   
cv2.waitKey(0)