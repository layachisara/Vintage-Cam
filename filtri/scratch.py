import cv2
import numpy as np

input = cv2.imread('Foto/colazione.jpg')
height, width, depth = input.shape
mask = cv2.imread('Foto/struttura.jpg')
mask = np.zeros((height, width), np.uint8)
cv2.circle(mask, (int(width/2), int(height/2)), 280, 1, thickness=-1)
output = cv2.bitwise_and(input, input, mask=mask)

cv2.imshow('scratch', output)
cv2.waitKey(0)
cv2.destroyAllWindows()