import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Images\home.jpg')
rows,cols,depth = img.shape
pts1 =np.float32([[50,50],[200,50],[50,200]])
pts2 =np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('dst',dst)
cv.waitKey(0)

img = cv.imread('Images\sudoku.jpg')
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv.getPerspectiveTransform(pts1,pts2)
dst=cv.warpPerspective(img,M,(img.shape[1],img.shape[0]))
cv.imshow('dst',dst)
cv.waitKey(0)

img = cv.imread("Images\home.jpg")
cv.imshow("Image",img)
color = ('b','g','r')
for i,col in enumerate(color):
    histr=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


image = cv.imread("Images\home.jpg",0)
cv.imshow("Image",image)
Image_equ = cv.equalizeHist(image)
cv.imshow("Image_equalized", Image_equ)
cv.waitKey(0)

image =cv.imread("Images\home.jpg")
cv.imshow("orginal image",image)
blur=cv.blur(image,(7,7))
cv.imshow("blur images",blur)
cv.waitKey(0)

image=cv.imread("Images\home.jpg")
cv.imshow("orginal image",image)

gBlur=cv.GaussianBlur(image,(7,7),10)
cv.imshow("Gaussian Blur",gBlur)
cv.waitKey(0)


image=cv.imread("Images\home.jpg")
cv.imshow("orginal image",image)

mBlur=cv.medianBlur(image,5)
cv.imshow("Median Blur",mBlur)
cv.waitKey(0)

