import cv2
import sys

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

if image.shape[0] < 100 or image.shape[1] < 100:
    print("Image too small")
    sys.exit()


x_range = (50, 100)
y_range = (50, 100)
for i in range(y_range[0], y_range[1]):
    for j in range(x_range[0], x_range[1]):
        image[i][j] = (255, 255, 255)


cv2.imshow("Changed Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
