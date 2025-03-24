import cv2

image = cv2.imread("../images/joe.jpg")
roi = image[0:-1, len(image[0]) // 2 : -1]
cv2.imshow("Joe Right Half", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
