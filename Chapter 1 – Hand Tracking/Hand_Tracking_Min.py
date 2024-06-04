# Hand Tracking - Basics

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

# Hand Detection module
mpHands = mp.solutions.hands
# Creating a object called hands
# We Can wrtite this as False (!OPTIONAL! -> We have to Give paramenters in the "Hands()")
# Initially it is set to False To improve Efficiency and not Keep Tracking all the time
# Refer The Method Online
hands = mpHands.Hands()

# Function/Method
mpDraw = mp.solutions.drawing_utils

# FPS
pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # Sending a RGB IMAGE TO OUR OBJECT AS IT ONLY ACCEPTS/USES RBG IMAGE
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) # Gives us Just the Media base Solution Endlessly
    # print(results.multi_hand_landmarks) # To Check if Something is Detected or not use the provided Method

    if results.multi_hand_landmarks:
        # Extracting info of Each hand
        for handLms in results.multi_hand_landmarks:
            # Getting the info of Each hand and Landmark info (all we have to do is check the index number)
            for id, lm in enumerate(handLms.landmark): # Already listed in Correct Order
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy) # Id of the point on the hand and its position on the Screen
                if id == 0: # For Thumb
                    cv2.circle(img, (cx, cy), 25, (225, 0, 225), cv2.FILLED)


            # Inserting a Function/Method by mediapipeto Check the Distance Between points there are total 21 in total in one Hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow('MediaPipe Pose', img)
    cv2.waitKey(1)