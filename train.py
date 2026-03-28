import os
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle

data = []
labels = []

dataset_path = "dataset"

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        
        data.append(img.flatten())
        labels.append(person)

data = np.array(data)
labels = np.array(labels)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(data, labels)

with open("models/face_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")