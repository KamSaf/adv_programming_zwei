import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
(center_x, center_y) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for i in range(0, 280, 20):
    cv2.rectangle(
        canvas,
        (center_x - i // 2, center_y - i // 2),
        (center_x + i // 2, center_y + i // 2),
        (255, 255, 255),
    )

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
