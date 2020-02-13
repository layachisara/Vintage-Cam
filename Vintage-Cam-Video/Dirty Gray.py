import cv2
import numpy as np

def dirty_gray(frame):
    ## gray filter
    output_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ## shrapening filter
    Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
    output_sharpen = cv2.filter2D(output_gray, -1, Kernel)
    return output_sharpen

# lettura video
cap = cv2.VideoCapture('video-input/video-1.mp4',0)
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/dirty-gray.mp4', fourcc, 20.0, size,0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # applica filtro
        frame = dirty_gray(frame)
        out.write(frame)
        cv2.imshow('Dirty Gray', frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()