import cv2 as cv 

img= cv.imread("Images/ronaldo.jpg")

cv.imshow("basic",img)

# gray image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

# Blur
blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

# Edge Cascade

canny=cv.Canny(img,125,175)
cv.imshow("canny Edges",canny)


#dialting the image


dialted=cv.dilate(canny,(7,7),iterations=3)

cv.imshow("dialted",dialted)


# Eroding 
eroded=cv.erode(dialted,(7,7),iterations=3)
cv.imshow("eroded",eroded)

# Resize

resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)

# cropping 
cropped=img[50:200,100:200]
cv.imshow("cropped",cropped)

cv.waitKey(0)