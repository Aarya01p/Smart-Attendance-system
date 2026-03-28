import cv2
import numpy as np
import pickle
import csv
from datetime import datetime

# Load model
with open("models/face_model.pkl", "rb") as f:
    model = pickle.load(f)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot access camera")
    exit()

def mark_attendance(name):
    with open("attendance/attendance.csv", "a", newline='') as f:
        writer = csv.writer(f)
        now = datetime.now()
        writer.writerow([name, now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d")])

marked = set()

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100)).flatten().reshape(1, -1)
        
        name = model.predict(face)[0]
        
        if name not in marked:
            mark_attendance(name)
            marked.add(name)
        
        cv2.putText(img, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Attendance System", img)
    
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break


cam.release()
cv2.destroyAllWindows()