# Feature Working Plays a Sound When the Eyes is Closed and the Graph is in -ve Area 

# NOTE: THE BLINKING MAY NOT BE ACCURATE DUE TO LACK OF BRIGHTNESS AND OTHER FACTORS LIKE EYE-SIZE AND EVEN MORE. 
# THAT SHOULD BE CONSIDERED AND OPTIMISED FURTHER ACCORDINGLY IN THE FUTURE DRIVING UPDATES FOR THE SAFETY FOR THE DRIVER

# import cv2
# import cvzone
# import winsound
# import time
# from cvzone.FaceMeshModule import FaceMeshDetector
# from cvzone.PlotModule import LivePlot

# cap = cv2.VideoCapture(0)
# detector = FaceMeshDetector(maxFaces=1)
# plotY = LivePlot(640, 360, [20, 50], invert=True)

# idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
# ratioList = []
# blinkCounter = 0
# color = (255, 0, 255)
# alert_sound_played = False
# alert_threshold = 3  # Threshold in seconds to trigger alert
# last_blink_time = time.time()

# while True:
#     if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

#     success, img = cap.read()
#     img, faces = detector.findFaceMesh(img, draw=False)

#     if faces:
#         face = faces[0]
#         leftUp = face[159]
#         leftDown = face[23]
#         leftLeft = face[130]
#         leftRight = face[243]
#         lenghtVer, _ = detector.findDistance(leftUp, leftDown)
#         lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

#         cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
#         cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

#         ratio = int((lenghtVer / lenghtHor) * 100)
#         ratioList.append(ratio)
#         if len(ratioList) > 3:
#             ratioList.pop(0)
#         ratioAvg = sum(ratioList) / len(ratioList)

#         if ratioAvg < 35:
#             blinkCounter += 1
#             current_time = time.time()
#             if current_time - last_blink_time >= alert_threshold and not alert_sound_played:
#                 winsound.Beep(1000, 500)
#                 alert_sound_played = True
#         else:
#             last_blink_time = time.time()
#             alert_sound_played = False

#         cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100),
#                            colorR=color)

#         imgPlot = plotY.update(ratioAvg, color)
#         img = cv2.resize(img, (640, 360))
#         imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
#     else:
#         img = cv2.resize(img, (640, 360))
#         imgStack = cvzone.stackImages([img, img], 2, 1)

#     cv2.imshow("Image", imgStack)
#     cv2.waitKey(25)

