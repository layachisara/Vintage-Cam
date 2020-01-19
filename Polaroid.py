import cv2
import numpy as np

input = cv2.imread('foto/colazione.jpg')
blur = cv2.GaussianBlur(input,(5,5),cv2.BORDER_DEFAULT)

red_img  = np.full((682, 512, 3), (0, 0, 220), np.uint8)
mask_resized = cv2.resize(red_img, (input.shape[1], input.shape[0]))

fused_img  = cv2.addWeighted(input, 0.8, mask_resized, 0.2, 0)
WHITE = [255, 255, 255]
black_border_img = cv2.copyMakeBorder(fused_img, 60,60,20,20, cv2.BORDER_CONSTANT, value=WHITE)




