import cv2 as cv
import numpy as np


img=cv.imread("Images/home.jpg")
cv.imshow("image",img)
blank=np.zeros(img.shape[:2],dtype="uint8")

b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
red=cv.merge([blank,blank,r])
green=cv.merge([blank,g,blank])
cv.imshow("blue",blue)
cv.imshow("red",red)
cv.imshow("green",green)

merged=cv.merge([b,g,r])
cv.imshow("merged",merged)

cv.waitKey(0)