#laplacian Pramid

"""Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for
 that. Laplacian pyramid images are like edge images only. Most of its elements are zeros. 
 They are used in image compression. A level in Laplacian Pyramid is formed by the difference
 between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.
 The three levels of a Laplacian level will look like below (contrast is adjusted to enhance the
 contents):"""
 
#---------------------------------code---------------------------------------

import cv2


img = cv2.imread('H:\\a.jpg',0)

lap = cv2.Laplacian(img,cv2.CV_64F)   #laplace function
lower_reso = cv2.pyrDown(lap) #down pramid lower in resolution after laplace applied
cv2.imshow("Downpramid",lower_reso)
cv2.waitKey(0)

     