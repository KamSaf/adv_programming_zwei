import cv2


gray = cv2.imread("../images/dashed_line.jpg", cv2.IMREAD_GRAYSCALE)
kernel_sizes = [(x, x) for x in range(1, 10)]
cv2.imshow("Original", gray)
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernel_size[0], kernel_size[1]), closing)
    cv2.waitKey(0)
cv2.destroyAllWindows()
