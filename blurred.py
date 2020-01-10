import cv2
import numpy as np

input = cv2.imread('foto/mele.jpg')

cv2.imshow('input', input)
cv2.waitKey(0)

kernel_7x7 = np.ones((7, 7), np.float32) / 49
output = cv2.filter2D(input, -1, kernel_7x7)

cv2.imshow('7x7 Kernel Blurring', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Per mostrarle una accanto all'altra
#plt.subplot(121), plt.imshow(img), plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(median), plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
#plt.show()