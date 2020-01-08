import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Foto/libro-spiaggia.jpg')
median = cv2.medianBlur(img, 9)
#blur = cv2.GaussianBlur(img, (9,9), 0)
#kernel = np.ones((9,9),np.float32)/81
#dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
