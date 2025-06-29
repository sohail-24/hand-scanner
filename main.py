import os
import cv2
import mediapipe as mp
import numpy as np

# Load template and video
template_path = 'hand_template.png'
video_path = 'vid.mp4'

template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
if template is None:
    raise FileNotFoundError(f"Template image not found at: {template_path}")

template_h, template_w = template.shape[:2]

# ✅ Check if webcam exists
if not os.path.exists('/dev/video0'):
    print("⚠️ No webcam detected. Skipping camera-dependent part.")
    # Just preview the video as a test
    video = cv2.VideoCapture(video_path)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow('Hand Scanner Demo (No Webcam)', frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()
    exit(0)

# If webcam exists, continue with scanner
cap = cv2.VideoCapture(0)

# Rest of your hand detection logic follows...

