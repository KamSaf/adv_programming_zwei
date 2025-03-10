import cv2

image = cv2.imread("../images/joe.jpg")
h, w, c = image.shape[:3]
print(f"channels: {c}")
