import cv2
import numpy as np

image = cv2.imread("../images/bad_guy_staring.jpg")
(h, w) = image.shape[:2]
mask = np.zeros((h, w), dtype="uint8")
center_coordinates = (w // 2, h // 2)
axes_length = (w // 4, h // 3)
angle = 0
startAngle = 0
endAngle = 360

cv2.ellipse(mask, center_coordinates, axes_length, angle, startAngle, endAngle, 255, -1)

background_mask = cv2.bitwise_not(mask)
blurred = cv2.GaussianBlur(image, (21, 21), 0)
foreground = cv2.bitwise_and(image, image, mask=mask)
background = cv2.bitwise_and(blurred, blurred, mask=background_mask)
result = cv2.add(foreground, background)
cv2.imshow("Original", image)
cv2.imshow("Depth of field", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
