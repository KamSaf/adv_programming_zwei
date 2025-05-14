import cv2
import imutils

NEW_WIDTH = 300.0
image = cv2.imread("../images/brick.png")
h, w = image.shape[:2]
ratio = w / NEW_WIDTH
resized = imutils.resize(image, width=int(NEW_WIDTH), height=int(h * ratio))
for t in (100, 140, 180):
    thresh = cv2.threshold(resized, t, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)
