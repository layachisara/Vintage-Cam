import cv2
import numpy as np
from PIL import Image

def stile_retro(frame):
    ## SEPPIA FILTER
    array = np.array(frame)
    seppiaMatrix = np.array([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168],[0.272, 0.534, 0.131]])
    filter = cv2.transform(array, seppiaMatrix)
    # Check wich entries have a value greather than 255 and set it to 255
    filter[np.where(filter > 255)] = 255
    output_pil: Image
    output_pil = Image.fromarray(filter)
    output_np = np.array(output_pil)
    output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)
    # sherpening
    Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
    output_sherpen = cv2.filter2D(output_cv, -1, Kernel)
    return output_sherpen

# lettura video
cap = cv2.VideoCapture('video-input/video-2.mp4')
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object.
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/stile-retro.mp4', fourcc, 20.0, size)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    # applica filtro
        frame = stile_retro(frame)
        out.write(frame)
        cv2.imshow('Stile retro', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
