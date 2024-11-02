import cv2 as cv 


capture=cv.VideoCapture(0)
haar_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    isTrue,frame=capture.read()
    # cv.imshow("video",frame)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    face_rect=haar_cascade.detectMultiScale(gray,1.1,6)
    print(f"number of faces found {len(face_rect)}")

    for (x,y,w,h) in face_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow("detect",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# img=cv.imread("Images/eye.jpg")
# cv.imshow("person",img)
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
# haar_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# face_rect=haar_cascade.detectMultiScale(gray,1.1,3)
# print(f"number of faces found {len(face_rect)}")

# for (x,y,w,h) in face_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imshow("detect",img)

# haar_cascade_eye=cv.CascadeClassifier("haarcascade_eye.xml")
# eye_rect=haar_cascade_eye.detectMultiScale(gray,1.1,3)
# print(f"number of eyes found {len(eye_rect)}")
# for (x,y,w,h) in eye_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imshow("eye detect",img)
# cv.waitKey(0)