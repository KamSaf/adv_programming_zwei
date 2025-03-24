import cv2

image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]

start_x = 0
stop_x = 200
while stop_x < w:
    # frame = image[start_x:stop_x, 0:h]
    frame = image[0:h, start_x:stop_x]
    cv2.imshow("Frame", frame)
    # cv2.waitKey(5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    start_x += 10
    stop_x += 10
