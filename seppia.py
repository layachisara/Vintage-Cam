
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

input = cv2.imread("foto/mele.jpg")

array = np.array(input)

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

# stampa
cv2.imshow('seppia', output_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()