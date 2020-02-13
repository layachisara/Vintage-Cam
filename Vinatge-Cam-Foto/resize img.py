import cv2


W = 450.
input = cv2.imread('foto/foto-13.jpg')
height, width, depth = input.shape
imgScale = W/width
newX,newY = input.shape[1]*imgScale, input.shape[0]*imgScale
newimg = cv2.resize(input,(int(newX),int(newY)))
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite("foto resized/foto-13-v1.jpg",newimg)