import cv2
import numpy as np
from PIL import Image

# read image
input = cv2.imread('foto-input/foto-3.jpg')

# Apply Seppia matrix
array = np.array(input)
seppiaMatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
filter = cv2.transform(array, seppiaMatrix)
# Check wich entries have a value greather than 255 and set it to 255
filter[np.where(filter > 255)] = 255

# Create an image from the array
output: Image
output = Image.fromarray(filter)

#conversion from Pil to cv
output_np = np.array(output)
output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

# add texture
mask = cv2.imread('Texture/blu-texture.jpg')
mask_resized = cv2.resize(mask, (output_cv.shape[1], output_cv.shape[0]))
output = cv2.addWeighted(output_cv, 0.7, mask_resized, 0.1, 0)

cv2.imshow('Classic seppia', output)
cv2.waitKey(0)
cv2.imwrite("foto-output/classic-seppia.jpg",output)
cv2.destroyAllWindows()
