import cv2
import numpy as np
from PIL import Image

def seppia (frame):
    # Seppia matrix
    array = np.array(frame)
    seppiaMatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131] ])
    filter = cv2.transform(array, seppiaMatrix)
    # Check wich entries have a value greather than 255 and set it to 255
    filter[np.where(filter > 255)] = 255

    # Create an image from the array
    output: Image
    output = Image.fromarray(filter)

    #conversione da Pil a cv
    output_np = np.array(output)
    output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

    ## shrapening filter
    Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output_sharpen = cv2.filter2D(output_cv, -1, Kernel)
    return output_sharpen

    return output_sharpen

# lettura video
cap = cv2.VideoCapture('video-input/video-6.mp4')
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/classic-seppia.mp4', fourcc, 20.0, size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    # applica filtro
        frame = seppia(frame)
        out.write(frame)
        cv2.imshow('Classic seppia', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
