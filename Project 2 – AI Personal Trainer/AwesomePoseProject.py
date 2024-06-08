# Baisc Project that you can integrate this Feature

import cv2
import time
import PoseModule as pm


cap = cv2.VideoCapture('Badtameez Dil  Easy Dance Choreography  Nayan Rathod  Surat.mp4')
pTime = 0
detector = pm.poseDetector()

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