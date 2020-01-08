import cv2
import numpy as np

img1 = cv2.imread('Foto/struttura.jpg')

img2 = cv2.imread('Foto/cesso.jpg')

image = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('imma', image)
cv2.waitKey(0)