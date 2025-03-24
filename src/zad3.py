import numpy as np
import cv2


image = cv2.imread("../images/joe.jpg")

M = np.ones(image.shape, dtype="uint8") * 80
opencv_darker = cv2.subtract(image, M)

cv2.imshow("Darker Joe (opencv)", opencv_darker)
numpy_darker = image - M
cv2.imshow("Darker Joe (numpy)", numpy_darker)
cv2.waitKey(0)
cv2.destroyAllWindows()
