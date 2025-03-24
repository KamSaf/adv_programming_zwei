import cv2

image = cv2.imread("../images/joe.jpg")
roi = image[0:101, 0:101]
cv2.imshow("Joe ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
