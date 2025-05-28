import cv2

image = cv2.imread("../images/jeep.jpg")
for name, chan in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
for name, chan in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
