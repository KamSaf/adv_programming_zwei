import cv2

image = cv2.imread("../images/joe.jpg")
roi = image[100:301, 100:301]
cv2.imwrite("../images/cropped_image.jpg", roi)
