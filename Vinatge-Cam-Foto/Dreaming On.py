import cv2

# read image
input = cv2.imread('foto-input/foto-6.jpg')

# add texture
mask = cv2.imread('Texture/texture-dream.jpg')
mask_resized = cv2.resize(mask, (input.shape[1], input.shape[0]))
output1 = cv2.addWeighted(input, 0.7, mask_resized, 0.6, 0)
# mask1 = cv2.imread('Texture/texture-2.jpeg')
# mask_resized1 = cv2.resize(mask1, (dst.shape[1], dst.shape[0]))
# dst1 = cv2.addWeighted(dst, 0.7, mask_resized1, 0.1, 0)

# add texture
mask = cv2.imread('Texture/blu-texture.jpg')
mask_resized = cv2.resize(mask, (output1.shape[1], output1.shape[0]))
output2 = cv2.addWeighted(output1, 0.7, mask_resized, 0.2, 0)

cv2.imshow('Dreaming On', output2)
cv2.waitKey(0)
cv2.imwrite("foto-output/dreaming-on.jpg",output2)
cv2.destroyAllWindows()