import cv2

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
flipped = cv2.flip(image, -1)
cv2.imshow("Joe Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
