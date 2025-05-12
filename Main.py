# Step 1: Install dependencies
!pip install opencv-python-headless

# Step 2: Upload video file
from google.colab import files
uploaded = files.upload()

# Step 3: Import libraries and process video
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Get uploaded file name
video_path = list(uploaded.keys())[0]

# Open video
cap = cv2.VideoCapture(video_path)

# Sample parking spot coordinates (adjust as per your video)
# Format: (x, y, width, height)
parking_spots = [
    (100, 50, 40, 80),
    (200, 50, 40, 80),
    (300, 50, 40, 80),
]

def check_occupancy(spot_img, threshold=900):
    gray = cv2.cvtColor(spot_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    _, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)
    non_zero = cv2.countNonZero(binary)
    return non_zero > threshold

# Read first frame for demo
ret, frame = cap.read()
if ret:
    for i, spot in enumerate(parking_spots):
        x, y, w, h = spot
        roi = frame[y:y+h, x:x+w]
        occupied = check_occupancy(roi)
        color = (0, 0, 255) if occupied else (0, 255, 0)
        label = "Occupied" if occupied else "Free"
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2_imshow(frame)
else:
    print("Failed to read video.")

cap.release()
