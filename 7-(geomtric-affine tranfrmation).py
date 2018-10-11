# in tgis affine all parallel lines in the original image will still be parallel in the output image.
#Then cv2.getAffineTransform will create a 2x3 matrix which is to be passed to cv2.warpAffine.

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('H:\\a.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)  #create matrix

dst = cv2.warpAffine(img,M,(cols,rows)) #pass in this

plt.subplot(121),plt.imshow(img),plt.title('Input')
a=plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.imshow("aa",dst)
cv2.waitKey(0)