import numpy as np
import cv2

canvas_size = (300, 300)
rect = (100, 100)
radius = 30
(center_y, center_x) = (d // 2 for d in canvas_size)

rect_coord = tuple(
    map(
        lambda x: (int(x[0]), int(x[1])),
        (
            (center_x - rect[0] / 2, center_y - rect[1] / 2),
            (center_x + rect[0] / 2, center_y + rect[1] / 2),
        ),
    )
)

canvas = np.zeros((canvas_size[0], canvas_size[1], 3), dtype="uint8")
cv2.circle(canvas, (center_x, center_y), radius, (0, 255, 0))
cv2.rectangle(
    canvas,
    rect_coord[0],
    rect_coord[1],
    (0, 255, 0),
)


cv2.imshow("Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
