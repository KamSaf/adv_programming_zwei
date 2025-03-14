import imutils
import cv2

image = cv2.imread("../images/joe.jpg")
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Joe Rotated by -33 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
