#Straight lines will remain straight even after the transformation. 
#To find this transformation matrix, you need 4 points on the input image and
#corresponding points on the output image. 
#Among these 4 points, 3 of them should not be collinear


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('H:\\a.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.imshow("result",dst)
cv2.waitKey(0)