import cv2
import imutils

image = cv2.imread("../images/joe.jpg")
shifted = imutils.translate(image, 50, 100)
cv2.imshow("Shifted Joe", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
