import cv2

image = cv2.imread("../images/pavement.png")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for block_size in (11, 21, 31, 41):
    result = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, block_size, 10
    )
    cv2.imshow(f"Mean Adaptive Thresholding (block size {block_size})", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Przy silnych róznicach w oświetleniu najlepiej z wykrywaniem konturów radzi sobie block_size = 11
