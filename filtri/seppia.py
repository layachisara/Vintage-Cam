import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

output: Image
input = cv2.imread("Foto/mela vintage.jpg")

array = np.array(input)

seppiaMatrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]
                             ])
filter = cv2.transform(array, seppiaMatrix)
# Check wich entries have a value greather than 255 and set it to 255
filter[np.where(filter > 255)] = 255
output: Image
output = Image.fromarray(filter)
# Create an image from the array
plt.imshow(output)
plt.show()