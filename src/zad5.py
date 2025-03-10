import cv2

image = cv2.imread("../images/joe.jpg")
(y, x) = (d // 2 for d in image.shape[:2])
for i in range(len(image)):
    if i > y:
        break
    for j in range(len(image[i])):
        if j > x:
            continue
        image[i][j] = (255, 0, 0)

cv2.imshow("Joe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
