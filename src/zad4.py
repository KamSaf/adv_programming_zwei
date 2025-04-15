import cv2


gray = cv2.imread("../images/license_plate.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

for kernel in [(7, 7), (10, 10), (20, 20)]:
    blur = cv2.blur(gray, kernel)
    cv2.imshow("Blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for kernel in [(3, 3), (9, 9), (15, 15)]:
    gaussian_blur = cv2.GaussianBlur(gray, kernel, 0)
    cv2.imshow("Gaussian blur", gaussian_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for k in (3, 9, 15):
    median_blur = cv2.medianBlur(gray, k)
    cv2.imshow("Median blur", median_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for diameter, sigmaColor, sigmaSpace in [(11, 21, 7), (11, 41, 21), (11, 61, 39)]:
    b_blur = cv2.bilateralFilter(gray, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("Bilateral filter", b_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# najmocniej rozmywa cv2.blur, najbardziej czytelny jest przy cv2.medianBlur i cv2.bilateralFilter,
# ale cv2.medianBlur lepiej wygladza szumy
