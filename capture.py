import cv2
import os

name = input("Enter your name: ")
dataset_path = "dataset/" + name

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot access camera")
    exit()
    
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

while True:
    ret, img = cam.read()
       
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]
        
        cv2.imwrite(f"{dataset_path}/{count}.jpg", face)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('Capturing Faces', img)
    
    if cv2.waitKey(1) == 27 or count >= 50:
        break

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break


cam.release()
cv2.destroyAllWindows()