import cv2 as cv



def rescale_frame(frame,scale=0.75):
    #images , videos, live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def chanageRes(width,height):
    #live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('Images/test.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow("video",frame)
    resized_frame=rescale_frame(frame)
    cv.imshow("resized video",resized_frame) 

    if cv.waitKey(20) & 0xFF==ord('p'):
        break

capture.release()
cv.destroyAllWindows()