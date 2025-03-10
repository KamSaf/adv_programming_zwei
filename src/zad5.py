import cv2

image = cv2.imread("../images/joe.jpg")
cv2.imshow("Joe 1", image)

image2 = cv2.imread("../images/joe_gray.jpg")
cv2.imshow("Joe 2", image2)

windows = [True, True]
while windows[0] or windows[1]:
    k = cv2.waitKey(0)
    if k == ord("q"):
        cv2.destroyWindow("Joe 1")
        windows[0] = False
        continue
    elif k == ord("w"):
        cv2.destroyWindow("Joe 2")
        windows[1] = False
        continue
