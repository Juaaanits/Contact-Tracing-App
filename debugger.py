import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)

    key = cv2.waitKey(30) & 0xFF
    print(f"Key pressed: {key}")  # debug print
    if key == ord('q'):
        print("Q pressed, exiting...")
        break

cap.release()
cv2.destroyAllWindows()
