import cv2

image = cv2.imread("../images/pavement.png")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for c in (2, 5, 10, 15):
    mean = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, c
    )
    gauss = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, c
    )
    cv2.imshow(f"Mean Adaptive Thresholding (c {c})", mean)
    cv2.imshow(f"Gaussian Adaptive Thresholding (c {c})", gauss)


cv2.waitKey(0)
cv2.destroyAllWindows()

# Najlepiej radzi sobie gaussian przy c = 15
