#Inage pramid
#We will see these functions: cv2.pyrUp(), cv2.pyrDown()
"""Normally, we used to work with an image of constant size. But in some occassions, we need to work 
with images of different resolution of the same image. For example, while searching for something 
in an image, like face, we are not sure at what size the object will be present in the image. 
In that case, we will need to create a set of images with different resolution and search for object'
in all the images. These set of images with different resolution are called Image Pyramids .
 
There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids."""
"""Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and
 columns in Lower level (higher resolution) image. Then each pixel in higher level is formed by 
 the contribution from 5 pixels in underlying level with gaussian weights.
 The same pattern continues as we go upper in pyramid (ie, resolution decreases). 
 Similarly while expanding, area becomes 4 times in each level."""
 
#==============code===================================== 
import cv2


img = cv2.imread('H:\\a.jpg')
lower_reso = cv2.pyrDown(img) #down pramid lower in resolution
cv2.imshow("Downpramid",lower_reso)

higher_reso2 = cv2.pyrUp(lower_reso)#this give higher resolution
cv2.imshow("Uppramid",higher_reso2)
cv2.waitKey(0)



