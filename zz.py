import cv2

CAMERA_URL = "http://192.168.18.18:8080/video"
cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("❌ Cannot connect to camera.")
else:
    print("✅ Connected successfully!")
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Test Stream", frame)
        cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
