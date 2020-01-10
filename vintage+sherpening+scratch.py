import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

input = cv2.imread('foto/mele.jpg')
rows, cols = input.shape[:2]

# Create a Gaussian filter
kernel_x = cv2.getGaussianKernel(cols, 400)
kernel_y = cv2.getGaussianKernel(rows, 400)
kernel = kernel_y * kernel_x.T

filter = 255 * kernel / np.linalg.norm(kernel)

vintage_im = np.copy(input)

# for each channel in the input image, we will apply the above filter
for i in range(3):
    vintage_im[:, :, i] = vintage_im[:, :, i] * filter


array = np.array(vintage_im)

seppiaMatrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]
                             ])
filter = cv2.transform(array, seppiaMatrix)
# Check wich entries have a value greather than 255 and set it to 255
filter[np.where(filter > 255)] = 255
output_pil: Image
output_pil = Image.fromarray(filter)
output_np = np.array(output_pil)
output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

### applica sherpening
Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
output_sherpen = cv2.filter2D(output_cv, -1, Kernel)

## applica maschera scratch
mask = cv2.imread('foto/texture-2.jpeg')
#image = cv2.addWeighted(output_sherpen, 0.5, mask, 0.5, 0)
mask_resized = cv2.resize(mask, (output_sherpen.shape[1], output_sherpen.shape[0]))
dst = cv2.addWeighted(output_sherpen, 0.7, mask_resized, 0.3, 0)

cv2.imshow('stile retrò', dst)
cv2.waitKey(0)