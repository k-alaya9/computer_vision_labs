import cv2 as cv 
import numpy as np

img=cv.imread("Images/eye.jpg")
cv.imshow("ronaldo",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.resize(gray,(500,500))
cv.imshow("gray",gray)

#Lapcian edge detector
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)

#Sobel edge detector
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combained_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("sobel",combained_sobel)

#canny edge detector 
canny=cv.Canny(gray,125,16)
cv.imshow("canny",canny)


cv.waitKey(0)
