import cv2

gray = cv2.imread("../images/image_with_noise.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original", gray)

kernel_sizes = [(1, 1), (2, 2), (3, 3)]
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernel_size[0], kernel_size[1]), opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
