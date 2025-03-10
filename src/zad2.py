import cv2

image = cv2.imread("../images/joe.jpg")
(height, width) = image.shape[:2]
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image[height - 1, width - 1] = (0, 0, 255)
cv2.imshow("Changed Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
