import cv2

WINDOW_NAME = "Image window"
image = cv2.imread("../images/rock_alone.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow(WINDOW_NAME)


def update(val):
    block_size = cv2.getTrackbarPos("blockSize", WINDOW_NAME)
    C = cv2.getTrackbarPos("C", WINDOW_NAME) - 20
    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3
    binary = cv2.adaptiveThreshold(
        image,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=block_size,
        C=C,
    )
    cv2.imshow(WINDOW_NAME, binary)


cv2.createTrackbar("blockSize", WINDOW_NAME, 11, 51, update)
cv2.createTrackbar("C", WINDOW_NAME, 20, 40, update)
update(0)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
