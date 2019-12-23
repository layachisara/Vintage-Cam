
import cv2
from matplotlib import pyplot as plt
import numpy as np

im_BGR = cv2.imread("foto/ragazzo-fiori.jpg")
im_BGR = cv2.cvtColor(im_BGR, cv2.COLOR_BGR2GRAY)
plt.imshow(im_BGR, cmap='Greys_r')
plt.show()

# im_BGR = cv2.imread("foto/man-and-woman-with-a-child.jpg")
# im_BGR = cv2.cvtColor(im_BGR, cv2.COLOR_BGR2GRAY)
# plt.imshow(im_BGR, cmap='Greys_r')
# plt.show()

# path = "foto/portrait-of-woman-wearing-black-blouse.jpg"
# img_gray_mode = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# plt.imshow(img_gray_mode, cmap='Greys_r')
# plt.show()
