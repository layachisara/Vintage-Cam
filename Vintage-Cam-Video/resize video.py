import cv2 as cv
#
# def resize (frame):
#     W = 1000.
#     height, width, depth = frame.shape
#     imgScale = W/width
#     newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale
#     newFrame = cv2.resize(frame,(int(newX),int(newY)))
#     return newFrame
#
# # lettura video
# cap = cv2.VideoCapture('video/video-1.mp4')
# fps = 15
# capSize = (1028,720)
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# out = cv2.VideoWriter('video resized/video-1-v1.mp4', fourcc, fps,capSize)
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         # applica resize
#         frame = resize(frame)
#         out.write(frame)
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
#
# cap.release()
# out.release()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv.VideoCapture('video/video-2.mp4')
# Define the codec and create VideoWriter object
percent = 75
width_frame = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height_frame = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
w = int(width_frame * percent / 100)
h = int(height_frame * percent / 100)
size = (w, h)
fourcc = cv.VideoWriter_fourcc(*'m', 'p', '4', 'v')
out = cv.VideoWriter('video resized/video-2-v1.mp4', fourcc, 20.0, size)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
         out.write(frame)
         if cv.waitKey(10) & 0xFF == ord('q'):
             break
    else:
         break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()