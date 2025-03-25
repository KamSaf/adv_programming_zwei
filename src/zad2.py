import cv2

image_1 = cv2.imread("../images/frame_1.png")
image_2 = cv2.imread("../images/frame_2.png")

diff = cv2.bitwise_xor(image_1, image_2)
cv2.imshow("XOR", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
