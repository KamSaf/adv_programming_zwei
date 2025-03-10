import cv2

image = cv2.imread("../images/joe.jpg")
(y, x) = (d // 2 for d in image.shape[:2])
(b, g, r) = image[y - 1, x - 1]
print(f"Pixel at ({x}, {y}) - Red: {r}, Green: {g}, Blue: {b}")
