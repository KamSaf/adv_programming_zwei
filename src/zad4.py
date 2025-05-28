import cv2


image = cv2.imread("../images/jeep.jpg")
h, w = image.shape[:2]
resized = cv2.resize(image, (w // 5, h // 5), interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
channels = list(cv2.split(hsv))
channels[0] = cv2.add(channels[1], 30)

altered_image = cv2.merge(channels)
cv2.imshow("altered_image", altered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
