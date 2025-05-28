import cv2


image = cv2.imread("../images/jeep.jpg")
h, w = image.shape[:2]
resized = cv2.resize(image, (w // 5, h // 5), interpolation=cv2.INTER_AREA)
cv2.imshow("original image", resized)
hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
for val in (-30, 30):
    channels = list(cv2.split(hsv))
    channels[1] = cv2.add(channels[1], val)
    altered_image = cv2.merge(channels)
    cv2.imshow(f"altered image (val: {val})", altered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
