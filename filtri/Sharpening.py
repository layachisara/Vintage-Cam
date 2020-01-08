import cv2 as cv
import numpy as np

input = cv.imread("Foto/mela vintage.jpg")

Kernel = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]
                     ])
output = cv.filter2D(input, -1, Kernel)

cv.imshow('sharpening', output)
cv.waitKey(0)