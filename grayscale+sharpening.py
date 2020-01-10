import cv2
import numpy as np

input = cv2.imread("foto/mele.jpg")

output_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

## shrapening
Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])

output_sharpen = cv2.filter2D(output_gray, -1, Kernel)

cv2.namedWindow('grayscale', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('grayscale', 600,600)
output_size = cv2.resize(output_sharpen, (1080, 1350))
cv2.imshow('grayscale', output_size)
cv2.waitKey(0)
cv2.destroyAllWindows()