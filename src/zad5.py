import cv2
import numpy as np

image = cv2.imread("../images/green_image.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 100, 50])
upper_green = np.array([80, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("og image", image)
cv2.imshow("green mask", mask)
cv2.imshow("green color segmentation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
