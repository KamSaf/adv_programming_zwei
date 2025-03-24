import cv2

image = cv2.imread("../images/joe.jpg")
roi = image[45:100, 50:250]
image[200:255, 100:300] = roi
cv2.imshow("Patchwork", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
