import numpy as np
import cv2 as cv   

img=cv.imread("Images/chessboard.jpg")
cv.imshow("image",img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("blank",blank)
mask=cv.circle(blank,(img.shape[0]//2,img.shape[1]//2),150,255,-1)
cv.imshow("mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
cv.waitKey(0)