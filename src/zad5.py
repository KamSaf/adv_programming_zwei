import cv2
import imutils

image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
r = 500.0 / w
dim = (500, int(h * r))
resized = imutils.resize(image, dim[0], dim[1])
cv2.imshow("Resized Joe", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
