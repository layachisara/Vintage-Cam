import cv2
import numpy as np

image = cv2.imread('Foto/JukeBox.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

kernel_7x7 = np.ones((7, 7), np.float32) / 49
blurred = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()