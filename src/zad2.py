import cv2


gray = cv2.imread("../images/image_with_noise.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

for kernel in [(x, x) for x in range(1, 15)]:
    blur = cv2.blur(gray, kernel)
    cv2.imshow(f"Blur kernel - {kernel}", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for kernel in [(3, 3), (9, 9), (15, 15)]:
    gaussian_blur = cv2.GaussianBlur(gray, kernel, 0)
    cv2.imshow(f"Gaussian blur kernel - {kernel}", gaussian_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for k in (3, 9, 15):
    median_blur = cv2.medianBlur(gray, k)
    cv2.imshow(f"Median blur kernel - {k}", median_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for diameter, sigmaColor, sigmaSpace in [(11, 21, 7), (11, 41, 21), (11, 61, 39)]:
    b_blur = cv2.bilateralFilter(gray, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(
        f"Bilateral filter kernel - ({diameter, sigmaColor, sigmaSpace})", b_blur
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Wraz z wzrostem wielkości kernela wzrasta rozmycie obrazu
# Optymalny rozmiar kernela:
#   - cv2.blur - 5
#   - cv2.GaussianBlur - (9, 9)
#   - cv2.medianBlur - 3
#   - cv2.bilateralFilter - (11, 41, 21)
