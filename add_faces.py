import cv2
import pickle
import numpy as np
import os

# Initialize video capture and face detector
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0

# Input for user's name
name = input("Enter Your Name: ")

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50))

        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resized_img)

        i += 1
        cv2.putText(frame, f"Samples: {len(faces_data)}/100", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q') or len(faces_data) == 100:
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()

# Convert collected face data to numpy array and reshape
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(len(faces_data), -1)

# Save name and faces data to files
names_file = 'data/names.pkl'
faces_file = 'data/faces_data.pkl'

if not os.path.isfile(names_file):
    names = [name] * len(faces_data)
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)
else:
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
    names += [name] * len(faces_data)
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)

if not os.path.isfile(faces_file):
    with open(faces_file, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open(faces_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open(faces_file, 'wb') as f:
        pickle.dump(faces, f)

print("Data collection completed and saved.")
