import cv2

image = cv2.imread("../images/bad_guy_staring.jpg")
radius_1 = 1
radius_2 = 345
cv2.circle(image, (245, 375), radius_1, (0, 0, 255), 90)
cv2.circle(image, (425, 365), radius_1, (0, 0, 255), 90)
cv2.rectangle(image, (260, 560), (420, 580), (0, 255, 0), 50)
cv2.circle(image, (330, 400), radius_2, (255, 0, 0), 3)

cv2.imshow("wie bitte", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
