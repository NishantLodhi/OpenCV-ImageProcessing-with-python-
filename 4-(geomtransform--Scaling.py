#Scaling is just resizing of the image. function cv2.resize()
#Different interpolation methods are used. Preferable interpolation methods are cv2.INTER_AREA for shrinking 
#and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming.
# By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes



import cv2
import numpy as np

img = cv2.imread('H:\\a.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC) #use this or resize
#height, width = img.shape[:2]
#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC) #use this also with height
cv2.imshow("scaling",res)
cv2.waitKey()