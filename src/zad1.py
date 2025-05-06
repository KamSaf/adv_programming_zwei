import cv2

image = cv2.imread("../images/pavement.png")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
thresh_mean = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10
)
cv2.imshow("Mean Adaptive Thresholding", thresh_mean)
thresh_gaussian = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10
)
cv2.imshow("Gaussian Adaptive Thresholding", thresh_gaussian)
(T, thresh_inv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresh_inv)

(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))


cv2.waitKey(0)
cv2.destroyAllWindows()
