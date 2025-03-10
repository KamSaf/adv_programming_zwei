import cv2
import sys

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

if image.shape[0] < 100:
    print("Image too small")
    sys.exit()

for i in range(image.shape[1]):
    image[99, i] = (0, 255, 0)

cv2.imshow("Changed Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
