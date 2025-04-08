import cv2


gray = cv2.imread("../images/license_plate.jpg", cv2.IMREAD_GRAYSCALE)
kernel_size = (15, 15)
cv2.imshow("Original", gray)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
cv2.imshow(f"Closing: {kernel_size}", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
