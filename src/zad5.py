import cv2


gray = cv2.imread("../images/bad_guy_staring.jpg", cv2.IMREAD_GRAYSCALE)
kernel_size = (6, 6)
cv2.imshow("Original", gray)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
cv2.imshow(f"Closing: {kernel_size}", closing)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
cv2.imshow(f"Opening: {kernel_size}", opening)
ITERATIONS = 5
diluted = cv2.dilate(opening, kernel, iterations=ITERATIONS)
cv2.imshow(f"Dilution: iterations - {ITERATIONS}", diluted)

cv2.waitKey(0)
cv2.destroyAllWindows()
