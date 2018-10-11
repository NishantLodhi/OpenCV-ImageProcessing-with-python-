"""As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF),
high-pass filters (HPF), etc.A LPF helps in removing noise, or blurring the image.
A HPF filters helps in finding edges in an image. """
#OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image




import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
cv2.imshow("original",img)

kernel = np.ones((5,5),np.float32)/25   #pixel of an image broke into matrix and divide by 25
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow("Averaging",dst)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)