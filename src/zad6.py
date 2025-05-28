import cv2
import numpy as np

image = cv2.imread("../images/dude.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_skin = np.array([0, 30, 60])
upper_skin = np.array([20, 150, 255])


mask = cv2.inRange(hsv, lower_skin, upper_skin)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("og image", image)
cv2.imshow("skin mask", mask)
cv2.imshow("skin color segmentation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
