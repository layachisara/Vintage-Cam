import cv2
import numpy as np

input = cv2.imread("foto-input/foto-1.jpg")

# gray filter
output_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

# shrapening filter
Kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
output_sharpen = cv2.filter2D(output_gray, -1, Kernel)

cv2.imshow('Dirty Gray', output_sharpen)
cv2.waitKey(0)
cv2.imwrite("foto-output/dirty-gray.jpg",output_sharpen)
cv2.destroyAllWindows()