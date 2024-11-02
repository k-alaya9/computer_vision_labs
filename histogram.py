import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np


img=cv.imread("Images/eye.jpg")
blank=np.zeros(img.shape[:2],dtype='uint8')
# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("image",img)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow("masked",masked)
# gray_hist=cv.calcHist([masked],[0],None,[256],[0,256])

plt.figure()
# plt.title("gray scale histogram")
# plt.xlabel("bins")
# plt.ylabel("number of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
color=('b','g','r')
for i,col in enumerate(color):
    color_hist=cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(color_hist,color=col)
    plt.xlim([0,256])
    plt.title("color histogram")
    plt.xlabel("bins")
    plt.ylabel("number of pixels")
plt.show()

cv.waitKey(0)
