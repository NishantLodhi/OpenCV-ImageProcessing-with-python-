"""But there is a slight problem with that. Black-to-White transition is taken as Positive slope 
(it has a positive value) while White-to-Black transition is taken as a Negative slope 
(It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. 
In simple words, you miss that edge.
If you want to detect both edges, better option is to keep the output datatype to some higher forms,
like cv2.CV_16S, cv2.CV_64F etc, take its absolute value and then convert back to cv2.CV_8U"""





import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.imshow("sobelx64f",sobelx64f)
abs_sobel64f = np.absolute(sobelx64f)
cv2.imshow("abs_sobel64f",abs_sobel64f)
sobel_8u = np.uint8(abs_sobel64f)
cv2.imshow("sobel_8u",sobel_8u)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

cv2.waitKey(0)