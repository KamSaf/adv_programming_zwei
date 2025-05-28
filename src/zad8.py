import cv2
import numpy as np

image = cv2.imread("../images/dude.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 80, 50])
upper_green = np.array([80, 255, 255])

lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
merged_mask = cv2.bitwise_or(mask_green, mask_blue)

result = cv2.bitwise_and(image, image, mask=merged_mask)

cv2.imshow("og image", image)
cv2.imshow("mask", merged_mask)
cv2.imshow("image with mask applied", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
