import cv2
import sys

image = cv2.imread("../images/joe.jpg")

try:
    (x, y) = [int(input(f"Enter {c} value: ")) for c in ("X", "Y")]
except Exception:
    print("Invalid data entered")
    sys.exit()

if x < 0 or y < 0:
    print("X and Y coordinates cannot be negative values")
    sys.exit()

(height, width) = image.shape[:2]
if x > height:
    print("Given Y coordinate is too big")
    sys.exit()
elif y > width:
    print("Given X coordinate is too big")
    sys.exit()


image[y - 1, x - 1] = (0, 0, 0)
