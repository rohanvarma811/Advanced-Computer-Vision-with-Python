import cv2
import mediapipe as mp
import time

# Initialize video capture
cap = cv2.VideoCapture("Free people expression footage  mad shocked surprised wow amazed face    NO COPYRIGHT VIDEOS.mp4")
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

pTime = 0

# Initialize Mediapipe FaceMesh
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame from video file.")
        break
    
    # Reduce the resolution of the image
    img = cv2.resize(img, (640, 480))

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            try:
                mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)
            except Exception as e:
                print(f"Error in drawing landmarks: {e}")
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                print(id, x, y)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
