import numpy as np
import cv2


image = cv2.imread("../images/joe.jpg")

M = np.ones(image.shape, dtype="uint8") * 50
opencv_lighter = cv2.add(image, M)

cv2.imshow("Lighter Joe (opencv)", opencv_lighter)
numpy_lighter = image + M
cv2.imshow("Lighter Joe (numpy)", numpy_lighter)
cv2.waitKey(0)
cv2.destroyAllWindows()
