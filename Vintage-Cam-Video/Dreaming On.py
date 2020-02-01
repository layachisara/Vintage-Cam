import cv2
import numpy as np

def dreaming_on(frame):
    mask = cv2.imread('Texture/texture-dream.jpg')
    mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
    dst = cv2.addWeighted(frame, 0.7, mask_resized, 0.4, 0)
    ## add sharpen
    Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output_sharpen = cv2.filter2D(dst, -1, Kernel)
    return output_sharpen

cap = cv2.VideoCapture('video-input/video-1.mp4')
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/dreaming-on.mp4', fourcc, 20.0, size)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = dreaming_on(frame)
        out.write(frame)
        cv2.imshow('Dreaming On', frame)
        #out.write(frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
