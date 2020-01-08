import cv2
import numpy as np

#image = cv2.imread('Foto/mela vintage.jpg')
#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow('modified', hsv)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cap = cv2.VideoCapture('video/video4.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()