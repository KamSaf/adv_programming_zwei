import numpy as np
import cv2

image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]
# M = np.float32([[1, 0, w // 2 + 50], [0, 1, h // 2 + 50]])
M = np.array([[1, 0, w // 2 + 50], [0, 1, h // 2 + 50]], dtype=np.float32)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Joe", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
