import numpy as np
import cv2

image = cv2.imread("../images/bad_guy_staring.jpg")
mask = np.zeros(image.shape[:2], dtype="uint8")
ellipse = cv2.ellipse(mask, (330, 370), (120, 40), 0, 0, 360, 255, 80)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
