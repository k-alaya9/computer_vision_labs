import cv2 as cv 
import numpy as np 
img=cv.imread("Images/closing.png")
cv.imshow("orginal image ",img)

kernal=np.ones((5,5),dtype='uint8')

ersion=cv.erode(img,kernel=kernal,iterations=2)
cv.imshow("test",ersion)
dilate=cv.dilate(img,kernel=kernal,iterations=1)
cv.imshow("dilate",dilate)

bitwise_or=cv.bitwise_or(ersion,dilate)
cv.imshow("or",bitwise_or)
numbers=cv.imread("Images/opening.png")
cv.imshow("orginal",numbers)
opening=cv.morphologyEx(numbers,cv.MORPH_OPEN,kernel=kernal)
cv.imshow("open",opening)
j=cv.imread("Images/closing.png")
closing=cv.morphologyEx(j,cv.MORPH_CLOSE,kernel=kernal)
cv.imshow("closing",closing)
j_image=cv.imread("Images/j.png")
gradient=cv.morphologyEx(j_image,cv.MORPH_GRADIENT,kernal)
cv.imshow("gradients",gradient)
cv.waitKey(0)