import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("Images\horse.png",0)
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)
cv.imshow("skel--", skel)
ret, img = cv.threshold(img, 127,255, 0)
cv.imshow("img", img)
element =cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
done = False
while (not done):
    eroded = cv.erode(img, element)
    temp = cv.dilate(eroded, element)
    temp = cv.subtract(img, temp)
    skel = cv.bitwise_or(skel, temp)
    img = eroded.copy()
    zeros = size - cv.countNonZero(img)
    if zeros == size:
        done = True
cv.imshow("skel", skel)

f = cv.imread('Images/rubik.png',0)
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()
# image in frequency domain
F = np.fft.fft2(f)
plt.imshow(np.log1p(np.abs(F)), cmap='gray')
plt.axis('off')
plt.show()
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')
plt.show()
cv.waitKey(0)

# original image
f = cv.imread('rubik.png',0)
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()
# image in frequency domain
F = np.fft.fft2(f)
plt.imshow(np.log1p(np.abs(F)), cmap='gray')
plt.axis('off')
plt.show()
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')
plt.show()

# Filter: Low pass filter
M,N = f.shape
mask = np.zeros((M,N))
D0 = 50
circle = cv2.getStructuringElement(cv.MORPH_ELLIPSE,(D0, D0))
center_h = M//2
center_w = N//2
h_r = D0 //2
mask[center_h - h_r:center_h + h_r ,center_w - h_r:center_w + h_r] = circle.copy()
plt.imshow(mask, cmap='gray')
plt.axis('off')
plt.show()

