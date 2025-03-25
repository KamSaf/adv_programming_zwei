import numpy as np
import cv2

# image = cv2.imread("../images/bad_guy_staring.jpg")
image = cv2.imread("../images/joe.jpg")


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, np.array((0, 0, 0)), np.array((25, 75, 265)))
# mask = cv2.inRange(hsv, np.array((0, 0, 0)), np.array((140, 255, 255)))
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("masked", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
