import cv2
import numpy as np

# read image
input = cv2.imread('foto-input/foto-4.jpg')

# add blur
kernel = np.ones((4,4), np.float32) / 16
blur_img = cv2.filter2D(input, -1, kernel)

# add texture
mask = cv2.imread('Texture/texture-dust.jpg')
mask_resized = cv2.resize(mask, (blur_img.shape[1], blur_img.shape[0]))
output = cv2.addWeighted(blur_img, 0.7, mask_resized, 0.2, 0)

cv2.imshow('Sweet Dusty', output)
cv2.waitKey(0)
cv2.imwrite("foto-output/sweet-dusty.jpg",output)
cv2.destroyAllWindows()