import cv2
import numpy as np

# read image
input = cv2.imread('foto-input/foto-2.jpg')

# add BLURRING: image blurring is achieved by convolving the image with a low-pass filter kernel.
# It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image.
# So edges are blurred a little bit in this operation (there are also blurring techniques which don't blur the edges).
#blur = cv2.GaussianBlur(input,(13,13),cv2.BORDER_DEFAULT)
Kernel = np.ones((4, 4), np.float32) / 16
blur_img = cv2.filter2D(input, -1, Kernel)

mask = cv2.imread('Texture/polaroid-texture.jpg')
mask_resized = cv2.resize(mask, (blur_img.shape[1], blur_img.shape[0]))
out = cv2.addWeighted(blur_img, 0.7, mask_resized, 0.5, 0)

# create an image with a single color (red)
red_img  = np.full((682,512,3), (0,0,150), np.uint8)
mask_resized = cv2.resize(red_img, (out.shape[1], out.shape[0]))

# add the filter  with a weight factor of 20% to the target image
fused_img  = cv2.addWeighted(out, 0.8, mask_resized, 0.2, 0)
WHITE = [255,255,255]
white_border_img = cv2.copyMakeBorder(fused_img, 60,60,20,20, cv2.BORDER_CONSTANT, value=WHITE)

# add text
position = (120,700)
cv2.putText(
     white_border_img, #numpy array on which text is written
     "Happy Birthday", #text
     position, #position at which writing has to start
     cv2.FONT_HERSHEY_SIMPLEX, #font family
     1, #font size
     (0, 0, 0, 0), #font color
     3) #font stroke

cv2.imshow("Polaroid", white_border_img)
cv2.waitKey(0)
cv2.imwrite("foto-output/polaroid.jpg",white_border_img)
cv2.destroyAllWindows()