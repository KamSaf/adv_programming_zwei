import numpy as np
import cv2


image = cv2.imread("../images/joe.jpg")
M = np.ones(image.shape, dtype="uint8") * [10, -20, 30]
filtered = cv2.add(image, M, dtype=cv2.CV_8U)

cv2.imshow("Insta Joe", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
