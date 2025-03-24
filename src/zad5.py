import cv2

image = cv2.imread("../images/bad_guy_staring.jpg")
roi = image[65:740, 110:550]
cv2.imshow("Face", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
