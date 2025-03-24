import numpy as np
import cv2


image = cv2.imread("../images/joe.jpg")

M = np.ones(image.shape, dtype="uint8") * 150
mod_image = image + M

cv2.imshow("Burnt Joe", mod_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
