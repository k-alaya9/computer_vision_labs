import cv2 as cv 
import numpy as np


blank=np.zeros((400,400),dtype='uint8')

rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rect)
cv.imshow('Circle',circle)

# bitwise AND
bitwise_and=cv.bitwise_and(rect,circle)
cv.imshow('AND',bitwise_and)

# bitwise OR
bitwise_or=cv.bitwise_or(rect,circle)
cv.imshow("OR",bitwise_or)

# bitwise XOR
bitwise_xor=cv.bitwise_xor(rect,circle)
cv.imshow("XOR",bitwise_xor)

# bitwise NOT
bitwise_not=cv.bitwise_not(rect)
cv.imshow("NOT",bitwise_not)

cv.waitKey(0)