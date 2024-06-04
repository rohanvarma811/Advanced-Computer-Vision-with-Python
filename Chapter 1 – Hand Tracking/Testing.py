import cv2
import mediapipe as mp
import time

# (Optional) Set up a drawing utility for MediaPipe solutions
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# (Replace with your desired MediaPipe solution)
mp_pose = mp.solutions.pose  # For pose estimation
# mp_hands = mp.solutions.hands  # For hand tracking


# Hand Detection module
mpHands = mp.solutions.hands
# Creating a object called hands
# We Can wrtite this as False (!OPTIONAL! -> We have to Give paramenters in the "Hands()")
# Initially it is set to False To improve Efficiency and not Keep Tracking all the time
# Refer The Method Online
hands = mpHands.Hands()


# Initialize video capture
cap = cv2.VideoCapture(0)  # 0 for default webcam

while cap.isOpened():
    success, image = cap.read()

    # Sending a RGB IMAGE TO OUR OBJECT AS IT ONLY ACCEPTS/USES RBG IMAGE
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if not success:
        print("Ignoring empty camera frame.")
        continue

    # (Replace with your MediaPipe solution processing)
    # results = mp_pose.process(image)  # For pose estimation
    # mp_drawing.draw_landmarks(image, results.pose_landmarks,
    #                           mp_pose.POSE_CONNECTIONS,
    #                           mp_drawing_styles.get_default_pose_style())

    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:  # Press Esc to quit
        break

cap.release()
