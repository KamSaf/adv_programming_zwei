import cv2
import imutils
import numpy as np


image = cv2.imread("../images/brick.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
for i, c in enumerate(cnts):
    c = (c.astype("float32") * ratio).astype("int32")
    x, y, w, h = cv2.boundingRect(c)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        img=image,
        text=f"{w}x{h} px",
        org=(int(x + w / 2), int(y + h / 2)),
        fontFace=2,
        fontScale=0.5,
        color=(0, 0, 255),
    )
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
