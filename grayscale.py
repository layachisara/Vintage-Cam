import cv2

input = cv2.imread("foto/mele.jpg")

output = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('grayscale', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('grayscale', 600,600)
output_size = cv2.resize(output, (1080, 1350))
cv2.imshow('grayscale', output_size)
cv2.waitKey(0)
cv2.destroyAllWindows()
