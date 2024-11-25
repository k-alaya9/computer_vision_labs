import cv2 as cv 
import matplotlib.pyplot as plt 
# img= cv.imread('Images\home.jpg',0)
# plt.imshow(img,cmap='gray')
# plt.axis('off')
# plt.show()

# dim=img.shape

# res=cv.resize(img,(int(dim[1]*2),int(dim[0]*2)),interpolation=cv.INTER_CUBIC)

# plt.imshow(res,cmap='gray')
# plt.axis('off')
# plt.show()
# print(res.shape)
img= cv.imread('Images\home.jpg')
lower_reso = cv.pyrDown(img)
upper_reso = cv.pyrUp(img)
cv.imshow('base_reso',img)
cv.imshow('lower_reso',lower_reso)
cv.imshow('upper_reso',upper_reso)
cv.waitKey(0)
