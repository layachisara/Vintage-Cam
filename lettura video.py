import cv2

cap = cv2.VideoCapture('video/video4.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    # applica filtro
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()