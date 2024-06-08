# MAJOR CHANGES:
# This has Now Improved Counting Method and Can Count Simultaneously with the Bar-Percentage Working 
# Counting the Left and Right Hand Curls with Fps Counter
# When you Press "Esc" key on KeyBoard it Closes

# Future Feature:
# You Can add More Features Later Like Time to Time Health Checks in The Computer to Stay Fit and Healthy


import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count_left = 0
count_right = 0
dir_left = 0
dir_right = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Right Arm
        angle_right = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        angle_left = detector.findAngle(img, 11, 13, 15)

        per = np.interp(angle_right, (210, 310), (0, 100))
        bar = np.interp(angle_right, (220, 310), (650, 100))

        # Apply hysteresis for right arm
        if angle_right > 310:
            if dir_right == 0:
                count_right += 0.5
                dir_right = 1
        elif angle_right < 210:
            if dir_right == 1:
                count_right += 0.5
                dir_right = 0

        # Apply hysteresis for left arm
        if angle_left > 150:
            if dir_left == 0:
                count_left += 0.5
                dir_left = 1
        elif angle_left < 50:
            if dir_left == 1:
                count_left += 0.5
                dir_left = 0

        # Draw Bar for right arm
        color = (255, 0, 255)
        bar_right = np.interp(angle_right, (210, 310), (650, 100))
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar_right)), (1175, 650), color, cv2.FILLED)

        # Display curl count for right arm
        cv2.putText(img, "Right: " + str(int(count_right)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 15)

        # Display curl count for left arm
        cv2.putText(img, "Left: " + str(int(count_left)), (45, 620), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 15)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (50, 150), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    
    # Check for the "Esc" key press to close the window
    key = cv2.waitKey(1)
    if key == 27:  # "Esc" key
        break

cap.release()
cv2.destroyAllWindows()