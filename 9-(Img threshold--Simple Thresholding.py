#If pixel value is greater than a threshold value, it is assigned one value (may be white or black).
#First argument is the source image which should be a grayscale image.
#Second argument is the threshold value which is used to classify the pixel values. 
#Third argument is the maxVal which represents the value to be given --
#if pixel value is more than (sometimes less than) the threshold value.
#OpenCV provides different styles of thresholding and it is decided by the 
#fourth parameter of the function

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg',0)     #read image
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)  #these are different method
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] #titles of an images
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5] #resulting images

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')   #plot all images 
    plt.title(titles[i])    #give title
    #plt.xticks([]),plt.yticks([])

plt.show()

    

#in this two output will show one is retvalue and second is threshold image