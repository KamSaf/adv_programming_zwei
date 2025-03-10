import cv2

image_gray = cv2.imread("../images/joe.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray image", image_gray)
print(f"channels: {image_gray.shape}")
cv2.waitKey(0)
cv2.destroyAllWindows()
