import cv2

image = cv2.imread("../images/joe.jpg")
(y, x) = (d // 2 for d in image.shape[:2])
x_range = (x - 50, x + 50)
y_range = (y - 50, y + 50)
for i in range(y_range[0], y_range[1]):
    for j in range(x_range[0], x_range[1]):
        image[i][j] = (0, 0, 255)


cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
