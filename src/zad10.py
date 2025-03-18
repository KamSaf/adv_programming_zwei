import cv2


image = cv2.imread("../images/joe.jpg")
h = image.shape[0]
resized = cv2.resize(image, (800, h), interpolation=cv2.INTER_AREA)
cv2.imwrite("../images/wide_joe.jpg", resized)
