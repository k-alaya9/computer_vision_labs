import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')

def rescaleFrame (frame, scale=0.2):
    width= int(frame.shape[1]*scale)
    height= int (frame.shape[0]*scale)
    deminsions= (width, height)

    return cv.resize(frame, deminsions, interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('images', resized_image)
gray=cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#  1 Blur 
average_blur= cv.blur(gray, (3,3))
cv.imshow('Average Blur', average_blur)

gaussian_blur= cv.GaussianBlur(gray, (3,3), 0)
cv.imshow('Gaussian Image', gaussian_blur)

median_blur = cv.medianBlur(gray, 3)
cv.imshow('Median Blur', median_blur)

bilateral_blur = cv.bilateralFilter(gray,10,15,15)  
cv.imshow('Bilateral Blur', bilateral_blur)

#  2 Canny Edge
canny_edges_average = cv.Canny(gray,100,120)
cv.imshow('Canny Edges on Average Blur', canny_edges_average)

canny_edges_gaussian=cv.Canny(gaussian_blur,100,120)
cv.imshow('Canny Edges on Gaussian Blur',canny_edges_gaussian)

canny_edges_median=cv.Canny(median_blur,100,120)
cv.imshow('Canny Edges on Median Blur', canny_edges_median)

canny_edges_bilateral=cv.Canny(bilateral_blur,100,120)
cv.imshow('Canny Edges on Bilateral Blur', canny_edges_bilateral)


blur_image=cv.blur(gray,(3,3))
blur_image=cv.GaussianBlur(blur_image,(3,3),0)
cv.imshow("blur image",blur_image)

canny_edge=cv.Canny(blur_image,100,120)

cv.imshow("canny image on blur image ",canny_edge)

# 3 Morphological

# Erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(gray,kernel,iterations = 1)
cv.imshow('Erosion',erosion)

# dilation

dilation = cv.dilate(gray,kernel,iterations = 1)
cv.imshow('Dilation',dilation)

# open 
open_image = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel)
cv.imshow('Open', open_image)

# closing 
closing_image = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)
cv.imshow('Closing', closing_image)

# Gradient 
gradient_image = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
cv.imshow('Gradient', gradient_image)

# 4 Closing using bitwase or 
closing_image_bitwise = cv.bitwise_or(dilation,erosion)
cv.imshow('Closing using bitwise', closing_image_bitwise)


# 5 canny edges on Morphological images

canny_edge_gradient=cv.Canny(gradient_image,100,120)
cv.imshow('Canny Edges on Gradient', canny_edge_gradient)


cv.waitKey(0)