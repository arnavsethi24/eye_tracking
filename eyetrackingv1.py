import cv2 
import numpy as np 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascase = cv2.CascadeClassifier('haarcascade_eye.xml')

img  = cv2.imread('face1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

def detect_eyes(img, img_gray, cascade):
    coords = cascade.detectMultiScale(img_gray, 1.3, 5)
    height = np.size(img, 0) # get face frame height
    for (x, y, w, h) in coords:
        if y+h > height/2: #
            pass


for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),2)
    gray_face = img_gray[y:y+h, x:x+w]
    face = img[y:y+h, x:x+w]
    eyes = eye_cascase.detectMultiScale(gray_face)
    for (ex,ey,ew,eh) in eyes: 
        cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)





cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
