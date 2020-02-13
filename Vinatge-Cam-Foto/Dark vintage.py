import cv2
import numpy as np

# read image
input = cv2.imread('foto-input/foto-7.jpg')

# apply dark vintage filter
# Gaussian filter
rows, cols = input.shape[:2]
kernel_x = cv2.getGaussianKernel(cols,170)
kernel_y = cv2.getGaussianKernel(rows,170)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage_im = np.copy(input)
# for each channel in the input image, we will apply the above filter
for i in range(3):
    vintage_im[:,:,i] = vintage_im[:,:,i] * filter

# add texture
mask = cv2.imread('Texture/blu-texture.jpg')
mask_resized = cv2.resize(mask, (vintage_im.shape[1], vintage_im.shape[0]))
dst = cv2.addWeighted(vintage_im, 0.7, mask_resized, 0.3, 0)

# covert to gray
gray_im= cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

cv2.imshow('Dark vintage', gray_im)
cv2.waitKey(0)
cv2.imwrite("foto-output/dark-vintage.jpg",gray_im)
cv2.destroyAllWindows()