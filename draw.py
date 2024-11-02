import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
# cv.imshow('Blank',blank)

# paint the image with a color

blank[:]=255,255,0
cv.imshow('green',blank)
# # draw a shape with a color 
blank[200:300,300:400]=0,255,0
cv.imshow('shape',blank)

# draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
cv.imshow('rectangle',blank)

#draw circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow("circle",blank)

# draw line 

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=5)
cv.imshow("line",blank)

# write text
cv.putText(blank,"Hello World,",(0,255),cv.FONT_HERSHEY_PLAIN,1.0,(255,255,255))
cv.imshow("Text",blank)

cv.waitKey(0)
