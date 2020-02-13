import cv2
import numpy as np

def dirty_gray(frame):
    ## gray filter
    output_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ## shrapening filter
    Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
    output_sharpen = cv2.filter2D(output_gray, -1, Kernel)

    return output_sharpen

mask_filter= cv2.VideoCapture('Texture/old-tv-texture.mp4',0)
cap = cv2.VideoCapture('video-input/video-6.mp4')
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/old-tv.mp4', fourcc, 20.0, size,0)
while cap.isOpened():
    ret, frame = cap.read()
    ret1, frame1 = mask_filter.read()
    if ret == True and ret1 == True:
        h, w, c = frame.shape
        h1, w1, c1 = frame1.shape
        # adapt the mask to the video
        if h != h1 or w != w1:
            frame1 = cv2.resize(frame1, (w, h))
        both = cv2.addWeighted(frame, 0.9, frame1, 0.4, 0)
        output = dirty_gray(both)
        cv2.imshow('Old film', output)
        out.write(output)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
mask_filter.release()
cv2.waitKey(0)
cv2.destroyAllWindows()