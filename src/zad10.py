import cv2
import sys
import numpy as np

image = cv2.imread("../images/joe.jpg")

if image.shape[0] < 200 or image.shape[1] < 200:
    print("Image too small")
    sys.exit()

points = ((50, 50), (200, 200))
points_values = (image[points[0][0], points[0][1]], image[points[1][0], points[1][1]])

for index, p in enumerate(points_values):
    print(
        f"Pixel at ({points[index][0]}, {points[index][1]}) - Red: {p[2]}, Green: {p[1]}, Blue: {p[0]}\n"
    )

output = "{} - {}: R: {}, G: {}, B: {}\n"

point_1 = points_values[0]
point_2 = points_values[1]


def diff(coor_1, coor_2, point_1, point_2):
    print(
        output.format(
            coor_1,
            coor_2,
            np.int64(point_1[2]) - np.int64(point_2[2]),
            np.int64(point_1[1]) - np.int64(point_2[1]),
            np.int64(point_1[0]) - np.int64(point_2[0]),
        )
    )


diff(points[0], points[1], point_1, point_2)
diff(points[1], points[0], point_2, point_1)
