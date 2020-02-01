import cv2


W = 500.
input = cv2.imread('foto resized/foto-11-v1.jpg')
height, width, depth = input.shape
imgScale = W/width
newX,newY = input.shape[1]*imgScale, input.shape[0]*imgScale
newimg = cv2.resize(input,(int(newX),int(newY)))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite("foto resized/foto-11-v2.jpg",newimg)