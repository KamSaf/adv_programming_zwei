import cv2


image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]
resized = cv2.resize(image, (w // 5, h // 5), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Joe", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
