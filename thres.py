import cv2 as cv 

img=cv.imread("Images/ronaldo.jpg")
cv.imshow("ronaldo",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#simple
threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)
threshold,threshinv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow("thresh_Inverse",threshinv)

#adaptive
adaptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,5,3)
cv.imshow("adaptive",adaptive_threshold)
cv.waitKey(0)