import numpy as np
import cv2

# PATH = "../images/opencv_logo.png"
PATH = "../images/joe.jpg"

image = cv2.imread(PATH)
cv2.imshow("Original Joe", image)
B, G, R = cv2.split(image)
R = cv2.add(R, np.array([150]))
merged = cv2.merge([B, G, R])
cv2.imshow("Funny Joe", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
