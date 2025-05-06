import cv2

image = cv2.imread("../images/rock_alone.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, blockSize=3, C=41
)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (51, 51))
clean_mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
foreground = cv2.bitwise_and(image, image, mask=clean_mask)
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated_foreground = cv2.dilate(foreground, kernel=dilate_kernel, iterations=80)

blurred_foreground = cv2.GaussianBlur(dilated_foreground, (9, 9), 1)
_, binary_foreground = cv2.threshold(
    cv2.cvtColor(blurred_foreground, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY
)
foreground_mask = cv2.bitwise_not(binary_foreground)
result = cv2.bitwise_and(image, image, mask=foreground_mask)

cv2.imshow("Original", image)
cv2.imshow("Mask", foreground_mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
