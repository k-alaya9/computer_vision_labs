import os 
import cv2 as cv
import numpy as np 

p=[]
DIR=r"C:\Users\HP\Documents\AI projects\Faces\train"
haar_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")

for i in os.listdir(DIR):
    p.append(i)
print(p)
featuers=[]
labels=[]
def create_train():
    for person in p:
        path=os.path.join(DIR,person)
        label=p.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(gray,1.1,4)
            for (x,y,w,h) in face_rect:
                roi_gray=gray[y:y+h,x:x+w]
                featuers.append(roi_gray)
                labels.append(label)

create_train()

featuers=np.array(featuers,dtype="object")
labels=np.array(labels)
face_recoginzer=cv.face.LBPHFaceRecognizer_create()
face_recoginzer.train(featuers,labels)

face_recoginzer.save('face_trained.yml')
np.save('features.npy', featuers)
np.save('labels.npy', labels)