#OpenCV has a function, cv2.getStructuringElement(). You just pass the shape and size of the 
#kernel, you get the desired kernel.

import cv2
import numpy as np
rect= cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))    #Rectangular Kernal
print("The rectangular kernal",rect)
elipse=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))    #Eliptical kernal
print("The Eliptical kernal",elipse)
cross_shaped=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) #cross_shaped
print("The cross_shaped Kernal",cross_shaped)

cv2.waitKey(0)