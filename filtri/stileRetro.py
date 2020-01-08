import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from random import randint

input = cv2.imread('Foto/mela vintage.jpg')
rows, cols = input.shape[:2]



borderType = cv2.BORDER_REFLECT_101
#cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
border = 20
bottom = 200
#value = [randint(0, 255), randint(0, 255), randint(0, 255)]
dst = cv2.copyMakeBorder(input, border, bottom, border, border, borderType)

vintage_im = np.copy(dst)

cv2.imshow('retro', vintage_im)
cv2.waitKey(0)
cv2.destroyAllWindows()


