import cv2

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Joe Rotated by -90 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
