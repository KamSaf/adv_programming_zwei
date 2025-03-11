import cv2

image = cv2.imread("../images/joe.jpg")
(y, x) = (d // 2 for d in image.shape[:2])
cv2.line(image, (x, y), (image.shape[1], image.shape[0]), (255, 0, 0))
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
