import cv2 as cv


img=cv.imread("Images/home.jpg")
cv.imshow("image",img)

# Average Bluring 
average=cv.blur(img,(3,3))
cv.imshow("Average Bluring",average)

# gaussian bluring
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Bluring",gauss)

# Meadin bluring 
median=cv.medianBlur(img,3)
cv.imshow("Median Bluring",median)

# Bit bluring
bit=cv.bilateralFilter(img,10,15,15)
cv.imshow("Bit Bluring",bit)
cv.waitKey(0)