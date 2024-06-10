# # PROBLEM FIXED : adjusted the beep duration to 1000 milliseconds for a longer alert sound, modified the beeping logic to ensure continuous beeping as long as the eye closure persists.

# UPDATES : THIS IS A PC VERSION WITH A WEBCAM OF HIGHER RESOLUTION

import cv2
import cvzone
import time
import os
from playsound import playsound
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

# Function to play alert sound
def play_alert_sound(audio_path):
    try:
        playsound(audio_path)
    except Exception as e:
        print(f"Error playing alert sound: {e}")

# Capture video from the first camera (0 usually refers to the built-in webcam)
cap = cv2.VideoCapture(0)

# Initialize FaceMeshDetector from cvzone with a maximum of 1 face
detector = FaceMeshDetector(maxFaces=1)

# Create a LivePlot object to plot the blinking ratio
plotY = LivePlot(640, 360, [30, 50], invert=True)

# List of facial landmark IDs related to the eyes
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []  # List to keep track of the blinking ratios
blinkCounter = 0  # Counter to track the number of blinks
color = (255, 0, 255)  # Initial color for the text
alert_threshold = 2  # Threshold in seconds to trigger alert
last_blink_time = time.time()  # Time of the last blink

# Get the path to the alert audio file
alert_audio_path = os.path.join(os.getcwd(), 'Windows 10 Notification Sound.mp3')  # Ensure this file exists

while True:
    # Reset the video frame position if it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()  # Read a frame from the camera
    img, faces = detector.findFaceMesh(img, draw=False)  # Detect face mesh without drawing landmarks

    if faces:
        face = faces[0]
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lengthVer, _ = detector.findDistance(leftUp, leftDown)
        lengthHor, _ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        ratio = int((lengthVer / lengthHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)

        if ratioAvg < 38:
            blinkCounter += 1
            current_time = time.time()
            if current_time - last_blink_time >= alert_threshold:
                play_alert_sound(alert_audio_path)
                last_blink_time = current_time  # Reset the timer after alert
        else:
            last_blink_time = time.time()

        color = (0, 200, 0) if ratioAvg < 35 else (255, 0, 255)

        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100), colorR=color)

        imgPlot = plotY.update(ratioAvg, color)
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
    else:
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, img], 2, 1)

    cv2.imshow("Image", imgStack)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()