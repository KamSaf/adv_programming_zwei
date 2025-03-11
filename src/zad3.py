import numpy as np
import cv2

canvas_size = (300, 300)
radius = 40
radius_2 = 60

canvas = np.zeros((canvas_size[0], canvas_size[1], 3), dtype="uint8")
cv2.circle(canvas, (radius, radius), radius, (255, 0, 0))
cv2.circle(
    canvas,
    (canvas_size[0] - radius_2, canvas_size[1] - radius_2),
    radius_2,
    (0, 0, 255),
)

cv2.imshow("Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
