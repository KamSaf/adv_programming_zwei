import cv2

image = cv2.imread("../images/joe.jpg")
(height, width) = image.shape[:2]
(b, g, r) = image[height - 1, width - 1]
print(f"Pixel at ({width}, {height}) - Red: {r}, Green: {g}, Blue: {b}")
