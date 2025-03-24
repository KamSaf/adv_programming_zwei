import cv2
import numpy as np

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
flipped_half = cv2.flip(image[0 : len(image), len(image[0]) // 2 :], 0)
left_half = image[: len(image), : len(image[0]) // 2]
flipped = np.concatenate((left_half, flipped_half), axis=1)
cv2.imshow("Joe Halfly Flipped", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
