import cv2 as cv

input = cv.imread("foto/mele.jpg")

## applica maschera scratch
mask = cv.imread('foto/texture-4.jpg')
mask_resized = cv.resize(mask, (input.shape[1], input.shape[0]))
dst = cv.addWeighted(input, 0.7, mask_resized, 0.3, 0)

cv.imshow('stile retrò', dst)
cv.waitKey(0)
cv.destroyAllWindows()