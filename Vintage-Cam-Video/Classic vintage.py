import cv2
import numpy as np

def classic_vintage (frame):
    Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
    frame = cv2.filter2D(frame, -1, Kernel)
    return frame

# lettura video
cap = cv2.VideoCapture('video-input/video-1.mp4')
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/classic-vintage.mp4', fourcc, 20.0, size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    # applica filtro
        frame = classic_vintage(frame)
        cv2.imshow('Classic vintage', frame)
        out.write(frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
