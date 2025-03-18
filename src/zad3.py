import cv2


image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
resized = cv2.resize(image, (200, 300), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Joe", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
