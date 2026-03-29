Smart Attendance System using Computer Vision
 Project Overview

The Smart Attendance System is a computer vision-based application that automates the process of marking attendance using face recognition. Instead of manually recording attendance, the system uses a webcam to detect and recognize faces in real time and automatically logs attendance with date and time.

This project is built using Python, OpenCV, and machine learning techniques, and demonstrates a practical real-world application of computer vision.

Problem Statement

Traditional attendance methods:

Take a lot of time
Can be manipulated (proxy attendance)
Require manual effort

This project solves these issues by automating attendance using face recognition.

 Objectives
Detect faces using a webcam
Recognize individuals using a trained model
Automatically mark attendance
Maintain digital records
Support multiple users
 Features
 Real-time face detection
 Face recognition using KNN
 Supports multiple users
 Automatic attendance logging
 Easy to use and extend
 Technologies Used
Python
OpenCV
NumPy
Scikit-learn (KNN Algorithm)
CSV (for storing attendance)
📁 Project Structure
Smart-Attendance-System/
│
├── dataset/                # Stores face images
├── models/                 # Stores trained model
├── attendance/             # Stores attendance file
│   └── attendance.csv
│
├── capture.py              # Capture face images
├── train.py                # Train model
├── recognize.py            # Recognize & mark attendance
│
├── README.md

 How the Project Works

The system follows three main steps:

1. Capture Images
Uses webcam to capture face images
Stores images in dataset folder under user name
2. Train Model
Reads all images
Trains a KNN model
Saves model as face_model.pkl
3. Recognize & Mark Attendance
Detects faces in real-time
Matches with trained model
Saves attendance in CSV file
 Installation & Setup

Follow these steps carefully:

1. Clone the Repository
git clone <your-repo-link>
cd Smart-Attendance-System
2. Install Required Libraries
pip install opencv-python numpy scikit-learn
3.Create Required Folders

Make sure these folders exist:

dataset/
models/
attendance/

Create attendance file:

attendance/attendance.csv
 How to Run the Project
 Step 1: Capture Face Images
python capture.py
Enter your name
Webcam opens
Capture ~50 images
Press ESC to close
 Step 2: Train the Model
python train.py
Model will be trained
File saved in models/face_model.pkl
 Step 3: Start Attendance System
python recognize.py
Webcam opens
Face is detected and recognized
Attendance is recorded automatically
Press ESC to exit
 Output

Attendance is saved in:

attendance/attendance.csv

Example:

Aarya,10:45:12,2026-03-28
Rohan,10:47:03,2026-03-28
 Important Notes
Capture images for each person separately
Run train.py after adding new users
Ensure good lighting for better accuracy
Camera should not be used by other apps
 Common Errors & Fixes
Camera not opening
Try changing camera index:
cv2.VideoCapture(0)
cv2.VideoCapture(1)
Model file not found
Run:
python train.py
Attendance file error
Ensure:
attendance/attendance.csv exists
 Future Improvements
GUI interface
Deep learning-based face recognition
Cloud storage
Mobile app integration
Mask detection
Conclusion

This project successfully demonstrates how computer vision can automate attendance systems. It reduces manual effort, improves accuracy, and provides a scalable and efficient solution.
