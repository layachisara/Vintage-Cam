import cv2
import numpy as np

input = cv2.imread('foto/mele.jpg')
rows, cols = input.shape[:2]

borderType = cv2.BORDER_CONSTANT
#cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
border = 20
bottom = 200
#value = [randint(0, 255), randint(0, 255), randint(0, 255)]
dst = cv2.copyMakeBorder(input, border, bottom, border, border, borderType)

output = np.copy(dst)

cv2.imshow('polaroid', output)
cv2.waitKey(0)
cv2.destroyAllWindows()