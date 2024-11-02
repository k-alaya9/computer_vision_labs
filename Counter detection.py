import cv2 as cv
import numpy as np
img= cv.imread("Images/ronaldo.jpg")

cv.imshow("image",img)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("blank",blank)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur=cv.GaussianBlur(gray,(5,5),10)
# cv.imshow("blur",blur)


canny=cv.Canny(gray,125,175)
cv.imshow('canny',canny)

rent,thres=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("thresh",thres)

c,h=cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(c))
cv.drawContours(blank,c,-1,(255,0,0),1)
cv.imshow("contours",blank)
cv.waitKey(0)