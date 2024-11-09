import cv2 as  cv
import numpy as np
import mediapipe as mdp 
faceshape = mdp.solutions.face_mesh
face = faceshape.FaceMesh(static_image_mode = True, min_tracking_confidence = 0.7, min_detection_confidence=0.7)
draw = mdp.solutions.drawing_utils
cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv.flip(frame, flipCode=1)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    matrix = np.zeros(shape=(480,640,3), dtype=np.uint8)
    image = face.process(frame)
    if image.multi_face_landmarks:
        for i in image.multi_face_landmarks:
            draw.draw_landmarks(matrix,i, faceshape.FACEMESH_CONTOURS, landmark_drawing_spec=draw.DrawingSpec(color=(255,255,0), thickness=1))
    cv.imshow('face_landmark', matrix)
    facee=cv.cvtColor(frame.copy(), cv.COLOR_RGB2BGR)
    cv.imshow("face",facee)
    if cv.waitKey(1) == ord('q'):
        cap.release()
        cv.destroyAllWindows()