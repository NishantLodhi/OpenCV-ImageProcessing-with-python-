#functions : cv2.cvtColor(), cv2.inRange()
#more then 150 color space conversion but we use two-- BGR<<>>Gray,,,,,BGR<<>>HSV

#For color conversion, cv2.cvtColor(input_image, flag) 
#where flag determines the type of conversion.

#For BGR >>> Gray conversion we use the flags cv2.COLOR_BGR2GRAY
#for BGR >>>>>> HSV, we use the flag cv2.COLOR_BGR2HSV.

import cv2
import cv2


img1 = cv2.imread('H:\\oprn.jpg')
cv2.imshow("Image in BGR",img1)


img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV) # Convert from BGR to HSV
cv2.imshow("Image in hsv",img2)
cv2.waitKey(0)

