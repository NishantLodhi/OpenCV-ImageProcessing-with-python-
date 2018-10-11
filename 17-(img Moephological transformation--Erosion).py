# morphological operations like Erosion, Dilation, Opening, Closing.
# functions like : cv2.erode(), cv2.dilate(), cv2.morphologyEx() etc.

"""Morphological transformations are some simple operations based on the image shape. 
It is normally performed on binary images.It needs two inputs, one is our original image,
 second one is called structuring element or kernel which decides the nature of operation.
 Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, 
 Closing."""
 
#---- morphological operations----1).Erosion
"""The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of 
 foreground object (Always try to keep foreground in white). 
 The kernel slides through the image (as in 2D convolution). 
 A pixel in the original image (either 1 or 0) will be considered 1 only if 
 all the pixels under the kernel is 1,otherwise it is eroded (made to zero)."""

""" So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. 
 So the thickness or size of the foreground object decreases or simply white region decreases 
 in the image. It is useful for removing small white noises (as we have seen in colorspace 
 chapter), detach two connected objects etc."""

import cv2
import numpy as np

img = cv2.imread('H:\\mor.jpg',0)
kernel = np.ones((5,5),np.uint8) # 5x5 kernel with full of ones. 
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow("erosion",erosion)  
cv2.waitKey(0)