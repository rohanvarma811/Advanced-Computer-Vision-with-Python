import cv2
import mediapipe as mp
import time


mpPose = mp.solutions.pose

# Creating a Object
# When the static_image_mode=False 
# When u keep it False 
# And when the Confidence is High it will keep Tracking
# if its Goes above 0.5 it Tracks and if its Below 0.5 it Goes to Detection

# When you are Detecting and Tracking
# When True it will always Detect based on Model
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()



cap = cv2.VideoCapture('Badtameez Dil  Easy Dance Choreography  Nayan Rathod  Surat.mp4')
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy) # Id of the point on the hand and its position on the Screen
            cv2.circle(img, (cx, cy), 5, (225, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3, (225,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)