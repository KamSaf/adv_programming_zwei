import imutils
import cv2

image = cv2.imread("../images/joe.jpg")
rotated = imutils.rotate(image, 75)
cv2.imwrite("../images/rotated_output.jpg", rotated)
cv2.imshow("Joe Rotated by 75 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
