import cv2

image_gray = cv2.imread("../images/joe.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("../images/joe_gray.jpg", image_gray)
