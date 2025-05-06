import cv2

image = cv2.imread("../images/text.png")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gauss = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 15
)
cv2.imshow("Gaussian Adaptive Thresholding", gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
