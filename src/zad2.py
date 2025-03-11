import numpy as np
import cv2

canvas_size = (400, 400)

canvas = np.zeros((canvas_size[0], canvas_size[1], 3), dtype="uint8")

cv2.rectangle(canvas, (0, 0), (100, 50), (0, 255, 0))
cv2.rectangle(
    canvas,
    (canvas_size[0] - 100, canvas_size[1] - 50),
    (canvas_size[0], canvas_size[1]),
    (0, 0, 255),
    3,
)


cv2.imshow("Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
