import cv2
import numpy as np
from PIL import Image

# read image
input = cv2.imread('foto-input/foto-5.jpg')
# apply seppia filter
array = np.array(input)
seppiaMatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168],[0.272, 0.534, 0.131]])
filter = cv2.transform(array, seppiaMatrix)
# Check wich entries have a value greather than 255 and set it to 255
filter[np.where(filter > 255)] = 255
output_pil: Image
output_pil = Image.fromarray(filter)
output_np = np.array(output_pil)
output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

# apply sherpening
Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
output_sherpen = cv2.filter2D(output_cv, -1, Kernel)

# print output
cv2.imshow('Stile Retro', output_sherpen)
cv2.waitKey(0)
cv2.imwrite("foto-output/stile-retro.jpg",output_sherpen)
cv2.destroyAllWindows()