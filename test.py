from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
import pyttsx3

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load video capture and face detection model
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Load pre-trained data for faces and labels
try:
    with open('data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)
except FileNotFoundError:
    print("Pre-trained data not found. Ensure 'data/names.pkl' and 'data/faces_data.pkl' exist.")
    exit()

# Validate data consistency
if FACES.shape[0] != len(LABELS):
    min_samples = min(FACES.shape[0], len(LABELS))
    FACES = FACES[:min_samples]
    LABELS = LABELS[:min_samples]

print('Shape of Faces matrix --> ', FACES.shape)
print('Number of Labels --> ', len(LABELS))

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Load background image for display
imgBackground = cv2.imread("background.png")
if imgBackground is None:
    print("Background image not found. Ensure 'background.png' exists.")
    exit()

COL_NAMES = ['NAME', 'TIME']
os.makedirs("Attendance", exist_ok=True)  # Ensure Attendance folder exists

# Main loop for face recognition and attendance logging
while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to capture video frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)

        try:
            output = knn.predict(resized_img)
        except Exception as e:
            print("Error during prediction:", e)
            continue

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        file_path = f"Attendance/Attendance_{date}.csv"

        # Display rectangle and name on the video frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        # Prepare attendance record
        attendance = [str(output[0]), str(timestamp)]

        # Handle attendance logging
        if cv2.waitKey(1) == ord('o'):
            speak("Attendance Marked.")
            if not os.path.isfile(file_path):
                with open(file_path, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)  # Write column headers
                    writer.writerow(attendance)
            else:
                with open(file_path, "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(attendance)

    # Resize frame to fit the background dimensions
    frame_resized = cv2.resize(frame, (640, 480))
    imgBackground[162:162 + 480, 55:55 + 640] = frame_resized

    cv2.imshow("Frame", imgBackground)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        print("Exiting...")
        break

# Release resources
video.release()
cv2.destroyAllWindows()
