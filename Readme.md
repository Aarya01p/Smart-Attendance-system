# Smart Attendance System using Computer Vision

##  Problem Statement
Manual attendance systems are time-consuming and prone to errors. This project automates attendance using face recognition.

## Features
- Face detection using OpenCV
- Face recognition using KNN
- Automatic attendance marking
- Real-time webcam processing

## Technologies Used
- Python
- OpenCV
- NumPy
- Scikit-learn

## Installation

1. Install dependencies:
pip install opencv-python numpy scikit-learn

2. Run capture.py to collect images
3. Run train.py to train model
4. Run recognize.py to start attendance

## Output
Attendance is stored in:
attendance/attendance.csv

## Future Improvements
- GUI interface
- Deep learning models
- Cloud storage

## Working
The Smart Attendance System follows a structured pipeline to automate attendance using computer 
vision. First, the system captures face images of users through a webcam and stores them in a 
dataset. These images are then preprocessed by converting them to grayscale and resizing them for 
consistency. During the training phase, the stored images are used to train a K-Nearest Neighbors 
(KNN) classifier, which learns to recognize different individuals based on facial features. In the 
recognition phase, the system again captures real-time video, detects faces using OpenCV’s Haar 
Cascade classifier, and compares them with the trained model to identify the person. Once a face is 
successfully recognized, the system records the individual’s name along with the current date and 
time into a CSV file, thereby marking attendance automatically. This end-to-end process eliminates 
manual effort and ensures a fast and reliable attendance mechanism.