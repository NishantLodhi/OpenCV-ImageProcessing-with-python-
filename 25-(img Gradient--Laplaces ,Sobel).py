#Image Gradients
#We will see following functions : cv2.Sobel(), cv2.Scharr(), cv2.Laplacian() etc
#OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian. 

#Sobel and Scharr Derivatives
"""Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more 
resistant to noise.You can specify the direction of derivatives to be taken, vertical or horizontal 
(by the arguments, yorder and xorder respectively). You can also specify the size of kernel by the
 argument ksize. If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3
 Sobel filter."""
#2. Laplacian Derivatives
"""each derivative is found using Sobel derivatives. If ksize = 1, 
 then following kernel is used for filtering:"""
 
 #-----------------CODE-----------------------------------------
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)   #laplace function
cv2.imshow("Laplace_res",laplacian)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  #perform sobel
cv2.imshow("sobelx",sobelx)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow("sobely",sobely)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

cv2.waitKey(0)