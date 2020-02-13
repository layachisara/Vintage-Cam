import cv2
import numpy as np

def dark_vintage (frame):
    # apply dark vintage filter
    # Gaussian filter
    rows, cols = frame.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    filter = 255 * kernel / np.linalg.norm(kernel)
    vintage_im = np.copy(frame)
    # for each channel in the input image, we will apply the above filter
    for i in range(3):
        vintage_im[:, :, i] = vintage_im[:, :, i] * filter

    # add texture
    mask = cv2.imread('Texture/blu-texture.jpg')
    mask_resized = cv2.resize(mask, (vintage_im.shape[1], vintage_im.shape[0]))
    dst = cv2.addWeighted(vintage_im, 0.7, mask_resized, 0.2, 0)

    # covert to gray
    gray_im = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    return gray_im

# lettura video
cap = cv2.VideoCapture('video-input/video-4.mp4',0)
width_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width_frame,height_frame)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv2.VideoWriter('video-output/dark-vintage.mp4', fourcc, 20.0, size,0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    # applica filtro
        frame = dark_vintage(frame)
        cv2.imshow('Dark vintage', frame)
        out.write(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
