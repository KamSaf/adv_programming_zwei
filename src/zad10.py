import imutils
import cv2

image = cv2.imread("../images/joe.jpg")
angle = 0

while angle < 360:
    image = imutils.rotate(image, 15)
    cv2.imshow("Joe Rotated", image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    angle += 15
