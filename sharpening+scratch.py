import cv2
import numpy as np

input = cv2.imread("foto/mele.jpg")

Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])

output = cv2.filter2D(input, -1, Kernel)

## applica maschera scratch
mask = cv2.imread('foto/texture-4.jpg')
#image = cv2.addWeighted(output_sherpen, 0.5, mask, 0.5, 0)
mask_resized = cv2.resize(mask, (output.shape[1], output.shape[0]))
dst = cv2.addWeighted(output, 0.7, mask_resized, 0.3, 0)

cv2.imshow('stile retrò', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()