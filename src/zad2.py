import numpy as np
import cv2

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
# M = np.float32([[1, 0, -20], [0, 1, -50]])
M = np.array([[1, 0, -20], [0, 1, -50]], dtype=np.float32)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Joe", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
