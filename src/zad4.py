import cv2

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
cv2.imshow("Original Joe", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Joe Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Joe Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Joe Flipped Horizontally & Vertically", flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()
