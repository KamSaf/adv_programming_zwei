import cv2
import imutils
import numpy as np

WIDTHS = (200, 300, 400, 500, 600, 700, 800, 900, 1000)

for width in WIDTHS:
    image = cv2.imread("../images/brick.png")
    resized = imutils.resize(image, width=width)
    ratio = image.shape[0] / float(resized.shape[0])
    resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts)
    for i, c in enumerate(cnts):
        c = (c.astype("float32") * ratio).astype("int32")
        contours = c.reshape((-1, 1, 2)).astype(np.int32)
        x, y, w, h = cv2.boundingRect(c)
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, contours, -1, 255, -1)
        segmented_brick = cv2.bitwise_and(image, image, mask=mask)
        roi = segmented_brick[y : y + h, x : x + w]
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
