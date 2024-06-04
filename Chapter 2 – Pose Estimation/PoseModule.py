# import cv2
# import mediapipe as mp
# import time


# class poseDetector():
#     def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.upBody = upBody
#         self.smooth = smooth
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon


#         self.mpDraw = mp.solutions.drawing_utils
#         self.mpPose = mp.solutions.pose
#         self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, 
#                                      self.detectionCon, self.trackCon)
        
#     # Create a Method to Find a Pose
#     def findPose(self, img, draw=True): # Asks the user to Draw or not?

#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = self.pose.process(imgRGB)
#         if results.pose_landmarks:
#             if draw:
#                 self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

#         return img
    

#     def findPosition(self, img, draw=True):
#         lmList = []
#         if self.results.pose_landmarks:
#             for id, lm in enumerate(self.results.pose_landmarks.landmark):
#                 h, w, c = img.shape
#                 print(id, lm)
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 5, (225, 0, 0), cv2.FILLED)
#         return lmList



# def main():
#     cap = cv2.VideoCapture('Badtameez Dil  Easy Dance Choreography  Nayan Rathod  Surat.mp4')
#     pTime = 0
#     detector = poseDetector()

#     while True:
#         success, img = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             break
#         img = detector.findPose(img)
#         lmList = detector.findPosition(img, draw=False)
#         if lmList:
#             print(lmList[14])  # print first landmark for debugging

#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime

#         cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     main()








import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, 
                             model_complexity=1 if self.upBody else 0, 
                             smooth_landmarks=self.smooth, 
                             min_detection_confidence=self.detectionCon, 
                             min_tracking_confidence=self.trackCon)

        self.results = None
        
    def findPose(self, img, draw=True): 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results and self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture('Badtameez Dil  Easy Dance Choreography  Nayan Rathod  Surat.mp4')
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            print(lmList[14])  # print first landmark for debugging

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
