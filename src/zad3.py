import cv2
import numpy as np

image = cv2.imread("../images/nissan.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("og image", image)
cv2.imshow("blue color mask", mask)
cv2.imshow("blue color segmentation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
