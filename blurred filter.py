import cv2
import numpy as np

# Reading our image and displaying it
image = cv2.imread('foto/ragazzo-fiori.jpg')

#cv2.namedWindow('Original Image', cv2.WINDOW_AUTOSIZE)
#cv2.imshow('Original Image', image)
#cv2.waitKey(0)

# Creating our 3 x 3 kernel that would look like this:
# [[ 0.11111111  0.11111111  0.11111111]
#  [ 0.11111111  0.11111111  0.11111111]
#  [ 0.11111111  0.11111111  0.11111111]]
#kernel_3x3 = np.ones((3, 3), np.float32) / 9
# We apply the filter and display the image
#blurred = cv2.filter2D(image, -1, kernel_3x3)

#cv2.namedWindow('3x3 Kernel Blurring', cv2.WINDOW_AUTOSIZE)
#cv2.imshow('3x3 Kernel Blurring', blurred)
#cv2.waitKey(0)

# Let's try with 7 x 7 kernel to get a more blurred image
kernel_7x7 = np.ones((10, 10), np.float32) / 100
blurred2 = cv2.filter2D(image, -1, kernel_7x7)

cv2.namedWindow('7x7 Kernel Blurring', cv2.WINDOW_AUTOSIZE)
cv2.imshow('7x7 Kernel Blurring', blurred2)

cv2.waitKey(0)
cv2.destroyAllWindows()