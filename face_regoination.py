import numpy as np 
import cv2 as cv 

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling', 'sydney sweeney']
haar_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recoginzer=cv.face.LBPHFaceRecognizer_create()
face_recoginzer.read("face_trained.yml")

img=cv.imread("Faces/val/sydney sweeney/GettyImages-1864388767.jpg")
img=cv.resize(img,(900,500))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Face",gray)

#Detect face

faces_react=haar_cascade.detectMultiScale(gray,1.1,10)

for (x,y,h,w) in faces_react:
    face_roi=gray[y:y+h,x:x+w]

    label,conf=face_recoginzer.predict(face_roi)
    print(f"Label={people[label]} Conf={conf}")
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("detected face",img)
cv.waitKey(0)