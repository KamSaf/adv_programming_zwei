import imutils
import cv2

image = cv2.imread("../images/joe.jpg")
rotated = imutils.rotate(image, 60)
cv2.imshow("Joe Rotated by 60 Degrees (imutils)", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_2 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Joe Rotated by 30 Degrees (warpAffine)", rotated_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
